# Biên Bản Nghiệm Thu & Báo Cáo Kiểm Thử Chấp Nhận Người Dùng (UAT Acceptance Report)
> Template chuẩn của **BA Zone** · TrọBill UAT Methodology

## 1. Thông Tin Tổng Quan (Executive Summary)
- **Tên Hệ Thống / Ứng Dụng (Application Name)**: [Tên Hệ Thống]
- **Mã Báo Cáo (Report ID)**: UAT-REP-[MODULE]-[YYYYMMDD]
- **Môi Trường Kiểm Thử (Environment)**: [Staging / UAT Sandbox / Localhost]
- **URL Mục Tiêu (Target URL)**: `[URL của ứng dụng]`
- **Thời Gian Thực Hiện (Execution Date)**: [YYYY-MM-DD HH:mm]
- **Người Thực Hiện (Lead Tester / Evaluator)**: [Họ Tên / AI QA Agent]
- **Người Nghiệm Thu (Acceptance Sign-off Owner)**: [Product Owner / Lead BA]
- **Kết Quả Chung (Overall Status)**: **[PASS / FAIL / CONDITIONAL PASS]**
- **Tỷ Lệ Đạt (Pass Rate)**: `[XX%]` ([M]/[N] Test Cases)

---

## 2. Ma Trận Tài Khoản & Vai Trò Kiểm Thử (Credential & Role Matrix)

| Nhóm Vai Trò (Role) | Tài Khoản Kiểm Thử (Identifier) | Trạng Thái Đăng Nhập (Login State) | Ghi Chú Phiên (Session Notes) |
|---|---|---|---|
| **Quản trị viên (Admin)** | `admin_uat@example.com` | **SUCCESS** | Cookie HttpOnly lưu 24h, token JWT hợp lệ |
| **Chủ cơ sở (Manager)** | `manager01@example.com` | **SUCCESS** | Quyền hạn chuẩn xác, phân lập tenant thành công |
| **Khách hàng (User/Tenant)**| `tenant01@example.com` | **SUCCESS** | Route Guard chặn đúng khi truy cập `/admin` |
| **Khách vãng lai (Guest)** | *(Unauthenticated)* | **SUCCESS** | Hiển thị landing page, không rò rỉ dữ liệu nội bộ |

---

## 3. Bảng Chi Tiết Kết Quả Thực Thi Kịch Bản (Test Execution Matrix)

| Mã Ca Kiểm Thử (TC ID) | Module / Chức Năng | Loại Kịch Bản (Type) | Mô Tả Tóm Tắt (Summary) | Trạng Thái (Status) | Ghi Chú & Bằng Chứng (Notes & Evidence) |
|---|---|---|---|---|---|
| `TC-AUTH-01` | Authentication | **Happy Path** | Đăng nhập tài khoản hợp lệ | **PASS** | Chuyển hướng Dashboard trong 450ms |
| `TC-AUTH-02` | Authentication | **Negative Path** | Đăng nhập sai mật khẩu | **PASS** | Hiển thị thông báo đỏ thân thiện |
| `TC-AUTH-03` | Authentication | **Edge Case** | Nhập email > 120 ký tự | **PASS** | Cắt chuỗi an toàn, không vỡ layout |
| `TC-CORE-01` | Billing Calculation | **Happy Path** | Tính tổng hóa đơn điện nước | **PASS** | Kết quả khớp 100% công thức nghiệp vụ |
| `TC-CORE-02` | Billing Calculation | **Edge Case** | Chỉ số điện mới nhỏ hơn cũ | **PASS** | Xuất hiện cảnh báo đỏ xác thực |
| `TC-CORE-03` | VietQR Payment | **Happy Path** | Sinh mã VietQR động | **PASS** | Quét thử trên App ngân hàng nhận đúng số tiền |
| `TC-DATA-01` | Data Export | **Happy Path** | Xuất file sao lưu JSON/Excel | **PASS** | File tải về nguyên vẹn, chuẩn font UTF-8 |
| `TC-NET-01` | Network Fault | **Negative Path** | Ngắt kết nối mạng khi lưu dữ liệu | **PASS** | Báo lỗi mất mạng, không mất dữ liệu trên form |

---

## 4. Nhật Ký Lỗi & Vấn Đề Phát Hiện (Defect & Issue Log)

| Mã Lỗi (Defect ID) | Test Case Liên Quan | Mức Độ Nghiêm Trọng (Severity) | Mô Tả Lỗi (Description) | Các Bước Tái Hiện (Steps to Reproduce) | Trạng Thái Xử Lý (Resolution Status) |
|---|---|---|---|---|---|
| `BUG-01` | `TC-CORE-02` | **Minor** | Màu nút "Xác nhận nhập lùi số" hơi tối trên Dark Theme | 1. Đổi Dark Mode 2. Nhập số lùi 3. Xem modal | Đã log Jira #142 (Hotfix Sprint sau) |
| `BUG-02` | `TC-AUTH-03` | **Trivial** | Thiếu tooltip giải thích mật khẩu yêu cầu ký tự hoa | 1. Mở màn hình đổi pass 2. Rê chuột vào ô pass | Đã cập nhật văn bản hướng dẫn |

