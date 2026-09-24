# UI_SPEC：众享源品 - 在线商城（应用级）

| 字段 | 值 |
|---|---|
| 文档名称 | 众享源品 - 在线商城应用级 UI 规范 |
| 文档编号 | UI-SPEC-gongyi_online |
| 版本 | 0.1.5 |
| 状态 | Approved |
| 覆盖范围 | Partial |
| 层级 | 前端应用 |
| 负责人 | TBD |
| 创建日期 | 2026-09-18 |
| 更新时间 | 2026-09-19 |
| 批准人 | 会话授权用户 |
| 批准日期 | 2026-09-19 |
| 批准口令 | UI_SPEC_APPROVAL=UI-SPEC-gongyi_online@0.1.5 |
| 关联 PRD | M07、M08、M09、M10、M11（顾客端现用页，DEC-008）；REQ-134 |
| 关联素材 | SRC-UI-003；MAT-GO-DOC-DESIGN；MAT-GO-TOK-DTCG；MAT-GO-ASSET-HOME-CHIP-SELECTED；MAT-GO-ASSET-HOME-CHIP-STAR；MAT-GO-ASSET-CAT-CHIP-SELECTED；MAT-GO-ASSET-CAT-RAIL-ARROW-UP；MAT-GO-ASSET-CAT-RAIL-ARROW-DOWN；MAT-GO-IMG-NEARBY |
| 关联决策 | UI-DEC-001、UI-DEC-002、UI-DEC-003、UI-DEC-004、UI-DEC-005、UI-DEC-006、DEC-008、DEC-046、DEC-069、DEC-071 v1.3.0、DEC-073、REQ-063 |
| 父级规范 | 无（`shared/UI_SPEC.md` 未启用，不继承后台/本地生活皮） |
| 代码真源 | `go-uni-app-online`（首页选中：`src/addon/shop/pages/indexPage/components/home.vue`；分类：`src/addon/shop/pages/indexPage/category.vue`；附近列表：`src/addon/shop/pages/nearby/index-f.vue`） |
| 替代文档 | 同目录 `UI_SPEC-0.1.5-Draft.md`（Draft 历史）；`UI_SPEC-0.1.4.md`（上一批准冻结）；`UI_SPEC-0.1.3.md`；`UI_SPEC-0.1.2.md`；`UI_SPEC-0.1.1.md`；`UI_SPEC-0.1.0.md`。 |

本文已按第 29 节批准。覆盖 Partial：底栏、首页、分类、附近列表。相对 0.1.4：附近整页已定 PRD 写入第 4 节覆盖。底栏 / 首页 / 分类沿用 0.1.4。店详情 `details-f.vue` **不**列入本版换皮。禁止 `/v2` 业务双轨。不是 Baselined。下级 `devices/` 无端差异，未标 Needs Review。

**本批准不改代码、不换皮、不开 32A。** 点名附近换皮或 32A 须另开口令。

相对 0.1.4：Partial 增加附近列表 `/addon/shop/pages/nearby/index-f`。这是页面覆盖，不是令牌升级。

## 1. 规范编号、层级、范围、版本和状态

- 编号：`UI-SPEC-gongyi_online`
- 层级：应用级。五端（ios / android / harmony / miniapp / h5）共用一份。`devices/` 无端差异覆盖。
- 范围：仅 `gongyi_online`。不约束 `admin_web`、`merchant_web`、`local_life_miniapp`、`onboarding_h5`。`gongyi_h5_host` 只托管本应用 H5 包，不另写皮。
- 版本 / 状态：0.1.5 **Approved**（Partial）。不是 Baselined。本批准不授权改 `go-uni-app-online`。
- 分闸：UI-DEC-001 已列入。其它应用 UI_SPEC 仍为占位。

## 2. 关联 PRD、原始素材和父级规范

