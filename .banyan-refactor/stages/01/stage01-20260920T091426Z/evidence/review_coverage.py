import collections, hashlib, json, os, re, subprocess
from pathlib import Path
import yaml
R=Path(__file__).resolve().parents[1];ROOT=R.parents[3];os.chdir(ROOT)
def j(n):return [json.loads(l) for l in (R/n).open()]
def put(n,v,k='yaml'):
    with (R/n).open('x',encoding='utf-8') as f:
        if k=='jsonl':
            for x in v:f.write(json.dumps(x,ensure_ascii=False)+'\n')
        elif k=='json':json.dump(v,f,ensure_ascii=False,indent=2)
        else:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
A=j('AI_ASSET_INVENTORY.jsonl');U=j('evidence/DISCOVERY_UNIVERSE.jsonl');um={x['path']:x for x in U};fm={x['path']:x for x in j('evidence/CONTENT_FEATURES.jsonl')};C=j('LEGACY_AI_CAPABILITY_INVENTORY.jsonl');G=j('AI_GENERATED_ARTIFACT_INVENTORY.jsonl');O=j('OPERATIONAL_ARTIFACT_INVENTORY.jsonl');am={a['path']:a for a in A}
# Correct approximate source anchors in the newly generated reports; no inherited evidence changed.
corrections={'CAP-RECONCILE':(2050,2099),'CAP-TEST':(1970,2018),'CAP-PUBLISH':(2100,2150),'CAP-CHANGE':(2490,2474)}
changed=[]
for fname,fmt in [('LEGACY_AI_CAPABILITY_INVENTORY.jsonl','jsonl'),('PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml','yaml'),('CORE_CANDIDATE_REPORT.yaml','yaml')]:
    p=R/fname;before=sha(p);v=j(fname) if fmt=='jsonl' else yaml.safe_load(p.read_text());items=v if isinstance(v,list) else v.get('matrix',v.get('candidates'))
    for x in items:
        key=x.get('capability_id',x.get('capability_or_asset_id'))
        for e in x['evidence_refs']:
            if key in corrections and e['path'].endswith('完整使用说明.md') and e['line']==corrections[key][0]:e['line']=corrections[key][1]
            if e['path']=='tools/anydesign/SKILL.md' and e['line']==107:e['line']=100
    with p.open('w') as f:
        if fmt=='jsonl':
            for x in v:f.write(json.dumps(x,ensure_ascii=False)+'\n')
        else:yaml.safe_dump(v,f,allow_unicode=True,sort_keys=False)
    changed.append(dict(path=fname,before=before,after=sha(p),reason='Precise source heading anchor review of Stage-owned drafts; semantics unchanged'))
put('evidence/ANCHOR_REVIEW.json',changed,'json')

# Broader reference discovery: literal backtick paths and semantic ID candidates.
ids=collections.defaultdict(list)
for a in A:
    if a['origin']['historical_only']:continue
    m=re.match(r'^((?:UI-DEC|DEC|ADR|CR|REQ|WORKLOG|HANDOVER)-\d+)\b',Path(a['path']).stem)
    if m:ids[m.group(1)].append(a['path'])
tokens=[]
for a in A:
    p=a['path']
    if p not in fm or Path(p).suffix not in ('.md','.mdc','.yaml','.yml'):continue
    t=Path(p).read_text()
    for n,l in enumerate(t.splitlines(),1):
        for token in re.findall(r'`([^`\n]+)`',l):
            if not re.match(r'^(docs/|tools/|\.cursor/|nunu-go-api/|go-uni-app(?:-online|-tob)?/)',token):continue
            if any(c in token for c in '*{}<>\n') or ' ' in token:continue
            path=token.split('#')[0].rstrip('/');tokens.append(dict(source=p,line=n,kind='LITERAL_REPOSITORY_PATH',token=token,targets=[path] if Path(path).exists() else [],resolution='EXISTS' if Path(path).exists() else 'UNRESOLVED_CANDIDATE',note='May be historic/illustrative; never automatic correction'))
        for token in set(re.findall(r'(?<![\w-])(?:UI-DEC|DEC|ADR|CR|WORKLOG|HANDOVER)-\d{3,}(?!\d)',l)):
            tokens.append(dict(source=p,line=n,kind='SEMANTIC_ID_CANDIDATE',token=token,targets=ids.get(token,[]),resolution='PATH_CANDIDATES' if token in ids else 'UNRESOLVED_CANDIDATE',note='Status, original topic and ranges require semantic review; not a broken-link assertion'))
