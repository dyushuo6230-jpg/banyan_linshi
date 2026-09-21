"""Stage 02 design artifacts from sealed Stage 01 inputs only.
No repository discovery, legacy reads, business writes, runtime execution or migration.
"""
from pathlib import Path
import collections, hashlib, json, os
import yaml

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[3]
S1=ROOT/'.banyan-refactor/stages/01/stage01-20260920T091426Z'
os.chdir(ROOT)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def jl(p):return [json.loads(l) for l in p.open()]
def ys(p):return yaml.safe_load(p.read_text())
def dump(path,value):
    p=RUN/path
    with p.open('x',encoding='utf-8') as f:yaml.safe_dump(value,f,allow_unicode=True,sort_keys=False)
def lines(path,rows):
    with (RUN/path).open('x',encoding='utf-8') as f:
        for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
def md(path,value):
    with (RUN/path).open('x',encoding='utf-8') as f:f.write(value)

pre=json.loads((RUN/'evidence/PRECHECK.json').read_text())
assert pre['stage01_handoff_result']=='PASS' and pre['tracked_diff_empty']
assert all(x['stage01_sealed'] and sha(S1/x['path'])==x['sha256'] for x in pre['stage01_inputs'])
CAP=jl(S1/'LEGACY_AI_CAPABILITY_INVENTORY.jsonl')
ASSETS=jl(S1/'AI_ASSET_INVENTORY.jsonl')
GEN=jl(S1/'AI_GENERATED_ARTIFACT_INVENTORY.jsonl')
OPS=jl(S1/'OPERATIONAL_ARTIFACT_INVENTORY.jsonl')
CORE=ys(S1/'CORE_CANDIDATE_REPORT.yaml')
ISSUES=ys(S1/'CONFLICT_GAP_REPORT.yaml')['issues']
ARTM=ys(S1/'PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml')
CAPM=ys(S1/'PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml')
assert len(CAP)==35 and len(ASSETS)==1026 and len(GEN)==425 and len(OPS)==289
assert {c['capability_id'] for c in CAP}=={c['capability_or_asset_id'] for c in CORE['candidates']}=={x['capability_id'] for x in CAPM['matrix']}
assert {g['artifact_id'] for g in GEN}=={x['artifact_id'] for x in ARTM['matrix']}
assert {o['artifact_id'] for o in OPS}=={x['artifact_id'] for x in ARTM['operational_mapping']}

