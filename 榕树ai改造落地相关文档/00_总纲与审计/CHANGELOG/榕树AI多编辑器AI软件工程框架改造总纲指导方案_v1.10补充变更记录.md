# 榕树AI多编辑器AI软件工程框架改造总纲指导方案 v1.10 补充变更记录

## 变更目的

基于 Stage 01 实际执行结果，对原 v1.9.1 总纲增加运行治理能力。

本次不是重构旧设计，而是在原设计基础上的增强。

# 新增一：AI Runtime Cost Governance

## 背景

真实 Stage 执行发现：

大量成本来自：

-   上下文读取
-   重复分析
-   大规模 Discovery

因此增加 AI 资源调度层。

## 目标

让 Banyan 支持：

-   任务识别
-   模型选择
-   Token预算
-   执行模式切换

# 新增二：AI Task Routing

任务类型：

-   Discovery
-   Classification
-   Migration
-   Architecture
-   Audit
-   Documentation
-   Coding

根据任务复杂度选择：

-   批处理
-   普通分析
-   高级推理

# 新增三：Capability Contract 化

原有能力不删除。

统一抽象：

Capability

↓

Contract

↓

Provider

↓

Artifact

↓

Runtime

# 新增四：Stage执行模式

增加：

## Full Audit Mode

用于：

-   安全基线
-   Gate Review
-   最终审计

## Engineering Mode

用于：

-   普通开发
-   资产分析
-   文档生成

## Batch Worker Mode

用于：

-   分类
-   索引
-   批量处理

## Human Decision Mode

用于：

-   架构选择
-   删除判断
-   冻结决策

# 保留声明

以下原有设计全部保留：

-   PRD体系
-   OpenSpec融合
-   变更稿模式
-   Parallel Draft
-   多编辑器支持
-   Git身份体系
-   WebUI规划
-   Progress系统
-   Handover系统
-   UI规范体系
-   Plain Document体系
-   AI能力迁移体系

v1.10 仅增加治理能力，不替代已有能力。