| 类型 | 路径或编号 |
|---|---|
| PRD | `docs/project/prd/modules/M07-online-mall.md` 等 |
| 设计图 | `docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/`（引用，不复制） |
| 附近对照图 | `MAT-GO-IMG-NEARBY`（文件名含删除板块；图面仍画出那些坑，以覆盖为准） |
| 切图 | `materials/assets/`（组 A 整图作抠星来源与观感参考；星独立切图启用；组 B 观感参考禁止拉伸；组 C/D 箭头启用） |
| 清单 | `materials/MATERIALS_MANIFEST.yaml` |
| 分析 | `materials/design-docs/design.md` |
| 令牌 | `materials/tokens/design-tokens.json` |
| 对比度 | `materials/design-docs/design-a11y.md` |
| 父级 | 无 Approved shared |
| 现码 | `home.vue`；`category.vue`；`nearby/index-f.vue`；星资源 `src/addon/shop/static/home/chip-star.png` |

PRD 与图冲突处：M07 仍写「底栏四 Tab」。以 **UI-DEC-002** 为准（五坑，第四坑购物车）。M07 GWT「没有甄选上新」以 **DEC-071 v1.1.0** 为准（不编造假入口；树上有则照出）。附近 PNG 与已定口径冲突处一律听第 4 节（删除板块、CPS 两行轮播、不画距离、顶灯片子列表、业态根筛选），不另开 UI-CONFLICT。

## 3. 设计目标

金顶会场 + 白卡片货架 + 橙红现价。青柠绿只给底栏侧边选中。中间 AI 用橙红圆形标。消费电商，不是后台、不是 Linear。附近是金顶 + 店列表，不是再做一套发现信息流。

## 4. 继承、覆盖、locked、禁止

**继承：** 无跨产品 shared 令牌。

**覆盖（相对 PNG）：**

