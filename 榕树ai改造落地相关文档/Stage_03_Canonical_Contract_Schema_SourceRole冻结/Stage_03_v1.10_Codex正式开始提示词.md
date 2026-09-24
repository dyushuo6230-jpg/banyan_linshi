# Stage 03 v1.10 — Codex 正式开始提示词（低 Token）

这是 Stage 03 正式执行，不是重新运行 Stage 01/02。

当前阶段：

```text
Stage 03 — Canonical Contract / Schema / Source Role 冻结
```

## 1. 先读最小输入

先只读取：

```text
榕树ai改造落地相关文档/Stage_02_Banyan核心边界设计与架构抽象/reviews/Stage_02_to_Stage_03_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_02_Banyan核心边界设计与架构抽象/reviews/Stage_03_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_03_Canonical_Contract_Schema_SourceRole冻结/
```

然后从 `.banyan-refactor/stages/02/stage02-20260920T131746Z/` 读取低 Token 索引要求的 Stage 02 实际产物。

## 2. 禁止重新盘点

禁止：

```text
重新扫描整个 Repository
重新跑 100k+ 路径 Discovery
重新生成 1026 AI Asset Inventory
重新跑 Git 全历史
重新生成 Stage 02 Candidate Mapping
```

只有遇到：

```text
CONFLICT
LOW_CONFIDENCE
MISSING_EVIDENCE
SCHEMA_COLLISION
```

才按 `evidence_refs` 定点回读。

## 3. 上游事实

```text
Stage 02 = COMPLETED / PASS_CANDIDATE_DESIGN
Stage 03 Entry Gate = PASS_FOR_CONTRACT_DESIGN
35 capabilities
21 Core candidates
2 Project Instance candidates
9 Provider candidates
3 Compatibility candidates
```

Stage 02 Candidate 不是最终 Contract。

## 4. 本阶段必须完成

冻结：

```text
Canonical Contract Schema
Capability Contract Registry
Source Role Schema + Registry
Artifact Registry Schema
Provider Port Schema
Project Overlay Schema
Reference Integrity Contract
Version / Status / Provenance Rules
Bootstrap → Canonical State Contract
Existing Project Layout Preservation Contract
AI Runtime Cost Governance Contract
Contract Freeze Register
```

35 项能力必须 35/35 accounted。

## 5. Existing Project

正式遵守：

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
BANYAN = DISCOVER + MAP + CLASSIFY/DESIGN
RELAYOUT = EXPLICIT_MIGRATION_ONLY
```

不得为了 Schema 整理项目目录。

## 6. Secret

Stage 00/01/02 继承的 13 个配置继续：

```text
SECRET_METADATA_ONLY
不读正文
不 Hash 正文
不复制
不修改
不删除
不移动
不提交
```

恢复仍是 `PARTIAL_APPROVED`。

## 7. AI Runtime Cost Governance

只冻结治理 Contract，不冻结具体：

```text
模型厂商
模型名称
价格
固定 token 百分比
```

模型只用能力等级表示。

## 8. 两项 HIGH Conflict

`CON-001` / `CON-002` 不要静默选 winner。

只冻结：

```text
conflict representation
precedence/freshness contract
activation blocker
owner stage
```

## 9. 写入边界

只允许：

```text
.banyan-refactor/stages/03/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

禁止：

```text
业务代码
正式文档正文
Legacy rule/prompt/skill 正文
正式 .banyan 初始化
banyan-framework 最终物理创建
Git commit/stash/reset/clean
修改 Git Identity
进入 Stage 04
```

## 10. Validation

执行：

```text
V03-01 ～ V03-20
```

硬指标：

```text
UNMAPPED_HIGH_VALUE_CAPABILITY = 0
UNOWNED_SCHEMA_COLLISION = 0
SOURCE_ROLE_WITHOUT_AUTHORITY_RULE = 0
CONTRACT_WITHOUT_FAILURE_SEMANTICS = 0
SILENT_CAPABILITY_DROP = 0
PROJECT_PATH_HARDCODED_IN_CORE_SCHEMA = 0
```

## 11. 完成

生成真实：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap Register/Trace。

Stage 03 完成后立即停止，不进入 Stage 04。

最后只汇报：

```text
1. Stage Status
2. Low-Token Input Verification
3. 35 Capability Contract Coverage
4. Frozen Schemas / Contracts
5. Source Role / Authority Result
6. Provider Port / Project Overlay Result
7. Reference Integrity Result
8. Existing Project Layout Contract
9. AI Runtime Cost Governance Contract
10. CON-001 / CON-002 carry-over
11. V03-01～V03-20
12. Hard Metrics
13. Actual Writes
14. Protected Areas
15. Bootstrap Register / Trace
16. NEXT_STAGE_HANDOFF
17. Stage 04 Entry Gate
```
