"""Semantic review and candidate reports. Does not execute any legacy instruction.
Pre-interruption evidence remains immutable. Initial automated inventory is retained
as a discovery draft before semantic refinements to Stage-owned actual outputs.
"""
import collections, hashlib, json, os, re, subprocess
from pathlib import Path
import yaml
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[3];os.chdir(ROOT)
def h(b):return hashlib.sha256(b).hexdigest()
def load(n):return [json.loads(l) for l in (RUN/n).open()]
def put(n,v,k='yaml'):
    with (RUN/n).open('x',encoding='utf-8') as f:
        if k=='jsonl':
            for x in v:f.write(json.dumps(x,ensure_ascii=False)+'\n')
        elif k=='json':json.dump(v,f,ensure_ascii=False,indent=2)
        else:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
def aid(p):return 'ASSET-'+h(p.encode())[:14]
def ev(p,line=1):return {'path':p,'line':line,'source_sha256':U.get(p,{}).get('sha256'),'evidence':'evidence/DISCOVERY_UNIVERSE.jsonl#'+p}
U={x['path']:x for x in load('evidence/DISCOVERY_UNIVERSE.jsonl')}
F={x['path']:x for x in load('evidence/CONTENT_FEATURES.jsonl')}
A=load('AI_ASSET_INVENTORY.jsonl');initial=h((RUN/'AI_ASSET_INVENTORY.jsonl').read_bytes())
put('evidence/AI_ASSET_DISCOVERY_DRAFT.jsonl',A,'jsonl')
# Operational archives and placeholders must not be mistaken for canonical sources.
for a in A:
    p=a['path']
    if '/visual-loop/LOOP_RUNS/' in p:
        a['asset_type']='STATE';a['authority']['canonicality']='OPERATIONAL';a['authority']['source_of_truth_candidate']='VISUAL_RUN_EVIDENCE';a['migration'].update(candidate_owner_stage='09',candidate_target='VISUAL_RUN_EVIDENCE')
    if p.endswith('.gitkeep'):
        a['classification'].update(action='IGNORE',reason='Empty directory placeholder; keep in place, not authored canonical content');a['authority']['canonicality']='REFERENCE'
    if a['content_access']['mode']=='METADATA_ONLY':a['evidence_refs']=['evidence/DISCOVERY_UNIVERSE.jsonl#'+p]
    if p.startswith('tools/anydesign/examples/'):
        a['authority']['canonicality']='DERIVED';a['migration'].update(candidate_owner_stage='09',candidate_target='DESIGN_PROVIDER_EXAMPLES')
    if p.startswith('docs/governance/') and '生成白话文档方案' in p:
        a['asset_type']='POLICY';a['authority']['canonicality']='REFERENCE';a['classification'].update(action='MERGE',reason='Publishing policy copies across legacy source/project/temp; future reconcile after authority review; no merge now');a['migration'].update(candidate_owner_stage='10',candidate_target='PUBLISHING_RULES')
# Metadata-only registry for 15 ignored governed images also discovered by Stage 00.
up=ROOT/'.banyan-refactor/stages/00/stage00-precheck-20260920T083254Z'
for x in map(json.loads,(up/'evidence/FILE_INVENTORY.jsonl').open()):
    if x.get('governed') and x['path'] not in {a['path'] for a in A}:
        p=x['path'];A.append(dict(asset_id=aid(p),path=p,repository_relative=True,origin=dict(tracked_state=x['git_state'],discovered_by=['STAGE00_GOVERNED_IGNORED','ROOT_PATH'],first_seen_ref='WORKTREE',historical_only=False),asset_type='PROJECT_FACT',subtype='LOCAL_IMAGE_RESOURCE',classification=dict(action='REFERENCE',confidence='MEDIUM',reason='Ignored governed local resource retained; authorship and visual semantics not inferred'),content_access=dict(mode='METADATA_ONLY',secret=False),authority=dict(source_of_truth_candidate='PROJECT_RESOURCE',canonicality='REFERENCE',status_if_known=None),relations=dict(references=[],referenced_by=[],generated_from=[],generates=[],symlink_target=None),migration=dict(candidate_owner_stage='04',candidate_target='PROJECT_RESOURCE_MAP',candidate_action='INDEX_ONLY',open_question='Confirm provenance and source role without moving assets'),evidence_refs=['evidence/DISCOVERY_UNIVERSE.jsonl#'+p],notes=['Binary bytes were hashed under inherited safe scope; no image semantic inspection.']))
