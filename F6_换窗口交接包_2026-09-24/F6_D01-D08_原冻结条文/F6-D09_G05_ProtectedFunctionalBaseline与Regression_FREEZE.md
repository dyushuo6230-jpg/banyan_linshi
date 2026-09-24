# F6-D09 — G05 Protected Functional Baseline × Regression 冻结条文

- **Stage**: F6
- **Decision**: F6-D09
- **Group**: 05
- **Status**: HUMAN_APPROVED
- **Freeze Status**: Architecture Freeze PASS
- **Type**: UI Conformance / Functional Regression Governance
- **Date**: 2026-09-24

## 1. Visual Target 与 Protected Functional Baseline 必须分开

Visual Target 回答：

- 页面应该长什么样；
- 状态应该如何表现；
- 布局关系应该是什么；
- 视觉与交互表现应该符合什么目标。

Protected Functional Baseline 回答：

> 哪些原本合法且受保护的功能能力，不能被本次 UI 调整破坏。

Protected Functional Baseline 可以包含：

- API Integration
- Routing
- Permission
- Business Logic
- Business State
- Data Contract
- Persistence
- Upload Logic
- Delete Logic
- Pagination
- Query Behavior
- Validated Callback
- Accepted Interaction

例如素材管理弹框：

```text
Visual Target:
上传列表样式、进度圈、布局、间距

Protected Functional Baseline:
分片上传仍正常
断点续传仍正常
秒传仍正常
取消上传仍正常
上传成功状态仍正确
```

正式冻结：

```text
Visual Target
!=
Protected Functional Baseline
```

并且：

```text
Existing Function
```

不能仅因为当前代码中存在，就自动升级为 Protected Functional Baseline。

Protected Functional Baseline 应来自有效治理依据，例如：

- Approved Product Rule
- Approved Change
- Existing Contract
- Accepted Behavior
- Explicit User Protection
- 其它已被当前治理链认可的保护依据

---

## 2. UI PASS 不能覆盖 Functional Regression

视觉一致性通过，不代表本次变更整体有效。

例如：

```text
圆角 = PASS
间距 = PASS
渐变 = PASS
选中效果 = PASS
```

但：

```text
删除按钮调用错误 API = FAIL
```

则不得把整个 Session 判定为成功。

应分别记录：

```text
UI Conformance = PASS
Functional Regression = FAIL
```

正式冻结：

```text
Conformance Success
=
Required UI Conformance Satisfied
AND
Required Protected Regression Checks Satisfied
```

因此：

> 看起来正确，不等于改得正确。

---

## 3. Regression Scope 必须由 Impact 决定，不默认全量回归

回归验证不应默认每次执行整个项目的全量测试。

应采用：

```text
Changed Scope
↓
Dependency / Impact Resolution
↓
Protected Functional Baseline
↓
Minimum Sufficient Regression Scope
```

例如只修改：

```text
二级分类选中背景色
```

通常不需要验证与其无关的注册、退款、支付、权限体系等能力。

但如果修改：

```text
Shared Category Component
```

且该组件被多个页面复用，则其受影响调用方必须纳入 Impact Scope。

正式冻结：

```text
Regression Scope
=
Impact-driven
```

不得退化为：

```text
Always Full Regression
```

也不得退化为：

```text
Only Changed DOM
```

---

## 4. Minimum Sufficient Regression 不能为了速度漏掉必要检查

虽然 Regression Scope 应尽量精确，但以下范围只要实际受到影响，就不得为了速度排除：

- Authority-sensitive
- Security-sensitive
- Permission-sensitive
- Business-critical
- Explicitly Protected
- Contract-sensitive
- Impacted Data Behavior

例如 UI 调整涉及删除按钮的 DOM 结构，如果已经影响到删除绑定，则必须检查 Delete API 行为。

如果 UI 显隐逻辑涉及权限，则必须检查 Permission Regression。

正式冻结：

```text
Minimum Sufficient
!=
Minimum Possible
```

目标是：

> 只测必要的，但必要的一项都不能少。

---

