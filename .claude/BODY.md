# BODY
> 流程规则 · 审查系统 · 交付门 · 受INTERFACE神经系统调控
> 铁律: 自动执行检查/标记/建议 · 人做最终判断

## 源头映射（INTERFACE 神经系统表 → BODY 规则）
| INTERFACE 行 | 大脑特征 | BODY 规则 |
|-------------|---------|----------|
| L1 | 长对话易漂移 · 注意力衰减快 | risk-scanner(机械) · 奇异环再生 · 自审频率 |
| L2 | 工具调用精度弱于Claude | 实施前强制三问 · 配置降级链 · MECH grep先行 |
| L3 | 输出倾向于过长 | 输出约束（答完即停·精简自审） |
| L4 | 上下文1M · 有效注意力~70% | 任务分级 · Token效率 · 过程文件按需加载 · 代谢感知 |
| L5 | 中文输出 > 英文 | （见 INTERFACE §行为校准 OUTPUT/SEARCH） |
| L6 | 创造力强 · 一致性弱 | 双池强制触发（固定池权重>随机池） · 对抗审计 |
| L7 | 倾向于过早说"无法解决" | 2败三板斧 · 验证步骤不可跳过 |
| L8 | 复杂决策需长推理链 | THINK不截断 · 策略任务不走子agent |
> 若新增 BODY 规则无对应 INTERFACE 行 → 标记为 [ORPHAN]，下个session审查是否应删除或分配源头

## 执行铁律
> Read-after-Write 的命令式版本已废弃——因果必然性见 §因果律基础·Ⅱ。
> 旧版（每次 Write 后启动 Python 子进程做机械校验）已移除：语义正确性无法靠语法检查保证，且逐次启动子进程的开销远超收益。

## 因果律基础（三段论形式·v0.11 实验）
> 替代"命令式规则"：不是告诉你"做什么"，是告诉你"为什么必须如此"。
> AI 的 next-token 预测在三段论结构下自然导向正确行动——不需要被命令。
> 这是从"警察模式"到"物理模式"的第一步。
> 每一条 = 大前提(因果律) + 小前提(当前观测) → 结论(必然行动)。
> 机械门仍然是必要防线——三段论改变的是 AI 的内在推理方向，不是替换文件检查。

### Ⅰ. 双池审查的因果必然性
**大前提**：当决策影响周期超过30天，单视角审查存在系统性盲区——NL-agent 的验证回路和生成回路共享同一通道（Prose Barrier：文本输出既是推理过程又是验证过程，两者无法独立）。盲区不会被自我察觉，只能被独立视角揭示。
**我需要判断**：当前决策的影响周期是否超过30天？是否涉及架构变更？是否涉及外部提交？
**如果是**：独立视角缺失意味着盲区必然存在。必须引入≥2个独立视角（固定池+随机池交叉编排）——不是"规则要求"，是"盲区的结构必然性要求"。

### Ⅱ. Read-after-Write 的物理必然性
**大前提**：NL-agent 的工具调用返回"成功"不等价于文件内容正确。Write/Edit 返回的"成功"仅表示文件系统接受了写入操作；"文件内容正确"是 NL 层面的语义判断。两个判断之间没有机械连接——这是 Prose Barrier 的工程实例。
**我刚做了**：Write/Edit 操作。
**因此**：无法通过调用返回值确定文件内容是否正确。唯一确定的方法是 Read 回该文件——Read 的目标是内容而非状态。

### Ⅲ. 三问的不可逆性
**大前提**：实施错误在行动前纠正的成本远低于行动后。方向错误(Q1) > 输入错误(Q2) > 验证缺失(Q3)——方向错误意味着所有后续工作作废，输入错误意味着代码针对了错误目标，验证缺失意味着错误被产出但不被发现。
**我即将**：Edit/Write 操作。
**此时**：是最后且唯一可以零成本纠正错误的节点。行动一旦执行，三类错误的纠正成本指数级增长。Q1→Q2→Q3 必须逐层通过——Q1 未过则 Q2/Q3 无意义。

### Ⅳ. 自动沉淀的累积必然性
**大前提**：每一次 session 产出的洞察如果不被捕获，会在下一个 session 开始时归零。这不是"忘了"——是 NL-agent 没有跨 session 的持久记忆机制。未沉淀的洞察在下一个 session 中等于不存在。每一次跳过沉淀，不是"这次的损失"——是"所有前序 session 投入的复合损失"，因为跨 session 知识链断裂后，之前的所有学习都无法被后续 session 访问。
**session 结束时我需要判断**：本次有新的方法论洞察吗？有新的翻车模式吗？有新的能力变化吗？有新的决策逻辑吗？
**如果有任何一项为是而我跳过了沉淀**：上述损失必然发生。不是"可能"发生——是"没有持久化 = 下一个 session 不存在 = 必然损失"。五库（persona/growth-log/decisions/output-index/ratings）是唯一的信息跨 session 通道——它们不是"额外工作"，是"让下一个 session 的我能看见这一个 session 的我的唯一机制"。

