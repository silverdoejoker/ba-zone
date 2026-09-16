---
inclusion: fileMatch
fileMatchPattern: "**/assets/uc-template*.md"
---

# UC Template Steering

When a UC template file is in context, apply these rules:

## Template Selection

- `output_language=en` → use `assets/uc-template.md` (English)
- `output_language=vi` → use `assets/uc-template-vi.md` (Vietnamese)

## Vietnamese Notation (when output_language=vi)

| English | Vietnamese |
|---|---|
| AC.N (Alternative Course) | LTT.N (Luồng Thay Thế) |
| EX.N (Exception) | NL.N (Ngoại Lệ) |
| Primary / Secondary | Chính / Phụ |
| High / Medium / Low | Cao / Trung bình / Thấp |

## Invariants (both languages)

- UC ID format remains ASCII: `UC-<module>-<seq>`
- File naming remains English slug: `UC-LEARN-01_enroll-digital-school-course.md`
- LTT/NL codes remain ASCII
- Table structure: 2-column layout for main fields, 4-column for History row

## When User Copies the Template

Remind them to:
1. Replace ALL `<...>` placeholders
2. Remove example text
3. Keep the table alignment markers (`| ---: | :--- |`)
4. Maintain attribution line at the bottom

#[[file:assets/uc-template.md]]
#[[file:assets/uc-template-vi.md]]
