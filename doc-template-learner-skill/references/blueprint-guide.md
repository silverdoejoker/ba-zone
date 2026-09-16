# Document Blueprint Extraction Guide

This guide provides deep technical patterns for reverse-engineering and cloning document templates across major Business Analysis standards: BRD, URD, SRS, and FSD.

---

## 1. Blueprint Archetypes

### Archetype A: BRD / URD (Business / User Requirements Document)
- **Primary Focus**: Business problem, high-level objectives, project ROI, scope boundaries, stakeholder personas, and operational business rules.
- **Typical Blueprint Structure**:
  ```markdown
  # [Document Title] (e.g., Business Requirements Document: Project X)
  
  | Metadata Field | Value |
  |---|---|
  | Project Name / Code | ... |
  | Business Owner / Stakeholders | ... |
  | Version / Date | ... |
  
  ## 1. Executive Summary & Business Context
  ### 1.1 Business Problem & Opportunity
  ### 1.2 Strategic Goals & Objectives
  
  ## 2. Project Scope
  | In Scope (Trong phạm vi) | Out of Scope (Ngoài phạm vi) |
  |---|---|
  | ... | ... |
  
  ## 3. Stakeholder & Persona Analysis
  | Persona Role | Description | Core Pain Points | Expected Business Outcome |
  |---|---|---|---|
  
  ## 4. High-Level Business Requirements (BR-XX)
  | ID | Requirement Description | Priority | Business Value / Justification |
  |---|---|---|---|
  
  ## 5. Assumptions, Constraints & Dependencies
  ```

---

### Archetype B: SRS (Software Requirements Specification - IEEE 830 / ISO 29148)
- **Primary Focus**: Complete behavioral specification of the software system, system interfaces, detailed functional requirements, performance, security, and verification criteria.
- **Typical Blueprint Structure**:
  ```markdown
  # Software Requirements Specification (SRS) for [System Name]
  
  ### Document Control & Approval Page
  | Role | Name | Signature | Date |
  |---|---|---|---|
  | Lead Business Analyst | ... | ... | ... |
  | Project Manager | ... | ... | ... |
  | Technical Architect | ... | ... | ... |
  | Product Sponsor | ... | ... | ... |
  
  ### Document Revision History
  | Version | Date | Author | Description of Changes |
  |---|---|---|---|
  
  ## 1. Introduction
  ### 1.1 Purpose
  ### 1.2 Scope of the Software
  ### 1.3 Definitions, Acronyms, and Abbreviations
  ### 1.4 References
  
  ## 2. Overall Description
  ### 2.1 Product Perspective (System Context Diagram / Mermaid)
  ### 2.2 Product Functions (Summary)
  ### 2.3 User Classes and Characteristics
  ### 2.4 Operating Environment
  ### 2.5 Design and Implementation Constraints
  ### 2.6 User Documentation
  ### 2.7 Assumptions and Dependencies
  
  ## 3. Specific System Requirements
  ### 3.1 External Interface Requirements
  #### 3.1.1 User Interfaces (UI)
  #### 3.1.2 Hardware Interfaces
  #### 3.1.3 Software Interfaces (APIs, Database, 3rd party)
  #### 3.1.4 Communications Interfaces (Protocols, Security)
  ### 3.2 Functional Requirements (FR-XX)
  #### 3.2.1 [Subsystem / Feature 1]
  - **FR-01.01**: [Requirement statement with 'The system shall...']
  - **Inputs / Outputs / Validations**
  - **Business Rules (BR-XX)**
  ### 3.3 Non-Functional Requirements (NFR-XX)
  - Performance, Availability, Reliability, Security, Maintainability.
  
  ## 4. Requirements Traceability Matrix (RTM)
  ```

---

### Archetype C: FSD (Functional Specification Document)
- **Primary Focus**: Screen-by-screen specifications, user interaction flows, data fields dictionary, validations, error codes, and state transitions.
- **Typical Blueprint Structure**:
  ```markdown
  # Functional Specification Document (FSD): [Module / Feature]
  
  ## 1. Feature Overview & Architecture Flow
  ```mermaid
  sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant DB
  ```
  
  ## 2. Screen Specifications (SCR-XX)
  ### 2.1 SCR-01: [Screen Name]
  - **UI Mockup / Wireframe Reference**: [Layout description or ASCII/Mermaid mock]
  - **Screen Elements & Data Dictionary**:
    | Field Name | Type | Length | Required | Default | Validation Rules | Description |
    |---|---|---|---|---|---|---|
    | Email | String | 100 | Yes | None | Regex email format | Login identifier |
  - **Button / Interaction Specifications**:
    | Control ID | Trigger Event | Condition | Action / System Response | Target Screen |
    |---|---|---|---|---|
  - **Screen State Machine**: (Normal state, Loading state, Error state, Empty state)
  
  ## 3. Data Processing & Business Rules
  - Calculations, batch processing, background jobs.
  
  ## 4. Error Code Dictionary
  | Error Code | HTTP Status | Display Message (EN) | Display Message (VI) | Root Cause |
  |---|---|---|---|---|
  ```

---

## 2. Structural Parity Verification Rules

When cloning a document template, the generated document must pass 5 parity tests:
1. **Header Depth Check**: If the template uses 3-level headings (`### 1.1.1`), the generated document must maintain identical depth.
2. **Table Schema Check**: Every table column name from the source template must have an exact equivalent in the target document.
3. **Identifier Format Check**: If source uses `FR-AUTH-001`, don't switch to `REQ-1`. Preserve the exact regex schema.
4. **Visual Diagram Presence**: If the source document contains Mermaid diagrams (flowcharts, sequence diagrams, ERDs), equivalent diagrams must be authored for the target domain.
5. **No Orphan Placeholders**: No remaining `[...]` or `TBD` placeholders in production output unless explicitly marked as pending stakeholder decision.
