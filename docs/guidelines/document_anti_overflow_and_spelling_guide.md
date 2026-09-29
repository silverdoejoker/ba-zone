# Hướng Dẫn Kỹ Thuật: Chống Tràn Trang A4, Bố Cục Bảng & Chuẩn Mực Chính Tả BA

> **Mã số tài liệu:** `NVG-ITD-GUI-08`  
> **Áp dụng cho:** Tất cả các tài liệu đặc tả BRD, URD, PRD, Solution Design (SOP14) và Báo cáo kiểm định tại NVG-ITC.  
> **Quy chuẩn nguồn:** Compounding Loop Lesson Learned (29/09/2026).

---

## 1. Bối Cảnh & Bài Học Kinh Nghiệm (Lesson Learned)

Trong quá trình xây dựng và xuất bản tài liệu BRD cho dự án Hệ thống Quản lý & Điểm danh Đào tạo (TAS), hệ thống đã ghi nhận 3 vấn đề kỹ thuật phổ biến gây ảnh hưởng nghiêm trọng đến trải nghiệm của Stakeholders (PMO, Sponsor, Khách hàng):

1. **Bảng dữ liệu nhiều chữ bị tràn lề ngang khi xuất PDF / Word:**
   - *Nguyên nhân:* Nhồi nhét 6-7 cột trong cùng một bảng (Mã, Tên tính năng, Hiện trạng QLCH, Giải pháp TAS, Phân kỳ hoàn thành), kết hợp với thuộc tính CSS `white-space: nowrap` và thiếu `table-layout: fixed`. Chiều rộng trang giấy A4 Portrait chỉ có ~16.5cm khả dụng, dẫn đến việc chữ bị tràn qua mép phải hoặc ép cột thành từng dòng 1-2 từ.
   - *Giải pháp triệt để:* Áp dụng **Ngân Sách Cột Tối Đa 4 Cột (Table Column Budget)** và **Tách bảng theo từng phân kỳ (Phase-based Split)**.
2. **Lỗi thẻ Markdown unclosed và lệch cột bảng:**
   - *Nguyên nhân:* Để sót ký tự in đậm mở mà không đóng (ví dụ `**Tiêu đề` thiếu `**` đóng ở dòng REP-02) hoặc các dòng dữ liệu thiếu dấu phân tách cột `|`.
   - *Giải pháp triệt để:* Thêm bộ quét syntax integrity tự động phát hiện thẻ lẻ.
3. **Lỗi chính tả & chuẩn mực xưng hô đối ngoại:**
   - *Nguyên nhân:* Sai chính tả các từ chuyên ngành BA (`giản viên` thay vì `giảng viên`, `thư kí` thay vì `thư ký`, `chuyên cân` thay vì `chuyên cần`), hoặc nêu đích danh cá nhân giảng viên (Ms. Quyên) như bên gây nghẽn tiến độ thay vì dùng danh xưng tập thể ngoại giao (`Phòng TRC`).
   - *Giải pháp triệt để:* Xây dựng Từ điển chính tả 26+ cặp từ lỗi và bộ lọc giọng văn doanh nghiệp trong kịch bản kiểm tra tự động `scripts/audit_outputs.py`.

---

## 2. Quy Tắc "Ngân Sách 4 Cột" Cho Bảng Nghiệp Vụ (Table Column Budget)

Khi thiết kế bảng đặc tả tính năng / đối chiếu hệ thống (Feature Mapping Matrix) trong môi trường A4 Portrait:

### ❌ Anti-Pattern (Tuyệt đối tránh):
```markdown
| STT | Mã BRD | Tính Năng Yêu Cầu (Rất Dài) | Hiện Trạng Hệ Thống Cũ (Rất Dài) | Giải Pháp Mới (Rất Dài) | Phân Kỳ Triển Khai |
```
*Hệ quả:* 6 cột với 3 cột diễn giải dài chắc chắn sẽ vỡ khung trang giấy A4, tràn lề khi in và biến dạng khi import sang Word (.docx).

### ✅ Best Practice (Bắt buộc áp dụng):
**Tách bảng làm 2 nhóm phân kỳ riêng biệt**, bỏ cột "Phân kỳ" và sử dụng **4 cột chuẩn vàng**:

