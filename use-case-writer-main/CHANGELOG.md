# Changelog · BA Zone Use Case Writer

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

> Maintained by **Phúc NT** · BA Zone · Digital School

---

## [1.0.3] - 2026-05-16

### Added
- `assets/uc-template-vi.md` — full Vietnamese copy-ready template with translated field labels, LTT/NL notation (Luồng Thay Thế / Ngoại Lệ), and an Anh–Việt field label reference table
- `SKILL.md` now references the correct template file based on `output_language`: `uc-template.md` for `en`, `uc-template-vi.md` for `vi`
- Vietnamese notation convention: Alternative Course IDs use `UC-XX-YY.LTT.N`, Exception IDs use `UC-XX-YY.NL.N`; UC IDs and file names remain ASCII for tooling compatibility

### Changed
- README.md repo structure tree and installation verification tree updated to include `uc-template-vi.md`
- `SKILL.md` References section updated with both template files

---

## [1.0.2] - 2026-05-16

### Added
- `output_language` session variable in `SKILL.md` to control UC artifact language (`en` = English, default; `vi` = full Vietnamese). The variable applies to the entire UC document — all field labels, content, Normal Course steps, Alternative Courses, Exceptions, everything. Conversational language between skill and user is unaffected.
- Trigger phrases for setting the variable: `set output_language=vi`, "write in Vietnamese", "UC bằng tiếng Việt", and equivalents
- Auto-detect logic at session start: if the user's first message is in Vietnamese with a UC request, skill asks once for language preference before proceeding
- File naming note: filename slug stays in English (ASCII-safe) even when `output_language=vi`

### Changed
- `SKILL.md` workflow box updated to reflect 16-field count and `output_language` detection in Step 1
- README.md Usage section now includes an `output_language` reference table
- README.md Features list updated: "Bilingual interaction" → "Bilingual output" with variable description

---

## [1.0.1] - 2026-05-16

### Fixed
- Corrected field count from "13-field" to "16-field" throughout README.md and SKILL.md, with an explanatory note clarifying that the original Wiegers template has 13 fields and this skill uses an extended 16-field version (adds Includes, Assumptions, Notes and Issues)
- Removed dangling reference to non-existent `ba-zone-user-story-ac-writer` skill in README.md "What this skill does NOT do" section
- Added out-of-scope note for UC-MENTOR-04 in `references/examples-edtech.md` (AC.1 of UC-MENTOR-03 referenced it without explanation)
- Fixed broken 4-column Markdown table header in `assets/uc-template.md` and both examples in `references/examples-edtech.md` — History rows now use a properly declared 4-column separator row so they render correctly across all Markdown renderers
- Updated `source` URL in `SKILL.md` front-matter to point to the specific repo instead of the org root

---

## [1.0.0] - 2026-05-14

### Initial release — BA Zone Edition

#### Added
- Core `SKILL.md` with 4-step workflow (Classify → Scope → Write → Validate)
- 4 operating modes: write new, split into UC list, refine existing, write specific section
- Sequential generation in 5 section groups with confirmation gates
- 20-point quality checklist (Groups A-F covering Scope, Actor, Conditions, Flow, AC/EX, Completeness)
- Alistair Cockburn's scoping rules: coffee-break test, 3 goal levels, system boundary
- 3 UC identification techniques: goal-driven, event-driven, CRUD-driven
- `references/template-guide.md` — field-by-field guidance with Digital School / EdTech examples
- `references/writing-style.md` — active voice rules, numbering conventions, 10 anti-patterns
- `references/quality-checklist.md` — full 20-point checklist with pass/fail examples
- `references/examples-edtech.md` — 2 complete EdTech UC examples:
  - UC-LEARN-01: Enroll in a Digital School course
  - UC-MENTOR-03: Approve learner 1-on-1 mentor session request
- `assets/uc-template.md` — copy-ready Markdown template

#### Configuration
- Output language: English (artifact always in English regardless of user's chat language)
- Output format: Markdown with 2-column table layout
- Workflow mode: Sequential (section-by-section with confirmation gates)
- Domain examples: EdTech / Digital School (replaces generic banking examples)

#### Attribution
- Author: Phúc NT · BA Zone · Digital School
- License: MIT with attribution requirement