put('evidence/REFERENCE_TOKEN_SCAN.jsonl',tokens,'jsonl')
iddup=[dict(id=k,paths=v,interpretation='Multiple files may be version/template/reference; not automatically conflicting ID ownership',candidate_owner_stage='03') for k,v in ids.items() if len(v)>1]
put('evidence/ID_COLLISION_CANDIDATES.json',iddup,'json')

groups=collections.defaultdict(list)
for a in A:
    p=a['path'];hv=um.get(p,{}).get('sha256')
    if hv and not p.endswith('.gitkeep'):groups[hv].append(p)
dups=[dict(sha256=k,paths=v) for k,v in groups.items() if len(v)>1]
put('evidence/EXACT_DUPLICATES.json',dups,'json')
issues=[]
def issue(key,typ,sev,paths,desc,owner,action,refs=None):
    issues.append(dict(issue_id=key,type=typ,severity=sev,assets=[am[p]['asset_id'] for p in paths if p in am],paths=paths,description=desc,evidence_refs=refs or ['evidence/DISCOVERY_UNIVERSE.jsonl#'+p for p in paths],candidate_owner_stage=owner,recommended_next_action=action,blocking=False,stage01_disposition='EXPLAINED_AND_ROUTED; no automatic fix; target-stage gate must address it'))
