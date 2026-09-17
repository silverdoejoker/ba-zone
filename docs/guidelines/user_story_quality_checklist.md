# User Story & AC Quality Checklist — Self Review Guide
> Bảng tự kiểm tra chất lượng User Story và Acceptance Criteria trước khi bàn giao · **BA Zone**  
> Biên soạn bởi **Phúc NT** · Digital School · BA Zone

Tài liệu này cung cấp checklist 5 phần để BA / PO tự rà soát hoặc dùng trong quy trình CI/CD audit trước khi đưa story vào backlog chính thức.

---

## 1. User Story Quality

### Persona (As a...)
- [ ] Persona cụ thể, không dùng "user" chung chung.
- [ ] Có mô tả trạng thái/điều kiện kèm theo (đã đăng ký, đã xác thực email, đang theo học...).
- [ ] Phân biệt rõ ràng với các vai trò khác trong sản phẩm.

### Goal (I want to...)
- [ ] Mô tả hành động cụ thể, dùng động từ rõ ràng.
- [ ] Có thể xác minh được thời điểm "đã làm xong".
- [ ] Tránh dùng các từ mơ hồ như "manage", "handle".

### Business Value (So that...)
- [ ] Khác biệt rõ với phần "I want to".
- [ ] Mô tả kết quả nghiệp vụ (outcome), không phải giải pháp kỹ thuật (feature).
- [ ] Trả lời được câu hỏi: *"Nếu không làm thì người dùng / doanh nghiệp mất gì?"*

---

## 2. INVEST Compliance

| Tiêu chí | Đã kiểm tra? | Ghi chú |
|---|---|---|
| **Independent** | [ ] | Story có thể phát triển và triển khai độc lập |
| **Negotiable** | [ ] | Có không gian thảo luận giải pháp kỹ thuật |
| **Valuable** | [ ] | Mang lại giá trị nghiệp vụ rõ ràng |
| **Estimable** | [ ] | Dev có thể ước lượng effort (nếu không, tạo Spike trước) |
| **Small** | [ ] | Hoàn thành trong <= 5 ngày dev work |
| **Testable** | [ ] | QA có thể viết test case nhị phân Pass/Fail |

---

## 3. Acceptance Criteria Quality

### Số lượng & Cấu trúc
- [ ] Tối thiểu 3 AC: 1 Happy Path + 1 Edge Case + 1 Negative Path.
- [ ] Tối đa 7-8 AC (nếu nhiều hơn, xem xét chia nhỏ story).
- [ ] Định dạng Given-When-Then chuẩn mực cho từng kịch bản.

### Đo lường & Tránh Anti-patterns
- [ ] Có số liệu cụ thể (thời gian xử lý, dung lượng, số ký tự).
- [ ] Có thông báo lỗi cụ thể, không ghi "hiển thị thông báo lỗi" chung chung.
- [ ] Không chứa chi tiết cài đặt kỹ thuật (tên bảng DB, endpoint API, framework).
- [ ] Không chứa chi tiết UI vụn vặt (màu sắc, vị trí pixel, font chữ).

---

## 4. Red Flags — Cần Sửa Ngay Nếu Gặp

- 🚨 Story description dài hơn 200 từ -> Quá chi tiết, mất tính thương lượng.
- 🚨 AC dài hơn 10 dòng -> Quá phức tạp, cần tách nhỏ.
- 🚨 Không có AC nào -> Vi phạm tính Testable.
- 🚨 "So that" rỗng hoặc lặp lại "I want to" -> Vi phạm tính Valuable.
- 🚨 Persona là "user" hoặc "everyone" -> Quá chung chung.
- 🚨 Có chữ "AND" trong tiêu đề -> Đang gộp 2 story độc lập.
- 🚨 AC dùng các từ mơ hồ ("nhanh", "đẹp", "dễ dùng", "v.v.").
