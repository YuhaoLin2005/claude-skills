# Part 3 References: Causal Structure Encoding

## Core Mechanism Reference

1. **Pender, M. A. (2026).** "Formal Constraint and Routing Reorganization: A Constrained-Transport View of Transformer Attention." Zenodo. DOI: 10.5281/zenodo.19363505.
   - Treats causal attention as transport graph; 5 prompt classes.
   - Key: Logical/relational prompts induce distinct higher-curvature routing regime.
   - Cross-model: GPT-2, Qwen 0.5B.

2. **Heris, M. K. (2025).** "Prompt Decorators: A Declarative and Composable Syntax." arXiv:2510.19850.
   - Declarative tags (+++Reasoning, +++Tone) for LLM control.
   - Difference: Tags = external commands. We encode causality INTO structure.

3. **SemEval-2026 Task 11.** Syllogistic reasoning with LLMs.
   - SDP 100.0, Neuro-Symbolic 100.0, FregeLogic 94.3%.
   - Difference: They judge syllogism validity. We use syllogism AS prompt format.

4. **"The Magic of IF."** Code-LLMs for causal reasoning.
   - Conditional structures outperform text-only. Structure > format.

5. **Javadov (2026).** "When Does Routing Become Interpretable?" arXiv:2606.13168.
   - Routing mass ≠ causal importance.

6. **Darade & Thorat (2026).** "Represented Is Not Computed." arXiv:2605.22488.
   - Probes ≠ causal mechanisms.

## Our Position

```
LMQL/BAML ──── 输出格式约束（语法）
Prompt Decorators ──── 声明式标签（命令替代NL）
Neuro-Symbolic ──── 外部逻辑验证（外包）
Constitutional AI ──── 训练时注入（需RLHF）
Pender (2026) ──── 格式→路由证据（纯分析）

我们 ──── 格式→路由→行为的工程转化
          （Pender机制 + 行为验证 → 因果结构编码范式）
```

## Gaps

- [ ] Direct causal mediation on syllogism vs imperative (needs local model)
- [ ] Cross-model replication (Claude, GPT-4)
- [ ] Larger n A/B test (current: 2 sessions)
- [ ] Formalize attention routing hypothesis
- [ ] Baseline comparison vs Prompt Decorators
