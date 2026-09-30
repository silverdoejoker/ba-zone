# NVG System Architecture & Dev Spine Conventions (Dành Cho IT BA)

Tài liệu quy định các nguyên tắc kiến trúc và kỹ thuật chuẩn hóa (dựa trên `ARCHITECTURE-SPINE.md` và `Architect-2026.png`) bắt buộc áp dụng khi IT BA viết tài liệu đặc tả (BRD, SRS, URD, Use Case, User Story, API Contract, Data Dictionary và Kịch bản UAT).

---

## 1. Ranh giới Xác thực & Nhận dạng (Authentication & Identity Boundary)
- **Zero Local Auth**: Tuyệt đối **không đưa vào scope** các chức năng tạo tài khoản cục bộ, đăng nhập form riêng, quên mật khẩu, kích hoạt OTP nội bộ cho nhân sự NVG.
- **SSO Gateway**: Toàn bộ xác thực tập trung tại tầng `application-gateway` (JWT Verification, Redis session cache) kết nối với **MS Entra (Azure AD)** và **SAP SuccessFactors** qua `user-service`.
- **Request Headers**: Các Upstream Backend Services chỉ nhận request và kiểm tra quyền thông qua các headers định danh do gateway chuyển tiếp: `x-user-id`, `x-user-email`, `x-request-id`.

---

## 2. Mô hình Ma trận AM & Phân tách 2 Tầng (Approval Matrix & Data Scope)
- **Thuật ngữ chuẩn**: Luôn sử dụng **"Ma trận Phê duyệt (Approval Matrix - AM)"** hoặc **"Ma trận Thẩm quyền Phê duyệt (AM)"** hoặc **"Ma trận AM"**. Tuyệt đối **KHÔNG dùng "Authority Matrix"** (NovaGroup không sử dụng thuật ngữ này).
- **Cấu trúc 4 cấp**:
  $$\text{User / JobCode (Chức danh)} \longrightarrow \text{Role} \longrightarrow \text{Permission} \longrightarrow \text{Action (API Endpoint)}$$
- **Phân tách 2 Tầng khi viết Đặc tả**:
  1. **Functional Permission (Quyền tính năng)**: Kiểm tra ở UI component và middleware API (Ví dụ: `gms_leasing.contract.create`, `gms_leasing.quote.approve`).
  2. **Data Scope (Phạm vi dữ liệu)**: Kiểm tra độc lập ở tầng Security L7 (`Authorization Data Scope`). Trong mọi Use Case/User Story, BA **bắt buộc làm rõ phạm vi dữ liệu**: User được xem/thao tác trên toàn bộ hệ thống hay chỉ trong các Dự án / Phân khu / Tòa nhà được phân công.

---

## 3. Quy chuẩn Cơ sở Dữ liệu & Data Dictionary (DB Schema & Entity Conventions)
- **Tiền tố bảng bắt buộc**: Toàn bộ bảng CSDL nghiệp vụ phải có tiền tố `{service-prefix}_`. Ví dụ phân hệ GMS: bắt buộc bắt đầu bằng `gms_` (`gms_project`, `gms_zone`, `gms_block`, `gms_floor`, `gms_product`, `gms_contract`, `gms_quote`, `gms_lease_term`...).
- **Cấu trúc phân cấp tài sản BĐS chuẩn**:
  $$\text{Project (Dự án)} \longrightarrow \text{Zone (Phân khu)} \longrightarrow \text{Block/Tower (Tháp/Khối)} \longrightarrow \text{Floor (Tầng)} \longrightarrow \text{Product (Sản phẩm/Mặt bằng)}$$
- **5 Cột Audit Bắt buộc**: Mọi bảng dữ liệu nghiệp vụ đều sở hữu 5 trường audit metadata:
  - `createdAt`, `updatedAt`, `deletedAt` (cho soft-delete), `createdBy`, `updatedBy`.

---

## 4. Nguyên tắc Xóa Mềm Tuyệt Đối (Strict Soft-Delete Invariant)
- **Zero Hard-Delete**: Trong các luồng nghiệp vụ "Xóa" (Mặt bằng, Khách thuê, Báo giá, Hợp đồng, Biểu phí), **tuyệt đối không cho phép xóa vật lý (Hard-delete) khỏi Database**.
- **Yêu cầu trong Spec**:
  - Ghi nhận thời điểm xóa vào `deletedAt` và người thực hiện vào `updatedBy`.
  - Ẩn khỏi các danh sách tra cứu thông thường của người dùng cuối.
  - Quy định rõ ràng điều kiện khôi phục (Restore) và lưu vết thanh tra (Audit Trail).

---

## 5. Tính Bất Biến Trạng Thái & Lịch Sử Biến Động (Immutability & State Mutation)
- Với các đối tượng giao dịch tài chính, pháp lý và tính tiền:
  - **Hợp đồng đã ký/duyệt, Phụ lục, Bảng chốt công nợ, Hóa đơn/Biểu phí**: Không cập nhật đè (No in-place overwrite).
  - Phải sử dụng cơ chế sinh phiên bản mới (Versioning), phụ lục điều chỉnh (Amendment), hoặc ghi log sự kiện (Audit Log / History Table).

---

## 6. Quy chuẩn Endpoint & API Response Envelope (Dành cho Spec Tích hợp)
- **Danh từ số ít**: Endpoint luôn dùng định dạng `/{service_prefix}/v1/internal/{resource}/{action}` (Ví dụ: `contract/create`, `contract/detail/:id`, `quote/approve`, `product/import-excel`). Tuyệt đối không dùng danh từ số nhiều (`contracts`, `products`).
- **Response Envelope Chuẩn**:
  - **Chi tiết / Đơn lẻ**:
    ```json
    { "ok": true, "statusCode": 200, "statusMessage": "SUCCESS", "data": { ... } }
    ```
  - **Danh sách / Phân trang**:
    ```json
    { "ok": true, "statusCode": 200, "statusMessage": "SUCCESS", "data": [ ... ], "total": 120 }
    ```
  - **Lỗi nghiệp vụ**:
    ```json
    { "ok": false, "statusCode": "ERR_VALIDATION", "statusMessage": "Thông tin mã căn không hợp lệ", "data": null }
    ```

---

## 7. Xử lý Bất đồng bộ (Async Background Processing)
- Với các tác vụ tốn thời gian xử lý:
  - Import Excel khối lượng lớn (> 100 dòng).
  - Kết xuất file báo cáo tổng hợp, xuất file PDF hợp đồng hàng loạt.
  - Chạy tính tiền thuê / tiền dịch vụ định kỳ hàng tháng.
- **Yêu cầu BA**: Đặc tả theo luồng xử lý bất đồng bộ sử dụng Queue (**RabbitMQ / NATS**):
  - Người dùng bấm nút ➔ Hệ thống trả về trạng thái Tiếp nhận (`PENDING` / `PROCESSING`) kèm mã tác vụ (`task_id`).
  - Worker chạy nền ➔ Cập nhật tiến độ ➔ Đẩy thông báo hoàn tất qua UI (WebSocket/Toast), Email hoặc Webhook **MS Teams**.
