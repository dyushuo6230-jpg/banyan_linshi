# gongyi_online

| 字段 | 值 |
|---|---|
| 文档名称 | 众享源品 - 在线商城多端 UI 应用目录 |
| 文档编号 | UI-APP-gongyi_online |
| 版本 | 0.1.0 |
| 状态 | Mapped |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-19 |
| 关联来源 | ADR-044、PROJECT_STRUCTURE、DEC-008、v3.1.15 |
| 关联决策 | ADR-044、UI-DEC-001、UI-DEC-002、UI-DEC-003、UI-DEC-004、UI-DEC-005、UI-DEC-006 |

- application_id / slug：`gongyi_online`
- repository_path：`go-uni-app-online`
- 类型：众享源品 - 在线商城多端
- 设备：ios / android / harmony / miniapp / h5（见 `devices/`，G9.1 占位；主规范在 `materials/` 与应用级 `UI_SPEC.md`）
- 逻辑终端：`LT-gongyi-youxuan-c`
- 映射 PRD 模块：M07、M08、M09、M10、M11
- UI 现状：页面以 `go-uni-app-online` 现码为准（DEC-008）。**底栏/首页/分类/附近列表已点名换皮。**
- `UI_SPEC.md`：0.1.5 **Approved / Partial**（含附近列表）。上一批准冻结：`UI_SPEC-0.1.4.md`、`UI_SPEC-0.1.3.md`、`UI_SPEC-0.1.2.md`、`UI_SPEC-0.1.1.md`、`UI_SPEC-0.1.0.md`。Draft 历史：`UI_SPEC-0.1.5-Draft.md`、`UI_SPEC-0.1.4-Draft.md`、`UI_SPEC-0.1.3-Draft.md`、`UI_SPEC-0.1.2-Draft.md`、`UI_SPEC-0.1.1-Draft.md`、`UI_SPEC-0.1.0-Draft.md`。Contract **0.1.5**（分类听 `category.vue`；附近听第 4 节覆盖。附近换皮/32A 须另开口令）。
- anydesign：`materials/design-docs/` 与 `materials/tokens/`；令牌 UI-DEC-003 已确认。
- 说明：`gongyi_h5_host` 只是 H5 托管产物，逛买页面真源仍是本应用。
- 底栏：结构与中间 AI 听整栏图（UI-DEC-003）；第四坑购物车（UI-DEC-002）。现码仍藏发现。
- 首页横向分类选中：UI_SPEC / Contract 已锁同盒三件套。分类页 32A 听 Contract 0.1.5 + `UI_SPEC.md` 0.1.5 + `category.vue`（UI-DEC-005/006）。分类左栏顶底两态：32A `20260918-gongyi_online-category-rail` 通过。附近列表已入 0.1.5，换皮/32A 须另开口令。
