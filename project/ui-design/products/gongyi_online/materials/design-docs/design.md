---
version: anydesign-1
name: 众享源品 - 在线商城
source: docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/
captured_at: 2026-09-18
description: |
  消费级电商 App：顶区大面积金黄渐变，页面浅灰底白卡片，售价用高饱和橙红。
  底栏选中图标是卡通青柠绿。金顶栏是品牌时刻；青柠绿只给底栏选中。
  覆盖 SRC-UI-003 逛买主链截图。底栏发现文案按 UI-DEC-002 改为购物车。
  金主按钮深字压金；底栏结构听整栏图、中间 AI 橙红标；详情主价加大；首页右上购物袋保留（UI-DEC-003）。

colors:
  brand-gold: "#FFC31B"
  brand-gold-deep: "#FEC001"
  brand-gold-soft: "#FFD854"
  surface: "#FFFFFF"
  surface-page: "#F6F6F6"
  text-primary: "#222222"
  text-muted: "#989898"
  inverse: "#FFFFFF"
  price: "#FD5800"
  promo: "#F87000"
  accent-lime: "#A6F342"
  accent-lime-hi: "#EAFF76"
  search-cta: "#111111"
  border: "#E8E8E8"

typography:
  display:
    fontFamily: "PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 20px
    fontWeight: 600
    letterSpacing: 0
  title:
    fontFamily: "PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 17px
    fontWeight: 600
  body:
    fontFamily: "PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
  caption:
    fontFamily: "PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
  caption-mono:
    fontFamily: "PingFang SC, ui-monospace, monospace"
    fontSize: 11px
    fontWeight: 400
  price-xl:
    fontFamily: "PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 28px
    fontWeight: 600
    letterSpacing: 0

spacing:
  base: 4px
  scale: [4, 8, 12, 16, 24, 32, 48, 64]

rounded:
  sm: 8px
  md: 12px
  lg: 16px
  pill: 999px

shadows:
  card: "0 4px 16px rgba(0,0,0,0.06)"
  tab: "0 -0.5px 0 #EEEEEE"

components:
  nav-gold-header:
    backgroundColor: "{colors.brand-gold}"
    textColor: "{colors.text-primary}"
    padding: 12px 16px
  search-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    rounded: "{rounded.pill}"
    padding: 8px 12px
  tab-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    padding: 6px 0 8px
  goods-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 12px
  button-primary:
    backgroundColor: "{colors.brand-gold}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.pill}"
    padding: 12px 28px
  button-cart:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.promo}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
  chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.pill}"
    padding: 6px 12px
  category-rail:
    backgroundColor: "{colors.surface-page}"
    textColor: "{colors.text-primary}"
    padding: 12px 8px
---

# Design Analysis: 众享源品 - 在线商城

> Analysis generated with the `anydesign` skill. Date: 2026-09-18. Emphasis: reconstruction + design system

## Source

- **Source type**: 本地 PNG 设计图（iPhone 竖屏导出，多数 1125×2436，首页 1125×5477）
- **Path / URL**: `docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/`（SRC-UI-003，引用不复制）
- **Capture method**: 直接读图 + `extract_colors.py --top 8` + 关键区域像素取样。未跑 URL/Figma。
- **Detected limitations**: 无矢量、无 CSS 变量、无交互态帧；字号/间距由 3x 位图反推，标 ⚠️。618 大促物料是季节图，不锁进令牌。AI 视频 5 张本批不做。AI 助手 4 张只抽令牌、不像素验收（DEC-008）。
- **Decision overlays（覆盖图面，不是猜测）**:
  - **UI-DEC-002**：图上底栏第四坑写「发现」→ 重建必须改成「购物车」，图标暂用发现资源；发现业务仍不做。
  - **UI-DEC-003**：金主按钮深字；底栏结构听整栏五坑图、中间 AI 橙红标；《Tab Bar交互》上半仅侧边交互、下半仅列表空态；详情主价 `price-xl`；首页右上购物袋保留。
  - **UI-DEC-004**：首页横向分类选中观感听组 A（黑底、星、尾巴），实现听现码三件套（同盒 CSS 黑底 + 独立星 + CSS 三角），不升级系统 `chip` 浅金。禁止整图拉伸。UI_SPEC 0.1.2 已批准。
  - **DEC-071 v1.1.0**：不编造假入口，树上有的一级照出。左栏选中浅金+外侧上下箭头切图，不把格子加高。二级选中用代码金气泡+三角，组 B 整图只作观感参考、禁止拉伸。外底板/左栏竖条/二级槽/三级内白卡分层。
  - **UI-DEC-005 / DEC-071 v1.3.0**：分类外底板听现状。圆角分层：外底板 `16rpx`，竖条与选中金卡 `10rpx`。底色奶油落到页灰 + `16rpx` 内边距。不对《分类.png》米金条。不升 locked 令牌。
  - **UI-DEC-006**：左栏选中白边包金芯、箭头在内、选中加高；竖条禁止 `side-bg.png` 拉伸；三级 CSS grid 三列；全部分类面板内可滚。32A 不得按 0.1.3 旧句改回。UI_SPEC 0.1.5 Approved。
  - **附近文件名**：超市便利、生鲜果蔬、优选超市、美团团购、数码百货、看病买药、鲜花绿植等板块删除且不对接。
  - **DEC-073**：附近详情距离/驾车本袋不验收。

