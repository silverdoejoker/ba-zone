# Standard Document Blueprint Schema
> Template chuẩn của **BA Zone** · Doc Template Learner Skill

When reverse-engineering a document template, summarize the extracted structure using this standardized schema:

```yaml
document_blueprint:
  name: "Document Name / Type (e.g. BRD / SRS / FSD)"
  source_file: "path/to/reference/sample.md"
  output_language: "en | vi"
  tone: "Formal enterprise | Technical specification | Agile functional"
  numbering_scheme:
    requirement_prefix: "REQ- | FR- | BR- | UC-"
    heading_style: "Numbered (1., 1.1) | Topic-based"
  metadata_block:
    fields:
      - Project Name
      - Document Version
      - Author & Date
      - Approval Matrix
      - Revision History
  sections:
    - id: "sec-01"
      level: 1
      title: "Section Title"
      purpose: "Brief explanation of what goes here"
      components:
        - type: "table | text | mermaid_diagram | bullet_list"
          headers: ["Column 1", "Column 2", "Column 3"]
      subsections:
        - id: "sec-01-01"
          level: 2
          title: "Sub-section Title"
          components:
            - type: "text"
```
