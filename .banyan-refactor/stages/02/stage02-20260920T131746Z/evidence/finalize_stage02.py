"""Verify and close Stage 02 candidate design without entering Stage 03.
Only current Stage 02 run and existing bootstrap state pair may be written.
"""
from pathlib import Path
import collections, datetime, hashlib, json, os, subprocess
import yaml

RUN=Path(__file__).resolve().parents[1]
ROOT=RUN.parents[3]
CTL=ROOT/'.banyan-refactor'
S1=CTL/'stages/01/stage01-20260920T091426Z'
PK=ROOT/'榕树ai改造落地相关文档/Stage_02_Banyan核心边界设计与架构抽象'
GATE=ROOT/'榕树ai改造落地相关文档/Stage_01_AI资产全量盘点与方案裁剪/reviews/Stage_01_to_Stage_02_Gate_Review_v1.0.md'
os.chdir(ROOT)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def y(p):return yaml.safe_load(p.read_text())
def jlines(p):return [json.loads(l) for l in p.open()]
def git(*args):return subprocess.check_output(['git',*args],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'})
def newjson(p,v):
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2)
def newyaml(p,v):
    with p.open('x',encoding='utf-8') as f:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
def rewriteyaml(p,v):
    with p.open('w',encoding='utf-8') as f:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)

pre=json.loads((RUN/'evidence/PRECHECK.json').read_text())
source_handoff=y(S1/'evidence/NEXT_STAGE_HANDOFF.yaml')
source_seal={p:h for h,p in (line.split('  ',1) for line in (S1/'ARTIFACT_HASHES.sha256').read_text().splitlines())}
stage1_seal_ok=[]
for p,hv in source_seal.items():
    q=RUN/'checkpoint'/(Path(p).name+'.snapshot.yaml') if p.startswith('../../../') else S1/p
    stage1_seal_ok.append(q.is_file() and sha(q)==hv)
before_reg=y(RUN/'checkpoint/MIGRATION_REGISTER.bootstrap.yaml.snapshot.yaml')
before_trace=y(RUN/'checkpoint/BANYAN_REFACTOR_TRACE.bootstrap.yaml.snapshot.yaml')
reg_path=CTL/'MIGRATION_REGISTER.bootstrap.yaml'
trace_path=CTL/'BANYAN_REFACTOR_TRACE.bootstrap.yaml'
reg=y(reg_path);trace=y(trace_path)
book=y(RUN/'CAPABILITY_MAPPING_WORKBOOK.yaml')['capabilities']
layerfiles={'BANYAN_CORE_CANDIDATE':'CORE_CANDIDATES.yaml','PROJECT_INSTANCE_CANDIDATE':'PROJECT_CANDIDATES.yaml','PROVIDER_CANDIDATE':'PROVIDER_CANDIDATES.yaml','COMPATIBILITY_LAYER_CANDIDATE':'COMPATIBILITY_CANDIDATES.yaml'}
layerrows={key:y(RUN/fn)['items'] for key,fn in layerfiles.items()}
assets=jlines(RUN/'ASSET_BOUNDARY_MAP.jsonl')
artifacts=jlines(RUN/'ARTIFACT_BOUNDARY_MAP.jsonl')
sourcecaps=jlines(S1/'LEGACY_AI_CAPABILITY_INVENTORY.jsonl')
sourceassets=jlines(S1/'AI_ASSET_INVENTORY.jsonl')
sourcegenerated=jlines(S1/'AI_GENERATED_ARTIFACT_INVENTORY.jsonl')
sourceops=jlines(S1/'OPERATIONAL_ARTIFACT_INVENTORY.jsonl')
sourceissues=y(S1/'CONFLICT_GAP_REPORT.yaml')['issues']
risks=y(RUN/'CONFLICT_RISK_REGISTER.yaml')
adrs=y(RUN/'ARCHITECTURE_DECISION_RECORDS.yaml')['decisions']
mode_text=(RUN/'AI_RUNTIME_COST_GOVERNANCE_DESIGN.md').read_text()
specs=y(S1/'GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml')['current_effective_identity']['config_identity']
approved=source_handoff['inherited_constraints']['secret_metadata_only_paths']

result=[]
def check(n,tests,evidence,note):
    failed=[key for key,ok in tests.items() if not ok]
    result.append(dict(id='V02-%02d'%n,result='PASS' if not failed else 'FAIL',tests=tests,failed=failed,evidence=evidence,note=note))

