# AGENTS.md (Workspace Agents & Skills Registry)

## Purpose
This directory (`.agents/`) defines project-specific custom agent rules, quality audit loops, and skills tailored for **BA Zone (Business Analysis & Document Writing Toolkit)**.

---

## Active Skills Registry (`.agents/skills/`)

### 1. `doc-template-learner-skill`
- **Location:** `.agents/skills/doc-template-learner-skill/`
- **Description:** Reverse-engineers and extracts formatting rules, structure, table templates, and writing tone from reference documents (BRD, SRS, PRD, FSD).
- **Core Capability:** Learns document structural blueprints and generates structurally identical documents populated with new project content. Includes the official NVG template library:
  - **NVG Solution Architecture Design Template (`NVG-ITD-SOP14.F01`)** in `docs/templates/template_thiet_ke_giai_phap_sop14.md` (5-section architecture: Document change history, General info & Glossary, Application overview & AM scope, Functional requirements & Core Use Cases, System solution architecture with calculation engine & dynamic project-specific test scenarios).
  - **NVG Application Requirement Template (`NVG-ITD-SOP01.F01`)** in `docs/templates/template_yeu_cau_ptud_sop01.md` (3-part official form: General info, Requirement description with workflow tables & SSO, 3-tier submission & 2-tier approval).
  - **NVG Standard BRD Template (`TEMPLATE-BRD-NVG-STD-2026`)** in `docs/templates/template_brd_standard.md` (6-section architecture: Request overview, Feature priority, calculation engine with flexible test scenarios matrix, concise use cases, and raw/rollup export schemas).

> **Nguyên tắc Ma trận Kịch bản Kiểm thử (Flexible Test Scenarios Policy):**  
> Tuyệt đối KHÔNG gán cứng số lượng Test Cases cố định (như 13 cases). Số lượng và độ phủ của Ma trận Kịch bản Kiểm thử (Test Scenarios Matrix) phải được xác định linh hoạt căn cứ theo quy mô, bản chất nghiệp vụ và rủi ro thực tế của từng dự án cụ thể.

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

### 7. `digital-transformation-roadmap-skill`
- **Location:** `.agents/skills/digital-transformation-roadmap-skill/`
- **Description:** Enterprise Digital Transformation Strategy & Architecture RAG Knowledge Base (2025–2030).
- **Core Capability:** 
  - Đóng gói Lộ trình 5 Wave CĐS (2024-2030+), Phân hoạch 5 Tầng Kiến trúc (EDP Lakehouse, ECT, ESB).
  - Mô hình Vận hành IT-as-a-Business, 6 Task-Force chuyên trách & Chu trình phối hợp 6 bước với Business.
  - Nền tảng One Nova (Employee Journey 12 bước, Cascade KPI 100%, Ma trận AM).
  - Quy trình 5 bước kiểm tra đối chiếu tính tương thích kiến trúc khi nhận dự án mới.

### 8. `dev-architecture-spine-skill`
- **Location:** `.agents/skills/dev-architecture-spine-skill/`
- **Description:** Technical Baseline & Architecture Spine 2026 for IT BA specification authoring.
- **Core Capability:** 
  - 7 Trụ cột kiến trúc chuẩn hóa (Application Gateway SSO, Ma trận AM 2 tầng, Table Prefix `gms_*`, Strict Soft-delete 100%, Immutability, API Envelope, Async Queue RabbitMQ/NATS).
  - Checklist 7 Điểm đối chiếu tương thích kỹ thuật giữa BA Specs và Dev Architecture.
  - Phân tách ranh giới rõ ràng giữa Functional RBAC và Security L7 Data Scope.

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
| `scripts/audit_outputs.py` | Real Output Documents Quality, AM, Dev Architecture Spine, NDA & Links | `docs/outputs/` Living Specifications |

### Running the Master Audit Suite:
```powershell
./scripts/audit-all.ps1
```

---

