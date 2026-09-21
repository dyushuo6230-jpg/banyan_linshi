# Stage 02 — Capability → Contract → Provider → Artifact → Runtime

状态：**设计候选；不创建运行实现、不冻结正式 Schema**。证据来自 Stage 01 的 35 项能力、1026 项资产、425 项正式/派生产物候选和 289 项运行记录。逐项映射见 `CAPABILITY_MAPPING_WORKBOOK.yaml`，物理资产和产物分别见两个 Boundary Map。

## 1. Capability

稳定单元是用户可观察的工程行为及其守卫和失败语义，不是某个 prompt 文件或目录。每项能力保留 Stage 01 的 ID、旧来源、输入/输出、门禁、失败方式；即使最终不是 Core，能力也不因实现混乱被删除。Stage 01 的 21/2/9/3 是候选分类，不是移植性证明。

## 2. Contract

候选接口输入：`capability_id`、项目上下文引用、事实来源与版本、请求动作、访问/授权证据、预算约束。输出：有来源和状态的结果、守卫决策、失败类型、追踪引用。只读与可能写入的能力必须显式区分。草拟失败类别：`SOURCE_UNVERIFIED`、`STALE_AUTHORITY`、`DECISION_REQUIRED`、`PERMISSION_DENIED`、`BUDGET_EXCEEDED`、`PROVIDER_UNAVAILABLE`、`PARTIAL_RESULT`、`VALIDATION_FAILED`。具体字段、编码、幂等键与版本由 Stage 03/05 定义，本阶段不冻结。

高影响变更必须携带用户决策证据；首次选择或模型推荐都不等于应用授权。项目级数字、路径、端口、业态和 G 阶段编号通过 Project Instance 映射注入，不能成为通用接口常量。

## 3. Provider

Provider 只能通过受限端口取得项目事实、读写正式文档、运行设计工具、与编辑器交互或访问模型。其具体工具路径和产品名不得渗入 Core。当前 AnyDesign 九项能力是设计 Provider 候选；Cursor 规则和旧 v3.1 用兼容层读入。模型、Git 和人工确认也需要端口，但没有任何 Stage 02 实现或默认写权限。

## 4. Artifact

正式 Canonical 候选、Derived、Operational 与旧来源分别标注权威性和生命周期。正式文档继续原位；派生产物记录输入/消费者/版本/重建证据；运行记录保留 in_progress、叫停、回退等状态。未知 AI 作者身份和未经证明的精确重建能力保持 UNKNOWN。Stage 03 冻结 Source Role、Schema、引用完整性时应消费 `ARTIFACT_BOUNDARY_MAP.jsonl`，不得依本阶段候选删除文件或把旧 ID 挂新主题。

## 5. Runtime

候选 Runtime 负责按任务风险路由、预算与模式选择、阶段门禁、暂停与恢复、观察成本与结果。状态推进以正式源和有效授权为依据；Provider 执行结果必须经过 Contract 校验才可发布或写正式真源。Full Audit、Engineering、Batch Worker、Human Decision 四种执行模式的成本策略见 `AI_RUNTIME_COST_GOVERNANCE_DESIGN.md`。没有启动 Runtime，也没有模型调用。

## 边界不变量

1. Existing Project → `PRESERVE_IN_PLACE`；Banyan → `DISCOVER + MAP + DESIGN`；重新布局只能 `EXPLICIT_MIGRATION_ONLY`。Stage 01 Handoff 的 `DISCOVER + MAP + CLASSIFY` 是已完成发现阶段，本阶段的 DESIGN 只增加候选分析，不改变原约束。
2. 项目事实由 Project Instance 持有。Core 使用来源引用和适用性，不复制项目真源；兼容层也不成为第二个可写真源。
3. 13 份本地环境配置与其余 Secret 继续 metadata-only；本阶段未读、未复制、未 Hash、未修改、未删除、未提交。
4. 35 项能力全部保留候选归宿；0 项因不通用而退役。迁移与激活需各 Owner Stage 验证。
5. 本设计不等于跨项目可用性、性能、成本或安全已经测试通过。
