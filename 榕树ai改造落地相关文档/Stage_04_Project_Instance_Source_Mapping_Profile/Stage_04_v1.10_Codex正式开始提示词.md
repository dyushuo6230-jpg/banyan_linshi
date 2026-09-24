# Stage 04 v1.10 — Codex 正式执行提示词（低 Token）

这是 Stage 04 正式执行，不是重跑 Stage 01/02/03。

当前阶段：

```text
Stage 04 — Project Instance / Source Mapping / Profile
```

## 1. 最小读取

先只读取：

```text
榕树ai改造落地相关文档/Stage_03_Canonical_Contract_Schema_SourceRole冻结/reviews/Stage_03_to_Stage_04_Gate_Review_v1.0.md
榕树ai改造落地相关文档/Stage_03_Canonical_Contract_Schema_SourceRole冻结/reviews/Stage_04_低Token输入索引_v1.0.md
榕树ai改造落地相关文档/Stage_04_Project_Instance_Source_Mapping_Profile/
```

再读取 Stage 03 Handoff 和低 Token 索引列出的 Frozen Contract/Schema。

## 2. 禁止

禁止：

```text
全仓重新扫描
重跑 Stage 01 Inventory
重做 Stage 02 Candidate Mapping
重写 Stage 03 Frozen Contract
移动项目目录
创建 project-sources/
修改业务代码
修改正式 docs/project
创建最终 banyan-framework
激活正式 .banyan
执行 Legacy Migration
修改 Git Identity
自动 commit
进入 Stage 05
```

## 3. 核心目标

基于 Stage 03 Frozen Contract 完成：

```text
Project Instance Schema
Project Instance Layout Contract
Source Mapping Schema / Registry
Source Role Binding
Project Overlay Binding
Variable Resolution
Project Profile
Contributor Profile
Provider Binding
Existing Project Adoption Contract
New Project Initialization Contract
Framework vs Project Instance Boundary
Bootstrap → Canonical Migration Design
Runtime / Index / Trace / Generated location contract
```

## 4. Existing Project

必须：

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
```

Project Sources 是逻辑集合，不是物理包装目录。

禁止要求：

```text
现有源码搬入 project-sources/
docs/tools/code 统一搬家
```

## 5. Generic Core

Generic Core 中不得出现当前项目业务内容、业务名称、固定目录、端口或人员信息。

项目差异只能进入：

```text
Project Instance
Source Mapping
Overlay
Profile
Variable Binding
Provider Binding
```

## 6. Contributor Profile

只允许：

```text
display_name
status
note
```

Key 使用实际 Git identity。

禁止：

```text
Profile 授权
自动合并 Git identities
猜测物理操作者
固定前后端/模块职责
```

## 7. Secret

13 个配置继续 metadata-only：

```text
不读正文
不复制
不 Hash
不修改
不删除
不移动
不提交
```

Recovery 仍为 `PARTIAL_APPROVED`。

## 8. Evidence on Demand

只有发生：

```text
CONTRACT_AMBIGUITY
MISSING_BINDING
PROJECT_MAPPING_COLLISION
PROVIDER_PORT_GAP
ACTIVATION_BLOCKER
```

才定点回读 Stage 02/01 Evidence。

## 9. Validation

执行 V04-01～V04-20。

硬指标全部必须为 0：

```text
UNMAPPED_SOURCE_ROLE
SOURCE_MAPPING_WITHOUT_ROLE
PROJECT_SPECIFIC_VALUE_IN_GENERIC_CORE_SCHEMA
PHYSICAL_RELAYOUT_REQUIRED_BY_DEFAULT
PROFILE_FIELD_USED_AS_AUTHORIZATION
UNKNOWN_VARIABLE_SILENTLY_DEFAULTED
```

## 10. 写入范围

仅允许：

```text
.banyan-refactor/stages/04/${RUN_ID}/**
.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml
.banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml
```

## 11. 完成后

生成：

```text
ACCEPTANCE_REPORT.md
evidence/NEXT_STAGE_HANDOFF.yaml
```

更新 Bootstrap Register / Trace。

完成 Stage 04 后立即停止，不进入 Stage 05。

最后汇报：

```text
1. Stage Status
2. Low-Token Verification
3. Project Instance Schema
4. Project Instance Layout Contract
5. Source Mapping / Role Coverage
6. Project Overlay / Variable Resolution
7. Project / Contributor Profile
8. Provider Binding
9. Existing Project Adoption
10. New Project Initialization
11. Framework vs Project Instance Boundary
12. Bootstrap → Canonical Migration Design
13. Runtime/Index/Trace/Generated Locations
14. Open Risks
15. V04-01～V04-20
16. Hard Metrics
17. Actual Writes / Protected Areas
18. Bootstrap Register / Trace
19. NEXT_STAGE_HANDOFF
20. Stage 05 Entry Gate
```
