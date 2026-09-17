# AGENTS.md (Workspace Agents & Skills Registry)

## Purpose
This directory (`.agents/`) defines project-specific custom agent rules, quality audit loops, and skills tailored for **BA Zone (Business Analysis & Document Writing Toolkit)**.

---

## Active Skills Registry (`.agents/skills/`)

### 1. `doc-template-learner-skill`
- **Location:** `.agents/skills/doc-template-learner-skill/`
- **Description:** Reverse-engineers and extracts formatting rules, structure, table templates, and writing tone from reference documents (BRD, SRS, PRD, FSD).
- **Core Capability:** Learns document structural blueprints and generates structurally identical documents populated with new project content.

### 2. `use-case-writer-skill`
- **Location:** `.agents/skills/use-case-writer-skill/`
- **Description:** Standardized skill for authoring full 16-field Use Case specifications (Karl Wiegers / IIBA Babok standard).
- **Core Capability:** Cockburn goal-level scoping (Coffee-break test), Normal Course, Alternative Courses, Exceptions, and 20-point quality audit.

### 3. `user-story-writer-skill`
- **Location:** `.agents/skills/user-story-writer-skill/`
- **Description:** Standardized skill for authoring User Stories and Acceptance Criteria (INVEST & Gherkin syntax).
- **Core Capability:** INVEST criteria self-check, 3 mandatory Gherkin scenarios (Happy Path, Edge Case, Negative Path), and bilingual output (`output_language=en|vi`).

### 4. `web-app-uat-skill`
- **Location:** `.agents/skills/web-app-uat-skill/`
- **Description:** Web & Mobile Web Application User Acceptance Testing (UAT), exploratory testing, and staging/live verification framework (TrọBill Methodology).
- **Core Capability:** 
  - 8-Phase UAT Protocol (Pre-flight, Multi-Role RBAC, Happy Path Walkthrough, Edge Cases, Negative Fault Tolerance, Cross-device Viewports, Console Health Sniffing).
  - 3-Second Fail-Fast guard for headless DOM inspection & Token Preservation.
  - Hardware Isolation Registry (Manual check boundary for Camera OCR, Google Play/Apple IAP, Biometrics/SAF).
  - Generates comprehensive UAT Acceptance reports and GO/NO-GO release decisions.

---

## Strict Repository Policy: Documentation Only (Zero Prototype/Build Leakage)
- **Repository Boundary**: This repository is strictly for Business Analysis specifications, PRD/BRD documents, test plans, and templates.
- **Prototypes & Mockups**: All interactive prototypes or mockup files built under `prototypes/`, `mockups/`, or build bundles (`dist/`, `build/`, `node_modules/`) must **NEVER** be committed to Git.
- **Enforcement**: Automated audit script `scripts/audit_hygiene.py` runs in `audit-all.ps1` to detect and block any accidental commits of prototype files.

## Scratch Script Lifecycle & Cleanup Policy (`scratch/`)
- **Tạo script tạm**: Mọi script phân tích raw data, cào dữ liệu mẫu, hoặc debug tạm thời trong quá trình thực thi phải được tạo trong `scratch/`.
- **Đánh giá sau khi Done Task (Post-Task Assessment)**:
  - Khi hoàn thành task, Agent & Người dùng **BẮT BUỘC** đánh giá giá trị tái sử dụng của script đó.
  - **Nếu có giá trị lâu dài (Keep)**: Di chuyển, chuẩn hóa tài liệu và đưa vào `scripts/` (đồng thời đăng ký vào bộ audit nếu cần).
  - **Nếu dùng một lần / phục vụ debug cục bộ (Drop)**: Xóa bỏ (`drop/delete`) ngay lập tức khỏi `scratch/` để giữ repository sạch sẽ, chỉ giữ lại file `.gitkeep`.
- **Chặn commit Git**: Thư mục `scratch/*` luôn nằm trong `.gitignore` để đảm bảo không bao giờ bị rò rỉ lên remote repository.

---

## Quality Audits & Compounding Verification (`scripts/audit-all.ps1`)

The workspace includes automated quality auditor scripts under `scripts/` to enforce 100% compliance across all skills and generated artifacts:

| Auditor Script | Target Standard | Skill / Policy Audited |
|---|---|---|
| `scripts/audit_hygiene.py` | Zero Prototype / Build Leakage Policy | Repository Cleanliness & `.gitignore` Integrity |
| `scripts/audit_uc.py` | Karl Wiegers / IIBA 16-Field Template Integrity | `use-case-writer-skill` |
| `scripts/audit_us.py` | INVEST Principles & 3-Scenario Gherkin Syntax | `user-story-writer-skill` |
| `scripts/audit_uat.py` | 8-Phase Protocol, Test Matrix, & Hardware Registry | `web-app-uat-skill` |

### Running the Master Audit Suite:
```powershell
./scripts/audit-all.ps1
```

---

## Agent Usage & Rules
- All skills in `.agents/skills/` are automatically discovered by Antigravity AI Agent for project tasks.
- Keep `SKILL.md` instructions and audit scripts synchronized whenever adding or modifying skill workflows.