*(Nếu không có lỗi nào phát hiện, ghi rõ: "Không phát hiện lỗi nghiêm trọng nào. Hệ thống hoạt động ổn định 100% theo tiêu chuẩn yêu cầu.")*

---

## 5. Kiểm Thử Giao Diện Đa Màn Hình & Trải Nghiệm (Responsive & Viewport Verification)

| Môi Trường / Thiết Bị (Device & Viewport) | Độ Phân Giải (Resolution) | Trạng Thái Bố Cục (Layout Health) | Hiện Tượng Cuộn Ngang (Horizontal Scroll) | Trạng Thái (Status) |
|---|---|---|---|---|
| **Màn hình Máy tính (Desktop)** | `1920 x 1080` | Hoàn hảo, Sidebar mở rộng đầy đủ | **KHÔNG** | **PASS** |
| **Máy tính bảng (Tablet)** | `768 x 1024` (iPad) | Tự động co gọn Sidebar thành Icon | **KHÔNG** | **PASS** |
| **Điện thoại Di động (Mobile)** | `375 x 667` (iPhone) | Chuyển đổi sang Bottom Navigation Bar | **KHÔNG** | **PASS** |
| **Giao diện Tối (Dark Theme)** | `Adaptive HSL` | Tương phản tốt, nhãn chữ rõ ràng | **KHÔNG** | **PASS** |

---

## 6. Sức Khỏe Bảng Điều Khiển & Mạng (Console & Network Health)
- **Javascript Console Exceptions**: `0` lỗi unhandled (`Uncaught Error: 0`, `TypeError: 0`).
- **Network HTTP Failures**: Không có mã lỗi `500 Internal Server Error` hoặc tài nguyên ảnh/font bị `404 Not Found`.
- **Bộ nhớ & Rò rỉ DOM (Memory & DOM Leaks)**: Số lượng DOM nodes ổn định sau 10 lần chuyển tab liên tục.

---

## 7. Danh Mục Phân Lập Phần Cứng / Kiểm Thử Thủ Công (Hardware Isolation Registry)

| Tính Năng (Feature) | Lý Do Phân Lập (Isolation Reason) | Quy Trình Kiểm Thử Bằng Tay (Manual Verification Steps) | Kết Quả Thủ Công (Manual Result) |
|---|---|---|---|
| **Camera OCR Scanner** | Cần luồng video camera vật lý và điều chỉnh khoảng cách thực | 1. Mở app trên điện thoại thật.<br>2. Chọn biểu tượng Máy ảnh.<br>3. Rọi đồng hồ điện thật.<br>4. Kiểm tra số nhận diện được. | **PASS** (Nhận diện chính xác 5/5 lần thử) |
| **Google Play IAP Billing** | Cần tài khoản Sandbox Play Store và kết nối native bridge | 1. Mở Cài đặt -> Mua bản Pro.<br>2. Xác nhận hiển thị bottom sheet Google Play.<br>3. Không thanh toán tiền thật. | **PASS** (Sheet hiển thị đúng giá tiền) |

---

## 8. Kết Luận & Quyết Định Nghiệm Thu (Acceptance Sign-off & Recommendation)

### 8.1. Đánh Giá Tiêu Chuẩn Xuất Xưởng (Exit Criteria Checklist)
- [x] 100% Test Case thuộc nhóm Happy Path và Critical đạt yêu cầu.
- [x] Tỷ lệ đạt tổng thể: `100%` (vượt ngưỡng yêu cầu 95%).
- [x] `0` lỗi mức độ Critical và `0` lỗi mức độ Major.
- [x] Đã kiểm tra tính toàn vẹn trên cả 3 breakpoint màn hình.
- [x] Console log hoàn toàn sạch sẽ, không có runtime crash.

### 8.2. Quyết Định Nghiệm Thu Chính Thức (Final Decision)

> ### 🟢 QUYẾT ĐỊNH: **GO (CHẤP THUẬN PHÁT HÀNH / ACCEPTED FOR PRODUCTION)**  
> Hệ thống đáp ứng đầy đủ và toàn diện các tiêu chí nghiệm thu UAT, đảm bảo chất lượng nghiệp vụ và trải nghiệm người dùng theo cam kết đặc tả.

### 8.3. Đại Diện Các Bên Ký Duyệt (Signatures)

| Đại Diện Bên Phát Triển (Dev/QA Lead) | Đại Diện Quản Lý Sản Phẩm (PO / BA Lead) | Đại Diện Khách Hàng / Vận Hành (Stakeholder) |
|---|---|---|
| *(Đã ký & xác nhận)* | *(Đã duyệt nghiệm thu)* | *(Đã đồng ý nhận bàn giao)* |
| **Ngày**: [YYYY-MM-DD] | **Ngày**: [YYYY-MM-DD] | **Ngày**: [YYYY-MM-DD] |