# Every row is an explicit architectural hypothesis, not a frozen schema or owner.
# Tuple: contract, provider port, project overlay, artifact role, runtime phase, key risk.
SPEC={
 'AUTH':('ActionAuthorization','HumanApprovalEvidence','project roles and protected paths','DecisionEvidence','PRE_AUTHORIZE','Do not infer permission from a legacy prompt or an earlier choice.'),
 'PROFILE':('VariableResolution','ProjectFactReader','project variables and migration defaults','ProjectVariableMap','LOAD_CONTEXT','TBD values cannot be silently defaulted.'),
 'INTAKE':('SourceIntake','ProjectSourceReader','source batches and document roots','SourceRecord','ENGINEERING','Historic source status needs a project mapping.'),
 'PRD':('RequirementLifecycle','CanonicalDocumentReader','PRD stages and local labels','RequirementDocument','HUMAN_DECISION','Approval status cannot be inferred from a file path.'),
 'IDP':('DecisionSession','HumanDecisionChannel','DEC-042 five-question project overlay','DecisionEvidence','HUMAN_DECISION','Generic HIGH=1/LOW=2 and project overlay conflict; no winner selected.'),
 'ARCH':('DesignGate','DecisionRegistryReader','current G6/G7 labels and project baseline','ArchitectureDecision','HUMAN_DECISION','DIRECT_DRAFT must not bypass approval.'),
 'SCHEMA':('ArtifactStatusAndIdentity','ArtifactRegistryReader','project numbering namespace','ArtifactMetadata','ENGINEERING','ID ownership and Approved/Baselined status need proof.'),
 'IDREF':('ReferenceIntegrity','DocumentReferenceReader','DEC/ADR/CR/REQ local namespaces','ReferenceGraph','FULL_AUDIT','Never change meaning of an occupied ID or replace referenced body.'),
 'TRACE':('EvidenceTrace','SourceGraphReader','project trace vocabulary and document roots','TraceEdge','FULL_AUDIT','Missing edges must remain explicit, not fabricated.'),
 'CHANGE':('ChangeApplication','CanonicalDocumentWriter','project CR/PRD version policy','ChangeRecord','HUMAN_DECISION','Only confirmed scope can cross the canonical write boundary.'),
 'PARALLEL':('DraftPromotion','DraftWorkspaceReader','changes_temp path and PRD state','PromotionPlan','HUMAN_DECISION','Draft cannot become canonical or reserve final IDs automatically.'),
 'RECONCILE':('BatchReconciliation','BatchEvidenceReader','36A trigger and business-delta semantics','ReconciliationRecord','ENGINEERING','Incomplete reconciliation cannot silently start the next batch.'),
 'TEST':('TestIntegrity','TestEvidenceReader','project test/acceptance rules','TestIntegrityEvidence','FULL_AUDIT','Temporary stubs cannot remain or redefine success.'),
 'PROGRESS':('ProgressProjection','ProgressRegistryReader','weights and applicability of project work','ProgressProjection','ENGINEERING','Stale summaries must not override the register or imply completion.'),
 'HANDOVER':('OperationalHandover','WorklogReader','local log/handover format','HandoverRecord','ENGINEERING','Missing work/risks must not be dropped from recovery context.'),
 'CONTEXT':('ContextRecovery','ProjectStateReader','current project authority/freshness rules','RecoveryContext','LOAD_CONTEXT','README/dashboard conflicts require source/freshness resolution.'),
 'UI_SCOPE':('UIApplicationScope','ApplicationMapReader','application slugs and enabled list','UIScopeMap','ENGINEERING','Disabled applications must not count as active UI constraints.'),
 'UI_CONTRACT':('EffectiveUIContract','UISpecReader','application/page/device version map','EffectiveUIContract','ENGINEERING','Only Approved/Baselined applicable UI rules may constrain a batch.'),
 'UI_GATE':('UIApprovalGate','DesignEvidenceReader','project 25A/28A/29 steps and named pages','UIGateDecision','HUMAN_DECISION','Design tokens and Draft do not authorize implementation.'),
 'VISUAL':('VisualRepairRun','ScreenshotCapture','page/allowed-files/viewport/exception overlay','VisualRunEvidence','ENGINEERING','In-progress and user-stopped/reverted runs are not successes.'),
 'PUBLISH':('KnowledgeProjection','CanonicalFactReader','plain-spec and PLAIN_SYNC mapping','ProjectGuideProjection','BATCH_WORKER','Derived guide cannot become PRD truth or be rebuilt without lineage.'),
 'EDITOR':('EditorEntryCompatibility','EditorRuleAdapter','Cursor rule precedence and symlink entry','AdapterProjection','LOAD_CONTEXT','Cursor path/format cannot become a Core invariant.'),
 'PORT':('ProjectEndpointMap','ProjectConfigReader','8035/8037 and application-service binding','ProjectEndpointConfig','LOAD_CONTEXT','Ports and business application names remain project data.'),
 'SQL':('ProjectDeliveryConvention','ProjectSQLReader','numbered incremental SQL practice','ProjectDeliveryRecord','ENGINEERING','No SQL execution or new universal SQL policy implied.'),
 'COMMIT':('CommitPracticeCompatibility','GitCommitMetadataReader','nested Husky/commitlint installation and policy','CommitEvidence','HUMAN_DECISION','Missing lint:lint-staged and exact author identities; never commit automatically.'),
 'MERGE':('LegacyCollaborationReference','LegacyGuideReader','old branch names and ownership rules','LegacyMergeReference','FULL_AUDIT','Historic reset/force instructions are not current authorization.'),
 'DESIGN':('DesignAnalysis','AnyDesignAdapter','source and approval status of project UI materials','DesignAnalysisMaterial','ENGINEERING','Visual extraction is evidence, not Approved UI_SPEC.'),
 'CSS':('CssTokenExtraction','AnyDesignCssAdapter','project URL/input scope','CssTokenDigest','BATCH_WORKER','Network/style access can fail; no invented tokens.'),
 'CAPTURE':('PageVisualCapture','AnyDesignCaptureAdapter','project URL, viewport, allowed capture','CaptureEvidence','BATCH_WORKER','Playwright/network failure does not produce a valid screenshot.'),
 'COLORS':('ImagePaletteExtraction','AnyDesignColorAdapter','project source image identity','PaletteEvidence','BATCH_WORKER','Palette is an observation, not an accessibility/brand decision.'),
 'A11Y':('ContrastEvaluation','AnyDesignContrastAdapter','project color pairs','AccessibilityEvidence','BATCH_WORKER','A pass for selected color pairs is not UI acceptance.'),
 'LINT':('DesignDocumentLint','AnyDesignLintAdapter','project design.md inputs','DesignLintResult','BATCH_WORKER','Structural lint cannot approve design semantics.'),
 'TOKENS':('DesignTokenBuild','AnyDesignTokenAdapter','project frontmatter and source revision','DesignTokenProjection','BATCH_WORKER','Derived tokens need source revision and must not be hand-edited as truth.'),
 'DRIFT':('DesignDriftCheck','AnyDesignDriftAdapter','project URL and effective tokens','DesignDriftEvidence','BATCH_WORKER','Live URL failure or stale source is not a clean comparison.'),
 'EXPORT':('DesignPackageExport','AnyDesignExportAdapter','project export target and source revision','DesignExportBundle','BATCH_WORKER','Exported DOCX/PPTX/CSS is derived; exact replay not proven.'),
}
assert len(SPEC)==35
LAYER={'GENERIC_CORE_CANDIDATE':'BANYAN_CORE_CANDIDATE','PROJECT_ONLY_CANDIDATE':'PROJECT_INSTANCE_CANDIDATE','PROVIDER_CANDIDATE':'PROVIDER_CANDIDATE','COMPATIBILITY_CANDIDATE':'COMPATIBILITY_LAYER_CANDIDATE'}
core_byid={x['capability_or_asset_id']:x for x in CORE['candidates']}
asset_by_path={x['path']:x for x in ASSETS}
work=[]
for cap in CAP:
    key=cap['capability_id'][4:]
    contract,port,overlay,role,phase,risk=SPEC[key]
    cc=core_byid[cap['capability_id']]
    sources=[asset_by_path[p]['asset_id'] for p in cap['legacy_sources'] if p in asset_by_path]
    row=dict(capability_id=cap['capability_id'],name=cap['name'],legacy_source=cap['legacy_sources'],legacy_asset_ids=sources,current_behavior=cap['behaviors'],inputs=cap['inputs'],outputs=cap['outputs'],guards=cap['guards'],failure_semantics=cap['failure_semantics'],candidate_layer=LAYER[cap['candidate_boundary']],secondary_boundary=['PROJECT_INSTANCE_POLICY_OR_DATA'] if cap['candidate_boundary']=='GENERIC_CORE_CANDIDATE' else ['GENERIC_PORT'] if cap['candidate_boundary']=='PROVIDER_CANDIDATE' else [],contract_need=dict(name=contract,inputs=cap['inputs'],outputs=cap['outputs'],guards=cap['guards'],failure_semantics=cap['failure_semantics'],status='DESIGN_CANDIDATE_NOT_FROZEN'),provider_port_candidate=port,artifact_role_candidate=role,runtime_phase_candidate=phase,project_overlay_candidate=overlay,migration_risk=risk,purity_risk='NO_INDEPENDENT_CROSS_PROJECT_EXECUTION_PROOF',decision_owner_stage=str(cap['candidate_owner_stage']),stage02_design_owner='02',stage01_boundary=cap['candidate_boundary'],stage01_core_candidate_ref='../../01/stage01-20260920T091426Z/CORE_CANDIDATE_REPORT.yaml#'+cap['capability_id'],stage01_capability_ref='../../01/stage01-20260920T091426Z/LEGACY_AI_CAPABILITY_INVENTORY.jsonl#'+cap['capability_id'],evidence_refs=cap['evidence_refs'],candidate_action=cap['candidate_action'],open_question=cap['open_question'])
    if cc['project_specific_dependencies']:row['project_dependency_warning']='Stage 01 source file contains project facts; Stage 02 maps these to overlay, not automatically to this capability semantics.'
    work.append(row)
