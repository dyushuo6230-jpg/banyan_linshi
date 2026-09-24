# Stage 02 Pre Design Guidance v1.10

## 目的

本文件用于指导 Stage 02：Banyan核心边界设计与架构抽象。

Stage 02 不执行迁移，不改变项目结构。

核心目标：

将 Stage 01 已发现的能力、资产和产物进行架构边界分析。

------------------------------------------------------------------------

## 输入

必须消费 Stage 01：

-   AI_ASSET_INVENTORY.jsonl
-   LEGACY_AI_CAPABILITY_INVENTORY.jsonl
-   AI_GENERATED_ARTIFACT_INVENTORY.jsonl
-   PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml
-   CORE_CANDIDATE_REPORT.yaml

禁止重新扫描整个仓库。

------------------------------------------------------------------------

## 核心原则

保留能力，不保留混乱实现。

允许：

-   抽象
-   接口化
-   重构
-   迁移规划

禁止：

-   删除有效能力
-   因无法通用而废弃能力
-   提前移动项目文件

------------------------------------------------------------------------

## 架构分析模型

Capability

↓

Contract

↓

Provider

↓

Artifact

↓

Runtime

------------------------------------------------------------------------

## 边界分类

每项能力分析：

1.  Banyan Core Candidate
2.  Project Instance Candidate
3.  Provider Candidate
4.  Compatibility Layer Candidate

本阶段不冻结最终结果。

------------------------------------------------------------------------

## 项目目录约束

Existing Project：

PRESERVE_IN_PLACE

Banyan：

DISCOVER + MAP + DESIGN

RELAYOUT：

EXPLICIT_MIGRATION_ONLY

------------------------------------------------------------------------

## AI Runtime Cost Governance

Stage 02 增加设计：

-   模型选择策略
-   Token预算
-   执行模式
-   批处理策略

不执行运行时开发。

------------------------------------------------------------------------

## 完成标准

输出：

-   Core边界建议
-   Project边界建议
-   Provider边界建议
-   冲突处理方案
-   下一阶段输入

完成后停止。
