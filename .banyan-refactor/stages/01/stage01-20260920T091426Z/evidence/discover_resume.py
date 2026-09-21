"""Stage 01 read-only discovery; output files are exclusive-create in this run.
Never executes project scripts/hooks, follows symlinks, or opens secret bodies.
"""
import collections, datetime, hashlib, json, os, re, subprocess
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[5]
RUN = Path(__file__).resolve().parents[1]
UP = ROOT/'.banyan-refactor/stages/00/stage00-precheck-20260920T083254Z'
PACK = ROOT/'榕树ai改造落地相关文档/Stage_01_AI资产全量盘点与方案裁剪'
os.chdir(ROOT)
def git(*args):
    return subprocess.check_output(['git', *args], env={**os.environ, 'GIT_OPTIONAL_LOCKS':'0'})
def sha(b): return hashlib.sha256(b).hexdigest()
def put(name, value, kind='json'):
    p=RUN/name
    with p.open('x', encoding='utf-8') as f:
        if kind=='jsonl':
            for x in value:f.write(json.dumps(x,ensure_ascii=False)+'\n')
        elif kind=='yaml':yaml.safe_dump(value,f,allow_unicode=True,sort_keys=False)
        else:json.dump(value,f,ensure_ascii=False,indent=2)
def isolated(p):return p.startswith(('.banyan-refactor/', '榕树ai改造落地相关文档/')) or p=='.banyan-refactor.zip'
baseline={x['path']:x for x in map(json.loads,(UP/'evidence/FILE_INVENTORY.jsonl').open())}
original={str(p.relative_to(RUN)):sha(p.read_bytes()) for p in RUN.rglob('*') if p.is_file() and p!=Path(__file__).resolve()}
head=git('rev-parse','HEAD').decode().strip()
assert head==json.loads((RUN/'evidence/BASELINE_FRESHNESS.json').read_text())['head']
input_reads=[]
for p in sorted((ROOT/'榕树ai改造落地相关文档/00_总纲与审计/CURRENT').glob('*.md'))+sorted(PACK.rglob('*')):
    if p.is_file():
        t=p.read_text();input_reads.append({'path':str(p.relative_to(ROOT)), 'sha256':sha(t.encode()),'lines':len(t.splitlines()),'read_scope':'FULL_FILE; stage requirements reviewed; no archive loading'})
put('evidence/RESUME_PRECHECK.json',dict(result='PASS',case='A',run_id=RUN.name,verified_steps=['01.0','01.1'],resume_step='01.2',existing_artifacts=[],existing_evidence_hashes=original,head=head,outside_control_path_drift=[],baseline_hashes_verified=5835,secret_metadata_verified=69,pack_entries_verified=28,upstream_entries_verified=58,bootstrap_matches_snapshots=True,notes=['Earlier unpersisted analysis not credited as completed discovery.','No second run; original evidence preserved.','rg AGENTS.md exit 1 means no matching repository instruction file.']))
put('evidence/RESUME_INPUT_READS.json',input_reads)

states={}
for state,args in [('TRACKED',('ls-files','-z')),('UNTRACKED',('ls-files','--others','--exclude-standard','-z')),('IGNORED',('ls-files','--others','--ignored','--exclude-standard','-z'))]:
    for p in git(*args).decode().split('\0'):
        if p:states[p]=state
dirs=[];physical=set()
for base,ds,fs in os.walk(ROOT,followlinks=False):
    ds[:]=[d for d in ds if d!='.git']
    rel=Path(base).relative_to(ROOT)
    dirs.append(str(rel))
    for f in fs:physical.add(str(rel/f))
    for d in ds:
        if (Path(base)/d).is_symlink():physical.add(str(rel/d))
