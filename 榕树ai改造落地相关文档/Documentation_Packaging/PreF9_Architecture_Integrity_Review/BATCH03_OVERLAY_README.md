# Batch 3 Archive Overlay — 使用说明

本压缩包是 `PreF9_Architecture_Integrity_Review` 的 **Batch 3 增量覆盖包**。

## 使用方法

1. 找到仓库目录：

```text
榕树ai改造落地相关文档/
└── Documentation_Packaging/
    └── PreF9_Architecture_Integrity_Review/
```

2. 将本 ZIP 解压后的**全部内容**复制到：

```text
PreF9_Architecture_Integrity_Review/
```

3. 出现同名文件时选择覆盖：
   - `README.md`
   - `99_NEXT_WINDOW_START_HERE.md`

4. `10_HUMAN_APPROVED_PATCHES/` 只会新增 `AUDIT-PATCH-011`，不会覆盖 001～010。

5. 完成覆盖后，仓库状态应为：

```text
Audit Batch 1 = CLOSED
Audit Batch 2 = CLOSED
Audit Batch 3 = CLOSED
AUDIT-PATCH-011 = HUMAN_APPROVED
```

## 本包不会做的事

- 不修改 F1～F8 v1.0 Freeze Pack；
- 不授权 Implementation；
- 不授权 RP2；
- 不执行 Authority Cutover；
- 不做 Canonical Replacement；
- 不做 Final Activation；
- 不做 Legacy Retirement；
- 不冻结 SQLite 物理表结构。

## 文件清单

- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-011_Product_Design_Typed_Semantic_Linkage_and_Impact_Applicability.md`
- `11_BATCH03_FINAL_CLOSEOUT.md`
- `12_BATCH03_WORKING_HANDOVER_CHECKPOINT.md`
- `README.md`
- `99_NEXT_WINDOW_START_HERE.md`
- `PACKAGE_MANIFEST_v4.0.md`
- `PACKAGE_MANIFEST_v4.0.json`
- `BATCH03_OVERLAY_README.md`
