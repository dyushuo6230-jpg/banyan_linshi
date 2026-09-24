# UI_SPEC：众享源品 - 在线商城（应用级）· 0.1.1 Draft 历史

> 冻结副本。当前批准真源见同目录 `UI_SPEC.md`（0.1.4 Approved）。本文件不再修订。

| 字段 | 值 |
|---|---|
| 文档名称 | 众享源品 - 在线商城应用级 UI 规范 |
| 文档编号 | UI-SPEC-gongyi_online |
| 版本 | 0.1.1 |
| 状态 | Draft（历史） |
| 覆盖范围 | Partial |
| 层级 | 前端应用 |
| 负责人 | TBD |
| 创建日期 | 2026-09-18 |
| 更新时间 | 2026-09-18 |
| 关联 PRD | M07、M08、M09、M10、M11（顾客端现用页，DEC-008） |
| 关联素材 | SRC-UI-003；MAT-GO-DOC-DESIGN；MAT-GO-TOK-DTCG；MAT-GO-ASSET-HOME-CHIP-SELECTED |
| 关联决策 | UI-DEC-001、UI-DEC-002、UI-DEC-003、UI-DEC-004、DEC-008、DEC-071、DEC-073、REQ-063 |
| 父级规范 | 无（`shared/UI_SPEC.md` 未启用，不继承后台/本地生活皮） |
| 代码真源 | `go-uni-app-online` |
| 替代文档 | 同目录 `UI_SPEC.md`（0.1.1 Approved）。本文是 0.1.1 Draft 冻结副本。 |

本文由第 30 节从已确认 UI-DEC-004 与切图物资增量映射。Partial 点名页仍是底栏、首页、分类。禁止 `/v2` 业务双轨。下级 `devices/` 无独立 UI_SPEC，无端差异，不必标 Needs Review。

相对 0.1.0 只增加：首页横向分类选中页面覆盖（组 A）；分类左栏顶底渐变/圆角两态。不升级 locked `chip` 令牌。不启用组 B/C/D。

## 1. 规范编号、层级、范围、版本和状态

- 编号：`UI-SPEC-gongyi_online`
- 层级：应用级。五端（ios / android / harmony / miniapp / h5）共用一份。`devices/` 无端差异覆盖。
- 范围：仅 `gongyi_online`。不约束 `admin_web`、`merchant_web`、`local_life_miniapp`、`onboarding_h5`。`gongyi_h5_host` 只托管本应用 H5 包，不另写皮。
- 版本 / 状态：0.1.1 **Draft**（Partial）。未经第 29 节批准不得升 Approved。本 Draft 不授权改 `go-uni-app-online`。
- 分闸：UI-DEC-001 已列入。其它应用 UI_SPEC 仍为占位。

## 2. 关联 PRD、原始素材和父级规范

| 类型 | 路径或编号 |
|---|---|
| PRD | `docs/project/prd/modules/M07-online-mall.md` 等 |
| 设计图 | `docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/`（引用，不复制） |
| 切图 | `materials/assets/`（组 A 启用；组 B/C/D 冻结） |
| 清单 | `materials/MATERIALS_MANIFEST.yaml` |
| 分析 | `materials/design-docs/design.md` |
| 令牌 | `materials/tokens/design-tokens.json` |
| 对比度 | `materials/design-docs/design-a11y.md` |
| 父级 | 无 Approved shared |

PRD 与图冲突处：M07 仍写「底栏四 Tab」。以 **UI-DEC-002** 为准（五坑，第四坑购物车）。不另开 UI-CONFLICT。

## 3. 设计目标

金顶会场 + 白卡片货架 + 橙红现价。青柠绿只给底栏侧边选中。中间 AI 用橙红圆形标。消费电商，不是后台、不是 Linear。

## 4. 继承、覆盖、locked、禁止

**继承：** 无跨产品 shared 令牌。

**覆盖（相对 PNG）：**