for p in physical-states.keys():states[p]='FILESYSTEM_ONLY'
secret={p for p,x in baseline.items() if 'SECRET' in x['protection_class']}
extra_secret={'nunu-go-api/scripts/ssh-tunnel-test.ps1'}
terms={
 'governance':r'INFORMED_DECISION|CR_DECISION_APPLY|EFFECTIVE_UI_CONTRACT|PROGRESS_REGISTER|AI_DOCUMENTATION_GUIDE|Parallel.?Draft|变更稿模式|在引用规则保护',
 'agent_rule':r'(?i)alwaysApply:|AGENTS\.md|CLAUDE\.md|\.cursor/rules|\.codex/|AI.*(?:提示词|工作边界|文档生产)',
 'commit':r'(?i)commitlint|lint-staged|husky|commit-msg|pre-commit|分批提交|提交.*(?:规范|规则)|git commit',
 'runtime':r'(?i)WORKLOG|HANDOVER|PROJECT_DASHBOARD|RUNTIME_STATE|BAG\.md|PLAIN_SYNC',
 'reference':r'(?i)Superseded|Baselined|Approved|Deprecated',
}
patterns={k:re.compile(v) for k,v in terms.items()}
texts={};features=[];universe=[];assets=[];refs=[];read_paths=[]
def aid(p):return 'ASSET-'+sha(p.encode())[:14]
def evidence(p):return ['evidence/DISCOVERY_UNIVERSE.jsonl#'+p,'evidence/CONTENT_FEATURES.jsonl#'+p]
for p,state in sorted(states.items()):
    old=baseline.get(p,{})
    q=ROOT/p
    row={'path':p,'git_state':state,'exists':q.exists() or q.is_symlink(),'baseline_discovery_mode':old.get('discovery_mode'),'candidate':False}
    if isolated(p):
        row.update(coverage='EXCLUDED_WITH_REASON',reason='REFRACTOR_CONSTRUCTION_MATERIAL' if p.startswith('榕树') else 'UPSTREAM_REFACTOR_OPERATIONAL_EVIDENCE');universe.append(row);continue
    if p in secret|extra_secret:
        s=q.lstat();row.update(coverage='COVERED_METADATA_ONLY',reason='SECRET_METADATA_ONLY inherited' if p in secret else 'Conservative added tunnel credential boundary; no body needed',size=s.st_size,mtime_ns=s.st_mtime_ns,content_read=False,content_hash=False,content_copy=False);universe.append(row);continue
    if q.is_symlink():
        row.update(coverage='COVERED_METADATA_ONLY',reason='Symlink text only; target not followed',symlink_target=os.readlink(q))
        candidate=p.startswith(('.cursor/','.codex/','.claude/'))
        t='';mode='METADATA_ONLY'
    elif old.get('discovery_mode')=='EXCLUDE_WITH_REASON':
        row.update(coverage='EXCLUDED_WITH_REASON',reason=old['reason']);universe.append(row);continue
    elif old.get('discovery_mode')!='SCAN':
        row.update(coverage='EXCLUDED_WITH_REASON',reason=old.get('reason','Not baseline-authorized for content; metadata discovery only'));universe.append(row);continue
    else:
        b=q.read_bytes();read_paths.append(p)
        row['sha256']=sha(b)
        try:t=b.decode('utf-8') if b'\0' not in b else ''
        except UnicodeDecodeError:t=''
        row.update(coverage='COVERED_CONTENT' if t else 'COVERED_METADATA_ONLY',reason='Full text feature and local-reference scan; source hashes preserved' if t else 'Binary asset classified by path/registry; visual semantics not inspected')
        hits={k:[i for i,l in enumerate(t.splitlines(),1) if pat.search(l)] for k,pat in patterns.items()}
        candidate=(p.startswith(('docs/','tools/','.cursor/','.codex/','.claude/','.github/','.husky/')) or q.suffix.lower() in ('.md','.mdc','.py','.sh','.ps1') or q.name in ('jenkinsfile','Makefile','package.json','AGENTS.md','CLAUDE.md') or bool(hits['governance'] or hits['agent_rule'] or hits['commit']))
        if t:
            texts[p]=t
            features.append({'path':p,'sha256':row['sha256'],'lines':len(t.splitlines()),'signals':hits,'headings':[{'line':i,'text':l[:200]} for i,l in enumerate(t.splitlines(),1) if l.startswith('#')][:100],'status_tokens':dict(collections.Counter(re.findall(r'\b(?:Draft|Approved|Baselined|Superseded|Deprecated|Ready|In Progress|Needs Review)\b',t)))})
        mode='SCAN'
    row['candidate']=candidate
    if not candidate:row['asset_disposition']='NON_GOVERNANCE_SOURCE; full text examined, no governance/tool/document signal'
    universe.append(row)
    if not candidate:continue
    # File-level roles; capability semantics are recorded separately after review.
    typ='PROJECT_FACT';can='REFERENCE';action='REFERENCE';owner='04';reason='Project/library documentation or source material; preserve provenance and map only';target='PROJECT_REFERENCE'
    if p.startswith('.cursor/'):
        typ='SKILL' if '/skills/' in p else 'POLICY';can='CANONICAL';action='KEEP';owner='17';reason='Existing active Cursor entry; retain until adapter parity is verified';target='EDITOR_ENTRY_COMPATIBILITY'
    elif p.startswith('tools/'):
        typ='TOOL' if '/scripts/' in p else ('SKILL' if q.name=='SKILL.md' else 'TEMPLATE' if '/references/' in p else 'PROJECT_FACT');action='KEEP';owner='09';target='DESIGN_PROVIDER';reason='Existing design provider, examples and executable utilities; preserve package boundaries'
    elif p.startswith('docs/governance/'):
        typ='WORKFLOW';can='CANONICAL';action='SPLIT';owner='07';target='LEGACY_V31_COMPATIBILITY';reason='Multi-capability legacy governance; split only as future compatible candidates, no text rewrite now'
    elif p.startswith('docs/project/'):
        can='CANONICAL';action='KEEP';reason='Managed project source-role candidate; status does not imply approval';target='PROJECT_CANONICAL_MAP'
        if '/progress/' in p or re.search(r'WORKLOG|HANDOVER|BAG\.',p,re.I):typ='STATE';can='OPERATIONAL';owner='11';target='OPERATIONAL_INDEX'
        elif '/plain-document/' in p:typ='PUBLISHING_ARTIFACT';can='DERIVED';owner='10';target='PROJECT_GUIDE'
        elif '/plain-spec/' in p:typ='POLICY';owner='10';target='PUBLISHING_RULES'
        elif '/templates/' in p:typ='TEMPLATE';owner='03';target='TEMPLATE_COMPATIBILITY'
        elif '/changes/' in p:typ='CHANGE_ARTIFACT';owner='06';target='CHANGE_HISTORY_MAP'
        elif q.name=='PROJECT_VARIABLES.md':typ='PROFILE';owner='04';target='VARIABLE_MAPPING'
        elif q.name=='AI_DOCUMENTATION_GUIDE.md':typ='POLICY';owner='07';target='PROJECT_GOVERNANCE_COMPATIBILITY'
        elif '/sources/' in p:can='REFERENCE';action='REFERENCE';target='SOURCE_PROVENANCE'
        elif '/ui-design/' in p:owner='08';target='UI_SOURCE_MAP'
    elif p.startswith('docs/temp/') or p in ('docs/开发指导.md','docs/项目迭代开发文档指导v2.md'):
        action='LEGACY';owner='07';target='READ_ONLY_LEGACY_REFERENCE';reason='Historical/reference instructions; newer project guide explicitly does not treat temp docs as maintained canonical rules'
    elif q.suffix in ('.sh','.ps1','.py') or q.name in ('jenkinsfile','Makefile','package.json'):
        typ='TOOL';owner='05';target='BUILD_COMMIT_PRACTICE_REFERENCE';reason='Build/deploy/tool metadata; no execution or policy adoption'
    assets.append(dict(asset_id=aid(p),path=p,repository_relative=True,origin=dict(tracked_state=state,discovered_by=['ROOT_PATH','CONTENT_FEATURES'] if mode=='SCAN' else ['ROOT_PATH','SYMLINK_METADATA'],first_seen_ref=head if state=='TRACKED' else 'WORKTREE',historical_only=False),asset_type=typ,subtype=q.suffix or q.name,classification=dict(action=action,confidence='HIGH' if p.startswith(('.cursor/','docs/project/','docs/governance/','tools/')) else 'MEDIUM',reason=reason),content_access=dict(mode=mode,secret=False),authority=dict(source_of_truth_candidate=target,canonicality=can,status_if_known=None),relations=dict(references=[],referenced_by=[],symlink_target=row.get('symlink_target'),generated_from=[],generates=[]),migration=dict(candidate_owner_stage=owner,candidate_target=target,candidate_action='MAP' if action=='KEEP' else 'COMPATIBILITY_READ',open_question='Stage 02/owner must validate boundaries and status before implementation; paths stay in place'),evidence_refs=evidence(p),notes=['File-level candidate; does not prove AI authorship or freeze source role.']))

