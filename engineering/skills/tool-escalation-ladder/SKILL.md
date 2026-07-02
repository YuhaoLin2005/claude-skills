---
name: "tool-escalation-ladder"
description: "Enforce grep→Read→Agent tool escalation order. Blocks Agent calls for pure-search tasks (find files, count occurrences, list matches) before they waste tokens. Use when you catch yourself or your agent reaching for Agent to search, find, or count — or when session cost logs show Agent calls that grep could have handled."
---

# Tool Escalation Ladder

> **TL;DR:** If it can be expressed as a regex, it doesn't need an LLM. grep finds strings. Read confirms context. Agent reasons. Use them in that order — enforced by a pre-agent hook that blocks search-verb Agent calls before they burn tokens.

**Triggers:** "search for X in the codebase" | "find all files that..." | "count occurrences of..." | "list all sessions where..." | "grep for pattern Y" (as an Agent description) | any Agent call whose description starts with a search verb without a reasoning verb

## Problem

Claude Code agents default to spawning sub-agents for exploration tasks — "search for X across the project", "find all files containing Y", "count how many times Z is called." These tasks cost 5-20k tokens per Agent call but can be solved deterministically with grep in near-zero tokens. A single misrouted "search for error handling patterns" Agent call on a large repository can burn 200k+ tokens scanning files that grep could process in milliseconds.

The root cause isn't laziness — it's that **Agent is the default tool** for "I need to look at something." When the model doesn't have a mechanical reminder, it reaches for the most general tool rather than the cheapest sufficient one. This skill installs that mechanical reminder: a pre-agent hook that blocks pure-search Agent calls before they execute, plus a quality-gate audit that catches what the hook misses.

## The Carmack Principle

> **John Carmack's engineering philosophy:** "Measure before you optimize" — performance is craft, not afterthought. **Applied here:** if the task description can be expressed as a regex, it doesn't need an LLM.

The first sentence is Carmack's documented principle. The second sentence is this skill's operational reframing — converting a performance philosophy into a concrete tool-selection rule. The reframing works because regex-expressibility is a clean proxy for "no reasoning required": if you can describe what you're looking for as a pattern, grep can find it deterministically.

This isn't a soft guideline. It's a hard rule enforced by `scripts/pre-agent-guard.py` — a PreToolUse hook that intercepts Agent calls, checks the description against search-verb patterns, and blocks pure-search calls with exit code 2. The hook prints a suggestion with the equivalent grep command, so the agent learns the correct tool over repeated sessions.

> **Script dependency:** `scripts/pre-agent-guard.py` must be installed alongside this skill. Without it, the skill provides guidance only — the mechanical enforcement layer won't function. The script requires `--help` and `--json` flags and uses exit codes 0 (allow), 1 (error), 2 (block) per project conventions.

## The Three Tiers

| Tier | Tool | What it does | Token cost | When to use |
|------|------|-------------|------------|-------------|
| **1** | `grep`, `head`, `ls`, `find`, `wc` | Pattern matching, listing, counting, existence checks | Near-zero (no LLM involvement) | The answer is a set of file paths, line matches, or counts |
| **2** | `Read` | Read specific files for content and context | Low (file content only, no reasoning overhead) | You know which file to read and need to see its contents |
| **3** | `Agent` | Reasoning, analysis, synthesis, judgment | High (full context window + reasoning) | The task requires understanding *why* or *whether*, not just *where* or *how many* |

**The rule:** Start at Tier 1. Only escalate when the lower tier provably cannot answer the question. Never skip tiers — grep before Read, Read before Agent.

## Decision Table

Ask one question before every Agent call: **"Can I express what I'm looking for as a regex or file pattern?"**

| Task | Correct tool | Wrong tool |
|------|-------------|------------|
| Find files containing "handleError" | `grep -r "handleError" --include="*.ts" .` | Agent "search for error handling in the codebase" |
| List all JSON files modified today | `find . -name "*.json" -mtime -1` | Agent "find recent JSON config files" |
| Count occurrences of `fetchUser(` | `grep -c "fetchUser(" **/*.ts` | Agent "count how many times fetchUser is called" |
| Check if a config file exists | `ls path/to/config.json` | Agent "check if the config file exists" |
| Read a known file | `Read` tool (Tier 2) | Agent "read the auth middleware" |
| Understand WHY auth is structured a certain way | Read the file → THEN Agent if needed | Agent "explain the auth flow" (without reading first) |
| Review architecture for security issues | Agent (genuine Tier 3 reasoning) | — |
| Compare two implementation approaches | Agent (genuine Tier 3 analysis) | — |

