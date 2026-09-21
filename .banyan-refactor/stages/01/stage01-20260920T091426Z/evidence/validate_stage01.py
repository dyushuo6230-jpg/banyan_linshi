"""Independent structural, coverage, provenance and safety checks; no business tests.
Usage: python evidence/validate_stage01.py [--final]
Writes a new validation result only; existing evidence is never overwritten.
"""
import hashlib,json,os,subprocess,sys
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1];ROOT=R.parents[3];B=ROOT/'.banyan-refactor';UP=B/'stages/00/stage00-precheck-20260920T083254Z';os.chdir(ROOT)
def j(n):return [json.loads(l) for l in (R/n).open()]
def y(n):return yaml.safe_load((R/n).read_text())
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'})
A=j('AI_ASSET_INVENTORY.jsonl');C=j('LEGACY_AI_CAPABILITY_INVENTORY.jsonl');G=j('AI_GENERATED_ARTIFACT_INVENTORY.jsonl');O=j('OPERATIONAL_ARTIFACT_INVENTORY.jsonl');U=j('evidence/DISCOVERY_UNIVERSE.jsonl');um={x['path']:x for x in U};cov=y('DISCOVERY_COVERAGE_REPORT.yaml');cm=y('PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml')['matrix'];gm=y('PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml');reg=y('../../../MIGRATION_REGISTER.bootstrap.yaml');trace=y('../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml');hand=y('evidence/NEXT_STAGE_HANDOFF.yaml');safety=json.loads((R/'evidence/FINAL_SAFETY_CHECK.json').read_text());results=[]
def check(n,conditions,ev,note):
    failed=[k for k,v in conditions.items() if not v];results.append(dict(id='V01-%02d'%n,result='FAIL' if failed else 'PASS',checks=conditions,failed=failed,evidence=ev,note=note))
def refs_exist(items):
    for a in items:
        for ref in a.get('evidence_refs',[]):
            if isinstance(ref,dict):
                p=ROOT/ref['path']
                if not p.is_file() or not 1<=ref['line']<=len(p.read_text().splitlines()):return False
                if ref.get('source_sha256') and h(p)!=ref['source_sha256']:return False
            elif not (R/ref.split('#')[0]).exists():return False
    return True
upok=[]
for e in json.loads((R/'evidence/UPSTREAM_INTEGRITY.json').read_text())['entries']:
    p=(R/'checkpoint'/(Path(e['path']).name+'.snapshot.yaml')) if e['path'].startswith('../../../') else UP/e['path']
    upok.append(h(p)==e['sha256'])
