# F6_NEXT_WINDOW_START_HERE

在新的 ChatGPT 窗口中，把本文件和另外两个 F6 交接文件上传，然后直接发送下面这段：

```text
继续 Banyan 架构冻结工作。

F1～F5 已完成并已经上传 Git，不需要重新设计。
请读取我上传的：
1. F6_WORKING_HANDOVER_CHECKPOINT.md
2. F6_CONFIRMED_FREEZE_PACK.md
3. F6_NEXT_WINDOW_START_HERE.md

当前状态：
F6-D01～D08 已 HUMAN_APPROVED / Architecture Freeze PASS。
Implementation 仍未授权。
F6-D09 尚未确认。

最近我们补充讨论了 UI Conformance / 视觉循环：
- 顶层使用 UI Conformance Session（UI 一致性校准会话）；
- Visual Repair Loop 只是 VISUAL + REPAIR compatibility profile；
- 默认 OFF / ON_DEMAND / NON_BLOCKING；
- 可点名 App / Page / Region / Component / State / Interaction；
- INSPECT 与 REPAIR 分开；
- Repair Target 优先来自 Current Effective UI_SPEC，其次 Governed Design Package，再次用户明确点名 Design Source；
- 只有 PRD、没有足够 UI Target 时不能直接 Repair，必须先 Design Formation；
- Existing UI 默认是 Current Reality，明确要求时可作为 Protected Baseline；
- Repair 必须保护已实现功能；
- 每次 Repair 明确 Target Scope / Allowed Mutation Scope / Protected Functional Baseline；
- 不得借视觉修复修改 API、业务逻辑、权限、业务状态、数据契约；
- 目标要求当前不存在业务能力时，形成 FUNCTIONAL_GAP / BUSINESS_AFFECTING_CHANGE；
- Repair 是局部收敛，不是页面重写；
- 每轮 Repair 后既做 UI Revalidation，也做必要 Protected Function Regression Check。

请不要直接沿用旧 F6-D09。
先把以上新结论与旧 D09 候选重新对账，
输出一版完整新版 F6-D09 让我确认。

D09 确认后再进入：
F6-D10 — Repair Governance × UI Conformance Action × Design-Code Synchronization。

不要重开 D01～D08。
不要进入 Implementation / Cursor Coding。
```