dump('CAPABILITY_MAPPING_WORKBOOK.yaml',dict(schema_version='stage02-design-candidate-v1',stage='02',run_id=RUN.name,source_stage01_run=S1.name,status='CANDIDATE_ONLY',not_frozen=['final contract schema','physical layout','runtime implementation','provider selection','source role','migration'],count=len(work),capabilities=work))

def records(layer):
    out=[]
    for r in work:
        if r['candidate_layer']!=layer:continue
        out.append(dict(capability_id=r['capability_id'],name=r['name'],candidate_layer=layer,contract=r['contract_need']['name'],provider_port=r['provider_port_candidate'],artifact_role=r['artifact_role_candidate'],runtime_phase=r['runtime_phase_candidate'],project_overlay=r['project_overlay_candidate'],failure_semantics=r['failure_semantics'],migration_risk=r['migration_risk'],required_validation=['Cross-project fixture with another repository; no hardcoded x_shop_server path','Stage 03 contract/schema review','Stage 19 no-loss regression'] if layer=='BANYAN_CORE_CANDIDATE' else ['Provider/compatibility/project scope review','Stage 19 no-loss regression'],decision_owner_stage=r['decision_owner_stage'],evidence_refs=r['evidence_refs'],approval='NOT_APPROVED',execution_allowed=False))
    return out