## 5. Regression Finding 与 Visual Drift 必须分开记录

视觉偏离与功能回归必须保持不同语义。

例如：

```text
按钮位置偏 6px
→ LAYOUT_DRIFT
```

而：

```text
按钮点击后没有调用上传 API
→ FUNCTIONAL_REGRESSION
```

Regression Finding 至少允许区分：

```text
FUNCTIONAL_REGRESSION
INTERACTION_REGRESSION
ROUTING_REGRESSION
PERMISSION_REGRESSION
DATA_REGRESSION
INTEGRATION_REGRESSION
STATE_REGRESSION
```

未来可以扩展更多类别。

例如：

```text
D09-ISSUE-003
Classification = VISUAL_DRIFT
Risk = R1
```

与：

```text
D09-ISSUE-007
Classification = PERMISSION_REGRESSION
Risk = R3
```

必须走不同治理路径。

---

## 6. D09 只能发现 Regression，不能借 Regression 自主修业务

D09 对 Regression 可以执行：

- 发现；
- 采证；
- 定位 Affected Scope；
- 分类；
- 判断 Risk；
- 形成 Validation Result；
- 进入治理路由。

但 D09 不得因为发现回归，就自行：

- 重写 API；
- 修改权限；
- 修改数据契约；
- 修改业务逻辑；
- 替换路由；
- 修改 Canonical Product Truth；
- 修改 Frozen Contract。

特别是涉及：

- API
- Permission
- Data Contract
- Business Semantics
- Canonical Product Truth
- Frozen Contract

时，应进入：

```text
Regression Evidence
↓
Risk / Impact
↓
Governance Routing
↓
D10 或既有 Change / Decision Governance
```

不得形成：

```text
发现功能坏了
→ AI 顺手修一下
```

---

## 7. Protected Functional Baseline 本身也不能被静默改写

不能为了让回归检查通过，而把 Protected Functional Baseline 修改成当前实现状态。

如果发现 Baseline 已：

- 过期；
- 被新批准规则取代；
- 与当前正式业务规则冲突；
- 适用范围不再成立；

则应进入：

```text
BASELINE_STALE
BASELINE_CONFLICT
RECONCILIATION_REQUIRED
```

而不是：

```text
当前代码是什么
→ Baseline 就改成什么
```

正式冻结：

```text
Protected Baseline
!=
Current Reality Auto-Sync
```

---

## 8. G05 完整保护链

```text
UI Repair / Changed Scope
        ↓
Impact Resolution
        ↓
Protected Functional Baseline
        ↓
Minimum Sufficient Regression Scope
        ↓
Regression Evidence
        ↓
UI Conformance Result
+
Regression Result
        ↓
只有都满足要求
才可认为本次验证成功
```

---

## 9. 核心冻结边界

G05 正式冻结：

```text
Visual PASS
!=
Repair Success

Visual Target
!=
Functional Baseline

Minimum Sufficient
!=
Skip Important Checks

Regression Detection
!=
Business Rewrite Authority

Protected Baseline
!=
Current Reality Auto-Sync
```

---

## 10. 冻结结论

本组正式冻结：

1. Visual Target 与 Protected Functional Baseline 必须分离；
2. Existing Function 不因当前存在而自动成为 Protected Functional Baseline；
3. Protected Functional Baseline 必须有有效治理依据；
4. UI PASS 不能覆盖 Functional Regression；
5. Conformance Success 必须同时满足所需 UI Conformance 与所需 Regression Checks；
6. Regression Scope 必须由 Impact 驱动；
7. 不默认全量回归，也不能只检查 Changed DOM；
8. Minimum Sufficient Regression 不得漏掉受影响的重要功能；
9. Regression Finding 与 Visual Drift 必须分开记录；
10. Regression Classification 必须允许扩展；
11. D09 只能发现、判断和路由 Regression；
12. D09 不获得 Business Rewrite Authority；
13. Protected Functional Baseline 不得为了让验证通过而静默改写；
14. Baseline 过期或冲突时必须进入显式治理状态。

---

**HUMAN_APPROVED — 2026-09-24**
