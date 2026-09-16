---
name: doc-template-learner
description: |
  Learn, reverse-engineer, and replicate document structures and templates from any reference document (BRD, URD, SRS, FSD, PRD, Architecture Design, etc.).
  The skill extracts a comprehensive "Document Structural Blueprint" (metadata, heading hierarchy, section contracts, table layouts, Mermaid diagram styles, and writing tone),
  then generates a new document matching the exact template layout but populated with new project content from user prompts, notes, or attachments.
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
- **SRS (Software Requirements Specification)**: IEEE 830 / ISO 29148 standards, approval pages, revision history, system interfaces, detailed functional requirements, and non-functional requirements.
- **FSD (Functional Specification Document)**: UI screens, data dictionary, system state machines, API contracts, and screen-by-screen business rules.
- **Custom Internal Frameworks**: Confluence templates, client-mandated deliverables, or proprietary company formats.

Instead of forcing a one-size-fits-all format, this skill **learns your template** and produces documents that feel as if they were written by your company's senior lead BA.

---

## When to Use This Skill

Trigger this skill whenever the user:
- Provides a reference document (file path, attachment, or pasted markdown) and says:
  - *"Learn this template and write a BRD for my new feature..."*
  - *"Dựa vào template SRS này để viết SRS cho hệ thống..."*
  - *"Clone cấu trúc của tài liệu này nhưng áp dụng cho dự án..."*
  - *"Viết FSD theo format giống file đính kèm..."*
- Asks to extract or standardize a reusable document blueprint from an existing artifact.
- Needs to convert unstructured notes, user stories, or meeting transcripts into a formal enterprise document matching an approved organizational template.

---

## Session Variable: `output_language`

| Variable | Values | Default | Description |
|---|---|---|---|
| `output_language` | `en` (English) · `vi` (Vietnamese) | `en` | Controls headings, field labels, and generated prose |

### Language Rules:
1. **Inheritance Rule**: If not specified, default to `en`. If the reference template is clearly in Vietnamese (e.g. headers like *"Tổng quan dự án"*, *"Phạm vi"*), default `output_language=vi` unless the user specifies otherwise.
2. **Translation Mode**: The skill can ingest an English template and produce a Vietnamese document, or vice versa, translating all structural labels while preserving exact layout and numbering schemas.
3. **Conversational Language**: Always chat with the user in the language they converse in.

---

## 5-Phase Workflow

```
Phase 1: INGEST & DECONSTRUCT   → Analyze reference template & sample content
Phase 2: EXTRACT BLUEPRINT       → Build & confirm Document Structural Blueprint
Phase 3: INGEST TARGET INPUT     → Ingest user prompt, notes, attachments, or Q&A
Phase 4: GENERATE TARGET DOC     → Produce new doc (Interactive by chapter or Batch)
Phase 5: PARITY AUDIT & HANDOVER → Verify 100% structural alignment against Blueprint
```

---

### Phase 1: Ingest & Deconstruct Reference Document

The user provides a reference sample via file path (e.g., `use-case-writer-main/BRD_Semantic_Search_527432316.md`), attachment, or pasted text.

Analyze and extract the following structural elements:
1. **Document Identity**: Document Type (BRD, SRS, FSD, URD, Architecture Doc).
2. **Front Matter / Metadata Block**: Cover block, Approval matrix, Revision history table, Project info table.
3. **Heading Hierarchy (TOC)**: Exact depth and numbering scheme (e.g. `1.`, `1.1`, `1.1.1` or `Chapter 1`, `Section 1.1`).
4. **Section Contracts**:
   - What is each section intended to convey?
   - What data formats are used? (Markdown tables, bullet lists, numbered steps, callouts, Mermaid diagrams).
   - What naming conventions and prefixes are used? (e.g., `REQ-001`, `FR-XX`, `NFR-XX`, `UC-XX`).
5. **Tone & Style**:
   - Technical depth (high-level business vs. detailed technical).
   - Tone (formal third-person, imperative, active voice).
   - Specific recurring phrases (e.g., *"The system shall..."*, *"Hệ thống phải..."*).

