# Đặc Tả Use Case: UC-AUTH-01 - Đăng Ký Tài Khoản Học Viên
> Tài Liệu Mẫu Thực Chiến · **BA Zone** (Karl Wiegers / IIBA BABOK Standard)

| Trường thông tin | Chi tiết |
|---|---|
| **Mã Use Case** | `UC-AUTH-01` |
| **Tên Use Case** | Đăng ký tài khoản học viên |
| **Người tạo & Ngày tạo** | Phúc NT · 2026-09-16 |
| **Người cập nhật & Ngày cập nhật** | Phúc NT · 2026-09-16 |
| **Tác nhân chính** | Học viên tiềm năng |
| **Mô tả** | Học viên tiềm năng đăng ký tài khoản mới trên hệ thống để có thể đăng ký các khóa học và truy cập tài nguyên học tập. |
| **Tiền điều kiện** | 1. Người dùng có kết nối Internet và địa chỉ email hợp lệ.<br>2. Email chưa từng đăng ký tài khoản nào trước đó trên hệ thống. |
| **Hậu điều kiện** | 1. Bản ghi học viên mới được lưu vào cơ sở dữ liệu.<br>2. Mã xác thực kích hoạt được gửi đến hòm thư người dùng. |
| **Độ ưu tiên** | Cao (Luồng tiếp nhận người dùng trọng yếu) |
| **Tần suất sử dụng** | ~300 lượt đăng ký mỗi ngày |

### Luồng sự kiện chính (Happy Path)

| Bước | Hành động của Tác nhân | Phản hồi của Hệ thống |
|---|---|---|
| 1 | Học viên tiềm năng truy cập vào trang đăng ký tài khoản. | Hệ thống hiển thị biểu mẫu đăng ký với các trường bắt buộc. |
| 2 | Học viên nhập đầy đủ thông tin cá nhân và nhấn nút Xác nhận. | Hệ thống kiểm tra tính hợp lệ của toàn bộ dữ liệu nhập. |
| 3 | | Hệ thống khởi tạo hồ sơ học viên trạng thái chờ và gửi mã OTP qua email. |
| 4 | Học viên nhập mã xác thực OTP nhận được từ email. | Hệ thống xác thực mã OTP và kích hoạt trạng thái tài khoản. |
| 5 | | Hệ thống chuyển hướng Học viên đến trang tổng quan chào mừng. |

### Luồng sự kiện thay thế

#### UC-AUTH-01.LTT.1: Đăng ký nhanh qua tài khoản Google
- **Điểm rẽ nhánh**: Tại bước 1 của Luồng sự kiện chính.
- **Điều kiện kích hoạt**: Học viên chọn "Đăng ký với Google".
- **Các bước thực hiện**:
  1. Hệ thống chuyển hướng Học viên đến trang đăng nhập Google OAuth.
  2. Học viên cấp quyền chia sẻ thông tin cơ bản.
  3. Hệ thống tiếp nhận email đã xác thực và tự động kích hoạt tài khoản.
- **Điểm quay lại / Kết thúc**: Quay lại Luồng chính tại bước 5.

### Luồng ngoại lệ

#### UC-AUTH-01.NL.1: Email đã tồn tại trong hệ thống
- **Điều kiện phát sinh**: Tại bước 2, Hệ thống phát hiện email đã được sử dụng.
- **Phản hồi hệ thống**: Hệ thống hiển thị thông báo lỗi: "Email này đã được đăng ký. Vui lòng đăng nhập hoặc khôi phục mật khẩu."
- **Trạng thái cuối cùng**: Giao dịch bị hủy bỏ, không tạo thêm bản ghi. Học viên ở lại biểu mẫu đăng ký.

### Yêu cầu bổ sung

| Trường thông tin | Chi tiết |
|---|---|
| **Use Case liên kết** | UC-AUTH-02: Xác thực mã OTP |
| **Yêu cầu đặc biệt** | - **Hiệu năng**: Thời gian phản hồi xử lý biểu mẫu < 1.5 giây.<br>- **Bảo mật**: Mật khẩu mã hóa bằng bcrypt, toàn bộ đường truyền mã hóa TLS 1.3. |
| **Giả định & Ghi chú** | Cổng gửi email bên thứ ba cam kết thời gian hoạt động SLA 99.9%. |
