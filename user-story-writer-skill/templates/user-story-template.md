# User Story & Acceptance Criteria Templates (Song Ngữ EN / VI)

This document contains standard Agile User Story and Acceptance Criteria templates compliant with INVEST criteria and Gherkin (Given-When-Then) syntax.

---

## 1. English Template (`output_language=en`)

```markdown
# User Story: US-[MODULE]-[NN] - [Story Title]

**US-[MODULE]-[NN]**: [Story Title]

**As an** [authenticated persona / specific role]  
**I want to** [perform a specific, measurable action]  
**So that** [achieve a clear business objective or quantifiable value]  

---

### INVEST Evaluation

| Criterion | Status | Evaluation & Commentary |
|---|---|---|
| **Independent** | ✅ PASS | Story can be planned, developed, and delivered independently. |
| **Negotiable** | ✅ PASS | Focuses on user intent rather than inflexible implementation constraints. |
| **Valuable** | ✅ PASS | Delivers clear, tangible value to the target persona. |
| **Estimable** | ✅ PASS | Boundaries and business rules are sufficiently defined for estimation. |
| **Small** | ✅ PASS | Scope fits comfortably within a single sprint iteration. |
| **Testable** | ✅ PASS | Binary pass/fail conditions are verifiable via the ACs below. |

---

### Acceptance Criteria (Gherkin Format)

#### AC1: Successful Execution (Happy Path)
- **Given** [concrete initial condition / system state]
- **When** [user performs the primary valid action]
- **Then** [expected success state or output is produced]
- **And** [secondary state update or notification sent]

#### AC2: Boundary / Validation Check (Edge Case)
- **Given** [boundary conditions or input limits]
- **When** [user enters input at the upper or lower boundary]
- **Then** [system processes valid edge values or enforces format rules]

#### AC3: Failure Handling & Error Messaging (Negative Path)
- **Given** [condition leading to failure, e.g. invalid input, expired session]
- **When** [user attempts to submit or proceed]
- **Then** [system halts operation and displays user-friendly error message]
- **And** [system state is safely preserved without partial commits]

---

### Notes & Assumptions
- **Dependencies**: [Pre-requisite features or external integrations]
- **Business Rules**: [Specific formulas, regulatory conditions, or thresholds]
- **Open Questions**: [Items requiring Product Owner clarification]
```

---

## 2. Vietnamese Template (`output_language=vi`)

```markdown
# Câu Chuyện Người Dùng: US-[MODULE]-[NN] - [Tiêu đề Story]

**US-[MODULE]-[NN]**: [Tiêu đề Story]

**Là một** [vai trò / persona cụ thể đã xác thực]  
**Tôi muốn** [thực hiện một hành động cụ thể, đo lường được]  
**Để** [đạt được mục tiêu nghiệp vụ hoặc giá trị rõ ràng]  

---

### Bảng Đánh Giá Tiêu Chuẩn INVEST

| Tiêu chí | Trạng thái | Đánh giá & Ghi chú |
|---|---|---|
| **Independent (Độc lập)** | ✅ ĐẠT | Story có thể được lên kế hoạch, phát triển và bàn giao độc lập. |
| **Negotiable (Thương lượng được)** | ✅ ĐẠT | Tập trung vào mong muốn của người dùng thay vì áp đặt giải pháp kỹ thuật cứng. |
| **Valuable (Có giá trị)** | ✅ ĐẠT | Mang lại giá trị nghiệp vụ rõ ràng cho đối tượng thụ hưởng. |
| **Estimable (Ước lượng được)** | ✅ ĐẠT | Phạm vi và quy tắc nghiệp vụ đủ rõ ràng để dev ước tính effort. |
| **Small (Vừa vặn)** | ✅ ĐẠT | Kích thước phù hợp để hoàn thành trọn vẹn trong 1 sprint. |
| **Testable (Kiểm thử được)** | ✅ ĐẠT | Các tiêu chí nghiệm thu bên dưới rõ ràng, có thể kiểm thử đạt/không đạt. |

---

### Tiêu Chí Nghiệm Thu (Acceptance Criteria - Gherkin)

#### AC1: Thực hiện thành công (Happy Path)
- **Cho biết (Given)** [tiền điều kiện ban đầu / trạng thái hệ thống xác thực]
- **Khi (When)** [người dùng thực hiện hành động chính xác]
- **Thì (Then)** [hệ thống xử lý thành công và hiển thị kết quả mong đợi]
- **Và (And)** [cập nhật trạng thái hệ thống hoặc gửi thông báo tương ứng]

#### AC2: Kiểm tra biên và xác thực dữ liệu (Edge Case)
- **Cho biết (Given)** [điều kiện biên về số lượng, độ dài chuỗi hoặc giới hạn định dạng]
- **Khi (When)** [người dùng nhập dữ liệu sát ngưỡng tối đa hoặc để trống trường tùy chọn]
- **Thì (Then)** [hệ thống áp dụng đúng quy tắc xác thực dữ liệu biên]

#### AC3: Xử lý lỗi và thông báo sự cố (Negative Path)
- **Cho biết (Given)** [điều kiện dẫn đến thất bại, ví dụ: dữ liệu không hợp lệ, tài khoản bị khóa]
- **Khi (When)** [người dùng nhấn nút xác nhận hoặc gửi yêu cầu]
- **Thì (Then)** [hệ thống dừng xử lý và hiển thị thông báo lỗi rõ ràng, dễ hiểu]
- **Và (And)** [trạng thái dữ liệu được bảo toàn an toàn, không lưu dữ liệu rác]

---

### Ghi Chú & Giả Định
- **Phụ thuộc**: [Các tính năng tiền đề hoặc API tích hợp bên ngoài]
- **Quy tắc nghiệp vụ**: [Công thức tính toán, quy định pháp lý hoặc hạn mức]
- **Câu hỏi mở**: [Vấn đề cần Product Owner làm rõ thêm]
```