for layer,name in [('BANYAN_CORE_CANDIDATE','CORE_CANDIDATES.yaml'),('PROJECT_INSTANCE_CANDIDATE','PROJECT_CANDIDATES.yaml'),('PROVIDER_CANDIDATE','PROVIDER_CANDIDATES.yaml'),('COMPATIBILITY_LAYER_CANDIDATE','COMPATIBILITY_CANDIDATES.yaml')]:
    rows=records(layer)
    dump(name,dict(stage='02',status='CANDIDATE_ONLY',layer=layer,count=len(rows),items=rows))

asset_map=[]
for a in ASSETS:
    p=a['path']
    if a['origin']['historical_only'] or p.startswith(('docs/temp/','docs/governance/')):
        layer='COMPATIBILITY_LAYER_CANDIDATE';reason='Legacy/history remains readable and in place; semantics may feed future contracts.'
    elif p.startswith(('tools/anydesign/','.cursor/skills/anydesign')):
        layer='PROVIDER_CANDIDATE';reason='Existing design tool/entry remains provider-owned; no copy into Core.'
    elif p.startswith('.cursor/'):
        layer='COMPATIBILITY_LAYER_CANDIDATE';reason='Current editor entry remains active until adapter parity; project policy stays overlay.'
    else:
        layer='PROJECT_INSTANCE_CANDIDATE';reason='Current Reference Project content remains at its path; Core may reference its mapped semantics only.'
    asset_map.append(dict(asset_id=a['asset_id'],path=p,stage01_asset_type=a['asset_type'],stage01_disposition=a['classification']['action'],stage02_candidate_layer=layer,current_role=a['authority']['canonicality'],reason=reason,action='PRESERVE_IN_PLACE_AND_MAP',stage01_evidence_refs=a['evidence_refs']))
lines('ASSET_BOUNDARY_MAP.jsonl',asset_map)

artifact_map=[]
for g in GEN:
    layer='PROVIDER_CANDIDATE' if g['path'].startswith('tools/anydesign/') else 'PROJECT_INSTANCE_CANDIDATE'
    artifact_map.append(dict(artifact_id=g['artifact_id'],path=g['path'],stage01_class=g['artifact_class'],stage02_candidate_layer=layer,source_role_candidate=g['candidate_source_role'],source=g['source'],rebuildability=g['rebuildability'],integrity_risk=g['integrity_risk'],preservation='KEEP_IN_PLACE + MAP + INDEX',stage03_contract_need='Authorship/provenance/status/rebuildability recorded separately; exact Source Role pending',no_regeneration_without_verified_lineage=True,evidence_refs=g['evidence_refs']))
for o in OPS:
    artifact_map.append(dict(artifact_id=o['artifact_id'],path=o['path'],stage01_class='OPERATIONAL',stage02_candidate_layer='PROJECT_INSTANCE_CANDIDATE',source_role_candidate='OPERATIONAL_HISTORY',freshness=o['freshness'],preservation='KEEP_IN_PLACE + INDEX',stage03_contract_need='Append-only chronology/failure and supersession semantics; not formal source of truth',no_regeneration_without_verified_lineage=True,evidence_refs=o['evidence_refs']))
lines('ARTIFACT_BOUNDARY_MAP.jsonl',artifact_map)

