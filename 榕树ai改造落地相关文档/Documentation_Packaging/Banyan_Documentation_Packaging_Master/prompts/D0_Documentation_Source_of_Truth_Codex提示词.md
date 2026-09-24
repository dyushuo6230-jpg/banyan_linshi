# Banyan Documentation Packaging — D0 Source of Truth

目标：只建立文档事实底座，不写大批正文，不修改 Banyan Core。

请基于当前已经完成的 Framework / Stage20 accepted evidence，定点盘点：

```text
实际 CLI
实际 WebUI 页面
实际 Runtime API
实际 Adapter
实际 Capability / Skill
实际 Workflow
实际 Role
实际 Status / Enum
实际 ID / Variable
实际关键文档类型
实际目录
实际 Project Instance
```

输出：

```text
banyan-framework/docs/DOCUMENTATION_SOURCE_OF_TRUTH.yaml
banyan-framework/docs/DOCUMENTATION_INVENTORY.md
```

要求：
1. 只记录实际存在/已冻结的内容。
2. 不凭空补枚举、命令、Skill、Workflow。
3. 若用户期望与当前实现不同，记录为 DOC-GAP-CANDIDATE。
4. 不修改 Runtime / Policy / Permission / Git / .banyan。
5. 不迁移 docs/project。
6. 不启动 WebUI Help Center 实现。
7. 完成后停止，等待 D1。