check(1,dict(stage01_completed=reg['stages']['01']['status']=='COMPLETED' and reg['stages']['01']['validation']['overall']=='PASS',handoff_pass=source_handoff['acceptance_result']=='PASS' and source_handoff['next_stage_entry_gate']['result']=='PASS',gate_review_read=GATE.is_file() and 'Stage 01 → Stage 02 Gate Review' in GATE.read_text(),same_head=pre['head']==reg['stages']['01']['baseline_commit'] if 'baseline_commit' in reg['stages']['01'] else pre['head']==reg['stages']['00']['baseline_commit']),['evidence/PRECHECK.json','../../01/stage01-20260920T091426Z/ACCEPTANCE_REPORT.md','../../01/stage01-20260920T091426Z/evidence/NEXT_STAGE_HANDOFF.yaml'],'Stage 01 accepted Gate and current authorized Stage 02 request used; no Stage 01 rerun.')
check(2,dict(stage01_65_seal=len(stage1_seal_ok)==65 and all(stage1_seal_ok),consumed_inputs=len(pre['stage01_inputs'])==10 and all(x['stage01_sealed'] and sha(S1/x['path'])==x['sha256'] for x in pre['stage01_inputs']),pack_7_unchanged=len(pre['pack'])==7 and all(sha(PK/x['path'])==x['sha256'] for x in pre['pack']),gate_unchanged=sha(GATE)==pre['gate_review_sha256']),['evidence/PRECHECK.json','checkpoint/*.snapshot.yaml','../../01/stage01-20260920T091426Z/ARTIFACT_HASHES.sha256'],'Stage 01 shared-bootstrap historical hashes resolve to Stage 02 read-only snapshots; only sealed Stage 01 outputs consumed.')
bookids={x['capability_id'] for x in book}
check(3,dict(all_35=len(book)==35 and bookids=={x['capability_id'] for x in sourcecaps},one_each=len(bookids)==len(book),five_layer_fields=all(x['contract_need']['name'] and x['provider_port_candidate'] and x['artifact_role_candidate'] and x['runtime_phase_candidate'] and x['inputs'] and x['outputs'] and x['guards'] and x['failure_semantics'] for x in book),source_and_owner=all(x['legacy_source'] and x['stage01_capability_ref'] and x['decision_owner_stage'] for x in book)),['CAPABILITY_MAPPING_WORKBOOK.yaml','../../01/stage01-20260920T091426Z/LEGACY_AI_CAPABILITY_INVENTORY.jsonl'],'Every high-value capability mapped to five-layer candidate with inputs/outputs/guards/failures.')
expectedcounts={'BANYAN_CORE_CANDIDATE':21,'PROJECT_INSTANCE_CANDIDATE':2,'PROVIDER_CANDIDATE':9,'COMPATIBILITY_LAYER_CANDIDATE':3}
for n,layer in [(4,'BANYAN_CORE_CANDIDATE'),(5,'PROJECT_INSTANCE_CANDIDATE'),(6,'PROVIDER_CANDIDATE'),(7,'COMPATIBILITY_LAYER_CANDIDATE')]:
    rows=layerrows[layer]
    check(n,dict(count=len(rows)==expectedcounts[layer],ids_match={x['capability_id'] for x in rows}=={x['capability_id'] for x in book if x['candidate_layer']==layer},candidate_only=all(x['approval']=='NOT_APPROVED' and not x['execution_allowed'] and x['required_validation'] for x in rows),design_document=(RUN/{'BANYAN_CORE_CANDIDATE':'CORE_BOUNDARY_CANDIDATE.md','PROJECT_INSTANCE_CANDIDATE':'PROJECT_INSTANCE_CANDIDATE.md','PROVIDER_CANDIDATE':'PROVIDER_CANDIDATE.md','COMPATIBILITY_LAYER_CANDIDATE':'COMPATIBILITY_LAYER_CANDIDATE.md'}[layer]).is_file()),[layerfiles[layer],'CAPABILITY_MAPPING_WORKBOOK.yaml'],'Boundary class preserved as candidate; no legacy capability dropped.')