| 项 | 听谁 |
|---|---|
| 第四坑文案/路由 | UI-DEC-002：购物车，不是发现 |
| 金主按钮字色 | UI-DEC-003：深字压金，不跟详情图白字 |
| 分类名称是否出现 | **DEC-071 v1.1.0：** 不编造假入口；平台类目树上有的一级照出，第一项不收窄、不加高成另一套格子 |
| AI 视频/生图 | 本批不做 |
| 首页横向分类选中 | **UI-DEC-004 观感 + 现码三件套。** 观感：黑底、青柠星、下三角、白字；不是定稿浅金胶囊。实现（`home.vue`）：选中与未选中同一套盒子（高 `56rpx`、圆角 `76rpx`、左右 `33rpx`、边 `2rpx`）；选中只改底/边为 `#222222`（从组 A 中心量出，**不**升级 locked 令牌）；星用 `MAT-GO-ASSET-HOME-CHIP-STAR` 绝对定位右上（约 `22rpx`，`top: -8rpx; right: 10rpx`）；三角用 CSS `border` 水平居中画在盒子下方（`border-width: 14rpx 12rpx 0`，`bottom: -12rpx`），**不计入**盒子高度。宽度随文案变，圆角保持胶囊、禁止被长字拉变形。组 A 整图 `首页横向分类选中背景15` 只作抠星来源与观感参考。**禁止**把该整图设为 `background-image` 并 `background-size: 100% 100%` 拉伸。循环不得改回系统 `chip` 浅金，也不得改回整图拉伸。未选中仍白底细边 `#e8e8e8`。 |
| 分类页图层 | **DEC-071 v1.3.0 + UI-DEC-005。** 外底板听 `category.vue` 现状：圆角分层——外底板 `16rpx`，左栏竖条与选中金卡 `10rpx`。底色奶油落到页灰 `#fff8df → #fffdf4 → #f8f8f8 → #f6f6f6`，内边距 `16rpx`。左栏与右侧间距 `20rpx`。不对《分类.png》顶上那条米金做像素验收。奶油色不升 locked 令牌。左栏单独竖条皮，**禁止**把 `side-bg.png` 大胶囊切图当竖条底拉伸。二级单独槽。三级每个模块一块内底板白卡，圆角 `15rpx`。循环不得刷回米金条，也不得把三处圆角强行统一。 |
| 分类左栏 | **UI-DEC-006 / 现码。** 未选中：同一宽高 `88rpx`、同一字号。选中：白底外包金芯（`.side-entry-fill`），白边约 `10rpx` 且在阴影内；圆角 `10rpx`；上下箭头切图画在金卡**里面**，选中块加高；阴影打在白底外圈。组 C/D 箭头启用。竖条顶角 `10rpx`，CSS 白底。顶底淡入跟现码：顶 `#fff6d6` 溶出、底白溶出，循环不得另配一套色。循环不得把箭头改回格外、把选中改回与未选同高、把白边挪到阴影外。 |
| 分类二级槽 | **现码。** 槽高 `64rpx`；胶囊高 `46rpx`、圆角 `35rpx`、左右 `18rpx`。选中金渐变 `#ffd24d → #ffc31b`、白字、`drop-shadow`；倒三角 CSS `bottom: -15rpx`，不算进盒子。左右遮罩结构可留，**不铺** `#fff6d6`（现码已注释）。`.tabs-scroll` 约 `88%`、下拉钮宽 `58rpx`，不升令牌。组 B 禁止拉伸。循环不得为贴图改槽高导致三角离卡，也不得铺回米金遮罩。 |
| 分类三级圆图 | **UI-DEC-006 / 现码。** `display: grid`；`grid-template-columns: repeat(3, minmax(0, 1fr))`；`column-gap: 16rpx`；`row-gap: 40rpx`。禁止 flex 换行挤成两列。圆 `140rpx`。白卡圆角 `15rpx`、内边距 `26rpx 26rpx 42rpx`。长名可省略号。 |
| 分类全部分类 | **UI-DEC-006 / 现码。** 叠在内容区 overlay；标题固定；列表区高 `520rpx` 且 `:deep(.uni-scroll-view)` `overflow-y: auto`。面板圆角 `14rpx`。条目灰底 `#f6f6f6`；选中金底 **深字 `#222222`**（不是白字）。循环不得改回不可滚、整块裁切，也不得把面板选中改成白字。点胶囊仍定位到对应二级白卡。 |
| 附近删除板块 | **文件名 + M07。** 超市便利、生鲜果蔬、优选超市、美团团购、数码百货、看病买药、鲜花绿植等图上有也不画、不对接。去静态坑。循环不得为贴图补回这些板块。 |
| 附近 CPS | **M07 + 现码 `swiper`。** 「美团外卖」到「更多」是两行、本页轮播、不删。实现：`nearby__cps-swiper`；每页最多上 5、下 5；超出翻页。图标/文案听平台目录上架项（DEC-046），不把图上静宫格或某一组写死名当像素目标。循环不得收成一页静格，也不得把目录项改成文件名已删板块。跳转不进 32A：DEC-046 要带 `from=mall-online`；现码本期只展示。循环不得借贴图改对接、也不得删宫格。 |
| 附近顶灯片 | **DEC-069。** 板块子列表，不是购物首页 banner 表。没配不轮、不拿页面静图冒充。循环不得把灯片改挂首页 banner。 |
| 附近筛选 | **DEC-046 / M07。** 筛选项=当前全部本地业态根（平台级，与某店勾选无关）。「全部业态」+ 横向业态。循环不得改成图上写死类目，也不得只留餐饮/美发/商超三名当规范。 |
| 附近列表与跳转 | **M07。** 列表=本地生活租户。点店→本地生活店详情（现码 `/addon/shop/pages/nearby/details-f`）。点货→电商详情。本期不拉起店小程序。店详情页本身不在本 Partial 换皮。循环不得改这些路由。 |
| 附近店卡字段 | **DEC-073 / REQ-134。** 头像、店名、业态、营业状态、地址、开业 30 天内招新开业。列表不展示让利、积分、共益分发。本袋不画距离、不驾车分钟、不真导航。图上的米数/驾车/让利标覆盖豁免，不得挡验收，不得为贴图补上。现码定位行「天安门广场西156米」不当像素目标；点定位敬请期待。循环不得接真定位。 |
| 附近底栏 | **UI-DEC-002。** 本页循环只改 `index-f.vue`，不改 `tabbar/index.vue`。第四坑仍购物车。底栏标签下内边距保持用户改回的 `30rpx`，附近 32A 不得再改。 |
| 附近端口 | 只打 mall-online **8035**。禁止 8032 / 8033 / 8037。 |

