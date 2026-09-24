# 04-D：Project Profile / Contributor Profile

## Project Profile

项目展示与运行辅助信息：

```text
project_id
display_name
description
lifecycle_status
governance_mode
technology_hints
```

## Contributor Profile

以 Git identity 为 key：

```text
author.name + author.email
```

可选字段：

```text
display_name
status
note
```

明确禁止：

```text
role_labels 作为长期岗位
module_owner 作为强绑定
profile status 作为授权
自动 alias / merge Git identities
推断物理操作者
```

Git 历史仍是真实提交来源。
