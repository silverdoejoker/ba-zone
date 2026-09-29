# Quy Chuẩn Kiểm Định Chất Lượng Đầu Ra (Output Quality & Standards Rule)

## Mục Đích & Phạm Vi Áp Dụng
Tất cả các tài liệu đặc tả nghiệp vụ, kiến trúc giải pháp, báo cáo phân tích, kế hoạch hành động và biên bản họp lưu trữ trong `docs/outputs/` (dưới cả định dạng `.md` và `.html`) **BẮT BUỘC** phải tuân thủ nghiêm ngặt 3 trụ cột chất lượng:
1. **Cấu Trúc Tài Liệu (Structure Standards)**
2. **Định Dạng & Chống Tràn Trang (Format & Anti-Overflow Standards)**
3. **Chính Tả Tiếng Việt & Chuẩn Mực Giao Tiếp Doanh Nghiệp (Spelling & BA Terminology)**

Quy chuẩn này được thực thi tự động qua kịch bản `scripts/audit_outputs.py` và là điều kiện tiên quyết (Gatekeeper) trước khi bàn giao bất kỳ tài liệu nào cho người dùng hoặc xuất bản ra khách hàng / Hội đồng thẩm định.

---

## TRỤ CỘT I: QUY CHUẨN CẤU TRÚC (STRUCTURE STANDARDS)

### 1. Khung Kiểm Soát Tài Liệu (Document Control Block)
Mọi tài liệu chính thức (BRD, Solution Architecture, Action Plan) phải mở đầu bằng khối metadata tối thiểu 6 trường:
- **Mã số biểu mẫu:** Chuẩn biểu mẫu tập đoàn (ví dụ `NVG-ITD-SOP14.F01` cho Solution Architecture Design, hoặc `TEMPLATE-BRD-NVG-STD-2026`).
- **Mã số định danh:** Mã tài liệu duy nhất (ví dụ `BRD-TAS-2026-v0.2`).
- **Phiên bản (Version):** Đánh số phiên bản theo quy ước `vX.Y` kèm mô tả vắn tắt nội dung thay đổi.
- **Ngày lập (Date):** Định dạng `dd/mm/yyyy`.
- **Tác giả (Author):** Họ tên, chức danh và địa chỉ email cán bộ NVG-ITC.
- **Chủ trì & Phê duyệt (Approval Authorities):** Ghi rõ Sponsor, PMO Specialist, Dev Lead, Đơn vị Nghiệp vụ đối ứng.

### 2. Thứ Bậc Tiêu Đề Nhất Quán (Heading Hierarchy)
- **Duy nhất 01 thẻ H1 (`#`)** cho tiêu đề chính của toàn bộ tài liệu.
- **Không nhảy cóc cấp độ heading:** Từ H1 (`#`) phải tuần tự đến H2 (`##`), H3 (`###`), H4 (`####`). Tuyệt đối không nhảy từ H1 thẳng xuống H3 hoặc H4.
- **Mục lục tổng quan (TOC):** Phải phản ánh chính xác cấu trúc các mục H2/H3 thực tế trong tài liệu.

### 3. Phân Định Phạm Vi Rõ Ràng (Scoping In/Out & Phasing)
- Bắt buộc phân tách ranh giới rõ ràng:
  - **In-Scope Giai đoạn 1 (Thử nghiệm UAT Pilot / Ưu tiên 1)**
  - **In-Scope Giai đoạn 2 (Tích hợp API / Mở rộng toàn diện)**
  - **Out-of-Scope (Phạm vi nằm ngoài hệ thống)**
- Không gán cứng ngày tháng cố định vào các mốc phụ thuộc thẩm quyền PMO/Hội đồng Dự án (ví dụ mốc UAT Pilot, mốc Go-Live); các mốc này phải ghi rõ thẩm quyền điều phối thuộc PMO trong Master Schedule.

---

## TRỤ CỘT II: ĐỊNH DẠNG & CHỐNG TRÀN TRANG (FORMAT & ANTI-OVERFLOW)

### 1. Ngân Sách Số Cột Bảng (Table Column Budget Policy)
Khi in ấn hoặc xuất PDF/Docx khổ giấy A4 Portrait, chiều rộng khả dụng của trang in chỉ có **~16.5cm** (sau khi trừ lề chuẩn 10-12mm). Do đó:
- **Bảng có cột mô tả diễn giải dài (text-heavy columns):** Tối đa **04 cột**:
  `STT (5-6%) | Mã & Yêu Cầu Nghiệp Vụ (30%) | Mapping / Hiện Trạng (32%) | Giải Pháp Kỹ Thuật (32%)`
