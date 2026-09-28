# F10 WORKING HANDOVER CHECKPOINT

## 1. Current Position

```text
F1～F8 = Frozen upstream architecture baseline
F9 = FINAL_FROZEN
F10 = NEXT ARCHITECTURE STAGE
```

F9 final approval:

```text
F9 FINAL ARCHITECTURE FREEZE HUMAN_APPROVED
```

---

## 2. Read First

按顺序读取：

1. `../00_README_START_HERE.md`
2. `../01_FINAL_FREEZE/F9_FINAL_ARCHITECTURE_FREEZE_HUMAN_APPROVED.md`
3. `F9_TO_F10_EFFECTIVE_HANDOFF.md`
4. `../03_FINAL_REVIEW/F9_FINAL_CROSS_TOPIC_REVIEW_RESULT.md`
5. `../05_GOVERNANCE_NOTES/EVIDENCE_RECONCILIATION_NOTE_01.md`
6. 需要核对具体边界时，再读取 `../02_F9_APPROVED_DECISIONS/` 对应 Decision。

不要新窗口一上来全量重读 D01～D12；按 Material Need 定向读取。

---

## 3. F9 Frozen Boundary

F9已经冻结：

- Index / Projection / Cache Truth Boundary；
- Indexed Subject / Metadata；
- Scope / Profile / Query Resolution；
- Context Selection / Assembly；
- Context Recovery；
- Freshness；
- Fingerprint / Change；
- Dependency / Impact；
- Cache / Projection / Rebuild；
- Failure / Fallback / Degraded；
- Deferred Obligation Discovery；
- F9→F10 Handoff。

F10不得重新设计这些 Owner Boundary，除非发现 Material Architecture Error，并走 Governed Patch。

---

## 4. F10 Immediate First Action

必须先做 **四源对账**：

```text
1. F1～F8 current frozen baseline
2. F9 Final Freeze Package
3. Historical F10 / Runtime / RP / legacy governance evidence
4. Current project / code / technical reality
```

然后先系统说明：

- F10到底解决什么；
- F10明确不解决什么；
- F9交给F10哪些状态；
- Runtime Permission / Execution / Provider / Adapter / Retry / Pause / Resume 等边界如何分 Owner；
- 哪些仍 Deferred；
- 哪些需要 Human Decision；
- 哪些确定性工作应该自动化。

不要直接写 F10 完整审批稿。

---

## 5. Fixed Working Method

每个 F10 子主题继续：

```text
四源对账
↓
大白话系统说明
↓
具体要确定什么
↓
举例
↓
讨论收敛
↓
完整审批稿
↓
用户明确 HUMAN_APPROVED
↓
独立 Markdown 归档
```

不得把普通“好的 / 下一步”当批准。

---

## 6. Design Principles

继续保持：

- 灵活，不把结构写死；
- Owner / Input / Output / State Boundary清晰；
- 新 Provider / Module / Rule 不要求推翻 Core；
- Scope / Profile / Index定向加载；
- Truth / Rule / Implementation / Inference / Authority / State分离；
- 可靠自动路由 × 最小人工决策；
- AI Autonomous Learning 不是当前能力。

---

## 7. Hard Prohibitions

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```

F10 Architecture Stage Entry 不改变这些状态。

---

## 8. Upstream Evidence Limitation

正式保留：

```text
EVIDENCE-RECONCILIATION-NOTE-01
```

不要声称上游 14 个 Material Deferred Obligations 已在 F9被 14/14 逐项重新核验。

获得正式 Register 后按原 Identity 做对账。

---

## 9. Next Exact Action

```text
Start F10
→ Four-source Reconciliation
→ F10 Overall Scope / Responsibility / Ownership discussion
```

不要直接进入 Implementation。

**END**
