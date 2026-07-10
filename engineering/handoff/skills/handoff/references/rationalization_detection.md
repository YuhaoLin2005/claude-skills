# Rationalization Detection

> Detects moments when an agent decides NOT to capture learning — the gap
> handoff and eval-learn-loop don't cover.

## Why

Handoff captures what was done. Eval-learn-loop captures what was learned.
Neither captures **the decision not to capture anything**.

Patterns like "I'll write growth-log next session" or "changes too small to
audit" are rationalizations — they sound reasonable but compound into zero
learning capture across sessions.

## Patterns

| Rationalization | Reality |
|---|---|
| "Just a few lines changed, skip the audit" | Small changes are the most dangerous — no test coverage, one line can break everything. |
| "Too tired, I'll write growth-log next session" | Every session that says this → zero sessions that actually do. |
| "I'll remember what I learned" | Knowledge not written down is knowledge lost. Same mistake next week proves it. |
| "All checks pass, no need to show output" | All-OK without specifics is suspicious. Complex tasks always find at least one thing. |

## Detection

Pattern-based, no LLM calls. Match against common rationalization phrases in
the session context before writing the handoff doc.

English patterns: `"pre-existing issue"`, `"skipping tests for now"`,
`"tests broken but we'll fix"`, `"not addressing the failing build"`,
`"I'll write it next session"`, `"changes too small to audit"`.

False positive rate: ~1 in 20. Tune per-project if higher.

## Usage

Run as a pre-write sanity check before composing the handoff document:

1. Scan session context for rationalization patterns
2. If detected → flag: "Is there genuinely nothing to capture?"
3. If clean → proceed with handoff

Not a blocking gate — a prompt to think twice before declaring "nothing learned."

## See Also

- [handoff_structure.md](handoff_structure.md)
- [deduplication_discipline.md](deduplication_discipline.md)
- `session-quality-gate` (deprecated standalone; merged here per Addy Osmani feedback)
