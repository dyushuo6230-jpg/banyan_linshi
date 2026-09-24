# F6-D09 — 校准目标来源与 Target Resolution 冻结条文

- **Stage**: F6
- **Decision**: F6-D09
- **Group**: 02
- **Status**: HUMAN_APPROVED
- **Freeze Status**: Architecture Freeze PASS
- **Type**: UI Conformance / Target Resolution Governance
- **Date**: 2026-09-24

## 1. Session 必须先解析明确 Target，禁止边检查边猜

正式执行 UI 一致性校准前，必须至少明确：

- Scope
- Target
- Target Version / Revision
- Target Applicability

如果存在多个潜在目标且无法依据当前有效治理关系唯一解析，例如：

- 多张设计图；
- 多个 Design Package；
- 多个 UI_SPEC；
- 新旧来源冲突；
- 用户点名目标与 Current Effective Contract 冲突；

则不得由 AI、Runtime 或 Provider 自行挑选“看起来最新”“最像目标”或“置信度最高”的来源。

正确状态应进入：

```text
TARGET_UNRESOLVED
```

并显式报告冲突或缺失。

## 2. Current Effective UI Contract 是正式一致性验证的默认治理目标

当当前 Scope 已存在适用的：

```text
Current Effective UI_SPEC
/
Effective UI Contract
```

正式 UI 一致性验证默认以其作为治理目标。

保持以下语义边界：

```text
Design Source = Evidence
Design Package = Governed Design Target Package
UI_SPEC = Approved UI Construction Contract
Effective UI Contract = 当前任务 / 批次实际消费的 Current Effective UI Contract 快照
```

禁止新 PNG 或更新时间更晚的文件自动覆盖 Current Effective UI Contract。

正式保持：

```text
Latest != Current Effective
```

## 3. 用户可以显式指定 Design Source 作为本 Session 比较目标

用户可以在某次 UI 一致性校准会话中明确指定 PNG、JPG、Figma、墨刀、Prototype、AnyDesign Output 或其它可追踪 Design Source 作为本次 Session 的比较目标。

该目标应标识为：

```text
USER_DESIGNATED_SOURCE_TARGET
```

该 Session 可以执行：

```text
Actual
VS
User-Designated Source
```

并形成 Difference / Drift Candidate / Validation Evidence。

但：

```text
User-Designated Design Source != Approved UI_SPEC
```

不得因为被本次点名，就自动修改 Design Package、UI_SPEC 或其它 Canonical Truth。

如果用户点名 Design Source 与 Current Effective UI Contract 冲突，D09 必须显式报告：

```text
TARGET_CONFLICT
```

并同时列出各目标的来源、版本、Scope 与差异，不得静默选边。

## 4. Existing UI / Existing Code 默认属于 Actual Reality，而不是 Design Truth

现有页面、组件、代码、DOM、渲染结果和当前交互行为默认表达：

```text
Current Implementation Reality
```

正式保持：

```text
Existing Reality != Design Truth
```

当用户明确要求某些当前区域保持不变时，该区域可以成为：

```text
Protected Baseline
```

即：

```text
Existing Reality
+
Explicit Protection
=
Protected Baseline
```

Protected Baseline 用于防止无关漂移、扩大修改范围和回归，但不会自动升级为全局 Design Truth。

## 5. Target 必须执行 Freshness 检查

任何 Validation Target 在用于正式 PASS / FAIL 判断前，都必须验证其当前有效性。

目标至少允许区分：

```text
CURRENT
STALE
REVIEW_REQUIRED
SUPERSEDED
CONFLICTED
UNKNOWN
```

如果相关的 PRD、Approved Product Change、Design Package、UI_SPEC、Behavior Model、Design Token、Foundation、User Design Constraint 或上游冻结契约发生影响当前 Scope 的变更，则既有目标必须进入 Freshness / Impact 判断。

不得出现：

```text
代码完全符合旧目标
→ 自动判定当前 PASS
```

当 Target 已过期、冲突或无法确认当前有效时，应使用：

```text
TARGET_STALE
TARGET_RECONCILIATION_REQUIRED
VALIDATION_NOT_READY
PARTIAL_RESULT
TARGET_UNRESOLVED
```

或后续实现阶段定义的等价状态。

正式原则：

> 完全符合一个已经失效的目标，不等于当前正确。

## 6. Target Resolution 推荐链路

在用户没有为本 Session 明确指定特殊 Target 时，推荐解析链：

```text
Session Scope
→ Current Effective UI Contract
→ Governed Design Package
→ User-Designated Design Source
→ TARGET_UNRESOLVED
```

但该链路始终受 Authority、Current Effectiveness、Applicability、Scope、Version / Revision、Freshness、Conflict State 约束，不得退化为简单静态优先级或 latest wins。

## 7. 核心禁止项

D09 Target Resolution 禁止：

1. AI 猜测哪个设计源“更正确”；
2. newest file wins；
3. newest image wins；
4. closest screenshot wins；
5. AI confidence wins；
6. Existing UI 自动成为 Design Truth；
7. Design Source 自动升级为 UI_SPEC；
8. 用户点名图片自动改写 Canonical Truth；
9. 过期 Target 产生伪 PASS；
10. 目标冲突时静默选边。

## 8. 冻结结论

本组正式冻结：

1. Session 必须先明确 Target；
2. Target 不明确时进入 TARGET_UNRESOLVED；
3. Current Effective UI Contract 是正式一致性验证的默认治理目标；
4. Latest 不等于 Current Effective；
5. 用户可显式点名 Design Source 作为本 Session 比较目标；
6. User-Designated Source 不自动升级为 Approved UI Truth；
7. Target 冲突必须显式报告；
8. Existing UI / Existing Code 默认只是 Current Reality；
9. Existing Reality 仅在用户明确保护时可成为 Protected Baseline；
10. Target 必须执行 Freshness 检查；
11. 过期、冲突或失效 Target 不得产生伪 PASS；
12. Target Resolution 不得依赖 AI 自主猜测。

---

**HUMAN_APPROVED — 2026-09-24**
