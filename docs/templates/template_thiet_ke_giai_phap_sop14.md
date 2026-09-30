# MẪU TÀI LIỆU THIẾT KẾ GIẢI PHÁP (NVG SOLUTION ARCHITECTURE DESIGN TEMPLATE)
> **Mã số mẫu biểu tập đoàn:** `NVG-ITD-SOP14.F01`  
> **Tên tài liệu:** TÀI LIỆU THIẾT KẾ GIẢI PHÁP (SOLUTION ARCHITECTURE & DESIGN DOCUMENT - SAD / BRD-SOLUTION)  
> **Đơn vị ban hành:** Khối Công nghệ Thông tin (NVG-ITC)  
> **Áp dụng cho:** IT Business Analysts, Solution Architects, Technical Leads khi đặc tả giải pháp hệ thống chi tiết cho các ứng dụng phần mềm của Tập đoàn NovaGroup.  
> **Quy chuẩn kiểm soát:** Tuân thủ chuẩn Ma trận Phê duyệt (`AM - Approval Matrix`, cấm dùng Authority Matrix) và Tiêu chuẩn Kiến trúc `Dev Architecture Spine Baseline 2026`.

---

# CÔNG TY CỔ PHẦN NOVAGROUP
## TÀI LIỆU THIẾT KẾ GIẢI PHÁP
### [TÊN DỰ ÁN / PHÂN HỆ HỆ THỐNG]

---

## 1. BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU (DOCUMENT CHANGE HISTORY)

| Ngày | Tác giả | Mô tả thay đổi | Phiên bản | Tính năng | Ghi chú (*) |
|:---:|---|---|:---:|---|:---:|
| [DD/MM/YYYY] | [Họ tên tác giả BA/SA] | [Tóm tắt nội dung khởi tạo / chỉnh sửa] | `V0.1` | [Mã phân hệ] | `M` |
| [DD/MM/YYYY] | [Họ tên tác giả BA/SA] | [Cập nhật theo góp ý của Stakeholder] | `V1.0` | [Mã phân hệ] | `S` |

*Ghi chú ký hiệu:*  
- **M (New):** Thêm mới yêu cầu / tính năng  
- **S (Modify):** Sửa đổi yêu cầu / luồng xử lý  
- **X (Delete):** Xóa bỏ / Hủy tính năng  

---

## 2. THÔNG TIN CHUNG (GENERAL INFORMATION)

### 2.1. Phạm vi tài liệu (Document Scope)
* Xác định ranh giới đối tượng độc giả và nội dung tài liệu: Dành cho các bên liên quan gồm Lãnh đạo Khối nghiệp vụ, PMO, BA, Kiến trúc sư giải pháp (SA), Đội ngũ Phát triển phần mềm (Dev), và Đội ngũ Kiểm thử chất lượng (QA/QC).
* Ranh giới phân kỳ triển khai (Phase 1 vs Phase 2).

### 2.2. Mục đích tài liệu (Document Purpose)
* Chuyển hóa các yêu cầu bài toán nghiệp vụ từ Đơn vị yêu cầu thành kiến trúc giải pháp hệ thống chi tiết.
* Làm căn cứ nghiệm thu chất lượng (UAT Criteria) và ký biên bản hoàn thành giải pháp phần mềm giữa Khối nghiệp vụ và Khối CNTT (ITC).

### 2.3. Khái niệm, thuật ngữ & Từ viết tắt (Glossary & Terminology)

