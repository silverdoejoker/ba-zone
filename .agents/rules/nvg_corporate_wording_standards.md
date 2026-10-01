# NVG Corporate Wording & Anti-AI Smell Standards (Chuẩn Mực Từ Ngữ Doanh Nghiệp & Chống "Mùi AI")

## Nguồn Tham Chiếu
Đúc kết trực tiếp từ tài liệu thực tế của **Ms. Hân (Han Vu - ITC-NVG)**:  
`docs/templates/NVL_ITD_SDD_Hệ thống thanh kiểm tra ICS copy.pdf` (Tài liệu Thiết kế Giải pháp SDD chuẩn NovaGroup).

---

## 1. Triết Lý Văn Phong: Thực Tế, Gãy Gọn & Nói Thẳng Vào Nghiệp Vụ
- **Không chém gió, không hoa mỹ:** Tài liệu kỹ thuật & giải pháp tại NovaGroup dùng để Dev lập trình, QA kiểm thử và Business nghiệm thu. Tuyệt đối không dùng phong cách tiếp thị, báo cáo chính trị hay chatbot ngoại giao.
- **Không viết lý thuyết sách vở:** Tuyệt đối cấm đưa các bảng phân tích hàn lâm (như định nghĩa các chữ cái S-M-A-R-T, template 16 trường Use Case Karl Wiegers...). Thay vào đó, viết thẳng hành động của người dùng, màn hình giao diện và quy tắc xử lý (Business Rules).

---

## 2. Từ Điển Thanh Lọc "Mùi AI" (Anti-AI Smell Dictionary)

| Cụm Từ Bị Cấm (Mùi AI) | Lý Do Bị Cấm | Cách Viết Chuẩn Xác Của NovaGroup (Ms. Hân) |
|---|---|---|
| *Triệt tiêu hoàn toàn nguy cơ điểm danh hộ* | Đao to búa lớn, phi thực tế | *Hạn chế tối đa tình trạng điểm danh hộ so với hình thức quét mã QR tĩnh* |
| *Xác thực siêu tốc* | Từ ngữ quảng cáo | *Thời gian phản hồi trên thiết bị POS < 2 giây/lượt chạm thẻ* |
| *Đột phá giải pháp / Tối ưu vượt trội* | Sáo rỗng, khẩu hiệu | *Hệ thống hóa và quản lý tập trung dữ liệu điểm danh và thời lượng đào tạo* |
| *Chuẩn xác 100% / Tuyệt đối* | Cam kết phi kỹ thuật | *Thời gian ghi nhận chuẩn xác theo đồng hồ máy chủ Server Clock* |
| *Căn cứ pháp lý duy nhất* | Dùng sai bối cảnh kỹ thuật | *Căn cứ đối chiếu thời gian hợp lệ của buổi học* |
| *Bộ máy tính toán Duration Engine cài đặt 10 quy tắc* | Hàn lâm, phức tạp hóa | *Quy tắc tính thời gian học thực tế: $\Delta t = \sum(RA - VÀO)$ sau khi trừ thời gian ra ngoài và cắt theo khung giờ lớp học* |
| *Thuật toán khử trùng lặp (De-bounce)* | Biệt ngữ sính chữ tiếng Anh | *Hai lần quẹt thẻ liên tiếp cách nhau dưới 5 giây: hệ thống chỉ ghi nhận 1 lượt quẹt đầu tiên* |
| *Sự kiện số lượt quẹt thẻ bị lẻ (ODD_SWIPE)* | Dịch gượng gạo | *Học viên có số lượt quẹt bị lẻ (quên quẹt ra khi tan học)* |
| *Strict Soft-delete 100%* | Thuật ngữ code | *Lưu lịch sử xóa dữ liệu, không xóa vật lý khỏi hệ thống (lưu trường deleted_at)* |
| *Kính thưa Ban Lãnh đạo / Trân trọng đề xuất* | Chatbot ngoại giao | Viết thẳng vào tiêu đề: *1. Thông tin chung*, *2. Quy trình nghiệp vụ*, *3. Giải pháp hệ thống* |

---

## 3. Cấu Trúc Tài Liệu Thiết Kế Giải Pháp Chuẩn (SDD Standard Structure)
Mọi tài liệu SDD tại NVG-ITC phải tuân thủ cấu trúc 3 chương kinh điển:

```
TÊN TÀI LIỆU: TÀI LIỆU THIẾT KẾ GIẢI PHÁP - [TÊN HỆ THỐNG]
1. BẢNG GHI NHẬN THAY ĐỔI TÀI LIỆU (Ngày, Tác giả, Mô tả, Phiên bản, Tính năng)
2. MỤC LỤC TỔNG QUAN (Chi tiết đến mục 3.x.x)
3. TRANG KÝ (2 bên: Phụ trách CNTT | Phụ trách nghiệp vụ)
4. CHƯƠNG 1: THÔNG TIN CHUNG
   1.1. Phạm vi tài liệu (1 dòng)
   1.2. Mục đích tài liệu (3 gạch đầu dòng)
   1.3. Khái niệm, thuật ngữ (Bảng 2 cột)
   1.4. Tài liệu tham khảo (Bảng 3 cột)
5. CHƯƠNG 2: QUY TRÌNH NGHIỆP VỤ
   2.1. Đối tượng áp dụng (Danh sách phòng ban/khối)
   2.2. Yêu cầu chung về hệ thống (Gạch đầu dòng + Sơ đồ phân hệ tổng quan)
   2.3. Quy trình vận hành (Sơ đồ Swimlane phân làn + Bảng mô tả quy trình)
6. CHƯƠNG 3: GIẢI PHÁP HỆ THỐNG (Từng phân hệ chi tiết)
   3.x.1. Yêu cầu chức năng (Bảng: STT | Chức năng | Mô tả)
   3.x.2. Quy trình chi tiết & Sơ đồ trạng thái Lifecycle (Khởi tạo -> Chờ thực hiện -> Hoàn thành)
   3.x.3. Mô tả giao diện (Hình ảnh Mockup + Bảng đặc tả UI Fields 5 cột)
   3.x.4. Quản trị danh mục & Quy tắc Import Excel
   3.x.5. Ma trận Notification (Bảng đối tượng nhận + Mẫu email/tin nhắn)
   3.x.6. Yêu cầu phi chức năng (NFR)
```

