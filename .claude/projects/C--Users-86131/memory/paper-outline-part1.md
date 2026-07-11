# Short Paper: Self-Referential Gate Architecture for Agent Configuration Integrity

> Revised 2026-07-10: Academic Researcher + Systems Engineer + Digital Twin + Web Search landscape.
> Target: arXiv → CHI LBW → ACL SRW.
> **Key shift**: Core contribution is NOT "dual-layer gate" — it's the **self-referential closure (strange loop)**.

## Competitive Landscape

- **HyperAgents** (Meta, ICLR 2026): code-layer. We work at config-layer.
- **Ouro Loop / Agentic Engineering**: task gates, no persistent agent identity.
- **ETH Zurich (arXiv 2604)**: validates "mechanical over semantic."
- **Our niche**: self-model regeneration + claimed-vs-evidenced cognition + creation-wiring gap. No existing framework does these.

## Title (Proposed v2 — post professor review)

> **Mechanical Before Semantic: Self-Verifying Configuration Integrity for AI Coding Agents**

(Not "ecosystem" — 4 checks, not an ecosystem. Not "strange loop" — self-referential feedback where gate output triggers self-model regeneration.)

**Core contribution (one sentence):**
Mechanical checks (mtime, regex, exit codes, hook wiring) detect and prevent AI agent configuration drift without relying on AI self-assessment — because the agent cannot reliably judge its own configuration integrity.

> **Dual-Layer Guard Architecture for AI Agent Configuration: Structural Convergence with Neural Activation Spaces**

Alternative: **Structural Isomorphism Across Implementation Layers: A Prompt-Level Guard Architecture and Its Neural Counterpart**

## Abstract (draft, ~150 words)

The dual-layer mechanical gate is an architecture for AI agent configuration that combines soft process monitoring with hard output blocking, deployed entirely at the prompt-engineering layer. We report an independently designed five-layer agent configuration system (identity, calibration, execution, memory, feedback) whose topology exhibits structural isomorphism with cross-layer convergence patterns observed in neural activation spaces. Across 30 controlled trials, Fisher's exact test yields p=0.0092 (odds ratio=11.0) for output quality improvement. Cross-domain behavioral generalization showed no significant result. QLoRA fine-tuning produced catastrophic forgetting—all behavioral metrics degraded despite decreasing loss. We interpret these results not as replication of neural-layer findings but as evidence for structural inevitability: the optimization target may determine architectural topology regardless of implementation substrate.

## Section Outline

### 1. Introduction
- Problem: single-developer AI agent reliability (no review/CI/QA infrastructure)
- Approach: dual-layer mechanical gate (soft process + hard output blocking)
- Surprise: independent convergence to five-layer topology mapping onto J-space
- Hypothesis: structural inevitability — same problem → same architectural shape
- Outline: related work → architecture → experiments → discussion

### 2. Related Work
- 2.1 Global Workspace Theory (Baars 1988, Goyal & Bengio 2022)
- 2.2 Neural Interpretability: J-space (Elhage et al. 2022, Bricken et al. 2023)
- 2.3 Constitutional AI and Guard Architectures (Bai et al. 2022, Kundu et al. 2024)
- 2.4 Prompt Engineering as Design Discipline (White et al. 2023, Zamfirescu-Pereira et al. 2023)
- 2.5 Behavioral Evaluation Beyond Perplexity (Lin et al. 2022 TruthfulQA)

### 3. Architecture
- Five layers: Identity → Calibration → Execution → Memory → Feedback
- Dual-layer gate: soft (config-health) + hard (quality-gate, exit 2)
- Key principles: mechanical over semantic, soft-on-process/hard-on-output, zero-token normal path
- Structural isomorphism with J-space (table)

### 4. Experiments
- 4.1 Controlled comparison: n=30, Fisher exact p=0.0092, OR=11.0
- 4.2 Cross-domain generalization: NULL (all p > 0.05)
- 4.3 QLoRA fine-tuning: NEGATIVE (loss↓ but behavior collapsed)

### 5. Discussion
- 5.1 Structural inevitability hypothesis
- 5.2 What null results mean
- 5.3 Limitations (n=30, single experimenter, single model, no blinding, no inter-rater reliability, qualitative isomorphism claim, no causal intervention)
- 5.4 Ethical considerations

### 6. Conclusion

## Part 2: Neural-Layer Gates — Beyond File System Verification

