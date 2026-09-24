# Stage 03 — VALIDATION AND ROLLBACK

| ID | 验证 | PASS 条件 |
|---|---|---|
| V03-01 | Upstream | Stage 02 Handoff/Seal 有效 |
| V03-02 | Low Token | 未重新做全仓 Discovery |
| V03-03 | Capability Coverage | 35/35 accounted |
| V03-04 | Contract Schema | 必填字段完整 |
| V03-05 | Failure Semantics | 无缺失 |
| V03-06 | Core Purity | Core Schema 无项目路径/业务硬编码 |
| V03-07 | Source Role | 每个 role 有 authority/freshness/conflict rule |
| V03-08 | Artifact Registry | identity/version/status/provenance/reference 完整 |
| V03-09 | Reference Integrity | supersession/deletion rules 明确 |
| V03-10 | Provider Port | Core 不绑定具体 Provider |
| V03-11 | Project Overlay | Project-specific 通过 Overlay/Mapping 进入 |
| V03-12 | Version/Status | 受控规则完整 |
| V03-13 | Provenance | 未知来源允许 UNKNOWN，不猜测 |
| V03-14 | Conflict | CON-001/002 未静默覆盖 |
| V03-15 | Bootstrap Lineage | 禁止 dual writable truth |
| V03-16 | Existing Layout | PRESERVE_IN_PLACE 已冻结 |
| V03-17 | Cost Governance | 接口冻结，未硬编码具体模型/价格阈值 |
| V03-18 | Secret Safety | Secret 正文零读取/复制/hash/写入 |
| V03-19 | Write Scope | 无业务/正式文档越界写 |
| V03-20 | Handoff | Register/Trace/Acceptance/Stage04 Handoff 完整 |

## 硬指标

```text
UNMAPPED_HIGH_VALUE_CAPABILITY = 0
UNOWNED_SCHEMA_COLLISION = 0
SOURCE_ROLE_WITHOUT_AUTHORITY_RULE = 0
CONTRACT_WITHOUT_FAILURE_SEMANTICS = 0
SILENT_CAPABILITY_DROP = 0
PROJECT_PATH_HARDCODED_IN_CORE_SCHEMA = 0
```

## Rollback

Stage 03 正常只写控制根。

失败：

```text
保留 Evidence
标记 BLOCKED/FAIL
不要用 destructive Git 操作
不要恢复/改写业务文件
```
