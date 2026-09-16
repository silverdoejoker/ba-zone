---
name: web-app-uat
description: |
  Hướng dẫn chuyên sâu và quy trình tự động/bán tự động kiểm thử, nghiệm thu (UAT) và trải nghiệm sản phẩm (Exploratory / Dogfooding QA) cho ứng dụng Web / Mobile Web khi có sẵn URL & Credentials (dựa trên thực tiễn chuẩn hóa tại TrọBill).
  Hỗ trợ xác thực kết nối, luồng đăng nhập đa vai trò (RBAC), kiểm tra DOM/Modal binding, Happy Path, Edge Cases, Negative Scenarios, Cross-device viewports, Console/Network error sniffing, phân lập ranh giới phần cứng (Camera OCR/IAP/Biometrics) và lập biên bản nghiệm thu UAT chuẩn mực.
author: Phúc NT @ BA Zone & Kiro Engineering
source: https://github.com/ba-zone
---

# Web Application UAT & Exploratory Testing Skill (TrọBill Methodology)
> by **Phúc NT** · BA Zone · Digital School · Kiro Engineering

Kỹ năng này cung cấp quy trình toàn diện, các nguyên tắc thực chiến và bộ công cụ tự động hóa để **kiểm thử chấp nhận người dùng (User Acceptance Testing - UAT)**, **trải nghiệm thực tế (Dogfooding / Exploratory Testing)** và **nghiệm thu chức năng** cho bất kỳ ứng dụng Web / Mobile Web nào khi đã được cung cấp **URL** và **Credentials** (tài khoản đăng nhập / vai trò).

Phương pháp luận được đúc kết từ quá trình phát triển và kiểm thử thực chiến của hệ thống **TrọBill (App Quản lý Nhà trọ & Thu tiền phòng)** — nơi đòi hỏi độ chính xác tuyệt đối về số liệu tài chính, bảo vệ token ngữ cảnh của AI và kiểm soát nghiêm ngặt các ranh giới thiết bị.

---

## 🎯 Giá Trị Cốt Lõi & Triết Lý Thực Chiến (TrọBill Principles)

Khi kiểm thử một ứng dụng web đang chạy thực tế, đặc biệt khi có sự hỗ trợ của AI Agent / Automation:

1. **Token-Preserving & Zero Retry Loops (Bảo toàn token AI)**:
   - Không thực hiện các vòng lặp thử đi thử lại (infinite retry loops) khi gặp lỗi giao diện hoặc dịch vụ ngoài.
   - Thất bại phải báo cáo ngay lập tức (*Fail-Fast*) với nguyên nhân rõ ràng (ví dụ: selector không tồn tại, HTTP 403, CORS block).

2. **3-Second Fail-Fast Guard for Headless Browser**:
   - Khi chạy headless browser (Edge/Chrome) kiểm tra DOM, luôn đặt timeout tối đa 3-5 giây. Nếu app bị kẹt tải hoặc loader xoay vô tận, ngắt tiến trình và ghi nhận lỗi `TIMEOUT` thay vì làm treo cả hệ thống.

3. **Hardware / Non-Automatable Boundary Isolation (Phân lập ranh giới phần cứng)**:
   - Các tính năng đòi hỏi phần cứng hoặc môi trường đặc thù:
     - **Camera OCR Scanner**: Cần luồng camera vật lý và xử lý ngưỡng nhị phân trực tiếp.
     - **Google Play IAP / Apple In-App Purchase**: Cần native billing client sheet và sandbox account.
     - **Native Storage Access Framework (SAF) / Biometrics**: Cần intent hệ điều hành và hộp thoại cấp quyền.
   - **Quy tắc bắt buộc**: Không cố gắng tự động hóa các tính năng này trong môi trường web tiêu chuẩn. Phải đưa vào **Manual Verification Registry** với hướng dẫn kiểm tra bằng tay rõ ràng.

4. **Bi-Directional Traceability (Truy xuất hai chiều BA ↔ Live App)**:
   - Mọi kịch bản kiểm thử (Test Case) phải liên kết trực tiếp với:
     - **Use Case Normal Course** hoặc **Alternative Course** (`UC-[MODULE]-[NN]`).
     - Hoặc **User Story Acceptance Criteria** (`AC1: Given-When-Then`).

