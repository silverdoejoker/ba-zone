---
inclusion: manual
---

# INVEST Criteria - Giải thích chi tiết

> INVEST là bộ 6 tiêu chí do Bill Wake đề xuất năm 2003, dùng để đánh giá 
> chất lượng User Story trong Agile/Scrum.
>
> Tài liệu này được biên soạn bởi **Phúc NT** cho chương trình **Digital School**
> của **BA Zone** — cộng đồng Business Analyst & Product Owner Việt Nam.

---

## I - Independent (Độc lập)

### Định nghĩa
Story phải có thể được phát triển, test, và deploy độc lập với các story khác. 
Tránh phụ thuộc cứng giữa các story.

### Dấu hiệu vi phạm
- Story B chỉ làm được sau khi story A xong
- Phải merge cùng lúc 2-3 story mới deploy được
- Test một story phải có data từ story khác

### Cách fix
- Gộp các story phụ thuộc thành 1 story lớn hơn (nếu nhỏ)
- Tách dependency ra thành story riêng + đặt ưu tiên trước
- Dùng mock data / stub để test độc lập

---

## N - Negotiable (Có thể thương lượng)

### Định nghĩa
Story là "lời mời thảo luận", không phải hợp đồng cứng. Chi tiết implementation 
được làm rõ trong quá trình refinement và development.

### Dấu hiệu vi phạm
- Story dài 3 trang mô tả từng pixel UI
- Chỉ định công nghệ cụ thể (phải dùng React, phải dùng Redis)
- Mô tả thuật toán chi tiết trong story

### Cách fix
- Giữ story ngắn gọn, focus vào "what" và "why"
- Đẩy chi tiết "how" sang AC hoặc tech design doc

---

## V - Valuable (Có giá trị)

### Định nghĩa
Mỗi story phải mang lại giá trị rõ ràng cho user, business, hoặc cả hai.

### Dấu hiệu vi phạm
- Phần "So that" rỗng hoặc lặp lại "I want"
- Không trả lời được câu "Nếu không làm thì sao?"

### Cách fix
- Viết phần "So that" theo công thức: business outcome + measurable
- Hỏi "Why?" 5 lần để tìm giá trị thật

---

## E - Estimable (Có thể ước lượng)

### Định nghĩa
Dev team phải có khả năng ước lượng effort để hoàn thành story.

### Dấu hiệu vi phạm
- Dev nói "không biết bao lâu, phải research thêm"
- Effort ước lượng chênh nhau quá lớn giữa các thành viên (>3 lần)

### Cách fix
- **Spike story**: tạo story riêng để research trước
- Bổ sung context, constraint, tham khảo

---

## S - Small (Nhỏ)

### Định nghĩa
Story đủ nhỏ để hoàn thành trong 1 sprint (thường 1-3 ngày làm việc của 1 dev).

### Dấu hiệu vi phạm
- Story ước lượng > 5 ngày work
- AC vượt quá 7-8 scenarios
- Tiêu đề có chữ "AND"

### Pattern split
1. **Theo CRUD**: tách Create / Read / Update / Delete riêng
2. **Theo persona**: Học viên / Mentor / Admin / HR Doanh nghiệp
3. **Theo data type**: Text / Video / File đính kèm
4. **Theo business rule**: Happy path / Validation / Permission
5. **Theo workflow step**: Đăng ký → Thanh toán → Enroll → Học
6. **Theo platform**: Web / Mobile App / API

---

## T - Testable (Có thể test)

### Định nghĩa
Story phải có AC rõ ràng, đo lường được, để QA viết test case và xác nhận "done".

### Dấu hiệu vi phạm
- AC dùng từ mơ hồ: "nhanh", "đẹp", "user-friendly", "intuitive"
- Không có AC, chỉ có description

### Cách fix
- Mỗi AC phải có Given/When/Then cụ thể
- Đo lường: số liệu, trạng thái, message text cụ thể

---

## Quick Reference Card

| Tiêu chí | Câu hỏi 1 dòng |
|----------|----------------|
| Independent | Story này có chạy độc lập được không? |
| Negotiable | Có chỗ cho thảo luận, hay đã quá chi tiết? |
| Valuable | Học viên/BA Zone được lợi gì cụ thể? |
| Estimable | Dev ước lượng được effort không? |
| Small | Hoàn thành trong 1 sprint không? |
| Testable | QA viết được test case từ AC không? |

---
*Biên soạn bởi **Phúc NT** · BA Zone · Digital School*