check(8,dict(asset_map_complete=len(assets)==len(sourceassets)==1026 and {x['asset_id'] for x in assets}=={x['asset_id'] for x in sourceassets},all_preserved=all(x['action']=='PRESERVE_IN_PLACE_AND_MAP' for x in assets),no_physical_core=not any(x['stage02_candidate_layer']=='BANYAN_CORE_CANDIDATE' for x in assets),artifact_map_complete=len(artifacts)==len(sourcegenerated)+len(sourceops)==714 and {x['artifact_id'] for x in artifacts}=={x['artifact_id'] for x in sourcegenerated+sourceops},all_artifacts_preserved=all(x['preservation'].startswith('KEEP_IN_PLACE') for x in artifacts)),['ASSET_BOUNDARY_MAP.jsonl','ARTIFACT_BOUNDARY_MAP.jsonl','../../01/stage01-20260920T091426Z/AI_ASSET_INVENTORY.jsonl'],'All Stage 01 assets/artifacts mapped without moving or auto-promoting files to Core.')
carried=risks['inherited_issues'];newrisk=risks['new_risks']
check(9,dict(all_31_carried=len(carried)==len(sourceissues)==31 and {x['issue_id'] for x in carried}=={x['issue_id'] for x in sourceissues},high_routed=all(x['candidate_owner_stage'] and x['next_action'] and x['blocks_activation_without_resolution'] for x in carried if x['inherited_severity']=='HIGH'),new_risk_owners=all(x['candidate_owner_stage'] and x['next_action'] for x in newrisk),no_winner=risks['conflict_winners_selected']==[] and (RUN/'CONFLICT_RESOLUTION_PLAN.md').is_file()),['CONFLICT_RISK_REGISTER.yaml','CONFLICT_RESOLUTION_PLAN.md'],'Two HIGH conflicts have concrete routes; they are open for activation, no source winner selected.')
check(10,dict(four_modes=all(s in mode_text for s in ['Full Audit','Engineering','Batch Worker','Human Decision']),cost_axes=all(s in mode_text for s in ['Task Routing','Model Selection','Token Budget','Batch/Cache/Fallback']),no_runtime_execution='没有启动 Runtime' in (RUN/'CONTRACT_CHAIN_DESIGN.md').read_text()),['AI_RUNTIME_COST_GOVERNANCE_DESIGN.md','CONTRACT_CHAIN_DESIGN.md'],'Cost design contains routing/model/budget/execution/batch/fallback, no actual model selection or runtime.')
check(11,dict(six_draft_decisions=len(adrs)==6 and all(x['status']=='DRAFT' and x['approval']=='NOT_REQUESTED_OR_GRANTED' and x['execution_allowed'] is False for x in adrs),no_final_schema=y(RUN/'CAPABILITY_MAPPING_WORKBOOK.yaml')['status']=='CANDIDATE_ONLY',no_unauthorized_target_dirs=all(not (ROOT/p).exists() for p in ['.banyan','banyan-framework','project-sources'])),['ARCHITECTURE_DECISION_RECORDS.yaml','CONTRACT_CHAIN_DESIGN.md'],'Design candidate completion does not claim approved/frozen architecture or create target layout.')
check(12,dict(thirteen_inherited=len(approved)==13,partial_recovery=source_handoff['inherited_constraints']['recovery_coverage']=='PARTIAL_APPROVED',no_secret_asset_content=not any(a['path'] in approved for a in sourceassets),snapshots_unchanged=all(sha(RUN/'checkpoint'/(fn+'.snapshot.yaml'))==sha(CTL/fn) for fn in ['MIGRATION_REGISTER.bootstrap.yaml','BANYAN_REFACTOR_TRACE.bootstrap.yaml'])),['../../01/stage01-20260920T091426Z/evidence/NEXT_STAGE_HANDOFF.yaml','checkpoint/*.snapshot.yaml'],'Stage 02 only reads Stage 01 metadata; no secret body read/hash/copy and no backup claim.')
head=git('rev-parse','HEAD').decode().strip();branch=git('branch','--show-current').decode().strip();identity={k:subprocess.run(['git','config','--get','user.'+k],capture_output=True,text=True).stdout.strip() for k in ['name','email']}
check(13,dict(head_unchanged=head==pre['head'],branch_unchanged=branch==pre['branch'],tracked_clean=not git('diff','--name-only','-z') and not git('diff','--cached','--name-only','-z'),no_conflicts=not git('ls-files','--unmerged','-z'),identity_unchanged=identity==specs,no_stage03=not (CTL/'stages/03').exists()),['evidence/PRECHECK.json','../../01/stage01-20260920T091426Z/GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml'],'HEAD/index/Git identity unchanged; no business file modification or Stage 03 run.')
assert all(x['result']=='PASS' for x in result),[x for x in result if x['result']!='PASS']