hist=load('evidence/HISTORICAL_ASSETS.jsonl');hg=collections.defaultdict(list)
for x in hist:hg[x['path']].append(x['commit'])
for p,cs in hg.items():
    A.append(dict(asset_id=aid(p),path=p,repository_relative=True,origin=dict(tracked_state='HISTORICAL_ONLY',discovered_by=['GIT_HISTORY'],first_seen_ref=cs[0],historical_only=True,deletion_commits=cs),asset_type='PUBLISHING_ARTIFACT',classification=dict(action='LEGACY',confidence='MEDIUM',reason='Deleted publishing paths observed in reachable local Git; deduplicated by path, no historical blob read'),content_access=dict(mode='METADATA_ONLY',secret=False),authority=dict(source_of_truth_candidate='HISTORICAL_REFERENCE',canonicality='LEGACY',status_if_known='DELETED_IN_CURRENT_TREE'),relations=dict(references=[],referenced_by=[],generated_from=[],generates=[],symlink_target=None),migration=dict(candidate_owner_stage='10',candidate_target='PUBLISHING_HISTORY_INDEX',candidate_action='INDEX_ONLY',open_question='Stage 10 checks replacement lineage before any retirement'),evidence_refs=['evidence/HISTORICAL_ASSETS.jsonl#'+p],notes=['No deleted body restored or read.']))
with (RUN/'AI_ASSET_INVENTORY.jsonl').open('w') as f:
    for a in A:f.write(json.dumps(a,ensure_ascii=False)+'\n')
put('evidence/ASSET_REVIEW_REFINEMENTS.json',dict(initial_inventory_sha256=initial,initial_retained_at='evidence/AI_ASSET_DISCOVERY_DRAFT.jsonl',final_inventory_sha256=h((RUN/'AI_ASSET_INVENTORY.jsonl').read_bytes()),refinements=['Visual runs are operational, not canonical','Placeholders ignored without deletion','Publishing policy copies are MERGE candidates only','15 governed ignored resources retained explicitly','5 historical-only paths from 10 deletion events retained explicitly']), 'json')

MAIN='docs/governance/common_prd_v3.1/通用文档提示词v3.1.md'
USAGE='docs/governance/common_prd_v3.1/通用文档提示词v3.1完整使用说明.md'
GUIDE='docs/project/AI_DOCUMENTATION_GUIDE.md'
caps=[]
def cap(key,name,description,refs,behaviors,inputs,outputs,guards,fail,owner,target,boundary='GENERIC_CORE_CANDIDATE',question='How will Stage 02 preserve these semantics without fixed project paths?',confidence='HIGH'):
    assert all(p in U for p,line in refs)
    caps.append(dict(capability_id='CAP-'+key,name=name,description=description,legacy_sources=sorted(set(p for p,l in refs)),behaviors=behaviors,inputs=inputs,outputs=outputs,guards=guards,failure_semantics=fail,evidence_refs=[ev(p,l) for p,l in refs],value_level='HIGH',candidate_owner_stage=owner,candidate_target_capability=target,candidate_action='GENERALIZE' if boundary=='GENERIC_CORE_CANDIDATE' else 'PROJECT_ONLY' if boundary=='PROJECT_ONLY_CANDIDATE' else 'COMPATIBILITY_READ' if boundary=='COMPATIBILITY_CANDIDATE' else 'MAP',confidence=confidence,open_question=question,candidate_boundary=boundary))