> Added 2026-07-10. AI Architect + Philosopher cross-review. Extends Part 1's file-system gates with neural-layer constraint fidelity detection.

### Motivation: The Prose Barrier

File-system gates (Part 1) check whether information ARRIVED — scripts exist, hooks are wired, files are updated. But they don't check whether constraints actually PENETRATED the generation process. The Prose Barrier (formalized in Part 1 §Discussion) implies that verification must operate at the level where information flows: the model's output distribution.

### Neural Gate v1: Constraint Echo Detection (deployed)

**Principle**: If a behavioral constraint defined in BODY.md is actively influencing the agent, its key concepts should appear as patterns in the agent's outputs.

**Implementation**: `neural-gate.py` — extracts 8 constraint themes from BODY.md, scans today's output files for keyword echoes. Silent constraint = may be decaying. 100% echo rate observed in initial deployment (2026-07-10).

### Neural Gate v2: Logprob Differential Detection (designed)

**Principle**: For a constraint to be neurally "active," it must shift the probability distribution over action-tokens in constraint-relevant contexts.

**Method**: For each constraint, a minimal completion prompt forcing binary choice (compliant vs violating). Call DeepSeek API with `logprobs=True`. Compute `delta = mean_logprob(compliant | constrained) - mean_logprob(compliant | baseline)`. Active threshold: delta > 0.3 logprob units.

**Status**: Script written (`neural-gate-v2.py`). Requires DEEPSEEK_API_KEY.

### Neural Gate v3: Residual Stream Probes (roadmap)

**Method**: On Qwen2.5-1.5B (fits RTX 3060 6GB), extract residual stream activations at last token position for constraint-bearing vs neutral prompts. Train logistic regression probes per layer. Deploy best-layer probe for real-time constraint presence detection.

**Feasibility**: RTX 3060 6GB sufficient for 1.5B model (~4GB VRAM). Extraction + training: ~2-4 hours. Not feasible for 7B+ locally — needs cloud GPU.

### Dual-Layer Completeness

| Failure Mode | File Gates | Neural v1 | Neural v2 | Neural v3 |
|------|:--:|:--:|:--:|:--:|
| Script not wired | ✅ | — | — | — |
| Constraint never echoed in output | — | ✅ | — | — |
| Constraint echoed, no prob shift | — | — | ✅ | — |
| Constraint encoded, no causal effect | — | — | — | ✅ |
| Constraint conflict (two rules clash) | — | — | — | — |

**Known gap**: Constraint conflict resolution — when "自动执行" and "不逆操作前确认" conflict, neither layer detects which constraint dominated. Future work.

## Part 3: Causal Structure Encoding — Format → Routing → Behavior

> Added 2026-07-11. Cross-disciplinary panel (logic/philosophy/anthropology/systems/AI behavior/risk) + 2-session blind cross-validation.
> Extends Part 1 (mechanical defense) and Part 2 (neural detection) with a third paradigm: encoding behavioral rules as causal structures that change transformer attention routing.

### Motivation: Beyond "Follow the Rules"

Parts 1 and 2 share an assumption: rules are external constraints the agent follows or violates. Mechanical gates detect violations; neural gates detect constraint echo. Neither changes how the agent *processes* the rules.

**What if the linguistic form of the rule changes how the transformer processes it?**

### Core Discovery: Syllogism vs. Imperative

Over 50+ sessions, imperative-form rules ("You must do X") were violated in ~30% of complex sessions. Converting rules to syllogistic causal form:

```
命令式: "影响>30天的决策必须双池审查——跳过=翻车"

三段论: "大前提: NL-agent的验证/生成共享通道→盲区结构性存在。
        我需要判断: 当前决策影响>30天？
        如果是: 盲区必然存在→独立视角是唯一的揭示机制。"
```

Two-session blind cross-validation: agent with ONLY syllogism-form rules naturally triggered dual-pool review without being commanded, discovered configuration inconsistencies proactively, and maintained rule-consistent behavior. 5/5 syllogism rules triggered correct behavior without explicit commands.

### Mechanism: Attention Routing Hypothesis

Pender (2026, Zenodo) showed **logical/relational prompts induce a measurably distinct internal routing regime** in transformer attention graphs — higher Forman curvature, stronger class separation in deeper layers, cross-model validation (GPT-2, Qwen 0.5B).

Our hypothesis: Imperative and syllogistic formulations of the same constraint trigger different attention routing patterns. Imperative ("Do X") = command → model can comply OR violate (both probabilistically valid). Syllogistic ("X inevitable because Y") = causal chain → next-token prediction constrained by established causal structure → violation is improbable continuation.