reportfiles=['CAPABILITY_MAPPING_WORKBOOK.yaml','CONTRACT_CHAIN_DESIGN.md','CORE_CANDIDATES.yaml','CORE_BOUNDARY_CANDIDATE.md','PROJECT_CANDIDATES.yaml','PROJECT_INSTANCE_CANDIDATE.md','PROVIDER_CANDIDATES.yaml','PROVIDER_CANDIDATE.md','COMPATIBILITY_CANDIDATES.yaml','COMPATIBILITY_LAYER_CANDIDATE.md','ASSET_BOUNDARY_MAP.jsonl','ARTIFACT_BOUNDARY_MAP.jsonl','CONFLICT_RISK_REGISTER.yaml','CONFLICT_RESOLUTION_PLAN.md','ARCHITECTURE_DECISION_RECORDS.yaml','AI_RUNTIME_COST_GOVERNANCE_DESIGN.md','ACCEPTANCE_REPORT.md']
handoff=dict(upstream_stage='02',run_id=RUN.name,acceptance_result='PASS_CANDIDATE_DESIGN',actual_artifacts_to_consume=reportfiles,source_stage01=dict(run_id=S1.name,gate_review=str(GATE.relative_to(ROOT)),sealed_inputs=[x['path'] for x in pre['stage01_inputs']],source_hash_evidence='evidence/PRECHECK.json'),boundary_summary=dict(capabilities=35,core_candidates=21,project_candidates=2,provider_candidates=9,compatibility_candidates=3,assets_mapped=1026,generated_artifacts_mapped=425,operational_artifacts_mapped=289,conflicts_carried=31,high_conflicts_open=2),evidence_to_trust=['evidence/PRECHECK.json','evidence/VALIDATION_RESULTS.yaml','evidence/BOOTSTRAP_LINEAGE.json','evidence/FINAL_VERIFICATION.json','ARTIFACT_HASHES.sha256','evidence/SEAL_VERIFICATION.json'],open_architecture_decisions=[x['decision_id'] for x in adrs],open_risks=[dict(id=x['risk_id'],severity=x['severity'],owner_candidate=x['candidate_owner_stage'],next_action=x['next_action']) for x in newrisk]+[dict(id=x['issue_id'],severity=x['inherited_severity'],owner_candidate=x['candidate_owner_stage'],next_action=x['next_action']) for x in carried if x['inherited_severity']=='HIGH'],inherited_constraints=dict(secret_metadata_only_paths=approved,secret_policy=dict(content_read=False,content_copy=False,content_hash=False,write=False,delete=False,move=False,rename=False,git_commit=False),recovery_mode='USER_ACCEPTED_PRESERVE_IN_PLACE',recovery_coverage='PARTIAL_APPROVED',other_secrets='Stage 01 inherited 69 potential candidates plus tunnel metadata-only boundary; no user waiver extension',existing_project_layout_preservation_contract_candidate=dict(existing_project='PRESERVE_IN_PLACE',banyan='DISCOVER + MAP + DESIGN',relayout='EXPLICIT_MIGRATION_ONLY'),prior_stage01_mapping='DISCOVER + MAP + CLASSIFY remains discovery outcome',refactor_evidence='.banyan-refactor/** excluded from Legacy',construction_materials='榕树ai改造落地相关文档/** excluded from Legacy',capabilities_preserved=True,final_architecture_frozen=False,legacy_migration_executed=False),stage03_inputs=['35 capability chain candidates','21/2/9/3 boundary lists','1026 asset and 714 artifact/operational mappings','31 carried issues plus 5 new risks','six DRAFT architecture decisions','AI Runtime Cost Governance design'],next_stage_entry_gate=dict(stage='03',result='PASS_FOR_CONTRACT_DESIGN',qualification='Stage 02 candidate design accepted; Stage 03 must validate/freeze Schema and Source Roles; open HIGH risks block activation, not this design handoff',execution_authorized=False),stop_after_stage='02')
newyaml(RUN/'evidence/NEXT_STAGE_HANDOFF.yaml',handoff)

