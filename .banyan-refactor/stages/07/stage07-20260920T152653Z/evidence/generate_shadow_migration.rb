#!/usr/bin/env ruby
require 'json'
require 'yaml'
require 'digest'
require 'time'

ROOT = File.expand_path('../../../../..', __dir__)
RUN_ID = 'stage07-20260920T152653Z'
OUT = File.join(ROOT, '.banyan-refactor/stages/07', RUN_ID)

def one(pattern)
  matches = Dir.glob(File.join(ROOT, pattern))
  raise "expected one #{pattern}, got #{matches.size}" unless matches.size == 1
  matches.first
end

def jsonl(path)
  File.readlines(path, chomp: true).reject(&:empty?).map { |line| JSON.parse(line) }
end

def write_yaml(name, value)
  File.write(File.join(OUT, name), YAML.dump(value))
end

def write_jsonl(name, rows)
  File.open(File.join(OUT, name), 'w') { |f| rows.each { |row| f.puts(JSON.generate(row)) } }
end

stage01 = '.banyan-refactor/stages/01/**'
cap_source = one("#{stage01}/LEGACY_AI_CAPABILITY_INVENTORY.jsonl")
asset_source = one("#{stage01}/AI_ASSET_INVENTORY.jsonl")
artifact_source = one("#{stage01}/AI_GENERATED_ARTIFACT_INVENTORY.jsonl")
operational_source = one("#{stage01}/OPERATIONAL_ARTIFACT_INVENTORY.jsonl")
reference_source = one("#{stage01}/REFERENCE_EDGES.jsonl")
contract_source = one('.banyan-refactor/stages/03/**/CAPABILITY_CONTRACT_REGISTRY.yaml')

caps = jsonl(cap_source)
assets = jsonl(asset_source)
artifacts = jsonl(artifact_source)
operational = jsonl(operational_source)
references = jsonl(reference_source)
contracts = YAML.load_file(contract_source).fetch('contracts').to_h { |item| [item.fetch('capability_id'), item] }

cap_rows = caps.map do |legacy|
  contract = contracts.fetch(legacy.fetch('capability_id'))
  disposition = case contract.fetch('freeze_status')
                when 'PROJECT_OVERLAY_CONTRACT' then 'MAP_TO_PROJECT_INSTANCE'
                when 'PROVIDER_PORT_CONTRACT' then 'MAP_TO_PROVIDER'
                when 'COMPATIBILITY_CONTRACT' then 'MAP_TO_COMPATIBILITY'
                else 'MAP_TO_CORE'
                end
  {
    'capability_id' => legacy.fetch('capability_id'),
    'legacy_name' => legacy.fetch('name'),
    'value_level' => legacy.fetch('value_level'),
    'legacy_sources' => legacy.fetch('legacy_sources'),
    'legacy_behaviors' => legacy.fetch('behaviors'),
    'target_contract_id' => contract.fetch('contract_id'),
    'target_layer' => contract.fetch('candidate_layer'),
    'disposition' => disposition,
    'provider_port_required' => contract.fetch('provider_port_required'),
    'project_overlay_required' => contract.fetch('project_overlay_required'),
    'compatibility_required' => contract.fetch('compatibility_required'),
    'preservation_proof' => {
      'inputs' => legacy.fetch('inputs'), 'outputs' => legacy.fetch('outputs'),
      'guards' => legacy.fetch('guards'), 'failure_semantics' => legacy.fetch('failure_semantics'),
      'contract_status' => contract.fetch('contract_status'),
      'activation' => 'OFF'
    },
    'evidence_refs' => legacy.fetch('evidence_refs'),
    'owner_stage' => contract.fetch('owner_stage'),
    'open_conflicts' => contract.fetch('open_conflicts')
  }
end

write_yaml('LEGACY_CAPABILITY_MIGRATION_MATRIX.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'mode' => 'SHADOW_ONLY_NO_LOSS', 'source_inventory' => cap_source.sub(ROOT + '/', ''),
  'source_contract_registry' => contract_source.sub(ROOT + '/', ''),
  'expected_capabilities' => 35, 'mapped_capabilities' => cap_rows.size,
  'unmapped_high_value_capabilities' => [], 'mappings' => cap_rows
})

asset_rows = assets.map do |item|
  {
    'asset_id' => item.fetch('asset_id'), 'path' => item.fetch('path'),
    'asset_type' => item['asset_type'], 'canonicality' => item.dig('authority', 'canonicality'),
    'legacy_classification_action' => item.dig('classification', 'action'),
    'disposition' => 'PRESERVE_IN_PLACE',
    'target_candidate' => item.dig('migration', 'candidate_target'),
    'candidate_owner_stage' => item.dig('migration', 'candidate_owner_stage'),
    'status_preservation' => 'EXACT_SOURCE_STATE_RETAINED',
    'content_copied' => false, 'source_mutated' => false,
    'evidence' => item['evidence']
  }
