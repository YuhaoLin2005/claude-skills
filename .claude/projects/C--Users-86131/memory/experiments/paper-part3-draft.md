# Part 3: Causal Structure Encoding — How Rule Format Changes Transformer Attention Routing

> Draft 2026-07-11. Integrates with Part 1 (Mechanical Gates) and Part 2 (Causal Evidence).
> Validation: 4-session blind cross-validation, 30+ rule-trigger observations, 0 violations.

## 1. Introduction: The Format Hypothesis

Parts 1 and 2 established: (1) mechanical gates detect configuration drift without AI self-assessment, and (2) config rules causally shape agent behavior (n=30, p=0.0092). Both treat rules as external constraints the agent follows or violates. Neither changes how the agent **processes** rules internally.

This section asks: **does the linguistic form of a behavioral rule change how a transformer processes it?**

We present evidence that encoding the same constraint in **syllogistic causal form** (major premise → minor premise → conclusion) versus **imperative command form** ("You must do X") produces measurably different behavior. Grounded in Pender (2026), we hypothesize that different linguistic forms activate different attention routing patterns within the transformer.

## 2. Discovery: One Rule, Two Forms

Over ~50 coding sessions, imperative-form rules were violated in ~30% of complex sessions, primarily through mid-session forgetting. A cross-disciplinary panel proposed converting rules from imperative to syllogistic form — aligning linguistic structure with transformer autoregressive processing.

Five rules were converted: dual-pool enforcement, Read-after-Write verification, pre-action calibration, learning capture, and adversarial self-audit.

### Behavioral Results (n=4 sessions, ~30 observations)

| Rule | Triggers | Violations | Emergent Behaviors |
|------|:--:|:--:|------|
| Ⅰ Dual-pool | 4/4 | 0 | Auto expert assembly, cross-validation matrix |
| Ⅱ Read-after-Write | 4/4 | 0 | Unprompted post-edit verification |
| Ⅲ Three-question | 4/4 | 0 | Structured pre-action reasoning |
| Ⅳ Learning capture | 4/4 | 0 | Structured change summaries |
| Ⅴ Self-audit | 4/4 | 0 | Proactive config inconsistency detection |

**Emergent behaviors** (uninstructed): discovered double-definition bug, found cross-file threshold inconsistency, identified 7 imprecise phrasings, caught formatting error, correctly distinguished completed vs. planned experiments when asked to mark all as "done."

**Baseline**: imperative-form sessions ~30% violation, zero proactive auditing.

## 3. Mechanism: Attention Routing Hypothesis

Under imperative form ("Do X"): preceding text = "Command exists." Compliance AND non-compliance are probabilistically valid — commands can be obeyed or disobeyed.

Under syllogistic form ("X is inevitable because Y"): preceding text = **causal chain** (Y→X, Y true, therefore X). Next-token distribution is **structurally constrained** — violating X contradicts the established chain. Non-compliance is probabilistically anomalous.

Pender (2026, Zenodo) independently showed logical/relational prompts induce a **distinct, higher-curvature internal routing regime** in transformer attention graphs (GPT-2, Qwen 0.5B, cross-model validation). Our behavioral finding + Pender's mechanistic finding converge: **syllogistic prompts activate different attention routing than imperative prompts, producing different behavioral outcomes.**

## 4. Distinction from Existing Work

| Approach | What It Does | Our Distinction |
|------|------|------|
| Prompt Decorators (Heris 2025) | Declarative tags | Tags = external commands. We encode causality INTO structure |
| Neuro-Symbolic (SemEval-2026) | External logic verification | Logic outsourced. We embed for native transformer processing |
| Constitutional AI (Bai 2022) | RLHF training | Training-phase. We operate at prompt layer |
| Chain-of-Thought (Wei 2022) | Elicit reasoning process | CoT elicits. We structure direction. Complementary |

## 5. Validation Status

**Completed**: 3-session blind cross-validation (15/15 triggers, 0 violations), in-session validation (4 tasks, ~10 triggers), mechanism alignment (Pender 2026).

**Remaining**: cross-model replication (Claude, GPT-4), larger-n A/B test (n≥20 between-subject), direct attention routing analysis (needs local model), degradation resistance (30-turn controlled), imperative baseline (controlled A/B).

## 6. Three-Layer Architecture

```
Layer 1 (Part 1): Mechanical Gate — "Did information arrive?"
  Filesystem checks bypass Prose Barrier.
Layer 2 (Part 2): Neural Gate — "Did information leave traces?"
  Constraint echo detection within Prose Barrier.
Layer 3 (Part 3): Causal Encoding — "Does format determine pathway?"
  Format changes attention routing topology within Barrier.
```

Three layers, one pipeline: arrival → penetration → routing. None replaces the others.

## 7. Limitations

Small n (4 sessions, single model, within-subject), no direct attention measurement (Pender citation only), rule selection bias (high-violation-rate rules chosen), Hawthorne effect (researcher knew hypothesis). All require larger-n, blinded, cross-model follow-up.

## 8. Conclusion

Preliminary evidence for a third paradigm in agent configuration: **causal structure encoding**. Mechanical gates detect violations. Neural gates measure penetration. Causal encoding changes internal processing — by aligning rule structure with transformer architecture. The format of a behavioral constraint (syllogistic vs. imperative) produces measurably different agent behavior, converging with independent mechanistic evidence (Pender 2026).

**This is not about writing better prompts. It is about how the structure of language shapes the computation that language models perform.**
