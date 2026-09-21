# Provider Candidate

九项 AnyDesign 能力映射为 Provider 候选，详见 `PROVIDER_CANDIDATES.yaml`。Full/Element 分析、CSS 变量、页面采集、颜色、对比度、lint、tokens、漂移与交付导出保留原有输入/输出/失败语义。工具源码、依赖和样例继续属于原项目及其工具包，不直接并入 Core。

候选端口遵循：显式输入与作用范围；可报告依赖/网络/解析失败；产物带来源和版本；不得把截图或生成 tokens 当批准的 UI_SPEC。未来 Provider 替换需可复核的行为对照，不能以新供应商 API 能运行作为等价证明。

需要设计的其它端口包括模型调用、编辑器规则、Git 元数据、正式文档读写、项目状态与人工确认。这里仅标出 Contract 所需接口，未选择供应商、模型、价格或执行器。编辑器适配与 Legacy 提示词走 Compatibility Layer，不把 Cursor 目录设为通用协议路径。