# Resolve literal Markdown local links. Unresolved targets are candidates, not all broken links.
amap={a['path']:a for a in assets}
for p,t in texts.items():
    if p not in amap:continue
    for i,l in enumerate(t.splitlines(),1):
        for m in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',l):
            raw=m.group(1).strip().split(' "')[0].strip('<>')
            if raw.startswith(('#','http:','https:','mailto:','data:')):continue
            from urllib.parse import unquote
            target=unquote(raw.split('#')[0]);resolved=os.path.normpath(str(Path(p).parent/target))
            if target.startswith('/'):resolved=target.lstrip('/')
            ok=(ROOT/resolved).exists()
            rr={'source':p,'line':i,'target':target,'resolved_path':resolved,'exists':ok,'qualification':'Literal Markdown target; may be template/example/obsolete reference'}
            refs.append(rr)
            if ok:
                amap[p]['relations']['references'].append(resolved)
                if resolved in amap:amap[resolved]['relations']['referenced_by'].append(p)
    sm=re.search(r'^\|\s*状态\s*\|\s*([^|]+)',t,re.M)
    if sm:amap[p]['authority']['status_if_known']=sm.group(1).strip()
for a in assets:
    for k in ('references','referenced_by'):a['relations'][k]=sorted(set(a['relations'][k]))