md('CONTRACT_CHAIN_DESIGN.md',f'''# Stage 02 — Capability → Contract → Provider → Artifact → Runtime

状态：**设计候选；不创建运行实现、不冻结正式 Schema**。证据来自 Stage 01 的 {len(CAP)} 项能力、{len(ASSETS)} 项资产、{len(GEN)} 项正式/派生产物候选和 {len(OPS)} 项运行记录。逐项映射见 `CAPABILITY_MAPPING_WORKBOOK.yaml`，物理资产和产物分别见两个 Boundary Map。

## 1. Capability

稳定单元是用户可观察的工程行为及其守卫和失败语义，不是某个 prompt 文件或目录。每项能力保留 Stage 01 的 ID、旧来源、输入/输出、门禁、失败方式；即使最终不是 Core，能力也不因实现混乱被删除。Stage 01 的 21/2/9/3 是候选分类，不是移植性证明。

## 2. Contract

候选接口输入：`capability_id`、项目上下文引用、事实来源与版本、请求动作、访问/授权证据、预算约束。输出：有来源和状态的结果、守卫决策、失败类型、追踪引用。只读与可能写入的能力必须显式区分。草拟失败类别：`SOURCE_UNVERIFIED`、`STALE_AUTHORITY`、`DECISION_REQUIRED`、`PERMISSION_DENIED`、`BUDGET_EXCEEDED`、`PROVIDER_UNAVAILABLE`、`PARTIAL_RESULT`、`VALIDATION_FAILED`。具体字段、编码、幂等键与版本由 Stage 03/05 定义，本阶段不冻结。

高影响变更必须携带用户决策证据；首次选择或模型推荐都不等于应用授权。项目级数字、路径、端口、业态和 G 阶段编号通过 Project Instance 映射注入，不能成为通用接口常量。

## 3. Provider

Provider 只能通过受限端口取得项目事实、读写正式文档、运行设计工具、与编辑器交互或访问模型。其具体工具路径和产品名不得渗入 Core。当前 AnyDesign 九项能力是设计 Provider 候选；Cursor 规则和旧 v3.1 用兼容层读入。模型、Git 和人工确认也需要端口，但没有任何 Stage 02 实现或默认写权限。

## 4. Artifact

正式 Canonical 候选、Derived、Operational 与旧来源分别标注权威性和生命周期。正式文档继续原位；派生产物记录输入/消费者/版本/重建证据；运行记录保留 in_progress、叫停、回退等状态。未知 AI 作者身份和未经证明的精确重建能力保持 UNKNOWN。Stage 03 冻结 Source Role、Schema、引用完整性时应消费 `ARTIFACT_BOUNDARY_MAP.jsonl`，不得依本阶段候选删除文件或把旧 ID 挂新主题。

## 5. Runtime

候选 Runtime 负责按任务风险路由、预算与模式选择、阶段门禁、暂停与恢复、观察成本与结果。状态推进以正式源和有效授权为依据；Provider 执行结果必须经过 Contract 校验才可发布或写正式真源。Full Audit、Engineering、Batch Worker、Human Decision 四种执行模式的成本策略见 `AI_RUNTIME_COST_GOVERNANCE_DESIGN.md`。没有启动 Runtime，也没有模型调用。

## 边界不变量

1. Existing Project → `PRESERVE_IN_PLACE`；Banyan → `DISCOVER + MAP + DESIGN`；重新布局只能 `EXPLICIT_MIGRATION_ONLY`。Stage 01 Handoff 的 `DISCOVER + MAP + CLASSIFY` 是已完成发现阶段，本阶段的 DESIGN 只增加候选分析，不改变原约束。
2. 项目事实由 Project Instance 持有。Core 使用来源引用和适用性，不复制项目真源；兼容层也不成为第二个可写真源。
3. 13 份本地环境配置与其余 Secret 继续 metadata-only；本阶段未读、未复制、未 Hash、未修改、未删除、未提交。
4. 35 项能力全部保留候选归宿；0 项因不通用而退役。迁移与激活需各 Owner Stage 验证。
5. 本设计不等于跨项目可用性、性能、成本或安全已经测试通过。
''')