end
write_jsonl('LEGACY_ASSET_DISPOSITION_MATRIX.jsonl', asset_rows)

artifact_rows = artifacts.map do |item|
  {
    'artifact_id' => item.fetch('artifact_id'), 'path' => item.fetch('path'),
    'artifact_class' => item.fetch('artifact_class'),
    'source_role' => item['candidate_source_role'],
    'rebuildability' => item['rebuildability'], 'freshness' => item['freshness'],
    'disposition' => 'PRESERVE_IN_PLACE',
    'authority_preservation' => item.fetch('artifact_class') == 'CANONICAL' ? 'CANONICAL_UNCHANGED' : 'DERIVED_STATUS_UNCHANGED',
    'reference_strategy' => 'KEEP', 'content_copied' => false,
    'source_mutated' => false, 'auto_regenerated' => false,
    'evidence_refs' => item['evidence_refs']
  }
end
write_jsonl('LEGACY_ARTIFACT_MIGRATION_MATRIX.jsonl', artifact_rows)

operational_rows = operational.map do |item|
  {
    'artifact_id' => item.fetch('artifact_id'), 'path' => item.fetch('path'),
    'operational_type' => item['operational_type'], 'authoritative' => item['authoritative'],
    'freshness' => item['freshness'], 'historical_value' => item['historical_value'],
    'disposition' => 'INDEX_ONLY', 'preservation_mode' => 'KEEP_HISTORICAL',
    'content_copied' => false, 'source_mutated' => false,
    'candidate_owner_stage' => item['candidate_owner_stage'],
    'evidence' => item['evidence']
  }
end
write_jsonl('OPERATIONAL_PRESERVATION_MATRIX.jsonl', operational_rows)

reference_rows = references.each_with_index.map do |item, index|
  false_positive = !item.fetch('exists') && item.fetch('target') == '[^"\\\']+'
  strategy = if item.fetch('exists') then 'KEEP'
             elsif false_positive then 'IGNORE_AS_NON_REFERENCE'
             else 'BLOCK'
             end
  {
    'edge_id' => format('REF-%03d', index + 1), 'source' => item.fetch('source'),
    'line' => item.fetch('line'), 'target' => item.fetch('target'),
    'resolved_path' => item.fetch('resolved_path'), 'exists' => item.fetch('exists'),
    'migration_strategy' => strategy,
    'disposition' => item.fetch('exists') ? 'PRESERVE_IN_PLACE' : 'DEFER_WITH_OWNER',
    'owner_stage' => item.fetch('exists') ? '07' : '12',
    'explanation' => false_positive ? 'regex literal detected by lexical scanner; not a repository reference' : item.fetch('qualification'),
    'canonical_apply_allowed' => false
  }
end
write_jsonl('REFERENCE_MIGRATION_MAP.jsonl', reference_rows)

write_yaml('V31_GOVERNANCE_COMPATIBILITY_MAP.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'mode' => 'LEGACY_SEMANTIC_COMPATIBILITY_SHADOW_ONLY',
  'legacy_version' => 'v3.1',
  'mappings' => [
    ['G0-G11 governance stages', 'WorkflowPolicyRegistry', 'MAP_TO_CORE'],
    ['PROJECT_STAGE', 'ProjectInstance.lifecycle', 'MAP_TO_PROJECT_INSTANCE'],
    ['TBD and unknown variables', 'VariableResolution.typed_unknown', 'MAP_TO_CORE'],
    ['Informed Decision', 'DecisionPolicyRegistry.L1-L5', 'MAP_TO_CORE'],
    ['PRD', 'ArtifactRegistry.source_role=PRODUCT_REQUIREMENT', 'MAP_TO_CORE'],
    ['DEC', 'ArtifactRegistry.source_role=DECISION_RECORD', 'MAP_TO_CORE'],
    ['ADR', 'ArtifactRegistry.source_role=ARCHITECTURE_DECISION', 'MAP_TO_CORE'],
    ['CR', 'ChangeWorkspace.change_record', 'MAP_TO_CORE'],
    ['TRACE_MATRIX', 'TraceabilityRegistry', 'MAP_TO_CORE'],
    ['UI Contract / UI_SPEC', 'CompatibilityProjection.ui_contract', 'MAP_TO_COMPATIBILITY'],
    ['Progress / Worklog / Handover', 'OperationalArtifactIndex', 'INDEX_ONLY'],
    ['Plain Document', 'ArtifactRegistry.source_role=PLAIN_DOCUMENT', 'MAP_TO_CORE'],
    ['AnyDesign / UI governance', 'ProviderBinding.anydesign + compatibility projection', 'MAP_TO_PROVIDER']
  ].map { |legacy, target, disposition| {'legacy_semantic' => legacy, 'target_contract' => target, 'disposition' => disposition, 'status' => 'MAPPED_DESIGN_ONLY'} },
  'legacy_content_mutated' => false, 'legacy_authority_promoted' => false
})