pk=ROOT/'榕树ai改造落地相关文档/Stage_01_AI资产全量盘点与方案裁剪'
pack=json.loads((R/'evidence/PACK_CHECK.json').read_text())
check(1,dict(upstream_seal_58=len(upok)==58 and all(upok),pack_28=len(pack['entries'])==28 and all(h(pk/e['path'])==e['sha256'] for e in pack['entries']),stage00_preserved=reg['stages']['00']==y('checkpoint/MIGRATION_REGISTER.bootstrap.yaml.snapshot.yaml')['stages']['00'],entry_gate=y('../../00/stage00-precheck-20260920T083254Z/evidence/NEXT_STAGE_HANDOFF.yaml')['stage01_entry_gate']['result']=='PASS'),['evidence/UPSTREAM_INTEGRITY.json','evidence/PACK_CHECK.json','checkpoint/*.snapshot.yaml'],'Stage 00 shared-state hashes resolve through immutable pre-update snapshots; original stage evidence stays unchanged.')
head=git('rev-parse','HEAD').decode().strip()
check(2,dict(head_matches=head==safety['head'],precheck_pass=json.loads((R/'evidence/RESUME_PRECHECK.json').read_text())['result']=='PASS',drift_explicit=(R/'evidence/EXTERNAL_ARCHIVE_DRIFT.json').exists(),freshness_classified=json.loads((R/'evidence/BASELINE_FRESHNESS.json').read_text())['classification']=='SAFE_DISCOVERY_DRIFT'),['evidence/RESUME_PRECHECK.json','evidence/BASELINE_FRESHNESS.json','evidence/EXTERNAL_ARCHIVE_DRIFT.json','evidence/FINAL_SAFETY_CHECK.json'],'Initial resume consistent; later archive duplicate disappearance separately classified, never silently called NO_DRIFT.')
ledger=j('evidence/CANDIDATE_RECONCILIATION.jsonl');expected={x['path'] for x in U if x['candidate']}|{x['path'] for x in ledger};actual={a['path'] for a in A}
check(3,dict(universe_unique=len(U)==len(um),all_reasoned=all(x.get('reason') and x.get('coverage') for x in U),candidate_complete=expected<=actual,governed_ignored_17=sum(a['origin']['tracked_state']=='IGNORED' for a in A)==17,root_evidence=(R/'evidence/ROOT_COVERAGE.json').exists(),tracked_count=cov['coverage']['tracked_considered']==len([p for p in git('ls-files','-z').split(b'\0') if p])),['DISCOVERY_COVERAGE_REPORT.yaml','evidence/DISCOVERY_UNIVERSE.jsonl','evidence/ROOT_COVERAGE.json','evidence/CANDIDATE_RECONCILIATION.jsonl'],'Root-wide path/content discovery plus history; binary/excluded scopes explicitly qualified.')
audit=json.loads((R/'evidence/CONTENT_ACCESS_AUDIT.json').read_text());approved=y('CHECKPOINT_RECORD.yaml')['secret_scope'];read=set(audit['read_paths']);secret=set(audit['secret_paths'])
check(4,dict(inherited69=len(secret)==69,approved13=len(approved)==13 and set(approved)<=secret,zero_secret_read=not read&secret,metadata_only=all(um[p]['coverage']=='COVERED_METADATA_ONLY' and um[p]['content_hash']==False for p in secret),no_secret_in_legacy=not actual&secret,partial_recovery=y('CHECKPOINT_RECORD.yaml')['recovery']['coverage']=='PARTIAL_APPROVED'),['evidence/CONTENT_ACCESS_AUDIT.json','CHECKPOINT_RECORD.yaml','evidence/FINAL_SAFETY_CHECK.json'],'Inherited secret bodies not read/hash/copied; no content-equality assertion. Added tunnel metadata-only boundary is documented separately.')
isolate=lambda p:p.startswith(('.banyan-refactor/','榕树ai改造落地相关文档/')) or p=='.banyan-refactor.zip'
check(5,dict(asset_isolation=not any(isolate(a['path']) for a in A),artifact_isolation=not any(isolate(a['path']) for a in G+O),capability_isolation=not any(isolate(p) for c in C for p in c['legacy_sources'])),['AI_ASSET_INVENTORY.jsonl','AI_GENERATED_ARTIFACT_INVENTORY.jsonl','OPERATIONAL_ARTIFACT_INVENTORY.jsonl'],'Construction and upstream refactor outputs never counted as Legacy.')
types={'ROLE','POLICY','SKILL','WORKFLOW','STATE','PROFILE','TEMPLATE','PROJECT_FACT','TOOL','ADAPTER','CHANGE_ARTIFACT','PUBLISHING_ARTIFACT','UNCLASSIFIED'}
check(6,dict(ids_unique=len({a['asset_id'] for a in A})==len(A),paths_unique=len(actual)==len(A),types_valid=all(a['asset_type'] in types for a in A),paths_locatable=all(Path(a['path']).exists() or a['origin']['historical_only'] for a in A),evidence_resolves=refs_exist(A)),['AI_ASSET_INVENTORY.jsonl','evidence/HISTORICAL_ASSETS.jsonl'],'1026 locatable current/historical assets with explicit type/action/evidence; path-level roles are candidates.')
cl=y('LEGACY_CLASSIFICATION_REPORT.yaml')
check(7,dict(classification_complete={x['asset_id'] for x in cl['items']}=={a['asset_id'] for a in A},actions_valid=all(a['classification']['action'] in ['KEEP','MERGE','SPLIT','REWRITE','REFERENCE','LEGACY','IGNORE'] for a in A),reasons_and_owners=all(x['reason'] and x['candidate_owner_stage'] and x['next_stage_plan'] for x in cl['items']),no_execution=cl['all_actions_candidates_only']),['LEGACY_CLASSIFICATION_REPORT.yaml'],'KEEP/MERGE/etc are proposed dispositions, not changes to legacy files.')
fields=['behaviors','inputs','outputs','guards','failure_semantics','candidate_owner_stage','candidate_target_capability','candidate_action','confidence','open_question','evidence_refs']
check(8,dict(semantic_capabilities=all(all(c.get(k) for k in fields) for c in C),unique_capabilities=len({c['capability_id'] for c in C})==len(C),source_evidence=refs_exist(C)),['LEGACY_AI_CAPABILITY_INVENTORY.jsonl'],'Capability units capture behavior, guards and failures, not just source file counts.')
check(9,dict(classes_valid=all(g['artifact_class'] in ['CANONICAL','DERIVED'] for g in G),source_consumer=all(g['source'] and g['consumer'] and g['rebuildability'] and g['freshness'] for g in G),authorship_qualified=all('CANDIDATE' in g['ai_authorship'] for g in G),approval_not_inferred=all(g['approval_not_inferred_from_path'] for g in G),evidence_resolves=refs_exist(G)),['AI_GENERATED_ARTIFACT_INVENTORY.jsonl','evidence/ARTIFACT_ELIGIBILITY.jsonl'],'AI-assisted output candidate corpus; exact per-file authorship/replay not proven. Canonical source role does not mean Approved.')
opset={o['path'] for o in O};ops_expected={a['path'] for a in A if a['authority']['canonicality']=='OPERATIONAL'}
check(10,dict(operational_complete=ops_expected<=opset,types_valid=all(o['operational_type'] in ['WORKLOG','HANDOVER','PROGRESS','DASHBOARD','RUNTIME_STATE','OTHER'] for o in O),owners_and_history=all(o['candidate_owner_stage'] and o['historical_value'] for o in O),evidence_resolves=refs_exist(O)),['OPERATIONAL_ARTIFACT_INVENTORY.jsonl'],'Preserves in-progress and user-stopped visual runs; no false success.')
issues=y('CONFLICT_GAP_REPORT.yaml')['issues'];high=[i for i in issues if i['severity'] in ['HIGH','CRITICAL']]
check(11,dict(high_routed=all(i['description'] and i['evidence_refs'] and i['candidate_owner_stage'] and i['recommended_next_action'] for i in high),no_unexplained_blockers=all(not i['blocking'] and i['stage01_disposition'].startswith('EXPLAINED') for i in high),all_issues_have_evidence=all(i['evidence_refs'] for i in issues)),['CONFLICT_GAP_REPORT.yaml','evidence/EXACT_DUPLICATES.json','evidence/REFERENCE_TOKEN_SCAN.jsonl'],'Two HIGH issues explicitly explained/routed; Stage 01 does not resolve authority conflicts or authorize migration.')
core=y('CORE_CANDIDATE_REPORT.yaml')
check(12,dict(all_capabilities_mapped={c['capability_id'] for c in C}=={c['capability_or_asset_id'] for c in core['candidates']},no_architecture_freeze=core['architecture_frozen']==False,purity_considered=all(c['purity_risk'] and c['required_abstraction'] and c['candidate_owner_stage']=='02' and c['open_questions'] for c in core['candidates'])),['CORE_CANDIDATE_REPORT.yaml'],'No Core acceptance or fixed Reference Project directory contract is declared.')
check(13,dict(no_capability_loss={c['capability_id'] for c in C}=={c['capability_id'] for c in cm},complete_mapping=all(all(x.get(k) for k in ['candidate_owner_stage','candidate_target_capability','candidate_action','confidence','open_question','evidence_refs']) for x in cm),execution_disabled=all(x['execution_allowed']==False for x in cm)),['PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml'],'35 high-value capability candidates mapped; no final owners frozen.')
check(14,dict(no_artifact_loss={g['artifact_id'] for g in G}=={g['artifact_id'] for g in gm['matrix']},canonical_fields=all(g['candidate_source_role'] and g['keep_or_migrate']=='KEEP_IN_PLACE + MAP + INDEX' and g['integrity_risk'] for g in G if g['artifact_class']=='CANONICAL'),op_mapping={o['artifact_id'] for o in O}=={o['artifact_id'] for o in gm['operational_mapping']},no_drop_execution=all(not x['execution_allowed'] for x in gm['matrix'])),['PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml'],'425 generated candidates plus 289 operational mappings preserve original locations and integrity risk.')
gp=y('GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml');commits=j('evidence/GIT_COMMIT_METADATA.jsonl')
check(15,dict(history_count=len(commits)==int(git('rev-list','--all','--count')),identities_exact=sum(x['commit_count'] for x in gp['identities'])==len(commits),semantic_review_recorded='semantic_review' in gp,no_policy_freeze=not gp['semantic_commit_policy_frozen'],no_alias_merge=not gp['identity_alias_merge_performed'],current_identity_unchanged=safety['git_identity_unchanged']),['GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml','evidence/GIT_COMMIT_METADATA.jsonl','evidence/GIT_TRAILER_PARSE.json'],'All 477 reachable commits analyzed; 16 exact identities remain distinct; hooks not executed; trailing blocks parsed separately.')
unknown=[a for a in A if a['asset_type']=='UNCLASSIFIED'];computed=dict(SILENTLY_IGNORED_ASSET=len(expected-actual),UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON=sum(not x.get('reason_ledger') for x in json.loads((R/'evidence/ROOT_COVERAGE.json').read_text())),HIGH_RISK_UNCLASSIFIED=sum(a.get('risk') in ['HIGH','CRITICAL'] for a in unknown))
check(16,dict(metrics_match=computed==cov['metrics'],metrics_zero=not any(computed.values()),unknowns_routed=all(a.get('risk') and a.get('candidate_owner_stage') and a.get('next_stage_plan') and a.get('reason_not_classified') for a in unknown)),['DISCOVERY_COVERAGE_REPORT.yaml','evidence/CANDIDATE_RECONCILIATION.jsonl'],'No unregistered candidate or unexplained root; ordinary reference/provenance questions retained with owner.')
hash_errors=[];metadata_errors=[]
for p in safety['managed_hash_paths']:
    if h(ROOT/p)!=next((x['sha256'] for x in [um.get(p,{})] if x.get('sha256')),None):
        # Construction paths are intentionally not hashed into the Legacy universe.
        old=next(json.loads(l) for l in (UP/'evidence/FILE_INVENTORY.jsonl').open() if json.loads(l)['path']==p)
        if h(ROOT/p)!=old['sha256']:hash_errors.append(p)