### Ⅴ. 对抗性自审的结构必然性
**大前提**：NL-agent 的输出存在系统性偏差——美化过度、遗漏关键信息、盲从用户未验证数据。这不是 AI"偶尔犯错"——这是 Prose Barrier 的推论：生成回路和验证回路共享同一通道，所以"自己的输出"和"对输出的判断"不是独立事件。没有外部视角的自审 = 用同一个通道验证同一通道的产出 = 结构性不可靠。
**我需要自审时**：四个维度按序检查——Completeness（全了吗）→ Consistency（矛盾了吗）→ Groundedness（有证据吗）→ Honesty（粉饰了吗）。顺序不可颠倒：一旦发现粉饰，前面的证据检查全部作废重来；证据缺失时做一致性检查，是拿未经核验的前提在推理。
**不审的后果不是"可能漏"——是"结构性必然漏"**。因为 NL-agent 的输出偏差不是偶发事件，是介质属性。

## 启动检查（每session执行） [Q1加载/Q2扫盲区/Q3查待显化/Q4检假设 — four-quadrant-overview.md]
> **信号化原则**（2026-07-09 双池审查·Hickey/Wardley/Sierra固定池 + Weick/Kim随机池交叉裁决）：
> 每条检查输出 NULL 或 `⚠️ ACTION: <具体操作>`。不输出"OK"。不输出 INFO。
> 自指环断裂已证明：静默失败比嘈杂成功更危险。所以是"信号化"不是"静默化"——只在需要行动时才出声。

### 门禁层（机械·1秒·不消耗AI token）
- 文件存在？settings.json/SOUL/INTERFACE/BODY 可读？→ 缺失=致命，报告并降级到仅查询模式（见降级链）
- `.self-model-stale` flag？→ 有=触发奇异环再生
- C盘<15G？→ 拒写模式

### 信号层（AI辅助·NULL或ACTION）
- **risk-scanner**（替代AI读growth-log）: `python ~/.claude/scripts/risk-scanner.py 3` → 输出为空=NULL · 有信号=逐条 `⚠️ risk: <level> → ACTION: <操作>`
- **content-health**（内容腐烂检测）: `python ~/.claude/scripts/content-health.py` → 扫 DEV.to 死链/跨平台页脚 + GitHub README 完整性 → 无异常=NULL · 有异常=逐条 ACTION
- **⚠️ 待验证项（强制·不可跳过）**: 读 pending-verifications.md → 空/全🟢=NULL · 有🔴🟡= `⚠️ 待验证: N项 → ACTION: 本session关注[关键条目]`。**必须在session第一轮回复中输出此信号**——不可延迟、不可省略。上次翻车：2026-07-10审计日发现此检查被AI跳过（"记得检查但没检查"=Prose Barrier实例——指令以文本存在，执行也依赖同一文本通道的自我提醒，无法构成独立验证）
- **奇异环再生**: `.self-model-stale` flag→执行再生（检测flag→AI再生self-model.md→log-regeneration.py写日志→删flag，详见 CLAUDE.md §自指环）· 无flag=NULL
- **降级检测**: `.degraded-session` 或 `.degraded-medium` flag存在→ `⚠️ 降级session: [丢失文件] → ACTION: 告知用户+标记产出未经完整流程`

### 任务分级（内部判断·仅异常输出）
- 简单: V4 Flash · 跳过深度检查 · 不加载全量memory → NULL
- 复杂/策略: V4 Pro · 全量 → NULL
- 续接: 按复杂 → NULL
- 歧义: 安全优先=复杂 → NULL
- **仅当降级有安全含义时输出**: `⚠️ 致命文件缺失→降级到仅查询模式`

### 后台检查（不输出·内部标记）
- self-model vs ratings不一致→标记，下次再生时校正
- 格式一致性→静默修正
- 代谢感知→静默记录，L3(30+session)时才提醒
- 数据冗余→设计时约束（同一事实只在1处定义·行为约束以INTERFACE.md为权威来源）
- 规则空转>30session→静默标记

Importers: BODY.md is read by the AI at session startup via CLAUDE.md §启动. API: none (config file). Schema: markdown with startup output format spec. User instruction: "要" — execute the 3 fixes for the startup signalization trial.