| Thuật Ngữ / Viết Tắt | Tên Tiếng Anh Đầy Đủ | Giải Thích Định Nghĩa Nghiệp Vụ Tại NovaGroup |
|---|---|---|
| **AM** | **Approval Matrix** | **Ma trận Phê duyệt / Ma trận Thẩm quyền Phê duyệt** tại NovaGroup (tuyệt đối không dùng *Authority Matrix*; thay thế thuật ngữ RBAC đơn thuần, phân tách Functional Permission và Security L7 Data Scope). |
| **GFA** | Gross Floor Area | Tổng diện tích sàn xây dựng của dự án/tòa nhà do Khối Quản lý Tài sản (NAM) theo dõi. |
| **NLA** | Net Lettable Area | Diện tích thực tế cho thuê thương mại, dùng để tính toán doanh thu và tỷ lệ lấp đầy (Occupancy Rate %). |
| **Fit-out** | Tenant Interior Fit-out | Giai đoạn khách thuê thi công cải tạo, hoàn thiện nội thất gian hàng trước ngày mở cửa khai trương. |
| **Rent-free** | Rent-free Period | Thời gian miễn phí tiền thuê mặt bằng để hỗ trợ khách thuê thi công hoàn thiện nội thất. |
| **Turnover Rent** | Revenue Share Rent | Phương thức tính tiền thuê biến đổi theo tỷ lệ % Doanh thu thực tế của gian hàng: $\max(\text{Min Rent}, \% \text{Turnover})$. |
| **ĐXCT** | Proposal / Deal Closing Approval | **Tờ trình Đề xuất Cho thuê** (theo mẫu tập đoàn `CCM-SOP01.F02`), là căn cứ chính thức để kích hoạt Khóa Căn Tự Động. |
| **BBBG** | Handover Record | Biên Bản Bàn Giao mặt bằng hiện trạng giữa Bên Cho Thuê và Khách Thuê. |

### 2.4. Tài liệu tham khảo (References)

| STT | Tên Tài Liệu / Mã Tham Chiếu | Phiên Bản / Ngày Ban Hành | Nguồn / Đơn Vị Ban Hành |
|:---:|---|:---:|---|
| 1 | `NVG-ITD-SOP01.F01`: Phiếu Yêu cầu Phát triển Ứng dụng | 2025 | Khối CNTT (ITC) |
| 2 | `NVG-ITD-SOP14.F01`: Quy trình Thiết kế Tài liệu Giải pháp | 2026 | Khối CNTT (ITC) |
| 3 | `NVLG-LS-SOP03` & `CCM-SOP01.F02`: Quy trình Đề xuất Cho thuê | 2018 / 2026 | Tập đoàn NovaGroup / NLE |
| 4 | `MẪU HĐ THUÊ NRM`: Hợp đồng thuê sàn xây dựng chuẩn | 2026 | Ban Pháp chế & NLE |
| 5 | Biên bản cuộc họp Discovery Workshop (MoM) | 24/09/2026 | ITC – NLE – NAM |

---

## 3. TỔNG QUAN ỨNG DỤNG (APPLICATION OVERVIEW)

### 3.1. Mục đích (Objectives & SMART Goals)
* **S (Specific):** Xây dựng giải pháp phần mềm chuyên dụng giải quyết toàn diện bài toán số hóa...
* **M (Measurable):** Đạt 100% tự động hóa... thời gian phản hồi hệ thống $\le 3$ giây...
* **A (Achievable):** Kế thừa kiến trúc nền tảng hiện có, đảm bảo tính khả thi trong khung thời gian quy định.
* **R (Relevant):** Bám sát mục tiêu Chuyển đổi số của Ban Lãnh đạo Tập đoàn.
* **T (Time-bound):** Nghiệm thu và đưa vào vận hành thực tế trong [Thời gian mốc].

### 3.2. Phạm vi (System Scope Boundaries)
* **Phạm vi trong hệ thống (In-Scope Phase 1):** [Liệt kê các phân hệ, chức năng được xây dựng ngay].
* **Phạm vi ngoài hệ thống (Out-of-Scope Phase 2):** [Liệt kê các tính năng hoãn lại giai đoạn sau để kiểm soát tiến độ].

### 3.3. Quyền hạn sử dụng & Ma trận AM (Approval Matrix & Security L7)
* Phân tách rõ ràng giữa **Quyền chức năng (Functional Permissions)** và **Phạm vi dữ liệu (Security L7 Data Scope)** theo quy chuẩn Dev Architecture Spine 2026.

| Vai trò Nghiệp vụ (AM Role) | Mã Phân Quyền | Quyền Thao Tác Chức Năng | Thẩm Quyền Phê Duyệt | Phạm Vi Dữ Liệu Cho Phép (Data Scope) |
|---|:---:|---|---|---|
| [Tên vai trò 1] | `role.code_1` | [Xem, tạo, sửa...] | [Thẩm quyền ký duyệt] | [Dự án được phân công / Toàn khối / Toàn tập đoàn] |
| [Tên vai trò 2] | `role.code_2` | [Xem, thẩm định...] | [Thẩm quyền ký duyệt] | [Phạm vi dữ liệu quản lý] |

