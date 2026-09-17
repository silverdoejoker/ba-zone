# CHANGELOG

All notable changes to the **BA Zone (Requirements & Documentation Toolkit)** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased] - 2026-09-17

### Added
- **Strict Prototype / Mockup Ignore Rule**:
  - Updated `.gitignore` to strictly ignore all files under `prototypes/` and `mockups/` (except `.gitkeep`).
  - Completely blocks builds (`dist/`, `build/`, `out/`, `node_modules/`, `.next/`, `.nuxt/`) from ever being committed.
- **Repository Hygiene Auditor (`scripts/audit_hygiene.py`)**:
  - New automated validator integrated as **Suite 1/4** in `audit-all.ps1`.
  - Scans Git tracked index (`git ls-files`) to guarantee 0 prototype or build files are tracked.
  - Verifies `.gitignore` contains mandatory protection rules for enterprise document repositories.
- **Workspace Agents & Skills Registry**:
  - Initialized standard `.agents/` structure with `AGENTS.md` monitor registry.
  - Documented strict **Zero Prototype/Build Leakage Policy** in `AGENTS.md`.
  - Copied & synchronized all core AI skills into `.agents/skills/`:
    - `doc-template-learner-skill`
    - `use-case-writer-skill`
    - `user-story-writer-skill`
    - `web-app-uat-skill`
- **NDA & Confidential Documents Protection**:
  - Updated `.gitignore` to block all raw enterprise client documents (`docs/inputs/*`, `*.docx`, `*.pdf`, `use-case-writer-main/`, `user-story-ac-writer-main/`).
  - Added temporary ignore rule for `docs/NLE_CLARIFICATION_AGENDA_AND_GAP_CHECKLIST.md` to preserve user's working notes locally while completely excluding from Git.
  - Sanitized all pending reports: `docs/CR_LEASING_GAP_ANALYSIS_REPORT.md`, `docs/LEASING_MANAGEMENT_AS_IS_SUMMARY.md`, and `docs/URD_GMS_SYSTEM_CONTEXT_REPORT.md` (generalized all client entities: MegaCorp, RetailLease, AssetMgmt, REF-GMS-2026).
  - Guarantees signed agreements, corporate URLs, internal IPs, and PII can never be leaked to Git.
- **Centralized Templates & References Library (`docs/templates/`)**:
  - Consolidated all template types (.docx, .pdf, .md, .json) into `docs/templates/` with master catalog [`README.md`](file:///d:/repo/ba-zone/docs/templates/README.md):
    - Enterprise Client References: `[signed]3.URD_GMS_Full_Final 23.03.26.pdf`, `NLE-IT-Yeu cau PTUD-100926.pdf` (and raw Word originals in `docs/inputs/`).
    - Standard Specification Templates: `template_blueprint_schema.md`, `template_use_case_16_fields.md`, `template_user_story_invest.md`, `template_acceptance_criteria_gherkin.md`, `template_uat_test_plan.md`, `template_uat_acceptance_report.md`.
    - Real-World Reference Samples: `brd_semantic_search_template.md`, `sample_use_case_contract_flow.md`, `sample_use_case_en.md`, `sample_use_case_vi.md`, `sample_user_story_en.md`, `sample_user_story_vi.md`, `sample_user_stories_epics.md`, `sample_uat_report_en.md`, `sample_uat_report_vi.md`, `sample_uat_credentials.json`.
  - Established BA Guidelines & Checklists Library (`docs/guidelines/`):
    - `blueprint_extraction_guide.md`: Reverse-engineering guide for BRD, URD, SRS, FSD archetypes & 5 structural parity rules.
    - `use_case_quality_checklist.md`: 20-point Karl Wiegers & Alistair Cockburn quality checklist.
    - `use_case_writing_style.md`: Readability-first principles, active voice, and step granularity rules.
    - `invest_criteria_guide.md`: 6 INVEST criteria with anti-patterns and 6 splitting patterns.
    - `user_story_quality_checklist.md`: Pre-commit self-review checklist for User Stories and Gherkin ACs.
  - Complete NDA protection maintained: Raw binary `.docx` and `.pdf` files remain safely ignored in `.gitignore` to prevent accidental Git commit.
- **Scratch Script Lifecycle & Cleanup Policy**:
  - Established rule for temporary scripts in `scratch/`: must undergo post-task assessment (Keep vs Drop).
  - Scripts with long-term reuse are promoted to `scripts/`; one-off debug scripts must be dropped to prevent repository clutter.
  - Ensured `scratch/*` is permanently excluded from Git commits via `.gitignore` and audited by `audit_hygiene.py`.

---

## [1.2.0] - 2026-09-17

### Added
- **Web App UAT & Exploratory Testing Skill (`web-app-uat-skill`)**:
  - 8-Phase UAT Protocol (Pre-flight, Multi-Role RBAC, Happy Path, Edge Cases, Negative Fault Tolerance, Cross-device Viewports, Console Health).
  - Token-Preserving & 3-Second Fail-Fast guard for headless DOM inspection.
  - Hardware Isolation Registry for Camera OCR, Google Play/Apple IAP, and Biometrics/SAF.
- **Automated Quality Auditor (`scripts/audit_uat.py`)**:
  - Verifies UAT acceptance reports against mandatory 8-phase structure.
  - Added automated live app probe CLI mode (`--url`, `--username`, `--password`).
- **Master Compounding Loop Suite (`audit-all.ps1`)**:
  - Master PowerShell verification script executing validation suites with 100% pass guarantee.

---

## [1.1.0] - 2026-09-17

### Added
- **Document Template Learner & Generator (`doc-template-learner-skill`)**:
  - Reverse-engineers and extracts structural blueprints from reference BRD, URD, SRS, FSD, and PRD files.
  - Added interactive section-by-section generation and full batch generation.
- **User Story & Acceptance Criteria Writer (`user-story-writer-skill`)**:
  - Enforces 6 INVEST criteria validation.
  - Enforces 3 mandatory Gherkin scenarios (Happy Path, Edge Case, Negative Path).
  - Added bilingual prompt and artifact support via `output_language=en|vi`.
- **Automated Story Auditor (`scripts/audit_us.py`)**:
  - Automated INVEST and Gherkin scenario validation.

---

## [1.0.0] - 2026-09-17

### Initial Release
- **Use Case Writer Skill (`use-case-writer-skill`)**:
  - Implemented Karl Wiegers / IIBA BABOK 16-field standard specification template.
  - Enforced Alistair Cockburn scoping (Coffee-break test, User-goal level).
  - 20-point quality audit checklist.
- **Automated Use Case Auditor (`scripts/audit_uc.py`)**:
  - Validates 16 fields, sequential numbering, alternation, and exception branches.
- **Documentation**:
  - Comprehensive `README.md` with Vietnamese & English usage guidelines.