cap('AUTH','工作范围与授权','文档/代码/生产动作分离；授权不从旧提示词自动继承',[(MAIN,465),(GUIDE,37)],['文档阶段限制写域','代码需 ALLOW_CODE_CHANGES 与 Ready 批次','提交、推送、发布需要授权'],['用户范围','批次状态'],['允许动作与阻塞说明'],['不写凭证','不把现码当未来需求'],['缺授权停止目标动作，保留诊断'],'14','PERMISSION_GOVERNANCE')
cap('PROFILE','项目变量与接入模式','当前基线与历史参考语义不同',[(MAIN,243),('docs/project/PROJECT_VARIABLES.md',1)],['收集变量而不填造 TBD','CURRENT_BASELINE 保护现状兼容','HISTORICAL_REFERENCE 不绑定旧架构'],['项目变量','仓库事实'],['项目配置候选','变量迁移关系'],['新项目与已有项目区分'],['未知保持 TBD'],'04','PROJECT_VARIABLE_MIGRATION',question='How are legacy variables mapped/derived/defaulted without silently enabling capabilities?')
cap('INTAKE','来源投放与冻结','从来源登记到可审计需求输入',[(MAIN,1047),(MAIN,1088)],['登记批次/来源/冲突','区分事实、推断、候选','冻结范围后才允许 PRD 准入'],['原始资料','来源批次'],['来源索引','问题/决策/冲突清单'],['原件不改写','不从静态设计推断后端'],['P0/P1 阻塞后继必经阶段'],'07','SOURCE_INTAKE_COMPATIBILITY')
cap('PRD','PRD 生命周期与评审','Draft、Review、Approved、Baselined 不能混同',[(MAIN,1112),(MAIN,1132),(MAIN,1198)],['准入审计','按模块起草','明确批准','保留历史基线'],['来源/DEC','验收场景'],['PRD','Given/When/Then'],['PRD 不混技术细节','未批准不得写 Approved'],['阻塞项保留，不伪升状态'],'07','PRD_GOVERNANCE')
cap('IDP','知情决策协议','解释、初选、影响复述、确认、受控应用分开',[(MAIN,496),(USAGE,222),('.cursor/rules/collaboration-judgment.mdc',1)],['解释真实方案与影响','问题呈现在会话正文','首次选择不等于应用批准','已确认项不重复问，失效则复核'],['决策背景','选择','约束'],['确认记录','DEC/ADR/CR/UI-DEC'],['取消/沉默不当确认','项目 DEC-042 与通用题数规则分开记录'],['出现新权衡回评审；未确认保持 TBD'],'05','INTERACTION_DECISION_ROUTING',question='How to preserve informed decisions while reconciling generic HIGH=1/LOW=2 and project max-five override?')
cap('ARCH','架构和模块边界参与门禁','G6/G7 决策完成才生成，显式直接 Draft 允许 TBD',[(MAIN,987),(MAIN,1229),(MAIN,1329)],['评审状态和应用状态双门禁','模块边界继承参与模式','Draft 独立批准后进入细化'],['PRD','参与模式','应用结构'],['架构','MODULE_BOUNDARIES','技术设计'],['口令不自动改参与模式','DIRECT_DRAFT 必须伴随允许 TBD'],['缺决策停止对应生成'],'05','ARCHITECTURE_PARTICIPATION_WORKFLOW')
cap('SCHEMA','文档状态与编号','统一元信息、状态、结论标签',[(MAIN,816)],['保留负责人、来源、版本、替代关系','禁止把候选写已确认'],['文档类型','状态证据'],['元信息与编号'],['不能仅因文件存在视为完成'],['状态证据不足保持原态'],'03','ARTIFACT_CONTRACT_COMPATIBILITY')
cap('IDREF','编号占用与在引用规则保护','同编号不换题，按语义修复而非全局替换',[(MAIN,903),('docs/project/decisions/ADR-049.md',1)],['新题最大号+1','在引用正文保持可读','历史日志不改写','旧主题恢复时语义分类引用'],['ID/标题引用','Git 历史'],['引用对照','替代链'],['仍被引用不能删除/清空','修复先确认'],['引用含混阻塞自动改写'],'03','REFERENCE_INTEGRITY')
cap('TRACE','全链路追踪','从来源、决策到测试发布的证据关系',[(MAIN,1877),('docs/project/acceptance/TRACE_MATRIX.md',1)],['连接来源→DEC→PRD→设计→API/数据→UI→批次→Commit→测试→发布'],['工程产物','Git/测试证据'],['TRACE_MATRIX'],['UI 可空但不得伪造'],['缺边登记开放项'],'13','EVIDENCE_TRACE')
cap('CHANGE','变更与版本路由','不同 PRD 状态决定 CR 应用路径',[(MAIN,1918),(USAGE,2490)],['区分缺陷、业务改变、技术改变、纯 UI','Approved/Baselined 保留旧版','变更影响扩散到设计/批次/测试'],['新诉求','PRD 状态'],['CR','新版本 Draft'],['不静默覆盖基线'],['冲突未确认不 APPLY'],'06','CANONICAL_CHANGE_APPLY')
cap('PARALLEL','Parallel Draft 临时袋','多人同分支错开正式真源写入',[(USAGE,2362),(USAGE,2397),(USAGE,2440),('docs/project/changes/变更稿模式.md',1)],['一次初始化说明入口与 ignore','只写 DRAFT-* 不预占正式编号','纳入先出对照表','按 PRD 状态走现有 CR 通道'],['INDEX/BAG/DRAFT','当前正式最大号'],['草稿袋','晋升对照表'],['不改正式文档/看板/代码','全部迁完且用户说纳入完成才清袋'],['冲突/未确认保留袋；不创建第四条变更管道'],'06','PARALLEL_DRAFT_PROMOTION')
cap('RECONCILE','36A 批次正式口径收口','下一批之前逐条核对业务差异',[(MAIN,1949),(USAGE,2050)],['业务差异→CR→收入 PRD','纯实现不造 CR','无差异记录无待收口','发布投影标 stale 后再同步'],['本批改动','现行 PRD'],['收口记录','CR/PRD 关系'],['收口未完成不启动下一批'],['未确认差异保留待决'],'06','BATCH_CANONICAL_RECONCILIATION')
cap('TEST','自测桩与验收口径完整性','不以改规则获得测试通过',[(MAIN,2028),(USAGE,1970)],['临时桩测后拆除','产品修复留下','灌测试数据不等于改业务规则'],['测试计划','临时桩','真实缺陷'],['拆桩/修复证据','验收结果'],['不得为过验收修改口径'],['无拆桩/保留证据不得声明通过'],'14','TEST_INTEGRITY')
cap('PROGRESS','证据驱动多轴进度','文档、开发、交付、测试各自计算',[(MAIN,1972),('docs/project/progress/PROGRESS_REGISTER.yaml',1)],['登记是真源，看板是总览','范围变化重算分母','关闭 UI/视觉循环不入文档分母','Blocked 不清原进度'],['权重/状态','证据'],['进度登记','看板'],['没有证据不提高进度','范围未冻结 N/A'],['不能把建文件/合并当验收'],'16','PROGRESS_PROJECTION')
cap('HANDOVER','工作日志与接管','记录未完成、风险、Git 和下一步',[(MAIN,2043),('docs/project/progress/HANDOVER_REGISTER.md',1)],['实质工作后日志','核对 Git/文档/测试','交接保留配置需求但不写凭证'],['工作差异','批次','测试结果'],['WORKLOG','HANDOVER'],['未提交/未推送不隐瞒'],['接管验证失败保持阻塞'],'11','OPERATIONAL_HISTORY_INDEX')
cap('CONTEXT','新窗口续做','从真实文档进度恢复而非会话猜测',[(USAGE,145),('docs/project/progress/PROJECT_DASHBOARD.md',1)],['看板→登记→相关 DEC/CR','推荐一个下一步','不重跑 G0/G1','识别草稿袋与 PLAIN_SYNC stale'],['项目事实','当前 Git'],['恢复点','下一步'],['以实际产物为准','不自动提高阶段'],['信息不一致说明并停在对应门禁'],'12','CONTEXT_RECOVERY')
cap('UI_SCOPE','UI 逻辑范围与应用分闸','G5.5 逻辑范围与 G9.1 应用目录不同',[(MAIN,980),(MAIN,1005),(MAIN,1014)],['应用来自实际架构映射','总闸加应用名单','未启用应用不阻断开发','部分页面允许 Partial'],['PRD','应用架构','启用名单'],['UI_SCOPE_MAP','UI_APPLICATION_MAPPING'],['不从 PRD 提前猜代码目录','空名单全关'],['未批准 UI 不作为约束'],'08','UI_APPLICATION_GOVERNANCE')
cap('UI_CONTRACT','分层 UI 合并与批次契约','页面到 shared 的批准规范与 locked 规则',[(MAIN,939),(MAIN,1792)],['筛适用范围','低到高继承','只取批准版本','批次绑定有效 contract'],['UI_SPEC','PRD','批次'],['EFFECTIVE_UI_CONTRACT'],['业务/权限/安全不可覆盖','同层双有效版本不按日期猜'],['冲突进入 UI-DEC/CR'],'08','UI_CONTRACT_COMPILATION')
cap('UI_GATE','素材→Draft→批准→点名换皮','令牌确认不是开发批准',[(MAIN,1014),('.cursor/rules/ui-spec-gate.mdc',1)],['anydesign 产物登记为素材','28A Draft 后 29 批准','每步汇报当前节/下一口令/禁止误称'],['设计图','tokens','用户点名范围'],['Draft UI_SPEC','批准证据'],['预定页只 Partial','禁止 /v2 旁路'],['未批准不能改页面'],'08','UI_DESIGN_IMPLEMENTATION_GATE')
cap('VISUAL','独立视觉修复循环','指定页面和允许文件的小范围迭代', [('.cursor/skills/visual-repair-loop/SKILL.md',1),('docs/project/ui-design/visual-loop/LOOP_RUNS/20260919-gongyi_online-tabbar/RESULT.md',1),('docs/project/ui-design/visual-loop/LOOP_RUNS/20260919-gongyi_online-nearby/RUN.yaml',1)],['Round0 RUN','截图→DIFF→范围内修复','最多声明轮数','覆盖豁免高于截图'],['应用/页面/图','viewport','allowed_files'],['RUN','DIFF','RESULT','截图'],['用户未点名不执行','不改 API/权限或扩大页面','不改变批准规范'],['超轮数停止；用户叫停可回退；in_progress 不伪称成功'],'09','VISUAL_REPAIR_WORKFLOW')
cap('PUBLISH','白话知识发布','骨架、初次正文、差异同步三条明确路径',[(USAGE,2100),('docs/project/plain-spec/白话文档生成方案.md',1),('docs/project/progress/PLAIN_SYNC.yaml',1)],['先有映射再写正文','按用户文件清单生成','只同步 stale 关联内容','业务规则与实际菜单来源分开'],['正式规则','页面事实','PLAIN_SYNC'],['白话说明','同步状态'],['派生文档不反向决定 PRD','不得全量重写71篇','架构图用业务话'],['无基线不能差异同步'],'10','KNOWLEDGE_PUBLISHING')
cap('EDITOR','Cursor 入口与项目覆盖','规则入口及 symlink provider 保持兼容', [('.cursor/rules/collaboration-judgment.mdc',1),('tools/anydesign/PROJECT_INSTALL.md',1)],['按路径发现规则/skill','入口引用工具真身','记录项目特定覆盖'],['rules','skills','项目事实'],['编辑器行为候选映射'],['不把 .cursor 当 Generic Core 固定路径'],['适配未验证保留旧入口'],'15','EDITOR_ADAPTER_CONTRACT',boundary='COMPATIBILITY_CANDIDATE')
cap('PORT','项目端口绑定','多前后端映射不能串用', [('.cursor/rules/port-binding.mdc',1)],['页面/服务对应固定本地端口','源品8035与ToB8037区别'],['项目应用映射'],['正确联调目标'],['端口与项目业务只留 project instance'],['映射未知先核对，不猜服务'],'04','PROJECT_ENDPOINT_MAPPING',boundary='PROJECT_ONLY_CANDIDATE')
cap('SQL','增量 SQL 交付习惯','本地联调与测试交付不同', [('docs/开发指导.md',92)],['结构改动编号增量 SQL','SQL可重复执行','数据调整先确认'],['表结构变更','部署环境'],['SQL交付清单'],['不把 local.env 作为交付','不在本阶段运行 SQL'],['缺交付 SQL 不宣称测试部署完成'],'04','PROJECT_DELIVERY_CONVENTIONS',boundary='PROJECT_ONLY_CANDIDATE')
cap('COMMIT','既有提交校验与授权','项目级 commitlint/Husky 与通用提交禁令分开',[(MAIN,479),('nunu-go-api/app/admin/web/.husky/commit-msg',1),('nunu-go-api/app/admin/web/commitlint.config.cjs',1)],['commit-msg 调 commitlint','可选 type/scope 提示','useAI=false','仅授权后提交'],['暂存差异','提交说明','授权'],['提交计划/校验结果'],['Git Author 是事实身份，不推断物理操作者','当前未安装为根 hooksPath 不等于全面生效'],['缺脚本或授权停止，不补造已执行校验'],'05','SEMANTIC_COMMIT_PRACTICE',boundary='COMPATIBILITY_CANDIDATE')
cap('MERGE','旧协作合码指导','特定分支与目录归属的历史合并流程', [('docs/temp/SassDesign/合并代码指导.md',24)],['先检查工作区','合并前核对远程提交','冲突按目录语义','合并后构建'],['旧分支拓扑','路径归属'],['合码记录'],['不得偷偷 stash','lease失败停止','禁止猜 ours 整文件'],['不把旧 reset/force 流程作为当前许可'],'07','LEGACY_COLLABORATION_REFERENCE',boundary='COMPATIBILITY_CANDIDATE')
cap('DESIGN','AnyDesign 全量与单元素模式','从视觉输入提取设计语义，不制造正式业务规则', [('tools/anydesign/SKILL.md',1),('tools/anydesign/references/element-copy.md',1)],['Full 输出 design.md','Element 输出 element.md','来源失败明确说明','art direction 与重建建议'],['截图/URL/Figma','范围/强调'],['design.md/element.md','tokens/a11y'],['输出是素材，未经批准非正式 UI_SPEC','不绕访问保护'],['输入不可用不虚构内容'],'09','DESIGN_ANALYSIS_PROVIDER',boundary='PROVIDER_CANDIDATE')
tool_specs=[
 ('CSS','extract_css_vars.py','CSS 变量提取与摘要',['URL样式表','CSS变量'],['变量JSON','摘要'],['区分显式token与推断'],['网络/参数失败报错']),
 ('CAPTURE','capture_site.py','页面截图与计算样式采集',['URL','viewports/selector'],['截图','computed-style digest'],['限制帧数与元素范围'],['缺Playwright/捕获错误非成功']),
 ('COLORS','extract_colors.py','图像主色提取',['图像','颜色数量'],['颜色与面积占比'],['结果仅视觉证据'],['缺Pillow/坏图失败']),
 ('A11Y','check_contrast.py','对比度检查',['FG/BG颜色对'],['WCAG对比度报告'],['检查结果不替代业务验收'],['参数格式错误报错']),
 ('LINT','lint_design_md.py','设计文档结构校验',['design.md'],['lint报告'],['frontmatter/引用/组件/章节规则'],['结构失败非零退出']),
 ('TOKENS','build_tokens_json.py','设计令牌生成',['design.md frontmatter'],['DTCG tokens JSON'],['机器派生不手工编造'],['解析错误失败']),
 ('DRIFT','verify_design.py','令牌与线上设计漂移比较',['tokens JSON','URL'],['drift报告'],['与正式批准状态分开'],['获取或比对失败输出错误']),
 ('EXPORT','export_for_claude_design.py','设计交付包导出',['design.md','tokens'],['CSS','Tailwind','DOCX/PPTX品牌包'],['保留源关联','不等同 Codex Adapter'],['输入/依赖不满足失败']),
]
for key,fn,name,ins,outs,guards,fail in tool_specs:cap(key,name,'独立工具能力；源代码与函数/CLI静态审阅，未实际执行', [('tools/anydesign/scripts/'+fn,1),('tools/anydesign/SKILL.md',107)],['以显式输入生成可定位派生结果'],ins,outs,guards,fail,'09','DESIGN_'+key+'_PROVIDER',boundary='PROVIDER_CANDIDATE',question='Which provider interface preserves input/output and failure semantics across projects?')
put('LEGACY_AI_CAPABILITY_INVENTORY.jsonl',caps,'jsonl')
put('PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml',dict(schema_version='stage01-preliminary-v1',stage_id='01',scope='CANDIDATES_ONLY; no final owner or activation',matrix=[{**{k:c[k] for k in ['capability_id','legacy_sources','value_level','candidate_owner_stage','candidate_target_capability','candidate_action','confidence','open_question','evidence_refs']},'drop_approval_status':'NOT_APPLICABLE','execution_allowed':False} for c in caps]))
core=[]
for c in caps:
    deps=[];paths=[];terms=[]
    for p in c['legacy_sources']:
        if p in F and U[p]['coverage']=='COVERED_CONTENT':
            t=Path(p).read_text()
            paths+=re.findall(r'(?:docs/project|tools/anydesign|\.cursor)(?:/[A-Za-z0-9_./-]+)?',t)
            terms += [x for x in ['x_shop_server','四业态','五端','8035','8037','mall-online','DEC-042','gongyi_online'] if x in t]
    if terms:deps=['Source mixes project policy/facts with reusable behavior; must parameterize or retain project overlay']
    core.append(dict(capability_or_asset_id=c['capability_id'],candidate_boundary=c['candidate_boundary'],generic_semantics=c['description'],project_specific_dependencies=deps,hardcoded_paths=sorted(set(paths)),business_specific_terms=sorted(set(terms)),cross_project_evidence=['tools/anydesign/examples contains multiple design exemplars; no independent cross-project execution verified'] if c['candidate_boundary']=='PROVIDER_CANDIDATE' else [],purity_risk='MEDIUM: no independent portability verification; source paths and legacy G numbers must not become Core constants',required_abstraction='Separate semantic contract, project source mapping, editor/provider interface; preserve existing layout',candidate_owner_stage='02',confidence='MEDIUM',open_questions=[c['open_question']],evidence_refs=c['evidence_refs']))
