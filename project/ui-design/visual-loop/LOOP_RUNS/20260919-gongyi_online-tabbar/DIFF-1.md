# DIFF-1

- 运行：20260919-gongyi_online-tabbar
- 圈次：1
- 实现截图：actual-1.png（底栏条；全页 actual-1-full.png）
- 设计图：`个人页2.png` 页脚结构；《Tab Bar交互》上半仅侧边选中色。视口 390×844。`padding-bottom` 实测 `0px`（H5 无 Home 条）
- 令牌：`design-tokens.json`（`accent-lime` `#A6F342`、`text-muted` `#989898`、`text-primary` `#222222`）
- 合同覆盖：第四坑购物车 + 发现图标；中间 AI 橙红标；不把《Tab Bar交互》当完整底栏

| id | 位置 | 类型 | 现在 | 目标 | 严重程度 | 建议文件 |
|---|---|---|---|---|---|---|
| D1 | 底栏五字下方到栏底 | 间距 | 文案底到 `.tabbar-v2` 底 **15.6px**（`padding-bottom: 30rpx`） | 听 `个人页2.png` 页脚：字贴白底下沿（H5 无 Home 条，不留这一截空带） | 挡验收 | `tabbar/index.vue` |
| D2 | 第四坑文案 | 文案 | 「购物车」 | 合同 UI-DEC-002，不对图上「发现」 | 覆盖豁免 | — |
| D3 | 栏底安全区 | 尺寸 | `env(safe-area-inset-bottom)=0` | 不对设计图 iPhone Home 条 | 覆盖豁免 | — |
| D4 | 五坑 / 中间抬高 / 橙红 AI / 选中青柠 | 颜色 / 显隐 | 已与合同 + 页脚结构一致 | 保持 | 不修 | — |

本圈不改代码。D1 不是整页改布局，第 2 圈只收 `padding-bottom`。
