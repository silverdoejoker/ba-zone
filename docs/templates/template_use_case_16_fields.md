# Use Case Standard 16-Field Template (Song Ngữ EN / VI)
> Template chuẩn của **BA Zone** · Karl Wiegers / IIBA BABOK & Alistair Cockburn standards

Tài liệu này chứa mẫu đặc tả Use Case chuẩn 16 trường áp dụng cho toàn bộ dự án của BA Zone, hỗ trợ xuất bản song ngữ Anh - Việt.

---

## 1. English Template (`output_language=en`)

```markdown
# Use Case Specification: UC-[MODULE]-[NN] - [Use Case Name]

| Field | Details |
|---|---|
| **Use Case ID** | `UC-[MODULE]-[NN]` |
| **Use Case Name** | [Active Verb + Specific Noun Phrase, e.g., Register Student Account] |
| **Created By & Date** | [Author Name] · [YYYY-MM-DD] |
| **Last Updated By & Date** | [Editor Name] · [YYYY-MM-DD] |
| **Primary Actor** | [Specific Persona / Role, e.g., Prospective Student] |
| **Description** | [2-3 sentences explaining Why this is needed, What the actor achieves, and the Outcome] |
| **Preconditions** | 1. [Precondition 1 - verifiable state before execution]<br>2. [Precondition 2] |
| **Postconditions** | 1. [Postcondition 1 - verifiable state after successful completion]<br>2. [Postcondition 2] |
| **Priority** | [High / Medium / Low] ([Business rationale]) |
| **Frequency of Use** | [Estimated count, e.g., ~200 times/day] |

### Normal Course of Events (Happy Path)

| Step | Actor Action | System Response |
|---|---|---|
| 1 | Actor accesses the registration page. | System displays registration form with required fields. |
| 2 | Actor enters required personal information and submits. | System validates submitted fields against validation rules. |
| 3 | | System creates pending account record and issues OTP code. |
| 4 | Actor enters OTP verification code. | System verifies OTP and activates student account. |
| 5 | | System redirects Actor to dashboard and sends welcome email. |

### Alternative Courses

#### UC-[MODULE]-[NN].AC.1: [Alternative Course Name]
- **Branch Point**: At step [N] of Normal Course.
- **Condition**: [Condition triggering the alternative path].
- **Flow**:
  1. [Action 1]
  2. [Action 2]
- **Rejoin / Exit**: Rejoin Normal Course at step [M] / Terminates with [Outcome].

### Exceptions

#### UC-[MODULE]-[NN].EX.1: [Exception Name]
- **Trigger**: At step [N], [Failure condition occurs].
- **System Response**: System logs error code [ERR-XXX], displays error message "[Message text]".
- **Final State**: Transaction rolled back. No data committed. Actor remains at step [N].

### Supplemental Specifications

| Field | Details |
|---|---|
| **Includes** | [UC-[MODULE]-[NN]: Sub-use case name if applicable, or None] |
| **Special Requirements** | - **Performance**: [e.g., Response time < 2s for 95% of requests]<br>- **Security**: [e.g., Passwords encrypted using bcrypt, 2FA required] |
| **Assumptions** | 1. [Operational / external assumption]<br>2. [Assumption 2] |
| **Notes & Issues** | - [Open question or pending decision] |
```

---

## 2. Vietnamese Template (`output_language=vi`)

```markdown
# Đặc Tả Use Case: UC-[MODULE]-[NN] - [Tên Use Case]

| Trường thông tin | Chi tiết |
|---|---|
| **Mã Use Case** | `UC-[MODULE]-[NN]` |
| **Tên Use Case** | [Động từ hành động + Cụm danh từ cụ thể, ví dụ: Đăng ký tài khoản học viên] |
| **Người tạo & Ngày tạo** | [Tên tác giả] · [YYYY-MM-DD] |
| **Người cập nhật & Ngày cập nhật** | [Tên người sửa] · [YYYY-MM-DD] |
| **Tác nhân chính** | [Vai trò cụ thể, ví dụ: Học viên tiềm năng] |
| **Mô tả** | [2-3 câu nêu rõ Lý do tại sao cần, Tác nhân đạt được gì và Kết quả đầu ra] |
| **Tiền điều kiện** | 1. [Tiền điều kiện 1 - trạng thái hệ thống bắt buộc phải có trước khi thực hiện]<br>2. [Tiền điều kiện 2] |
| **Hậu điều kiện** | 1. [Hậu điều kiện 1 - trạng thái hệ thống được bảo đảm sau khi hoàn thành thành công]<br>2. [Hậu điều kiện 2] |
| **Độ ưu tiên** | [Cao / Trung bình / Thấp] ([Lý do nghiệp vụ]) |
| **Tần suất sử dụng** | [Ước lượng định lượng, ví dụ: ~200 lần/ngày] |

### Luồng sự kiện chính (Normal Course)

| Bước | Hành động của Tác nhân | Phản hồi của Hệ thống |
|---|---|---|
| 1 | Tác nhân truy cập vào trang đăng ký. | Hệ thống hiển thị biểu mẫu đăng ký với các trường bắt buộc. |
| 2 | Tác nhân điền thông tin cá nhân và nhấn gửi. | Hệ thống kiểm tra tính hợp lệ của các trường dữ liệu theo quy tắc. |
| 3 | | Hệ thống khởi tạo bản ghi tài khoản chờ kích hoạt và gửi mã OTP. |
| 4 | Tác nhân nhập mã OTP xác thực. | Hệ thống xác thực mã OTP và kích hoạt tài khoản học viên. |
| 5 | | Hệ thống chuyển hướng Tác nhân đến trang tổng quan và gửi email chào mừng. |

### Luồng sự kiện thay thế (Alternative Courses)

#### UC-[MODULE]-[NN].AC.1: [Tên luồng thay thế]
- **Điểm rẽ nhánh**: Tại bước [N] của Luồng sự kiện chính.
- **Điều kiện kích hoạt**: [Điều kiện dẫn đến luồng rẽ nhánh].
- **Các bước thực hiện**:
  1. [Bước 1]
  2. [Bước 2]
- **Điểm quay lại / Kết thúc**: Quay lại Luồng chính tại bước [M] / Kết thúc với [Kết quả].

### Luồng ngoại lệ (Exceptions)

#### UC-[MODULE]-[NN].EX.1: [Tên ngoại lệ / Lỗi]
- **Điều kiện phát sinh**: Tại bước [N], [Sự cố / Lỗi xảy ra].
- **Phản hồi hệ thống**: Hệ thống ghi log mã lỗi [ERR-XXX], hiển thị thông báo lỗi "[Nội dung thông báo]".
- **Trạng thái cuối cùng**: Giao dịch bị hủy bỏ (Rollback). Dữ liệu không bị lưu sai lệch. Tác nhân ở lại bước [N].

### Yêu cầu bổ sung

| Trường thông tin | Chi tiết |
|---|---|
| **Use Case liên kết (Includes)** | [UC-[MODULE]-[NN]: Tên Use Case con nếu có, hoặc Không có] |
| **Yêu cầu đặc biệt** | - **Hiệu năng**: [ví dụ: Thời gian phản hồi < 2s cho 95% yêu cầu]<br>- **Bảo mật**: [ví dụ: Mật khẩu mã hóa bằng bcrypt, áp dụng 2FA] |
| **Giả định** | 1. [Giả định về môi trường hoặc hệ thống bên ngoài]<br>2. [Giả định 2] |
| **Ghi chú & Vấn đề mở** | - [Câu hỏi cần làm rõ thêm với Product Owner / Stakeholder] |
```