md('CORE_BOUNDARY_CANDIDATE.md',f'''# Banyan Core Candidate

{len(records('BANYAN_CORE_CANDIDATE'))} 项能力的**语义**可抽象为 Core 候选；没有一份既有项目文件被宣布为 Core 的物理资产。每项的输入、输出、守卫、失败方式、接口名和验证条件见 `CORE_CANDIDATES.yaml`。

Core 可以持有授权/决策/状态/引用/追踪/变更/证据/上下文/UI 合并/知识投影等通用规则。Core 不持有当前 `docs/project`、`.cursor`、G 编号、DEC-042、端口、五端和四业态的具体取值。大提示词中出现这些词只说明**来源文件混合了项目事实与通用语义**，并不证明每个能力本身依赖它们；`CAPABILITY_MAPPING_WORKBOOK.yaml` 为每项列出项目 Overlay。

进入最终 Core 的验证门槛：另一项目的独立 fixture 可调用同一 Contract；无硬编码本仓路径/业务词；错误和授权语义一致；Provider 可替换；Stage 19 No-Loss 回归不丢现有能力。Stage 02 没有这些跨项目执行证据，因此 21 项仍是 Candidate，Stage 03/04/05/领域 Owner Stage 再细化，未批准部署。
''')
md('PROJECT_INSTANCE_CANDIDATE.md','''# Project Instance Candidate

主边界 2 项：`CAP-PORT`（项目端口及前后端绑定）、`CAP-SQL`（当前增量 SQL 交付习惯），逐项见 `PROJECT_CANDIDATES.yaml`。Core 候选的项目 Overlay 还包括文档真源路径、批准状态/编号命名、G 阶段名、DEC-042 覆盖、四业态与五端、UI 应用/页面/服务绑定、业务进度权重和本地工作约定；逐能力对应见 Workbook。Overlay 不是新增能力数，也不让项目文件进入 Core。

现有 `docs/project/**`、`docs/temp/**`、`.cursor/**`、`tools/**` 和业务目录保持原位。`ASSET_BOUNDARY_MAP.jsonl` 为全部 1,026 项资产给出原位角色；`ARTIFACT_BOUNDARY_MAP.jsonl` 给出产物与历史记录的候选 Source Role。Legacy 参考档只读，正式 PRD/DEC/ADR/CR/UI_SPEC 的批准与旧版本关系保持原语义。Stage 04 再设计项目实例映射，不以统一 `project-sources/` 作为前提。

目录保护：EXISTING_PROJECT → PRESERVE_IN_PLACE；BANYAN → DISCOVER + MAP + DESIGN；RELAYOUT → EXPLICIT_MIGRATION_ONLY。这里的 DESIGN 是候选边界描述；不移动或重写文件。
''')
md('PROVIDER_CANDIDATE.md','''# Provider Candidate

九项 AnyDesign 能力映射为 Provider 候选，详见 `PROVIDER_CANDIDATES.yaml`。Full/Element 分析、CSS 变量、页面采集、颜色、对比度、lint、tokens、漂移与交付导出保留原有输入/输出/失败语义。工具源码、依赖和样例继续属于原项目及其工具包，不直接并入 Core。

候选端口遵循：显式输入与作用范围；可报告依赖/网络/解析失败；产物带来源和版本；不得把截图或生成 tokens 当批准的 UI_SPEC。未来 Provider 替换需可复核的行为对照，不能以新供应商 API 能运行作为等价证明。

需要设计的其它端口包括模型调用、编辑器规则、Git 元数据、正式文档读写、项目状态与人工确认。这里仅标出 Contract 所需接口，未选择供应商、模型、价格或执行器。编辑器适配与 Legacy 提示词走 Compatibility Layer，不把 Cursor 目录设为通用协议路径。
''')
md('COMPATIBILITY_LAYER_CANDIDATE.md','''# Compatibility Layer Candidate

三项主边界：`CAP-EDITOR`、`CAP-COMMIT`、`CAP-MERGE`，见 `COMPATIBILITY_CANDIDATES.yaml`。旧 v3.1 超级提示词的来源投放、PRD、决策、版本和工作流仍是多项能力的现行实现来源；先做只读解释与行为回归，不能在 Stage 02 直接拆改旧文或关闭入口。

Cursor 规则与 symlink skill 是既有入口，兼容映射要保留覆盖顺序及项目规则。Nested Husky/commitlint 的存在不证明根提交钩子生效，已发现缺少 `lint:lint-staged` 脚本；不得自动安装、执行或调整 Git Identity。旧合码指导包含特定分支、reset/force 语境，仅作历史参考，不能转成 Runtime 权限。

兼容层的读入结果必须注明来源、版本、适用项目和是否过期。它不能成为另一个项目真源，也不能悄悄把旧提示词视为未来通用 Contract。Stage 07/17 做兼容实施与回归；Stage 19 做 No-Loss 终验。Stage 02 仅记录约束和候选接口。
''')
md('AI_RUNTIME_COST_GOVERNANCE_DESIGN.md','''# AI Runtime Cost Governance — Stage 02 design candidate

本设计没有选择模型、执行请求或生成费用数据。预算数值、模型清单、价格和路由实现留给 Runtime Owner Stage，需依据其当时可验证的配置与质量数据确定。

## Task Routing

先判任务的影响、是否写正式真源、必须读取的来源、失败时能否安全重试，再选执行模式。高影响决策和生产/数据动作始终经人工授权门禁；允许的低风险只读索引可批处理。路由依据是任务需求和证据等级，不是某个编辑器或模型品牌。

## Model Selection

定义候选输入维度：所需推理深度、上下文长度、工具权限、数据敏感级别、确定性/结构化输出要求、时延和预计成本。选择器只在合规 Provider 集内选择；输出模型选择理由、预计/实际用量和质量校验。质量不足时升级模型或转人工，不静默降低必需验证。含 Secret 的路径仍只传元数据；模型预算不能放宽内容读取权限。

## Token Budget

按任务设置软预算和硬上限，并预留证据/验证/重试份额。长文档先用已验证索引和引用定位；摘要必须带来源哈希/版本、覆盖与缺口，不能替代权威原文。预算耗尽时暂停并交接已完成证据与未完成项，不虚报 PASS。成本事件至少可追踪 capability、任务/阶段、provider、估算/实际 token、重试、缓存命中、产物、失败原因；敏感正文不得写日志。

## Execution Mode

- **Full Audit**：安全、权限、Source of Truth、引用完整性、No-Loss 或阶段验收；必须保留足够审计证据，成本不足则暂停，不能省略必需检查。
- **Engineering**：当前经授权的单项开发/文档工作；只取适用上下文，限制改动范围并验证受影响对象。
- **Batch Worker**：可独立、可重试、无歧义的派生/索引任务；记录每项输入与结果，部分失败不合并为整体成功。
- **Human Decision**：有多个实质方案、高影响或权威冲突；预算与模型不能代替知情决策、影响复述和有效确认。

## Batch/Cache/Fallback

批次按相同 Contract 版本、权限、来源快照和输出验证要求分组；不同真源状态不得混批。缓存键候选包含来源版本、Contract 版本、Provider 能力版本和项目上下文指纹；Secret 内容不入缓存。Provider 失败可按幂等规则重试或交给人工，不能在需要批准时自动改走写入路径。派生产物缓存失效应标 stale，正式文档不靠缓存重写。

## 后续验证

Stage 03 定义用量/证据字段；Stage 05 定义路由、门禁、暂停/恢复；Stage 14 校验权限；Stage 15 实现 Provider/Runtime API；Stage 16 显示成本与进度；Stage 19 用真实工作负载验证质量与成本。所有阈值在对应 Owner Stage 冻结，本阶段不设虚构数字。
''')

