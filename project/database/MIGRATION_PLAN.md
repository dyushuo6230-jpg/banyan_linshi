# 迁移与回滚

| 字段 | 值 |
|---|---|
| 文档名称 | 迁移与回滚 |
| 文档编号 | DB-G9-MIG |
| 版本 | 0.1.1 |
| 状态 | Baselined |
| 负责人 | TBD |
| 创建日期 | 2026-09-05 |
| 更新时间 | 2026-09-05 |
| 关联来源 | ADR-042、DEC-011、DEC-014、DEC-017、G8 各模块 §10、CURRENT_BASELINE `nunu-go-api/deploy/sql` |
| 关联需求 | REQ-001～REQ-120 |
| 关联决策 | G9-DRAFT=A |
| 适用版本 | 文档体系 v0.1.3 |
| 替代文档 | 无 |

不灌库。生产清库 **不批准**。本期测试可清库（DEC-017）只约束测试环境。

以后凡改真表，**先遵循**本节 `deploy/sql` 增量规范，再按第 3 节业务步骤落地。`ALLOW_CODE_CHANGES=true` 后，Ready 批次可写入 `deploy/sql/`；本文件仍不代替具体 SQL。

## 1. 改表落点（现行工程规范）

口诀：**dump 是底子，增量 SQL 改真表，GORM 结构体是说明书。**

| 项 | 口径 |
|---|---|
| 底子 | 本地/测试空库先导入现行 dump，再按编号执行增量 |
| 增量唯一正路 | `nunu-go-api/deploy/sql/` |
| 文件名 | `NN-简短说明.sql`；编号接着该目录**当前最大号加一**，不跳号抢号，不复用已归档旧号 |
| 可重复执行 | 必须。加列/加索引/补菜单先查是否已存在，有则跳过（`information_schema` / `NOT EXISTS`），与现码 `01`、`02` 同风格 |
| 同提交 | 有 `ALTER` / `CREATE` / 改菜单 SQL，必须同时改 `nunu-go-api/model/` 对应 struct 的 type、size、可空、comment；只改 struct 没有 SQL **禁止**合入 |
| 新表 | SQL 建表 + struct 说明书。不要把新表塞进 `AllModels()` 指望 AutoMigrate |
| 执行顺序 | 本地跑完 → 测试跑同一份 → 正式**只跑这一份** |
| 正式库 | 有真实租户和订单，**禁止** DROP 后整库导入 dump |

禁止：

- `make migrate`
- GORM AutoMigrate 当发布或对齐测试/正式库的手段
- 启动时 AutoMigrate 建表/改表
- 把归档目录里的旧编号 SQL 再按历史顺序重跑

以已经进库的 dump + 已执行增量 SQL 为准；struct 对不齐时改说明书，不让库迁就 AutoMigrate。

本窗获准改业务代码后，本期树/入驻/池/快照等改表必须按本规范出可重复执行的增量 SQL。DEV-001 可写树相关增量；入驻/池/快照分属后续批次。

## 2. 原则

- 先加列/加表，再切读写，最后才考虑弃用旧权威。
- 回滚代码不得把已确认规则倒回去（例如再把店铺 `commission_rate` 当新单权威，或再把 `merchant_category` 当新申请主数据）。
- 无消息队列补偿要求（ADR-005）。
- 回滚脚本若需要，同样放 `deploy/sql/` 新编号文件，且可重复执行；不得靠 AutoMigrate 回滚。

## 3. 分步（逻辑；实施时写成增量 SQL）

| 步 | 谁 | 做什么 | 回滚 |
|---|---|---|---|
| 树种子 | 实施 | `02-business-tree.sql`：四业态根；缺则补。费率 NULL。显示名可后改 | 不删根 |
| 菜单四套模板 | 实施 | `05`～`09`：现网单树标餐饮并复制三套；按已点名 DEC 删行；在线商城补店铺资料 | 可恢复单树（回滚另出 SQL） |
| 树只读切换 | `onboarding`/`goods`/`trade` | 新申请/新发品/新单读树 | 旧扁平类目可留只读 |
| 通用平台类目种子 | 实施 | `04-goods-category-seed.sql` 写入 `goods_category`（DEC-012 示例树，名称可改；费率 NULL） | 可软删节点；不删业态根 |
| 入驻绑定 | `onboarding` | `10-merchant-onboarding-binding.sql`：新申请写业态与一级；过审写店铺绑定；存量待审不猜业态 | 已通过绑定保留 |
| 无业态老店 | 实施 | 默认餐饮；已是餐饮跳过；`is_self=1` 不迁在线商城 | 不自动改回无业态 |
| 商品 | `goods` | 本地生活上架即可售、平台不审；在线商城送审。`13-goods-audit.sql` 只加批审 API。不把已通过改回待审（DEC-017/026） | 不把已通过改回待审 |
| 待审拼团秒杀 | `group-seckill` | 改未上架，不自动开卖（DEC-014） | 不恢复平台审场次为必验 |
| 用户池 | `user` | 存量视为店铺池。列落地 DEC-045：`12-user-pool.sql` 加 `user_pool` / `order_info.user_pool` | 不得拆成两张用户表 |
| 订单快照 | `trade` | 新单写节点费率快照；历史已付不重算 | 不重算旧单 |
| mall-online | 实施（DEV-010 Ready 未合入） | 共库；不建独立用户表；本机 8035（DEC-049） | 回退进程，不动拆表 |
| h5-online | 实施（DEV-010 overlay） | 整包静态；本机 8036；无独立库 | 回退该二进制，不动库 |

## 4. 明确不做

- 并 `goods_category` 静默删表或灌数（DEC-021：本批不并表删除，只加费率列）
- 把 `merchant_id=0` 迁成众享源品 - 在线商城
- 删除平台 `banner` 表
- 删除小魔推 / 推广员现码表
- 为众享源品 - 在线商城新建用户表