```markdown
#### 4.1.1. Nhóm Tính Năng Giai Đoạn 1 (Thử Nghiệm Pilot — Ưu Tiên 1)
| STT (6%) | Mã & Yêu Cầu Nghiệp Vụ (30%) | Kế Thừa Nền Tảng Sẵn Có (32%) | Giải Pháp Kỹ Thuật Đáp Ứng (32%) |

#### 4.1.2. Nhóm Tính Năng Giai Đoạn 2 (Tích Hợp API & Mở Rộng — Ưu Tiên 2)
| STT (6%) | Mã & Yêu Cầu Nghiệp Vụ (30%) | Kế Thừa Nền Tảng Sẵn Có (32%) | Giải Pháp Kỹ Thuật Đáp Ứng (32%) |
```
*Lợi ích:* Mỗi cột mô tả kỹ thuật có hơn **5.5cm chiều rộng**, bảng thông thoáng, dễ đọc, 100% không bị tràn trang khi in ấn hoặc xuất PDF.

---

## 3. Khung CSS Chống Tràn Trang Chuẩn Cho File HTML

Mọi tài liệu HTML giao tiếp hoặc in ấn phải tích hợp khối CSS sau:

```css
/* 1. Khóa cứng chiều rộng bảng trong giao diện Web */
table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    margin: 14px 0 24px 0;
    font-size: 13px;
    word-wrap: break-word;
    word-break: break-word;
}

th, td {
    padding: 9px 12px;
    text-align: left;
    border: 1px solid #ebecf0;
    vertical-align: top;
    word-wrap: break-word;
    word-break: break-word;
}

/* 2. Tuyệt đối không để nowrap ở th khi bảng có nhiều cột */
th {
    background-color: #f4f5f7;
    font-weight: 600;
    color: #172b4d;
    white-space: normal;
}

/* 3. Cấu hình khổ giấy in ấn A4 Portrait */
@page {
    size: A4 portrait;
    margin: 12mm 10mm;
}

@media print {
    .action-bar { display: none !important; }
    body { background: white !important; font-size: 10px !important; color: #000 !important; }
    .container { box-shadow: none !important; padding: 0 !important; max-width: 100% !important; border: none !important; }
    table { font-size: 9px !important; table-layout: fixed !important; width: 100% !important; }
    th, td { padding: 4px 6px !important; line-height: 1.35 !important; }
    th { background-color: #f0f0f0 !important; color: #000 !important; white-space: normal !important; }
    tr { page-break-inside: avoid !important; }
}
```

---

## 4. Bảng Từ Điển Chính Tả Tiếng Việt Chuẩn Hóa Tại NVG-ITC

| Từ thường gõ nhầm / Không chuẩn | Từ chuẩn mực bắt buộc | Ghi chú ngữ cảnh |
|---|---|---|
| `giản viên` | **giảng viên** | Giảng viên đào tạo, vai trò AM |
| `thư kí` | **thư ký** | Thư ký lớp, nghiệp vụ QLCH |
| `qui trình` | **quy trình** | Quy trình phê duyệt AM |
| `chuyên cân` | **chuyên cần** | Báo cáo chuyên cần, điểm danh |
| `điễm danh`, `diem danh` | **điểm danh** | Ứng dụng điểm danh TAS |
| `chuổi` | **chuỗi** | Chuỗi timestamp quẹt thẻ |
| `xữ lý`, `xử lí` | **xử lý** | Xử lý dữ liệu, Duration Engine |
| `sắp sếp` | **sắp xếp** | Sắp xếp lượt quẹt |
| `thời lựong` | **thời lượng** | Thời lượng học thực tế |
| `lưu trử` | **lưu trữ** | Lưu trữ CSDL |
| `đăng nhâp` | **đăng nhập** | Xác thực hệ thống SSO |
| `thực tê` | **thực tế** | Nghiệp vụ thực tế |
| `hệ thốn` | **hệ thống** | Cấu trúc hệ thống |
| `báo các` | **báo cáo** | Mẫu biểu báo cáo 5.1 & 5.2 |
| `thẩm quyên` | **thẩm quyền** | Thẩm quyền phê duyệt trong AM |

---

## 5. Chuẩn Mực Văn Phong Doanh Nghiệp (Diplomatic Corporate Tone)

1. **Nguyên tắc tôn trọng đơn vị nghiệp vụ (TRC/Khách hàng):**
   - Không ghi tên cá nhân giảng viên như một nguyên nhân làm chậm tiến độ (ví dụ: *"Đang chờ cô Quyên duyệt"* ➔ **SAI**).
   - Bắt buộc dùng đại diện danh xưng tập thể ngoại giao: *"Phòng TRC phối hợp cùng ITC thống nhất tiêu chí..."* hoặc *"Đại diện Khối Đào tạo TRC cử đầu mối đối ứng..."* ➔ **ĐÚNG**.
