# MẪU ĐẶC TẢ YÊU CẦU NGHIỆP VỤ TIÊU CHUẨN (NVG STANDARD BRD TEMPLATE)
> **Mã số mẫu:** `TEMPLATE-BRD-NVG-STD-2026`  
> **Nguồn gốc chuẩn hóa:** Reverse-engineered từ tài liệu yêu cầu thực tế của Trung tâm Đào tạo NVG (`BRD_UngDungDiemDanh_NFC_v1.pdf`)  
> **Áp dụng cho:** IT Business Analysts, Product Owners, Technical Writers soạn thảo BRD, URD, FSD trong toàn bộ dự án.  
> **Quy chuẩn kiểm soát:** Tuân thủ `enterprise-nda-sanitizer` và Quy chuẩn Ma trận Thẩm quyền (`AM - Authority Matrix`).  

---

## [TÊN ĐƠN VỊ YÊU CẦU] → [TÊN ĐƠN VỊ THỰC HIỆN / IT-PMO]
# [TÊN ỨNG DỤNG / TÊN HỆ THỐNG]
### Yêu cầu · Tính năng · Use case

| Hạng mục | Thông tin |
|---|---|
| **Gửi** | [Họ tên & Chức danh Người nhận, vd: Ms. Thái Ngọc Anh Tú - ITC-PMO] |
| **Từ** | [Họ tên & Chức danh Người đặt yêu cầu, vd: Trợ lý CĐS Đào tạo / Product Owner] |
| **Mã yêu cầu** | [Mã tiền tố yêu cầu, vd: REQ-01 đến REQ-05 hoặc NFC-01 đến NFC-05] |
| **Phiên bản** | [Mã phiên bản, vd: V1.0 · DD/MM/YYYY] |

---

## 1. Yêu cầu (Request Overview & Problem Statement)

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **Mã yêu cầu** | [Mã định danh nhóm yêu cầu, vd: REQ-01 đến REQ-05] |
| **Tên yêu cầu** | [Tên tóm tắt một câu về giải pháp mong muốn] |
| **Hạng mục gốc** | [Mục tiêu nghiệp vụ cốt lõi, phạm vi bài toán quản trị] |
| **Người đặt yêu cầu** | [Họ tên và chức danh người đại diện nghiệp vụ] |
| **Bên thực hiện** | [Đơn vị công nghệ / Đội ngũ IT phụ trách] |
| **Ngày gửi** | [DD/MM/YYYY] |
| **Mức ưu tiên** | `High` / `Medium` / `Low` |
| **Hiện đang làm thế nào (As-Is)** | [Mô tả quy trình thủ công hiện tại, công cụ đang dùng, vd: Excel, MS Form, Giấy tờ] |
| **Vấn đề (Pain Points)** | [Các nút thắt, rủi ro, sai sót, lãng phí thời gian của quy trình hiện tại] |
| **Người dùng (Target Personas)** | [Các đối tượng trực tiếp sử dụng hệ thống và đối tượng thụ hưởng báo cáo] |
| **Mong muốn (To-Be Goals)** | [Đầu ra cụ thể mong muốn sau khi ứng dụng phần mềm] |
| **Ràng buộc (Constraints)** | [Các ràng buộc về hệ thống nguồn (SuccessFactors, SAP, HRM), thiết bị phần cứng, nền tảng] |

---

## 2. Tính năng và thứ tự ưu tiên (Feature Breakdown & Delivery Milestones)

| Ưu tiên | Mã Tính Năng | Yêu Cầu Nghiệp Vụ | Mô Tả Tính Năng / Giải Pháp Chi Tiết | Mốc Hoàn Thành (Deadline) |
|:---:|:---:|---|---|:---:|
| **Ưu tiên 1** | `REQ-01` | [Tên yêu cầu nghiệp vụ 1] | [Mô tả hành vi hệ thống và tính năng cần xây dựng] | [DD/MM/YYYY] |
| **Ưu tiên 1** | `REQ-02` | [Tên yêu cầu nghiệp vụ 2] | [Mô tả hành vi hệ thống và tính năng cần xây dựng] | [DD/MM/YYYY] |
| **Ưu tiên 1** | `REQ-03` | [Tên yêu cầu nghiệp vụ 3] | [Mô tả hành vi hệ thống và tính năng cần xây dựng] | [DD/MM/YYYY] |
| **Ưu tiên 2** | `REQ-04` | [Tên yêu cầu nghiệp vụ 4] | [Tính năng mở rộng, phân loại tự động] | [DD/MM/YYYY] |
| **Ưu tiên 2** | `REQ-05` | [Điều chỉnh dữ liệu / Audit] | [Tính năng sửa đổi dữ liệu có lưu vết Audit Trail] | [Sau DD/MM/YYYY] |
| **Ưu tiên 2** | `REQ-06` | [Cơ chế dự phòng / Fallback] | [Giải pháp dự phòng khi sự cố mạng hoặc quên thiết bị] | [DD/MM/YYYY] |