---

## 4. MÔ TẢ YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS)

### 4.1. Danh sách yêu cầu chức năng (Feature Matrix)

| Mã Yêu Cầu | Tên Chức Năng Nghiệp Vụ | Mức Ưu Tiên | Phân Kỳ Triển Khai | Mô Tả Tóm Tắt Giải Pháp |
|:---:|---|:---:|:---:|---|
| `REQ-01` | [Tên chức năng 1] | Critical / High | Phase 1 | [Tóm tắt hành vi giải pháp] |
| `REQ-02` | [Tên chức năng 2] | Critical / High | Phase 1 | [Tóm tắt hành vi giải pháp] |
| `REQ-03` | [Tên chức năng 3] | High | Phase 1 | [Tóm tắt hành vi giải pháp] |

### 4.2. Đặc tả Use Cases chi tiết (Core Use Cases - Karl Wiegers Standard)

#### [UC-XX] — [Tên Use Case]
* **Người thực hiện (Actor):** [Tên vai trò thực hiện]
* **Điều kiện tiên quyết (Preconditions):** [Điều kiện trước khi kích hoạt]
* **Luồng xử lý chính (Main Flow):**
  1. Bước 1...
  2. Bước 2...
  3. Bước 3...
* **Luồng ngoại lệ (Alternative / Exception Flows):**
  * *Ngoại lệ 1:* [Mô tả và cách xử lý lỗi]
  * *Ngoại lệ 2:* [Mô tả và cách xử lý lỗi]
* **Dữ liệu ghi nhận (Data Entities):** [Tên bảng CSDL lưu vết]
* **Điều kiện kết thúc (Postconditions):** [Trạng thái sau khi hoàn thành]

---

## 5. GIẢI PHÁP HỆ THỐNG (SYSTEM ARCHITECTURE & SOLUTION DESIGN)

### 5.1. Kiến trúc Tổng thể & Nguyên tắc Kỹ thuật Baseline 2026
* **Zero Local Auth:** 100% người dùng nội bộ đi qua Application Gateway tích hợp SSO MS Entra ID.
* **Database Schema Invariant:** Bảng CSDL mang tiền tố `{prefix}_` (vd: `gms_*`), tích hợp đủ 5 cột audit metadata (`createdAt`, `updatedAt`, `deletedAt`, `createdBy`, `updatedBy`).
* **Strict Soft-Delete Invariant 100%:** Tuyệt đối không xóa vật lý (Zero Hard-Delete), chỉ cập nhật `deletedAt`.
* **Async Queue:** Xử lý bất đồng bộ qua RabbitMQ / NATS cho các tác vụ khối lượng lớn (tính tiền hàng loạt, xuất PDF, import Excel).

### 5.2. Giải pháp Cơ sở Dữ liệu & Thực thể (Database Schema Design)
* Danh sách bảng CSDL mang tiền tố chuẩn hóa `{prefix}_*`.
* Mô tả chi tiết các trường dữ liệu và quan hệ khóa ngoại (ERD / Tables catalog).

### 5.3. Công thức Tính toán & Ma trận Kịch bản Kiểm thử (Calculation Engine & Test Matrix)
* Các công thức toán học và quy tắc nghiệp vụ (Business Rules).
* Ma trận các kịch bản kiểm thử mẫu (Test Scenarios Matrix) bảo đảm tính chính xác của thuật toán.

### 5.4. Sơ đồ Luồng Tuần tự (Sequence Diagram)
* Sơ đồ tương tác giữa Người dùng, Giao diện UI, Dịch vụ Backend, Cơ sở dữ liệu và Hệ thống bên ngoài.

### 5.5. Cấu trúc Dữ liệu Xuất Báo cáo & Tích hợp (Data Export & Integration Schema)
* Cấu trúc dữ liệu nhật ký giao dịch thô (Raw Transaction Logs).
* Cấu trúc dữ liệu báo cáo tổng hợp (Aggregated Rollup Reports) đẩy về Kho dữ liệu EDP Lakehouse của Tập đoàn.