**Edge case — large result sets:** If grep returns 500+ matches, Read a representative sample first. Only escalate to Agent if you need to reason *across* the matches (pattern detection, anomaly identification) — not just to present the list.

## Safety Override: Semantic Verb Allowlist

Pure-search patterns trigger the block — but some tasks genuinely need an Agent even when they contain search verbs. The hook uses **two-step logic:**

1. **Match:** Does the description contain a search-verb phrase? (e.g., "search for", "find all files", "count how many")
2. **Override:** Does it also contain a semantic verb that indicates genuine reasoning?

**If step 2 matches → allow.** (The task requires reasoning, not just retrieval.)
**If step 1 matches but step 2 doesn't → block.** (Pure search — use grep.)

| Description | Search verb? | Semantic verb? | Verdict |
|------------|-------------|----------------|---------|
| "search for error handling and analyze the patterns" | "search for" | "analyze" | ALLOW |
| "search for all TODO comments" | "search for" | none | BLOCK → `grep -r "TODO"` |
| "find all test files and review coverage gaps" | "find all ... files" | "review" | ALLOW |
| "find all JSON config files" | "find all ... files" | none | BLOCK → `find . -name "*.json"` |
| "count how many times init() is called and check if it's consistent" | "count how many" | "check if" | ALLOW |
| "list all Python files" | "list all ... files" | none | BLOCK → `find . -name "*.py"` |

**Conservative principle:** When in doubt, allow. Agent waste is cheaper than a false block that breaks a legitimate workflow. Concretely: if the description contains ANY word not in the known search-verb patterns → allow. If you encounter a false block, add the missing semantic verb to the allowlist — do NOT disable the hook.

The full 30+ semantic verb stems are defined in `scripts/pre-agent-guard.py` (`SEMANTIC` list). They cover analysis, understanding, review, reasoning, investigation, explanation, evaluation, comparison, design, implementation, debugging, refactoring, and more.

## Architecture: Two-Layer Enforcement

| Layer | Script | Hook | Action | What it catches |
|-------|--------|------|--------|-----------------|
| **Prevention** | `pre-agent-guard.py` | PreToolUse (Agent matcher) | Exit 2 — hard block before execution | Search-verb Agent calls caught at the call site |
| **Detection** | Session-end audit | Stop | Warning in audit output | Calls that slipped past prevention (pattern gaps, edge cases) |

The prevention layer stops waste before it happens. The detection layer audits at session end — if a search-pattern Agent call slipped through, it appears in the audit warning with the exact description. This dual layer means the system **fails closed**: even if one layer misses, the other catches it.

> **Self-check invariant:** If BOTH layers miss the same call, there's a bug in the patterns. File an issue with the description that slipped through.

## Hook Installation

