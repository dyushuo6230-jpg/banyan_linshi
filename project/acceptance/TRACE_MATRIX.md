# 追踪矩阵

| 字段 | 值 |
|---|---|
| 文档名称 | 追踪矩阵 |
| 文档编号 | TRACE_MATRIX |
| 版本 | 0.1.0 |
| 状态 | Approved |
| 负责人 | TBD |
| 创建日期 | 2026-09-04 |
| 更新时间 | 2026-09-17 |
| 关联来源 | SRC-REQ-001、SRC-REQ-002、SRC-REQ-003、SRC-CODE、SRC-UI-001、SRC-UI-002、SRC-UI-003、SRC-CHANGE-001 |
| 关联需求 | REQ-001～REQ-120、REQ-130～REQ-134 |
| 关联决策 | DEC-001～DEC-073、ADR-045、CR-006～CR-051 |
| 适用版本 | 文档体系 v0.1.44 |
| 替代文档 | 无（G0 空表） |

开发批次列已填 Planned 批次号（ADR-045）。架构、技术设计、API、数据、测试、发布列未实施前仍为 `—`。UI_SPEC / UI Contract 本期关闭，填 `N/A`。视觉验收本期不启用。当前业务真源 **PRD v0.1.44 Approved**（CR-051 / DEC-073）。上一 **v0.1.43 Approved** 只读。不是 Baselined。

