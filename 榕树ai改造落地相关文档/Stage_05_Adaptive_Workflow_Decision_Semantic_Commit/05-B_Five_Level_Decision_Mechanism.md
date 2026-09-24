# 05-B Five-Level Decision Mechanism

```text
L0 AUTO_SAFE
L1 AUTO_WITH_TRACE
L2 PROPOSE_AND_CONTINUE_IF_POLICY_ALLOWS
L3 HUMAN_CONFIRMATION_REQUIRED
L4 BLOCKED_OR_OWNER_DECISION_REQUIRED
```

每一级必须有：

```text
entry criteria
allowed action
evidence requirement
escalation rule
fallback
```

任何级别都不能绕过 Secret / Protected Write / Git Identity 安全底线。