## Mandatory Post-Generation Auto-Audit Hook (Quy trình Tự Động Audit Sau Khi Tạo Tài Liệu)
Mỗi khi Agent tạo mới hoặc chỉnh sửa bất kỳ tài liệu nào trong `docs/outputs/`:
1. **Auto-Run Audit**: Agent **BẮT BUỘC** tự động chạy kiểm định chất lượng (thông qua `scripts/audit_outputs.py`).
2. **Quy chuẩn thực thi**: Tuân thủ toàn diện [`.agents/rules/output_quality_standards.md`](file:///d:/repo/ba-zone/.agents/rules/output_quality_standards.md) với 8 tiêu chí kiểm định tự động:
   - **Cấu trúc & Thứ bậc (Structure & Hierarchy)**: Đầy đủ 6 trường Document Control metadata, **Mục lục tổng quan (Table of Contents)** và **Trang ký duyệt (Sign-off Page)** đặt ngay đầu tài liệu theo mẫu chuẩn Ms. Hân (`NVL_ITD_SDD`); Scope in/out phân kỳ rõ ràng; thứ bậc tiêu đề H1 -> H2 -> H3 tuần tự, không nhảy cóc.
   - **Định dạng & Chống tràn trang (Anti-Overflow Format)**: Bảng có cột nội dung dài tối đa 4 cột (tách bảng theo từng phân kỳ nếu nhiều cột); khóa cứng CSS `table-layout: fixed; width: 100%; word-break: break-word;` và `@page { size: A4 portrait; margin: 12mm 10mm; }` trên toàn bộ file HTML; cân bằng số cột dòng header và body rows.
   - **Tính toàn vẹn cú pháp Markdown/HTML**: Thẻ mở phải có thẻ đóng đối ứng (không để sót thẻ unclosed `**`, `*`, ```` ` ````); không lỗi cú pháp HTML.
   - **Chính tả tiếng Việt & Chuẩn mực giao tiếp (Vietnamese Spelling & Tone)**: Quét từ điển lỗi chính tả BA (bắt buộc: `giảng viên`, `thư ký`, `quy trình`, `chuyên cần`, `điểm danh`, `xử lý`, `lưu trữ`...); không lỗi vỡ font UTF-8 (Mojibake); không đặt dấu cách trước dấu câu; dùng danh xưng ngoại giao tập thể ("Phòng TRC phối hợp...", không nêu đích danh giảng viên như bên gây nghẽn).
   - **Chuẩn Mực Từ Ngữ Doanh Nghiệp & Chống "Mùi AI" (Anti-AI Smell)**: Tuân thủ toàn diện [`.agents/rules/nvg_corporate_wording_standards.md`](file:///d:/repo/ba-zone/.agents/rules/nvg_corporate_wording_standards.md). Cấm tiệt từ ngữ khoa trương ("triệt tiêu hoàn toàn", "siêu tốc", "vượt trội", "đột phá", "chuẩn xác 100%"), cấm lý thuyết sách vở (định nghĩa SMART, Use Case 16 trường Karl Wiegers); bắt buộc dùng bảng đặc tả UI Field Specs 5 cột (`TT` | `Tên trường thông tin` | `Loại` | `Business rule` | `Bắt buộc`) và Ma trận Notification (Teams/Email).
   - **Thuật ngữ chuẩn NVG**: Bắt buộc chuẩn hóa Ma trận phê duyệt / thẩm quyền thành **"AM" (Approval Matrix)**. Tuyệt đối KHÔNG dùng *Authority Matrix* (NovaGroup không sử dụng thuật ngữ này).
   - **Dev Architecture Spine 2026**: Zero local auth, Ma trận AM 2 tầng kèm Data Scope, CSDL prefix `{prefix}_`, Strict Soft-delete 100%, Async Queue cho batch jobs.
   - **Enterprise NDA Sanitization**: Không rò rỉ PII nhân sự, credential bí mật hoặc định danh hợp đồng bảo mật.
   - **Mermaid Diagrams & Links Integrity**: Toàn bộ sơ đồ luồng/kiến trúc hợp lệ cú pháp 100%; mọi liên kết chéo nội bộ (`[link](...)`) phải trỏ chính xác đến file đang tồn tại thực tế.
   - **Quy Chuẩn Phông Chữ & Cỡ Chữ (Corporate Typography Standard)**: 100% tài liệu xuất bản và deliverable HTML/Word bắt buộc dùng thống nhất phông chữ **`Times New Roman`** (`font-family: 'Times New Roman', Times, serif;`), cỡ chữ thân văn bản (Body text, Paragraphs `<p>`, Lists) chuẩn **`12pt`** (line-height: 1.5, màu chữ `#000000`), bảng biểu (`<table>`, `<th>`, `<td>`) chuẩn **`11pt`** (line-height: 1.45) để vừa vặn trang in A4 Portrait và không tràn lề khi xuất sang Word.
   - **Text-First & Tương Thích Microsoft Word (Anti-Graphics Degradation)**: Tuyệt đối tránh CSS Grid (`display: grid`), card decks bóng đổ và pill badges bo tròn mềm trong HTML deliverables; bắt buộc dùng `<table>` chuẩn cho Metadata/KPI cards để Word nhận diện thành native table; dùng nhãn ngoặc vuông `[...]` cho badges; luôn đính kèm bảng văn bản dự phòng (Text Fallback Table) bên dưới các sơ đồ Mermaid để chuyển đổi PDF -> DOCX không bị vỡ khung vẽ hoặc phải sửa manual.
3. **Self-Healing Loop**: Nếu phát hiện cảnh báo hoặc lỗi, Agent tự động sửa lỗi ngay lập tức trước khi bàn giao.
4. **Audit Status Report**: Luôn đính kèm trạng thái nghiệm thu chất lượng (Audit Status: PASS - 0 Errors) khi phản hồi người dùng.

---

## Enterprise Domain & Terminology Conventions (Quy chuẩn thuật ngữ nghiệp vụ NVG)
- **Ma trận Thẩm quyền Phê duyệt (Approval Matrix - AM)**: 
  - Tại NVG (NovaGroup / Nova Service / ITC), Ma trận phê duyệt / thẩm quyền phê duyệt được gọi chính thức là **Approval Matrix (AM)** (Ma trận Phê duyệt / Ma trận Thẩm quyền Phê duyệt). Tuyệt đối **KHÔNG dùng "Authority Matrix"** (NovaGroup không sử dụng thuật ngữ này).
  - Trong mọi tài liệu đặc tả (BRD, URD, PRD, SRS, Use Case, UAT, SOP14):
    - Đổi/chuẩn hóa các đề mục liên quan từ *RBAC* hoặc *Ma trận phân quyền* thành **"Ma trận Phê duyệt (Approval Matrix - AM)"**, **"Ma trận Thẩm quyền Phê duyệt (AM)"** hoặc **"Ma trận AM"**.
    - Khi trao đổi với Stakeholders (PMO Ms. Tú, BA Ms. Khanh - Nguyễn Thụy Mai Khanh, Đào tạo, BOM): Luôn sử dụng thuật ngữ **"Ma trận AM"** hoặc **"AM"** (Approval Matrix).
- **Danh bạ định danh cán bộ ITC (Verified Directory)**:
  - Ms. Trang (Giám đốc Bộ phận Quản lý CĐS): `itc.gdbp.4@novagroup.vn`
  - Ms. Tú (Chuyên gia Quản lý Dự án - PMO): `itc.cg.3@novagroup.vn` | SĐT: `0397479999`
  - Ms. Khanh (Chuyên viên Cao cấp BA PM QLCH): `itc.cvcc.3@novagroup.vn` | SĐT: `0904884874`
  - Ms. Hân (Chuyên viên BA / Tác giả mẫu chuẩn NVL_ITD_SDD): Vũ Thị Hân (ITC-NVG)
- **Quy chuẩn Kiến trúc Kỹ thuật (Dev Architecture Baseline 2026)**:
  - Tuân thủ toàn diện các quy ước tại `.agents/rules/dev_architecture_conventions.md` và `docs/guidelines/ARCHITECTURE-SPINE.md`.
  - Zero Local Auth (SSO qua Application Gateway).
  - Tách bạch Ma trận AM (Functional Permission) và Security L7 Data Scope (Dự án/Phân khu).
  - Bảng CSDL có prefix `{prefix}_` (ví dụ `gms_*`).
  - 100% Xóa mềm (Strict Soft-delete).
  - Tác vụ nặng (Excel import, tính tiền hàng loạt, xuất PDF lớn) phải quy định luồng xử lý bất đồng bộ (Async Queue RabbitMQ/NATS).

---

## Agent Usage & Rules
- All skills in `.agents/skills/` are automatically discovered by Antigravity AI Agent for project tasks.
- Keep `SKILL.md` instructions and audit scripts synchronized whenever adding or modifying skill workflows.
- Strictly adhere to NVG Terminology Conventions (AM for Approval Matrix; strictly ban "Authority Matrix") across all generated specifications and discussions.
- Strictly enforce the Dev Architecture Baseline (`dev-architecture-spine-skill`) on all BRD, SRS, Use Case, Data Dictionary, and UAT artifacts.
- Strictly execute the Mandatory Post-Generation Auto-Audit Hook on every document output.
