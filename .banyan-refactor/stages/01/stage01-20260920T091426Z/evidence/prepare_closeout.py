import collections,datetime,hashlib,json,os,subprocess
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1];ROOT=R.parents[3];B=ROOT/'.banyan-refactor';UP=B/'stages/00/stage00-precheck-20260920T083254Z';os.chdir(ROOT)
def load(n):return [json.loads(l) for l in (R/n).open()]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(n,v,k='yaml'):
    with (R/n).open('x',encoding='utf-8') as f:
        if k=='json':json.dump(v,f,ensure_ascii=False,indent=2)
        else:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
def git(*a):return subprocess.check_output(['git',*a],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'})
A=load('AI_ASSET_INVENTORY.jsonl');G=load('AI_GENERATED_ARTIFACT_INVENTORY.jsonl');C=load('LEGACY_AI_CAPABILITY_INVENTORY.jsonl');O=load('OPERATIONAL_ARTIFACT_INVENTORY.jsonl');gm={g['path']:g for g in G};prior=h(R/'AI_ASSET_INVENTORY.jsonl')
for a in A:
    if a['path'] in gm and gm[a['path']]['artifact_class']=='DERIVED':a['authority']['canonicality']='DERIVED'
    if a['path'] in gm:a['notes'].append('Artifact source/consumer/provenance qualification is in AI_GENERATED_ARTIFACT_INVENTORY.jsonl; no authorship inferred.')
with (R/'AI_ASSET_INVENTORY.jsonl').open('w') as f:
    for a in A:f.write(json.dumps(a,ensure_ascii=False)+'\n')
put('evidence/FINAL_ROLE_ALIGNMENT.json',dict(prior_inventory_sha256=prior,final_inventory_sha256=h(R/'AI_ASSET_INVENTORY.jsonl'),reason='Align derived publication/design/compiled-contract roles across inventories; no source files modified'),'json')

old={x['path']:x for x in map(json.loads,(UP/'evidence/FILE_INVENTORY.jsonl').open())};errors=[];hashed=[];meta=[]
extra={'nunu-go-api/scripts/ssh-tunnel-test.ps1'}
for p,x in old.items():
    q=ROOT/p
    if 'SECRET' in x['protection_class'] or p in extra:
        s=q.lstat();meta.append(dict(path=p,size=s.st_size,mtime_ns=s.st_mtime_ns,mode=s.st_mode&0o777,inode=s.st_ino,content_read=False,content_hash=False,content_copy=False))
        if (s.st_size,s.st_mtime_ns,s.st_ino)!=(x['size'],x['mtime_ns'],x['inode']):errors.append('metadata drift: '+p)
    elif x.get('sha256'):
        if h(q)!=x['sha256']:errors.append('hash drift: '+p)
        hashed.append(p)
path_drift={}
for f,args in [('tracked.z',('ls-files','-z')),('untracked.z',('ls-files','--others','--exclude-standard','-z')),('ignored.z',('ls-files','--others','--ignored','--exclude-standard','-z'))]:
    before=set((R/'evidence'/f).read_bytes().split(b'\0'));after=set(git(*args).split(b'\0'));out=lambda s:sorted(x.decode() for x in s if x and not x.startswith(b'.banyan-refactor/'))
    path_drift[f]=dict(added=out(after-before),removed=out(before-after))
    if path_drift[f]['added'] or path_drift[f]['removed']:errors.append('path drift: '+f)
head=git('rev-parse','HEAD').decode().strip();index_same=git('ls-files','--stage','-z')==(R/'evidence/index.z').read_bytes()
current=yaml.safe_load((R/'GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml').read_text())['current_effective_identity']
identity_same=all(subprocess.run(['git','config','--get','user.'+k],capture_output=True,text=True).stdout.strip()==current['config_identity'][k] for k in ['name','email'])
prior_evidence=json.loads((R/'evidence/RESUME_PRECHECK.json').read_text())['existing_evidence_hashes']
unchanged_resume={p:h(R/p)==hv for p,hv in prior_evidence.items()}
upcheck=json.loads((R/'evidence/UPSTREAM_INTEGRITY.json').read_text());upresults=[]
for e in upcheck['entries']:
    p=UP/e['path'];actual=h(p);upresults.append(dict(path=e['path'],matches=actual==e['sha256']))
assert not errors and index_same and identity_same and all(unchanged_resume.values()) and all(x['matches'] for x in upresults)
assert not any(Path(p).exists() for p in ['.banyan','banyan-framework','project-sources'])
status=git('-c','core.quotepath=false','status','--porcelain=v1','--untracked-files=all')
(R/'evidence/POST_STAGE_GIT_STATUS.txt').write_bytes(status)
put('evidence/FINAL_SAFETY_CHECK.json',dict(result='PASS',head=head,index_unchanged=index_same,git_identity_unchanged=identity_same,managed_hashes_verified=len(hashed),managed_hash_paths=hashed,metadata_only_paths=meta,secret_policy='69 inherited candidates + additional tunnel script; 13 approved local config paths still protected',tunnel_qualification='Stage 01 initial inherited baseline hash freshness check included tunnel script before more-conservative metadata-only discovery designation; no body content emitted or copied. It was not one of the inherited 69 secret candidates.',outside_control_path_drift=path_drift,original_resume_evidence_unchanged=unchanged_resume,stage00_seal_before_bootstrap_update=upresults,tracked_diff_empty=not git('diff','--name-only') and not git('diff','--cached','--name-only'),forbidden_target_layouts_absent=True,errors=errors,limits='Secret content equality not asserted; lstat and no write operations only. Dependencies/build/ignored exclusions not body-hash verified.'),'json')
oldreg=yaml.safe_load((B/'MIGRATION_REGISTER.bootstrap.yaml').read_text());oldtrace=yaml.safe_load((B/'BANYAN_REFACTOR_TRACE.bootstrap.yaml').read_text());approved=oldreg['stages']['00']['open_risks'][0]['scope']
put('CHECKPOINT_RECORD.yaml',dict(stage_id='01',run_id=R.name,kind='CONTROL_ARTIFACT_CHECKPOINT_AND_UPSTREAM_REFERENCE',upstream_checkpoint='../../00/stage00-precheck-20260920T083254Z/CHECKPOINT_RECORD.yaml',recovery={'coverage':'PARTIAL_APPROVED','mode':'USER_ACCEPTED_PRESERVE_IN_PLACE'},secret_scope=approved,secret_policy=dict(classification='SECRET_METADATA_ONLY',preserve_in_place=True,writable=False,deletable=False,content_read_allowed=False,content_hash_allowed=False,content_copy_allowed=False,checkpoint_content_copy_allowed=False,git_commit_allowed=False),explicit_attestation=['13 local config bodies not read','13 local config bodies not copied','13 local config bodies not hashed','13 local config files not modified/deleted/moved/renamed','User accepted no independent Banyan Backup for these 13 only','Subsequent stages inherit metadata-only/no-write protection'],bootstrap_snapshots=[dict(path='checkpoint/'+f+'.snapshot.yaml',sha256=h(R/'checkpoint'/(f+'.snapshot.yaml')),historical_read_only=True,writable_truth=False) for f in ['MIGRATION_REGISTER.bootstrap.yaml','BANYAN_REFACTOR_TRACE.bootstrap.yaml']],rollback='Retain evidence. Do not restore business files automatically. Shared bootstrap rollback requires comparing later work and explicit scoped action; snapshot is historical evidence, not a second writable truth.'))
artifacts=['AI_ASSET_INVENTORY.jsonl','LEGACY_CLASSIFICATION_REPORT.yaml','CORE_CANDIDATE_REPORT.yaml','CONFLICT_GAP_REPORT.yaml','LEGACY_AI_CAPABILITY_INVENTORY.jsonl','AI_GENERATED_ARTIFACT_INVENTORY.jsonl','OPERATIONAL_ARTIFACT_INVENTORY.jsonl','DISCOVERY_COVERAGE_REPORT.yaml','PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml','PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml','GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml','CHECKPOINT_RECORD.yaml','ACCEPTANCE_REPORT.md']
risks=[dict(id='R00-SECRET-001',status='USER_ACCEPTED',recovery_coverage='PARTIAL_APPROVED',scope=approved,description='No independent backup of these 13 secret bodies; preserved only in current local environment'),dict(id='R01-PROVENANCE',status='ROUTED',owner_candidate='03/09/10',description='Individual AI authorship, exact generation lineage and byte reproducibility not established; no delete/regenerate authorization'),dict(id='R01-PRECEDENCE',status='ROUTED',owner_candidate='02/05/07/12',description='CON-001/002 require future architecture/freshness/override handling before compatibility activation; Stage 01 does not select winner'),dict(id='R01-LOCAL-EVIDENCE',status='OPEN',description='Control artifacts remain uncommitted local evidence, not independent off-machine backup')]
handoff=dict(upstream_stage='01',run_id=R.name,acceptance_result='PENDING_FINAL_VALIDATION',actual_artifacts_to_consume=artifacts,evidence_to_trust=['evidence/RESUME_PRECHECK.json','evidence/DISCOVERY_UNIVERSE.jsonl','evidence/CONTENT_FEATURES.jsonl','evidence/CANDIDATE_RECONCILIATION.jsonl','evidence/REFERENCE_EDGES.jsonl','evidence/REFERENCE_TOKEN_SCAN.jsonl','evidence/GIT_COMMIT_METADATA.jsonl','evidence/GIT_TRAILER_PARSE.json','evidence/FINAL_SAFETY_CHECK.json','evidence/VALIDATION_RESULTS.yaml','evidence/BOOTSTRAP_LINEAGE.json','ARTIFACT_HASHES.sha256'],unresolved_risks=risks,open_architecture_questions=[dict(capability_id=c['capability_id'],question=c['open_question'],candidate_owner_stage=c['candidate_owner_stage']) for c in C],candidate_boundaries=yaml.safe_load((R/'CORE_CANDIDATE_REPORT.yaml').read_text())['summary'],inherited_constraints=dict(secret_metadata_only_paths=approved,all_other_secret_candidates='Inherit Stage 00 69 candidates plus Stage 01 conservative tunnel boundary; user exception never extends',secret_policy=dict(content_read=False,content_copy=False,content_hash=False,write=False,delete=False,move=False,rename=False,git_commit=False),recovery_mode='USER_ACCEPTED_PRESERVE_IN_PLACE',recovery_coverage='PARTIAL_APPROVED',refactor_operational_evidence='.banyan-refactor/** and .banyan-refactor.zip excluded from Legacy',construction_materials='榕树ai改造落地相关文档/** excluded from Legacy',existing_project_layout_preservation_candidate=dict(existing_project='PRESERVE_IN_PLACE',banyan='DISCOVER + MAP + CLASSIFY',relayout='EXPLICIT_MIGRATION_ONLY'),final_contracts_frozen=False),bootstrap_lineage=dict(active_register='../../../MIGRATION_REGISTER.bootstrap.yaml',active_trace='../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml',stage00_shared_hashes_resolve_to='checkpoint/*.snapshot.yaml; immutable historical copies',evidence='evidence/BOOTSTRAP_LINEAGE.json',future_canonical_migration='source hash/run → target hash → validation → bootstrap read-only archive; no dual writable truth'),next_stage_entry_gate=dict(stage='02',result='PENDING_FINAL_VALIDATION',reason='Requires all 18 checks PASS, coverage/no-loss and final seal',execution_authorized=False),stop_after_stage='01')
put('evidence/NEXT_STAGE_HANDOFF.yaml',handoff)
base=str(R.relative_to(B));oldreg['bootstrap']['run_id']=R.name;oldreg['refactor']['current_stage']='01'
oldreg['stages']['01']=dict(status='VALIDATING',run_id=R.name,resume_case='A',resumed_from_step='01.2',actual_artifacts=[base+'/'+a for a in artifacts]+[base+'/evidence/NEXT_STAGE_HANDOFF.yaml'],validation=dict(overall='PENDING',evidence=base+'/evidence/VALIDATION_RESULTS.yaml'),open_risks=risks,recovery_coverage='PARTIAL_APPROVED',next_stage_handoff=base+'/evidence/NEXT_STAGE_HANDOFF.yaml',next_gate='Stage 02 Entry Gate; no execution authorization')
oldtrace['bootstrap']['run_id']=R.name
families=[('DISCOVERY','Full repository discovery including metadata exclusions',['AI_ASSET_INVENTORY.jsonl','DISCOVERY_COVERAGE_REPORT.yaml']),('CAPABILITY','Semantic capability preservation candidates',['LEGACY_AI_CAPABILITY_INVENTORY.jsonl','PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml']),('ARTIFACT','Canonical/derived/operational preservation candidates',['AI_GENERATED_ARTIFACT_INVENTORY.jsonl','OPERATIONAL_ARTIFACT_INVENTORY.jsonl','PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml']),('BOUNDARY','Core purity and conflict/gap candidates',['CORE_CANDIDATE_REPORT.yaml','CONFLICT_GAP_REPORT.yaml','LEGACY_CLASSIFICATION_REPORT.yaml']),('GIT','Read-only identity/commit practice',['GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml'])]
for key,desc,arts in families:oldtrace['requirements'].append(dict(requirement_id='BANYAN-S01-'+key,description=desc,owner_stage=['01'],implementation_artifacts=[base+'/'+a for a in arts],validation_artifacts=[base+'/evidence/VALIDATION_RESULTS.yaml'],evidence=[base+'/evidence/NEXT_STAGE_HANDOFF.yaml'],capability_state='VALIDATING',activation_mode='OFF',status='PENDING',candidate_only=True))
for fname,v in [('MIGRATION_REGISTER.bootstrap.yaml',oldreg),('BANYAN_REFACTOR_TRACE.bootstrap.yaml',oldtrace)]:
    with (B/fname).open('w') as f:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
put('evidence/CLOSEOUT_PREPARATION.json',dict(status='VALIDATING',counts=dict(assets=len(A),capabilities=len(C),generated=len(G),operational=len(O)),bootstrap_updated=True,stage00_run_files_untouched=True,remaining='Independent V01-01..18, then finalize acceptance/handoff/state/seal; no Stage 02'), 'json')
print('Closeout prepared; independent validation required.')