carry=[]
for i in ISSUES:
    carry.append(dict(issue_id=i['issue_id'],inherited_severity=i['severity'],type=i['type'],source_stage01='../../01/stage01-20260920T091426Z/CONFLICT_GAP_REPORT.yaml#'+i['issue_id'],description=i['description'],evidence_refs=i['evidence_refs'],stage02_treatment='Candidate boundary mapping only; no source edit or automatic conflict winner',candidate_layer='PROJECT_INSTANCE_POLICY_OVERLAY + CORE_PRECEDENCE_CONTRACT' if i['issue_id']=='CON-001' else 'PROJECT_SOURCE_FRESHNESS + REFERENCE_INTEGRITY' if i['issue_id']=='CON-002' else 'COMPATIBILITY_OR_PROJECT_SOURCE_REVIEW',candidate_owner_stage=str(i['candidate_owner_stage']),next_action=i['recommended_next_action'],status='OPEN_ROUTED',blocks_stage02_design=False,blocks_activation_without_resolution=i['severity'] in ('HIGH','CRITICAL')))
newrisk=[
 dict(risk_id='R02-PURITY-001',severity='HIGH',description='21 Core semantic candidates have no independent cross-project execution proof; source-file keyword hits are overbroad and cannot establish semantic dependence.',candidate_owner_stage='03/04/19',next_action='Stage 03 contract review plus second-project fixture and Stage 19 portability/no-loss validation before final Core acceptance.',blocks_stage02_design=False,blocks_activation_without_resolution=True),
 dict(risk_id='R02-SOURCE-002',severity='HIGH',description='Canonicality, AI authorship, exact generated lineage and rebuildability remain candidate/unknown for many artifacts.',candidate_owner_stage='03/09/10',next_action='Freeze source-role schema, map provenance and test regeneration before any replace/archive decision.',blocks_stage02_design=False,blocks_activation_without_resolution=True),
 dict(risk_id='R02-COST-003',severity='MEDIUM',description='AI Runtime cost governance is conceptual; no model/price/token threshold or quality benchmark verified.',candidate_owner_stage='05/15/16/19',next_action='Define cost/quality telemetry and benchmark real workloads, then set thresholds with controlled configuration.',blocks_stage02_design=False,blocks_activation_without_resolution=False),
 dict(risk_id='R02-SECRET-004',severity='HIGH',description='13 user-approved local environment configurations have no independent Banyan backup; all 13 and other Secret candidates remain metadata-only.',candidate_owner_stage='ALL_LATER_STAGES',next_action='Preserve in place, no body read/hash/copy/write/delete/commit; recovery coverage remains PARTIAL_APPROVED.',blocks_stage02_design=False,blocks_activation_without_resolution=True),
 dict(risk_id='R02-LOCAL-005',severity='MEDIUM',description='Control artifacts are local uncommitted evidence, not independent off-machine backup. Stage 01 also recorded an externally disappeared duplicate zip.',candidate_owner_stage='ALL_LATER_STAGES',next_action='Preserve sealed evidence and classify freshness before each new stage; do not recreate or attribute zip deletion without proof.',blocks_stage02_design=False,blocks_activation_without_resolution=False),
]
dump('CONFLICT_RISK_REGISTER.yaml',dict(stage='02',status='OPEN_ROUTED',inherited_issue_count=len(carry),new_risk_count=len(newrisk),inherited_issues=carry,new_risks=newrisk,conflict_winners_selected=[],legacy_files_edited=False))

