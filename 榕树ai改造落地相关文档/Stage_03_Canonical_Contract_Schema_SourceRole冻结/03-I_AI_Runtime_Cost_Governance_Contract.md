# 03-I：AI Runtime Cost Governance Contract

## 本阶段冻结治理接口

```text
task_class
execution_mode
model_capability_class
budget_policy
batchability
cacheability
context_strategy
escalation_condition
quality_gate
telemetry
```

## Execution Modes

```text
FULL_AUDIT
ENGINEERING
BATCH_WORKER
HUMAN_DECISION
```

## Model Routing

使用“能力等级”而不是具体模型名：

```text
LOW_COST_WORKER
STANDARD_ENGINEERING
HIGH_REASONING
MAX_REASONING
```

实际 Provider/模型以后绑定。

## Token / Cost

冻结：

```text
预算必须存在
超预算必须降级/分批/请求升级
重复 Evidence 优先缓存/索引
```

不冻结具体百分比或价格。

## 默认省 Token 策略

```text
Index first
Summary second
Evidence on demand
No full rescan unless freshness invalid
```
