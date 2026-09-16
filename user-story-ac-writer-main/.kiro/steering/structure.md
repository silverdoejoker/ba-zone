# Project Structure

```
user-story-ac-writer/
├── SKILL.md                        # Entry point — full AI behavioral instructions
├── README.md                       # Setup, usage, trigger phrases, example output
├── LICENSE                         # MIT License
├── templates/
│   ├── user-story-template.md      # Blank US template (As a / I want / So that + INVEST table)
│   └── ac-template.md              # Blank AC template (Given-When-Then, 3 scenario types)
├── references/
│   ├── invest-criteria.md          # Deep explanation of all 6 INVEST criteria with examples
│   └── examples.md                 # 7 sample US+AC pairs for EdTech/Digital School domain
└── _ checklists/
    └── quality-checklist.md        # Self-review checklist the AI runs before producing output
```

## File Roles

| File | Purpose |
|------|---------|
| `SKILL.md` | Primary instruction file. Defines workflow, modes, anti-patterns, split patterns, and output format. Always read this first. |
| `templates/user-story-template.md` | Reference when generating a new US — use the ID format `US-[FEATURE-CODE]-[NUMBER]` |
| `templates/ac-template.md` | Reference when generating AC — enforce Given/When/Then with And clauses |
| `references/invest-criteria.md` | Consult when evaluating or explaining INVEST compliance |
| `references/examples.md` | Consult for domain-specific patterns; contains 7 worked examples |
| `_ checklists/quality-checklist.md` | Run before every final output; fail any item → fix before returning |

## Conventions

- All content is in **Vietnamese** (primary language of the BA Zone community)
- US IDs follow the pattern: `US-[FEATURE-CODE]-[NUMBER]` (e.g., `US-MENTOR-BOOK-001`)
- AC are numbered sequentially: `AC1`, `AC2`, `AC3`...
- Every output includes: User Story → INVEST self-check table → Acceptance Criteria → Notes
- Do not add new file types or folders outside this structure without updating `README.md`