---

## 🌐 Biến Phiên Làm Việc: `output_language`

| Giá trị | Ý nghĩa | Hành vi |
|---|---|---|
| `output_language=vi` | **Tiếng Việt** *(Khuyên dùng)* | Toàn bộ kế hoạch kiểm thử, bảng ca kiểm thử và biên bản nghiệm thu UAT được xuất bằng tiếng Việt chuyên ngành. |
| `output_language=en` | **Tiếng Anh** | Báo cáo UAT, Test Cases, Defect Log và Sign-off Sheet được xuất bằng tiếng Anh chuẩn quốc tế. |

---

## 🚀 Quy Trình Nghiệm Thu Chuẩn 8 Bước (8-Phase UAT Protocol)

```
[Phase 1: Pre-flight & Target Check]  ──> HTTP 200, SSL, Latency, Headless Boot
                 │
[Phase 2: Authentication & Session]   ──> Login credentials, Token/Cookie, Redirect
                 │
[Phase 3: Persona & RBAC Permissions] ──> Role isolation (Landlord vs Tenant vs Admin)
                 │
[Phase 4: Core Domain & Happy Path]   ──> End-to-end CRUD, Billing logic, Reports
                 │
[Phase 5: Edge Cases & Boundaries]    ──> Empty states, limits, special chars, debouncing
                 │
[Phase 6: Negative Testing & Fault]   ──> Invalid credentials, network drop, 4xx/5xx
                 │
[Phase 7: Responsive & Console Sniff] ──> Desktop, Tablet, Mobile & Zero console.error
                 │
[Phase 8: Hardware Registry & Sign-off]─> Manual item registry & Final GO/NO-GO
```

---

### Phase 1: Pre-flight & Target Connectivity (Kiểm tra Khởi động)
- **Mục tiêu**: Đảm bảo URL mục tiêu phản hồi hợp lệ trước khi thực hiện bất kỳ thao tác người dùng nào.
- **Tiêu chí kiểm tra**:
  - Mã trạng thái HTTP trả về: `200 OK` (hoặc redirect `302/301` đến trang đăng nhập).
  - Tốc độ tải ban đầu (Time To First Byte - TTFB) < 2.5 giây.
  - Kiểm tra chứng chỉ bảo mật HTTPS (nếu môi trường staging/production).
  - Kiểm tra tiêu đề trang (`<title>`), các thẻ meta viewport và biểu tượng favicon.
  - Headless Browser Boot: Khởi động Chromium/Edge headless dump DOM trong tối đa 3 giây để xác nhận render engine không bị crash.

---

### Phase 2: Authentication & Multi-Role Session (Xác thực & Phiên làm việc)
- **Mục tiêu**: Kiểm tra quy trình đăng nhập, duy trì phiên và thoát khỏi hệ thống với các bộ thông tin đăng nhập (credentials) được cung cấp.
- **Tiêu chí kiểm tra**:
  - Điền đúng tài khoản/mật khẩu -> Đăng nhập thành công và chuyển hướng tới Dashboard chính.
  - Kiểm tra tính lưu trữ phiên: Kiểm tra cookie `HttpOnly` hoặc `localStorage` / `sessionStorage` token.
  - Tải lại trang (F5 / Refresh): Phiên đăng nhập vẫn duy trì, không bị đá ra màn hình Login.
  - Đăng xuất (Logout): Xóa sạch token/phiên; bấm phím Back của trình duyệt không được xem lại dữ liệu nhạy cảm.
  - Session Expiry / 401 Unauthorized: Khi token hết hạn hoặc giả lập xóa token, ứng dụng tự động hiển thị thông báo và điều hướng về trang Login.

---

