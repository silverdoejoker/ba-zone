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

### 5. `enterprise-nda-sanitizer`
- **Location:** `.agents/skills/enterprise-nda-sanitizer/`
- **Description:** Tự động ẩn danh hóa (Sanitize / Generalize) toàn bộ thực thể doanh nghiệp nhạy cảm khi viết tài liệu, specs và báo cáo kiến trúc hệ thống.
- **Core Capability:** 
  - Triết lý: "Generalize by Default, Specialize only on Export".
  - Ánh xạ tự động: Tên tập đoàn ➔ MegaCorp / RetailCorp, Vendor ➔ TechPartner, Mã định danh hợp đồng ➔ REF-XXX, URLs/IPs nội bộ ➔ example.com.
  - Cờ điều khiển: `official_export=true` chỉ bật khi xuất bản bàn giao chính thức cho khách hàng.

### 6. `kpi-goal-writer-skill`
- **Location:** `.agents/skills/kpi-goal-writer-skill/`
- **Description:** Generate KPI / Goal specifications for HR Performance Review systems (probation, quarterly, annual) following the standardized "Tạo Hiệu quả công việc Goal" form template used at NVG/ITC.
- **Core Capability:** 
  - **BA Controls Principle**: Mọi mốc KPI phải nằm 100% trong tầm kiểm soát của BA, lọc bỏ mọi dependency vào Dev/Ops/Deployment.
  - **Risk-Aware Scoping**: Tự động phân loại quy mô DA (Small/Medium vs Large/Complex) để đề xuất scope phù hợp (UAT Package vs Ma trận AM & Prototype).
  - **Parallel Project Weight Allocation**: Phân bổ trọng số hợp lý cho DA song song, chừa dự phòng cho DA ad-hoc phát sinh.
  - **13-Field HR Form Template**: Output copy-paste-ready trực tiếp vào hệ thống đánh giá Goal/KPI của HR.
  - **10-Point Quality Checklist**: Audit tự động sau khi tạo KPI (BA Controls, timeline conflicts, weight sum = 100%).

---

## Strict Repository Policy: Documentation Only (Zero Prototype/Build Leakage)
- **Repository Boundary**: This repository is strictly for Business Analysis specifications, PRD/BRD documents, test plans, and templates.
- **Prototypes & Mockups**: All interactive prototypes or mockup files built under `prototypes/`, `mockups/`, or build bundles (`dist/`, `build/`, `node_modules/`) must **NEVER** be committed to Git.
- **Enterprise NDA & Client Isolation**:
  - `docs/inputs/` (Raw client documents), `docs/outputs/` (Working exports/meeting checklists), and `docs/projects/` (Client project workspaces with PII/emails) are strictly local-only and ignored in `.gitignore`.
  - Only sanitized templates in `docs/templates/` and methodology guides in `docs/guidelines/` are tracked.
  - All office binaries (`*.docx`, `*.doc`, `*.pdf`, `*.xlsx`, `*.pptx`, `*.vsdx`) are permanently ignored across the repository.
- **Enforcement**: Automated audit script `scripts/audit_hygiene.py` runs in `audit-all.ps1` to detect and block any accidental commits of prototype or confidential client files.

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
| `scripts/audit_outputs.py` | Real Output Documents Quality, AM, NDA & Links | `docs/outputs/` Living Specifications |

### Running the Master Audit Suite:
```powershell
./scripts/audit-all.ps1
```

---

## Mandatory Post-Generation Auto-Audit Hook (Quy trình Tự Động Audit Sau Khi Tạo Tài Liệu)
Mỗi khi Agent tạo mới hoặc chỉnh sửa bất kỳ tài liệu nào trong `docs/outputs/`:
1. **Auto-Run Audit**: Agent **BẮT BUỘC** tự động chạy kiểm định chất lượng (thông qua `scripts/audit_outputs.py`).
2. **5 Tiêu chí kiểm định tự động**:
   - **Cấu trúc & Template**: Đầy đủ Document Control metadata, Mục tiêu SMART, Scope in/out, Core Functional Modules, Ma trận Fit-Gap.
   - **Thuật ngữ chuẩn NVG**: Bắt buộc chuẩn hóa Ma trận phân quyền / thẩm quyền thành **"AM" (Authority Matrix)**.
   - **Enterprise NDA Sanitization**: Không rò rỉ PII nhân sự, credential bí mật hoặc định danh hợp đồng bảo mật.
   - **Mermaid Diagrams**: Toàn bộ sơ đồ luồng, kiến trúc, sequence diagrams phải hợp lệ cú pháp 100%.
   - **Cross-Links Integrity**: Mọi liên kết chéo nội bộ (`[link](...)`) phải trỏ chính xác đến các file tồn tại thực tế.
3. **Self-Healing Loop**: Nếu phát hiện cảnh báo hoặc lỗi, Agent tự động sửa lỗi ngay lập tức trước khi bàn giao.
4. **Audit Status Report**: Luôn đính kèm trạng thái nghiệm thu chất lượng (Audit Status: PASS) khi phản hồi người dùng.

---

## Enterprise Domain & Terminology Conventions (Quy chuẩn thuật ngữ nghiệp vụ NVG)
- **Ma trận Phân quyền & Thẩm quyền (Authority Matrix)**: 
  - Tại NVG (NovaGroup / Nova Service / ITC), Ma trận phân quyền / thẩm quyền phê duyệt được gọi tắt chính thức là **'AM'** (Authority Matrix / Approval Matrix).
  - Trong mọi tài liệu đặc tả (BRD, URD, PRD, SRS, Use Case, UAT):
    - Đổi/chuẩn hóa các đề mục liên quan từ *RBAC* hoặc *Ma trận phân quyền* thành **"Ma trận Phân quyền & Thẩm quyền (Authority Matrix - AM)"** hoặc **"Ma trận AM"**.
    - Khi trao đổi với Stakeholders (PMO Ms. Tú, BA Ms. Khanh - Nguyễn Thụy Mai Khanh, Đào tạo, BOM): Luôn sử dụng thuật ngữ **"Ma trận AM"** hoặc **"AM"**.
- **Danh bạ định danh cán bộ ITC (Verified Directory)**:
  - Ms. Trang (Giám đốc Bộ phận Quản lý CĐS): `itc.gdbp.4@novagroup.vn`
  - Ms. Tú (Chuyên gia Quản lý Dự án - PMO): `itc.cg.3@novagroup.vn` | SĐT: `0397479999`
  - Ms. Khanh (Chuyên viên Cao cấp BA PM QLCH): `itc.cvcc.3@novagroup.vn` | SĐT: `0904884874`
  - Minh (Trần Quang Anh - Senior IT BA): `itc.cvcc.55@novagroup.vn`

---

## Agent Usage & Rules
- All skills in `.agents/skills/` are automatically discovered by Antigravity AI Agent for project tasks.
- Keep `SKILL.md` instructions and audit scripts synchronized whenever adding or modifying skill workflows.
- Strictly adhere to NVG Terminology Conventions (AM for Authority Matrix) across all generated specifications and discussions.
- Strictly execute the Mandatory Post-Generation Auto-Audit Hook on every document output.