| 项 | 听谁 |
|---|---|
| 第四坑文案/路由 | UI-DEC-002：购物车，不是发现 |
| 金主按钮字色 | UI-DEC-003：深字压金，不跟详情图白字 |
| 分类「甄选上新」加高 | DEC-071：不验收 |
| 附近文件名删除板块 | 不做、不对接 |
| AI 视频/生图 | 本批不做 |
| 首页横向分类选中 | UI-DEC-004：听切图组 A `首页横向分类选中背景15`（黑底、星、下箭头尾巴）。不定稿浅金胶囊。循环不得改回系统 `chip` 浅金。未选中仍白底细边。 |
| 分类左栏顶底 | 有内容被裁切/滚出时，顶底用渐变遮挡；没有藏住的内容时，顶底同等圆角和边距。不恢复甄选上新，不加高，不插上下箭头，不用组 B/C/D。 |

**locked（≥两页出现且已确认）：** `brand-gold` `#FFC31B`、`surface` `#FFFFFF`、`surface-page` `#F6F6F6`、`text-primary` `#222222`、`price` `#FD5800`、`accent-lime` `#A6F342`、`search-cta` `#111111`。底栏结构（五坑、中间缺口、橙红 AI）UI-DEC-003。系统 `chip` 选中浅金仍 locked；首页横向分类选中是覆盖，不是令牌升级。

**禁止：** 令牌写入 `shared/`；`design.md` 复制进 `devices/`；业务路由 `/v2`；未 Approved 当像素验收；把《Tab Bar交互》当完整底栏；把组 B/C/D 当本版启用。

## 5. 组件库和版本

无第三方设计系统。栈：UniApp Vue3、750rpx、现码零件。图标用现有 tabbar 资源；第四坑暂用发现图。无应用级 `ICON_MANIFEST.yaml`。切图组 A：`MAT-GO-ASSET-HOME-CHIP-SELECTED`。

## 6. Design Token

真源：`materials/tokens/design-tokens.json`（由 `design.md` frontmatter 导出，禁止手改 JSON）。落地 rpx = 逻辑 px × 2。本版不改令牌文件。

## 7. 色彩、字体、圆角、阴影、间距和图标

| 角色 | Token | 值 |
|---|---|---|
| 顶栏金 | brand-gold | `#FFC31B` |
| 页底 / 卡片 | surface-page / surface | `#F6F6F6` / `#FFFFFF` |
| 主文 / 次文 | text-primary / text-muted | `#222222` / `#989898` |
| 现价 | price | `#FD5800` |
| 底栏选中 | accent-lime | `#A6F342` |
| 搜索实心钮 | search-cta | `#111111` |
| 反白（仅深底） | inverse | `#FFFFFF` |

字体：系统黑体 PingFang SC 等。列表/首页现价 20px/40rpx（`display`）；详情主价 28px/56rpx（`price-xl`）。圆角 pill 999px、卡片 lg 16px。阴影见 tokens。图标：侧边选中青柠填色；中间 AI 橙红标。首页横向分类选中底图用切图组 A，不把该黑底抽成新 locked 色。

## 8. 页面布局和页面模式

画布 375pt / 750rpx。H5 预览 390×844。

| 点名页 | 路由（现码） | 模式 | 对照图 |
|---|---|---|---|
| 底栏 | `addon/shop/components/tabbar/index.vue` | 五坑白底中间抬高 | 整栏图 + 《Tab Bar交互》上半 |
| 首页 | `/addon/shop/pages/indexPage/index` | 金顶 + 搜索 + 运营位 + 双列货 | `公益优选-商城首页定稿.png` + 横向分类选中听组 A |
| 分类 | `/addon/shop/pages/indexPage/category` | 金顶 + 搜索黑钮 + 左栏 + 右 3 列圆图 | `分类.png`（DEC-071）+ 左栏顶底两态 |

未点名有图页（列表、搜索、详情、我的、附近）令牌可复用，**不**列入本版换皮范围。无 PNG 页 F0。

## 9. 组件使用规范

