---
name: user-story-writer
description: |
  Generate User Stories and Acceptance Criteria compliant with INVEST and Gherkin (Given-When-Then) standards for IT BAs and Product Owners.
  The skill enforces 6 INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) and mandates at least 3 AC scenarios covering Happy path, Edge case, and Negative path.
  Supports 3 modes: drafting from scratch, refining existing stories, and detailing Acceptance Criteria.
  Bilingual support via `output_language` variable (`en` default, `vi` for Vietnamese).
author: Phúc NT @ BA Zone
source: https://github.com/ba-zone
---

# User Story & Acceptance Criteria Writer — Skill for IT BAs & POs
> by **Phúc NT** · BA Zone · Digital School

This skill helps Business Analysts and Product Owners author **high-quality User Stories (US)** and **Acceptance Criteria (AC)** ready for developer estimation and QA test case generation.

---

## When to Use This Skill

Trigger this skill whenever the user says:
- *"Write user story"*, *"draft US"*, *"create user story"*, *"viết user story"*, *"viết US"*.
- *"Write acceptance criteria"*, *"AC Given-When-Then"*, *"Gherkin AC"*, *"tiêu chí nghiệm thu"*.
- *"Review this user story"*, *"refine US"*, *"check INVEST criteria"*, *"US này đã chuẩn chưa"*.
- *"Split user story"*, *"story is too big"*, *"tách story"*.
- Pastes a feature requirement or PRD excerpt and asks for User Stories.

*Do NOT use this skill for formal Use Case specifications (use `use-case-writer`), entire SRS documents, or technical test scripts.*

---

## Session Variable: `output_language`

This skill uses a session variable to control the language of the produced User Story & AC document:

| Variable | Values | Default | Description |
|---|---|---|---|
| `output_language` | `en` (English) · `vi` (Vietnamese) | `en` | Controls story statement, table labels, and AC wording |

### Usage Rules:
1. **Setting**: The user can set it explicitly (`set output_language=en` or `set output_language=vi`) or via prompt (`"viết bằng tiếng Việt"`, `"write in English"`).
2. **Persistence**: The variable remains active for the remainder of the session unless changed.
3. **Conversational Language**: Always communicate with the user in the language they write in. The variable strictly dictates the language of the generated artifact.
4. **Initial check**: If the user's initial prompt is in Vietnamese and doesn't specify a language, ask once: *"Bạn muốn User Story & AC document xuất ra bằng tiếng Anh hay tiếng Việt? (output_language=en/vi)"*.

### Story & AC Language Structure:

| Section | English (`en`) | Vietnamese (`vi`) |
|---|---|---|
| **Role** | As a [specific persona] | Là một [vai trò cụ thể] |
| **Action** | I want to [specific action] | Tôi muốn [hành động cụ thể] |
| **Value** | So that [measurable business value] | Để [giá trị kinh doanh đo lường được] |
| **AC Given** | Given [precondition] | Cho biết [tiền điều kiện] |
| **AC When** | When [user action] | Khi [hành động của người dùng] |
| **AC Then** | Then [expected outcome] | Thì [kết quả mong đợi] |
| **AC And** | And [additional condition/result] | Và [điều kiện hoặc kết quả bổ sung] |

---

## 6-Step Standard Workflow

```
Step 1: DETERMINE MODE       → Mode A (New), Mode B (Refine), or Mode C (Add ACs)
Step 2: GATHER CORE INPUTS   → Validate 4 required inputs: Persona, Goal, Value, Context
Step 3: WRITE STORY HEADER   → Apply As a / I want / So that (or Là một / Tôi muốn / Để)
Step 4: INVEST SELF-CHECK    → Evaluate against 6 INVEST criteria with ✅/⚠️
Step 5: DRAFT ACs (GHERKIN)  → Author min 3 ACs: Happy Path, Edge Case, Negative Path
Step 6: FINAL POLISH & NOTES → Summarize dependencies, open questions, PO clarifications
```