- **Tuyệt đối KHÔNG gộp chung 6-7 cột** trong một bảng khi nội dung có nhiều câu dài. Nếu có nhiều phân kỳ, bắt buộc phải **tách bảng theo từng phân kỳ** (ví dụ: Bảng 4.1.1 cho Giai đoạn 1 Pilot, Bảng 4.1.2 cho Giai đoạn 2 API).
- **Cân bằng số cột trong bảng Markdown:** Toàn bộ các dòng dữ liệu (`data rows`) phải có số lượng ô phân tách (`|`) bằng chính xác số lượng ô ở dòng tiêu đề (`header row`).

### 2. Khóa Cứng CSS Chống Tràn Trang Trong File HTML
Mọi file `.html` tài liệu phải áp dụng đầy đủ bộ CSS bảo vệ:
```css
/* Khóa cố định bảng không vượt chiều rộng trang */
table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    word-wrap: break-word;
    word-break: break-word;
}
th, td {
    word-break: break-word;
    overflow-wrap: break-word;
}
th {
    white-space: normal; /* Không dùng nowrap trên bảng nhiều cột */
}

/* Quy chuẩn in ấn A4 Portrait */
@page {
    size: A4 portrait;
    margin: 12mm 10mm;
}
@media print {
    .action-bar { display: none !important; }
    body { background: white !important; font-size: 10px !important; }
    table { font-size: 9px !important; table-layout: fixed !important; width: 100% !important; }
    tr { page-break-inside: avoid !important; }
}
```

