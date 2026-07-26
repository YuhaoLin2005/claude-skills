---
name: evolution-roadmap
description: "系统演化路线图——从当前阶段1(概念验证)到阶段4(宪法层+正典化)的硬性达标条件和目标架构。2026-07-04深度讨论产出。"
metadata:
  node_type: memory
  type: project
  originSessionId: current
  created: 2026-07-04
  sources: self-model.md v0.5, SOUL.md, INTERFACE.md, BODY.md, ratings-tracker.md, pending-verifications.md
---

# 系统演化路线图

> **核心原则**: 科学指导而非类比驱动。LLM 的物理现实决定架构上限——primacy effect、self-consistency、Constitutional AI、MemGPT。生命/宗教类比提供直觉方向，不替代科学理解。
> **硬约束**: 每个阶段必须跑稳后才能进入下一阶段。禁止兴奋升级。

---

## 当前状态：阶段 1 — 概念验证

**已达成的:**
- 奇异环设计完成，4/5 步机械化（quality-gate 写 flag / health-check 检测 / AI 再生 / log-regeneration 写日志）
- 双层机械门部署（config-health 过程层 + quality-gate 产出层）
- 双池审查系统（固定池 + 随机池，anti-fabrication discipline）
- SOUL/INTERFACE/BODY 三层分离（"换 LLM 只换 INTERFACE"）
- MEMORY.md HOT/WARM/COLD 三级索引
- 人格池、growth-log、ratings-tracker、decisions/log
- ~23 脚本、50K 行 Python

**未达成的（阶段 2 准入条件）:**

| # | 条件 | 当前 (2026-07-11 验证) | 目标 |
|---|------|------|------|
| 1 | 奇异环连续完整闭环 | ✅ 日志存在(7条, 7/2→7/10)，✅ flag检测正常，✅ 冷却期正常(24h)，🟡 连续3session触发trigger=flag待验证(entry#6为manual触发)，🟡 entry#7 flag_cleaned=false | 连续 3 session 完整闭环(trigger=flag, validation=PASSED)，4 步全部机械证据 |
| 2 | HOT 区收敛 | ✅ 53→15 (2026-07-10审计日策展)，🟡 持续≤15待跨session验证 | ≤15 条持续≥3 session |
| 3 | ratings 外部验证 | 🟡 大量 confidence=low, self_report 未变 | ≥3 个维度升级到 confidence=medium（外部证据） |
| 4 | pending-verifications 激活 | ✅ 文件有7条待验证项(🔴5+🟡2)，⚠️ 但SessionStart未机械检查此文件，依赖AI记忆读取 | 至少 1 轮完整的"添加→追踪→验证→自动删除" + SessionStart机械检查 |
| 5 | 数据积累 | ✅ growth-log 6/25→7/10 (16天)，远超10 session | ≥10 session 连续数据（growth-log, cost, config-usage） |

---

## 目标架构：阶段 4 — 宪法层 + 正典化

> 以下为达标后的转变方向。**当前不可执行，仅为方向记录。**

### 四层架构（科学基础标注）

```
宪法层 (CONSTITUTION.md)
  ├─ 位置: context window 最前 10%（primacy effect 保护）
  ├─ 性质: 自然语言宪法，修宪需 3/5 人格共识 + 用户批准 + 24h 冷却
  ├─ 机制: Constitutional AI (Bai et al., 2022) — LLM 自我批判-修订循环
  └─ 不可由 session 级决策修改
        ↓
评价场（触发式多路径采样）
  ├─ 机制: Self-Consistency (Wang et al., 2023) — 温度 0.7-0.8, 3-5 独立采样
  ├─ 触发: 新规则提出 / 规则 >10 session / 规则矛盾 / 自模型再生前
  └─ 不一致 = 能量 = 驱动辩论；一致 = 稳定吸引子
        ↓
执行层（当前 BODY + INTERFACE）
  ├─ 宪法授权的 session 级规则
  ├─ 可被 lost-in-the-middle（宪法 primacy anchor 保护核心约束）
  └─ 规则有腐烂期限，到期自动降级为候选
        ↓
反馈层（growth-log + quality-gate + 记忆自动管理）
  ├─ 机制: MemGPT (Packer et al., 2023) — LLM 自判断记忆热度
  ├─ 监控执行与宪法偏差
  └─ 触发修宪提案，不直接修改宪法
```

### 生成性对抗正典化流程

```
① 生成: AI 提议新规则 → candidate/ 目录
② 批判: 3 人格独立评估（不同 prompt, T=0.8）
    - 与宪法一致？
    - 机械执行门槛是什么？
    - 可能与哪条现行规则冲突？
③ 对抗:
    - ≥2/3 通过 → 进入正典化
    - ≥2/3 不通过 → rejected + 理由
    - 分裂(1-2/3) → 触发 5 人格深度辩论
④ 正典化: 通过 + 用户批准 + 24h 冷却 → 写入 CONSTITUTION.md
```

### 记忆自动管理

```
session 收尾 prompt:
"回顾本 session 产生的所有记忆条目，
 对每条，估计你在未来 session 中需要引用它的概率（0-10）。
 >7 = HOT, 3-7 = WARM, <3 = COLD。
 给出判断并附一句话理由。"

优势: LLM 是实际使用记忆的一方，按语义相关性判断，
     比 curator.py 按最后修改时间更科学
```

---

## LLM 物理约束（设计时必须遵守）

| LLM 不是 | 意味着 | 设计推论 |
|----------|--------|---------|
| 活系统 | 无后台进程、无肌肉记忆 | 所有"持续"行为 = 触发式加载 prompt |
| 有 DNA | 持久化只有文件和上下文 | 所有演化必须体现为文件内容变化 |
| 有随机突变 | 参数在 session 内固定 | 多样性靠 prompt 扰动 + 温度采样 |

| 已证实的科学机制 | 工程实现 |
|-----------------|---------|
| Primacy Effect | 最重要的约束放 context 最前面 |
| Lost-in-the-Middle | 执行层规则可被衰减，宪法层不可 |
| Self-Consistency | 多路径采样 + 统计收敛 = 质量信号 |
| Constitutional AI | 自然语言宪法 + LLM 自我批判-修订 |
| MemGPT 虚拟内存 | LLM 自判断记忆冷热度 |

---

## 禁止模式

- **兴奋升级**: 概念未被当前阶段验证就推进到下一阶段
- **类比驱动设计**: 用"免疫系统这样做"代替"LLM 的实际机制是什么"
- **规则堆积**: 每发现一个问题加一个 guard → guard 的 guard → guard 的 guard 的 guard
- **声明即执行幻觉**: 在 .md 里写了规则就假设它被执行（需机械验证）

---

## 下一步（本 session 及后续）

1. **立即**: 修复 `.self-model-regeneration.jsonl` 缺失——定位 log-regeneration.py 是否被正确调用
2. **本 session 收尾**: quality-gate 写 `.self-model-stale` flag
3. **下次 session 启动**: 验证 health-check 检测 flag → AI 再生 → log 写入，全闭环
4. **持续**: HOT 区收敛、ratings 外部验证、pending-verifications 激活
5. **达标后**: 创建 `CONSTITUTION.md` 草稿，触发首次正典化辩论

---

## See Also

- [[self-model]] — 当前自我认知 v0.5
- [[ratings-tracker]] — 能力量化追踪
- [[pending-verifications]] — 待验证项
- [[dual-layer-mechanical-gate]] — 双层机械门
- [[hermes-positioning]] — 赫尔墨斯工程定位