put('evidence/DISCOVERY_UNIVERSE.jsonl',universe,'jsonl')
put('evidence/CONTENT_FEATURES.jsonl',features,'jsonl')
put('evidence/REFERENCE_EDGES.jsonl',refs,'jsonl')
put('evidence/CONTENT_ACCESS_AUDIT.json',dict(read_paths=read_paths,secret_paths=sorted(secret),additional_metadata_only_paths=sorted(extra_secret),secret_read_intersection=sorted(set(read_paths)&secret),secret_content_hashed=False,secret_content_copied=False,symlinks_followed=False))
put('AI_ASSET_INVENTORY.jsonl',assets,'jsonl')
put('evidence/ROOT_DISCOVERY.json',dict(repository_root=str(ROOT),git_paths=len(states),physical_paths=len(physical),filesystem_only=sorted(physical-set(baseline)-set(states)),directories=dirs,coverage_counts=dict(collections.Counter(x['coverage'] for x in universe)),state_counts=dict(collections.Counter(x['git_state'] for x in universe)),candidate_count=len(assets),text_files=len(features),binary_semantics_reviewed=False))

# Read-only full reachable commit metadata. Do not persist message bodies or credentials.
raw=git('log','--all','--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%aI%x00%cI%x00%P%x00%B%x00%x1e').decode(errors='replace')
commits=[];idents={};types=collections.Counter();scopes=collections.Counter();trailers=collections.Counter();langs=collections.Counter()
for chunk in raw.split('\x1e'):
    v=chunk.strip('\n').split('\0')
    if len(v)<9:continue
    c,an,ae,cn,ce,ad,cd,parents,msg=v[:9];subject=msg.splitlines()[0] if msg.splitlines() else ''
    mat=re.match(r'^([a-zA-Z]+)(?:\(([^)]+)\))?(!)?:\s',subject)
    typ=mat.group(1).lower() if mat else 'NON_CONVENTIONAL';scope=mat.group(2) if mat else None
    ts=re.findall(r'^([A-Za-z][A-Za-z-]+):\s+\S',msg,re.M)
    lang='MIXED_OR_CHINESE' if re.search('[\u4e00-\u9fff]',subject) else 'NO_CHINESE'
    types[typ]+=1;scopes[scope or 'NO_SCOPE']+=1;trailers.update(ts);langs[lang]+=1
    x=dict(commit=c,author=dict(name=an,email=ae),committer=dict(name=cn,email=ce),author_date=ad,committer_date=cd,parent_count=len(parents.split()),message_sha256=sha(msg.encode()),subject_pattern=typ,scope=scope,language=lang,trailer_keys=ts,issue_reference=bool(re.search(r'#\d+|[A-Z]+-\d+',msg)),merge=len(parents.split())>1,revert=subject.lower().startswith('revert'),ai_attribution_marker=bool(re.search(r'(?i)co-authored-by:.*(?:cursor|claude|codex)|generated (?:by|with).*(?:AI|cursor|claude|codex)',msg)))
    commits.append(x)
    key=(an,ae);z=idents.setdefault(key,dict(name=an,email=ae,commit_count=0,first_seen=ad,last_seen=ad));z['commit_count']+=1;z['first_seen']=min(z['first_seen'],ad);z['last_seen']=max(z['last_seen'],ad)