**分类页现码冻结（32A 不得为对齐《分类.png》或已冻结的 0.1.3 改这些）：** `.body` 内边距 `16rpx 20rpx 0`；`.board` 圆角 `16rpx`、内边距 `16rpx`、奶油落到页灰；`.main` 左距 `20rpx`；竖条宽 `100rpx`、CSS 白底、顶角 `10rpx`、**不用** `side-bg.png`；未选中格 `88rpx`；选中白底外包金芯、白边约 `10rpx` 在阴影内、圆角 `10rpx`、阴影 `1rpx 5rpx 8rpx rgba(255,184,0,0.42)`、金芯渐变 `#ffe566 → #ffc31b`、箭头切图在金卡内 `28×14rpx`、选中加高；顶淡入 `#fff6d6`、底淡入白；二级槽与三级 grid / 全部分类见上表。单次 rpx 不升 locked 令牌。

**附近列表可对图（覆盖之外）：** 金顶渐变洗墙、定位行结构（针 + 文案 + 箭头，不含米数验收）、白胶囊搜索 + 黑「搜索」钮、灯片骨架与圆角、CPS 两行图标区观感、全部业态+横向筛选条、店卡骨架、空态「店家正在入住中...」。单次 rpx 不升 locked 令牌。

**locked（≥两页出现且已确认）：** `brand-gold` `#FFC31B`、`surface` `#FFFFFF`、`surface-page` `#F6F6F6`、`text-primary` `#222222`、`price` `#FD5800`、`accent-lime` `#A6F342`、`search-cta` `#111111`。底栏结构（五坑、中间缺口、橙红 AI）UI-DEC-003。系统 `chip` 选中浅金仍 locked；首页横向分类选中是覆盖，不是令牌升级。选中黑底 `#222222` 只给这一粒，不写入 tokens JSON。分类二级选中金底用 `brand-gold`，不抽新 locked 色。附近复用金顶与搜索黑钮，不抽新 locked 色。

**禁止：** 令牌写入 `shared/`；`design.md` 复制进 `devices/`；业务路由 `/v2`；未 Approved 当像素验收；把《Tab Bar交互》当完整底栏；把组 B 整图当选中底拉伸；把组 A 整图当选中底拉伸；编造树上没有的一级；借 32A 按已冻结的 0.1.3 或《分类.png》改 `category.vue`；借 32A 按附近 PNG 补回删除板块、收掉 CPS 轮播、补距离/驾车/让利、改底栏、改店详情页、改接口端口。

## 5. 组件库和版本

无第三方设计系统。栈：UniApp Vue3、750rpx、现码零件。图标用现有 tabbar 资源；第四坑暂用发现图。无应用级 `ICON_MANIFEST.yaml`。切图：组 A 整图 `MAT-GO-ASSET-HOME-CHIP-SELECTED`（参考）；星 `MAT-GO-ASSET-HOME-CHIP-STAR`（启用）；组 B `MAT-GO-ASSET-CAT-CHIP-SELECTED`（观感参考）；组 C/D 左栏箭头（启用）。附近 CPS / 店卡用现码 `nearby/` 静态资源，本 Draft 不新登记切图。

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

字体：系统黑体 PingFang SC 等。列表/首页现价 20px/40rpx（`display`）；详情主价 28px/56rpx（`price-xl`）。圆角 pill 999px、卡片 lg 16px。阴影见 tokens。图标：侧边选中青柠填色；中间 AI 橙红标。首页横向分类选中黑底用代码 `#222222`，星用独立切图（青柠，来自组 A），不把该黑底抽成新 locked 色。分类二级选中白字压金底。附近金顶与搜索黑钮复用上表，不抽新色。

## 8. 页面布局和页面模式

画布 375pt / 750rpx。H5 预览 390×844。

| 点名页 | 路由（现码） | 模式 | 对照图 |
|---|---|---|---|
| 底栏 | `addon/shop/components/tabbar/index.vue` | 五坑白底中间抬高 | 整栏图 + 《Tab Bar交互》上半 |
| 首页 | `/addon/shop/pages/indexPage/index` | 金顶 + 搜索 + 运营位 + 双列货 | `公益优选-商城首页定稿.png` + 横向分类选中听第 4 节三件套（不对组 A 整图贴合） |
| 分类 | `/addon/shop/pages/indexPage/category` | 金顶 + 搜索黑钮 + 外底板 + 左栏竖条 + 二级槽 + 三级内白卡 | `分类.png` + DEC-071 v1.3.0 / UI-DEC-005 / UI-DEC-006（听现码） |
| 附近列表 | `/addon/shop/pages/nearby/index-f` | 金顶 + 定位行 + 搜索黑钮 + 灯片 + CPS 两行轮播 + 业态筛 + 店卡 | `MAT-GO-IMG-NEARBY` + 第 4 节整页 PRD 覆盖 |