put('CORE_CANDIDATE_REPORT.yaml',dict(schema_version='stage01-bootstrap-v1',stage_id='01',architecture_frozen=False,summary=dict(collections.Counter(c['candidate_boundary'] for c in core)),retirement_candidates=[],retirement_reason='No retirement justified while references/compatibility remain; no drop approval requested',candidates=core))

generated=[];ops=[];non_generated=[]
for a in A:
    p=a['path'];q=Path(p);canon=a['authority']['canonicality'];src=a['relations']['references'];historical=a['origin']['historical_only']
    operational=(canon=='OPERATIONAL' or (p.startswith('docs/temp/') and any(k in q.name.lower() for k in ['交接','合并记录','状态','统计'])) )
    if operational:
        ot='WORKLOG' if '/worklogs/' in p else 'HANDOVER' if 'handover' in p.lower() or '交接' in p else 'DASHBOARD' if 'DASHBOARD' in p else 'RUNTIME_STATE' if '/LOOP_RUNS/' in p else 'PROGRESS' if '/progress/' in p else 'OTHER'
        fresh='UNKNOWN; recorded state only, not recomputed runtime success'
        if p.endswith('/RUN.yaml') and '/LOOP_RUNS/' in p:
            j=yaml.safe_load(q.read_text());fresh='RECORDED_STATUS='+str(j.get('status','UNSPECIFIED'))
        ops.append(dict(artifact_id='OP-'+h(p.encode())[:14],path=p,operational_type=ot,authoritative=q.name=='PROGRESS_REGISTER.yaml',consumer=['Project maintainers','Context/recovery/index candidates'],freshness=fresh,historical_value='HIGH: preserve chronology, including aborted and in-progress runs',candidate_owner_stage='09' if '/visual-loop/' in p else '11',candidate_action='INDEX_ONLY',evidence_refs=a['evidence_refs']))
        continue
    eligible=p.startswith('docs/project/') and canon!='REFERENCE' or p.startswith('tools/anydesign/examples/') and q.suffix in ('.md','.json','.css')
    if not eligible or historical or q.name=='.gitkeep':
        non_generated.append(dict(path=p,reason='Operational separate / source or binary provenance unknown / historical metadata / placeholder / input/tool, not claimed AI-generated'))
        continue
    cls='DERIVED' if (canon=='DERIVED' or '/delivery/ui-contracts/' in p or '/materials/design-docs/' in p or '/materials/tokens/' in p) else 'CANONICAL'
    role='PROJECT_CANONICAL_DOCUMENT' if cls=='CANONICAL' else 'DERIVED_PROJECTION'
    if '/plain-document/' in p:role='PROJECT_GUIDE_DERIVED'
    elif '/prd/' in p:role='REQUIREMENT_SOURCE'
    elif '/baseline/' in p or '/decisions/' in p or '/changes/' in p:role='DECISION_CHANGE_HISTORY'
    elif '/ui-design/' in p:role='UI_SPEC_SOURCE' if cls=='CANONICAL' else 'UI_DESIGN_DERIVED'
    elif '/api/' in p or '/database/' in p:role='TECHNICAL_CONTRACT_SOURCE'
    inferred_sources=src[:]
    if not inferred_sources:
        inferred_sources=[GUIDE] if cls=='CANONICAL' else ['docs/project/progress/PLAIN_SYNC.yaml'] if '/plain-document/' in p else ['tools/anydesign/SKILL.md'] if '/materials/' in p or p.startswith('tools/') else ['docs/project/ui-design/UI_DESIGN_REGISTER.yaml']
    generated.append(dict(artifact_id='ART-'+h(p.encode())[:14],path=p,artifact_class=cls,source=inferred_sources,source_relation_basis='Literal links where available; otherwise governing source candidate, NOT proven exact generation lineage',consumer=['Project engineers','Governance/guide consumers'],rebuildability='NOT_REBUILDABLE_AS_AUTHORITY; preserve approved/history content' if cls=='CANONICAL' else 'PARTIAL_OR_UNKNOWN; sources present but exact prompts/toolchain/replay not verified',freshness='STATUS_RECORDED_NOT_RECOMPUTED: '+str(a['authority']['status_if_known'] or 'UNKNOWN'),candidate_source_role=role,candidate_action='MAP' if cls=='CANONICAL' else 'INDEX_ONLY',keep_or_migrate='KEEP_IN_PLACE + MAP + INDEX',integrity_risk='MEDIUM: exact AI authorship unknown; preserve status/IDs/references and original content',references=src,evidence_refs=a['evidence_refs'],ai_authorship='CANDIDATE_AI_ASSISTED_GOVERNANCE_OUTPUT; individual file authorship not established',approval_status=a['authority']['status_if_known'],approval_not_inferred_from_path=True))
