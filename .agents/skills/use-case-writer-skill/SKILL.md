---
name: use-case-writer
description: |
  Generate Use Case specifications in English or Vietnamese Markdown following the IT BA standard 16-field template (Karl Wiegers / IIBA, extended). 
  Use whenever a BA needs to scope, analyze, document, refine, or review a Use Case. 
  Triggers include "write a use case", "draft UC", "use case specification", "analyze UC scope", "split feature into use cases", "review my UC", "write normal course / alternative course / exceptions", "define actors", and Vietnamese equivalents like "viết use case", "viết UC", "đặc tả use case", "phân tích use case", "review UC".
  Skill enforces Cockburn's guidelines (coffee-break test, goal levels) and runs a 20-point quality checklist. 
  Output language is controlled by the `output_language` session variable (default: `en`; set to `vi` for Vietnamese).
author: Phúc NT @ BA Zone
source: https://github.com/ba-zone/ba-zone-use-case-writer
---

# Use Case Writer — Skill for IT Business Analysts
> by **Phúc NT** · BA Zone · Digital School

This skill guides IT Business Analysts to **scope, analyze, and document Use Cases** in English or Vietnamese Markdown following the industry standard 16-field template (Karl Wiegers / IIBA style, extended), integrating best practices from Alistair Cockburn's *"Writing Effective Use Cases"* and the IIBA BABOK Guide.

---

## When to Use This Skill

Trigger this skill whenever the user needs to:
- Draft a new Use Case from a feature description, BRD, or PRD.
- Refine or review an existing UC for completeness and correctness.
- Split a large, complex feature into a structured list of discrete Use Cases.
- Detail specific UC sections: Normal Course, Alternative Courses, or Exceptions.
- Validate a UC document against the 20-point IIBA quality checklist.

---

## Session Variable: `output_language`

This skill uses a session variable to determine the language of the final Use Case document:

| Variable | Values | Default | Description |
|---|---|---|---|
| `output_language` | `en` (English) · `vi` (Vietnamese) | `en` | Controls artifact labels and generated content |

### Usage Rules:
1. **Setting the variable**: User can state `set output_language=en` / `set output_language=vi`, or naturally say *"write in English"* / *"viết bằng tiếng Việt"*.
2. **Persistence**: Once set, `output_language` applies to all subsequent UC documents generated in the session.
3. **Conversational vs. Document Language**: Always chat with the user in the language they use (English or Vietnamese). `output_language` **only** dictates the language of the produced Use Case specification.
4. **Session start rule**: If the user's initial prompt is in Vietnamese and requests a Use Case without specifying a language preference, briefly ask: *"Bạn muốn Use Case document xuất ra bằng tiếng Anh hay tiếng Việt? (output_language=en/vi)"*.

### 16 Fields Bilingual Label Mapping:

| # | English Field Label (`en`) | Vietnamese Field Label (`vi`) | Group |
|---|---|---|---|
| 1 | Use Case ID | Mã Use Case | Group 1 |
| 2 | Use Case Name | Tên Use Case | Group 1 |
| 3 | Created By & Date | Người tạo & Ngày tạo | Group 1 |
| 4 | Last Updated By & Date | Người cập nhật & Ngày cập nhật | Group 1 |
| 5 | Primary Actor | Tác nhân chính | Group 1 |
| 6 | Description | Mô tả | Group 1 |
| 7 | Preconditions | Tiền điều kiện | Group 2 |
| 8 | Postconditions | Hậu điều kiện | Group 2 |
| 9 | Priority | Độ ưu tiên | Group 2 |
| 10 | Frequency of Use | Tần suất sử dụng | Group 2 |
| 11 | Normal Course of Events | Luồng sự kiện chính | Group 3 |
| 12 | Alternative Courses | Luồng sự kiện thay thế | Group 4 |
| 13 | Exceptions | Luồng ngoại lệ | Group 4 |
| 14 | Includes | Use Case liên kết | Group 5 |
| 15 | Special Requirements | Yêu cầu đặc biệt | Group 5 |
| 16 | Assumptions & Notes | Giả định & Ghi chú | Group 5 |

---

## Output Rules (Non-negotiable)

1. **Language Control**: Strictly honor `output_language`. All headers, labels, and narrative content must match the selected language.
2. **Format**: Clean Markdown tables (`.md`) matching the 16-field standard template.
3. **Sequential Delivery**: Deliver the Use Case **one section group at a time**, then **stop and confirm** with the user before proceeding to the next group. Never output all 16 fields at once unless explicitly requested with *"give me the full UC at once"*.

---

## 4-Step Standard Workflow

```
Step 1: CLASSIFY & CONTEXT  → Determine mode (A/B/C/D) & confirm output_language
Step 2: SCOPE THE UC        → Apply Cockburn Coffee-break test & Goal levels
Step 3: WRITE SEQUENTIALLY  → Fill the 16 fields across 5 Section Groups (stop & verify)
Step 4: VALIDATE CHECKLIST  → Execute the 20-point IIBA quality audit
```

