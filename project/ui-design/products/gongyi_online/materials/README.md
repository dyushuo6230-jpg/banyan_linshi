# gongyi_online materials

| 字段 | 值 |
|---|---|
| 文档名称 | 众享源品 C 端应用级 UI 素材 |
| 版本 | 0.1.0 |
| 状态 | 已登记 BATCH-003 引用 + 切图 assets + anydesign 令牌已确认 |
| 更新时间 | 2026-09-18 |

源品五端共用这一层。不要把主规范复制进 `../devices/`。

| 子目录 | 用途 |
|---|---|
| `design-images/` | 可选存放设计图拷贝；优先引用 BATCH-003 |
| `assets/` | 切图。组 A 整图作抠星来源（禁止当选中底拉伸）；星独立切图启用（UI-DEC-004）；组 B 观感参考禁止拉伸；组 C/D 箭头启用（DEC-071 v1.1.0） |
| `design-docs/` | anydesign 的 `design.md` |
| `tokens/` | anydesign 的 `design-tokens.json` |

设计图源：`docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/`（SRC-UI-003），只引用不复制。切图在 `assets/`。anydesign 已写入 `design-docs/design.md` 与 `tokens/design-tokens.json`。清单不能当像素验收。
