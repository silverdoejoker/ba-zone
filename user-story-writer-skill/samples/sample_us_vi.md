# Câu Chuyện Người Dùng: US-COURSE-01 - Lọc Danh Sách Khóa Học

**US-COURSE-01**: Lọc Danh Sách Khóa Học Theo Danh Mục

**Là một** học viên đã đăng nhập đang xem danh mục đào tạo  
**Tôi muốn** lọc danh sách các khóa học theo chủ đề và mức học phí  
**Để** nhanh chóng tìm thấy chương trình học phù hợp với nhu cầu phát triển kỹ năng của bản thân  

---

### Bảng Đánh Giá Tiêu Chuẩn INVEST

| Tiêu chí | Trạng thái | Đánh giá & Ghi chú |
|---|---|---|
| **Independent (Độc lập)** | ✅ ĐẠT | Có thể phát triển và bàn giao độc lập với tính năng thanh toán. |
| **Negotiable (Thương lượng được)** | ✅ ĐẠT | Tập trung vào hành vi tìm kiếm của học viên thay vì trói buộc giao diện cứng. |
| **Valuable (Có giá trị)** | ✅ ĐẠT | Giúp học viên tiết kiệm thời gian tìm kiếm khóa học đáng kể. |
| **Estimable (Ước lượng được)** | ✅ ĐẠT | Tiêu chí lọc rõ ràng, dev dễ dàng ước lượng effort truy vấn cơ sở dữ liệu. |
| **Small (Vừa vặn)** | ✅ ĐẠT | Phạm vi gọn gàng, hoàn thành trọn vẹn trong 1 sprint. |
| **Testable (Kiểm thử được)** | ✅ ĐẠT | Các tiêu chí nghiệm thu bên dưới có thể kiểm thử đạt/không đạt rõ ràng. |

---

### Tiêu Chí Nghiệm Thu (Acceptance Criteria - Gherkin)

#### AC1: Lọc dữ liệu có kết quả phù hợp (Happy Path)
- **Cho biết (Given)** học viên đang ở trang danh mục khóa học với nhiều khóa học đang mở
- **Khi (When)** học viên chọn chủ đề "Phân Tích Dữ Liệu" và áp dụng bộ lọc
- **Thì (Then)** hệ thống hiển thị danh sách các khóa học thuộc chủ đề "Phân Tích Dữ Liệu"
- **Và (And)** số lượng khóa học tìm thấy được cập nhật chính xác

#### AC2: Lọc dữ liệu không có kết quả phù hợp (Edge Case)
- **Cho biết (Given)** học viên kết hợp các điều kiện lọc mà không có khóa học nào thỏa mãn
- **Khi (When)** áp dụng bộ lọc
- **Thì (Then)** hệ thống hiển thị thông báo "Không tìm thấy khóa học phù hợp với tiêu chí đã chọn"
- **Và (And)** hiển thị nút bấm "Xóa bộ lọc" để người dùng thao tác lại nhanh chóng

#### AC3: Mất kết nối mạng trong quá trình tải dữ liệu (Negative Path)
- **Cho biết (Given)** kết nối mạng chập chờn khi hệ thống đang truy vấn danh sách lọc
- **Khi (When)** học viên nhấn nút áp dụng lọc
- **Thì (Then)** hệ thống hiển thị thông báo nhẹ: "Không thể tải danh sách khóa học. Vui lòng thử lại sau."
- **Và (And)** giữ nguyên trạng thái các ô checkbox đã chọn trước đó, không gây crash trang

---

### Ghi Chú & Phụ Thuộc
- **Phụ thuộc**: API truy vấn danh mục khóa học phải sẵn sàng hoạt động.
