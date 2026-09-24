# Banyan R0 Framework Self-Containment Remediation Pack v1.0

## 这是什么

R0 是 D1.5 审计后的第一轮真正 Framework Remediation（框架修复施工）。

目标只有一个：

> 让 `banyan-framework/` 自己携带、解释、校验并发布属于 Banyan Framework 的正式 Contract / Registry / Schema / Compatibility 定义，不再依赖 `.banyan-refactor/stages/**` 或施工文档才能知道框架“是什么”。

R0 不是：
- Role / Skill / Workflow 全部实现阶段；
- 自然语言自动编排阶段；
- Project Instance Final Activation；
- D2 / D3 文档编写阶段；
- WebUI Help Center 阶段。

R0 完成后，Framework 应该具备稳定的“正式定义落脚点”，为后续 R1 v3.1 Artifact Migration Completion 提供基础。

---

## 推荐放置位置

解压到项目：

```text
榕树ai改造落地相关文档/
└── Documentation_Packaging/
    └── Banyan_R0_Framework_Self_Containment_Remediation_Pack_v1.0/
```

本施工包本身属于“施工指挥资料”，不要直接复制进 `banyan-framework/`。

真正的正式 Framework 产物由 Codex 按本包提示词写入 `banyan-framework/**`。

---

## 使用顺序

1. 解压本 Pack。
2. 新开一个 Codex 窗口。
3. 让 Codex 完整读取：
   `prompts/R0_Codex正式施工提示词.md`
4. Codex 按提示词读取 D1.5 审计结果、Stage 03/07/15/20 等权威资料。
5. Codex 只执行 R0，不进入 R1。
6. 生成 R0 验收报告后停止。
7. 把验收报告和新增目录打包发回 ChatGPT 验收。

---

## R0 预期成果

R0 最终应至少解决：

```text
FRAMEWORK_RELEASE_NOT_SELF_CONTAINED
```

并建立稳定 Framework-owned assets，例如（具体目录以现有架构最小侵入为准，提示词要求先审计再决定）：

```text
banyan-framework/
├── contracts/
├── registry/
├── schemas/
├── compatibility/
└── ...
```

或等价的已有目录扩展。

禁止为了“看起来整齐”盲目新建目录；必须兼容当前 Stage 20 架构。

---

## 完成后发回

请发回：
- `R0_FRAMEWORK_SELF_CONTAINMENT_ACCEPTANCE_REPORT.md`
- Codex 最终总结
- 新增/修改的 `banyan-framework/**` 文件清单
- 最好把 R0 相关改动打包上传