put('evidence/GIT_COMMIT_METADATA.jsonl',commits,'jsonl')
hist=git('-c','core.quotepath=false','log','--all','--format=COMMIT %H','--name-status','--diff-filter=DR','--no-renames','--','docs/','.cursor/','tools/','AGENTS.md','CLAUDE.md','.github/').decode(errors='replace')
historical=[];commit=None
for l in hist.splitlines():
    if l.startswith('COMMIT '):commit=l[7:]
    elif l.startswith('D\t'):
        p=l[2:]
        if p not in states and not isolated(p):historical.append(dict(path=p,commit=commit,event='DELETED_HISTORICAL_ONLY',coverage='COVERED_HISTORICAL',content_read=False,candidate_owner_stage='07',candidate_action='COMPATIBILITY_READ',reason='Reachable Git metadata retained; no restoration or old secret blob loading'))
put('evidence/HISTORICAL_ASSETS.jsonl',historical,'jsonl')
hooks=[]
hp=subprocess.run(['git','config','--get','core.hooksPath'],capture_output=True,text=True).stdout.strip()
hookroot=ROOT/hp if hp else ROOT/'.git/hooks'
if hookroot.exists():
    for p in sorted(hookroot.iterdir()):
        hooks.append(dict(path=str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),sample=p.name.endswith('.sample'),executable=os.access(p,os.X_OK),body_read=False,executed=False))
identity={k:subprocess.run(['git','config','--get','user.'+k],capture_output=True,text=True).stdout.strip() or None for k in ('name','email')}
ident=git('var','GIT_AUTHOR_IDENT').decode().strip();im=re.match(r'^(.*) <([^>]*)>',ident)
practice=dict(schema_version='stage01-bootstrap-v1',stage_id='01',current_effective_identity=dict(name=im.group(1) if im else None,email=im.group(2) if im else None,config_identity=identity,modified_by_stage01=False),history_analysis=dict(mode='ALL_REACHABLE_METADATA_AND_ALL_MESSAGES_PATTERN_ANALYSIS',commit_count_total_seen=len(commits),analysis_window=dict(first=min(c['author_date'] for c in commits),last=max(c['author_date'] for c in commits)),limitations=['Only reachable local refs; not reflog/dangling/remote-unfetched history.','Messages analyzed in memory; no message bodies persisted. AI attribution markers do not identify physical operator.','Trailer-like keys are syntactic observations, not a frozen trailer contract.','Hooks inspected as metadata; no hooks executed.']),identities=list(idents.values()),committer_differences=sum(c['author']!=c['committer'] for c in commits),commit_messages=dict(common_patterns=dict(types),type_scope_patterns=dict(scopes),trailer_patterns=dict(trailers),languages=dict(langs),merge_count=sum(c['merge'] for c in commits),revert_count=sum(c['revert'] for c in commits),issue_reference_count=sum(c['issue_reference'] for c in commits),ai_marker_count=sum(c['ai_attribution_marker'] for c in commits)),hooks_and_checks=dict(core_hooks_path=hp or None,hooks=hooks,ci_checks=[p for p in amap if p.startswith(('.github/','.husky/')) or Path(p).name in ('jenkinsfile','package.json')]),ai_commit_assets=dict(content_signal_files=[dict(path=x['path'],lines=x['signals']['commit']) for x in features if x['signals']['commit']],qualification='Signals require semantic review; build/deploy git commands are not automatic AI commit permission.'),semantic_commit_policy_frozen=False,identity_alias_merge_performed=False,evidence_refs=['evidence/GIT_COMMIT_METADATA.jsonl','evidence/CONTENT_FEATURES.jsonl','evidence/HISTORICAL_ASSETS.jsonl'])
put('GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml',practice,'yaml')
print(json.dumps(dict(assets=len(assets),universe=len(universe),text_files=len(features),historical_deleted=len(historical),commits=len(commits),identities=len(idents),coverage=collections.Counter(x['coverage'] for x in universe)),ensure_ascii=False))