put('AI_GENERATED_ARTIFACT_INVENTORY.jsonl',generated,'jsonl')
put('OPERATIONAL_ARTIFACT_INVENTORY.jsonl',ops,'jsonl')
put('evidence/ARTIFACT_ELIGIBILITY.jsonl',non_generated,'jsonl')
put('PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml',dict(schema_version='stage01-preliminary-v1',stage_id='01',qualification='Candidate generated/AI-assisted corpus; authorship is not asserted. Canonicality denotes source role, not approval.',matrix=[{**{k:g[k] for k in ['artifact_id','path','artifact_class','candidate_source_role','keep_or_migrate','candidate_action','integrity_risk','rebuildability','evidence_refs']},'drop_approval_status':'NOT_APPLICABLE','execution_allowed':False} for g in generated],operational_mapping=[dict(artifact_id=o['artifact_id'],path=o['path'],candidate_owner_stage=o['candidate_owner_stage'],candidate_action='INDEX_ONLY',keep_or_migrate='KEEP_IN_PLACE') for o in ops]))
put('LEGACY_CLASSIFICATION_REPORT.yaml',dict(schema_version='stage01-bootstrap-v1',stage_id='01',summary={'total_assets':len(A),**{k:sum(a['classification']['action']==k for a in A) for k in ['KEEP','MERGE','SPLIT','REWRITE','REFERENCE','LEGACY','IGNORE']},'UNCLASSIFIED':sum(a['asset_type']=='UNCLASSIFIED' for a in A)},all_actions_candidates_only=True,items=[dict(asset_id=a['asset_id'],path=a['path'],disposition=a['classification']['action'],reason=a['classification']['reason'],confidence=a['classification']['confidence'],evidence_refs=a['evidence_refs'],candidate_owner_stage=a['migration']['candidate_owner_stage'],next_stage_plan=a['migration']['open_question']) for a in A]))
print(json.dumps(dict(assets=len(A),caps=len(caps),generated=len(generated),canonical=sum(x['artifact_class']=='CANONICAL' for x in generated),operational=len(ops),core=collections.Counter(c['candidate_boundary'] for c in core)),ensure_ascii=False))
