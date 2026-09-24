# Banyan R1 — Artifact Migration Completion Pack v1.0

## 本轮目标

R1 在 R0 已完成 Framework Self-Containment 的基础上，正式完成：

```text
Legacy v3.1
+
Accepted / Frozen Banyan Refactor Additions
+
Current Implemented Runtime Facts
        ↓
Framework-native Artifact Migration
```

重点对象：

- Role
- Policy
- Skill
- Workflow
- State
- Template
- Decision Protocol
- Context / Recovery
- Compatibility

R1 的目标不是“多造文件”，而是让已经存在的 Legacy 语义与后续已冻结设计，进入 Banyan 的正式 Artifact / Registry / Contract 体系，并保留 provenance、compatibility 和 implementation status。

---

## 放置位置

建议解压到：

```text
榕树ai改造落地相关文档/
└── Documentation_Packaging/
    └── Banyan_R1_Artifact_Migration_Completion_Pack_v1.0/
```

---

## 使用顺序

1. 新开 Codex 窗口。
2. 读取：
   `prompts/R1_Codex正式施工提示词.md`
3. 严格只执行 R1。
4. 完成后停止，不进入 R2/R3。
5. 把以下内容发回 ChatGPT：
   - `R1_ARTIFACT_MIGRATION_ACCEPTANCE_REPORT.md`
   - `R1_ARTIFACT_MIGRATION_MATRIX.yaml`
   - `R1_NEW_PROPOSAL_REGISTER.yaml`
   - Codex 最终总结
   - 如有 Human Decisions Required，一并发回。

---

## 核心原则

```text
No-loss
No silent invention
No semantic drift
No docs-as-runtime
No token-saving by forgetting provenance
```

特别要求：

```text
TOKEN_EFFICIENCY_MUST_NOT_REDUCE_GOVERNANCE_FIDELITY
```

省 Token 可以减少重复读取，但不能丢失来源、状态、决策、兼容性、治理约束。
