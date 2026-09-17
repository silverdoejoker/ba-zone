# User Story: US-COURSE-01 - Filter Courses by Category
> Sample Reference · **BA Zone** (Agile INVEST & Gherkin Standard)

**US-COURSE-01**: Filter Courses by Category

**As an** authenticated student browsing the catalog  
**I want to** filter the available courses by categories and price range  
**So that** I can rapidly find learning materials suited to my skill development needs  

---

### INVEST Evaluation

| Criterion | Status | Evaluation & Commentary |
|---|---|---|
| **Independent** | ✅ PASS | Can be developed and deployed independently of course purchase workflow. |
| **Negotiable** | ✅ PASS | Defines search and filtering intent without prescribing rigid UI components. |
| **Valuable** | ✅ PASS | Significantly reduces search friction for registered learners. |
| **Estimable** | ✅ PASS | Well-defined filter parameters allow straightforward backend query estimation. |
| **Small** | ✅ PASS | Self-contained story deliverable in a single iteration. |
| **Testable** | ✅ PASS | Acceptance criteria below provide deterministic validation rules. |

---

### Acceptance Criteria (Gherkin Format)

#### AC1: Filter with Matching Results (Happy Path)
- **Given** the student is on the course catalog page with multiple courses listed
- **When** the student selects category "Data Analytics" and applies the filter
- **Then** the page displays only courses tagged with "Data Analytics"
- **And** the total matching course count is updated accurately

#### AC2: Apply Filters with No Matching Results (Edge Case)
- **Given** the student selects a combination of filters with 0 matching courses
- **When** the filter is submitted
- **Then** the system displays an empty state message "No courses match your criteria"
- **And** provides a "Clear All Filters" shortcut button

#### AC3: Network Timeout / Server Failure (Negative Path)
- **Given** an intermittent network connection while fetching filtered course data
- **When** the student triggers the filter
- **Then** the system displays a non-blocking notification "Unable to load courses. Please retry."
- **And** preserves the previously selected filter checkboxes without crashing

---

### Notes & Dependencies
- **Dependencies**: Category metadata API must be available.