未点名有图页（列表、搜索、商品详情、我的、店详情）令牌可复用，**不**列入本版换皮范围。无 PNG 页 F0。

## 9. 组件使用规范

| 组件 | 用法 |
|---|---|
| nav-gold-header | 金洗墙。首页左频道、**右上购物袋保留**（进购物车）。附近无购物袋，改定位行 |
| search-bar | 白胶囊。首页无黑钮；分类 / 搜索 / **附近**右侧黑「搜索」 |
| tab-bar | 购物 / 附近 / AI助手 / **购物车** / 我的。中间橙红 AI。第四坑发现图标、购物车文案、进 `/addon/shop/pages/goods/cart`。附近循环不改此零件 |
| goods-card | 白卡 lg 圆角，现价 `price` |
| button-primary | 金底 **深字** |
| button-cart | 白底橙描边（详情页，非本 Partial 换皮范围） |
| chip | 默认选中浅金。**首页横向分类选中**例外：同盒 CSS 黑底 + `MAT-GO-ASSET-HOME-CHIP-STAR` + CSS 三角，见第 4 节。**分类二级选中**例外：同盒 CSS 金底 + 渐变 + 白字 + CSS 倒三角，见第 4 节 |
| category-rail | 未选中同高；选中白边包金芯、箭头在内、选中加高；竖条 CSS 白底 10rpx，禁止 `side-bg.png` 拉伸。顶底淡入跟现码。右 3 列 **CSS grid** 圆图落在三级白卡上。全部分类面板内可滚 |
| nearby-cps | 两行本页 `swiper`，每页最多 5+5；听平台目录；循环不得改成静宫格 |
| nearby-store-card | 头像 / 名 / 业态 / 营业 / 地址 / 招新开业；不画距离、让利、共益分发 |

## 10. 交互规范

触屏无悬停。底栏点击切 Tab，第四坑进购物车不是发现。分类左栏点一级，右侧展示该级下二级模块（DEC-071）。首页右上购物袋与底栏购物车都可进车。真扣款不要求（DEC-050）。首页横向分类点选切换选中三件套（同盒黑底、星、三角）；分类左栏滚动时切换顶底淡入两态；分类二级点选切换代码金气泡（胶囊对齐、三角顶住三级白卡）；点右侧三角打开全部分类，超出在面板内滚。

附近：按店名搜索；按全部业态或某个本地根筛列表；点店进店详情、点货进电商详情、不拉起店小程序；CPS 可翻页，点了不由 32A 改跳转；点定位敬请期待。灯片跳转仍听 DEC-069 子列表类型，循环不改。

## 11. Loading、Empty、Error、Disabled、No Permission、Offline、Success

| 状态 | 本 Partial |
|---|---|
| Empty | 商品列表到底用「别再搜，我到底啦~」（《Tab Bar交互》下半）。附近店空用现码「店家正在入住中...」 |
| Loading / Error / Offline / Success | 沿用现码，本 Partial 不新造 |
| Disabled | 主按钮禁用不得改成青柠 |
| No Permission | 未登录「我的」按个人页图；非本 Partial |

## 12. 响应式和设备适配

只保 375 逻辑宽。禁止擅自四列。五端同一套代码，差异用条件编译，不在 `devices/` 复制规范。

## 13. 可访问性

见 `design-a11y.md`。主按钮必须深字压金（9.91:1）。`text-muted` 不得用于长文。价签仅大号。白字只给黑搜索钮、首页选中黑底、分类二级选中金底等深/金底。

## 14. 高保真要求

| 页 | 等级 | 说明 |
|---|---|---|
| 底栏、首页、分类 | F3（点名换皮后） | 分类听第 4 节 + `category.vue` 现状；不对 0.1.3 外侧箭头/米金条/flex 两列 |
| 附近列表 | F3（点名换皮且 32A 之后） | 金顶/搜索/灯片/店卡骨架对图；第 4 节附近覆盖不对 PNG 1:1 |
| 店详情 | 不在本 Partial | DEC-073；另开口令 |
| 购物车页 | 不像素 | DEC-008；本规范只约束入口 |
| AI 助手整页 | 不像素 | DEC-008 |
| AI 视频/生图 | 不做 | |
| 其余无图页 | F0 | |