### Phase 3: Persona & RBAC Permissions (Phân quyền Vai trò)
- **Mục tiêu**: Đảm bảo tính toàn vẹn phân quyền dữ liệu theo vai trò người dùng (Multi-tenant & Role-Based Access Control).
- **Ví dụ trong bài toán Quản lý Nhà trọ (TrọBill)**:
  - **Chủ trọ (Landlord / Admin)**: Toàn quyền xem doanh thu tổng, chỉnh sửa giá điện nước, thêm bớt phòng, xóa dữ liệu, xuất file Excel/JSON.
  - **Khách thuê (Tenant / User)**: Chỉ được xem phòng của mình, hóa đơn tiền phòng cá nhân, lịch sử thanh toán và quét mã VietQR. Tuyệt đối **không** thấy doanh thu phòng khác hay menu cài đặt hệ thống.
  - **Khách vãng lai (Guest)**: Chỉ thấy trang giới thiệu (Landing Page) và màn hình đăng nhập/đăng ký.
- **Tiêu chí kiểm tra**:
  - Không chỉ ẩn phần tử trên UI (UI masking), mà các đường dẫn trực tiếp (URL deep linking) tới trang quản trị phải bị Route Guard chặn đứng.

---

### Phase 4: Core Domain & Happy Path Walkthrough (Luồng Nghiệp Vụ Chính)
- **Mục tiêu**: Kiểm thử thông suốt các chức năng cốt lõi tạo nên giá trị của phần mềm, đối soát 1:1 với Use Case Normal Course.
- **Kịch bản mẫu chuẩn TrọBill**:
  1. **Khởi tạo dữ liệu cơ bản**: Tạo một bất động sản/nhà trọ mới (Tên, địa chỉ, đơn giá điện, đơn giá nước theo người hoặc theo khối).
  2. **Quản lý phòng (Room CRUD)**: Thêm mới phòng trọ, điền thông tin khách thuê, số CCCD, tiền cọc.
  3. **Chốt số điện nước & Tính toán hóa đơn**:
     - Nhập chỉ số cũ và chỉ số mới.
     - Kiểm tra công thức: $\text{Tổng} = \text{Tiền phòng} + (\Delta \text{Điện} \times \text{Đơn giá}) + (\text{Nước}) + \text{Dịch vụ} + \text{Nợ cũ}$.
     - Xác nhận không có lỗi làm tròn số học, số lẻ thập phân hoặc sai dấu.
  4. **Thanh toán & Sinh mã VietQR**:
     - Bấm xem chi tiết hóa đơn -> Hiển thị mã VietQR động chứa chính xác số tài khoản, ngân hàng thụ hưởng, số tiền và nội dung chuyển khoản chuẩn cú pháp.
  5. **Chốt chu kỳ (Save Month / Rollover)**:
     - Lưu tháng thành công -> Chỉ số mới của tháng này tự động chuyển thành chỉ số cũ của tháng kế tiếp.
  6. **Sao lưu & Phục hồi (Data Export / Import)**:
     - Xuất dữ liệu ra file JSON/Excel -> Dữ liệu đầy đủ, mở được, không bị lỗi font Tiếng Việt UTF-8.

---

### Phase 5: Edge Cases & Data Boundary Limits (Kịch bản Biên & Dữ liệu Cực hạn)
- **Mục tiêu**: Đảm bảo ứng dụng không sập hoặc hiển thị giao diện vỡ vụn khi người dùng nhập dữ liệu biên.
- **Tiêu chí kiểm tra**:
  - **Dữ liệu rỗng (Zero / Empty States)**: Khi tài khoản mới toanh chưa có phòng nào, Dashboard phải hiển thị hình minh họa và nút hướng dẫn tạo phòng đầu tiên (Empty State Illustration), không được để trống trơn hay báo lỗi `TypeError: Cannot read properties of undefined`.
  - **Độ dài ký tự cực đại**: Tên phòng hoặc ghi chú dài 255 - 1000 ký tự -> Giao diện tự động xuống dòng (`word-break: break-word;`), không bị tràn khung hay đè lên các nút bấm.
  - **Số học biên**:
    - Số điện tháng này nhỏ hơn tháng trước (chỉ số đồng hồ quay vòng hoặc nhập nhầm) -> Phải hiển thị cảnh báo đỏ ngay lập tức.
    - Tiền phòng = 0 VNĐ hoặc tiền phòng cực lớn (ví dụ: 100.000.000.000 VNĐ) -> Định dạng tiền tệ phân tách hàng nghìn bằng dấu chấm/phẩy chính xác (`100,000,000 đ`).
  - **Ký tự đặc biệt & XSS Injection**: Nhập `<script>alert(1)</script>` hoặc emoji `🎉✨` vào tên khách thuê -> Ứng dụng encode an toàn, không thực thi mã độc.
  - **Thao tác nhanh (Debounce / Double Click)**: Nhấp đôi (double click) thật nhanh vào nút "Lưu hóa đơn" -> Hệ thống vô hiệu hóa nút (disable) ngay sau cú nhấp đầu tiên, không tạo ra 2 hóa đơn trùng lặp.