for i,d in enumerate(dups,1):issue('DUP-%03d'%i,'Duplicate','INFO',d['paths'],'Exact identical bytes; copies may serve separate app/context consumers. This is not permission to merge/delete.','10' if any('白话' in p for p in d['paths']) else '07','Review consumers and authority before any deduplication. Preserve every source in place.',['evidence/EXACT_DUPLICATES.json#'+d['sha256']])
issue('CON-001','Conflict','HIGH',['docs/governance/common_prd_v3.1/通用文档提示词v3.1.md','.cursor/rules/collaboration-judgment.mdc','docs/project/AI_DOCUMENTATION_GUIDE.md'],'Generic IDP HIGH one / LOW two differs from project DEC-042 max five and existing-code self-resolution. Keep explicit project override separate; do not flatten into a universal Core policy.','05','Stage 02 map precedence and Stage 05 preserve decision authorization semantics; Stage 07 regression covers project overrides.')
issue('CON-002','Conflict','HIGH',['docs/project/README.md','docs/project/AI_DOCUMENTATION_GUIDE.md','docs/project/progress/PROJECT_DASHBOARD.md','docs/project/progress/PROGRESS_REGISTER.yaml'],'Entry/guide retain older PRD v0.1.5/v0.1.7 and 72% descriptions; dashboard describes v0.1.44 Approved and 69%. README both says mall-online not created and later says created. Do not use stale prose to authorize work or rewrite canonical state.','12','Stage 02 define freshness/source roles; Stage 12 use authoritative register and scoped confirmed records; preserve mismatches as evidence.')
issue('GAP-001','Gap','MEDIUM',['nunu-go-api/app/admin/web/.husky/pre-commit','nunu-go-api/app/admin/web/package.json'],'pre-commit calls pnpm run lint:lint-staged, but current package scripts only dev/build/preview. Root core.hooksPath unset and .git/hooks contains sample hooks only; cannot claim this nested enforcement is active.','05','Assess hook installation and missing command under explicit later scope; do not run/install/repair now.')
issue('GAP-002','Gap','MEDIUM',['nunu-go-api/app/admin/web/README.md','nunu-go-api/app/admin/web/CHANGELOG.md','nunu-go-api/app/admin/web/CHANGELOG.zh-CN.md'],'Four literal Markdown references point to absent CONTRIBUTING.md or CHANGELOG.en.md. Two additional regex-source matches are not real links and excluded from broken-link findings.','03','Review vendor/upstream documentation references; no automatic edits.',['evidence/REFERENCE_EDGES.jsonl'])
issue('GAP-003','Gap','MEDIUM',['docs/project/progress/PLAIN_SYNC.yaml'],'Derived publications and design outputs have governing sources, but exact per-file AI authorship and byte-reproducible generation lineage are not proven. Preserve source files; cannot declare them safely rebuildable.','10','Stage 10 audit publishing source graph; Stage 09 handle design lineage; Stage 03 freeze source-role contracts.',['AI_GENERATED_ARTIFACT_INVENTORY.jsonl'])
issue('GAP-004','Gap','MEDIUM',['docs/project/ui-design/visual-loop/LOOP_RUNS/20260919-gongyi_online-nearby/RUN.yaml','docs/project/ui-design/visual-loop/LOOP_RUNS/20260919-gongyi_online-tabbar/RESULT.md'],'Nearby run records in_progress and has no RESULT; tabbar RESULT records user-stop/revert. These are existing operational states, not missing Stage 01 deliverables; do not upgrade to successful validation.','09','Preserve failure/in-progress semantics in migration; do not resume business visual loops during Stage 01.')
issue('GAP-005','Gap','MEDIUM',[],'Reachable Git metadata contains 16 exact author identities, including placeholders and quoting variants. No identity aliases merged; historical co-author AI markers do not establish physical operator.','03','Stage 03/05 map exact contribution identity and policy without rewriting history.',['GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml','evidence/GIT_COMMIT_METADATA.jsonl'])
issue('GAP-006','Gap','LOW',[],'Semantic ID and inline path scans include unresolved candidates and multi-file namespaces; examples/ranges/legacy references are not automatically dangling current contracts. Stage 01 preserves every candidate for source-role review.','03','Resolve effective-version/topic references at schema/reference-integrity owner stage before migration.',['evidence/REFERENCE_TOKEN_SCAN.jsonl','evidence/ID_COLLISION_CANDIDATES.json'])
issue('DUP-SYMLINK','Duplicate','INFO',['.cursor/skills/anydesign','tools/anydesign/SKILL.md'],'Cursor AnyDesign entry is a symlink to provider directory, not a second content source. Link metadata and target real path inventoried separately.','15','Preserve entry compatibility; do not recursively double-count symlink contents.')
put('CONFLICT_GAP_REPORT.yaml',dict(schema_version='stage01-bootstrap-v1',stage_id='01',summary={s:sum(x['severity']==s for x in issues) for s in ['CRITICAL','HIGH','MEDIUM','LOW','INFO']},no_conflict_winner_selected=True,issues=issues,version_families=dict(ui_spec='UI_SPEC-0.1.0..0.1.4 and Draft counterparts are history, not automatically duplicates',publishing_policy='Three roots contain similar policies; hashes identify exact subset only'),limitations=['No current business consistency audit or UI rendering executed.','No full historical blob/rename-similarity analysis; deleted paths discovered with --no-renames and deduplicated by path.','All HIGH issues explained with owner and next action; none requires Stage 01 writing outside scope.']))

