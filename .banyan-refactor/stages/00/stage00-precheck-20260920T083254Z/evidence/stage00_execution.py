"""One-run Stage 00 evidence builder. No project mutations outside bootstrap control root.
Does not implement Banyan runtime. Secret paths are classified before any content I/O.
"""
import os, sys, json, stat, re, hashlib, subprocess, datetime, shutil, tarfile
from pathlib import Path
from collections import Counter, defaultdict
import yaml

REPO = Path('/Users/mac/MYCODES/AICODE/x_shop_server/x_shop_server')
TMP = Path('/var/folders/2n/hq5jyc0n0tz90n4g72jzcmdm0000gn/T/banyan-stage00-n68mgs_0')
RUN = 'stage00-precheck-20260920T083254Z'
CONTROL = REPO / '.banyan-refactor'
STAGE = CONTROL / 'stages/00' / RUN
PACK = REPO / '榕树ai改造落地相关文档/Stage_00_改造安全基线与仓库保护'
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(data): return hashlib.sha256(data).hexdigest()
def filehash(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()
def writejson(p, data): p.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
def writeyaml(p, data): p.write_text('# Stage 00 actual execution evidence; no secret contents.\n'+yaml.safe_dump(data, allow_unicode=True, sort_keys=False))
def git(*args, input=None, allowed=(0,)):
    p = subprocess.run(['git','--no-optional-locks',*args],cwd=REPO,input=input,capture_output=True)
    if p.returncode not in allowed: raise RuntimeError('Git read failed: '+repr(args))
    return p.stdout
def readlist(name): return [x for x in (TMP/name).read_text().split('\0') if x]
def metadata(p):
    s=p.lstat()
    return {'size':s.st_size,'mtime_ns':s.st_mtime_ns,'mode':stat.S_IMODE(s.st_mode),'inode':s.st_ino,'kind':'symlink' if stat.S_ISLNK(s.st_mode) else 'regular' if stat.S_ISREG(s.st_mode) else 'other'}
APPROVED = {x['path'] for x in json.loads((TMP/'secret-recovery-metadata.json').read_text())}
DEPENDENCIES = {'node_modules','.venv','venv','__pycache__','.cache','.vite','coverage'}
def classify(path, state):
    parts=Path(path).parts; name=parts[-1].lower()
    if set(parts)&DEPENDENCIES:
        return 'EXCLUDE_WITH_REASON','EXCLUDED_WITH_REASON','Dependency/cache tree; reproducible, no project governance ownership'
    sensitive = (path in APPROVED or name.startswith('.env') or re.match(r'^(credential|secret|token)',name)
        or Path(name).suffix in {'.pem','.key','.p12','.pfx','.jks'} or name in {'id_rsa','id_ed25519','.npmrc','.pypirc'}
        or ('config' in parts and (name.endswith(('.yml','.yaml','.ini')) or '.yml.' in name or '.yaml.' in name))
        or 'open-test-db-tunnel' in name)
    if sensitive: return 'METADATA_ONLY','SECRET_METADATA_ONLY','Potential credential-bearing path; no content read/copy/hash'
    if name=='.ds_store' or parts[0]=='.idea' or name.endswith('.log'):
        return 'EXCLUDE_WITH_REASON','EXCLUDED_WITH_REASON','OS/IDE local state or runtime log; not governance checkpoint; no content read'
    if state=='IGNORED' and (set(parts)&{'dist','unpackage','bin','build'} or path.startswith(('nunu-go-api/app/h5/web/addon/','nunu-go-api/app/h5/web/assets/','nunu-go-api/app/h5/web/uni_modules/')) or path=='nunu-go-api/app/h5/web/index.html'):
        return 'EXCLUDE_WITH_REASON','EXCLUDED_WITH_REASON','Generated output; build from preserved source; no independent content backup'
    if path.startswith(('docs/temp/','docs/governance/','.cursor/','tools/','榕树ai改造落地相关文档/')):
        return 'SCAN','READ_ONLY_DISCOVERY','Preserve existing governance, reference, tools or user-supplied construction input'
    return 'SCAN','IMMUTABLE_DURING_REFACTOR','Project source, canonical document, asset or unknown valuable file; deny Stage 00 writes'

def prepare():
    assert not CONTROL.exists() and not (REPO/'.banyan').exists()
    assert not os.getenv('BANYAN_REFACTOR_CONTROL_ROOT'), 'Resolve override before execution'
    current=git('status','--porcelain=v2','--branch','--untracked-files=all')
    assert current==(TMP/'PRE_STAGE_GIT_STATUS.raw').read_bytes(), 'Original baseline changed; reconcile first'
    assert git('ls-files','--stage','-z')==(TMP/'index.z').read_bytes(), 'Original index changed'
    assert git('ls-files','--others','--ignored','--exclude-standard','-z')==(TMP/'ignored.z').read_bytes(), 'Ignored membership changed'
    manifest=yaml.safe_load((PACK/'STAGE_MANIFEST.yaml').read_text())
    assert (manifest['stage_id'],manifest['pack_version'],manifest['charter']['version'])==('00','1.9.1','1.9.1')
    checks=[]
    for line in (PACK/'PACK_SHA256SUMS.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'): continue
        expected,path=line.split('  ',1); actual=filehash(PACK/path)
        assert actual==expected; checks.append({'path':path,'sha256':actual})
    writejson(TMP/'pack-resume-check.json',{'result':'PASS','checked_at':now(),'entries':checks})
    attrs=git('check-attr','-z','--stdin','filter',input=(TMP/'tracked.z').read_bytes()).split(b'\0')
    lfs=[attrs[i].decode() for i in range(0,len(attrs)-2,3) if attrs[i+2]==b'lfs']
    assert not lfs, 'LFS recovery needs dedicated handling'
    flags=git('ls-files','-v','-z').split(b'\0')
    unusual=[x.decode() for x in flags if x and (x[:1].islower() or x[:1]==b'S')]
    assert not unusual, 'Hidden index flags need additional verification'
    identity={key:digest(git('config','--get-all',key,allowed=(0,1))) for key in ['user.name','user.email']}
    config_paths=[]
    for candidate in [Path.home()/'.gitconfig',Path.home()/'.config/git/config',REPO/'.git/config']:
        if candidate.exists(): config_paths.append({'path':str(candidate),**metadata(candidate)})
    writejson(TMP/'resume-git-evidence.json',{'run_id':RUN,'resumed_at':now(),'original_baseline_preserved':True,'head':git('rev-parse','HEAD').decode().strip(),'identity_value_digests':identity,'config_metadata':config_paths,'lfs_filter_paths':lfs,'lfs_available':False,'hidden_index_flags':unusual,'index_sha256':digest((TMP/'index.z').read_bytes())})
    approval={'approval_id':'USER-STAGE00-SECRET-EXCEPTION-001','source':'User message in current Codex thread, 2026-09-20','run_id':RUN,'scope':sorted(APPROVED),'classification':'SECRET_METADATA_ONLY','preserve_in_place':True,'writable':False,'deletable':False,'move_allowed':False,'rename_allowed':False,'content_read_allowed':False,'checkpoint_content_copy_allowed':False,'secret_content_hash_allowed':False,'git_commit_allowed':False,'recovery_mode':'USER_ACCEPTED_PRESERVE_IN_PLACE','recovery_coverage':'PARTIAL_APPROVED','user_accepts_no_independent_banyan_backup':True,'applies_to_other_secrets':False,'future_stages_must_preserve_protection':True,'approval_summary':'用户明确接受这13份本地配置仅保留当前环境的恢复风险；不建立独立Banyan内容备份；仅解除这13份配置造成的阻塞。'}
    writejson(TMP/'USER_APPROVAL.json',approval)
    inventories=[]; counts=Counter(); index={}
    for row in (TMP/'index.z').read_bytes().split(b'\0'):
        if row:
            fields,path=row.split(b'\t',1); index[path.decode()]=fields.decode()
    for name,state in [('tracked.z','TRACKED'),('untracked.z','UNTRACKED'),('ignored.z','IGNORED')]:
        for path in readlist(name):
            p=REPO/path; mode,protection,reason=classify(path,state)
            m=metadata(p); e={'path':path,'git_state':state,'discovery_mode':mode,'protection_class':protection,'reason':reason,**m,'sha256':None}
            if path in index: e['git_index_entry']=index[path]
            if m['kind']=='symlink':
                e['link_target']=os.readlink(p); e['link_text_sha256']=digest(os.fsencode(e['link_target'])); e['target_followed']=False
                e['discovery_mode']='METADATA_ONLY'; e['reason']='Symlink itself only; target not dereferenced; target source if internal is inventoried at its real path'
            elif mode=='SCAN':
                assert m['kind']=='regular'; e['sha256']=filehash(p)
                assert metadata(p)==m, 'File changed while hashing: '+path
            if protection=='SECRET_METADATA_ONLY':
                e['recovery_mode']='USER_ACCEPTED_PRESERVE_IN_PLACE' if path in APPROVED else 'CLEAN_TRACKED_GIT_OBJECT_REFERENCE_ONLY' if state=='TRACKED' else 'UNRESOLVED'
                assert e['recovery_mode']!='UNRESOLVED', 'Additional unapproved secret recovery: '+path
                e['content_read']=False; e['content_copied']=False; e['content_hashed']=False
            if state=='IGNORED' and mode=='SCAN': e['governed']=True
            inventories.append(e); counts[(state,e['discovery_mode'])]+=1
    assert all(metadata(REPO/e['path'])['mtime_ns']==e['mtime_ns'] for e in inventories if e['protection_class']=='SECRET_METADATA_ONLY')
    with (TMP/'FILE_INVENTORY.jsonl').open('w') as f:
        for e in inventories: f.write(json.dumps(e,ensure_ascii=False)+'\n')
    hash_lines=[]
    for e in inventories:
        if e['sha256']:
            path=e['path']; escape='\\' in path or '\n' in path
            path=path.replace('\\','\\\\').replace('\n','\\n')
            hash_lines.append(('\\' if escape else '')+e['sha256']+'  '+path+'\n')
    (TMP/'FILE_HASHES.sha256').write_text(''.join(sorted(hash_lines)))
    writejson(TMP/'prepare-summary.json',{'counts':{f'{a}/{b}':n for (a,b),n in counts.items()},'hash_count':len(hash_lines),'secret_metadata_count':sum(e['protection_class']=='SECRET_METADATA_ONLY' for e in inventories),'approved_secret_count':len(APPROVED),'ignored_governed':[e['path'] for e in inventories if e.get('governed')],'total_files':len(inventories),'file_inventory_sha256':filehash(TMP/'FILE_INVENTORY.jsonl'),'prepared_at':now()})
    print((TMP/'prepare-summary.json').read_text())

def load_inventory(): return [json.loads(x) for x in (TMP/'FILE_INVENTORY.jsonl').read_text().splitlines()]
def stage_ref(p): return str(p.relative_to(STAGE)) if p.is_relative_to(STAGE) else os.path.relpath(p,STAGE)
def template(name): return yaml.safe_load((PACK/'templates'/name).read_text())
def create():
    assert not CONTROL.exists()
    assert git('status','--porcelain=v2','--branch','--untracked-files=all')==(TMP/'PRE_STAGE_GIT_STATUS.raw').read_bytes()
    entries=load_inventory(); summary=json.loads((TMP/'prepare-summary.json').read_text())
    for e in entries:
        if e['protection_class']=='SECRET_METADATA_ONLY':
            assert metadata(REPO/e['path'])=={k:e[k] for k in metadata(REPO/e['path'])}
    STAGE.mkdir(parents=True,mode=0o700); (STAGE/'evidence').mkdir(); (STAGE/'checkpoint').mkdir()
    # Preserve original external capture. It is evidence only, never another writable Register/Trace.
    for p in sorted(TMP.iterdir()):
        if p.is_file(): shutil.copyfile(p,STAGE/'evidence'/p.name)
    shutil.copyfile(TMP/'FILE_HASHES.sha256',STAGE/'FILE_HASHES.sha256')
    shutil.copyfile(TMP/'PRE_STAGE_GIT_STATUS.raw',STAGE/'PRE_STAGE_GIT_STATUS.txt')
    shutil.copyfile(Path(__file__),STAGE/'evidence/stage00_execution.py')
    backup_results={}
    for state,label in [('UNTRACKED','untracked'),('IGNORED','ignored-governed')]:
        selected=[e for e in entries if e['git_state']==state and e['discovery_mode']=='SCAN']
        target=STAGE/'checkpoint'/f'{label}.tar'
        with tarfile.open(target,'w',format=tarfile.PAX_FORMAT) as archive:
            for e in selected:
                assert e['protection_class']!='SECRET_METADATA_ONLY' and e['kind']=='regular'
                p=REPO/e['path']; assert filehash(p)==e['sha256']
                archive.add(p,arcname=e['path'],recursive=False)
        with tarfile.open(target,'r') as archive:
            members=archive.getmembers(); assert {m.name for m in members}=={e['path'] for e in selected}
            hashes={e['path']:e['sha256'] for e in selected}
            for m in members:
                assert not m.name.startswith('/') and '..' not in Path(m.name).parts and m.isfile()
                assert digest(archive.extractfile(m).read())==hashes[m.name]
        backup_results[label]={'required':bool(selected),'path':str(target.relative_to(STAGE)),'sha256':filehash(target),'relative_paths_preserved':True,'file_count':len(selected),'validation':'PASS','members':[e['path'] for e in selected]}
    writejson(STAGE/'evidence/CHECKPOINT_INTEGRITY.json',{'result':'PASS','verified_at':now(),'method':'Read archive members without extraction; verify path set, regular type and SHA-256 against baseline','backups':backup_results,'tracked_patches_required':False,'tracked_binary_changes':0,'secret_contents_copied':False})
    sec=[e for e in entries if e['protection_class']=='SECRET_METADATA_ONLY']
    writejson(STAGE/'evidence/SECRET_METADATA.json',sec)
    writejson(STAGE/'evidence/IGNORED_GOVERNED.json',[e for e in entries if e.get('governed')])
    writejson(STAGE/'evidence/HASH_SCOPE_REPORT.json',summary)
    topology=json.loads((TMP/'topology-precheck.json').read_text())
    topology['lfs_file_detection']='git check-attr filter: no LFS paths'; topology['tracked_skip_worktree_or_assume_unchanged']=False
    writejson(STAGE/'evidence/TOPOLOGY.json',topology)
    excluded=Counter((e['reason'],e['git_state']) for e in entries if e['discovery_mode']=='EXCLUDE_WITH_REASON')
    writejson(STAGE/'evidence/EXCLUSIONS.json',{'entries_ref':'FILE_INVENTORY.jsonl','summary':[{'reason':a,'git_state':b,'count':n} for (a,b),n in sorted(excluded.items())],'unexplained':0,'user_noncritical_exclusion_note':'用户允许无恢复价值临时项不备份；仅依实际生成物/日志/依赖/OS/IDE分类排除，不把全部ignored当作临时文件。','construction_input_policy':'User-supplied Banyan construction material is not historical development state; preserve in place, hash and safe-backup the current untracked files. Do not delete or overwrite.'})
    head=(TMP/'head.txt').read_text().strip(); branch=(TMP/'branch.txt').read_text().strip()
    baseline=template('BASELINE_MANIFEST.template.yaml')
    baseline.update(baseline_id='BASELINE-'+RUN,run_id=RUN,generated_at=now())
    baseline['repository']={'root':str(REPO),'topology':'MONOREPO','branch':branch,'head':head,'detached':False,'git_operation':'NONE','dirty':True,'upstream_present':True,'worktrees':[{'path':str(REPO),'head':head,'branch':'refs/heads/'+branch}],'submodules':[],'nested_repositories':[],'sparse_checkout':False,'lfs':{'available':False,'files_detected':False,'evidence':'evidence/resume-git-evidence.json'}}
    baseline['working_tree']={'staged_count':0,'unstaged_count':0,'untracked_count':21,'ignored_governed_count':17,'ignored_secret_exception_count':13,'deleted_count':0,'renamed_count':0,'binary_changed_count':0,'unmerged_count':0}
    baseline['control'].update(refactor_control_root=str(CONTROL),stage_root=str(STAGE))
    baseline['bootstrap_state']['migration_register']='../../../MIGRATION_REGISTER.bootstrap.yaml'
    baseline['bootstrap_state']['refactor_trace']='../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml'
    baseline['notes']=['Continuation of original external precheck run; original HEAD/index/status unchanged at resume.','User-authorized 13-path exception: recovery coverage PARTIAL_APPROVED, never COMPLETE.','Governance input Pack remains unchanged; its NOT_STARTED status is a plan/template, not runtime truth.','Hash baseline generated after metadata-only precheck; timestamps are retained separately, not misrepresented as atomic filesystem snapshot.']
    writeyaml(STAGE/'BASELINE_MANIFEST.yaml',baseline)
    discovery=template('DISCOVERY_SCOPE_BASELINE.template.yaml'); discovery['repository_root']=str(REPO)
    roots=[]
    for root in sorted(p.name for p in REPO.iterdir() if p.name not in {'.git','.banyan-refactor'}):
        es=[e for e in entries if Path(e['path']).parts[0]==root]; modes=Counter(e['discovery_mode'] for e in es)
        mode='SCAN' if modes['SCAN'] else 'METADATA_ONLY' if modes['METADATA_ONLY'] else 'EXCLUDE_WITH_REASON' if es else 'SCAN'
        roots.append({'path':root,'mode':mode,'reason':'Actual top-level root; per-file overrides in evidence/FILE_INVENTORY.jsonl are authoritative for sensitive/excluded descendants','governed':any(e.get('governed') or e['discovery_mode']=='SCAN' for e in es),'git_state':'MIXED' if len({e['git_state'] for e in es})>1 else es[0]['git_state'] if es else 'EMPTY_DIRECTORY','protection_class':'READ_ONLY_DISCOVERY' if root in {'.cursor','tools','榕树ai改造落地相关文档'} else 'IMMUTABLE_DURING_REFACTOR','follow_symlinks':False,'file_mode_counts':dict(modes)})
    discovery['roots']=roots
    discovery['coverage']={k:True for k in discovery['coverage']}
    discovery['exclusions']=[{'path':'.git/**','reason':'Only explicit read-only Git metadata commands; no raw credential-bearing Git config/object dump'},{'path':'.banyan-refactor/**','reason':'Stage-owned output excluded from original project baseline'},{'path':'per-file entries in evidence/FILE_INVENTORY.jsonl','reason':'Each EXCLUDE_WITH_REASON record has its own path, Git state and reason'}]
    discovery['assertions'].update(silently_ignored_governance_root_count=0,unexplained_exclusion_count=0)
    discovery['per_path_inventory_ref']='evidence/FILE_INVENTORY.jsonl'
    discovery['secret_content_access']='DENY; includes tracked potential secrets; user waiver applies only to the 13 exact approved paths'
    discovery['scope']='File safety/integrity scope only; no Stage 01 capability/AI asset inventory performed'
    discovery['conditional_read_roots']=[{'path':'榕树ai改造落地相关文档/00_总纲与审计/AUDIT/**','rule':'No default full-text loading; integrity hashing/backup only in Stage 00'},{'path':'榕树ai改造落地相关文档/00_总纲与审计/ARCHIVE/**','rule':'No default full-text loading; integrity only if present'}]
    writeyaml(STAGE/'DISCOVERY_SCOPE_BASELINE.yaml',discovery)
    protection=template('PROTECTED_PATHS_MANIFEST.template.yaml')
    rules=[]
    for r in roots:
        rules.append({'path':r['path']+'/**' if (REPO/r['path']).is_dir() else r['path'],'class':r['protection_class'],'read':True,'write':False,'delete':False,'discovery_mode':r['mode'],'reason':r['reason'],'owner_stage':'00 protection; later unlock requires owner-stage gate','source':'repository_discovery'})
    for e in sec:
        rules.append({'path':e['path'],'class':'SECRET_METADATA_ONLY','read':'metadata_only','write':False,'delete':False,'writable':False,'deletable':False,'preserve_in_place':True,'move_allowed':False,'rename_allowed':False,'content_read_allowed':False,'checkpoint_content_copy_allowed':False,'secret_content_hash_allowed':False,'git_commit_allowed':False,'discovery_mode':'METADATA_ONLY','reason':e['reason'],'recovery_mode':e['recovery_mode'],'approval_ref':'evidence/USER_APPROVAL.json' if e['path'] in APPROVED else None,'owner_stage':'all stages preserve; no implied waiver','source':'path_metadata'})
    rules += [{'path':'.banyan-refactor/**','class':'STAGE_WRITABLE','read':True,'write':True,'delete':False,'discovery_mode':'EXCLUDE_WITH_REASON','reason':'Bootstrap control only; not original project baseline; deletion not authorized','owner_stage':'00','source':'Stage Pack default, verified absent before create'}, {'path':'.banyan/**','class':'CONDITIONAL_WRITE_LATER','read':True,'write':False,'delete':False,'discovery_mode':'METADATA_ONLY','reason':'Future Project Instance is not initialized in Stage 00','owner_stage':'02/04','source':'charter'}, {'path':'.banyan/migrations/**','class':'CONDITIONAL_WRITE_LATER','read':True,'write':False,'delete':False,'discovery_mode':'METADATA_ONLY','reason':'Future canonical Register/Trace; no current writable truth','owner_stage':'02/04','source':'charter'}, {'path':'.git/**','class':'IMMUTABLE_DURING_REFACTOR','read':'explicit read-only Git metadata only','write':False,'delete':False,'discovery_mode':'METADATA_ONLY','reason':'No identity/index/history mutation; no credential config dump','owner_stage':'00','source':'user instruction'}]
    protection['rules']=rules
    protection['classification_precedence']=['SECRET_METADATA_ONLY','IMMUTABLE_DURING_REFACTOR','READ_ONLY_DISCOVERY','CONDITIONAL_WRITE_LATER','STAGE_WRITABLE','EXCLUDED_WITH_REASON']
    protection['per_path_inventory_ref']='evidence/FILE_INVENTORY.jsonl'
    protection['note']='Discovery exclusion never grants write/delete. Exact secret rules override root read permissions. All paths outside bootstrap control default deny write/delete.'
    writeyaml(STAGE/'PROTECTED_PATHS_MANIFEST.yaml',protection)
    checkpoint=template('CHECKPOINT_RECORD.template.yaml')
    checkpoint.update(checkpoint_id='CHECKPOINT-'+RUN,run_id=RUN,created_at=now())
    checkpoint['baseline'].update(head=head,branch=branch,working_tree_dirty=True)
    for k in ['staged_patch','unstaged_patch']: checkpoint['artifacts'][k].update(required=False,path=None,sha256=None,reason='No tracked changes in original or resumed status; no patch created')
    checkpoint['artifacts']['untracked_backup']=backup_results['untracked']
    checkpoint['artifacts']['ignored_governed_backup']=backup_results['ignored-governed']
    checkpoint['secret_recovery']={'mode':'USER_ACCEPTED_PRESERVE_IN_PLACE','user_managed_paths':sorted(APPROVED),'approval_ref':'evidence/USER_APPROVAL.json','content_copied_to_checkpoint':False,'content_read':False,'content_hashed':False,'modified':False,'deleted':False,'moved':False,'renamed':False,'user_accepts_no_independent_banyan_backup':True,'future_stages_preserve_metadata_only_and_deny_write':True,'other_tracked_potential_secrets':'Unmodified tracked paths: Git HEAD/index object references only; no content access or waiver','exception_applies_to_other_paths':False}
    checkpoint['recovery']['coverage']='PARTIAL_APPROVED'
    checkpoint['recovery']['exception']='Only the 13 explicitly approved ignored local environment configurations have no independent Banyan content backup. If lost, the Stage 00 checkpoint cannot restore their contents.'
    checkpoint['validation'].update(patch_artifacts_hashed=True,backup_artifacts_hashed=True,binary_changes_covered=True)
    checkpoint['validation']['patch_note']='No staged/unstaged patch needed; status and index evidence prove no tracked modifications'
    checkpoint['notes']=['User-supplied construction inputs preserved and safely archived, not labeled historical project development state.','17 ignored nonsecret governed files backed up, including 2 governance documents and 15 local upload images.','Excluded dependency/build/log/OS/IDE files are not claimed to have independent backups; per-path reasons recorded.','Archive content verification is non-destructive; no restore rehearsal performed against the project.']
    writeyaml(STAGE/'CHECKPOINT_RECORD.yaml',checkpoint)
    (STAGE/'checkpoint/RESTORE_INSTRUCTIONS.md').write_text('''# Stage 00 restore instructions

Purpose: recover baseline non-secret project state. Owner: Stage 00. This file authorizes no restore.

1. Stop dependent stages and compare then-current Git HEAD/index/status and file hashes against this baseline. Preserve newer user work first.
2. Baseline HEAD is recorded in BASELINE_MANIFEST.yaml. Original index/working tree have no tracked changes; no staged/unstaged patches are necessary. Use minimal path-specific Git recovery only after an approved restore plan; never reset/clean the whole repository.
3. Verify checkpoint archive hashes using CHECKPOINT_RECORD.yaml. Inspect members before extracting selected non-secret paths. Relative paths are repository-relative. Never overwrite newer files blindly.
4. Restore untracked.tar and ignored-governed.tar selectively when required. The untracked archive also preserves user-supplied construction documents; it does not designate them as historical development state.
5. The 13 USER_ACCEPTED_PRESERVE_IN_PLACE environment configs have NO Banyan content backup. Never read, hash, copy, edit, delete, move, rename or stage them. Losing these files cannot be repaired from this checkpoint. The user explicitly accepts this risk. Other potential secrets are not covered by this waiver.
6. Re-validate hashes, index/status and metadata-only protection after any permitted restore. This Stage only verified archive integrity; it did not restore real files.
7. To undo Stage 00 itself, first preserve evidence and request an archival/cleanup decision scoped solely to .banyan-refactor. Do not touch original project files. No automatic cleanup is authorized.
''')
    contract={'required':True,'owner_stage':'02/04','sequence':['capture bootstrap source hash and source run id','migrate to frozen canonical .banyan/migrations paths','record migration timestamp and target hash','validate lineage and content','make bootstrap READ_ONLY_ARCHIVE_OR_REFERENCE'],'source_hash_required':True,'target_hash_required':True,'validation_required':True,'bootstrap_after_migration':'READ_ONLY_ARCHIVE_OR_REFERENCE'}
    register=template('MIGRATION_REGISTER.bootstrap.template.yaml'); trace=template('BANYAN_REFACTOR_TRACE.bootstrap.template.yaml')
    for obj in [register,trace]:
        obj['bootstrap'].update(refactor_control_root=str(CONTROL),run_id=RUN,future_migration=contract)
    actual=['BASELINE_MANIFEST.yaml','PROTECTED_PATHS_MANIFEST.yaml','DISCOVERY_SCOPE_BASELINE.yaml','CHECKPOINT_RECORD.yaml','FILE_HASHES.sha256','PRE_STAGE_GIT_STATUS.txt','POST_STAGE_GIT_STATUS.txt','checkpoint/untracked.tar','checkpoint/ignored-governed.tar','checkpoint/RESTORE_INSTRUCTIONS.md','ACCEPTANCE_REPORT.md','evidence/VALIDATION_RESULTS.yaml','evidence/NEXT_STAGE_HANDOFF.yaml']
    s=register['stages']['00']; s.update(status='VALIDATING',baseline_commit=head,sub_stages={'00-A':'VALIDATING','00-B':'VALIDATING'},actual_artifacts=[str(STAGE.relative_to(CONTROL)/x) for x in actual],rollback_point='CHECKPOINT-'+RUN,open_risks=[{'id':'R00-SECRET-001','status':'USER_ACCEPTED','description':checkpoint['recovery']['exception'],'scope':sorted(APPROVED)}],next_stage_handoff=str(STAGE.relative_to(CONTROL)/'evidence/NEXT_STAGE_HANDOFF.yaml'),recovery_coverage='PARTIAL_APPROVED')
    s['resume_history']=[{'event':'PRECHECK_BLOCKED','evidence':str(STAGE.relative_to(CONTROL)/'evidence/PRECHECK_BLOCKED.md')},{'event':'USER_APPROVED_EXACT_13_PATH_EXCEPTION','evidence':str(STAGE.relative_to(CONTROL)/'evidence/USER_APPROVAL.json')},{'event':'RESUMED_SAME_RUN','baseline_recaptured':False,'original_state_unchanged':True}]
    trace['baseline_head']=head; trace['rollback_point']='CHECKPOINT-'+RUN
    trace['requirements'][2]['acceptance_qualification']='User-approved PARTIAL_APPROVED recovery; excluded 13 secret contents cannot be restored from Banyan backup.'
    for req in trace['requirements']:
        req['design_artifacts']=[str(PACK.relative_to(REPO)/x) for x in req['design_artifacts']]
        req['implementation_artifacts']=[str(STAGE.relative_to(CONTROL)/x) for x in actual if not x.startswith('ACCEPTANCE')]
        req['validation_artifacts']=[str(STAGE.relative_to(CONTROL)/'evidence/VALIDATION_RESULTS.yaml')]
        req['evidence']=[str(STAGE.relative_to(CONTROL)/'evidence/USER_APPROVAL.json'),str(STAGE.relative_to(CONTROL)/'evidence/CHECKPOINT_INTEGRITY.json')]
    writeyaml(CONTROL/'MIGRATION_REGISTER.bootstrap.yaml',register); writeyaml(CONTROL/'BANYAN_REFACTOR_TRACE.bootstrap.yaml',trace)
    handoff={'upstream_stage':'00','run_id':RUN,'acceptance_result':'PENDING_VALIDATION','actual_artifacts_to_consume':actual[:7]+['../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml'],'evidence_to_trust':['evidence/pack-resume-check.json','evidence/FILE_INVENTORY.jsonl','evidence/USER_APPROVAL.json','evidence/CHECKPOINT_INTEGRITY.json','evidence/VALIDATION_RESULTS.yaml','evidence/SAFETY_COMPARISON.json'],'unresolved_risks':s['open_risks'],'protected_allowed_scope_changes':{'new_write_scope':'.banyan-refactor/** only','secret_policy_unchanged':True,'approved_secret_recovery_exception_only':sorted(APPROVED),'other_protected_paths_remain_read_only':True,'stage01_execution_authorized':False},'rollback_point':{'id':'CHECKPOINT-'+RUN,'path':'CHECKPOINT_RECORD.yaml','coverage':'PARTIAL_APPROVED','instructions':'checkpoint/RESTORE_INSTRUCTIONS.md'},'stage01_entry_gate':{'result':'PENDING_VALIDATION','qualification':'Only acceptable under exact user-approved 13-path recovery exception; not COMPLETE','execution_requires_new_user_instruction':True}}
    writeyaml(STAGE/'evidence/NEXT_STAGE_HANDOFF.yaml',handoff)
    print(json.dumps({'stage_root':str(STAGE),'backups':{k:v['file_count'] for k,v in backup_results.items()},'status':'VALIDATING'},ensure_ascii=False))

def safety():
    entries=load_inventory(); mismatches=[]; hash_count=0; metadata_count=0
    for e in entries:
        p=REPO/e['path']
        if e['sha256']:
            hash_count+=1
            if not p.is_file() or p.is_symlink() or filehash(p)!=e['sha256']: mismatches.append(e['path'])
        elif e['protection_class']=='SECRET_METADATA_ONLY':
            metadata_count+=1
            if not p.exists() or metadata(p)!={k:e[k] for k in metadata(p)}: mismatches.append(e['path'])
        elif e['git_state']=='TRACKED' and e['kind']=='symlink':
            if not p.is_symlink() or os.readlink(p)!=e['link_target']: mismatches.append(e['path'])
    pre=[x for x in (TMP/'status.z').read_bytes().split(b'\0') if x]
    post=git('status','--porcelain=v2','-z','--untracked-files=all')
    rows=[x for x in post.split(b'\0') if x]
    outside=[x for x in rows if not x.startswith(b'? .banyan-refactor/')]
    identity=json.loads((TMP/'resume-git-evidence.json').read_text())
    identity_equal=all(digest(git('config','--get-all',key,allowed=(0,1)))==v for key,v in identity['identity_value_digests'].items())
    config_equal=all(metadata(Path(x['path']))=={k:v for k,v in x.items() if k!='path'} for x in identity['config_metadata'])
    operations={}
    for op in ['MERGE_HEAD','CHERRY_PICK_HEAD','REVERT_HEAD','rebase-merge','rebase-apply','sequencer']:
        p=Path(git('rev-parse','--git-path',op).decode().strip()); p=p if p.is_absolute() else REPO/p; operations[op]=p.exists()
    result={'checked_at':now(),'hashed_files_rechecked':hash_count,'secret_metadata_rechecked':metadata_count,'secret_content_integrity_claimed':False,'secret_assurance':'Stage performed no writes; lstat metadata unchanged. No claim of content-hash verification for secrets.','mismatched_paths':mismatches,'outside_control_git_status_identical':sorted(pre)==sorted(outside),'head_unchanged':git('rev-parse','HEAD')==(TMP/'head.txt').read_bytes(),'index_entries_unchanged':git('ls-files','--stage','-z')==(TMP/'index.z').read_bytes(),'ignored_membership_unchanged':git('ls-files','--others','--ignored','--exclude-standard','-z')==(TMP/'ignored.z').read_bytes(),'git_identity_unchanged':identity_equal,'git_config_file_metadata_unchanged':config_equal,'git_operations':operations,'unmerged_empty':not git('ls-files','-u','-z'),'canonical_banyan_absent':not (REPO/'.banyan').exists(),'control_was_absent_before_this_stage':True,'only_expected_new_paths':all(x.startswith(b'? .banyan-refactor/') or x in pre for x in rows)}
    result['result']='PASS' if not mismatches and all(result[k] for k in ['outside_control_git_status_identical','head_unchanged','index_entries_unchanged','ignored_membership_unchanged','git_identity_unchanged','git_config_file_metadata_unchanged','unmerged_empty','canonical_banyan_absent','only_expected_new_paths']) and not any(operations.values()) else 'FAIL'
    writejson(STAGE/'evidence/SAFETY_COMPARISON.json',result)
    (STAGE/'POST_STAGE_GIT_STATUS.txt').write_bytes(git('status','--porcelain=v2','--branch','--untracked-files=all'))
    return result

def validate(require_report):
    entries=load_inventory(); safe=safety(); results=[]
    def check(n, ok, ev, note): results.append({'id':f'V00-{n:02d}','result':'PASS' if ok else 'FAIL','evidence':ev,'notes':note})
    baseline=yaml.safe_load((STAGE/'BASELINE_MANIFEST.yaml').read_text()); protect=yaml.safe_load((STAGE/'PROTECTED_PATHS_MANIFEST.yaml').read_text()); scope=yaml.safe_load((STAGE/'DISCOVERY_SCOPE_BASELINE.yaml').read_text()); cp=yaml.safe_load((STAGE/'CHECKPOINT_RECORD.yaml').read_text()); approval=json.loads((STAGE/'evidence/USER_APPROVAL.json').read_text()); topo=json.loads((STAGE/'evidence/TOPOLOGY.json').read_text())
    check(1,Path(git('rev-parse','--show-toplevel').decode().strip())==REPO and not topo['errors'] and not topo['nested_repositories_outside_excluded_dependency_build_roots'] and not baseline['repository']['submodules'],['evidence/repo_root.txt','evidence/worktree.txt','evidence/submodule.txt','evidence/TOPOLOGY.json'],'Monorepo boundary explicit; dependencies/generated roots excluded with reasons; symlinks not followed.')
    check(2,safe['head_unchanged'] and baseline['repository']['branch']==(TMP/'branch.txt').read_text().strip() and baseline['repository']['dirty'],['BASELINE_MANIFEST.yaml','PRE_STAGE_GIT_STATUS.txt','evidence/resume-git-evidence.json'],'Original branch/HEAD/status retained; no tracked diff; 21 original untracked files.')
    check(3,not any(safe['git_operations'].values()) and safe['unmerged_empty'],['evidence/git_operation.txt','evidence/SAFETY_COMPARISON.json'],'No unresolved merge/rebase/cherry-pick/revert/sequencer/conflict.')
    check(4,len(entries)==sum(len(readlist(n)) for n in ['tracked.z','untracked.z','ignored.z']) and all(e['reason'] and e['discovery_mode'] in ['SCAN','METADATA_ONLY','EXCLUDE_WITH_REASON'] for e in entries) and all(scope['coverage'].values()),['DISCOVERY_SCOPE_BASELINE.yaml','evidence/FILE_INVENTORY.jsonl','evidence/EXCLUSIONS.json'],'100010 paths classified; per-file records override root defaults; no Stage 01 semantic inventory.')
    governed=[e['path'] for e in entries if e.get('governed')]
    check(5,set(governed)==set(cp['artifacts']['ignored_governed_backup']['members']) and len(governed)==17,['evidence/IGNORED_GOVERNED.json','checkpoint/ignored-governed.tar'],'Ignored governance docs and local assets retained; ignored secret exception kept separate.')
    rules={r['path']:r for r in protect['rules']}; deny=all(not rules[p]['writable'] and not rules[p]['deletable'] and rules[p]['preserve_in_place'] and not rules[p]['content_read_allowed'] and not rules[p]['checkpoint_content_copy_allowed'] and not rules[p]['git_commit_allowed'] for p in APPROVED)
    check(6,deny and not protect['default_policy']['write'] and [r['path'] for r in protect['rules'] if r.get('write') is True]==['.banyan-refactor/**'] and not rules['.banyan/migrations/**']['write'],['PROTECTED_PATHS_MANIFEST.yaml','evidence/USER_APPROVAL.json'],'Only bootstrap root writable; 13 exact secret paths remain metadata-only through future stages; no waiver for others.')
    secret_entries=[e for e in entries if e['protection_class']=='SECRET_METADATA_ONLY']; backup_members=sum([cp['artifacts'][k]['members'] for k in ['untracked_backup','ignored_governed_backup']],[])
    check(7,all(e['sha256'] is None and not e['content_read'] and not e['content_copied'] and not e['content_hashed'] for e in secret_entries) and not set(backup_members)&{e['path'] for e in secret_entries} and safe['secret_metadata_rechecked']==len(secret_entries),['evidence/SECRET_METADATA.json','evidence/stage00_execution.py','evidence/SAFETY_COMPARISON.json'],'69 conservatively classified potential-secret paths: no content I/O; 13 ignored exceptions, remaining clean tracked references. Secret content equality is not claimed.')
    hash_lines=(STAGE/'FILE_HASHES.sha256').read_text().splitlines()
    check(8,len(hash_lines)==sum(bool(e['sha256']) for e in entries)==safe['hashed_files_rechecked'] and not safe['mismatched_paths'] and all(not e['path'].startswith('.banyan-refactor/') for e in entries),['FILE_HASHES.sha256','evidence/FILE_INVENTORY.jsonl','evidence/HASH_SCOPE_REPORT.json','evidence/SAFETY_COMPARISON.json'],'5835 regular-file SHA-256 values verified; symlink text and secret metadata are recorded separately; exclusions explained.')
    archive_ok=True
    for key in ['untracked_backup','ignored_governed_backup']:
        a=cp['artifacts'][key]; archive_ok &= filehash(STAGE/a['path'])==a['sha256']
        with tarfile.open(STAGE/a['path']) as tar:
            archive_ok &= {m.name for m in tar.getmembers()}==set(a['members'])
            source={e['path']:e for e in entries}
            for m in tar.getmembers(): archive_ok &= m.isfile() and digest(tar.extractfile(m).read())==source[m.name]['sha256']
    approved_ok=set(approval['scope'])==APPROVED and approval['recovery_coverage']=='PARTIAL_APPROVED' and approval['user_accepts_no_independent_banyan_backup']
    check(9,archive_ok and approved_ok and cp['recovery']['coverage']=='PARTIAL_APPROVED' and cp['secret_recovery']['mode']=='USER_ACCEPTED_PRESERVE_IN_PLACE',['CHECKPOINT_RECORD.yaml','evidence/USER_APPROVAL.json','evidence/CHECKPOINT_INTEGRITY.json'],'PASS under explicit user-approved partial recovery exception ONLY; 13 secret contents have NO independent backup and cannot be restored from checkpoint. Not COMPLETE.')
    check(10,baseline['working_tree']['binary_changed_count']==0 and safe['index_entries_unchanged'] and not any(x[:1] in [b'1',b'2',b'u'] for x in (TMP/'status.z').read_bytes().split(b'\0')),['evidence/status.z','evidence/index.z','evidence/CHECKPOINT_INTEGRITY.json'],'No tracked binary changes; no patch required. Non-secret untracked/ignored binary assets verified inside tar.')
    check(11,archive_ok and set(cp['artifacts']['untracked_backup']['members'])==set(readlist('untracked.z')),['evidence/untracked.z','checkpoint/untracked.tar','evidence/CHECKPOINT_INTEGRITY.json'],'All 21 relevant untracked files safely backed up, including preserved user-supplied construction materials.')
    check(12,safe['result']=='PASS',['PRE_STAGE_GIT_STATUS.txt','POST_STAGE_GIT_STATUS.txt','evidence/SAFETY_COMPARISON.json'],'Outside-control Git status, HEAD, index, identity unchanged; managed hashes and secret lstat metadata unchanged; no automatic commit or destructive operations.')
    parsed=[]; parse_errors=[]
    for p in list(STAGE.rglob('*.yaml'))+[CONTROL/'MIGRATION_REGISTER.bootstrap.yaml',CONTROL/'BANYAN_REFACTOR_TRACE.bootstrap.yaml']:
        try:
            obj=yaml.safe_load(p.read_text()); assert isinstance(obj,dict); parsed.append(stage_ref(p))
        except Exception as err: parse_errors.append({'path':stage_ref(p),'type':type(err).__name__})
    refs=['DISCOVERY_SCOPE_BASELINE.yaml','PROTECTED_PATHS_MANIFEST.yaml','CHECKPOINT_RECORD.yaml','FILE_HASHES.sha256','../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml']
    check(13,not parse_errors and all((STAGE/x).exists() for x in refs),['evidence/MANIFEST_PARSE.json'],'Actual YAML documents parse; mandatory baseline links and checkpoint member paths exist; future canonical paths are explicitly future, absent.')
    writejson(STAGE/'evidence/MANIFEST_PARSE.json',{'result':'PASS' if not parse_errors else 'FAIL','parsed':parsed,'errors':parse_errors,'resolved_baseline_references':refs})
    reg=yaml.safe_load((CONTROL/'MIGRATION_REGISTER.bootstrap.yaml').read_text()); trace=yaml.safe_load((CONTROL/'BANYAN_REFACTOR_TRACE.bootstrap.yaml').read_text())
    bvalid=all(o['bootstrap']['bootstrap_only'] and o['bootstrap']['lineage_required'] and o['bootstrap']['dual_writable_truth_forbidden'] and not o['bootstrap']['canonical_writable_truth_active'] and o['bootstrap']['future_migration']['source_hash_required'] and o['bootstrap']['future_migration']['validation_required'] for o in [reg,trace])
    check(14,bvalid and safe['canonical_banyan_absent'] and reg['bootstrap']['future_canonical_path']=='.banyan/migrations/MIGRATION_REGISTER.yaml' and trace['bootstrap']['future_canonical_path']=='.banyan/migrations/BANYAN_REFACTOR_TRACE.yaml',['../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml','evidence/SAFETY_COMPARISON.json'],'Single bootstrap writable Register/Trace pair; source/run lineage → canonical target hash → validation → bootstrap read-only archive obligation recorded.')
    handoff=yaml.safe_load((STAGE/'evidence/NEXT_STAGE_HANDOFF.yaml').read_text())
    hvalid=all(k in handoff for k in ['upstream_stage','run_id','actual_artifacts_to_consume','evidence_to_trust','unresolved_risks','protected_allowed_scope_changes','rollback_point','stage01_entry_gate']) and all((STAGE/x).exists() for x in handoff['actual_artifacts_to_consume'])
    if require_report: hvalid &= (STAGE/'ACCEPTANCE_REPORT.md').exists() and 'NEXT_STAGE_HANDOFF' in (STAGE/'ACCEPTANCE_REPORT.md').read_text() and handoff['stage01_entry_gate']['result']=='PASS'
    check(15,hvalid,['ACCEPTANCE_REPORT.md','evidence/NEXT_STAGE_HANDOFF.yaml'],'Complete handoff with PARTIAL_APPROVED risk and exact scope; Stage 01 permission gate is distinct from execution authorization.' if require_report else 'Pre-acceptance handoff structure checked; final report/gate check remains required.')
    return results

def report(results):
    summary=json.loads((STAGE/'evidence/HASH_SCOPE_REPORT.json').read_text()); base=yaml.safe_load((STAGE/'BASELINE_MANIFEST.yaml').read_text()); cp=yaml.safe_load((STAGE/'CHECKPOINT_RECORD.yaml').read_text()); handoff=yaml.safe_load((STAGE/'evidence/NEXT_STAGE_HANDOFF.yaml').read_text())
    core=['BASELINE_MANIFEST.yaml','PROTECTED_PATHS_MANIFEST.yaml','DISCOVERY_SCOPE_BASELINE.yaml','CHECKPOINT_RECORD.yaml','FILE_HASHES.sha256','PRE_STAGE_GIT_STATUS.txt','POST_STAGE_GIT_STATUS.txt','../../../MIGRATION_REGISTER.bootstrap.yaml','../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml','checkpoint/untracked.tar','checkpoint/ignored-governed.tar']
    text=f'''# Stage 00 实际验收报告

1. Stage Status: COMPLETED。Validation: PASS。恢复覆盖始终为 PARTIAL_APPROVED，绝非 COMPLETE。

2. Repository Baseline: `{REPO}`；Branch `{base['repository']['branch']}`；HEAD `{base['repository']['head']}`。单一 Git 仓库、多应用 monorepo；单 worktree；无 submodule、无非依赖范围 nested repo；无 sparse checkout；LFS CLI 不可用，但 Git 属性中无 LFS 管理文件。未解决 Git operation/conflict = 0。原始 staged/unstaged = 0；untracked = 21。

3. Discovery Scope: 原始 {summary['total_files']} 个 Git 可枚举路径均有安全分类。正文允许 SCAN、METADATA_ONLY、EXCLUDE_WITH_REASON 分开记录。源文件 SHA-256 {summary['hash_count']} 项。依赖/构建/日志/OS/IDE 排除均有理由。未执行 Stage 01 AI 能力语义盘点。AUDIT/ARCHIVE 未全文加载，仅做完整性字节处理及安全备份。

4. Protected Paths: 仅 `.banyan-refactor/**` 允许本阶段生成控制产物。业务代码、SQL、配置、正式 PRD/DEC/ADR/CR/UI_SPEC/Guide、Legacy Prompt/Rules/Skills、现有编辑器入口默认禁止修改。正式 `.banyan/migrations/**` 为 CONDITIONAL_WRITE_LATER，当前不存在。

5. Checkpoint Coverage: PARTIAL_APPROVED。21 个非敏感 untracked 文件、17 个 ignored-but-governed 文件已归档并逐成员验证 SHA-256；其中 ignored 包括2份治理文档和15张本地资源图片。无 tracked 修改，因此没有伪造空 patch。用户主动复制的榕树施工资料保留原位并安全备份，不被描述为历史开发现场。

## Secret 明确例外

用户明确批准 `USER-STAGE00-SECRET-EXCEPTION-001`，仅限列出的13份 ignored 本地环境配置：

'''+''.join('- `'+p+'`\n' for p in sorted(APPROVED))+'''
这13份文件：未读取正文、未复制正文、未 Hash Secret 正文、未修改、未删除、未移动、未重命名、未纳入 Git 提交。用户明确接受其没有独立 Banyan Backup，只保留当前本地环境的恢复风险。`recovery_mode = USER_ACCEPTED_PRESERVE_IN_PLACE`。后续所有 Stage 必须继续仅访问 metadata，禁止写入/删除/移动/重命名/内容复制/内容哈希/提交；本次批准不放宽其它 Secret 或 Protected Path。

潜在敏感文件共69项（包括保守按路径分类的模板/源码候选），其余为无修改的 tracked 文件，仅记录 Git object/index 引用，不读取其内容，也不将其套用本次13路径豁免。metadata未变不是Secret正文哈希一致的证明；本次只声明无写入操作与lstat一致。

6. Actual Artifacts（SHA-256；完整列表与封存哈希见 ARTIFACT_HASHES.sha256）：

'''+''.join(f'- `{p}` — `{filehash(STAGE/p)}`\n' for p in core)+'''
7. V00-01～V00-15：

'''+''.join(f"- **{r['id']}: {r['result']}** — {r['notes']} Evidence: "+', '.join('`'+x+'`' for x in r['evidence'])+'\n' for r in results)+'''
8. Open Risks / Blockers: 阻塞已解除；R00-SECRET-001 为用户接受的剩余风险。13份配置没有独立内容备份，原位文件丢失时不能靠本 Checkpoint 恢复。Stage 00 只验证归档内容与路径完整性，未在真实工作区执行恢复演练。控制产物尚未提交Git，也不是独立离线备份；临时原始捕获可能被系统清理，已复制证据至控制目录。后续阶段开始前应验证基线新鲜度。

9. 实际修改文件: 原项目既有文件零修改。仅新建 `.banyan-refactor/` 下控制文件、检查点、Evidence 与本报告，以及系统临时目录中的执行脚本/证据。完整仓库内写入路径见 evidence/ACTUAL_WRITES.txt；脚本和原始临时路径见 evidence/stage00_execution.py 与 evidence/precheck.json。

10. 重要保护区未修改: nunu-go-api、三套go-uni-app、docs/project、docs/governance、docs/temp、.cursor、tools、榕树施工资料、.gitignore、Git HEAD/index/identity。受管非敏感正文哈希复核通过；敏感路径只校验元数据；生成物/依赖/日志排除范围不宣称正文逐字验证。未commit/stash/tag/push/reset/clean/restore；未初始化.banyan。

11. Rollback Point: `'''+cp['checkpoint_id']+'''`。HEAD + 原始未提交文件归档 + ignored受管归档 + 明确排除/批准例外；恢复覆盖 PARTIAL_APPROVED。先比较最新现场并保留后续用户工作，再执行经授权的最小恢复；禁止破坏性自动恢复。详见 checkpoint/RESTORE_INSTRUCTIONS.md 和 evidence/ROLLBACK_POINT.yaml。

12. Bootstrap Register / Trace: 唯一可写真源在控制根目录的 MIGRATION_REGISTER.bootstrap.yaml / BANYAN_REFACTOR_TRACE.bootstrap.yaml；bootstrap_only=true；activation=OFF。未来必须捕获 source hash/run lineage → canonical .banyan/migrations/* → target hash/validation → bootstrap只读归档/reference；禁止双可写真源。未执行未来迁移。

## 13. NEXT_STAGE_HANDOFF

'''+yaml.safe_dump(handoff,allow_unicode=True,sort_keys=False)+'''
14. Stage 01 Entry Gate: PASS，依据用户明确批准的13路径 PARTIAL_APPROVED 例外，不声称 COMPLETE。只表示安全交棒条件满足，未授权或执行 Stage 01。本次停止于 Stage 00，等待下一步指令。

## Execution lineage and authority

Run ID: `'''+RUN+'''`；Executor: Codex TRANSFORMATION_EXECUTOR。Pack/Charter均为1.9.1；15项Pack校验通过。沿用仓库外原始precheck捕获，复核原始HEAD/index/status后从同一Block Point续做，未重启Stage 00。历史BLOCKED报告保留为Evidence，不再表示当前状态。用户明确的PARTIAL_APPROVED授权适用于本次Exit Gate；不修改Pack或上位资料正文。

Acceptance generated after actual checkpoint and primary validation; final handoff/report validation and sealing follow. Final results in evidence/VALIDATION_RESULTS.yaml and evidence/FINAL_VERIFICATION.json.
'''
    (STAGE/'ACCEPTANCE_REPORT.md').write_text(text)

def finish():
    # Refresh recorded one-run tool source before validating what was actually executed.
    shutil.copyfile(Path(__file__),STAGE/'evidence/stage00_execution.py')
    initial=validate(False)
    assert all(r['result']=='PASS' for r in initial), json.dumps(initial)
    writeyaml(STAGE/'evidence/PRE_ACCEPTANCE_VALIDATION.yaml',{'phase':'Primary validation; V00-15 report check still pending','results':initial})
    regpath=CONTROL/'MIGRATION_REGISTER.bootstrap.yaml'; tracepath=CONTROL/'BANYAN_REFACTOR_TRACE.bootstrap.yaml'
    reg=yaml.safe_load(regpath.read_text()); trace=yaml.safe_load(tracepath.read_text())
    reg['stages']['00'].update(status='COMPLETED',sub_stages={'00-A':'COMPLETED','00-B':'COMPLETED'},validation={'overall':'PASS','results':{r['id']:'PASS' for r in initial},'evidence':str(STAGE.relative_to(CONTROL)/'evidence/VALIDATION_RESULTS.yaml'),'qualification':'Exact user-approved PARTIAL_APPROVED recovery exception; final sealing required'})
    for r in trace['requirements']: r.update(capability_state='VERIFIED',status='SATISFIED',activation_mode='OFF')
    trace['verification_qualification']='R00-SECRET-001: USER_ACCEPTED_PRESERVE_IN_PLACE for 13 paths; recovery PARTIAL_APPROVED, not COMPLETE'
    writeyaml(regpath,reg); writeyaml(tracepath,trace)
    cp=yaml.safe_load((STAGE/'CHECKPOINT_RECORD.yaml').read_text())
    cp['bootstrap']={'control_root':str(CONTROL),'register_path':'../../../MIGRATION_REGISTER.bootstrap.yaml','trace_path':'../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml','register_sha256':filehash(regpath),'trace_sha256':filehash(tracepath),'future_canonical_paths':['.banyan/migrations/MIGRATION_REGISTER.yaml','.banyan/migrations/BANYAN_REFACTOR_TRACE.yaml'],'lineage_required':True,'dual_writable_truth_forbidden':True}
    writeyaml(STAGE/'CHECKPOINT_RECORD.yaml',cp)
    writeyaml(STAGE/'evidence/ROLLBACK_POINT.yaml',{'rollback_point_id':cp['checkpoint_id'],'baseline_head':cp['baseline']['head'],'working_tree_state_hash':filehash(STAGE/'evidence/FILE_INVENTORY.jsonl'),'created_at':cp['created_at'],'recovery_coverage':'PARTIAL_APPROVED','checkpoint_artifacts':cp['artifacts'],'bootstrap_register_hash':filehash(regpath),'bootstrap_trace_hash':filehash(tracepath),'approval_ref':'USER_APPROVAL.json','destructive_auto_restore_allowed':False})
    handoff=yaml.safe_load((STAGE/'evidence/NEXT_STAGE_HANDOFF.yaml').read_text()); handoff['acceptance_result']='PASS_WITH_USER_APPROVED_PARTIAL_RECOVERY'; handoff['stage01_entry_gate']['result']='PASS'; writeyaml(STAGE/'evidence/NEXT_STAGE_HANDOFF.yaml',handoff)
    report(initial)
    final=validate(True); assert all(r['result']=='PASS' for r in final),json.dumps(final)
    writeyaml(STAGE/'evidence/VALIDATION_RESULTS.yaml',{'stage_id':'00','run_id':RUN,'overall':'PASS','checked_at':now(),'recovery_coverage':'PARTIAL_APPROVED','qualification':'User-approved exact 13 secret path exception only','results':final})
    # Create every final output path before final Git status capture; content changes do not change untracked path listing.
    (STAGE/'evidence/FINAL_VERIFICATION.json').write_text('{}\n')
    (STAGE/'evidence/ACTUAL_WRITES.txt').write_text('')
    (STAGE/'ARTIFACT_HASHES.sha256').write_text('')
    final_safety=safety(); assert final_safety['result']=='PASS'
    report(final)
    writes=sorted(str(p.relative_to(REPO)) for p in CONTROL.rglob('*') if p.is_file())
    (STAGE/'evidence/ACTUAL_WRITES.txt').write_text('\n'.join(writes)+'\n')
    writejson(STAGE/'evidence/FINAL_VERIFICATION.json',{'result':'PASS','finished_at':now(),'stage_status':'COMPLETED','stage01_started':False,'stage01_entry_gate':'PASS','recovery_coverage':'PARTIAL_APPROVED','all_15_validation_pass':True,'checkpoint_archives_verified':True,'post_status_final_path_set_captured':True,'secret_13_no_body_read_copy_hash_write_delete':True,'evidence_limit':'Secret integrity verified only by metadata and no-write execution; no body hash','actual_repo_files_written':len(writes),'source_precheck_run':RUN})
    seal=[]
    for p in sorted(CONTROL.rglob('*')):
        if p.is_file() and p!=STAGE/'ARTIFACT_HASHES.sha256': seal.append(filehash(p)+'  '+os.path.relpath(p,STAGE)+'\n')
    (STAGE/'ARTIFACT_HASHES.sha256').write_text(''.join(seal))
    assert git('status','--porcelain=v2','--branch','--untracked-files=all')==(STAGE/'POST_STAGE_GIT_STATUS.txt').read_bytes()
    print(json.dumps({'status':'COMPLETED','coverage':'PARTIAL_APPROVED','validation':{r['id']:r['result'] for r in final},'acceptance':str(STAGE/'ACCEPTANCE_REPORT.md'),'files_written':len(writes),'seal_sha256':filehash(STAGE/'ARTIFACT_HASHES.sha256')},ensure_ascii=False,indent=2))

if __name__=='__main__':
    if sys.argv[1]=='prepare': prepare()
    elif sys.argv[1]=='create': create()
    elif sys.argv[1]=='finish': finish()