adrs=[
 ('S02-ADR-001','Five-layer capability chain','Keep semantic capability separate from Contract, Provider, Artifact and Runtime','Extract all legacy files into one monolithic Core; treat current tool paths as API; separate layered candidates','Separating layers preserves 35 behaviors while allowing provider and project changes','Stage 03 must formalize contracts; no runtime built'),
 ('S02-ADR-002','Preserve project layout','Keep existing project paths and map source roles','Relayout now; require one universal project-sources tree; preserve in place with explicit mapping','No migration risk during design; compatible with existing canonical references','Stage 04 must test source mapping and explicit future migration only'),
 ('S02-ADR-003','Provider ports','Keep specific tools/model/editor behind capability ports','Directly call existing scripts from Core; use provider interfaces with typed failure','Separates tool failure from governance decisions','Stage 09/15 must verify adapter equivalence'),
 ('S02-ADR-004','Legacy compatibility','Read old rules through versioned compatibility projection','Delete old prompts; silently make them canonical Core; versioned read-only compatibility','Preserves user-facing behavior and avoids dual writable truth','Stage 07/17 require regression before switching entrypoints'),
 ('S02-ADR-005','Runtime cost','Route tasks by risk and evidence with budgets and four modes','One premium model for everything; cheapest model for everything; risk-aware routing with quality gates','Cost visibility without weakening required evidence','Thresholds, models and prices require later validated configuration'),
 ('S02-ADR-006','Artifact authority','Maintain project canonical source, derived and operational roles','Treat generated outputs as disposable; treat every file as canonical; preserve classified roles','Prevents data loss and false authority','Stage 03 formal schema and source graph required'),
]
dump('ARCHITECTURE_DECISION_RECORDS.yaml',dict(stage='02',status='DRAFT_NOT_APPROVED',decisions=[dict(decision_id=id,title=title,decision='CANDIDATE: '+decision,context='Stage 01 sealed inventories and Gate Review',options=options.split('; '),impact=impact,risk=risk,status='DRAFT',approval='NOT_REQUESTED_OR_GRANTED',execution_allowed=False) for id,title,decision,options,impact,risk in adrs]))
print(json.dumps(dict(run_id=RUN.name,capabilities=len(work),core=len(records('BANYAN_CORE_CANDIDATE')),project=len(records('PROJECT_INSTANCE_CANDIDATE')),provider=len(records('PROVIDER_CANDIDATE')),compatibility=len(records('COMPATIBILITY_LAYER_CANDIDATE')),assets=len(asset_map),artifacts=len(artifact_map),carried_issues=len(carry),new_risks=len(newrisk)),ensure_ascii=False))