| 组件 | 用法 |
|---|---|
| nav-gold-header | 金洗墙。首页左频道、**右上购物袋保留**（进购物车） |
| search-bar | 白胶囊。首页无黑钮；分类/搜索页右侧黑「搜索」 |
| tab-bar | 购物 / 附近 / AI助手 / **购物车** / 我的。中间橙红 AI。第四坑发现图标、购物车文案、进 `/addon/shop/pages/goods/cart` |
| goods-card | 白卡 lg 圆角，现价 `price` |
| button-primary | 金底 **深字** |
| button-cart | 白底橙描边（详情页，非本 Partial 换皮范围） |
| chip | 默认选中浅金、分类横向胶囊。**首页横向分类选中**例外：听 `MAT-GO-ASSET-HOME-CHIP-SELECTED`，见第 4 节 |
| category-rail | 左栏同高（不要甄选上新加高、不插箭头）；右 3 列圆图。顶底：有裁切用渐变遮挡，无裁切则同等圆角和边距 |

## 10. 交互规范

触屏无悬停。底栏点击切 Tab，第四坑进购物车不是发现。分类左栏点一级，右侧展示该级下二级模块（DEC-071）。首页右上购物袋与底栏购物车都可进车。真扣款不要求（DEC-050）。首页横向分类点选切换选中切图；分类左栏滚动时切换顶底遮挡/圆角两态。

## 11. Loading、Empty、Error、Disabled、No Permission、Offline、Success

| 状态 | 本 Partial |
|---|---|
| Empty | 列表到底用「别再搜，我到底啦~」（《Tab Bar交互》下半）。不是底栏 |
| Loading / Error / Offline / Success | 沿用现码，本 Partial 不新造 |
| Disabled | 主按钮禁用不得改成青柠 |
| No Permission | 未登录「我的」按个人页图；非本 Partial |

## 12. 响应式和设备适配

只保 375 逻辑宽。禁止擅自四列。五端同一套代码，差异用条件编译，不在 `devices/` 复制规范。

## 13. 可访问性

见 `design-a11y.md`。主按钮必须深字压金（9.91:1）。`text-muted` 不得用于长文。价签仅大号。白字只给黑搜索钮等深底。首页选中切图上的字保持可读（白字压黑底）。

## 14. 高保真要求

| 页 | 等级 | 说明 |
|---|---|---|
| 底栏、首页、分类 | F3（点名换皮后） | 分类例外 DEC-071；第四坑不跟「发现」文案；首页横向分类选中听 UI-DEC-004 |
| 购物车页 | 不像素 | DEC-008；本规范只约束入口 |
| AI 助手整页 | 不像素 | DEC-008 |
| AI 视频/生图 | 不做 | |
| 其余无图页 | F0 | |

## 15. 必须遵守、推荐、禁止

**必须：** locked 令牌；底栏五坑+橙红 AI；第四坑购物车；金钮深字；首页右上购物袋；750rpx；接口 8035。批准后：首页横向分类选中听组 A；分类左栏顶底两态。

**推荐：** 模块间距 8/12/16；卡片靠灰底托白，少描边。

**禁止：** 青柠涂按钮/价签/顶栏；恢复发现业务；`/v2`；手改 tokens JSON；把源品色写入 shared；本版启用组 B/C/D；借覆盖把左栏选中加高。

## 16. 视觉验收标准

仅在点名换皮之后做视觉验收。视口 390×844。对照点名 PNG + 本规范覆盖项。建议第 32A 节循环，不是门禁。阈值：关键尺寸 ±1px；颜色对 locked 令牌，**首页横向分类选中除外**（对切图组 A，循环不得改回浅金胶囊）。分类左栏须验两态（有裁切 / 无裁切），静图一张不够。

本 Draft **不**自动开始换皮或截图循环。须第 29 节批准后再点名 32A。

## 17. 待确认问题

- 系统黑体是否以后换品牌字体：TBD，当前系统黑体。
- PRD M07「四 Tab」正文未改：以 UI-DEC-002 为准，批准 UI_SPEC 时不阻塞；正式收口可另走 CR。
- 未点名有图页（详情/列表/搜索/我的/附近）是否纳入下一份 Partial：TBD，不在本次范围。
- 组 B/C/D（金气泡、左栏箭头）何时启用：须另改 DEC-071 第 4 条，不在 0.1.1。

无新的高影响未决项需当场第 2A 节；首页选中覆盖已 UI-DEC-004。