### Step 1: Classify Input & Pick a Mode
- **Mode A (New UC)**: User provides feature info -> Proceed to Step 2 & 3.
- **Mode B (Split Feature)**: User asks how many UCs are needed -> Output UC list first, then let user choose which to detail.
- **Mode C (Refine/Review)**: User inputs existing UC -> Jump directly to Step 4.
- **Mode D (Specific Section)**: User wants only Normal Course, Exceptions, etc. -> Detail that section directly.

*If input is vague (e.g. 1 short sentence), ask max 3 clarifying questions:*
1. Who is the primary actor?
2. What is the actor's primary business goal?
3. Which system / module does this belong to?

### Step 2: Scope the Use Case
Enforce Alistair Cockburn's core principles:
- **Coffee-break Test**: Can the actor complete this task and take a coffee break feeling it is finished? If no, it is a sub-function, not a full UC.
- **Goal Level**: Must be **User-goal level (Sea level)**. Avoid Summary level (Cloud - too big) or Sub-function level (Fish - too low-level, make it an `Include` or step).
- **Rule of One**: 1 primary actor + 1 discrete business goal + 1 continuous session.

### Step 3: Write the Use Case (5 Section Groups)

#### Group 1: Identity & Actor
- **ID**: `UC-[MODULE]-[NN]` (e.g., `UC-AUTH-01`).
- **Name**: Active Verb + Specific Object (e.g., `Enroll in Course`, `Đăng ký khóa học`).
- **Created/Updated**: Author & Date.
- **Actor**: Specific role / user persona (never just "User").
- **Description**: 2-3 sentences covering Why (business context), What (action), Outcome.

#### Group 2: Context & Constraints
- **Preconditions**: Concrete, verifiable system states that MUST exist before execution (e.g., "Learner is authenticated and course has available slots").
- **Postconditions**: Guaranteed system state changes upon successful completion (data saved, notifications dispatched, status updated).
- **Priority**: High / Medium / Low (with business rationale).
- **Frequency of Use**: Quantified estimate (e.g., "~500 enrollments/day").

#### Group 3: Normal Course of Events (Happy Path)
- Numbered sequential steps (`1.`, `2.`, `3.`, ...).
- **Strict alternation**: Clearly alternate between Actor action and System response.
- **Atomic actions**: 1 action per step. No embedded `if/else` logic in normal flow.

#### Group 4: Alternative Courses & Exceptions
- **Alternative Courses**: Numbered `UC-XX.AC.1`. Must explicitly specify **"At step N"**, trigger condition, flow of events, and where it branches back.
- **Exceptions**: Numbered `UC-XX.EX.1`. Must include:
  1. Trigger event / error condition.
  2. System response (logging, user notification).
  3. Final system state (transaction rolled back, session state preserved).

#### Group 5: Supplemental & Non-Functional
- **Includes**: Referenced reusable sub-use cases (e.g., `UC-AUTH-02: Verify OTP`).
- **Special Requirements**: Non-functional requirements specific to this UC (performance, SLA, security, regulatory constraints).
- **Assumptions**: Environmental or operational premises.
- **Notes & Issues**: Open questions or dependencies.

---

## Step 4: Quality Checklist (20 Points)

Before final sign-off, evaluate the generated Use Case against the 20-point audit matrix:

| Category | # | Inspection Item | Pass Criteria |
|---|---|---|---|
| **Scope** | 1 | Goal Level | User-goal level (passes Coffee-break test) |
| | 2 | UC Name | Active Verb + Noun Phrase |
| | 3 | Unique ID | Follows `UC-[MODULE]-[NN]` convention |
| | 4 | Primary Actor | 1 specific, non-generic role |
| **Context** | 5 | Description | Contains Why + What + Outcome |
| | 6 | Preconditions | Verifiable state; not an assumption or action |
| | 7 | Postconditions | Complete system change on success |
| | 8 | Priority & Frequency | Clearly stated and quantified |
| **Normal Course** | 9 | Numbered Steps | Sequential integers |
| | 10 | Alternation | Alternates between Actor and System |
| | 11 | Step Atomicity | 1 action per step; no branching if/else |
| | 12 | End State | Culminates in achievement of the primary goal |
| **Branches** | 13 | AC Branch Point | Every AC references "At step N" of Normal Course |
| | 14 | AC Rejoin/Exit | AC clearly states where it rejoins or terminates |
| | 15 | Exception Trigger | Clear failure / error trigger identified |
| | 16 | System Protection | Rollback / state preservation explicitly stated |
| | 17 | Error Notification | User receives actionable, friendly feedback |
| **Supplemental** | 18 | Includes | Only genuine sub-functions, properly prefixed |
| | 19 | Special Requirements | Truly non-functional constraints (not general rules) |
| | 20 | Assumptions | Distinguishes external assumptions from preconditions |

Output a brief validation summary table (`Item | Status [✅/⚠️/❌] | Notes`) before finalizing the document.
