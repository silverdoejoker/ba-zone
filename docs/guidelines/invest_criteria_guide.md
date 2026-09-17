# INVEST Criteria Guide — Hướng Dẫn Chi Tiết Tiêu Chuẩn User Story
> Tài liệu hướng dẫn chuyên sâu về tiêu chuẩn INVEST · **BA Zone** · Biên soạn bởi **Phúc NT** · Digital School

INVEST là bộ 6 tiêu chí do Bill Wake đề xuất năm 2003, dùng để đánh giá và đảm bảo chất lượng của Agile User Stories trước khi đưa vào Sprint Planning.

---

## I - Independent (Độc lập)

### Định nghĩa
Story phải có thể được phát triển, test và deploy độc lập với các story khác. Tránh phụ thuộc cứng (hard dependency) giữa các story trong cùng một sprint.

### Dấu hiệu vi phạm & Cách khắc phục
- ❌ **Vi phạm**: Story B bắt buộc phải đợi Story A deploy mới test được.
- ✅ **Khắc phục**: Dùng seed data / mock API để test độc lập; hoặc gộp thành 1 story vừa vặn nếu cả hai quá nhỏ.

---

## N - Negotiable (Có thể thương lượng)

### Định nghĩa
Story là "lời mời thảo luận", không phải hợp đồng kỹ thuật đóng băng. Chi tiết giải pháp kỹ thuật được làm rõ trong quá trình refinement và sprint execution.

### Dấu hiệu vi phạm & Cách khắc phục
- ❌ **Vi phạm**: Mô tả từng pixel UI hoặc áp đặt cấu trúc database, framework vào story.
- ✅ **Khắc phục**: Tập trung vào "What" (người dùng muốn gì) và "Why" (giá trị mang lại), dành "How" cho technical design.

---

## V - Valuable (Có giá trị)

### Định nghĩa
Mỗi story phải mang lại giá trị rõ ràng cho user, business, hoặc cả hai. Tránh viết story thuần kỹ thuật ("vì dev muốn refactor").

### Dấu hiệu vi phạm & Cách khắc phục
- ❌ **Vi phạm**: Phần "So that" rỗng hoặc lặp lại "I want".
- ✅ **Khắc phục**: Đo lường giá trị cụ thể (tiết kiệm thời gian, tăng doanh thu, giảm tỷ lệ rời bỏ).

---

## E - Estimable (Có thể ước lượng)

### Định nghĩa
Dev team phải có khả năng ước lượng effort để hoàn thành story.

### Dấu hiệu vi phạm & Cách khắc phục
- ❌ **Vi phạm**: Story quá mơ hồ, chứa nhiều rủi ro công nghệ chưa biết khiến dev không thể dự toán.
- ✅ **Khắc phục**: Tạo Spike Story (nghiên cứu trong khung thời gian cố định 1-2 ngày) trước khi viết story chính thức.

---

## S - Small (Vừa vặn)

### Định nghĩa
Story đủ nhỏ để hoàn thành trọn vẹn trong 1 sprint (thường 1-3 ngày làm việc của 1-2 devs).

### 6 Pattern chia nhỏ User Story (Splitting Patterns)
1. **Theo CRUD**: Tách Create / Read / Update / Delete riêng.
2. **Theo Persona**: Học viên / Mentor / Quản trị viên / Đối tác.
3. **Theo Data Type**: Text / Video / File đính kèm.
4. **Theo Business Rule**: Happy path / Validation nâng cao / Phân quyền.
5. **Theo Workflow Step**: Đăng ký -> Thanh toán -> Kích hoạt -> Sử dụng.
6. **Theo Nền tảng**: Web Portal / Mobile App.

---

## T - Testable (Có thể kiểm thử)

### Định nghĩa
Story phải có Acceptance Criteria rõ ràng, có thể kiểm thử đạt/không đạt (nhị phân), để QA viết test case và nghiệm thu release.

### Dấu hiệu vi phạm & Cách khắc phục
- ❌ **Vi phạm**: Dùng từ mơ hồ ("hệ thống phản hồi nhanh", "giao diện trực quan").
- ✅ **Khắc phục**: Cú pháp Gherkin Given-When-Then với số liệu và trạng thái đo lường được.

---

## Quick Reference Card

| Tiêu chí | Câu hỏi kiểm tra 1 dòng |
|---|---|
| **Independent** | Story này có thể dev và test độc lập được không? |
| **Negotiable** | Còn không gian thảo luận giải pháp hay đã quá cứng nhắc? |
| **Valuable** | Người dùng hoặc doanh nghiệp nhận được giá trị cụ thể gì? |
| **Estimable** | Đội ngũ kỹ thuật có đủ dữ liệu để ước lượng effort không? |
| **Small** | Story có hoàn thành gọn gàng trong 1 sprint không? |
| **Testable** | QA có thể viết test case nhị phân Pass/Fail từ AC không? |
