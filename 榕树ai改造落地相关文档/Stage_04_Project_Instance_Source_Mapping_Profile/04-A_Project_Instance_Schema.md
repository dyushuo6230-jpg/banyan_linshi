# 04-A：Project Instance Schema

Project Instance 必填域：

```yaml
instance:
  project:
  source_mappings:
  overlays:
  profiles:
  variable_bindings:
  provider_bindings:
  feature_activation:
  locations:
  lineage:
```

`locations` 仅描述 Banyan 自己的实例数据位置，
不能反向要求项目业务目录搬迁。

Project Instance 不是业务真源。