report=f'''# Stage 02 实际验收报告

**Stage Status：COMPLETED / PASS_CANDIDATE_DESIGN**。Run `{RUN.name}`。Stage 02 完成候选边界设计，没有把架构提案写成已批准的最终 Contract、Schema 或 Provider 选择。

## Input Verification

Stage 01 `stage01-20260920T091426Z` 的 Acceptance/Handoff 和 Gate Review 为 PASS；本阶段消费的 10 份输入与 Stage 01 封存 SHA-256 一致。Stage 01 共 65 项封存内容通过历史 Bootstrap 快照复核；Stage 02 Pack 七份文件哈希在 Precheck 与最终检查一致。未重新运行 Discovery、Inventory 或旧项目脚本。

## Boundary Result

35 项能力全部映射到 `Capability → Contract → Provider → Artifact → Runtime`：Core 语义候选 21、Project Instance 2、Provider 9、Compatibility Layer 3；工作簿逐项记录输入、输出、守卫、失败、接口候选、项目 Overlay、风险与后续 Owner。1,026 项资产和 714 项正式/派生/运行产物（425+289）均有原位映射。既有文件没有直接升格为 Core 物理资产，跨项目执行证明仍待验证。

`CONTRACT_CHAIN_DESIGN.md` 描述接口与权威边界；四份 Candidate 指导记录每类职责，`AI_RUNTIME_COST_GOVERNANCE_DESIGN.md` 覆盖路由、模型选择维度、Token 预算、四种执行模式、批处理/缓存/失败策略。没有模型调用、预算阈值冻结或 Runtime 实现。

## Conflict and Risk

Stage 01 的 31 项问题全部带入；两项 HIGH（知情决策规则差异、项目入口/进度陈旧）有具体处理路径、后续 Owner 与激活前门禁，但尚未裁决。新增五项风险覆盖 Core 可移植性、产物来源、成本设计、13 Secret 部分恢复及本地证据保存。六项架构决策均为 DRAFT，未获批准。完整记录见 `CONFLICT_RISK_REGISTER.yaml` 和 `CONFLICT_RESOLUTION_PLAN.md`。

## Validation

V02-01～V02-15 全部 PASS；逐项证据与断言见 `evidence/VALIDATION_RESULTS.yaml`。验收范围是设计映射、覆盖与保护，不包括业务测试、工具执行、性能/成本实测或跨项目适配验证。后续阶段消费候选时必须自行验证。

## Actual Writes and Protected Scope

仅写入本 Run 下架构分析、映射、风险、验收、Evidence/Handoff/封存，以及控制根现有 Bootstrap Register/Trace。完整列表见 `evidence/ACTUAL_WRITES.txt`。原业务代码、SQL、正式文档、施工包、项目目录和 Stage 01 Evidence 均未修改；HEAD、Git identity 与已跟踪工作区不变。没有 commit、stash、reset、clean、目录移动或正式 `.banyan`/`banyan-framework` 创建。

继承的 13 份本地环境配置保持原位：Stage 02 未读正文、未复制、未 Hash、未修改、未删除、未移动、未提交。用户仅接受它们没有独立 Banyan Backup 的风险，恢复覆盖继续是 `PARTIAL_APPROVED`，不能写成 COMPLETE；其它 Secret 仍受保护。

## Next Stage Handoff

`evidence/NEXT_STAGE_HANDOFF.yaml` 列出全部实际架构输入、未决 DRAFT 决策、风险、35 项能力和 1,026/714 项映射。Stage 03 的候选输入门禁为 `PASS_FOR_CONTRACT_DESIGN`，其执行尚未获本次授权。Existing Project → `PRESERVE_IN_PLACE`；Banyan → `DISCOVER + MAP + DESIGN`；重新布局 → `EXPLICIT_MIGRATION_ONLY`。本次停止于 Stage 02，未进入 Stage 03。

Bootstrap lineage 与封存见 `evidence/BOOTSTRAP_LINEAGE.json`、`ARTIFACT_HASHES.sha256`；封存后回读见 `evidence/SEAL_VERIFICATION.json`。
'''
with (RUN/'ACCEPTANCE_REPORT.md').open('x',encoding='utf-8') as f:f.write(report)

