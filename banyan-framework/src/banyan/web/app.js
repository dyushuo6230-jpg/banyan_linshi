const $ = (id) => document.getElementById(id);
const show = (id, value) => { $(id).textContent = JSON.stringify(value, null, 2); };
let currentPlan = null;

async function api(path, options = {}) {
  const response = await fetch(path, {headers: {'Content-Type': 'application/json'}, ...options});
  const value = await response.json();
  if (!response.ok) throw new Error(value.detail || value.error || `HTTP ${response.status}`);
  return value;
}

async function loadDashboard() {
  const [status, policy, safety, providers, stages, readiness, trace] = await Promise.all([
    api('/api/status'), api('/api/policy'), api('/api/project-safety'), api('/api/providers'),
    api('/api/stages?offset=0&limit=25'), api('/api/activation-readiness'), api('/api/trace?offset=0&limit=25')
  ]);
  $('runtime-health').textContent = status.runtime_health;
  $('metric-runtime').textContent = status.runtime_health;
  $('metric-mode').textContent = status.execution_mode;
  $('metric-policy').textContent = status.compiled_policy_hash.slice(0, 12);
  $('metric-activation').textContent = status.activation_state;
  show('policy-output', policy); show('safety-output', safety); show('providers-output', providers);
  show('stages-output', stages); show('activation-output', readiness); show('trace-output', trace);
  const blockers = $('blockers'); blockers.replaceChildren(...status.open_blockers.map(value => {
    const chip = document.createElement('span'); chip.textContent = value; return chip;
  }));
}

$('preflight-button').addEventListener('click', async () => {
  try {
    const value = await api('/api/preflight', {method: 'POST', body: JSON.stringify({
      action_id: $('action-id').value, action_type: $('action-type').value,
      precondition_results: {evidence_complete:true,impact_reviewed:true,authorization_valid:true,secret_check_passed:true,freshness_valid:true,rollback_ready:true}
    })}); show('preflight-output', value);
  } catch (error) { show('preflight-output', {error: error.message}); }
});

$('plan-button').addEventListener('click', async () => {
  try {
    currentPlan = await api('/api/commit/plan', {method:'POST', body:JSON.stringify({classifications:JSON.parse($('classifications').value)})});
    show('plan-output', currentPlan);
  } catch (error) { show('plan-output', {error:error.message}); }
});

$('dryrun-button').addEventListener('click', async () => {
  if (!currentPlan) { show('dryrun-output', {error:'Build a plan first.'}); return; }
  try {
    const value = await api('/api/commit/dry-run', {method:'POST', body:JSON.stringify({plan:{groups:currentPlan.groups,classifications:currentPlan.classifications,blocked_paths:currentPlan.blocked_paths,leftovers:currentPlan.leftovers},authorization_ref:$('authorization-ref').value || null})});
    show('dryrun-output', value);
  } catch (error) { show('dryrun-output', {error:error.message}); }
});

$('provenance-button').addEventListener('click', async () => {
  try { show('provenance-output', await api(`/api/provenance/${encodeURIComponent($('provenance-id').value)}`)); }
  catch (error) { show('provenance-output', {error:error.message}); }
});

loadDashboard().catch(error => { $('runtime-health').textContent = 'ERROR'; show('policy-output', {error:error.message}); });