### Step 1: Identify Working Mode
- **Mode A (Draft New)**: Feature description provided -> Extract persona, goal, value -> Draft full US & AC.
- **Mode B (Refine)**: User provides existing US/AC -> Audit against INVEST & rewrite weak points.
- **Mode C (Detail ACs)**: User already has accepted US -> Author comprehensive Given-When-Then scenarios.

### Step 2: Gather Required Inputs
Before generating, ensure all 4 elements are present:
1. **Specific Persona**: Role who directly benefits (e.g. *"Authenticated Course Learner"*, never generic *"User"*).
2. **Clear Goal**: What concrete action the persona needs to perform.
3. **Business Value**: Why this capability matters (must be distinct from the goal itself).
4. **Context / Feature Boundary**: Which module or epic this belongs to.

*If any element is missing or ambiguous, ask before drafting.*

### Step 3: Write User Story Statement

Follow the standard 3-line format with ID:
```
**US-[MODULE]-[NN]**: [Concise, Descriptive Title]

**As a** [specific persona, not generic]
**I want to** [specific measurable action]
**So that** [clear business outcome / value]
```

### Step 4: Apply INVEST Checklist

Every User Story must be validated against the 6 INVEST principles before delivery:

| Criterion | Guiding Question | Remediation Action |
|---|---|---|
| **I - Independent** | Can this story be developed and released on its own? | Decouple dependencies or merge tightly coupled stories. |
| **N - Negotiable** | Does it describe intent rather than a rigid UI/tech implementation? | Strip out explicit CSS, database schemas, or API endpoints. |
| **V - Valuable** | Is the business value clear to stakeholders? | Rewrite the "So that" clause to reflect end-user benefit. |
| **E - Estimable** | Can the engineering team reliably estimate effort? | Clarify business rules and scope boundaries. |
| **S - Small** | Can it be completed within 1 sprint (typically 1-3 story points)? | Split across CRUD operations, personas, or workflows. |
| **T - Testable** | Can QA define binary pass/fail test criteria? | Write unambiguous Acceptance Criteria. |

### Step 5: Draft Acceptance Criteria (Minimum 3 Scenarios)

Every User Story **must include at least 3 distinct scenarios** in Gherkin syntax (`Given-When-Then`):

1. **Happy Path (Kịch bản chuẩn)**: The standard success scenario where valid data is processed smoothly.
2. **Edge Case / Boundary Validation (Kịch bản biên)**: Extreme inputs, empty states, limits, or format checks.
3. **Negative / Error Path (Kịch bản lỗi)**: System failure, invalid credentials, unauthorized access, or duplicate records.

#### Gherkin Rules:
- **Given**: Initial context / verifiable system state before the action.
- **When**: Specific user trigger or event.
- **Then**: Observable, testable outcome (status change, message, record creation).
- **And**: Conjunction for additional preconditions or outcomes.
- Avoid technical jargon (e.g. write *"System displays 'Email already registered'"*, not *"Backend returns HTTP 409 Conflict with JSON payload"*).

### Step 6: Final Output Structure

Present the completed specification in this order:
1. **User Story Title & Statement** (As a / I want / So that)
2. **INVEST Evaluation Table** (with ✅ / ⚠️ ratings and brief commentary)
3. **Acceptance Criteria** (AC1 Happy Path, AC2 Edge Case, AC3 Negative Path)
4. **Notes & Open Questions** (Technical constraints, dependencies, questions for PO)

---

## Anti-Patterns to Avoid

- ❌ **Generic Persona**: *"As a user, I want..."* -> ✅ *"As a verified customer with an active subscription..."*
- ❌ **Circular Value**: *"I want to export PDF so that I can have a PDF"* -> ✅ *"I want to export PDF so that I can submit the monthly expense report to accounting offline"*.
- ❌ **Overly Technical ACs**: *"Then the API returns status 200 with JWT token"* -> ✅ *"Then the user is authenticated and redirected to the personalized dashboard"*.
- ❌ **Missing Negative Path**: Only documenting what happens when everything works.
- ❌ **Epic disguised as a Story**: Containing multiple full CRUD operations in one story (e.g. *"Manage all student accounts"*).