---

### Phase 6: Negative Testing & Fault Tolerance (Kịch bản Ngoại lệ & Khả năng Chịu lỗi)
- **Mục tiêu**: Kiểm tra cách ứng dụng ứng phó khi gặp sự cố, dữ liệu sai hoặc đường truyền gián đoạn.
- **Tiêu chí kiểm tra**:
  - **Sai thông tin xác thực**: Nhập sai mật khẩu -> Thông báo lỗi thân thiện: *"Tên đăng nhập hoặc mật khẩu không chính xác"*, không để lộ chi tiết kỹ thuật hệ thống (ví dụ: `SQLSTATE[HY000]`).
  - **Mất kết nối mạng đột ngột (Offline Mode / Network Drop)**: Ngắt kết nối mạng khi đang thực hiện thao tác -> Hiển thị thông báo mất mạng dạng Toast hoặc Banner màu vàng/cam; dữ liệu đã gõ trên form không bị mất sạch.
  - **Mã lỗi HTTP 404 / 500**: Truy cập một đường dẫn không tồn tại -> Hiển thị trang 404 tùy biến có nút *"Quay về Trang chủ"*, không dùng trang lỗi mặc định của web server (Nginx/Apache).

---

### Phase 7: Responsive UI & Console Health (Giao Diện Đa Thiết Bị & Sức Khỏe Console)
- **Mục tiêu**: Đảm bảo hiển thị hoàn hảo trên mọi kích thước màn hình và không có lỗi ngầm trong Javascript.
- **3 Breakpoint Viewport chuẩn**:
  1. **Desktop**: `1920 x 1080` (hoặc `1440 x 900`).
  2. **Tablet**: `768 x 1024` (iPad / Android Tablet dọc và ngang).
  3. **Mobile Phone**: `375 x 667` (iPhone SE) hoặc `390 x 844` (iPhone 14/15/16).
- **Tiêu chí kiểm tra giao diện**:
  - Không xuất hiện thanh cuộn ngang (Horizontal Scrollbar) ngoài ý muốn trên màn hình điện thoại di động.
  - Menu chuyển đổi mượt mà giữa Sidebar mở rộng (Desktop) sang Bottom Navigation Bar hoặc Hamburger Drawer (Mobile).
  - Tương phản màu sắc (Color Contrast) ở cả **Giao diện Sáng (Light Mode)** và **Giao diện Tối (Dark Mode)**, các nút bấm phụ không bị mờ nhạt chìm vào nền.
- **Tiêu chí Console Health**:
  - Mở Developer Tools (F12) -> Console: **Phải sạch sẽ, không có bất kỳ dòng chữ đỏ nào thuộc nhóm `Uncaught TypeError`, `Unhandled Promise Rejection` hay `404 Not Found (Missing Assets/Fonts)`**.

---

### Phase 8: Non-Automatable Registry & Final Acceptance Sign-off (Nghiệm Thu Bàn Giao)
- **Mục tiêu**: Tổng hợp kết quả, cô lập các tính năng phần cứng và đưa ra quyết định bàn giao chính thức.
- **Bảng Danh mục Phân lập Phần cứng (Hardware Isolation Registry)**:
  - Ghi nhận rõ: Tên tính năng, lý do không thể tự động hóa, quy trình kiểm tra bằng tay từng bước (Step-by-step manual check) để tester người thật thực hiện trong 2 phút.