for x in safety['metadata_only_paths']:
    s=Path(x['path']).lstat()
    if (s.st_size,s.st_mtime_ns,s.st_ino)!=(x['size'],x['mtime_ns'],x['inode']):metadata_errors.append(x['path'])
pre=json.loads((R/'evidence/RESUME_PRECHECK.json').read_text())['existing_evidence_hashes']
check(17,dict(nonsecret_hashes_unchanged=not hash_errors,metadata_unchanged=not metadata_errors,original_evidence_unchanged=all(h(R/p)==hv for p,hv in pre.items()),stage00_evidence_unchanged=all(upok),head_unchanged=head==safety['head'],index_unchanged=git('ls-files','--stage','-z')==(R/'evidence/index.z').read_bytes(),no_tracked_changes=not git('diff','--name-only') and not git('diff','--cached','--name-only'),no_new_layout=not any(Path(p).exists() for p in ['.banyan','banyan-framework','project-sources'])),['evidence/FINAL_SAFETY_CHECK.json','evidence/POST_STAGE_GIT_STATUS.txt','evidence/EXTERNAL_ARCHIVE_DRIFT.json'],'Only Stage-owned outputs/shared bootstrap written by executor. Archive disappearance is external/unattributed and explicitly reported, not concealed.')
final='--final' in sys.argv
conds=dict(same_run=reg['stages']['01']['run_id']==R.name,bootstrap_only=reg['bootstrap']['bootstrap_only'] and trace['bootstrap']['bootstrap_only'],trace_added=all(any(x['requirement_id']=='BANYAN-S01-'+key for x in trace['requirements']) for key in ['DISCOVERY','CAPABILITY','ARTIFACT','BOUNDARY','GIT']),layout_contract=hand['inherited_constraints']['existing_project_layout_preservation_candidate']==dict(existing_project='PRESERVE_IN_PLACE',banyan='DISCOVER + MAP + CLASSIFY',relayout='EXPLICIT_MIGRATION_ONLY'),secret_scope=hand['inherited_constraints']['secret_metadata_only_paths']==approved,no_stage02_execution=not hand['next_stage_entry_gate']['execution_authorized'] and not (B/'stages/02').exists())
if final:conds.update(acceptance_exists=(R/'ACCEPTANCE_REPORT.md').exists(),handoff_pass=hand['acceptance_result']=='PASS' and hand['next_stage_entry_gate']['result']=='PASS',all_actual_links=all((R/p).is_file() for p in hand['actual_artifacts_to_consume']))
check(18,conds,['../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml','evidence/NEXT_STAGE_HANDOFF.yaml']+(['ACCEPTANCE_REPORT.md'] if final else []),'Preflight checks handoff structure; final mode additionally checks actual acceptance and gate. Stage 02 execution remains false.')
out=dict(stage_id='01',run_id=R.name,mode='FINAL' if final else 'PREFLIGHT',overall='PASS' if all(x['result']=='PASS' for x in results) else 'FAIL',results=results,computed_metrics=computed)
name='evidence/VALIDATION_RESULTS.yaml' if final else 'evidence/VALIDATION_PREFLIGHT.yaml'
with (R/name).open('x') as f:yaml.safe_dump(out,f,allow_unicode=True,sort_keys=False)
print(json.dumps(dict(overall=out['overall'],failed=[x for x in results if x['result']=='FAIL']),ensure_ascii=False))
sys.exit(0 if out['overall']=='PASS' else 1)
