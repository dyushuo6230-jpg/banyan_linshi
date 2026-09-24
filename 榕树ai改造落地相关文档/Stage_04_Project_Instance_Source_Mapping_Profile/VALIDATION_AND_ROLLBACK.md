# Stage 04 Validation

| ID | 验证 | PASS |
|---|---|---|
| V04-01 | Upstream | Stage03 frozen hashes valid |
| V04-02 | Low Token | no full rediscovery |
| V04-03 | Project Instance | schema complete |
| V04-04 | Source Role Coverage | 9/9 accounted |
| V04-05 | Mapping Semantics | path != role |
| V04-06 | Existing Layout | no default relayout |
| V04-07 | Core Purity | no project value in Core schema |
| V04-08 | Overlay | cannot weaken Core safety |
| V04-09 | Variables | critical UNKNOWN blocks |
| V04-10 | Project Profile | schema complete |
| V04-11 | Contributor Profile | no authorization semantics |
| V04-12 | Git Identity | no merge/guess/modify |
| V04-13 | Provider Binding | generic ports remain unbound by default |
| V04-14 | Existing Adoption | preserve in place |
| V04-15 | New Init | recommended layout not mandatory |
| V04-16 | Framework Boundary | framework vs instance distinct |
| V04-17 | Bootstrap Migration | single writable truth |
| V04-18 | Secret Safety | 13 bodies untouched |
| V04-19 | Write Scope | no project/canonical writes |
| V04-20 | Handoff | Stage05 handoff complete, not started |

Hard metrics:

```text
UNMAPPED_SOURCE_ROLE = 0
SOURCE_MAPPING_WITHOUT_ROLE = 0
PROJECT_SPECIFIC_VALUE_IN_GENERIC_CORE_SCHEMA = 0
PHYSICAL_RELAYOUT_REQUIRED_BY_DEFAULT = 0
PROFILE_FIELD_USED_AS_AUTHORIZATION = 0
UNKNOWN_VARIABLE_SILENTLY_DEFAULTED = 0
```