---

## 3. Cách tính toán & Ma trận Kịch bản (Calculation Engine & Test Scenarios)

### 3.1. Quy tắc tính toán (Business Rules)

| Bước | Quy tắc nghiệp vụ (Business Rule) |
|---|---|
| **1. Khử trùng lặp** | [Mô tả cách xử lý giao dịch gửi trùng trong khoảng thời gian ngắn (vd: cách nhau vài giây)] |
| **2. Ghép cặp / Phân loại** | [Mô tả cách ghép cặp giao dịch Đầu - Cuối (vd: Lượt lẻ = VÀO, Lượt chẵn = RA)] |
| **3. Cắt theo biên thời gian** | [Phần giao dịch nằm ngoài khung giờ kế hoạch quy định sẽ bị cắt bỏ / không tính] |
| **4. Công thức tính toán** | [Công thức cụ thể, vd: Tổng phút = $\sum(RA - VÀO)$ của tất cả các cặp hợp lệ] |
| **5. Xử lý trường hợp lẻ / lỗi** | [Quy tắc gắn cờ khi dữ liệu bị thiếu lượt chẵn/lẻ hoặc thiếu giao dịch đóng] |
| **6. Xác định mốc Đầu - Cuối** | [Mốc bắt đầu = Giao dịch hợp lệ đầu tiên · Mốc kết thúc = Giao dịch hợp lệ cuối cùng] |
| **7. Quy tắc thời điểm** | [Bắt buộc đồng bộ theo giờ chuẩn của Máy chủ (Server Clock, đến đơn vị giây)] |
| **8. Quy tắc phân loại kết quả** | [Tiêu chuẩn đánh giá: Đạt / Chưa đạt / Có mặt / Vắng mặt] |
| **9. Xử lý đối tượng ngoại lệ** | [Cách xử lý dữ liệu phát sinh từ đối tượng ngoài danh sách kế hoạch (vd: khách vãng lai)] |

### 3.2. Ma trận Kịch bản kiểm thử mẫu (Test Scenarios Matrix)

> Dữ liệu minh họa tính toán theo khung giờ quy định: `[Giờ bắt đầu]` đến `[Giờ kết thúc]` (Tổng thời lượng: `X phút`).

| Case | Chuỗi Dữ Liệu Đầu Vào | Dữ Liệu Sau Khi Cắt Biên | Phép Tính Cụ Thể | Kết Quả Đầu Ra | Trạng Thái & Cờ Ghi Nhận |
|:---:|---|---|---|:---:|---|
| **1** | `[Input chuẩn đầu cuối]` | `[Cặp chuẩn]` | `[Phép tính]` | **[Kết quả]** | Chuẩn mốc giờ, đạt 100%. |
| **2** | `[Input có ra vào giữa giờ]` | `[Nhiều cặp]` | `[Tổng các cặp]` | **[Kết quả]** | Rời vị trí N lần. |
| **3** | `[Input sớm/muộn ngoài giờ]` | `[Cắt bỏ phần ngoài]` | `[Tính trong giờ]` | **[Kết quả]** | Cắt biên giờ kế hoạch. |
| **4** | `[Input gửi trùng lặp vài giây]`| `[Khử trùng]` | `[Tính 1 lần]` | **[Kết quả]** | Bỏ lượt trùng tự động. |
| **5** | `[Input bị lẻ lượt cuối]` | `[Cặp + Lượt lẻ]` | `[Tính theo quy định]` | **[Kết quả + Cờ]**| Gắn cờ: Thiếu lượt đóng. |
| **6** | `[Input đối tượng ngoài Roster]`| `[Tính bình thường]` | `[Tính thời lượng]` | **[Kết quả]** | Lưu riêng danh sách ngoại lệ. |
| **7** | `[Không có dữ liệu phát sinh]` | `-` | `0` | **0** | Ghi nhận Vắng mặt (Absent). |

---

## 4. Đặc tả Use Cases chi tiết (Core Use Cases)

### 4.1. [MÃ-UC-01] — [Tên Use Case 1]

| Trường thông tin | Nội dung đặc tả |
|---|---|
| **Người thực hiện (Actor)** | [Tên vai trò / Hệ thống tự động] |
| **Điều kiện trước (Precondition)** | [Điều kiện tiên quyết để kích hoạt Use Case] |
| **Luồng chính (Main Flow)** | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3]<br>4. [Bước 4]<br>5. [Bước 5] |
| **Trường hợp đặc biệt (Exceptions)**| • [Trường hợp lỗi mạng, mất kết nối, dữ liệu không hợp lệ]<br>• [Trường hợp ngoại lệ về quyền hạn hoặc thời gian] |
| **Dữ liệu lưu trữ (Data Schema)** | [Danh sách các trường dữ liệu ghi nhận vào cơ sở dữ liệu] |
| **Hoàn thành khi (Postcondition)** | [Tiêu chuẩn nghiệm thu khi luồng kết thúc thành công] |

