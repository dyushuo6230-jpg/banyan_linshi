# 09-A Design Source Intake / Provider Port

Design Source 类型可包括：

```text
IMAGE
SVG
FIGMA
PROTOTYPE
ANYDESIGN
EXISTING_UI
DESIGN_TOKEN_FILE
OTHER_PROVIDER
```

Provider Port 必须定义：

```text
intake
parse
extract_scene
extract_assets
extract_tokens
extract_states
report_confidence
report_failure
```

Provider 专属信息只能留在 extension / raw provider payload。