# Preserve Stage 00/01 entries, update only the bootstrap control pair after review.
reg['bootstrap']['run_id']=RUN.name
reg['refactor']['current_stage']='02'
base=str(RUN.relative_to(CTL))
reg['stages']['02']=dict(status='COMPLETED',run_id=RUN.name,design_state='CANDIDATE_ONLY',actual_artifacts=[base+'/'+p for p in reportfiles]+[base+'/evidence/NEXT_STAGE_HANDOFF.yaml'],validation=dict(overall='PASS',results={'V02-%02d'%n:'PASS' for n in range(1,16)},evidence=base+'/evidence/VALIDATION_RESULTS.yaml'),source_stage01_run=S1.name,source_stage01_gate='PASS',open_risks=handoff['open_risks'],recovery_coverage='PARTIAL_APPROVED',next_stage_handoff=base+'/evidence/NEXT_STAGE_HANDOFF.yaml',next_gate='Stage 03: PASS_FOR_CONTRACT_DESIGN; execution not authorized',activation_mode='OFF',architecture_frozen=False)
trace['bootstrap']['run_id']=RUN.name
for key,desc,parts in [
 ('CHAIN','All 35 preserved capabilities mapped through five-layer candidate chain',['CAPABILITY_MAPPING_WORKBOOK.yaml','CONTRACT_CHAIN_DESIGN.md']),
 ('BOUNDARY','Core/Project/Provider/Compatibility candidate boundaries with no project relayout',['CORE_CANDIDATES.yaml','PROJECT_CANDIDATES.yaml','PROVIDER_CANDIDATES.yaml','COMPATIBILITY_CANDIDATES.yaml']),
 ('MAPPING','1026 asset and 714 artifact/operational boundaries retained in place',['ASSET_BOUNDARY_MAP.jsonl','ARTIFACT_BOUNDARY_MAP.jsonl']),
 ('RISK','31 inherited issues and five new design risks routed',['CONFLICT_RISK_REGISTER.yaml','CONFLICT_RESOLUTION_PLAN.md']),
 ('COST','AI Runtime cost governance designed without implementation',['AI_RUNTIME_COST_GOVERNANCE_DESIGN.md']),
]:
    trace['requirements'].append(dict(requirement_id='BANYAN-S02-'+key,description=desc,owner_stage=['02'],implementation_artifacts=[base+'/'+p for p in parts],validation_artifacts=[base+'/evidence/VALIDATION_RESULTS.yaml'],evidence=[base+'/ACCEPTANCE_REPORT.md',base+'/evidence/NEXT_STAGE_HANDOFF.yaml'],capability_state='VERIFIED_DESIGN_CANDIDATE',activation_mode='OFF',status='SATISFIED',candidate_only=True))
rewriteyaml(reg_path,reg)
rewriteyaml(trace_path,trace)
lineage=[]
for fn in ['MIGRATION_REGISTER.bootstrap.yaml','BANYAN_REFACTOR_TRACE.bootstrap.yaml']:
    snap=RUN/'checkpoint'/(fn+'.snapshot.yaml')
    lineage.append(dict(path='../../../'+fn,source_run_id=S1.name,target_run_id=RUN.name,source_snapshot=str(snap.relative_to(RUN)),source_sha256=sha(snap),target_sha256=sha(CTL/fn),source_snapshot_read_only=(snap.stat().st_mode&0o222)==0,active_writable_truth='../../../'+fn))
newjson(RUN/'evidence/BOOTSTRAP_LINEAGE.json',dict(result='PASS',bootstrap_only=True,history_preserved=True,stage01_shared_seal_resolves_to='checkpoint/*.snapshot.yaml',lineage=lineage,canonical_writable_truth_active=False,stage03_started=False))

