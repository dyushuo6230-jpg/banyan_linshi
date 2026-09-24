# 工程和编码规范

| 字段 | 值 |
|---|---|
| 文档名称 | 工程和编码规范 |
| 文档编号 | DOC-G9-STD |
| 版本 | 0.1.0 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-10 |
| 关联来源 | ADR-042、ADR-001～041 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

本夹是工程规范唯一真源（G9 **Baselined**，ADR-043；TECH_BASELINE=v0.1.5）。待配置保持 TBD。

**叠加 DEC-049：** mall-online 与 h5-online 目录已建（本机 8035 / 8036）。盖章正文「不创建 mall-online」是开工前口径。

| 文件 | 职责 |
|---|---|
| [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) | 仓库目录与前端应用映射 |
| [CODING_STANDARDS.md](./CODING_STANDARDS.md) | 命名、错误、日志、事务、幂等、安全（含本地自测口令约定）、禁止事项、众享源品 - 在线商城多端条件编译 |
| [TESTING_AND_GIT.md](./TESTING_AND_GIT.md) | 测试、Git、Code Review、静态检查 |

API 细则见 `../api/`。数据库细则见 `../database/`。本夹不复制第二套接口或 DDL。
