# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This is a **comprehensive skills library** for Claude AI and Claude Code - reusable, production-ready skill packages that bundle domain expertise, best practices, analysis tools, and strategic frameworks. The repository provides modular skills that teams can download and use directly in their workflows.

**Current Scope:** 351 production-ready skills across 19 domains with 586 Python automation tools, 714 reference guides, 94 agents (cs-* + 7 personas), and 100 slash commands, distributed as 79 marketplace plugins. Headline counters are derived from the tree by `scripts/derive_counters.py` (run with `--check` to verify the docs still match). **v2.9.0 (complete)** added the **research-ops/** top-level domain — enterprise Research Operations (orchestrator + clinical-research + research-finance + market-research + product-research), the managed counterpart to the academic research/ domain, with `context: fork` orchestration and a Matt Pocock "Forcing-question library" in every SKILL.md plus `/cs:grill-research-ops`. **v2.8.0 (complete)** added 2 new top-level domains — **business-operations/** (7 internal-ops skills: orchestrator + process-mapper + vendor-management + capacity-planner + internal-comms + knowledge-ops + procurement-optimizer) and **commercial/** (8 per-deal-economics skills: orchestrator + pricing-strategist + deal-desk + partnerships-architect + channel-economics + commercial-policy + rfp-responder + commercial-forecaster) — with orchestrator skills using `context: fork` for chaining, Matt Pocock docs-anchored "Forcing-question library" in every SKILL.md, plus `/cs:grill-bizops` and `/cs:grill-commercial`. **v2.8.2** adds a productivity-shaped `handoff` skill (sibling to engineering/handoff) inspired by Matt Pocock — first-run setup with configurable save location, redaction linter, SessionStart + SessionEnd hooks, fidelity self-check, `--refresh` flag. **v2.8.1** upgraded the engineering role-skills (senior-fullstack / senior-frontend / senior-backend) with karpathy-coder + Matt Pocock decision engines + per-role forcing questions. v2.7.3 ports `alirezarezvani/aeo-box` — AEO (Answer Engine Optimization) skill into marketing-skill/ + security-guidance PreToolUse hook into engineering/. v2.7.0 added 13 Path-B skills across 3 top-level domains (productivity, marketing, research). v2.6.0 added 4 Matt Pocock-derived productivity skills.

**Key Distinction**: This is NOT a traditional application. It's a library of skill packages meant to be extracted and deployed by users into their own Claude workflows.

## Maintainer-Local Folders (gitignored)

The following exist on the maintainer's disk but are excluded from the public GitHub tree so cloners only see production skill packages:

- `documentation/` — sprint plans, strategy, implementation roadmaps
- `eval-workspace/` — Tessl evaluation outputs
- `megaprompts/` — pre-skill draft specs (Path-B source material)
- `tests/` — pytest suite (run locally; not in CI)
- `.autoresearch/` — autoresearch agent workspace
- `AUDIT_REPORT.md` — internal audit snapshots

**Distinct from the above:** the top-level `audit/` directory (e.g.
`audit/newgen-2026-06/`) is an **intentional, public** audit record — rubric +
per-domain reports with per-skill verification criteria that follow-up PRs use
as acceptance gates. It is excluded from headline counters by
`scripts/derive_counters.py`, but it is committed and visible to cloners.
`AUDIT_REPORT.md` (gitignored, above) is the older internal-snapshot format.

In-repo references to paths under these folders (e.g. `documentation/implementation/...`) resolve locally for the maintainer but appear as dead links on GitHub. This is intentional.

## Navigation Map

This repository uses **modular documentation**. For domain-specific guidance, see:

| Domain | CLAUDE.md Location | Focus |
|--------|-------------------|-------|
| **Agent Development** | [agents/CLAUDE.md](agents/CLAUDE.md) | cs-* agent creation, YAML frontmatter, relative paths |
| **Marketing Skills** | [marketing-skill/CLAUDE.md](marketing-skill/CLAUDE.md) | Content creation, SEO, ASO, demand gen, campaign analytics |
| **Product Team** | [product-team/CLAUDE.md](product-team/CLAUDE.md) | RICE, OKRs, user stories, UX research, SaaS scaffolding |
| **Engineering (Core)** | [engineering-team/CLAUDE.md](engineering-team/CLAUDE.md) | Fullstack, AI/ML, DevOps, security, data, QA tools |
| **Engineering (POWERFUL)** | [engineering/](engineering/) | Agent design, RAG, MCP, CI/CD, database, observability |
| **C-Level Advisory** | [c-level-advisor/CLAUDE.md](c-level-advisor/CLAUDE.md) | CEO/CTO strategic decision-making |
| **Project Management** | [project-management/CLAUDE.md](project-management/CLAUDE.md) | Atlassian MCP, Jira/Confluence integration |
| **RA/QM Compliance** | [ra-qm-team/CLAUDE.md](ra-qm-team/CLAUDE.md) | ISO 13485, MDR, FDA, GDPR, ISO 27001 compliance |
| **Business & Growth** | [business-growth/CLAUDE.md](business-growth/CLAUDE.md) | Customer success, sales engineering, revenue operations |
| **Finance** | [finance/CLAUDE.md](finance/CLAUDE.md) | Financial analysis, DCF valuation, budgeting, forecasting, SaaS metrics |
| **Research Operations** | [research-ops/CLAUDE.md](research-ops/CLAUDE.md) | Clinical study design, R&D finance, market research, product research (enterprise counterpart to academic research/) |
| **Markdown → HTML** | [markdown-html/CLAUDE.md](markdown-html/CLAUDE.md) | Markdown-to-interactive-HTML converter (orchestrator + design-system foundation; md-document/review/slides v2.10.1). Inspired by Shihipar's "Claude Code HTML output" essay |
| **Standards Library** | [standards/CLAUDE.md](standards/CLAUDE.md) | Communication, quality, git, security standards |
| **Templates** | [templates/CLAUDE.md](templates/CLAUDE.md) | Template system usage |

## Architecture Overview

### Repository Structure

```
claude-code-skills/
├── .claude-plugin/            # Plugin registry (marketplace.json)
├── agents/                    # 32 standalone agents (cs-* + 7 personas); 51+ cs-* agents repo-wide
├── commands/                  # slash commands (changelog, tdd, saas-health, prd, code-to-prd, plugin-audit, sprint-plan, slo-design, etc.); 87+ repo-wide
├── engineering-team/          # 51 core engineering skills + Playwright Pro + Self-Improving Agent + Security Suite
├── engineering/               # 78 POWERFUL-tier advanced skills (incl. AgentHub, autoresearch-agent, self-eval, llm-wiki, tc-tracker, ship-gate, slo-architect, write-a-skill, caveman, grill-me, handoff)
├── product-team/              # 17 product skills (incl. apple-hig-expert) + Python tools
├── marketing-skill/           # 46 marketing skills (8 pods) + Python tools
├── c-level-advisor/           # 66 C-level advisory skills (full C-suite + founder-mode agents + orchestration)
├── project-management/        # 9 PM skills + bundled Atlassian Remote MCP (.mcp.json)
├── ra-qm-team/                # 18 RA/QM compliance skills
├── compliance-os/             # 9 compliance-OS skills
├── business-growth/           # 5 business & growth skills + Python tools
├── business-operations/       # 7 internal-ops skills (orchestrator + 6 sub-skills)
├── commercial/                # 8 per-deal-economics skills (orchestrator + 7 sub-skills)
├── finance/                   # 4 finance skills + Python tools
├── research/                  # 8 academic research skills (orchestrator + 7 specialists)
├── research-ops/              # 5 research-ops skills (orchestrator + clinical-research + research-finance + market-research + product-research)
├── markdown-html/             # 2 markdown-to-HTML skills v2.10.0 foundation (orchestrator + design-system); md-document/review/slides land in v2.10.1
├── eval-workspace/            # Skill evaluation results (Tessl)
├── standards/                 # 5 standards library files
├── templates/                 # Reusable templates
├── docs/                      # MkDocs Material documentation site
├── scripts/                   # Build scripts (docs generation)
└── documentation/             # Implementation plans, sprints, delivery
```

### Skill Package Pattern

Each skill follows this structure:
```
skill-name/
├── SKILL.md              # Master documentation
├── scripts/              # Python CLI tools (no ML/LLM calls)
├── references/           # Expert knowledge bases
└── assets/               # User templates
```

**Design Philosophy**: Skills are self-contained packages. Each includes executable tools (Python scripts), knowledge bases (markdown references), and user-facing templates. Teams can extract a skill folder and use it immediately.

**Key Pattern**: Knowledge flows from `references/` → into `SKILL.md` workflows → executed via `scripts/` → applied using `assets/` templates.

## Git Workflow

**Branch Strategy:** feature → dev → main (PR only)

> **⛔ HARD RULE — PR TARGET IS ALWAYS `dev`, NEVER `main`.**
> Every PR (human or AI-created) must use `--base dev`. Nothing merges into `main`
> directly — `main` only receives periodic `dev → main` promotion PRs opened by the
> maintainer. If you find a PR targeting `main`, retarget it to `dev` before review.
> AI agents (Claude Code included): set the base branch explicitly when creating PRs;
> never rely on the repository default branch.

**Branch Protection Active:** Main branch requires PR approval. Direct pushes blocked.

### Quick Start

```bash
# 1. Always start from dev
git checkout dev
git pull origin dev

# 2. Create feature branch
git checkout -b feature/agents-{name}

# 3. Work and commit (conventional commits)
feat(agents): implement cs-{agent-name}
fix(tool): correct calculation logic
docs(workflow): update branch strategy

# 4. Push and create PR to dev
git push origin feature/agents-{name}
gh pr create --base dev --head feature/agents-{name}

# 5. After approval, PR merges to dev
# 6. Periodically, dev merges to main via PR
```

**Branch Protection Rules:**
- ✅ Main: Requires PR approval, no direct push
- ✅ Dev: Unprotected, but PRs recommended
- ✅ All: Conventional commits enforced

See [documentation/WORKFLOW.md](documentation/WORKFLOW.md) for complete workflow guide.
See [standards/git/git-workflow-standards.md](standards/git/git-workflow-standards.md) for commit standards.

## Development Environment

**No build system or test frameworks** - intentional design choice for portability.

**Python Scripts:**
- Use standard library only (minimal dependencies)
- CLI-first design for easy automation
- Support both JSON and human-readable output
- No ML/LLM calls (keeps skills portable and fast)

**If adding dependencies:**
- Keep scripts runnable with minimal setup (`pip install package` at most)
- Document all dependencies in SKILL.md
- Prefer standard library implementations


## Current Version

**Version:** v0.7.0 — Tier3 audit: 7 fixes deployed, 2d growth-logs absorbed — [Full changelog](CHANGELOG.md)

## Roadmap

**Phase 1-4 Complete:** 246 production-ready skills deployed across 9 domains
- Engineering Core (32), Engineering POWERFUL (40), Product (13), Marketing (44), PM (9), C-Level (28), RA/QM (14), Business & Growth (5), Finance (3)
- 359 Python automation tools, 485 reference guides, 27 agents, 33 commands
- Complete enterprise coverage from engineering through regulatory compliance, sales, customer success, and finance
- Reliability portfolio: feature-flags-architect, kubernetes-operator, chaos-engineering, slo-architect (Google SRE Workbook canon)
- MkDocs Material docs site with 293+ indexed pages for SEO

See domain-specific roadmaps in each skill folder's README.md or roadmap files.

## Key Principles

1. **Skills are products** - Each skill deployable as standalone package
2. **Documentation-driven** - Success depends on clear, actionable docs
3. **Algorithm over AI** - Use deterministic analysis (code) vs LLM calls
4. **Template-heavy** - Provide ready-to-use templates users customize
5. **Platform-specific** - Specific best practices > generic advice

## ClawHub Publishing Constraints

This repository publishes skills to **ClawHub** (clawhub.com) as the distribution registry. The following rules are **non-negotiable**:

1. **cs- prefix for slug conflicts only.** When a skill slug is already taken on ClawHub by another publisher, publish with the `cs-` prefix (e.g., `cs-copywriting`, `cs-seo-audit`). The `cs-` prefix applies **only on the ClawHub registry** — repo folder names, local skill names, and all other tools (Claude Code, Codex, Gemini CLI) remain unchanged.
2. **Never rename repo folders or local skill names** to match ClawHub slugs. The repo is the source of truth.
3. **No paid/commercial service dependencies.** Skills must not require paid third-party API keys or commercial services unless provided by the project itself. Free-tier APIs and BYOK (bring-your-own-key) patterns are acceptable.
4. **Rate limit: 5 new skills per hour** on ClawHub. Batch publishes must respect this. Use the drip timer (`clawhub-drip.timer`) for bulk operations.
5. **plugin.json schema** — Required fields: `name`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `skills`. Two **approved extension fields** are permitted in the repo (stripped at ClawHub-publish time, if/when a stripping pipeline lands):
   - `source` (object) — provenance metadata for skills built via Path-B megaprompt conversion. Recommended shape: `{spec: "megaprompts/NN-name.md", build_pattern: "...", distinct_from: "..."}`. Used by all 13 v2 megaprompt-derived skills (productivity/, marketing/, research/).
   - `attribution` (object) — credit metadata for skills derived from external MIT-licensed work. Used by `engineering/caveman`, `engineering/grill-me`, `engineering/grill-with-docs` (Matt Pocock derivatives).

   No other extras. The `skills` value depends on the plugin layout. Per the live Claude Code plugin spec ([plugins-reference](https://code.claude.com/docs/en/plugins-reference)), **all paths must be relative to the plugin root and start with `./`**. CC 2.1.144+ returns `Validation errors: skills: Invalid input` on a bare string without the prefix.

   **Canonical forms (CC 2.1.144+):**
   - Single-skill plugin (SKILL.md at root): `"skills": ["./"]` (array form required).
   - Plugin with `skills/` subdir: `"skills": "./skills"` or `"skills": ["./skills"]`.
   - Multi-skill domain plugin (skills are subfolders at root): `"skills": ["./sub1", "./sub2", ...]` (explicit list).

   **Legacy form (still tolerated by the validator):** `"skills": "skills"` (bare subdir name, no `./`). Older versions of CC accepted this; current CC rejects it. The repo has been fully migrated to the canonical form — the validator keeps WARN-level tolerance for the legacy literal as a safety net against accidental regressions in copied templates. Do **not** use this form in new manifests.

   **Historical regressions (now reversed upstream):** The `./` prefix was briefly forbidden between CC v2.1.107 and v2.1.144 (issues #539, #686). That window is closed; the `./` prefix is required again. Do **not** reintroduce the bare-string form for new manifests.

   **Enforcement:** `scripts/check_plugin_json.py --all` runs in `ci-quality-gate.yml` on every PR. It hard-fails on any non-`./`-prefixed string that isn't the legacy `"skills"` literal, on empty strings/arrays, and on non-string array entries. When CC tightens its path validator again in the future, update both the validator (`_check_skills_string` / `_check_skills_array`) and this section together — they must move in lockstep.
6. **Version follows repo versioning.** ClawHub package versions must match the repo release version (currently v2.7.0+).

## Anti-Patterns to Avoid

- Creating dependencies between skills (keep each self-contained)
- Adding complex build systems or test frameworks (maintain simplicity)
- Generic advice (focus on specific, actionable frameworks)
- LLM calls in scripts (defeats portability and speed)
- Over-documenting file structure (skills are simple by design)

## Working with This Repository

**Creating New Skills:** Follow the appropriate domain's roadmap and CLAUDE.md guide (see Navigation Map above).

**Editing Existing Skills:** Maintain consistency across markdown files. Use the same voice, formatting, and structure patterns.

**Quality Standard:** Each skill should save users 40%+ time while improving consistency/quality by 30%+.

## Additional Resources

- **.gitignore:** Excludes .vscode/, .DS_Store, AGENTS.md, PROMPTS.md, .env*
- **Plugin Registry:** [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) - Marketplace distribution
- **Standards Library:** [standards/](standards/) - Communication, quality, git, documentation, security
- **Implementation Plans:** [documentation/implementation/](documentation/implementation/)
- **Sprint Delivery:** [documentation/delivery/](documentation/delivery/)

---

**Last Updated:** June 10, 2026
**Version:** v2.10.3
**Status:** 345 skills deployed across 17 domains, 78 marketplace plugins, docs site live (counters derived via `scripts/derive_counters.py`)