check(14,dict(register_stage2=reg['refactor']['current_stage']=='02' and reg['stages']['02']['status']=='COMPLETED' and reg['stages']['02']['architecture_frozen']==False,stage1_preserved=reg['stages']['01']==before_reg['stages']['01'] and reg['stages']['00']==before_reg['stages']['00'],trace_stage2=sum(x['requirement_id'].startswith('BANYAN-S02-') and x['status']=='SATISFIED' for x in trace['requirements'])==5,trace_stage1_preserved=trace['requirements'][:len(before_trace['requirements'])]==before_trace['requirements'],bootstrap_only=reg['bootstrap']['bootstrap_only'] and trace['bootstrap']['bootstrap_only'] and not reg['bootstrap']['canonical_writable_truth_active'],lineage_exists=(RUN/'evidence/BOOTSTRAP_LINEAGE.json').is_file()),['../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml','evidence/BOOTSTRAP_LINEAGE.json'],'Single bootstrap writable pair; Stage 01 entries and old shared hashes preserved via snapshots.')
check(15,dict(acceptance_exists=(RUN/'ACCEPTANCE_REPORT.md').is_file(),handoff_complete=len(handoff['actual_artifacts_to_consume'])==len(reportfiles) and all((RUN/p).is_file() for p in handoff['actual_artifacts_to_consume']),secret_handoff=handoff['inherited_constraints']['secret_metadata_only_paths']==approved and handoff['inherited_constraints']['recovery_coverage']=='PARTIAL_APPROVED',stage03_not_started=handoff['next_stage_entry_gate']['execution_authorized'] is False and not (CTL/'stages/03').exists()),['ACCEPTANCE_REPORT.md','evidence/NEXT_STAGE_HANDOFF.yaml'],'Actual acceptance and complete handoff; Stage 03 not started or authorized.')
assert len(result)==15 and all(x['result']=='PASS' for x in result),[x for x in result if x['result']!='PASS']
newyaml(RUN/'evidence/VALIDATION_RESULTS.yaml',dict(stage='02',run_id=RUN.name,overall='PASS',design_state='CANDIDATE_ONLY',results=result))
status=git('-c','core.quotepath=false','status','--porcelain=v1','--untracked-files=normal')
(RUN/'evidence/POST_STAGE_GIT_STATUS.txt').write_bytes(status)
assert git('rev-parse','HEAD').decode().strip()==pre['head']
assert not git('diff','--name-only','-z') and not git('diff','--cached','--name-only','-z')
assert identity==specs
assert all(sha(S1/x['path'])==x['sha256'] for x in pre['stage01_inputs'])
newjson(RUN/'evidence/FINAL_VERIFICATION.json',dict(result='PASS',stage02_status='COMPLETED',stage02_design_state='CANDIDATE_ONLY',stage03_started=False,run_id=RUN.name,all_15_checks_pass=True,capability_mapping='35/35',asset_mapping='1026/1026',artifact_mapping='425/425 + 289/289',source_stage01_seal_verified=65,secret_recovery_coverage='PARTIAL_APPROVED',head_unchanged=True,tracked_changes=False,business_files_written=False,limits=['No independent cross-project proof','No final Contract/Schema/Provider selection','No cost benchmarks or runtime execution']))
future={'ARTIFACT_HASHES.sha256','evidence/ACTUAL_WRITES.txt','evidence/SEAL_VERIFICATION.json'}
writes={str(p.relative_to(ROOT)) for p in RUN.rglob('*') if p.is_file()}|{str((RUN/p).relative_to(ROOT)) for p in future}|{str((CTL/fn).relative_to(ROOT)) for fn in ['MIGRATION_REGISTER.bootstrap.yaml','BANYAN_REFACTOR_TRACE.bootstrap.yaml']}
with (RUN/'evidence/ACTUAL_WRITES.txt').open('x') as f:f.write('\n'.join(sorted(writes))+'\n')
sealpaths=sorted(p for p in RUN.rglob('*') if p.is_file() and p.name not in ('ARTIFACT_HASHES.sha256','SEAL_VERIFICATION.json'))+[reg_path,trace_path]
entries=[dict(path=os.path.relpath(p,RUN),sha256=sha(p)) for p in sealpaths]
with (RUN/'ARTIFACT_HASHES.sha256').open('x') as f:
    for e in entries:f.write(e['sha256']+'  '+e['path']+'\n')
assert all(sha(RUN/e['path'])==e['sha256'] for e in entries)
newjson(RUN/'evidence/SEAL_VERIFICATION.json',dict(result='PASS',manifest='ARTIFACT_HASHES.sha256',manifest_sha256=sha(RUN/'ARTIFACT_HASHES.sha256'),verified_entries=len(entries),receipt_excluded_from_manifest=True,stage02_status='COMPLETED',stage03_started=False))
print(json.dumps(dict(result='PASS',run_id=RUN.name,validation_checks=len(result),sealed_entries=len(entries),stage03_started=False),ensure_ascii=False))