### 4.2. [MÃ-UC-02] — [Tên Use Case 2]

| Trường thông tin | Nội dung đặc tả |
|---|---|
| **Người thực hiện (Actor)** | [Tên vai trò / Hệ thống tự động] |
| **Điều kiện trước (Precondition)** | [Điều kiện tiên quyết để kích hoạt Use Case] |
| **Luồng chính (Main Flow)** | 1. [Bước 1]<br>2. [Bước 2]<br>3. [Bước 3] |
| **Trường hợp đặc biệt (Exceptions)**| • [Các trường hợp ngoại lệ phát sinh] |
| **Dữ liệu lưu trữ (Data Schema)** | [Danh sách các trường dữ liệu ghi nhận] |
| **Hoàn thành khi (Postcondition)** | [Tiêu chuẩn nghiệm thu hoàn thành] |

---

## 5. Đặc tả Cấu trúc Dữ liệu Xuất & Báo cáo (Data Export Schema)

### 5.1. Báo cáo Chi tiết Giao dịch (Raw Transaction Logs)
> Xuất toàn bộ nhật ký chi tiết từng lượt tương tác của đối tượng.

| Tên Cột / Trường Dữ Liệu | Kiểu Dữ Liệu | Mô Tả & Quy Tắc Ghi Nhận |
|---|:---:|---|
| `entity_id` | String | Mã định danh duy nhất của đối tượng (theo Master Data). |
| `transaction_time` | Timestamp | Giờ máy chủ chuẩn đến giây (`YYYY-MM-DD HH:mm:ss`). |
| `sequence_order` | Integer | Thứ tự giao dịch trong phiên làm việc ($1, 2, 3...$). |
| `action_type` | Enum | Loại hành vi: `IN` (Vào) hoặc `OUT` (Ra). |
| `device_id` / `location_id`| String | Mã thiết bị nhận diện hoặc mã địa điểm. |
| `session_id` | String | Mã định danh phiên làm việc / buổi học / ca làm việc. |
| `flags` | String | Cờ đánh dấu: Quẹt trùng (`DUP`), Ngoài danh sách (`UNREG`). |

### 5.2. Báo cáo Tổng hợp Phiên (Aggregated Session Rollup)
> Xuất kết quả tổng hợp sau khi xử lý thuật toán (Mỗi đối tượng một dòng duy nhất).

| Tên Cột / Trường Dữ Liệu | Kiểu Dữ Liệu | Mô Tả & Quy Tắc Ghi Nhận |
|---|:---:|---|
| `entity_id` | String | Mã định danh đối tượng. |
| `session_id` | String | Mã phiên làm việc. |
| `status` | Enum | Kết quả: `Có mặt`, `Vắng mặt`, `Vắng có phép (AM Duyệt)`. |
| `check_in_time` | Timestamp | Thời điểm bắt đầu hợp lệ đầu tiên. |
| `check_out_time` | Timestamp | Thời điểm kết thúc hợp lệ cuối cùng. |
| `trip_count` | Integer | Tổng số lần rời khỏi vị trí (Số cặp $- 1$). |
| `total_duration_minutes` | Integer | Tổng thời lượng thực tế sau khử trùng và cắt biên. |
| `compliance_status` | Enum | Đánh giá chuyên cần: `Đủ giờ` (Đạt ngưỡng) hoặc `Thiếu giờ`. |
| `anomaly_flags` | String | Cảnh báo dữ liệu bất thường (vd: `ODD_COUNT`). |

---

## 6. Yêu cầu Quản trị, Ngoại lệ & Audit Trail (Governance & Phase 2)

| Mã Tính Năng | Tên Tính Năng | Mô Tả Nghiệp Vụ & Quy Tắc Kiểm Soát | Thẩm Quyền AM Phê Duyệt |
|:---:|---|---|:---:|
| `GOV-01` | **Điều chỉnh dữ liệu thủ công** | Cho phép cấp quản lý/cán bộ vận hành sửa đổi dữ liệu khi phát sinh sự cố quên quẹt/lỗi thiết bị. Bắt buộc nhập lý do giải trình và lưu vết lịch sử người sửa (Audit Trail). | Cán bộ lớp / Quản lý vận hành |
| `GOV-02` | **Cơ chế xác thực dự phòng** | Cung cấp phương thức xác thực thay thế (qua Mobile App, Biometrics, Beacon) khi không mang theo thiết bị/thẻ vật lý. | Tự động xác thực qua SSO |
| `GOV-03` | **Phê duyệt vắng mặt có lý do** | Quy trình tiếp nhận đơn xin vắng mặt, tự động đẩy thông báo phê duyệt qua MS Teams Bot tới đúng Quản lý trực tiếp (QLTT) theo cây tổ chức. | Quản lý trực tiếp (QLTT) |