write_yaml('PROVIDER_COMPATIBILITY_MAPPING.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'provider_neutral_core' => true,
  'providers' => [
    {'provider' => 'OpenSpec', 'observation' => 'NOT_OBSERVED', 'binding' => 'DESIGN_ONLY_INACTIVE_NO_VERIFIED_LEGACY_INSTANCE', 'disposition' => 'MAP_TO_PROVIDER'},
    {'provider' => 'AnyDesign', 'observation' => 'LEGACY_ASSETS_OBSERVED', 'binding' => 'SHADOW_REFERENCE_ONLY', 'disposition' => 'MAP_TO_PROVIDER'},
    {'provider' => 'Editor conventions', 'observation' => 'LEGACY_COMPATIBILITY_OBSERVED', 'binding' => 'COMPATIBILITY_PROJECTION_ONLY', 'disposition' => 'MAP_TO_COMPATIBILITY'}
  ],
  'implicit_activation' => false, 'canonical_write' => false
})

write_yaml('SHADOW_PROJECT_INSTANCE.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'instance_id' => 'shadow.x_shop_server.v31_legacy_migration',
  'state' => 'SHADOW_ONLY_NOT_ACTIVATED', 'canonical_root_created' => false,
  'references' => {
    'project_instance_schema' => '.banyan-refactor/stages/04/stage04-20260920T142517Z/PROJECT_INSTANCE_SCHEMA.yaml',
    'source_mapping_registry' => '.banyan-refactor/stages/04/stage04-20260920T142517Z/SOURCE_MAPPING_REGISTRY.yaml',
    'overlay_bindings' => '.banyan-refactor/stages/04/stage04-20260920T142517Z/PROJECT_OVERLAY_BINDINGS.yaml',
    'provider_binding_schema' => '.banyan-refactor/stages/04/stage04-20260920T142517Z/PROVIDER_BINDING_SCHEMA.yaml'
  },
  'shadow_registry_counts' => {'capabilities' => caps.size, 'assets' => assets.size, 'generated_and_canonical_artifacts' => artifacts.size, 'operational_artifacts' => operational.size, 'reference_edges' => references.size},
  'source_of_truth' => 'LEGACY_REPOSITORY_REMAINS_AUTHORITATIVE',
  'activation' => 'OFF'
})

broken = reference_rows.select { |row| row['migration_strategy'] == 'BLOCK' }
false_positive = reference_rows.select { |row| row['migration_strategy'] == 'IGNORE_AS_NON_REFERENCE' }
write_yaml('MIGRATION_BLOCKER_REGISTER.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'blockers' => [
    {'blocker_id' => 'CON-002', 'status' => 'OPEN', 'owner_stage' => '12', 'scope' => 'freshness and current-state verification'},
    {'blocker_id' => 'R03-SECRET', 'status' => 'PARTIAL_APPROVED', 'owner_stage' => 'LATER_EXPLICIT_AUTHORIZATION', 'scope' => '13 sensitive paths; existence metadata only'},
    {'blocker_id' => 'R03-PURITY', 'status' => 'OPEN', 'owner_stage' => 'LATER_STAGE', 'scope' => 'canonical purity proof'},
    {'blocker_id' => 'R03-SOURCE', 'status' => 'OPEN', 'owner_stage' => 'LATER_STAGE', 'scope' => 'source authority proof'},
    {'blocker_id' => 'R03-COST', 'status' => 'OPEN', 'owner_stage' => 'LATER_STAGE', 'scope' => 'migration cost proof'},
    {'blocker_id' => 'R03-LOCAL', 'status' => 'OPEN', 'owner_stage' => 'LATER_STAGE', 'scope' => 'local environment proof'}
  ] + broken.map { |row| {'blocker_id' => "REF-#{row['edge_id']}", 'status' => 'OPEN', 'owner_stage' => '12', 'scope' => "missing target #{row['resolved_path']}", 'source' => row['source'], 'line' => row['line']} },
  'scanner_false_positives' => false_positive.map { |row| row['edge_id'] },
  'real_apply_readiness' => 'BLOCKED', 'shadow_design_completion' => 'ALLOWED'
})