### 3. Tính Toàn Vẹn Cú Pháp Markdown (Syntax Integrity)
- **Thẻ mở phải có thẻ đóng đối ứng:** Tuyệt đối không để sót thẻ Markdown mở mà quên đóng, ví dụ `**nội dung` thiếu dấu `**` đóng, hoặc `` `code `` thiếu dấu đóng backtick.
- **Liên kết nội bộ (Cross-links):** Mọi cú pháp `[Tên](đường_dẫn)` phải trỏ chính xác đến file đang tồn tại thực tế.
- **Sơ đồ Mermaid:** 100% diagram phải hợp lệ cú pháp, có keyword mở đầu chuẩn (`flowchart`, `graph`, `sequenceDiagram`, `erDiagram`).

### 4. Quy Cách Dấu Câu & Khoảng Trắng (Typography & Spacing)
- **Không đặt khoảng trắng trước dấu câu:** Sai: `tính năng ,` hoặc `hệ thống .` hoặc `lưu trữ :`. Đúng: `tính năng,`, `hệ thống.`, `lưu trữ:`.
- **Bắt buộc có 01 khoảng trắng sau dấu câu:** Sai: `tính năng,sau đó`. Đúng: `tính năng, sau đó`.
- **Không lặp dấu câu bất thường:** Trừ dấu ba chấm (`...`), không sử dụng `??`, `!!`, `::`, `..`.

---

## TRỤ CỘT III: CHÍNH TẢ & CHUẨN MỰC GIAO TIẾP (SPELLING & BA CONVENTIONS)

### 1. Danh Mục Từ Điển Bắt Lỗi Chính Tả Tiếng Việt Phổ Biến Trong Tài Liệu BA
Script audit sẽ chặn và báo lỗi nếu phát hiện các từ sai chính tả sau:

| Từ sai chính tả / Lỗi gõ | Từ chuẩn xác bắt buộc | Lĩnh vực thường gặp |
|---|---|---|
| `giản viên` | **giảng viên** | Đào tạo, phân vai hệ thống |
| `thư kí` | **thư ký** | Vai trò nghiệp vụ, QLCH |
| `qui trình` | **quy trình** | Luồng nghiệp vụ |
| `chuyên cân` | **chuyên cần** | Báo cáo điểm danh |
| `điễm danh`, `diem danh` | **điểm danh** | Nghiệp vụ TAS / QLCH |
| `chuổi` | **chuỗi** | Chuỗi timestamp, chuỗi ký tự |
| `xữ lý` | **xử lý** | Logic xử lý hệ thống |
| `sắp sếp` | **sắp xếp** | Sắp xếp thứ tự, dữ liệu |
| `thời lựong` | **thời lượng** | Thời lượng học, họp |
| `lưu trử` | **lưu trữ** | CSDL, nhật ký dữ liệu |
| `đăng nhâp` | **đăng nhập** | Xác thực hệ thống |
| `thực tê` | **thực tế** | Nghiệp vụ thực tế |
| `hệ thốn` | **hệ thống** | Cấu trúc hệ thống |
| `báo các` | **báo cáo** | Kết xuất báo cáo |
| `kêt quả` | **kết quả** | Kết quả tính toán, xử lý |
| `thiêt bị` | **thiết bị** | Thiết bị POS, phần cứng |
| `phân hê` | **phân hệ** | Phân hệ phần mềm |
| `đôi ứng` | **đối ứng** | Cán bộ đối ứng nghiệp vụ |
| `thẩm quyên` | **thẩm quyền** | Thẩm quyền phê duyệt |
| `quẹt the` | **quẹt thẻ** | Thao tác POS NFC |
| `chức năg` | **chức năng** | Đặc tả chức năng |

### 2. Kiểm Soát Lỗi Vỡ Font & Mã Hóa UTF-8 (Mojibake)
- Toàn bộ file text phải lưu chuẩn `UTF-8` không BOM hoặc UTF-8 chuẩn.
- Bị chặn nếu chứa chuỗi ký tự vỡ font do sai encoding (ví dụ `Ä‘`, `Ã¡`, `Ãª`, `á»`, `Ã´`).

### 3. Chuẩn Mực Thuật Ngữ Nghiệp Vụ NVG (Mandatory Terminology)
- **Ma trận phân quyền & thẩm quyền:** Bắt buộc dùng thuật ngữ **"AM" (Authority Matrix)** hoặc **"Ma trận AM"**. Không dùng thuật ngữ kỹ thuật thuần túy như "RBAC" trong trao đổi và đề mục tài liệu với Stakeholders.
- **Ranh giới Dev Architecture Spine 2026:**
  - Tách bạch 2 tầng: **Quyền chức năng (Functional Permissions)** và **Phạm vi dữ liệu (Security L7 Data Scope)**.
  - Prefix bảng CSDL: `{prefix}_` (ví dụ `tas_*`, `gms_*`).
  - 100% Xóa mềm (Strict Soft-delete), cấm mô tả Hard-delete dữ liệu.
  - Tác vụ nặng (Excel import, tính toán khối lượng lớn, xuất PDF) phải có cơ chế bất đồng bộ (Async Queue).

### 4. Chuẩn Mực Ứng Xử & Giao Tiếp Doanh Nghiệp (Diplomatic Corporate Tone)
- **Quy chuẩn danh xưng cán bộ ITC:**
  - Ms. Trang (Giám đốc Bộ phận Quản lý CĐS ITC - Sponsor): `itc.gdbp.4@novagroup.vn`
  - Ms. Tú (Chuyên gia PMO): `itc.cg.3@novagroup.vn` (Tuyệt đối không dùng "anh Tú").
  - Ms. Khanh (BA PM QLCH): `itc.cvcc.3@novagroup.vn` (Tuyệt đối không viết thành "Khánh" hay "Nguyễn Thúy Mai").
  - Minh / Trần Quang Anh (Lead IT BA tác giả): `itc.cvcc.55@novagroup.vn`.
- **Giao tiếp với Đơn vị Nghiệp vụ / Giảng viên (TRC):**
  - Trong mục Giả định, Tồn đọng (Open Clarifications), Đề xuất & Kết luận: **Không nêu đích danh cá nhân giảng viên/chuyên gia như một bên gây nghẽn tiến độ**.
  - Luôn sử dụng danh xưng tập thể ngoại giao: *"Phòng TRC phối hợp cung cấp thêm thông tin..."*, *"Ban Đào tạo TRC cử đầu mối thống nhất tiêu chí..."*.
  - Nội bộ ITC làm việc trao đổi trực tiếp để thống nhất phương án, không đưa các trao đổi ad-hoc hoặc việc giao việc nội bộ vào tài liệu chính thức gửi cho Business.

---

## CƠ CHẾ THỰC THI (SELF-HEALING AUTO-AUDIT HOOK)
1. **Trigger:** Tự động kích hoạt ngay sau khi Agent tạo mới hoặc chỉnh sửa bất kỳ tài liệu nào trong `docs/outputs/`.
2. **Command:** `python scripts/audit_outputs.py` (hoặc `powershell ./scripts/audit-all.ps1`).
3. **Action:**
   - Nếu phát hiện cảnh báo hoặc lỗi: Agent tự động sửa lỗi ngay lập tức trên file (Self-healing).
   - Chỉ bàn giao khi trạng thái kiểm thử đạt: **`Audit Status: PASS` (0 Errors)**.