- **Tiêu chuẩn Ra Quyết Định Nghiệm Thu (Acceptance Decision Matrix)**:
  - **GO (Đạt chuẩn phát hành)**:
    - 100% Test Case mức độ Critical & Major vượt qua (`PASS`).
    - Tỷ lệ tổng thể Pass Rate >= 95%.
    - 0 lỗi bảo mật nghiêm trọng hoặc rò rỉ dữ liệu.
    - Console hoàn toàn sạch lỗi runtime.
  - **CONDITIONAL GO (Phát hành có điều kiện)**:
    - 100% Critical Pass. Một số lỗi Minor về thẩm mỹ UI hoặc câu từ i18n chưa ảnh hưởng đến dòng tiền/dữ liệu. Đã có kế hoạch khắc phục (Hotfix plan).
  - **NO-GO (Không đạt - Chặn phát hành)**:
    - Xuất hiện bất kỳ lỗi làm sai lệch số tiền, mất mát dữ liệu, sập ứng dụng (White Screen of Death) hoặc không thể đăng nhập.

---

## 🛠️ Bộ Công Cụ & Script Tự Động Hóa (`scripts/audit_uat.py`)

Kỹ năng đi kèm với script tự động `scripts/audit_uat.py` có hai chế độ hoạt động:

### 1. Chế độ Thăm Dò & Smoke Test Live App (`--url`)
Dùng khi bạn có một URL ứng dụng (ví dụ: môi trường dev/staging hoặc live app):
```powershell
python scripts/audit_uat.py --url http://localhost:8767/app/trobill/uat.html --username "admin" --password "123456"
```
Script sẽ tự động:
- Kiểm tra HTTP response status và latency.
- Bóc tách cấu trúc DOM, tiêu đề, meta viewport.
- Quét các form và input xác thực (`type="password"`, `type="email"`, `button[type="submit"]`).
- Kích hoạt Headless Edge/Chrome với bộ bảo vệ 3 giây (Fail-Fast) để kiểm tra trạng thái khởi động thực tế.
- Tự động kết xuất khung báo cáo UAT nghiệm thu nếu có tham số `--export-report <path>`.

### 2. Chế độ Kiểm Định Báo Cáo Nghiệm Thu (`--file`)
Dùng trong quy trình kiểm soát chất lượng CI/CD hoặc chạy trong `audit-all.ps1`:
```powershell
python scripts/audit_uat.py --file web-app-uat-skill/samples/sample_uat_report_vi.md
```
Script sẽ kiểm tra:
- Đầy đủ 8 phần cấu trúc bắt buộc của biên bản nghiệm thu UAT.
- Định dạng mã Test Case chuẩn `TC-[MODULE]-[NN]`.
- Đảm bảo độ phủ đủ cả 3 nhóm kịch bản: Happy Path, Edge Case, Negative Path.
- Kiểm tra phân loại lỗi theo mức độ nghiêm trọng (Severity: Critical, Major, Minor, Trivial).
- Kiểm tra chứng thực hiển thị đa màn hình (Desktop, Tablet, Mobile) và Console Health.
- Xác thực có danh mục phân lập ranh giới phần cứng và chữ ký nghiệm thu cuối cùng (GO / NO-GO).

---

## 📋 Mẫu Lời Kích Hoạt Kỹ Năng (Prompt Triggers)

- *"Mình có app TrọBill đang chạy ở http://localhost:8767/app/trobill/uat.html với tài khoản admin/123456, hãy thực hiện quy trình UAT và viết biên bản nghiệm thu đầy đủ cho mình."*
- *"Hãy lập kế hoạch và kịch bản kiểm thử UAT cho tính năng chốt tiền phòng và xuất hóa đơn VietQR."*
- *"Audit báo cáo nghiệm thu UAT này xem đã đạt chuẩn TrọBill và BA Zone chưa: `uat-report.md`"*
- *"Thực hiện exploratory testing trên trang đăng ký/đăng nhập của app và liệt kê các edge case cần lưu ý."*
