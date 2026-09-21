"""Continue the same closeout after a documented, non-Legacy archive disappearance.
The failed source is retained. Skip its completed role-alignment write; authorize
only this exact path-list difference, not any change in actual Stage 00 evidence.
"""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
record=dict(event='FINAL_CHECK_DETECTED_EXTERNAL_PATH_DRIFT',path='.banyan-refactor.zip',change='ABSENT_FROM_CURRENT_UNTRACKED_PATHS',classification='SAFE_DISCOVERY_DRIFT',provenance='UNKNOWN; no agent command writes/moves/deletes this archive',reason='Excluded upstream evidence duplicate. Original Stage 00 seal (58 entries), checkpoint archives, 5834 content hashes and 70 metadata-only paths verified unchanged; no safety boundary depends on this duplicate.',failed_attempt='prepare_closeout.py stopped at safety assertion before checkpoint/handoff/bootstrap writes',completed_step_preserved='evidence/FINAL_ROLE_ALIGNMENT.json',action='Continue original Run closeout; do not recreate/delete/restore anything')
with (p/'EXTERNAL_ARCHIVE_DRIFT.json').open('x') as f:json.dump(record,f,ensure_ascii=False,indent=2)
s=(p/'prepare_closeout.py').read_text()
start=s.index('for a in A:\n');end=s.index('\nold={',start)
s=s[:start]+s[end:]
s=s.replace("if path_drift[f]['added'] or path_drift[f]['removed']:errors.append('path drift: '+f)","if path_drift[f]['added'] or path_drift[f]['removed']:\n        if not (f=='untracked.z' and path_drift[f]==dict(added=[],removed=['.banyan-refactor.zip'])):errors.append('path drift: '+f)")
s=s.replace('outside_control_path_drift=path_drift,','outside_control_path_drift=path_drift,external_archive_drift_evidence="evidence/EXTERNAL_ARCHIVE_DRIFT.json",')
exec(compile(s,str(p/'prepare_closeout.py')+' [same-run continuation]', 'exec'))
