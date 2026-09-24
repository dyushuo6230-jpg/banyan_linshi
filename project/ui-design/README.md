# UI 设计目录规则

| 字段 | 值 |
|---|---|
| 文档名称 | UI 设计目录规则 |
| 文档编号 | DOC-G0-UI |
| 版本 | 0.2.0 |
| 状态 | Draft |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-19 |
| 关联来源 | G0 初始化、ADR-044、PROJECT_STRUCTURE、v3.1.15 |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | ADR-044、UI-DEC-001、UI-DEC-002、UI-DEC-003、UI-DEC-004、UI-DEC-005、UI-DEC-006 |
| 适用版本 | 文档体系 v0.1.3；治理模板 v3.1.15 |
| 替代文档 | 无 |

## 本期策略

- 总闸 `ENABLE_UI_SPEC_GENERATION=true`（UI-DEC-001）
- 分闸 `UI_SPEC_ENABLED_APPLICATIONS=gongyi_online`；其它应用仍关
- `UI_CONSTRAINT_MODE=NONE`（Contract 等点名换皮批次再出，以免卡住其它开发批次）
- G5.5 已填写 `UI_SCOPE_MAP.md`；G9.1 已按 ADR-044 映射
- 源品允许走 G9.5；`UI_SPEC.md` 0.1.5 **Approved Partial**；点名换皮 Contract **0.1.5**
- 不改 Element Plus / 本地生活现有 UI；后台 UI 升级另议
- 底栏/首页/分类已点名换皮。附近已入 Partial，换皮/32A 须另开口令
- 底栏：结构听整栏图 + UI-DEC-003；第四坑购物车 UI-DEC-002
- 首页横向分类选中：观感 UI-DEC-004；实现同盒三件套。分类覆盖：DEC-071 v1.3.0 + UI-DEC-005 + UI-DEC-006。附近覆盖：M07/DEC-046/069/073 写入 0.1.5 第 4 节

## 已创建

- 根目录登记、`shared/` 入口、逻辑范围
- `UI_APPLICATION_MAPPING.yaml`：6 个真实前端
- `products/{admin_web,merchant_web,local_life_miniapp,gongyi_online,onboarding_h5,gongyi_h5_host}/`
- `visual-loop/`：循环档案空壳（不计文档进度分母）

禁止虚构 `admin` / `miniapp` 等 slug。后端进程没有页面交付单元，不建 UI 应用目录。

## 源品材料放哪

众享源品 C 端五端（iOS / 安卓 / 鸿蒙 / 小程序 / H5）是 **一套** `go-uni-app-online` 代码。anydesign 主输出只放：

`products/gongyi_online/materials/`

- `design-images/`：可放拷贝，优先在清单里引用 `docs/project/sources/inbox/BATCH-003/`
- `design-docs/`：`design.md`
- `tokens/`：`design-tokens.json`

`products/gongyi_online/devices/{ios,android,harmony,miniapp,h5}/` 是 G9.1 **设备占位**。以后真有端差异才写覆盖。不要把同一份 `design.md` 拷五份。`devices/miniapp` **不是**独立小程序工程。

`shared/` 只放跨产品品牌。不要把源品商城色写进 shared，以免误伤后台 Element Plus 和本地生活。

`gongyi_h5_host` 只是 H5 托管产物，逛买页面真源仍是 `gongyi_online`。

## 视觉修复循环

档案：`visual-loop/LOOP_RUNS/`。随时可点名，不占 G 号。未点名不得改页面。