---

### Phase 2: Formulate & Present Document Blueprint

Before generating large volumes of text, **present the extracted Blueprint to the user** in a clean, structured summary:

```markdown
### 📋 Learned Document Blueprint: [Document Type]
- **Source Template**: [Filename or source description]
- **Target Language**: `output_language` ([en/vi])
- **Tone & Style**: [Formal enterprise / Technical specification]
- **Heading Outline**:
  1. [Section 1 Title] (Format: Key-value table)
  2. [Section 2 Title]
     2.1 [Sub-section 2.1] (Format: 3-column matrix)
     2.2 [Sub-section 2.2] (Format: Mermaid flowchart)
  3. [Section 3 Title] (Format: Numbered requirement IDs `REQ-XX`)
  ...
- **Identified Inputs Needed**:
  - [List of specific business/technical inputs needed from user to fill this template]
```

*Ask user: "Cấu trúc blueprint này đã chính xác chưa? Bạn muốn sinh toàn bộ một lần (Batch) hay duyệt từng chương (Interactive)?"*

---

### Phase 3: Ingest Target Content & Map to Blueprint

Collect and synthesize input for the target document:
- User prompt (e.g. *"Write this for our new AI Booking Engine"*).
- Attached raw notes, meeting transcripts, Jira tickets, or user stories.
- Q&A responses: If critical inputs are missing (e.g., out-of-scope boundaries, performance SLAs), ask targeted, concise questions.
- If information is unstated, propose sensible, industry-standard defaults with `[DRAFT / TO BE CONFIRMED]` tags.

---

### Phase 4: Generate Target Document

Follow the user's preferred generation mode:

#### Mode 1: Interactive / Chapter-by-Chapter (Recommended for SRS, FSD, or Docs > 5 pages)
1. Output one major chapter/section group at a time.
2. Maintain identical formatting (tables, column headers, diagrams, callouts).
3. Stop and ask for feedback / adjustments before moving to the next section.
4. Seamlessly incorporate user feedback into subsequent sections.

#### Mode 2: Batch Generation (For BRDs, Concept Notes, or upon explicit request)
1. Generate the complete, fully formed document in one comprehensive Markdown artifact.
2. Ensure no placeholder text (`Lorem Ipsum`, `TBD`, `TODO`) is left without explicit justification.

---

### Phase 5: Structural Parity Audit & Handover

Before final delivery, run an automated structural parity comparison:

| Audit Check | Inspection Criteria |
|---|---|
| **Outline Parity** | Does every section and sub-section in the Blueprint exist in the generated doc? |
| **Table Parity** | Are table column headers, alignments, and formats 100% aligned with the template? |
| **ID Prefix Parity** | Do requirement identifiers follow the template convention (`REQ-XX`, `FR-XX`)? |
| **Diagram Parity** | Where the template had architecture/flow diagrams, are corresponding Mermaid diagrams included? |
| **Language Parity** | Are all labels, headings, and body text strictly in the selected `output_language`? |

Provide a final **Parity Confirmation Box**:
```markdown
> [!NOTE]
> **Structural Parity**: 100% aligned with reference template.
> All [N] sections, [M] tables, and requirement conventions replicated.
```

---

## Anti-Patterns to Avoid

- ❌ **Flattening Rich Formatting**: Turning complex markdown tables or Mermaid diagrams from the template into plain bulleted lists.
- ❌ **Generic Hallucinations**: Inventing unrelated technical stacks or business logic when user context is absent; always flag assumptions.
- ❌ **Dropping Metadata Blocks**: Omitting document control, approval matrices, or revision history tables present in the original template.
- ❌ **Language Mixing**: Mixing English labels into Vietnamese body text or vice versa (except standardized technical terms like API, OAuth, SLA).
- ❌ **Ignoring Negative Scopes**: Skipping the "Out of Scope" (Ngoài phạm vi) or "Assumptions" sections which are critical for BA contracts.