Install `pre-agent-guard.py` as a PreToolUse hook in your Claude Code settings. The hook only fires for Agent calls (matcher: "Agent") and passes the tool input as JSON on stdin.

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Agent",
        "hooks": [{
          "type": "command",
          "command": "python3 ~/.claude/scripts/pre-agent-guard.py"
        }]
      }
    ]
  }
}
```

**Platform note:** On Windows (Git Bash), `python3` may resolve to a Microsoft Store stub rather than a working Python interpreter. Use `python` instead: `"command": "python ~/.claude/scripts/pre-agent-guard.py"`.

The hook reads the tool input from stdin, checks `description` and `prompt` fields against search-verb patterns, and exits 0 (allow), 1 (error), or 2 (block). When it blocks, it prints the blocked description and a suggested grep command to stderr.

> See `scripts/pre-agent-guard.py` for the full implementation. Run `python3 scripts/pre-agent-guard.py --help` for CLI usage. Run with `--json` for machine-readable output (useful in CI).

## Recovery: What To Do When Blocked

When the hook blocks an Agent call with exit 2, it prints the blocked description and a suggested grep command. Follow this sequence:

1. **Run the suggested grep command** (or `find`/`ls` equivalent) printed to stderr
2. **Read the results** — do you have what you need?
3. **Assess**: if grep results fully answer the question → done. If you need to read specific files → use Read (Tier 2). If you need to reason about patterns, anomalies, or implications across results → NOW escalate to Agent with a description that includes BOTH the search intent AND the reasoning verb (e.g., "analyze the grep results for error handling patterns to identify systemic issues")
4. **Do NOT** retry the same blocked description — the hook will block it again. Rewrite the description to include a reasoning verb.

False blocks happen when the semantic verb list is incomplete. If you believe the block was wrong, add the missing semantic verb to `SEMANTIC` in `pre-agent-guard.py` — don't disable the hook.

## When to Use

- You find yourself (or your agent) reaching for Agent to "search for X" or "find all Y"
- Session cost logs show Agent calls with search-verb descriptions and no semantic override
- Working in a large codebase (>100 files) where Agent-based search burns tokens on file scanning
- Want mechanical enforcement — not just a rule you have to remember each session

## When NOT to Use

- **Small codebases (<50 files):** Agent search cost is negligible; the hook adds friction without meaningful savings
- **Tasks that are purely reasoning/analysis** with no search component
- **Semantic code search that grep can't express:** e.g., "find functions that allocate memory" in C — this requires an AST-aware tool, not Agent *and* not grep. The ladder doesn't cover this case; use a language server or static analysis tool instead
- **When you're the hook system maintainer** debugging the hook itself — disable temporarily to avoid the hook blocking your debugging Agent calls

## Anti-Patterns

| Anti-Pattern | Why wrong | Fix |
|-------------|----------|-----|
| Agent for deterministic file/text search | Any search expressible as a regex — finding files, counting occurrences, listing matches — is a Tier 1 task. grep/find are faster, deterministic, and consume zero LLM tokens. | `grep -r "pattern" .` or `find . -name "*.ext"` |
| Agent "read config.json and tell me what's in it" | Use Read for the file, Agent only for the reasoning part. | `Read config.json` → then Agent if analysis needed |
| Pre-agent hook blocking too aggressively | False blocks are worse than false allows. The semantic verb list should be conservative. | Add the missing semantic verb; do NOT disable the hook |
| Skipping the detection layer | Prevention alone isn't enough — pattern gaps exist. The audit trail is your safety net. | Run a session-end audit (ship-gate, custom script) that checks for Agent misuse patterns |
| Using Agent because "I might need to reason later" | Retrieve first, decide if reasoning is needed second. Don't pay the reasoning tax upfront. | grep → Read → assess → Agent only if assessment says reasoning is needed |

## Maturity Stages

The skill's enforcement evolves through these stages. The first four describe progressive adoption; the last two are maintenance triggers.

- **Hook installed and active** → prevention layer running. Verify with a test Agent call: `"list all markdown files"` should be blocked.
- **One full session without Agent-misuse audit warnings** → pattern is working at the hook level.
- **Three consecutive sessions without audit warnings** → reflex is internalized. The agent now reaches for grep without being blocked. This is the target steady state.
- **False block encountered** → add the missing semantic verb to `SEMANTIC` in pre-agent-guard.py. Never disable the hook to work around a false block.
- **New search-verb pattern discovered** → add it to `SEARCH_VERB_PATTERNS` in pre-agent-guard.py and your session-end audit configuration (must stay in sync).
- **Detection layer converges** → zero Agent misuse warnings for 5 consecutive sessions AND no false blocks in that period. The agent's tool selection is consistently correct — downgrade to detection-only (remove the PreToolUse hook, keep the session-end audit as safety net).

## Cross-References

- **Complements:** `self-eval` (engineering/skills/) — self-eval scores ambition × execution for output quality; this skill enforces tool selection efficiency for process quality. Together they cover "is the output good?" and "was the process efficient?"
- **Complements:** `ship-gate` (engineering/skills/) — ship-gate audits pre-deployment across 8 categories; this skill audits pre-execution at the tool-call level. Different gates in the same quality pipeline.
- **Related:** `prompt-governance` (engineering/) — rule enforcement via hooks, different domain (prompt content vs. tool selection)
- **Related:** `llm-cost-optimizer` (engineering/) — strategic token cost optimization; this skill enforces tactical per-call tool efficiency. Different layers of the same cost stack.
- **Sources:** John Carmack — "measure before you optimize" (performance as craft, not afterthought). The regex-expressibility reframing is this skill's application of Carmack's principle, not Carmack's original formulation. Ken Thompson — Unix philosophy ("do one thing well" — each tool tier has exactly one job). Both cited with high confidence.
- **Theory:** Minimum Viable Token (MVT) principle (novel term, coined here) — every tool call should consume the minimum tokens necessary to answer the question. grep = O(1) LLM tokens for a search task; Agent = O(file_count × file_size) LLM tokens for the same task. The name follows the Minimum Viable Product pattern applied to token consumption.
