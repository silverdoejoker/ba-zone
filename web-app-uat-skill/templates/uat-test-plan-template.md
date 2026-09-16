# [Mã Kế Hoạch] Kế Hoạch Kiểm Thử Chấp Nhận Người Dùng (UAT Test Plan)

## 1. Thông Tin Chung (Document Information)
- **Tên Dự Án (Project Name)**: [Tên Hệ Thống / Ứng Dụng]
- **Mã Tài Liệu (Document ID)**: PLAN-UAT-[MODULE]-[YYYYMMDD]
- **Phiên Bản (Version)**: [e.g. 1.0.0-rc1]
- **Tác Giả / Lead QA (Author)**: [Họ Tên / Role]
- **Ngày Lập Kế Hoạch (Date)**: [YYYY-MM-DD]
- **Mục Tiêu (Objective)**: Xác nhận sự sẵn sàng của hệ thống cho môi trường thực tế (Production Readiness) và nghiệm thu chức năng với Stakeholders / PO.

---

## 2. Môi Trường & Thông Tin Truy Cập (Environment & Access)
- **URL Mục Tiêu (Target URL)**: `https://uat.example.com` (hoặc `http://localhost:8080`)
- **Bộ Tài Khoản Kiểm Thử (Credential Matrix)**:
  | Nhóm Vai Trò (Role) | Tài Khoản (Username/Email) | Quyền Hạn (Permissions) | Ghi Chú Dữ Liệu Ban Đầu (Seed Data) |
  |---|---|---|---|
  | **Quản trị viên (Admin)** | `admin_uat@example.com` | Toàn quyền cấu hình, quản lý người dùng, kế toán | Dữ liệu đầy đủ 12 tháng lịch sử |
  | **Chủ cơ sở (Manager/Owner)** | `owner01@example.com` | Quản lý danh mục phòng, khách thuê, hóa đơn | 10 phòng đang cho thuê |
  | **Khách hàng (User/Tenant)** | `tenant01@example.com` | Xem hóa đơn cá nhân, thanh toán VietQR | 1 hợp đồng thuê đang active |
  | **Khách vãng lai (Guest)** | *(Không cần login)* | Xem Landing Page, biểu phí, đăng ký dùng thử | Chưa có tài khoản |

> [!NOTE]
> Mật khẩu kiểm thử thực tế được lưu tại file an toàn nội bộ (ví dụ: `credentials.local.json` hoặc Vault), tuyệt đối không commit lên public repository.

---

## 3. Phạm Vi Kiểm Thử (Scope Boundaries)

### 3.1. Tính Năng Trong Phạm Vi (In-Scope)
- [x] Xác thực người dùng (Đăng nhập, đăng xuất, duy trì phiên, quên mật khẩu).
- [x] Các luồng nghiệp vụ chính (Happy Path) theo Use Case: [UC-AUTH-01, UC-BILL-01, ...].
- [x] Kiểm tra kịch bản biên (Edge cases) và kịch bản lỗi (Negative paths).
- [x] Hiển thị đa thiết bị (Desktop 1920x1080, Tablet 768x1024, Mobile 375x667).
- [x] Kiểm tra sức khỏe Javascript Console & Network API.

### 3.2. Tính Năng Ngoài Phạm Vi / Kiểm Thử Thủ Công (Out-of-Scope / Manual Only)
- [ ] Camera OCR trực tiếp (Yêu cầu thiết bị vật lý có camera).
- [ ] Giao dịch thật với cổng thanh toán Sandbox / Ngân hàng thực.
- [ ] Kiểm thử tải trọng cao (Performance Stress Test > 10.000 users).

---

## 4. Ma Trận Kịch Bản Kiểm Thử (Test Scenario Matrix)

| Test Case ID | Use Case / Story Ref | Module | Loại Kịch Bản (Type) | Mô Tả Tóm Tắt (Summary) | Tiêu Chí Đạt (Expected Outcome) |
|---|---|---|---|---|---|
| `TC-AUTH-01` | `UC-AUTH-01` / `AC1` | Authentication | **Happy Path** | Đăng nhập với tài khoản hợp lệ | Đăng nhập thành công, chuyển hướng về Dashboard |
| `TC-AUTH-02` | `UC-AUTH-01` / `AC2` | Authentication | **Negative** | Đăng nhập với sai mật khẩu | Báo lỗi thân thiện, không tiết lộ cấu trúc DB |
| `TC-AUTH-03` | `UC-AUTH-01` / `AC3` | Authentication | **Edge Case** | Nhập email cực dài (>100 ký tự) | Form tự động validate biên, không tràn layout |
| `TC-CORE-01` | `UC-BILL-01` / `AC1` | Core Business | **Happy Path** | Chốt chỉ số điện nước & tính tổng | Số tiền khớp 100% công thức định sẵn |
| `TC-CORE-02` | `UC-BILL-01` / `AC2` | Core Business | **Edge Case** | Chỉ số điện tháng mới < tháng cũ | Hiển thị cảnh báo đỏ và yêu cầu xác nhận |
| `TC-RESP-01` | N/A | UI/UX | **Responsive** | Mở trên màn hình Mobile 375x667 | Không có scrollbar ngang, menu chuyển bottom bar |

---

## 5. Tiêu Chuẩn Nghiệm Thu & Đánh Giá (Acceptance Criteria & Exit Thresholds)
- **Tỷ lệ Pass**: Tối thiểu `95%` tổng số Test Cases.
- **Lỗi mức độ Critical (Chặn luồng, sai tiền, mất dữ liệu)**: `0` lỗi.
- **Lỗi mức độ Major (Tính năng chính lỗi nhưng có workaround)**: `0` lỗi.
- **Lỗi mức độ Minor / Trivial (Thẩm mỹ, chính tả, khoảng cách)**: Tối đa `<= 3` lỗi và phải có kế hoạch khắc phục trong sprint tiếp theo.
- **Console Errors**: `0` lỗi runtime không được xử lý (`Uncaught Error`).
