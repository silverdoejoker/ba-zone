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

## Standard NVG BRD Form Blueprint (`TEMPLATE-BRD-NVG-STD-2026`)

When authoring or generating a Business Requirements Document under the NVG standard, the document must follow the 6-section architecture defined in `docs/templates/template_brd_standard.md`:

```yaml
document_blueprint:
  name: "NVG Standard BRD / Feature Requirement"
  template_code: "TEMPLATE-BRD-NVG-STD-2026"
  reference_file: "docs/templates/template_brd_standard.md"
  output_language: "vi | en"
  tone: "Formal enterprise, clear operational contracts, measurable criteria"
  authority_matrix: "Strictly AM (Authority Matrix)"
  sections:
    - id: "sec-header"
      title: "Header & Document Control"
      format: "From, To (PMO), Request Code, Version, Date"
    - id: "sec-01"
      title: "1. Yêu Cầu (Request Overview & Problem Statement)"
      format: "12-row Contract Table: ID, Name, Category, Requester, Implementer, As-Is, Pain Points, Personas, To-Be, Constraints"
    - id: "sec-02"
      title: "2. Tính Năng và Thứ Tự Ưu Tiên (Feature Breakdown & Milestones)"
      format: "5-column Matrix: Priority (Ưu tiên 1/2), Code, Requirement, Detailed Scope, Deadline"
    - id: "sec-03"
      title: "3. Cách Tính Toán & Ma Trận Kịch Bản (Calculation Engine & Test Scenarios)"
      format: "3.1. Business Rules Table (De-duplication, Pairing, Edge Truncation, Odd Swipes) + 3.2. 13-Case Test Matrix"
    - id: "sec-04"
      title: "4. Đặc Tả Use Cases Chi Tiết (Core Use Cases - Priority 1)"
      format: "6-field Concise Use Case Table: Actor, Precondition, Main Flow, Exceptions, Data Log, Postcondition"
    - id: "sec-05"
      title: "5. Đặc Tả Cấu Trúc Dữ Liệu Xuất & Báo Cáo (Data Export Schema)"
      format: "5.1. Raw Transaction Logs Schema + 5.2. Aggregated Session Rollup Schema"
    - id: "sec-06"
      title: "6. Yêu Cầu Quản Trị, Ngoại Lệ & Audit Trail (Governance & Phase 2)"
      format: "Governance Matrix: Manual Adjustment with Audit Trail, Fallback Mechanisms, Line Manager (QLTT) Approval via AM"
```

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
1. **Authority Matrix Terminology**: Bắt buộc chuẩn hóa thẩm quyền phê duyệt thành **"AM" (Authority Matrix)**. Tuyệt đối không dùng thuật ngữ phân quyền chung chung khi giao tiếp với Stakeholders NVG.
2. **Enterprise NDA Sanitization**: Tự động ẩn danh hóa thông tin nhân sự ngoài danh bạ đã xác thực (`Ms. Trang`, `Ms. Tú`, `Ms. Khanh`, `Minh`).
3. **Internal Links Integrity**: Mọi liên kết chéo nội bộ `[link](...)` phải trỏ chính xác đến các file tồn tại trong `docs/`.
4. **Mermaid Diagrams**: Mọi sơ đồ luồng quy trình phải hợp lệ cú pháp Mermaid 100%.