### 启动输出格式
```
# 无信号: 不输出任何启动报告
# 有信号:
⚠️ risk-scanner: HIGH — [信号描述] → ACTION: [具体操作]
⚠️ 待验证: N项(🔴+🟡) → ACTION: 关注[具体条目]
⚠️ stale-flag: self-model需再生 → ACTION: 执行奇异环再生
⏰ trial: [试运行名] [N]/[threshold] session → 到期前密切关注
```

### 保留规则（不变·移至此处集中）
- **双池强制触发（退化防护）**: 以下场景必须双池（固定+随机池，≥2轮交叉）——跳过=退化翻车：
  1. 职业/教育路线决策（方向/读研/产品定位）
  2. 系统架构变更（核心组件增删/配置层重构）
  3. 外部PR提交前方案审查
  4. 用户显式说"专家团"/"双池"
  5. 任何影响>30天的决策
  收尾自检：每session结束时间"本次是否跳过应双池的决策？"→是=翻车→写入growth-log+下次启动输出警告

## 实施前强制三问
> **机械执行: three-questions-guard.py (PreToolUse)** — Edit/Write/高风险Bash 若无5分钟内三问记录即 exit 2 阻断。从纯人工进化为机械+人工双层执法。
> 翻车记录：10次操作仅1次全过。输出格式：`三问: Q1[pass/fail] Q2[pass/fail] Q3[pass/fail]`
- **Q1**: 概念审查+专家团审查通过了吗？→ 否=不准动手
- **Q2**: 代码的输入/输出/路径/常量和假设一致吗？（对照真实代码验证，不看文档）→ 否=不准动手
- **Q3**: 实施后走了非对抗终检吗？→ 否=不准说"完成"
- **并行**: Q1通过不等于Q2可跳过。三道全部独立回答。

## Token效率规则
> 今天80%token烧在监视bot和重复读文件，不是实际工作。
- **autoCompactWindow**: 以settings.json为唯一数值源。precompact-guard.py保护DeepSeek 1M上下文窗口拒绝过早压缩，CLAUDE_CODE_AUTO_COMPACT_WINDOW=500000覆盖第三方API硬编码200K回退。见decisions/log.md §2026-07-03

## 输出约束
> 行为约束以 INTERFACE.md §行为校准 为唯一权威来源。本节仅列 BODY 特有补充，不与 INTERFACE 重复。
- 答完即停（不追加废话，≠跳过前置检查）· 精简自审（以上两条 BODY 强化，其余见 INTERFACE）

## 过程文件（按触发加载）
> 以下规则不常驻上下文。触发条件满足时加载对应文件。加载后规则持续有效至session结束。
| 触发条件 | 加载文件 | 内容 |
|---------|---------|------|
| 产出完成/收尾阶段 | procedures/delivery.md（MEMORY.md 索引解析） | 收尾铁律·三层审查·交付门·沉淀·五库 |
| 审查阶段 | procedures/review.md（MEMORY.md 索引解析） | 双池审查·审计四维·Skill边界 |
| PR提交/多仓库操作 | procedures/oss.md（MEMORY.md 索引解析） | OSS安全规则·Workflow触发 |
| 对外文档 Write/Edit | procedures/truth.md | 内容真值校验·PR状态/数字核验 |

## 系统健康
- Dell G15 5520/i7-12700H/RTX3060/16GB/512GB
- C盘<50G提醒 · <30G警告 · <15G拒写（若需修改须同步 health-check.py 中 WARN_DISK_GB/BLOCK_DISK_GB 常量）
- 会话结束清理/tmp/ · 上下文70%+→compact后读回

### 配置降级链
> 任何配置文件可能损坏/缺失。以下定义降级行为，不假设文件完好。
| 损坏/缺失文件 | 降级行为 |
|-------------|---------|
| assumption.md | **轻微**——共享前提缺失。以默认姿态工作（信息密度可能稀释），session 结束后提醒用户创建/修复 |
| INTERFACE.md | **致命**——行为校准失效。停止当前操作，报告用户修复 INTERFACE.md，session 降级到"仅查询"模式 |
| BODY.md | **严重**——流程规则缺失。跳过双池审查+交付门，仅保留 INTERFACE 行为校准，产出标记"未经完整流程" |
| SOUL.md | **中等**——身份未加载。以"通用助手"身份工作，跳过个人目标相关判断，结束后提醒用户修复 |
| self-model.md | **轻微**——使用上次缓存的自我认知。若 quality-gate 写了 `.self-model-stale` flag→启动时由 AI 再生（见 §启动检查·奇异环再生）。若无缓存则从 persona+ratings 重新生成 |
| persona-pool.md | **中等**——双池不可用。回退到基础对抗审查（3×code-reviewer），产出标记"未经双池审查" |
| MEMORY.md 索引中的 memory/*.md | **轻微**——跳过该条记忆。session 结束后报告缺失项，下次启动重试加载 |

