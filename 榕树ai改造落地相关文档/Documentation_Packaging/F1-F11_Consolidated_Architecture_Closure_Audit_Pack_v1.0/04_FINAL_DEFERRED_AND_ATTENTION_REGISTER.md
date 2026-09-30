# Final Deferred & Attention Register

## 1. Attention Register

### ATTENTION-05 — F1～F11 Unified Deferred Register

目标：

> 在 F12 正式开始前，将跨 F1～F11 的 Material Deferred 统一归档、去重、确认 Owner / Trigger / Guard。

状态：

```text
OPEN_NON_BLOCKING
```

### ATTENTION-06 — F1～F8 v1.1 Direct Evidence Visibility

当前已确认 F1～F8 v1.1 是 Current Effective Baseline，但当前审计窗口没有逐文件直接读取全部 v1.1 Freeze Baseline 内容。

分类：

```text
SOURCE_VISIBILITY
PACKAGING
DISCOVERABILITY
NON_BLOCKING
```

不得解释为：

```text
Architecture Gap
User upload failure
Freeze invalid
```

### ATTENTION-07 — Deferred → F12 Engineering Eligibility Classification

Pre-F12 / F12 期间需要把 Deferred 分类为：

```text
当前 F12 必须解决
F12 可工程化但不施工
Implementation Detail Later
Requires Separate Human Decision
Migration / Cutover Deferred
Future Capability Reserved
Not Applicable to Current F12
```

Exact Enum 尚未冻结。

### ATTENTION-08 — Historical F12 Stage-label / Future-owner Reconciliation

历史 PreF9 材料中曾有：

```text
F12 → Migration / Retirement
```

而当前规划中的未来 F12 倾向：

```text
Architecture → Engineering Baseline
+
Control-Surface / WebUI Engineering Baseline
```

因此必须在正式 F12 入口完成 Stage Label / Responsibility Reconciliation。

该项：

```text
NON_BLOCKING
```

并且：

```text
Historical F12 reference
!= Current F12 automatic authority
```

## 2. Deferred Common Contract

Material Deferred 至少应保持：

```text
Subject / Topic
Deferred Question
Rationale
Declaring Owner
Future Owner
Trigger
Preconditions
Must-Happen-Before
Forbidden-Before-Resolution
Expected Output
Authority / Decision Requirement
Dependencies
Status
Provenance
Closure / Supersession
```

继续保持：

```text
Deferred != Undefined
Deferred != Forgotten
Deferred != Unowned
Deferred != Authorized
Deferred Obligation != Backlog Task
Deferred Obligation != Implementation Task
Future Owner != Current Authorization
Trigger Reached != Work Authorized
```

## 3. PHYSICAL_STORE_TOPOLOGY

继续保持为受治理 Deferred。

在其合法解决前：

```text
SQLite Physical Schema = NOT_FROZEN
```

并且在触碰适用 Must-Happen-Before 前必须完成对应 Resolution。