This is not "better prompt engineering." **The format of a behavioral rule determines its internal processing pathway.** Causal-structural formats align with the transformer's autoregressive architecture; imperative formats do not.

### Research Questions

1. **RQ1 (Behavioral)**: Does syllogism-form encoding reduce rule violation vs. imperative? [Evidence: 2-session blind cross-validation, 30% → near-zero, 5/5 rules triggered]

2. **RQ2 (Mechanistic)**: Do syllogism vs. imperative trigger different attention routing? [Alignment with Pender 2026; direct causal mediation analysis TBD]

3. **RQ3 (Generalizability)**: Does format→routing→behavior hold across models (DeepSeek V4, Claude, GPT) and rule types?

### Competitive Landscape

| Approach | What They Do | Our Distinction |
|------|------|------|
| LMQL, BAML | Enforce output syntax | We encode behavioral causality, not syntax |
| Prompt Decorators (Heris 2025) | Declarative tags for LLM control | We show format changes internal routing |
| Neuro-Symbolic (SemEval-2026) | External logic verification | We embed causal structure IN prompt's processing path |
| Constitutional AI (Bai 2022) | RLHF training with principles | Prompt layer, no training |
| Attention Routing (Pender 2026) | Logical prompts → distinct routing | We engineer for behavioral effect, grounded in same mechanism |

### Three-Part Architecture

```
Part 1 (Mechanical)       Part 2 (Neural)          Part 3 (Causal Encoding)
防御层: 文件系统检查        检测层: NL回显检测         编码层: 格式改变路由
"信息到了门口没有？"       "信息留下痕迹了吗？"       "信息的形式决定走哪条路"
绕过 Prose Barrier         在 Barrier 内检测          改变 Barrier 内的路径
                               
          三层覆盖同一管道: 到达 → 穿透 → 路由
```

### Experimental Design

1. **A/B test**: n=20 sessions/condition, blind. Measure: rule violation, proactive following, self-audit frequency
2. **Cross-model**: Same rules on DeepSeek V4 vs Claude vs GPT. Measure: behavioral consistency
3. **Attention analysis** (needs logprobs/local model): Paired syllogism/imperative prompts, compare routing topology (Forman curvature, layer-wise KL)
4. **Degradation study**: Over 30-turn sessions, does causal encoding resist mid-session attention decay?

### References to Add

- Pender, M. A. (2026). Formal Constraint and Routing Reorganization: A Constrained-Transport View of Transformer Attention. Zenodo. DOI: 10.5281/zenodo.19363505
- Heris, M. K. (2025). Prompt Decorators: A Declarative and Composable Syntax. arXiv:2510.19850
- SemEval-2026 Task 11: Syllogistic Reasoning. Multiple systems achieving 100.0 via neuro-symbolic approaches.
- The Magic of IF: Code-LLMs outperform on causal reasoning with conditional structures — structure > format.

## Pre-Professor Checklist

### Blockers (do not schedule meeting without)
1. ⬜ Second rater for output classification (Cohen's kappa)
2. ⬜ Reproducible experimental protocol documented
3. ⬜ Fisher exact test independently recomputed
4. ⬜ Clarify 5-category/3-gate classification criteria

### Professor's First Questions (prepare)
5. ⬜ Power analysis (n=30 minimum detectable effect size?)
6. ⬜ Task list for 30 trials (difficulty, randomization, independence)
7. ⬜ J-space comparison formalization criterion
8. ⬜ Coincidence probability estimate

### Nice-to-Have
9. ⬜ Re-run with randomized task order
10. ⬜ Add second model backend (10 trials)
11. ⬜ Pre-registration (OSF/AsPredicted)
12. ⬜ Causal swap experimental design draft

## Meeting Readiness: YES (with conditions)

**Opening line**: "I built something that worked for my own use, noticed it structurally resembles something in published literature, ran initial experiments. Results mixed — one significant, two null. I want your advice on whether worth writing up as workshop paper."

**Professor will question**: (1) J-space citation legitimacy (2) Null hypothesis precision (3) Trial independence (4) PR #778 publication status (5) Whether Anthropic papers were actually read or just blog posts (6) Why convergence isn't just imposed pattern-matching.

**Bottom line**: Enough substance for first conversation. Honest about limitations. Concrete next-steps list.
