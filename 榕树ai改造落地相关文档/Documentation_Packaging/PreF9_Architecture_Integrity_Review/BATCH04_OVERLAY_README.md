# Batch 4 Archive Overlay — 使用说明

本压缩包是 `PreF9_Architecture_Integrity_Review` 的 **Batch 4 增量覆盖包**。

## 使用方法

找到仓库目录：

```text
榕树ai改造落地相关文档/
└── Documentation_Packaging/
    └── PreF9_Architecture_Integrity_Review/
```

将本 ZIP 解压后的**全部内容**复制到：

```text
PreF9_Architecture_Integrity_Review/
```

出现同名文件时选择覆盖。

本包会覆盖 / 更新：

- `README.md`
- `99_NEXT_WINDOW_START_HERE.md`

并新增：

- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-012_...md`
- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-013_...md`
- `13_BATCH04_FINAL_CLOSEOUT.md`
- `14_BATCH04_WORKING_HANDOVER_CHECKPOINT.md`
- `PACKAGE_MANIFEST_v5.0.md`
- `PACKAGE_MANIFEST_v5.0.json`
- `BATCH04_OVERLAY_README.md`

原有 Batch 1～3 文件、AUDIT-PATCH-001～011、v3/v4 历史 Manifest 均保留，不删除。

## 覆盖后状态

```text
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
Audit Batch 4 = CLOSED

AUDIT-PATCH-012 = HUMAN_APPROVED
AUDIT-PATCH-013 = HUMAN_APPROVED

B4-CHAIN-01 = ARCHITECTURALLY_RESOLVED
B4-CHAIN-02 = ARCHITECTURALLY_RESOLVED
B4-PATCH-03 = NOT REQUIRED

Final Completeness Sweep = PASS
```

## 本包不会做的事

```text
Implementation = NOT_AUTHORIZED
RP2 = NOT_AUTHORIZED
Authority Cutover = NOT_AUTHORIZED
Canonical Replacement = NOT_AUTHORIZED
Final Activation = NOT_AUTHORIZED
Legacy Retirement = NOT_AUTHORIZED
SQLite Physical Schema = NOT_FROZEN
```
