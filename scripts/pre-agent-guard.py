#!/usr/bin/env python3
"""PreToolUse hook for Agent calls. Blocks Agent calls that are pure string-search tasks
better served by grep/Bash. Part of the mechanical tool escalation ladder (grep→Read→Agent).

Hook: PreToolUse with matcher "Agent"
Exit codes: 0=allow, 1=error, 2=block

Design principle (Carmack): if the task description can be expressed as a regex,
it doesn't need an LLM. The pre-agent hook is the PREVENTION layer;
A session-end audit (detection layer) catches what the hook misses as a DETECTION fallback.
"""

import json, sys, re, os, argparse

# ---- Pure-search task patterns ----
# Two-step logic: (1) matches a search verb phrase → (2) no semantic verb → BLOCK
# Key: these match VERB PHRASES, not quoted strings. "search for X" → pure search.
# "search for X and analyze" → semantic verb "analyze" overrides → allow.
SEARCH_VERB_PATTERNS = [
    r"\bsearch\s+(?:for|in|through)\b",
    r"\bfind\s+(?:all\s+)?(?:files?|occurrences?|matches?|patterns?|sessions?)\b",
    r"\bcount\s+(?:how\s+many\s+)?(?:occurrences?|files?|matches?|sessions?)\b",
    r"\blist\s+(?:all\s+)?(?:files?|sessions?|directories?|matches?)\b",
    r"\bgrep\s+(?:for|pattern)\b",
    r"\blocate\s+(?:all\s+)?(?:files?|matches?)\b",
]

# ---- Safe override: semantic verbs that indicate genuine LLM need ----
# If description contains any of these stems, allow regardless of search patterns
# Conservative: when in doubt, allow (agent waste is cheaper than false block)
SEMANTIC = [
    "analyz", "understand", "review", "reason", "investigat",
    "explain", "summariz", "evaluat", "assess", "compar",
    "interpret", "determine whether", "check if", "decid",
    "design", "implement", "fix", "debug", "refactor",
    "propos", "recommend", "suggest", "research",
    "verif", "validat", "transform", "convert",
    "extract", "generat", "compos", "write",
]


def is_pure_search(text: str) -> bool:
    """Returns True if text describes a task that grep can handle."""
    if not text:
        return False
    text_lower = text.lower()
    # Safe override: semantic verbs → not pure search
    for stem in SEMANTIC:
        if stem in text_lower:
            return False
    # Check search patterns
    for pat in SEARCH_VERB_PATTERNS:
        if re.search(pat, text_lower):
            return True
    return False


def _suggest_grep(prompt: str) -> str:
    """Generate a grep suggestion for the blocked description."""
    ext = "jsonl"
    for candidate in ["jsonl", "md", "py", "js", "ts", "json", "yml", "yaml", "txt"]:
        if f".{candidate}" in prompt:
            ext = candidate
            break
    return f"cd <dir> && grep -r 'pattern' *.{ext}"


def process_input(raw: str) -> dict:
    """Process hook stdin input. Returns result dict with keys: allowed, reason, suggestion."""
    if not raw or not raw.strip():
        return {"allowed": True, "reason": "empty input"}

    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, TypeError) as e:
        return {"allowed": True, "reason": f"json parse error: {e}", "error": True}

    tool_name = data.get("tool_name", "")
    if tool_name != "Agent":
        return {"allowed": True, "reason": f"not an Agent call (got {tool_name})"}

    tool_input = data.get("tool_input", {})
    if not isinstance(tool_input, dict):
        return {"allowed": True, "reason": "tool_input is not a dict", "error": True}

    description = tool_input.get("description", "")
    prompt = tool_input.get("prompt", "")

    # Check both description and prompt (first 300 chars of prompt)
    text_to_check = f"{description} {prompt[:300]}"

    if is_pure_search(text_to_check):
        return {
            "allowed": False,
            "reason": "pure search - use grep/Bash instead",
            "description": description[:100],
            "suggestion": _suggest_grep(prompt),
        }

    return {"allowed": True, "reason": "not a pure search"}


def main():
    parser = argparse.ArgumentParser(
        description="PreToolUse hook: block Agent calls that are pure string-search tasks.",
        epilog="""
Exit codes:
  0 - allow (not a pure search, or semantic override)
  1 - hook error (stdin read failure, invalid JSON, unexpected state)
  2 - block (pure search detected, use grep instead)

Examples:
  echo '{"tool_name":"Agent","tool_input":{"description":"search for TODOs"}}' | python pre-agent-guard.py
  echo '{"tool_name":"Agent","tool_input":{"description":"search for TODOs"}}' | python pre-agent-guard.py --json
  python pre-agent-guard.py --help
        """.strip(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON instead of human-readable text.",
    )
    args = parser.parse_args()

    # Read hook input from stdin
    try:
        raw = sys.stdin.read()
    except OSError as e:
        if args.json:
            json.dump({"allowed": True, "warning": f"stdin read failed: {e}"}, sys.stdout)
        sys.exit(1)

    result = process_input(raw)

    if args.json:
        json.dump(result, sys.stdout, indent=2)
        sys.stdout.write("\n")
    elif not result["allowed"]:
        print(
            f"[AGENT-GUARD] BLOCKED: {result.get('reason', 'pure search')}\n"
            f"  description: {result.get('description', '')}\n"
            f"  suggestion: {result.get('suggestion', '')}",
            file=sys.stderr,
        )

    if result.get("error"):
        sys.exit(1)
    elif not result["allowed"]:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
