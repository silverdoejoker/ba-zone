---
name: kpi-goal-writer
description: |
  Generate KPI / Goal specifications for HR Performance Review systems (probation, quarterly, annual) 
  following the standardized "Tạo Hiệu quả công việc Goal" form template used at NVG/ITC.
  Use whenever a BA or any employee needs to set up, draft, or review KPI Goals for one or more 
  concurrent projects within a defined review period.
  Triggers include "set KPI", "tạo KPI", "viết KPI thử việc", "setup goal", "lập KPI", "KPI dự án",
  "draft KPI", "performance goal", "mục tiêu thử việc", "KPI probation".
  Skill enforces realistic milestone scoping (BA Controls principle), risk-aware dependency filtering,
  and parallel project weight allocation.
  Output language is controlled by the `output_language` session variable (default: `vi`; set to `en` for English).
author: Minh (Trần Quang Anh) · BA Zone
---

# KPI / Goal Writer — Skill for IT Business Analysts & Project Members
> by **Minh (Trần Quang Anh)** · BA Zone · ITC-NVG

This skill guides the creation of **KPI / Performance Goal specifications** that can be directly 
copy-pasted into the HR "Tạo Hiệu quả công việc Goal" form system, based on real project context 
from `docs/inputs/` and `docs/outputs/`.

---

## When to Use This Skill

Trigger this skill whenever the user needs to:
- Draft KPI Goals for a **probation period** (thử việc) or periodic review (quarterly/annual).
- Set up Goals for **one or more concurrent projects** (parallel DA).
- Review or refine existing KPI milestones for achievability and risk.
- Ensure KPI milestones are **100% within BA's control** (BA Controls principle).

---

## Session Variables

| Variable | Values | Default | Description |
|---|---|---|---|
| `output_language` | `en` (English) · `vi` (Vietnamese) | `vi` | Controls the language of KPI output document |
| `review_period` | `probation` · `quarterly` · `annual` | `probation` | Type of performance review cycle |
| `start_date` | Date (DD/MM/YYYY) | *(must be provided)* | Official start date of the review period |
| `end_date` | Date (DD/MM/YYYY) | *(must be provided)* | Official end date of the review period |

---

## Core Principles (MANDATORY)

### 1. BA Controls Principle (Nguyên tắc BA Làm Chủ 100%)
> **CRITICAL RULE**: Every KPI milestone MUST be 100% within the BA's direct control and deliverables.
> Never include milestones that depend on Dev completion, deployment, or third-party sign-off 
> that BA cannot influence.

**✅ Safe milestones (BA Controls):**
- BRD/URD/SRS document completion & approval
- Use Cases / User Stories authoring
- Ma trận Phân quyền & Thẩm quyền (Authority Matrix - AM)
- Wireframe / Prototype design & sign-off
- UAT Test Cases Matrix & User Guide **preparation** (NOT execution)
- Gap Analysis Report / Fit-Gap Matrix
- MoM (Minutes of Meeting) & Workshop facilitation
- Clarification Checklist / Discovery Questionnaire

**❌ Risky milestones (Dependencies on Dev/Ops):**
- UAT execution & Go-live sign-off (depends on Dev delivery)
- Production deployment (depends on DevOps/Infra)
- System integration testing (depends on multiple teams)
- End-user training completion (depends on scheduling & availability)

### 2. Risk-Aware Scoping by Project Size

| Project Size | Indicators | Recommended Scope for 2-month KPI |
|---|---|---|
| **Small/Medium** | Kế thừa hệ thống có sẵn, ít module mới, ≤3 luồng nghiệp vụ chính | BRD → SRS → **UAT Package sẵn sàng** |
| **Large/Complex** | CR bổ sung nhiều quy trình mới (≥5), nhiều stakeholders, phân pha Phase 1/2 | BRD → **Ma trận AM & Prototype** → **SRS Phase 1 bàn giao Dev** |

### 3. Parallel Project Weight Allocation (Phân bổ Trọng số Song song)

| Scenario | Recommended Weight Split |
|---|---|
| 2 DA song song, không có DA ad-hoc | 50% - 50% |
| 2 DA song song, **có khả năng DA ad-hoc phát sinh** | 40% - 40% - 20% (dự phòng) |
| 3 DA song song xác định | 35% - 35% - 30% |
| 1 DA chính + hỗ trợ nhiều DA nhỏ | 60% - 40% (hỗ trợ chung) |

> **TIP**: Luôn hỏi user: *"Có khả năng phát sinh DA ad-hoc trong kỳ đánh giá không?"* 
> để quyết định chừa trọng số dự phòng hay không.

---

## HR Goal Form Template (13 Fields)

Every KPI Goal output MUST map to exactly these 13 fields of the HR system form:

### Field Definitions

| # | Field Name (Vietnamese) | Field Name (English) | Type | Required | Notes |
|---|---|---|---|---|---|
| 1 | **Tên mục tiêu** | Goal Title | Text (500 chars) | ✅ | Concise, action-oriented title |
| 2 | **Phân quyền xem** | Visibility | Dropdown | ✅ | Default: `Công khai` |
| 3 | **Mô tả** | Description | Text (4000 chars) | ✅ | Milestone breakdown with % weights |
| 4 | **Chỉ số KPI** | KPI Metrics | Text (4000 chars) | ✅ | Measurable success criteria |
| 5 | **Đơn vị tính** | Unit | Dropdown | ✅ | Default: `%` |
| 6 | **Công thức** | Formula | Text (4000 chars) | ✅ | Calculation method |
| 7 | **Trọng số** | Weight | Number (%) | ✅ | Percentage weight of this goal |
| 8 | **Ngày bắt đầu** | Start Date | Date | ✅ | `start_date` variable |
| 9 | **Ngày kết thúc** | End Date | Date | ✅ | `end_date` variable |
| 10 | **Mục tiêu** | Target | Number | ✅ | Default: `100` |
| 11 | **Thực tế** | Actual | Number | — | Default: `0` (filled later) |
| 12 | **Khả năng thành công** | Success Likelihood | Dropdown | ✅ | `Thấp` / `Trung bình` / `Cao` |
| 13 | **Ghi chú (Thang điểm)** | Performance Criteria Table | Table | ✅ | Min/Target/Max rating scale |

### Performance Criteria Table Template

| Mô tả | % Hoàn thành | Xếp hạng |
|---|---|---|
| **Mức tối thiểu** | *(e.g. 80)* | *(e.g. 80)* |
| **Mức tối đa** | *(e.g. 120)* | *(e.g. 120)* |

> The system auto-calculates intermediate values. Only Min and Max rows are required.

---

## Generation Workflow

### Step 1: Gather Context
1. **Ask for or detect** the review period type (`probation` / `quarterly` / `annual`).
2. **Ask for or detect** `start_date` and `end_date`.
3. **Identify all concurrent projects** the user is involved in.
4. **Read project context** from `docs/inputs/` and `docs/outputs/` (BRD, URD, Action Plans, Gap Analysis Reports, etc.).
5. **Ask**: *"Có khả năng phát sinh DA ad-hoc trong kỳ đánh giá không?"*

### Step 2: Scope Milestones per Project
1. **Calculate working weeks** between `start_date` and `end_date`.
2. **Assess project size** (Small/Medium vs Large/Complex) from context documents.
3. **Apply BA Controls Principle**: Filter out any milestone that depends on Dev/Ops.
4. **Split into 3-4 milestones** evenly across the review period, each with 25% or 33% weight.
5. **Assign realistic deadline** for each milestone based on working weeks available.

### Step 3: Allocate Weights
1. **Determine weight split** based on number of parallel projects and ad-hoc likelihood.
2. **Validate**: Total weights across all KPI Goals MUST sum to 100%.

### Step 4: Generate KPI Forms
1. **Output one form per project**, following the 13-field template exactly.
2. **Format for direct copy-paste** into the HR system (use code blocks for long text fields).
3. **Include Performance Criteria Table** with realistic Min (80) and Max (120) benchmarks.

### Step 5: Generate Timeline Overview
1. **Create a parallel timeline** showing all projects' milestones side-by-side.
2. **Highlight weeks where milestones overlap** across projects (workload peaks).
3. **Flag any scheduling conflicts** or unrealistic compression.

---

## Output Format Template

For each project, generate the following copy-paste-ready block:

```
═══════════════════════════════════════════════════
📝 FORM KPI: [TÊN DỰ ÁN]
═══════════════════════════════════════════════════

Tên mục tiêu:
[Goal title text - max 500 chars]

Phân quyền xem: Công khai

Mô tả:
[Milestone breakdown - max 4000 chars]

Chỉ số KPI:
[Measurable metrics - max 4000 chars]

Đơn vị tính: %

Công thức:
[Formula text]

Trọng số: [XX] %

Ngày bắt đầu: [DD-MM-YYYY]
Ngày kết thúc: [DD-MM-YYYY]
Mục tiêu: 100
Thực tế: 0
% hoàn thành: 0 %
Khả năng thành công: Cao
Trạng thái: Đang thực hiện

Ghi chú (Thang điểm):
┌─────────────────┬───────────────┬──────────┐
│ Mô tả           │ % Hoàn thành  │ Xếp hạng │
├─────────────────┼───────────────┼──────────┤
│ Mức tối thiểu   │ [XX]          │ [XX]     │
│ Mức tối đa      │ [XX]          │ [XX]     │
└─────────────────┴───────────────┴──────────┘
```