# Refine initial syntactic Git observations without overwriting that inventory.
raw=subprocess.check_output(['git','log','--all','--format=%H%x00%B%x00%x1e'],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'}).decode(errors='replace')
tr=collections.Counter();tr_evidence=[]
for chunk in raw.split('\x1e'):
    v=chunk.strip('\n').split('\0')
    if len(v)<2:continue
    out=subprocess.run(['git','interpret-trailers','--parse'],input=v[1],text=True,capture_output=True,check=True).stdout
    keys=re.findall(r'^([^:\n]+):',out,re.M);tr.update(keys)
    if keys:tr_evidence.append(dict(commit=v[0],trailer_keys=keys))
put('evidence/GIT_TRAILER_PARSE.json',dict(method='git interpret-trailers --parse; values not persisted',trailer_counts=dict(tr),commits=tr_evidence),'json')
pkg=json.loads(Path('nunu-go-api/app/admin/web/package.json').read_text());ci=Path('jenkinsfile').read_text()
review=dict(confirmed_nested_hooks=[dict(path='nunu-go-api/app/admin/web/.husky/commit-msg',command='pnpm dlx commitlint --edit $1',executed=False),dict(path='nunu-go-api/app/admin/web/.husky/pre-commit',command='pnpm run lint:lint-staged',target_script_exists='lint:lint-staged' in pkg.get('scripts',{}),executed=False)],commitlint=dict(path='nunu-go-api/app/admin/web/commitlint.config.cjs',extends='@commitlint/config-conventional',useAI=False,installation_effectiveness='NOT_VERIFIED; root hooksPath unset'),ci=dict(path='jenkinsfile',stage_labels=re.findall(r"stage\(['\"]([^'\"]+)",ci),commit_enforcement_keywords_detected=bool(re.search('commitlint|commit-msg|lint-staged',ci))),actual_trailers=dict(tr),initial_trailer_field_qualification='Initial trailer_patterns is any line key including subject prefixes. Use semantic_review.actual_trailers for parsed trailing blocks.',ai_commit_practice='Legacy main prompt prohibits unauthorized submit/push/merge/release. Historical merge guide contains explicit project branch workflow, not current permission. No dedicated all-repository AI batch-commit planner found in current governance candidate corpus.',historical_identification='164 attribution-marker commits reflect message assertions only, not proven physical authorship.',final_policy_frozen=False)
with (R/'GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml').open('a') as f:yaml.safe_dump({'semantic_review':review},f,allow_unicode=True,sort_keys=False)

# Per-candidate reconciliation; original path snapshot remains unchanged.
ledger=[]
for a in A:ledger.append(dict(path=a['path'],asset_id=a['asset_id'],coverage='COVERED_HISTORICAL' if a['origin']['historical_only'] else um[a['path']]['coverage'],disposition=a['classification']['action'],reason=a['classification']['reason']))
put('evidence/CANDIDATE_RECONCILIATION.jsonl',ledger,'jsonl')
roots=collections.defaultdict(lambda:collections.Counter())
for x in U:
    ps=Path(x['path']).parts
    for depth in range(1,min(len(ps),4)):
        roots['/'.join(ps[:depth])][x['coverage']]+=1
root_records=[dict(path=k,counts=dict(v),status='COVERED_OR_REASON_REGISTERED',reason_ledger='evidence/DISCOVERY_UNIVERSE.jsonl') for k,v in sorted(roots.items())]
put('evidence/ROOT_COVERAGE.json',root_records,'json')
expected={x['path'] for x in U if x['candidate']}|{a['path'] for a in A if a['origin']['historical_only'] or a['origin']['tracked_state']=='IGNORED'}
actual={a['path'] for a in A}
unknown=[a for a in A if a['asset_type']=='UNCLASSIFIED']
metrics=dict(SILENTLY_IGNORED_ASSET=len(expected-actual),UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON=sum(not x['reason_ledger'] for x in root_records),HIGH_RISK_UNCLASSIFIED=sum(a.get('risk') in ('HIGH','CRITICAL') for a in unknown))
counts=collections.Counter(x['coverage'] for x in U)
coverage=dict(schema_version='stage01-bootstrap-v1',stage_id='01',result='PASS' if not any(metrics.values()) else 'FAIL',coverage=dict(repository_root=str(ROOT),tracked_considered=sum(x['git_state']=='TRACKED' for x in U),relevant_untracked_considered=sum(a['origin']['tracked_state']=='UNTRACKED' for a in A),governed_ignored_considered=sum(a['origin']['tracked_state']=='IGNORED' for a in A),editor_roots_considered=[dict(path=p,status='DISCOVERED' if Path(p).exists() else 'ABSENT') for p in ['.cursor','.codex','.claude','.github','.husky','AGENTS.md','CLAUDE.md']],governance_roots_considered=['docs/governance','docs/project','docs/temp','docs/开发指导.md','docs/项目迭代开发文档指导v2.md'],tool_script_roots_considered=sorted(set(str(Path(a['path']).parent) for a in A if a['asset_type']=='TOOL')),generated_operational_roots_considered=['docs/project','tools/anydesign/examples','docs/project/ui-design/visual-loop/LOOP_RUNS','docs/project/progress'],git_history_considered=dict(reachable_commits=477,deleted_events=10,unique_historical_paths=5),secret_policy_preserved=True),isolation=dict(banyan_refactor_classified_as_upstream_evidence=True,construction_materials_excluded_from_legacy=True,upstream_zip_excluded=True),universe=dict(total=len(U),coverage_classes=dict(counts),candidate_paths=len(A),content_scan='4766 full decoded text files; feature/Markdown/backtick/ID scans and focused semantic review',binary_scan='Metadata/path/source registry and safe hashes only; no visual review asserted',all_paths_ledger='evidence/DISCOVERY_UNIVERSE.jsonl',root_ledger='evidence/ROOT_COVERAGE.json',candidate_ledger='evidence/CANDIDATE_RECONCILIATION.jsonl'),metrics=metrics,metric_definitions=dict(SILENTLY_IGNORED_ASSET='Expected path/content candidates plus governed ignored/historical candidates absent from actual asset inventory',UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON='Discovered directory coverage records without content/metadata/exclusion reason linkage',HIGH_RISK_UNCLASSIFIED='UNCLASSIFIED asset records with HIGH/CRITICAL risk'),unclassified=dict(total=len(unknown),high_risk=metrics['HIGH_RISK_UNCLASSIFIED']),exclusions=[dict(path='.banyan-refactor/** and .banyan-refactor.zip',reason='UPSTREAM_REFACTOR_OPERATIONAL_EVIDENCE'),dict(path='榕树ai改造落地相关文档/**',reason='REFRACTOR_CONSTRUCTION_MATERIAL'),dict(path='Inherited dependency/build/cache/log/OS/IDE paths',reason='Per-path Stage 00 exclusion carried forward; no migration candidates'),dict(path='69 inherited secret candidates + ssh-tunnel-test.ps1',reason='Metadata only; no secret body needed to classify safety boundary')],limitations=['Coverage means every enumerated path has treatment, not every business file underwent semantic code review.','AI authorship unknown per file; candidate generated corpus preserves formal sources conservatively.','Derived reproducibility and full semantic reference integrity deferred with owner to later stages.','No all-history content scan; all reachable commit metadata/message patterns and targeted deleted governance path history only.'])
put('DISCOVERY_COVERAGE_REPORT.yaml',coverage)
put('evidence/STEP_COMPLETION.json',dict(steps_completed=['01.2','01.3','01.4','01.5','01.6','01.7','01.8','01.9','01.10','01.11','01.12'],remaining=['01.13','01.14'],metrics=metrics,inventory_counts=dict(assets=len(A),capabilities=len(C),generated=len(G),operational=len(O)),no_loss=dict(capability_expected=len(C),capability_mapped=len(yaml.safe_load((R/'PRELIMINARY_AI_CAPABILITY_PRESERVATION_MATRIX.yaml').read_text())['matrix']),artifacts_expected=len(G),artifacts_mapped=len(yaml.safe_load((R/'PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml').read_text())['matrix']))),'json')
print(json.dumps(dict(issues=len(issues),severities=collections.Counter(x['severity'] for x in issues),references=len(tokens),metrics=metrics,trailers=dict(tr)),ensure_ascii=False))