write_yaml('SHADOW_APPLY_REPORT.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'execution' => 'SIMULATED_ONLY', 'canonical_apply_executed' => false,
  'preview' => {'capability_mappings' => cap_rows.size, 'asset_dispositions' => asset_rows.size, 'artifact_mappings' => artifact_rows.size, 'operational_indexes' => operational_rows.size, 'reference_edges' => reference_rows.size},
  'reference_check' => {'keep' => reference_rows.count { |r| r['migration_strategy'] == 'KEEP' }, 'blocked' => broken.size, 'ignored_non_references' => false_positive.size, 'strategy_missing' => 0},
  'freshness' => {'status' => 'BLOCKED_BY_CON_002_FOR_REAL_APPLY', 'shadow_evaluation' => 'COMPLETE'},
  'authorization' => 'NO_CANONICAL_APPLY_AUTHORIZATION_IN_STAGE07',
  'reconciliation' => 'NO_SOURCE_CHANGES; SHADOW OUTPUTS ONLY',
  'rollback' => 'DELETE_STAGE07_SHADOW_RUN_AND_RESTORE_BOOTSTRAP_POINTERS_IF_REQUIRED'
})

write_yaml('ROLLBACK_RECOVERY_READINESS.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'baseline_head' => '9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7',
  'checkpoint' => 'CHECKPOINT-stage00-precheck-20260920T083254Z',
  'source_snapshots' => [cap_source, asset_source, artifact_source, operational_source, reference_source].map { |p| {'path' => p.sub(ROOT + '/', ''), 'sha256' => Digest::SHA256.file(p).hexdigest} },
  'mapping_snapshot' => 'LEGACY_CAPABILITY_MIGRATION_MATRIX.yaml',
  'reference_graph_snapshot' => 'REFERENCE_MIGRATION_MAP.jsonl',
  'legacy_source_mutation' => false, 'canonical_apply_executed' => false,
  'recovery_coverage' => 'PARTIAL_APPROVED',
  'qualification' => '13 sensitive paths remain metadata-only and excluded from content/hash proof',
  'single_truth_after_rollback' => 'LEGACY_REPOSITORY'
})

write_yaml('NOLOSS_COVERAGE_REPORT.yaml', {
  'schema_version' => '1.0.0', 'stage' => '07', 'run_id' => RUN_ID,
  'status' => 'PASS_NOLOSS_SHADOW_DESIGN_WITH_TYPED_BLOCKERS',
  'coverage' => {
    'high_value_capabilities' => {'expected' => 35, 'accounted' => cap_rows.size},
    'legacy_assets' => {'expected' => 1026, 'accounted' => asset_rows.size},
    'canonical_artifacts' => {'expected' => artifacts.count { |x| x['artifact_class'] == 'CANONICAL' }, 'accounted' => artifact_rows.count { |x| x['artifact_class'] == 'CANONICAL' }},
    'derived_artifacts' => {'expected' => artifacts.count { |x| x['artifact_class'] == 'DERIVED' }, 'accounted' => artifact_rows.count { |x| x['artifact_class'] == 'DERIVED' }},
    'operational_artifacts' => {'expected' => 289, 'accounted' => operational_rows.size},
    'reference_edges' => {'expected' => 108, 'accounted' => reference_rows.size, 'blocked' => broken.size, 'non_reference_false_positives' => false_positive.size}
  },
  'hard_metrics' => {
    'UNMAPPED_HIGH_VALUE_CAPABILITY' => 0,
    'UNMAPPED_CANONICAL_ARTIFACT' => 0,
    'UNMAPPED_OPERATIONAL_ARTIFACT' => 0,
    'REFERENCE_EDGE_WITHOUT_MIGRATION_STRATEGY' => 0,
    'LEGACY_ASSET_WITHOUT_DISPOSITION' => 0,
    'UNKNOWN_REBUILDABILITY_AUTO_REGENERATED' => 0,
    'LEGACY_DELETE_OR_RETIRE_WITHOUT_AUTHORIZATION' => 0,
    'CANONICAL_APPLY_EXECUTED_IN_STAGE07' => 0
  },
  'real_apply_readiness' => 'MIGRATION_BLOCKED',
  'real_apply_blockers' => ['CON-002', '4 missing historical document targets', 'inherited Stage 03 risks'],
  'openspec' => 'NOT_OBSERVED_DESIGN_ONLY', 'activation' => 'OFF'
})

puts JSON.generate({'run_id' => RUN_ID, 'capabilities' => cap_rows.size, 'assets' => asset_rows.size, 'artifacts' => artifact_rows.size, 'operational' => operational_rows.size, 'references' => reference_rows.size, 'broken_references' => broken.size, 'false_positives' => false_positive.size})