2. **Nguyên tắc phân định ranh giới BA vs PMO (Timeline Authority):**
   - BA tuyệt đối không tự ý gán cứng các mốc thời gian phụ thuộc (như ngày UAT Pilot, ngày Go-Live) vào BRD khi chưa có sự thống nhất giữa PMO và Lãnh đạo hai bên.
   - Các mốc phụ thuộc phải ghi rõ: *"Mốc thời gian do PMO (Ms. Tú) và Lãnh đạo ấn định trong Master Schedule (`Lich trinh Du an Chuyen doi so - TRC.xlsx`)"*.
3. **Nguyên tắc trao đổi nội bộ ITC:**
   - Toàn bộ việc phân chia task nội bộ (giữa BA, Dev Lead, QA, PMO) phải thực hiện qua trao đổi trực tiếp và quản lý qua Master Schedule của PMO, không đưa các trao đổi ad-hoc hoặc việc giao việc nội bộ vào tài liệu chính thức gửi cho Business.

---

## 6. Quy Chuẩn Thiết Kế Text-First & Tương Thích Microsoft Word (PDF $\rightarrow$ DOCX Zero Broken Graphics)

Khi tài liệu đặc tả HTML/PDF được chuyển đổi sang Microsoft Word (`.docx`) để gửi đi thẩm định hoặc lưu trữ:

### 6.1. Tại sao layout bị vỡ khi convert sang Word?
1. **CSS Grid (`display: grid`):** Word không hỗ trợ CSS Grid. Trình convert biến mỗi ô `div` trong grid thành một **khung vẽ tự do (Drawing Canvas / Shape)** trôi nổi độc lập, dẫn đến hiện tượng các ô đè lên nhau, vỡ viền hoặc nhảy trang.
2. **Pill Badges (`border-radius: 20px; display: inline-block`):** Mỗi thẻ huy hiệu bo tròn biến thành một hình vẽ vector riêng biệt, làm văn bản bên trong bị lệch tâm hoặc ngắt dòng lộn xộn.
3. **Sơ đồ Mermaid SVG:** Khi convert sang Word, vector SVG thường bị vỡ thành hàng chục mảnh đường cong (broken vector paths) hoặc bị Word loại bỏ hoàn toàn thành khung trống.

### 6.2. Các quy tắc chuẩn hóa "Text-First" bắt buộc
1. **Dùng Bảng Thuần (Native Table) Thay Cho Card Grid:**
   - **Document Metadata:** Thay `display: grid; grid-template-columns: repeat(2, 1fr)` bằng thẻ `<table>` 2 cột (`<table class="meta-table">`) với tỷ lệ chiều rộng `50% - 50%`.
   - **KPI Metric Decks:** Thay 4 thẻ div `.kpi-card` bằng thẻ `<table>` 1 dòng 4 cột (`<table class="kpi-table">`), mỗi ô `25%` có viền mỏng và nền sáng. Word sẽ nhận diện 100% thành native Word Table cố định, không sinh shape trôi nổi.
2. **Dùng Nhãn Ký Tự Ngoặc Vuông (Text-First Bracketed Labels):**
   - Thay vì thẻ `span` bo tròn nhiều pixel, sử dụng ký tự văn bản: `<strong>[NVG-ITD-SOP14.F01 · DRAFT v0.2]</strong>` hoặc `<strong>[SẴN SÀNG PILOT — 9 TÍNH NĂNG]</strong>`. Dù Word có xóa bỏ CSS background thì nhãn văn bản vẫn rõ ràng, đẹp mắt và không tạo rác đồ họa.
3. **Bắt Buộc Có Bảng Văn Bản Dự Phòng Dưới Sơ Đồ (Diagram Text Fallback Table):**
   - Dưới bất kỳ sơ đồ Mermaid nào (Kiến trúc hệ thống, Lưu đồ thuật toán), luôn bổ sung một bảng văn bản tóm tắt các tầng / các bước / luồng dữ liệu tương ứng.
   - Khi chuyển sang Word, người đọc vẫn có đầy đủ 100% dữ liệu kỹ thuật từ bảng văn bản mà không cần ai phải vẽ lại sơ đồ.
4. **Hộp Ghi Chú & Use Case Hợp Chuẩn:**
   - Dùng `<blockquote>` hoặc thẻ `<div>` có `border-left: 3px solid ...` và `background: #f8f9fa`, không dùng `box-shadow` hay `border-radius` lớn. Word tự động chuyển cấu trúc này thành paragraph shading và paragraph border native của Word.

