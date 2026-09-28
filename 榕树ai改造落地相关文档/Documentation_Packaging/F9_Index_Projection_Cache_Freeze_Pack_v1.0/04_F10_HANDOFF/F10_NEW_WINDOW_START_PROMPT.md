# F10 新窗口完整启动提示词

这是 Banyan / 榕树 AI 的连续架构治理工作。

当前正式状态：

```text
F1～F8 = 已冻结的上游架构基线
F9 = FINAL_FROZEN
F9 Final Approval = F9 FINAL ARCHITECTURE FREEZE HUMAN_APPROVED
F10 = 下一 Architecture Stage
```

请先读取我提供的 `Banyan_F9_Final_Freeze_Package_2026-09-28.zip`。

优先读取：

1. `00_README_START_HERE.md`
2. `01_FINAL_FREEZE/F9_FINAL_ARCHITECTURE_FREEZE_HUMAN_APPROVED.md`
3. `04_F10_HANDOFF/F9_TO_F10_EFFECTIVE_HANDOFF.md`
4. `04_F10_HANDOFF/F10_WORKING_HANDOVER_CHECKPOINT.md`
5. `05_GOVERNANCE_NOTES/EVIDENCE_RECONCILIATION_NOTE_01.md`

若某个 F9具体边界需要核对，再定向读取 `02_F9_APPROVED_DECISIONS/`，不要无目的全量重复扫描。

## 固定工作方法

进入 F10 前必须先执行“四源对账”：

1. F1～F8 当前正式冻结基线；
2. F9 Final Freeze Package；
3. 历史 F10 / Runtime / RP / Legacy Governance Evidence；
4. Current Project / Code / Technical Reality。

四源对账完成后，先用大白话系统讲清：

- F10总体要解决什么；
- 哪些不属于F10；
- F9向F10交了什么；
- Runtime Permission / Authorization Validation / Provider / Adapter / Execution / Retry / Pause / Resume 等边界应该如何讨论；
- 哪些确定性工作可以自动完成；
- 哪些真正需要人工决定；
- 哪些事项仍是 Deferred。

不要一开始就生成完整审批稿。

每个 F10 子主题继续固定流程：

```text
四源对账
→ 大白话系统说明
→ 说明具体需要决定什么
→ 举例
→ 讨论
→ 收敛
→ 完整审批稿
→ 我明确 HUMAN_APPROVED
→ 独立 Markdown 文件归档
```

普通的“好的”“下一步”“按建议继续”都不代表批准。

## 全局设计原则

按主题张弛有度使用，不机械套全部规则，也不允许欠设计：

- 灵活：允许组合、扩展、局部覆盖、演进；
- 职责清晰：Owner / Input / Output / State Boundary明确；
- Core可扩展：新增 Module / Rule / Provider / 技术栈不应推翻 Core；
- 高效：按 Scope / Profile / Index 定向加载；
- Truth / Rule / Implementation / Inference / Authority / State严格分离；
- 可靠自动路由 × 最小人工决策治理；
- 确定性工作自动完成；
- AI Autonomous Learning / Autonomous Optimization 不是当前能力。

## F9不可推翻的核心边界

```text
Index != Canonical Truth
Projection != Canonical Truth
Cache != Canonical Truth
Latest != Current Effective
Freshness != Authority
Potential Impact != Effective Invalidity
Rebuild != Re-resolution
Failure != Source Invalid
Candidate != Approved Deferred
Handoff != Authority Transfer
Later Stage != Higher Authority
```

F9的详细正式条文在包内 `02_F9_APPROVED_DECISIONS/`。

## Evidence Limitation

保留 `EVIDENCE-RECONCILIATION-NOTE-01`：

上游 Material Deferred Obligations 继续受原 Authority 管理，但 F9 Final Review 的当前证据集没有完整重现 14 条逐行 Register。

因此不得假装 `14/14 individually revalidated`，也不得重写、关闭、Waive、Extend 或删除这些上游 Obligation。

未来正式 Register 可用时，按原 Identity 对账 Current Relevance / Trigger / Owner / Supersession / Carry-forward。

## 当前硬禁止

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

F10 Architecture Stage Entry 不改变以上状态。

## 现在的第一步

请先完成 F10 四源对账，然后：

**系统讲清 F10 Overall Scope / Responsibility / Ownership Boundary，用大白话举例说明需要确定哪些问题，再开始讨论。**

不要直接进入 Implementation。
