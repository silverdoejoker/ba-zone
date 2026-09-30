---
name: doc-template-learner
description: |
  Learn, reverse-engineer, and replicate document structures and templates from any reference document (BRD, URD, SRS, FSD, PRD, Architecture Design, etc.).
  The skill extracts a comprehensive "Document Structural Blueprint" (metadata, heading hierarchy, section contracts, table layouts, Mermaid diagram styles, and writing tone),
  then generates a new document matching the exact template layout but populated with new project content from user prompts, notes, or attachments.
  Includes the official NVG Standard BRD Template (TEMPLATE-BRD-NVG-STD-2026) for enterprise requirement authoring.
  Supports both interactive section-by-section generation and full batch generation, with bilingual support via `output_language` (`en` or `vi`).
author: Phúc NT @ BA Zone
source: https://github.com/ba-zone
---

# Document Template Learner & Generator — Skill for IT Business Analysts
> by **Phúc NT** · BA Zone · Digital School

This skill empowers IT Business Analysts, Product Owners, and Technical Writers to **learn from any existing document template or reference artifact** (BRD, URD, SRS, FSD, PRD, etc.) and generate a structurally identical document customized for any new feature or domain.

---

## Core Value Proposition

In enterprise IT and software projects, every organization, client, and department has its own established document format:
- **BRD (Business Requirements Document) / URD (User Requirements Document)**: Business problem, project objectives, scope boundaries (in-scope / out-of-scope), stakeholder impact, and high-level requirements.
- **NVG Standard BRD Template (`TEMPLATE-BRD-NVG-STD-2026`)**: Standard 6-section template derived from TRC/NVG (`docs/templates/template_brd_standard.md`), featuring problem statement, priority milestones, calculation engine rules with 13 edge test cases, 6-field concise use cases, and raw/rollup data export schemas.
- **SRS (Software Requirements Specification)**: IEEE 830 / ISO 29148 standards, approval pages, revision history, system interfaces, detailed functional requirements, and non-functional requirements.
- **FSD (Functional Specification Document)**: UI screens, data dictionary, system state machines, API contracts, and screen-by-screen business rules.

Instead of forcing a one-size-fits-all format, this skill **learns your template** and produces documents that feel as if they were written by your company's senior lead BA.

---

## Standard NVG Document Blueprints Registry

Hệ thống tài liệu chuẩn hóa tại Khối CNTT NovaGroup (NVG-ITC) bao gồm 3 bộ khung tiêu chuẩn:

### 1. NVG Solution Architecture & Design Template (`TEMPLATE-NVG-ITD-SOP14-SAD-2026`)
* **Mã số mẫu:** `NVG-ITD-SOP14.F01`
* **File template:** [`docs/templates/template_thiet_ke_giai_phap_sop14.md`](file:///d:/repo/ba-zone/docs/templates/template_thiet_ke_giai_phap_sop14.md)
* **Cấu trúc 5 phần:**
  1. *Bảng ghi nhận thay đổi tài liệu:* Ngày, Tác giả, Mô tả, Phiên bản, Tính năng (ký hiệu M/S/X).
  2. *Thông tin chung:* Phạm vi tài liệu, Mục đích tài liệu, Khái niệm & thuật ngữ (AM, GFA/NLA, Turnover Rent), Tài liệu tham khảo.
  3. *Tổng quan ứng dụng:* Mục đích (SMART), Phạm vi (In/Out Scope), Quyền hạn sử dụng & Ma trận AM (Security L7 Data Scope).
  4. *Mô tả yêu cầu chức năng:* Danh sách yêu cầu chức năng, đặc tả Core Use Cases chi tiết.
  5. *Giải pháp hệ thống:* Kiến trúc Dev Spine 2026, CSDL `gms_*`, Calculation Engine & Ma trận Kịch bản Kiểm thử linh hoạt (Flexible Test Scenarios Matrix theo quy mô dự án), Sequence Diagram, Data Export Schema.

### 2. NVG Business Application Requirement Template (`TEMPLATE-NVG-ITD-SOP01-PTUD-2025`)
* **Mã số mẫu:** `NVG-ITD-SOP01.F01`
* **File template:** [`docs/templates/template_yeu_cau_ptud_sop01.md`](file:///d:/repo/ba-zone/docs/templates/template_yeu_cau_ptud_sop01.md)
* **Cấu trúc 3 phần:**
  - *I. Thông tin chung:* Người yêu cầu, Vị trí, Phòng ban, Người phê duyệt, Ngày & Số yêu cầu.
  - *II. Mô tả yêu cầu:* II.1 Mô tả chung, II.2 Yêu cầu nghiệp vụ (Phòng ban tham gia, As-is, To-be), II.3 Yêu cầu nghiệp vụ - chức năng (Quy trình nghiệp vụ dạng bảng, Chức năng SSO/Quản lý/Khóa căn, Biểu mẫu & Báo cáo Dashboard), II.4 Giao diện, II.5 Tích hợp, II.6 Phi chức năng.
  - *III. Thông tin khác:* Bảng 3 cấp Đề xuất (Người lập, Trưởng BP, Giám đốc đơn vị) và 2 cấp Phê duyệt (Lãnh đạo ITC, Ban Điều Hành).

### 3. NVG Standard BRD Template (`TEMPLATE-BRD-NVG-STD-2026`)
* **Mã số mẫu:** `TEMPLATE-BRD-NVG-STD-2026`
* **File template:** [`docs/templates/template_brd_standard.md`](file:///d:/repo/ba-zone/docs/templates/template_brd_standard.md)
* **Cấu trúc 6 phần:** Header, Yêu cầu bối cảnh, Phân rã tính năng & mốc bàn giao, Engine tính toán & ma trận kịch bản kiểm thử linh hoạt, 6-field concise use cases, Data export schema, Quản trị ngoại lệ AM.

---

## 5-Phase Workflow

```
Phase 1: INGEST & DECONSTRUCT   → Analyze reference template & sample content (PDF / MD / Docx)
Phase 2: EXTRACT BLUEPRINT       → Build & confirm Document Structural Blueprint
Phase 3: INGEST TARGET INPUT     → Ingest user prompt, notes, attachments, or Q&A
Phase 4: GENERATE TARGET DOC     → Produce new doc matching template (Markdown + HTML export)
Phase 5: PARITY AUDIT & HANDOVER → Verify 100% structural alignment & NVG AM compliance
```

---

## Mandatory Quality Rules for Generated BRDs:
1. **Approval Matrix Terminology**: Bắt buộc chuẩn hóa thẩm quyền phê duyệt thành **"AM" (Approval Matrix)**. Tuyệt đối không dùng *Authority Matrix* (NovaGroup không sử dụng thuật ngữ này). Không dùng thuật ngữ phân quyền chung chung khi giao tiếp với Stakeholders NVG.
2. **Enterprise NDA Sanitization**: Tự động ẩn danh hóa thông tin nhân sự ngoài danh bạ đã xác thực (`Ms. Trang`, `Ms. Tú`, `Ms. Khanh`, `Minh`).
3. **Internal Links Integrity**: Mọi liên kết chéo nội bộ `[link](...)` phải trỏ chính xác đến các file tồn tại trong `docs/`.
4. **Mermaid Diagrams**: Mọi sơ đồ luồng quy trình phải hợp lệ cú pháp Mermaid 100%.