## 15. 必须遵守、推荐、禁止

**必须：** locked 令牌；底栏五坑+橙红 AI；第四坑购物车；金钮深字；首页右上购物袋；750rpx；接口 8035。首页横向分类选中用同盒三件套；分类页按第 4 节现状覆盖（外底板、左栏选中、grid 三列、全部分类可滚）。附近：CPS 两行本页轮播；删除板块不画；店卡不画距离/让利；筛选项为本地业态根；顶灯片子列表；只打 8035。

**推荐：** 模块间距 8/12/16；卡片靠灰底托白，少描边。现码三角/星/箭头/面板高度的 rpx 可微调，不把单次数值冻成新令牌。附近金顶/搜索/灯片/店卡骨架的 rpx 可对图微调，同样不升令牌。

**禁止：** 青柠涂按钮/价签/顶栏；恢复发现业务；`/v2`；手改 tokens JSON；把源品色写入 shared；把组 B 整图当选中底拉伸；把组 A 整图当选中底拉伸；编造树上没有的一级；借循环把分类外底板刷回米金条；把外底板/竖条/选中卡圆角强行统一；把左栏箭头改回格外或把选中改回与未选同高；把 `side-bg.png` 当竖条底拉伸；把三级圆图改回 flex 两列；去掉全部分类滚动；铺回二级米金遮罩；改 `.main` 左距；把全部分类选中改白字；用 0.1.3「箭头贴外侧 / 格子不加高」当目标值。借附近循环：补回文件名删除板块；把 CPS 收成静宫格；补距离/驾车/让利/共益分发；改底栏或店详情；改 CPS/灯片/列表接口与跳转；打 8032。

## 16. 视觉验收标准

仅在点名换皮之后做视觉验收。视口 390×844。对照点名 PNG + 本规范覆盖项。建议第 32A 节循环，不是门禁。阈值：关键尺寸 ±1px；颜色对 locked 令牌。**首页横向分类选中除外：** 对第 4 节三件套（同盒、黑底 `#222222`、独立星、CSS 三角、白字），**不对** `首页横向分类选中背景15` 整图 1:1 贴合。循环不得改回浅金胶囊，也不得改回整图拉伸。**分类页：** 对第 4 节覆盖 + 现码 `category.vue`；外底板对 UI-DEC-005；左栏选中/三级 grid/全部分类滚动对 UI-DEC-006。**不对**《分类.png》米金条、外侧箭头、组 B 整图 1:1。左栏须验两态。循环不得改回：无箭头、箭头在外、选中与未选同高、米金条、flex 两列、不可滚的全部分类、`side-bg.png` 拉伸竖条。

**附近列表（点名换皮 / 32A 之后）：** 对第 4 节附近覆盖 + 金顶/搜索/灯片/店卡骨架。覆盖项（删除板块、CPS 轮播、距离/让利、写死类目）标豁免，不得挡验收，不得改代码去贴图。读序：`EFFECTIVE_UI_CONTRACT` 0.1.5 → 本规范第 4 节 → `index-f.vue`。分类页读序：本合同 → 本规范第 4 节 → `category.vue`。与《分类.png》或已冻结的 0.1.3 冲突时以现码为准。

本批准 **不**自动开始换皮或 32A。

## 17. 待确认问题

- 系统黑体是否以后换品牌字体：TBD，当前系统黑体。
- PRD M07「四 Tab」正文未改：以 UI-DEC-002 为准，批准 UI_SPEC 时不阻塞；正式收口可另走 CR。
- PRD M07 GWT「没有甄选上新」未改：以 DEC-071 v1.1.0 为准，批准不阻塞；正式收口可另走 CR。
- 未点名有图页（商品详情/列表/搜索/我的/店详情）是否纳入下一份 Partial：TBD，不在本次范围。
- CPS 点了是否跳第三方：业务听 DEC-046；现码本期只展示。本批准不裁决跳转，32A 不得改。

无新的高影响未决项需当场第 2A 节。附近覆盖均摘自已确认 PRD/DEC/文件名，不是新 UI-DEC。
