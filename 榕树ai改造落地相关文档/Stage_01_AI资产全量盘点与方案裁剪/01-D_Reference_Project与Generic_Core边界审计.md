# 01-D：Reference Project 与 Generic Core 边界审计

## 1. 原则

Reference Project：

```text
验证 Framework
≠ 拥有 Framework
```

本阶段只产出 Candidate，不冻结架构。

## 2. 重点污染源

检查候选能力是否依赖：

```text
x_shop_server 名称
当前业务域
当前 docs/project
当前 tools
当前 .cursor
当前端口/URL
当前 DEC/ADR/CR 编号
当前五端/业态
当前项目状态
当前历史目录约定
```

## 3. 输出判断

每个高价值 Candidate：

```yaml
candidate_boundary:
  - GENERIC_CORE_CANDIDATE
  - PROJECT_ONLY_CANDIDATE
  - PROVIDER_CANDIDATE
  - COMPATIBILITY_CANDIDATE

purity_risk:
project_specific_dependencies:
generalizable_semantics:
cross_project_evidence:
required_abstraction:
candidate_owner_stage:
```

## 4. Existing Project Preserve In Place

Stage 02 Handoff 必须携带：

```text
EXISTING_PROJECT -> PRESERVE_IN_PLACE
BANYAN -> DISCOVER + MAP + CLASSIFY
RELAYOUT -> EXPLICIT MIGRATION ONLY
```

Stage 01 不以搬目录作为“去项目化”。

## 5. Gate

Stage 01 可以存在：

```text
UNKNOWN_CORE_VS_PROJECT_BOUNDARY
```

但必须：

- 风险不是 HIGH；
- 有 candidate owner；
- 明确交给 Stage 02。

Stage 02 最终要求该类未知归零。