---

## 4. Chuẩn Bảng Đặc Tả UI Fields 5 Cột (UI Field Specifications)
Mỗi màn hình bắt buộc phải có bảng quy tắc chi tiết theo chuẩn Ms. Hân:

| Cột | Ý Nghĩa | Quy Cách Trình Bày |
|:---:|---|---|
| **TT** | Số thứ tự trường | Số nguyên tăng dần (1, 2, 3...) |
| **Tên trường thông tin** | Tên nhãn (Label) hiển thị trên màn hình | Ghi rõ tên nhãn hoặc tên Button: `Mã kế hoạch`, `Loại thanh tra`, `Button [Lưu]`, `Button [Hủy]` |
| **Loại** | Kiểu điều khiển UI (UI Control Type) | Chỉ dùng các loại chuẩn: `Dropdownlist`, `Only view`, `Textbox`, `TextArea`, `Checkbox`, `Button`, `dd/mm/yyyy hh:mm`, `Image, pdf, word, excel` |
| **Business rule** | Quy tắc nghiệp vụ cụ thể | Ghi rõ logic xử lý: quy tắc sinh mã tự động, điều kiện ngày tháng, nguồn load dữ liệu từ Orgchart/bảng HRM, sự kiện bấm nút cập nhật trạng thái nào |
| **Bắt buộc** | Thuộc tính bắt buộc nhập | Đánh dấu `x` nếu bắt buộc; để trống nếu không bắt buộc |

---

## 5. Chuẩn Ma Trận Thông Báo (Notification Matrix Standard)
Theo chuẩn Ms. Hân (NVL_ITD_SDD trang 47-65), mọi sự kiện hệ thống phải lập ma trận thông báo rõ ràng kèm mẫu nội dung cụ thể:

| Cột | Quy Cách Trình Bày |
|---|---|
| **STT** | Số thứ tự tăng dần |
| **Sự kiện kích hoạt** | Hành động nghiệp vụ sinh ra thông báo (vd: Nộp đơn, Phê duyệt, Nhắc quẹt thẻ) |
| **Kênh gửi** | `MS Teams Adaptive Card`, `Email`, `Push Notification OneNova`, `Loa / Màn hình POS` |
| **Người nhận** | Đối tượng nhận thông báo (QLTT, Học viên, Thư ký, Giảng viên) |
| **Thời điểm gửi** | Thời gian kích hoạt (Tức thì, trước giờ học 15p, 17:00 ngày kết thúc) |
| **Mẫu nội dung thông báo** | Văn bản mẫu có placeholder cụ thể (vd: `[Họ tên]`, `[Tên lớp]`, `[Lý do]`) |

---

## 6. Quy Chuẩn Phông Chữ Times New Roman & Font Size 12pt
- **Phông chữ duy nhất:** Bắt buộc sử dụng phông chữ **`Times New Roman`** (`font-family: 'Times New Roman', Times, serif;`) cho 100% tài liệu xuất bản và deliverable HTML/Word.
- **Cỡ chữ chuẩn:**
  - **Body text (Thân văn bản):** **`12pt`** (line-height: 1.5, màu chữ `#000000`).
  - **Bảng biểu (`table`, `th`, `td`):** **`11pt`** (line-height: 1.45) để chống tràn lề A4.
  - **Tiêu đề H1:** **`18pt`** Bold.
  - **Tiêu đề H2:** **`13.5pt - 14pt`** Bold.
  - **Tiêu đề H3:** **`12.5pt - 13pt`** Bold.
  - **Tiêu đề H4:** **`12pt`** Bold / Italic.
  - **Khung hộp (Boxes):** **`12pt`**.
- Không sử dụng font không chân (sans-serif) hoặc kích thước nhỏ dạng `13px` / `14px` làm phá vỡ chuẩn 12pt của tập đoàn.

---

## 7. Quy Chuẩn Soạn Thảo Email Doanh Nghiệp (Corporate Email Standards)
Chi tiết tại: [`.agents/rules/corporate_email_standards.md`](file:///d:/repo/ba-zone/.agents/rules/corporate_email_standards.md)
- **Phong thái:** Bình đẳng, gãy gọn, đi thẳng vào vấn đề (Direct & Concise, 3–5 câu).
- **Mở đầu:** `Dear anh/chị [Tên] và Anh/Chị,` hoặc `Kính gửi anh/chị [Tên]...`.
- **Cấm phong thái khúm núm:** Tuyệt đối không dùng "Dạ", "Thưa", "Dạ em chào", "Dạ vâng" và không kết câu bằng các từ đệm cảm thán (`...ạ`, `...nha`, `...nhé`).
- **Danh xưng tập thể & Kết thư:** Luôn dùng danh xưng đại diện là **`ITC`** (không dùng *Team BA* / *Nhóm BA*); kết thư: `Trân trọng,` + Họ tên + `ITC`.

