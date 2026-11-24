# Fundamental-particle classification repository storage audit — 2026-11-24

**Scope:** read-only current-tree audit and initial adoption of the central three-tier scientific data storage policy.  
**Repository:** `lm846802297-bit/fundamental-particle-classification`  
**Audited branch:** `main`

## 1. Repository baseline

- GitHub repository metadata size: **241 KiB**.
- Complete recursive main tree: **4 blobs**, approximately **0.016 MiB** summed uncompressed file bytes.
- Recursive tree response was complete (`truncated=false`).
- No file exceeds 1 MiB.
- The current tree contains only README, CONTRIBUTING, the research program, and a literature-review template.
- No numerical result bundle, native data, or LFS configuration is present.

GitHub metadata size and current-tree uncompressed bytes are different measures; this audit does not claim a historical Git-object-size breakdown.

## 2. Storage-tier decision

- **Ordinary Git:** appropriate for the current research program, literature records, theorem/construction matrices, derivations, bibliography, task briefs, provenance, and future small/medium native numerical or symbolic outputs.
- **Git LFS:** not enabled; no current dataset justifies it.
- **External object storage:** not configured; no bulk or long-term data object currently requires it.

If future symbolic/numerical work produces large datasets, select LFS or external storage based on actual size, access pattern, licensing, and retention. Preserve exact source/input identities, environment, parameters, native outputs, SHA-256, convergence/error analysis, and independent physical validation.

## 3. Integrity and migration boundary

- No existing file was modified, deleted, or moved by the audit.
- No Git history was rewritten.
- No scientific calculation was run or rerun.
- No LFS or external storage was configured.

## 4. Standards adoption

This repository's new `docs/standards-lock.yaml` pins central commit `14155487afc075d301fa7f6cf452c7bff137e869`, which includes central PR #42's three-tier Git / Git LFS / external object storage policy. Project-specific definitions of fundamental particles, dimensional scope, candidate criteria, and theorem assumptions remain local.

## 5. Conclusion

This is a minimal theory-program repository with no current numerical data. Ordinary Git is appropriate. **No migration and no LFS activation are required.** Apply the three-tier policy as the project develops and creates actual numerical or symbolic datasets.