| 需求编号 | 来源编号 | DEC | 模块 | 需求变化 | 结论标签 | 开放项状态 | 架构 | 技术模块/设计 | API/数据 | UI_SPEC | UI Contract | 开发批次 | Commit/PR | 测试 | 视觉验收 | 业务验收 | 发布版本 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | SRC-REQ-001 | DEC-001、DEC-046、DEC-047 | M01 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-001 | — | 自测 | N/A | 通过 | — |
| REQ-002 | SRC-REQ-001 | DEC-001、DEC-021、DEC-046 | M01 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-001 | — | 自测 | N/A | 通过 | — |
| REQ-003 | SRC-REQ-001、DEC-032 | DEC-001、DEC-032、DEC-044 | M01 | 修改 | 已确认 | 在线商城强制 1～3 个一级 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-004 | DEC-001 | DEC-001、DEC-021、DEC-055、DEC-058 | M01 | 修改 | 已确认 | 空或 0 不抽佣 | — | — | — | N/A | N/A | DEV-001 | — | — | N/A | 未开始 | — |
| REQ-005 | DEC-001 | DEC-001 | M01 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-001 | — | 自测 | N/A | 通过 | — |
| REQ-006 | DEC-011、DEC-001、DEC-006 | DEC-011 | M01 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-001 | — | 自测 | N/A | 部分 | — |
| REQ-007 | DEC-012、DEC-001、SRC-REQ-001、DEC-035 | DEC-012、DEC-021、DEC-035 | M01 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-001 | — | — | N/A | 未开始 | — |
| REQ-010 | SRC-REQ-001、SRC-CODE-006 | DEC-043 | M02 | 保留 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-011 | SRC-REQ-001、DEC-001、DEC-032 | DEC-001、DEC-032 | M02 | 修改 | 已确认 | 资质沿用现码执照 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-012 | DEC-006 | DEC-006 | M02 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-013 | SRC-CODE-001 | DEC-044 | M02 | 保留 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-014 | DEC-002、DEC-011 | DEC-002、DEC-011 | M02 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-003 | — | — | N/A | 进行中 | — |
| REQ-020 | DEC-002 | DEC-002 | M03 | 保留 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 通过 | — |
| REQ-021 | DEC-002 | DEC-002 | M03 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 通过 | — |
| REQ-022 | DEC-002、SRC-REQ-001 | DEC-002 | M03 | 新增 | 已确认 | 待配置（文案） | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 部分 | — |
| REQ-023 | SRC-REQ-001、DEC-002、DEC-020、DEC-028、DEC-031、DEC-039、DEC-046 | DEC-020、DEC-028、DEC-031、DEC-039、DEC-046 | M03 | 修改 | 已确认 | 周边与模块归属 DEC-046 | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 通过 | — |
| REQ-024 | SRC-REQ-001、DEC-002、DEC-004、DEC-039 | DEC-002、DEC-004、DEC-039 | M03 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 通过 | — |
| REQ-025 | SRC-REQ-001、DEC-002、CR-033、DEC-065 | DEC-002、DEC-065、CR-033、CR-040 | M03 | 修改 | 已确认 | 非超管必须有角色；四项不对普通角色开放 | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 部分 | — |
| REQ-030 | SRC-REQ-001、SRC-CODE-003、DEC-026、DEC-017、DEC-030、DEC-035 | DEC-026、DEC-017、DEC-030、DEC-035 | M04 | 保留 | 已确认 | 店内分类停用不可再售 | — | — | 13-goods-audit.sql | N/A | N/A | DEV-006 | — | — | N/A | 部分 | — |
| REQ-031 | SRC-REQ-001、DEC-012、DEC-030 | DEC-012、DEC-021、DEC-030、DEC-043、DEC-055、DEC-057 | M04 | 修改 | 已确认 | 无 | — | — | 13-goods-audit.sql | N/A | N/A | DEV-006 | — | — | N/A | 部分 | — |
| REQ-032 | SRC-REQ-001、DEC-026、DEC-018、CR-007 | DEC-026、DEC-018、DEC-044 | M04 | 修改 | 已确认 | 无 | — | — | 13-goods-audit.sql | N/A | N/A | DEV-006 | — | — | N/A | 部分 | — |
| REQ-033 | DEC-009、SRC-REQ-001、SRC-CODE-001 | DEC-009 | M04 | 保留 | 已确认 | 无 | — | — | 13-goods-audit.sql | N/A | N/A | DEV-006 | — | — | N/A | 部分 | — |
| REQ-034 | DEC-012、SRC-REQ-001、DEC-001、DEC-035 | DEC-012、DEC-021、DEC-035、DEC-044、DEC-055、DEC-057、DEC-058 | M04 | 修改 | 已确认 | 不冻结节点清单 | — | — | 13-goods-audit.sql | N/A | N/A | DEV-006 | — | — | N/A | 部分 | — |
| REQ-040 | SRC-REQ-001 | DEC-001、DEC-046 | M05 | 保留 | 已确认 | 周边/CPS 已插入编码；履约主体仍 DEV-007 | — | — | — | N/A | N/A | DEV-007 | — | — | N/A | 部分 | — |
| REQ-041 | SRC-REQ-001 | DEC-047、DEC-051、DEC-054、DEC-057、DEC-060、DEC-061、CR-034 | M05 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-007 | — | 自测 | N/A | 部分 | — |
| REQ-042 | SRC-REQ-001、DEC-034、DEC-037 | DEC-034、DEC-037、DEC-044、DEC-047、DEC-051、DEC-054、DEC-057、DEC-060、DEC-061、CR-034 | M05 | 新增 | 已确认 | 通知文案不验收 | — | — | — | N/A | N/A | DEV-007 | — | 自测 | N/A | 部分 | — |
| REQ-043 | SRC-REQ-001 | DEC-046 | M05 | 修改 | 已确认 | 归属加拼团/秒杀 | — | — | — | N/A | N/A | 插入（非 DEV-007）；坑位 DEV-013 | — | — | N/A | 部分 | — |
| REQ-044 | SRC-REQ-001 | — | M05 | 新增 | 已确认 | 待配置（市场运营） | — | — | — | N/A | N/A | DEV-007 | — | — | N/A | 部分 | — |
| REQ-045 | SRC-REQ-001 | — | M05 | 保留 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-007 | — | 自测 | N/A | 部分 | — |
| REQ-050 | SRC-REQ-001、DEC-004、DEC-038 | DEC-004、DEC-038、DEC-043、DEC-047、DEC-054、DEC-070 | M06 | 修改 | 已确认 | 新根随模板；店自发重写 | — | — | — | N/A | N/A | DEV-013 | — | 自测 | N/A | 部分 | — |
| REQ-051 | DEC-004、DEC-031 | DEC-004、DEC-031 | M06 | 废弃 | 已确认 | 侧栏删行；改库 DEV-008 | — | — | — | N/A | N/A | DEV-008 | — | 自测 | N/A | 部分 | — |
| REQ-052 | SRC-REQ-001、DEC-004、DEC-068 | DEC-068、CR-044 | M06 | 废弃 | 已废弃 | 已被 REQ-131 废止 | — | — | — | N/A | N/A | DEV-008（旧约束）/ DEV-013 | — | 自测 | N/A | 部分 | — |
| REQ-053 | DEC-014、DEC-004、SRC-CODE-001 | DEC-014 | M06 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-008 | — | 自测 | N/A | 部分 | — |
| REQ-054 | SRC-REQ-001、SRC-UI-001、DEC-070 | DEC-004、DEC-043、DEC-046、DEC-070 | M06 | 修改 | 已确认 | 新列表+复制详情 | — | — | — | N/A | N/A | DEV-013 | — | 自测 | N/A | 部分 | — |
| REQ-060 | SRC-REQ-001、DEC-029、SRC-UI-003、DEC-071 | DEC-029、DEC-050、DEC-051、DEC-052、DEC-053、DEC-054、DEC-057、DEC-058、DEC-060、DEC-061、DEC-071、CR-034、CR-043、CR-049 | M07 | 修改 | 已确认 | 现用页闭口；本轮不调起支付；不加新地址表；分类页 DEC-071 | — | — | — | N/A | N/A | DEV-010 / DEV-013 | — | — | N/A | 未开始 | — |
| REQ-061 | SRC-REQ-001、DEC-006 | DEC-006 | M07 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-010 | — | — | N/A | 未开始 | — |
| REQ-062 | SRC-REQ-001 | — | M07 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-010 | — | — | N/A | 未开始 | — |
| REQ-063 | SRC-REQ-001、CR-043 | DEC-029、CR-043 | M07 | 修改 | 已确认 | 发现不做；AI 假页 | — | — | — | N/A | N/A | DEV-010 / DEV-013 | — | — | N/A | 未开始 | — |
| REQ-064 | DEC-008、SRC-UI-002、SRC-UI-003、SRC-CODE-007、DEC-071 | DEC-008、DEC-050、DEC-071 | M07 | 修改 | 已确认 | 有图页一比一；分类页例外 DEC-071 | — | — | — | N/A | N/A | DEV-010 / DEV-013 | — | — | N/A | 未开始 | — |
| REQ-065 | SRC-REQ-001、DEC-029 | DEC-029、DEC-050 | M07 | 修改 | 已确认 | 必打 iOS/安卓/H5/微信小程序；本轮不调起支付 | — | — | — | N/A | N/A | DEV-010 | — | — | N/A | 未开始 | — |
| REQ-066 | DEC-005、CONFLICT-008、ADR-001、ADR-002、ADR-004 | ADR-001 | M07 | 新增 | 已确认 | 无（进程已确认） | ADR-001、ADR-004 | — | — | N/A | N/A | DEV-010 | — | — | N/A | 未开始 | — |
| REQ-070 | SRC-REQ-001、DEC-003 | DEC-003、DEC-045 | M08 | 修改 | 已确认 | 无（DEC-045 user_pool） | — | design/modules/user.md | 12-user-pool.sql | N/A | N/A | DEV-005 | — | — | N/A | 部分 | — |
| REQ-071 | SRC-REQ-001、DEC-003 | DEC-003、DEC-045 | M08 | 新增 | 已确认 | 登录等 DEV-010 | — | design/modules/user.md | 12-user-pool.sql | N/A | N/A | DEV-005 | — | — | N/A | 部分 | — |
| REQ-072 | DEC-003、DEC-005 | DEC-003、DEC-005、DEC-045 | M08 | 保留 | 已确认 | 无 | — | design/modules/user.md | — | N/A | N/A | DEV-005 | — | — | N/A | 部分 | — |
| REQ-073 | DEC-003 | DEC-003、DEC-045 | M08 | 修改 | 已确认 | 无 | — | design/modules/user.md | 12-user-pool.sql | N/A | N/A | DEV-005 | — | — | N/A | 部分 | — |
| REQ-080 | SRC-REQ-003 A2/A3/A14 | DEC-005、DEC-062、DEC-063、DEC-064、DEC-066、CR-033、CR-037、CR-038、CR-039、CR-041 | M09 | 修改 | 已确认 | 复杂度 DEC-062；存量后台强制改密 DEC-063；超管登录名 DEC-064；浏览器回填 DEC-066；找回密码短信已配须真发 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-081 | SRC-REQ-003 A4/A5 | DEC-005、CR-033 | M09 | 修改 | 已确认 | 不同账号互不踢 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-082 | DEC-005、SRC-REQ-003 A7 | DEC-005、DEC-050 | M09 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-083 | SRC-REQ-003 A6 | DEC-005 | M09 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-084 | SRC-REQ-003 A7/A8 | DEC-005、ADR-002 | M09 | 修改 | 已确认 | 无 | ADR-002 | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-085 | SRC-REQ-003 A10/A11 | DEC-005 | M09 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-086 | SRC-REQ-003 A12 | DEC-005、CR-033、DEC-065、CR-040 | M09 | 修改 | 已确认 | 每次请求读当时角色；超管只属于 ZadminDister | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-087 | SRC-REQ-003 A13 | DEC-005 | M09 | 修改 | 已确认 | 待配置（阈值沿用平台） | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-088 | SRC-REQ-003 A15 | DEC-005 | M09 | 修改 | 已确认 | PRD 后技术评估 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-089 | SRC-REQ-003 A1/A9/A16/A17 | DEC-005 | M09 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-090 | SRC-REQ-003、DEC-005 | DEC-005 | M09 | 保留 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-091 | SRC-REQ-003、DEC-005 | DEC-005 | M09 | 修改 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-004 | — | — | N/A | 部分 | — |
| REQ-100 | SRC-REQ-001、DEC-033 | DEC-033、DEC-051 | M10 | 保留 | 已确认 | 抽佣另对账 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-101 | SRC-REQ-001、DEC-001、ADR-003、DEC-050 | ADR-003、DEC-050、DEC-058 | M10 | 新增 | 已确认 | 本轮 C 端不调起；后续微信/支付宝/金豆 | ADR-003 | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-102 | DEC-001 | DEC-001、DEC-058 | M10 | 修改 | 已确认 | 空或 0 不抽佣 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-103 | DEC-013、DEC-001、DEC-012、DEC-035 | DEC-013、DEC-035、DEC-058 | M10 | 修改 | 已确认 | 未挂一级不可售；空或 0 不冒充已挂一级 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-104 | SRC-REQ-001、DEC-039 | DEC-039 | M10 | 修改 | 已确认 | 沿用现表，本期不加字段 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-105 | DEC-006、DEC-051 | DEC-006、DEC-051、DEC-054 | M10 | 修改 | 已确认 | 人看元；明细改表 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-106 | DEC-033、GAP-003、DEC-051 | DEC-033、DEC-051 | M10 | 新增 | 已确认 | 对公账号/账期等 R8 | — | — | — | N/A | N/A | DEV-009 | — | 自测 | N/A | 部分 | — |
| REQ-107 | DEC-052 | DEC-052、DEC-054、DEC-057、DEC-060、DEC-061、CR-033、CR-034 | M10 | 修改 | 已确认 | 展示列非库字段；平台售后只读；页签无平台介入；真评价提交；当时关库；未付倒计时 | — | — | 23-order-complete-refund.sql | N/A | N/A | DEV-009 | — | 自测 | N/A | 进行中 | — |
| REQ-110 | DEC-007、DEC-039、DEC-050、SRC-REQ-001、SRC-CODE-001 | DEC-007、DEC-039、DEC-050 | M11 | 修改 | 已确认 | 无数据不轮播 | — | — | — | N/A | N/A | DEV-010 / DEV-011 | — | — | N/A | 未开始 | — |
| REQ-111 | DEC-010、DEC-019、SRC-REQ-001、SRC-CODE-002、SRC-CODE-006、CR-035 | DEC-010、DEC-019 | M11 | 修改 | 已确认 | 无（侧栏隐藏已确认；扫码进店现状已补写、不必验） | — | — | — | N/A | N/A | DEV-002 | — | 自测 | N/A | 通过 | — |
| REQ-112 | DEC-006 | DEC-006 | M11 | 废弃 | 已确认 | PRD 后技术评估 | — | — | — | N/A | N/A | DEV-011 | — | — | N/A | 未开始 | — |
| REQ-113 | DEC-053、CR-028 | DEC-053 | M11 | 新增 | 已确认 | 无 | — | — | — | N/A | N/A | DEV-011 | — | — | N/A | 未开始 | — |
| REQ-120 | SRC-REQ-001 | — | M12 | 保留 | 现状 | 待配置 | — | — | — | N/A | N/A | 非必验 | — | — | N/A | 非必改 | — |
| REQ-130 | CR-042、DEC-067 | DEC-067、ADR-010 | M13 | 新增 | 已确认 | 无 | ADR-010 | — | — | N/A | N/A | DEV-012 | — | — | N/A | 未开始 | — |
| REQ-131 | SRC-CHANGE-001、DEC-068 | DEC-068、ADR-011、CR-044 | M07 | 新增 | 已确认 | 本批不真扣款、不真退 | ADR-011 | — | — | N/A | N/A | DEV-013 | — | — | N/A | 未开始 | — |
| REQ-132 | SRC-CHANGE-001、DEC-069 | DEC-069、ADR-016、CR-045 | M11 | 新增 | 已确认 | 三表不进 PRD；不覆盖支付 | ADR-016 | — | — | N/A | N/A | DEV-013 | — | — | N/A | 未开始 | — |
| REQ-133 | SRC-CHANGE-001、DEC-069 | DEC-069、CR-045 | M03 | 新增 | 已确认 | 每批最多 30 | — | — | — | N/A | N/A | DEV-013 | — | — | N/A | 未开始 | — |
| REQ-134 | SRC-UI-003、DEC-073 | DEC-073、CR-051 | M03 | 新增 | 已确认 | 距离导航后置 | — | — | — | N/A | N/A | DEV-014 | — | — | N/A | 进行中 | — |