---

## Quality Checklist (Post-Generation Audit)

After generating all KPI forms, validate against this checklist:

| # | Check | Pass? |
|---|---|---|
| 1 | Every milestone is 100% within BA's control (no Dev/Ops dependencies) | ☐ |
| 2 | Milestone deadlines are spaced evenly across the review period | ☐ |
| 3 | Total weight across all KPI Goals sums to exactly 100% | ☐ |
| 4 | Each milestone has a clear, measurable deliverable (document/artifact) | ☐ |
| 5 | Performance Criteria Min ≥ 70 and Max ≤ 120 | ☐ |
| 6 | No milestone deadline falls on weekends or public holidays | ☐ |
| 7 | Parallel project timelines do not have >2 milestones due in the same week | ☐ |
| 8 | Project-specific context from docs/inputs/ or docs/outputs/ was referenced | ☐ |
| 9 | NDA sanitization applied (no real client names if official_export ≠ true) | ☐ |
| 10 | `output_language` correctly applied to all labels and descriptions | ☐ |

---

## NVG Terminology Conventions (Inherited)

- **Ma trận Phân quyền & Thẩm quyền** → Always use **"Ma trận AM"** (Authority Matrix).
- **Tài liệu Yêu cầu Nghiệp vụ** → **BRD** (Business Requirements Document).
- **Tài liệu Đặc tả Chi tiết** → **SRS** (Software Requirements Specification).
- **Hồ sơ Kiểm thử Nghiệm thu** → **UAT Package** (Test Cases Matrix + User Guide).
- Refer to stakeholders by role title, not personal name, unless `official_export=true`.

---

## HR System Approval Workflow (Luồng Phê duyệt trên Hệ thống)

After filling in all 13 fields and saving the Goal form, the HR system requires an **approval workflow** before the KPI is officially active.

### Workflow Steps

```
┌──────────────┐     ┌──────────────────────┐     ┌──────────────┐
│  Nhân viên   │────▶│  Gửi QLTT phê duyệt  │────▶│    QLTT      │
│  (Tạo Goal)  │     │  (Submit to Manager)  │     │  (Phê duyệt) │
└──────────────┘     └──────────────────────┘     └──────────────┘
```

| Step | Actor | Action | Ghi chú |
|---|---|---|---|
| 1 | **Nhân viên** | Điền đầy đủ 13 trường → Nhấn **"Lưu"** | Lưu nháp, chưa gửi duyệt |
| 2 | **Nhân viên** | Nhấn **"Gửi QLTT phê duyệt"** | Popup xác nhận: *"Bạn sắp gửi biểu mẫu này cho người tiếp theo được chỉ định trong luồng công việc"* |
| 3 | **Nhân viên** | Điền **Nhận xét** (optional) → Nhấn **"Gửi QLTT phê duyệt"** | Biểu mẫu chuyển tiếp đến QLTT (Quản lý trực tiếp) |
| 4 | **QLTT** | Review → **Phê duyệt** hoặc **Từ chối** (trả lại kèm nhận xét) | Nếu từ chối: Nhân viên chỉnh sửa và gửi lại |

### Suggested "Nhận xét" Template (Copy-paste ready)

When submitting for approval, agent SHOULD generate a concise comment summarizing the KPI scope:

```
Kính gửi Anh/Chị,

Em gửi KPI thử việc gồm [X] mục tiêu cho [X] dự án song song:
1. [Tên DA 1] (Trọng số [XX]%): [Tóm tắt deliverables chính]
2. [Tên DA 2] (Trọng số [XX]%): [Tóm tắt deliverables chính]
[3. Nhiệm vụ ad-hoc / hỗ trợ phát sinh (Trọng số [XX]%)]

Tổng trọng số: 100%. Kính nhờ Anh/Chị review và phê duyệt.
Trân trọng.
```

### Key Terms in HR System UI

| UI Label (Vietnamese) | Meaning | Context |
|---|---|---|
| **QLTT** | Quản lý trực tiếp (Direct Manager) | Người phê duyệt KPI đầu tiên |
| **Gửi QLTT phê duyệt** | Submit to Direct Manager for approval | Nút gửi form lên cấp trên |
| **Nhận xét** | Comment / Remark | Ghi chú khi gửi hoặc phê duyệt/từ chối |
| **Lưu** | Save (Draft) | Lưu nháp, chưa gửi |
| **Hủy** | Cancel | Hủy thao tác hiện tại |
| **Đang thực hiện** | In Progress | Trạng thái mặc định khi tạo mới |
| **Điểm đánh giá** | Evaluation Score | Điểm do QLTT chấm sau kỳ đánh giá |