## TL;DR

这是一套「金顶栏 + 白卡片 + 橙红价」的消费电商皮肤。品牌时刻是顶区 `{colors.brand-gold}` (#FFC31B) 洗下来的渐变，不是产品摄影里的杂色。底栏选中用 `{colors.accent-lime}` (#A6F342)，不要把青柠绿铺到按钮和价格上。重建栈是 UniApp Vue3 `go-uni-app-online`、750rpx，本机 5176→8035；本文件只定令牌和零件，**未确认前不得换皮**。

## 1. Visual identity

### 1.1 Surface description

**Personality** (3-5 adjectives): 热闹、促销感、市民、圆润、信息密

**Mood**: 像社区团购/下沉电商首页——顶上先用金黄把人拉进「今天有活动」，下面再用白卡片把货摆出来。不是极简精品店。

**Detectable stylistic references**: 国内主流电商 App（顶栏金/橙、底栏卡通图标、双列商品卡）。不是 Linear/Vercel。

**Information density**: 高。首页一屏里同时有搜索、公告、活动宫格、秒杀横条、品牌卡、双列货。

**Implicit positioning**: 价格敏感的日常采购，而不是设计师品牌。售价永远比标题更抢眼。

**Confidence**: ✅ high — 首页、分类、列表、我的、附近顶栏同一套金顶 + 灰底。

### 1.2 Brand voice / Atmosphere

**先把「今天能买到便宜货」写在天上，再把货码在桌上。** 金顶栏占掉状态栏到搜索条的整段天空，不是一条 44pt 导航；它告诉用户这是会场，不是后台。白卡片和浅灰页底把商品摄影托住，避免金黄把货染脏。橙红价是第二声：标题可以灰、划线价可以灰，现价必须烫手。底栏那点青柠绿像活动贴纸，只在「你现在站在哪一坑」时亮一下——如果按钮也涂成这种绿，会场就变成儿童贴画。

### 1.3 The "ONE brand thing"

- **The thing**: 顶区金黄洗墙 `{colors.brand-gold}` (#FFC31B) → 过渡到 `{colors.surface}` / `{colors.surface-page}`。
- **Why it carries the brand**: 去掉金顶，剩下的白卡片+灰底可以是任何商城；有金顶才是这套「公益优选/源品」会场。
- **How everything else supports it**: 页面主体克制在白/浅灰；青柠绿不进顶栏、不进价签、不进主按钮。
- **Where it appears (and where it deliberately doesn't)**: 首页/分类/搜索/列表/我的/附近的顶区；商品摄影区、详情主图、列表卡片底 **不要**铺金。

**Confidence**: ✅ high

## 2. Design System (tokens)

像素取样与 `extract_colors.py` 对齐。摄影区会贡献大量 `#DCB770` / `#BB6F60`，那是图，不是令牌。令牌取自重复出现的 **chrome**（顶栏、搜索、底栏、价签、按钮）。

### 2.1 Colors

| Token | Hex | Role | Where it appears | Confidence |
|---|---|---|---|---|
| `brand-gold` | `#FFC31B` | 品牌金 / 顶栏主色 | 首页/分类/搜索/列表/我的/附近顶区；AI 助手顶区 | ✅ high |
| `brand-gold-deep` | `#FEC001` | 金顶略深 | 顶栏左侧、搜索条背后 | ✅ high |
| `brand-gold-soft` | `#FFD854` | 浅金高光 | 顶栏向白过渡、分类选中胶囊 | ⚠️ medium |
| `surface` | `#FFFFFF` | 卡片 / 底栏 / 输入条 | 商品卡、底栏、搜索胶囊内填 | ✅ high |
| `surface-page` | `#F6F6F6` | 页底 | 首页中段、搜索历史页大面积 | ✅ high |
| `text-primary` | `#222222` | 主文案 | 标题、商品名、底栏未选中描边 | ✅ high |
| `text-muted` | `#989898` | 次文案 | 底栏未选中、销量、占位提示 | ✅ high |
| `inverse` | `#FFFFFF` | 反白字 | 黑搜索按钮、深底促销条。**不用**在金主按钮上（UI-DEC-003） | ✅ high |
| `price` | `#FD5800` | 现价 | 首页双列、列表；详情主价同色但更大 | ✅ high |
| `promo` | `#F87000` | 促销条 / 描边 CTA | 详情「百万补贴」条、加入购物车描边 | ⚠️ medium |
| `accent-lime` | `#A6F342` | 底栏选中填色 | Tab 图标 stretch / 选中 | ✅ high |
| `accent-lime-hi` | `#EAFF76` | 底栏高光 | 《Tab Bar交互》图标高光 | ⚠️ medium |
| `search-cta` | `#111111` | 搜索实心按钮 | 分类/搜索页右侧「搜索」胶囊 | ✅ high |
| `border` | `#E8E8E8` | 细分割 | 卡片缝、底栏顶线（弱） | ⚠️ medium |

无深色模式截图。不要把摄影平均色写进令牌。

### 2.2 Typography

- **Declared family**: 未嵌入字体文件。视觉为中文系统黑体（PingFang SC / 系统 UI）。⚠️ medium
- **Fallback chain**: `PingFang SC, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif`
- **UniApp 落地**: 逻辑像素 ×2 = rpx（375 宽 → 750rpx）。`14px` → `28rpx`。

| Token | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| `display` | 20px / 40rpx | 600 | ~1.2 | 列表/首页双列现价 |
| `price-xl` | 28px / 56rpx | 600 | ~1.2 | 详情主价（UI-DEC-003） |
| `title` | 17px / 34rpx | 600 | 1.2 | 导航标题「商品分类」 |
| `body` | 14px / 28rpx | 400 | 1.4 | 商品名、工具列表 |
| `caption` | 12px / 24rpx | 400 | 1.3 | 副标题、底栏文案 |
| `caption-mono` | 11px / 22rpx | 400 | 1.2 | 「已售 xx 件」、划线价 |

**Notable tracking**: 无明显负字距。数字价略紧。⚠️
**Weights used**: 400、500（胶囊）、600（标题/价）。未见 700 大面积使用。

### 2.3 Spacing

- **Inferred base unit**: 4px 逻辑（8rpx）。常见 8 / 12 / 16。
- **Observed multiples**: 卡片内 12px；列沟约 8–12px；底栏图标区高度约 50px 逻辑（含文案）。
- **Consistency**: ⚠️ medium — 位图，未量到完整 8px 网格证据，但没有奇怪的 5/7px 节奏。

### 2.4 Radii

- `{rounded.sm}` 8px：小标签
- `{rounded.md}` 12px：排序条、弱卡片
- `{rounded.lg}` 16px：商品卡、我的页资产卡
- `{rounded.pill}` 999px：搜索条、黑搜索按钮、立即购买、历史胶囊、分类横向胶囊
- 分类右侧品类图：**正圆**（50%），不是 token 圆角

系统是「胶囊控件 + 圆角卡片」，不要把主按钮做成 4px 方钮。

### 2.5 Elevation system

| Level | Name | Treatment | Use |
|---|---|---|---|
| 0 | Page | `{colors.surface-page}` 平涂 | 页底 |
| 1 | Card | `{colors.surface}` + 轻阴影 `{shadows.card}` 或无描边 | 商品卡、我的订单卡 |
| 2 | Float | 白底 + `{shadows.tab}` 顶发丝 | 底栏、详情底栏 |

**Philosophy**: 主要靠灰底托白卡，不是厚投影。金顶是装饰性纵深（上金下白），不是 elevation token。

**Confidence**: ⚠️ medium — 阴影半径从位图估计。

#### Decorative depth (non-functional)

- 顶区金黄径向/纵向渐变，向页面中上部收成白。
- 首页大促主视觉是摄影+插画，季节性，重建用运营位，不要写进 colors。

### 2.6 Borders

- 默认约 0.5–1px `{colors.border}`；多数卡片靠底色差而不是描边。
- 加入购物车：1px `{colors.promo}` 描边 + 白底。
- 搜索条在金顶上时：**白填充胶囊**，外圈几乎无描边。
- 焦点态未见（静态图）。

### 2.7 Accessibility quick-check

见 companion `design-a11y.md`。摘要：

- `{colors.text-primary}` on `{colors.surface}`：15.91:1 — AAA ✅
- `{colors.text-muted}` on `{colors.surface}`：2.88:1 — **普通字 AA 失败**。底栏未选中、占位符本身如此；长文案不要用 muted。
- `{colors.price}` on `{colors.surface}`：3.2:1 — 仅 AA large；正文级不要用。
- `{colors.inverse}` on `{colors.brand-gold}`：1.61:1 — **失败**。已定不采用：主按钮用 `{colors.text-primary}` 压金（9.91:1 AAA，UI-DEC-003）。
- `{colors.inverse}` on `{colors.search-cta}`：18.88:1 — AAA ✅

## 3. Components Inventory

### 3.1 Generic components

#### nav-gold-header

- **Variants**: 首页（搜索条沉在金黄里，左「首页/特价/新品」+ **右上描边购物袋保留**，进购物车，UI-DEC-003）；内页（返回 + 居中标题，金黄向白过渡）
- **Sizes**: 顶区高于标准 44pt，含状态栏；内页搜索条压在过渡带上
- **Visible states**: 仅默认。滚动吸顶未见
- **Padding/Radius**: 水平约 16px；自身无圆角，下方内容卡片才圆
- **Confidence**: ✅ high

#### search-bar

- **Variants**: ① 首页：白胶囊 + 左放大镜 + 占位文案，**无**黑按钮，右可能是独立圆形搜索/购物车；② 分类/搜索页：白胶囊 + 右侧实心 `{colors.search-cta}` 「搜索」
- **Sizes**: 高度约 36px 逻辑 / 72rpx
- **Visible states**: 占位 `{colors.text-muted}`；输入态未见
- **Padding/Radius**: `{rounded.pill}`；内边距 8×12
- **Confidence**: ✅ high

#### tab-bar

- **Variants**: **结构真源是整栏五坑图**（白底、中间缺口抬高）：购物 / 附近 / AI助手 / 发现 / 我的。**重建覆盖（UI-DEC-002）**：第四坑文案改「购物车」，进现有购物车，发现业务不做；图标暂用发现造型。
- **《Tab Bar交互》不是完整底栏（UI-DEC-003）**：上半只给四个侧边图标的选中/未选中（灰线稿 ↔ `{colors.accent-lime}`）；下半是列表到底空态，见 3.2。
- **Sizes**: 底栏含安全区；中间 AI 大于两侧、凸在缺口里
- **Visible states**: 侧边未选中灰线稿；选中青柠填色。**中间 AI 固定为橙红圆形 AI 标**（整栏图），不得改成青柠卡通。
- **Padding/Radius**: 白底；顶发丝 `{shadows.tab}`
- **Confidence**: ✅ high（结构与 AI：整栏图 + UI-DEC-003）

#### goods-card

- **Variants**: 首页双列（上图下文，圆角白卡）；列表小图（左方图右文，白行卡）
- **Sizes**: 双列约各半减沟；列表行高随图约 120px 逻辑
- **Visible states**: 默认。无悬停（触屏）
- **Padding/Radius**: `{rounded.lg}`；图上圆下连文或图单独圆角
- **Confidence**: ✅ high

#### button-primary

- **Variants**: 详情底栏「立即购买」金胶囊；我的页「个人主页」小金胶囊
- **Sizes**: 详情主按钮高度约 44px 逻辑（够触摸）；小胶囊更扁
- **Visible states**: 仅默认
- **Padding/Radius**: `{rounded.pill}`；`{colors.brand-gold}` 填，`{colors.text-primary}` 字（UI-DEC-003，不跟详情 PNG 白字）
- **Confidence**: ✅ high

#### button-cart

- **Variants**: 详情「加入购物车」白底 + `{colors.promo}` 描边与字
- **Sizes**: 与立即购买并排，略窄
- **Visible states**: 仅默认
- **Padding/Radius**: `{rounded.pill}`
- **Confidence**: ✅ high

#### chip

- **Variants**: 搜索历史浅底胶囊；**分类二级选中**用同盒 CSS 金底 + 渐变 + 白字 + CSS 倒三角（DEC-071 v1.1.0 / UI_SPEC 0.1.3），不是组 B 整图拉伸；列表排序「综合排序」下划金条；**首页横向分类选中**用同盒 CSS 黑底 + `MAT-GO-ASSET-HOME-CHIP-STAR` + CSS 三角（UI-DEC-004 / UI_SPEC 0.1.2），不是系统浅金，也不是组 A 整图拉伸
- **Sizes**: 首页横向分类与未选中同盒：高 56rpx、圆角 76rpx、左右 33rpx；三角不算进盒子。分类二级未选中白胶囊与选中胶囊同高、同样大圆角、顶底对齐，倒三角不算进盒子。其它 chip 高度约 28–32px 逻辑
- **Visible states**: 默认选中金 / 未选白或透明。首页横向分类选中除外：黑底 `#222222` + 独立青柠星 + CSS 下三角 + 白字。分类二级选中除外：金底 + 白字 + CSS 倒三角 + 整块阴影
- **Padding/Radius**: `{rounded.pill}`；首页/分类二级选中与未选中同一套盒子，禁止长文案拉变形
- **Confidence**: ✅ high

#### category-rail

- **Variants**: 左窄栏一级类目，选中浅金底 + 外侧上下箭头切图；右侧分组落在三级内底板白卡上 + 3 列圆图
- **Sizes**: 左栏约 88–96px 逻辑宽；每项同一宽高，第一项不收窄
- **Visible states**: 选中/未选中。**DEC-071 v1.1.0**：树上有的一级照出，不编造假入口；选中不把格子加高；箭头贴在选中项外侧。顶底两态：有内容被裁切时渐变溶进外底板；无裁切时顶底同等圆角和边距
- **Padding/Radius**: 左栏单独竖条皮；外底板顶白边 + 米金渐变；右侧模块内底板白卡 `{rounded.lg}`
- **Confidence**: ✅ high（结构）；覆盖项见 DEC-071 v1.1.0

### 3.2 Signature components

**金顶会场头**（即 `nav-gold-header`）：这是品牌签名，不是普通 AppBar。内页把标题放在渐变里，搜索条骑在金/白交界。

**列表到底空态**（《Tab Bar交互》**下半**，与底栏无关）：浅紫警告标 + 「别再搜，我到底啦~」`{colors.text-muted}`。换皮列表到底沿用这句。

**No extra signatures**：不要发明吉祥物主 KV。中间 AI 用橙红标，不是图 1 的蘑菇。

## 4. Layout & Composition

### 4.1 Grid & containers

- **Canvas**: 设计稿 1125 宽 ≈ 375pt @3x。落地 **750rpx**，H5 预览视口 390×844。
- **Horizontal padding**: 约 12–16px 逻辑（24–32rpx）
- **Home grid**: 活动 5 宫格；商品双列；秒杀横滑
- **Category**: 左 1 + 右 3 列圆图
- **List**: 单列左图右文
- **Vertical rhythm**: 模块标题行 32–48px 逻辑；模块间距约 12px

### 4.2 Composition patterns

- **会场头**: 金洗墙 + 搜索条 + 运营主 KV
- **工具宫格**: 首页 5 个活动入口；我的订单 5 图标；附近顶部分类宫格（其中文件名点名的 **不实现**）
- **双列货架 / 单列清单**
- **详情**: 通栏主图 → 促销条 → 价 → 标题 → 规格/配送行 → 评价 → 详情图；底栏左购物图标 + 双 CTA
- **我的**: 头像行 + 三列资产 + 订单卡 + 常用工具 + 列表箭头

### 4.3 Responsive behavior

#### Breakpoints

| Name | Width | Key changes |
|---|---|---|
| 源品 H5 / App 逻辑 | 375pt / 750rpx | ✅ 全部 PNG 都是这一档 |
| 平板/桌面 | ≥ 768px | ❓ 无稿。禁止擅自改双列变四列 |

五端同一套 `go-uni-app-online`，条件编译只处理平台 API，不另做一套视觉（ADR/DEC-008）。

#### Touch targets

- 底栏、立即购买、搜索按钮视觉高度 ≥ 36px，多数贴近 44px。⚠️ 未逐个量。
- 分类左栏文字按钮偏窄，换皮时命中热区不要小于 44px 高（可透明扩大，视觉仍同尺寸——符合 DEC-071）。

#### Collapsing strategy

- 无多断点。横滑模块保持横滑，不要改成自动换行宫格，除非现码已如此且用户点名。

### 4.4 Image behavior

- **商品摄影**: 占卡片上半或列表左侧，圆角随卡。
- **分类圆图**: 正圆裁切，上下留品名。
- **运营 KV**: 首页/附近顶 Banner，圆角约 `{rounded.lg}`。
- **底栏图标**: 侧边选中态听《Tab Bar交互》上半；整栏布局与中间 AI 听整页底栏图（UI-DEC-003）。
- **空态插画**: 列表到底用《Tab Bar交互》下半，不要当成底栏。

## 5. Reconstruction Notes

### Suggested stack

**UniApp Vue3（`go-uni-app-online`）+ 750rpx + 现有路由/API。** 证据：这是源品 C 端唯一真源；禁止 `/v2` 业务双轨。本机热更新 5176，接口 8035。换皮是原地换视图，不新建路由。

### Quick wins

- 把 `{colors.brand-gold}` / `{colors.surface-page}` / `{colors.price}` / `{colors.accent-lime}` 写成 CSS 变量或 SCSS map，顶栏和价签立刻像这套皮。
- 搜索条做成白胶囊；分类/搜索页右侧黑「搜索」，首页不要硬造黑按钮。
- 底栏五坑按整栏图做结构，第四坑文案按 UI-DEC-002；首页右上购物袋保留（UI-DEC-003）。

### Tricky bits

- 金顶是 **渐变会场**，不是 `navigationBarBackgroundColor` 一块纯色能糊弄的；内页还要把搜索条骑在金白交界。
- 金主按钮必须 `{colors.text-primary}` 压金，不要白字（UI-DEC-003）。
- 底栏中间 AI 必须跟整栏图橙红标；《Tab Bar交互》上半只约束侧边四图标交互，下半只约束列表空态。
- 分类页 DEC-071 与 PNG 不一致：按决策不按「甄选上新」加高。
- 附近 PNG 与文件名互斥：文件名删除的生活服务板块 **不要画、不要对接**；店列表骨架、顶搜索、顶灯片仍可对。CPS 听 PRD 两行本页轮播，不对图上静宫格。距离/驾车/让利听 DEC-073，不对图上米数。
- 字体未授权：用系统黑体，不要私自换思源/阿里巴巴字体除非另有资产。

### Implicit states to define

按钮按压/禁用、搜索焦点、列表加载骨架、列表空、分类右栏空、未登录我的（图已给「登录/注册」）、底栏选中。悬停不做。

### Confidence map

| Layer | Confidence | Why |
|---|---|---|
| Identity | ✅ high | 多页金顶一致 |
| Colors (chrome) | ✅ high | 取样 + extract_colors 交叉 |
| Colors (摄影衍生) | 🚫 不用 | 平均色会脏 |
| Typography | ⚠️ medium | 无字体文件，字号反推 |
| Spacing / radius | ⚠️ medium | 位图估计 |
| Components | ✅ high | 搜索/卡/底栏/按钮重复出现 |
| Tab structure | ✅ high | 整栏五坑图 + UI-DEC-003 |
| Tab label | 覆盖 | UI-DEC-002 第四坑购物车 |
| Layout (375) | ✅ high | 全是竖屏稿 |
| 其它断点 | ❓ low | 无稿 |

## 6. Do's and Don'ts

### Do

- **把 `{colors.brand-gold}` (#FFC31B) 用在顶区洗墙和主购买按钮**，字用 `{colors.text-primary}` 压金（UI-DEC-003）。
- **现价只用 `{colors.price}` (#FD5800)**；列表/首页用 `{typography.display}`，详情主价用 `{typography.price-xl}`。
- **底栏结构听整栏图，中间 AI 用橙红标**；侧边选中填 `{colors.accent-lime}`；第四坑文案写「购物车」（UI-DEC-002）。
- **首页金顶右上购物袋保留**，与底栏购物车并存（UI-DEC-003）。
- **搜索内页右侧用 `{colors.search-cta}` 黑胶囊「搜索」**；输入条本身保持白底 `{rounded.pill}`。
- **卡片放在 `{colors.surface-page}` 上用 `{colors.surface}` + `{rounded.lg}`**，不要给每张卡加 2px 金边。
- **分类右栏继续 3 列圆图**；左栏选中用浅金底但 **同高度**（DEC-071）。
- **单位用 rpx**（px×2）；五端同一套，不要按端改色。

### Don't

- **不要在金主按钮上用 `{colors.inverse}` 白字**（UI-DEC-003）。白字只给黑「搜索」等深底。
- **不要把《Tab Bar交互》当成完整底栏**，也不要用它的青柠卡通替换中间 AI。
- **不要按 PNG 把第四坑做成「发现」列表/关注/内容流**（REQ-063 / UI-DEC-002）。
- **不要编造树上没有的一级，也不要把左栏选中格子加高成另一套**（DEC-071 v1.1.0）。
- **不要把组 B 整图当分类二级选中底拉伸**；箭头用组 C/D 切图贴外侧。
- **不要实现附近图上的超市便利、生鲜果蔬、优选超市、美团团购、数码百货、看病买药、鲜花绿植**（文件名删除板块）。CPS 两行轮播保留；跳转不由视觉循环改。
- **不要把 extract_colors 的摄影平均色（如 `#DCB770`）写成品牌色**。
- **不要新建 `/v2` 路由或 HTML 壳做对照**；未点名页不要改 `tabbar/index.vue`。
- **不要把手改 `design-tokens.json`**；改令牌只改本 `design.md` 再跑 `build_tokens_json.py`。
- **不要把 AI 视频/生图 5 张列入换皮范围**；AI 助手页不要像素验收。

## 7. Open Questions

- 金主按钮深字压金、底栏听整栏图、中间 AI 橙红标、详情 `price-xl`、首页右上购物袋保留：已确认，见 UI-DEC-003。
- 首页横向分类选中听 UI-DEC-004 观感：已确认。实现口径见 UI_SPEC 0.1.2 Approved（同盒三件套）。不升级 `chip` 令牌。
- 系统黑体是否以后换成品牌字体？当前按系统黑体，未另投字体资产。
- UI_SPEC 0.1.3 已 Approved。当前真源 `UI_SPEC.md`。Contract 0.1.3 已同步。不得把手改 `design-tokens.json` 当本覆盖的落地。

## 8. Companion files

- `../tokens/design-tokens.json` — 由 `build_tokens_json.py` 从本文件 frontmatter 导出（DTCG）
- `./design-a11y.md` — `check_contrast.py` 输出
- `../MATERIALS_MANIFEST.yaml` — SRC-UI-003 引用登记
- `docs/project/ui-design/UI-DEC-002.md` — 第四坑购物车
- `docs/project/ui-design/UI-DEC-003.md` — 令牌四条与底栏真源
- `docs/project/ui-design/UI-DEC-004.md` — 首页横向分类选中页面覆盖
- `../assets/` — 切图；组 A/星启用；组 B 观感参考禁止拉伸；组 C/D 箭头启用（DEC-071 v1.1.0）
- 设计图真源仍在 `docs/project/sources/inbox/BATCH-003/在线商城前端页面UI/`
