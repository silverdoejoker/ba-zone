# BÁO CÁO WALKTHROUGH UAT & SO SÁNH HIỆN TRẠNG PHÂN HỆ CHO THUÊ (LEASING)
**Dự án:** NovaGMS - Phân hệ Cho thuê & Đi thuê (Rent & Rent / Commercial Leasing)  
**Môi trường khảo sát:** UAT (`https://uat-gms.novagroup.vn/App/NovaGMS?appModule=DV`)  
**Tài khoản khảo sát:** `Trần Quang Anh Minh` (`itc.cvcc.55@novagroup.vn`)  
**Thời gian thực hiện:** 17/09/2026  
**Mục tiêu:** Khảo sát As-Is thực tế trên UAT, đối chiếu với URD ban đầu và Yêu cầu thay đổi (CR) từ NLE để chuẩn bị nội dung làm việc đầu tuần sau.

---

## 🎥 BẢN GHI HÌNH WALKTHROUGH TRỰC QUAN (SESSION RECORDING)

Toàn bộ phiên thao tác tự động trên môi trường UAT đã được hệ thống ghi lại trực tiếp:
- **Video Recording (WebP):** [leasing_walkthrough_1789620142368.webp](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/leasing_walkthrough_1789620142368.webp)

```
[Xem bản ghi hình hoạt động trình duyệt tại đường dẫn artifact trên]
```

---

## 📸 HÌNH ẢNH THỰC TẾ TRÊN UAT (LIVE SCREENSHOTS)

| Màn hình | Hình ảnh minh chứng | Mô tả chi tiết |
|---|---|---|
| **1. Dashboard Portal Tổng** | ![Dashboard Main](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/novagms_dashboard_main_1789620287465.png) | Hiển thị 10 phân hệ nghiệp vụ, bao gồm module **ĐT RENT & RENT** (Cho thuê & Đi thuê). |
| **2. Dashboard Phân hệ Cho thuê** | ![Leasing Dashboard](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/novagms_leasing_module_1789620317657.png) | Thẻ KPI Đi thuê/Cho thuê, Tổng số 7 mặt bằng, Biểu đồ Doanh thu 2026, Công nợ theo kỳ. |
| **3. Quản lý Hợp đồng Cho thuê** | ![Rental Contract](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/novagms_rental_contract_1789620413973.png) | Master Grid 19 hợp đồng, 11 khách hàng, 6 tab chi tiết: Management, Electricity, Water, Others, Deposit, Documents. |
| **4. Danh sách Mặt bằng** | ![Layout List](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/novagms_leasing_layout_1789620523483.png) | Lưới dữ liệu chi tiết từng lô/căn: Mã mặt bằng, Địa chỉ, Khu vực, Loại hình, Diện tích m², Trạng thái. |
| **5. Sơ đồ Mặt bằng Trực quan** | ![Layout Plan](file:///C:/Users/itc.cg.55/.gemini/antigravity-ide/brain/031ef671-4ae7-4009-86cf-f71ca640c243/novagms_leasing_layout_plan_1789620554123.png) | Dạng Card Grid trực quan theo màu: Đỏ (Chưa bán/cho thuê), Xanh dương (Đang bán/cho thuê), Tag Internal/Outside. |

---

## 🏛️ HIỆN TRẠNG KIẾN TRÚC HỆ THỐNG TRÊN UAT (AS-IS ARCHITECTURE)

### 1. Phân cấp Đơn vị Vận hành (Multi-Tenant Header)
Header hỗ trợ chọn cây đơn vị trực thuộc tập đoàn:
* `NOVAGROUP` ➔ `NOVA SERVICE GROUP` ➔ `NOVA LEASING (NLE)`, `CITIGYM (CTG)`, `NOVA RETAIL MANAGEMENT (NRM)`, `NOVA HOTEL & RESORT WORLD (NHW)`...
* `NOVALAND GROUP` & `CỤM DỰ ÁN (GMD-NVLG)`.

### 2. Cấu trúc Menu Chức năng (10 Nhóm Menu Trái)
1. **Dashboard (`#trang-chu`):** KPI Đi thuê/Cho thuê, Tỷ lệ lấp đầy, Công việc, Doanh thu 2026, Công nợ theo kỳ.
2. **Quản lý công việc:** `Request management` (Yêu cầu khách thuê), `Job` (Công việc vận hành), `My shifts` (Ca trực).
3. **Facilities (Quản lý mặt bằng):**
   * `Layout`: Sơ đồ & danh sách mặt bằng.
   * `Facilities`: Danh mục trang thiết bị, tài sản kèm mặt bằng.
   * `File`: Hồ sơ bản vẽ, tài liệu kỹ thuật.
   * `Inspection`: Nghiệm thu, kiểm tra hiện trạng.
   * `Plan`: Kế hoạch bảo trì.
4. **Customer service (Dịch vụ & Hợp đồng):**
   * `Information lookup`: Tra cứu thông tin.
   * `Rental contract`: Hợp đồng cho thuê (6 tab chi tiết).
5. **Payment book (Sổ thanh toán):** `Transaction` (Giao dịch thu), `Invoice` (Hóa đơn).
6. **Lease debt (Công nợ):** Quản lý nợ đọng, theo dõi kỳ thanh toán.
7. **Media (Truyền thông):** `Care notification` (Thông báo chăm sóc), `Article` (Tin tức).
8. **Plan (Phân công ca):** `Shift assignment`, `Kế hoạch hàng ngày`, `Kế hoạch định kỳ`.
9. **Report:** Hệ thống báo cáo thống kê.
10. **Category management (Danh mục):** `Human Resources`, `Urban area` (Khu đô thị), `Area` (Phân khu).

---

## ⚖️ BẢNG SO SÁNH 3 BÊN: URD BAN ĐẦU vs. UAT HIỆN TẠI vs. ĐỀ XUẤT MỚI TỪ NLE

| Nhóm Nghiệp Vụ | 1. URD Thiết Kế Ban Đầu (`0032/NVG/2026`) | 2. Thực Tế Triển Khai Trên UAT (As-Is Live) | 3. Yêu Cầu Mới NLE Đề Xuất (Change Request) | Đánh Giá Khoảng Trống (Gap Analysis) |
|---|---|---|---|---|
| **1. Cấu trúc Không gian & Dự án** | Quản lý Phân khu, Tòa nhà, Lô mặt bằng độc lập. | Đã có danh mục `Urban area`, `Area` và quản lý Mặt bằng theo căn/lô (`Layout`). | Quản lý danh mục Dự án cấp cao; phân rã diện tích GFA, NLA thương mại; tỷ lệ lấp đầy theo phân kỳ. | **GAP LỚN:** UAT hiện tại chỉ quản lý căn đơn lẻ, chưa có cấu trúc phân bổ tổng thể diện tích GFA/NLA toàn dự án. |
| **2. Báo cáo & Định giá Tài sản** | Chưa có mô hình tài chính chuyên sâu, chỉ có giá thuê cơ bản. | Dashboard hiển thị Doanh thu 2026 theo kỳ và Công nợ tháng. | Thẩm định tài chính tài sản, tính toán dòng tiền, tỷ suất hoàn vốn ROI, ROE cho từng dự án/mặt bằng. | **GAP MỚI 100%:** NLE muốn bổ sung module Asset Valuation & Financial Modeling chưa từng có trong URD. |
| **3. Phễu Bán hàng & Chăm sóc (CRM)** | Quy trình Tiếp nhận nhu cầu chào thuê ➔ Báo giá sơ bộ. | Chưa có phễu CRM; menu hiện tại chỉ có `Rental contract` (ký hợp đồng) và `Deposit contract`. | Xây dựng Leasing CRM Pipeline: Lead ➔ Cơ hội ➔ Booking giữ chỗ ➔ Thẩm định khách ➔ Ký HĐ. | **GAP LỚN:** Thiếu toàn bộ giai đoạn tiền hợp đồng (Pre-leasing Lead/Opportunity & Booking). |
| **4. Hợp đồng & Dịch vụ Tiện ích** | Hợp đồng cho thuê, theo dõi chỉ số Điện, Nước, Phí dịch vụ. | **ĐÃ HOÀN THIỆN RẤT TỐT:** Master Grid 19 HĐ, 6 sub-tabs (`Management`, `Electricity`, `Water`, `Others`, `Deposit`, `Documents`). | Bổ sung phụ lục giảm trừ tiền thuê, tính giá thuê theo % doanh thu (Revenue Share), trượt giá lũy tiến. | **GAP TÍNH NĂNG:** Cần mở rộng công thức tính giá thuê linh hoạt (% Doanh thu) thay vì chỉ giá cố định. |
| **5. Bàn giao & Thi công (Fit-out)** | Quy trình Bàn giao mặt bằng & Kiểm kê tài sản hiện trạng. | Đã có menu `Inspection` (Kiểm tra) và `Facilities` (Trang thiết bị kèm theo). | Quản lý quy trình Fit-out chi tiết: Nộp hồ sơ thiết kế, phê duyệt PCCC, đặt cọc thi công, phạt trễ tiến độ. | **GAP NGHIỆP VỤ:** UAT mới có biên bản kiểm tra chung, chưa có workflow quản lý hồ sơ Fit-out chuẩn của TTTM. |
| **6. Khách hàng & Đánh giá Tín nhiệm** | Quản lý thông tin hồ sơ pháp lý đối tác/khách hàng. | Quản lý danh sách khách thuê cơ bản gắn liền với hợp đồng. | Tenant Scoring & Rating: Xếp hạng uy tín khách thuê, cảnh báo rủi ro bùng cọc/nợ xấu. | **GAP MỚI:** Cần làm rõ bộ tiêu chí chấm điểm tín nhiệm (tự động hay thủ công). |
| **7. Quản lý Vận hành & Công việc** | Đã có mô tả phân công ca trực và xử lý sự cố. | **ĐÃ HOÀN THIỆN ĐẦY ĐỦ:** Menu `Quản lý công việc` (`Request`, `Job`, `My shifts`) và `Plan` (Ca trực hàng ngày). | Yêu cầu Sales KPI: Theo dõi chỉ số bán hàng của nhân viên môi giới/cho thuê. | **LỆCH PHẠM VI:** UAT hiện tập trung cho đội ngũ Vận hành (Operation/Facility), NLE lại muốn KPI cho đội Kinh doanh (Leasing Sales). |

---

## 🎯 DANH SÁCH 5 ĐIỂM CỐT LÕI CẦN LÀM RÕ VỚI NLE ĐẦU TUẦN SAU

Dựa trên kết quả khảo sát thực tế trên UAT, đây là 5 vấn đề chiến lược nhất bạn cần đưa ra thảo luận với chị Lê Phương Thúy (NLE) và anh Trịnh Phan Đăng Khoa (NAM):

1. **Về Cấu trúc Không gian (GFA / NLA):**
   * *Hiện trạng:* UAT đã có quản lý mặt bằng dạng danh sách và thẻ trực quan theo từng căn/lô (ShopHouse, Biệt thự, Lô thương mại).
   * *Câu hỏi:* NLE muốn bổ sung quản lý GFA/NLA ở cấp độ nào? Chỉ theo dõi số liệu tổng quan trên Dashboard hay muốn phân bổ chỉ tiêu diện tích xuống từng tầng/tòa nhà?
2. **Về Phễu CRM Bán hàng (Pre-leasing Pipeline):**
   * *Hiện trạng:* UAT đang đi thẳng từ Khách hàng ➔ Hợp đồng đặt cọc / Hợp đồng thuê.
   * *Câu hỏi:* NLE đã có hệ thống CRM nào khác (như Salesforce / HubSpot) để quản lý Lead/Cơ hội chưa? Hay muốn NovaGMS xây dựng hẳn một module Mini-CRM riêng?
3. **Về Mô hình Tính Giá Thuê (% Doanh thu - Turnover Rent):**
   * *Hiện trạng:* UAT đang tính tiền thuê theo đơn giá cố định và biểu phí điện nước/dịch vụ phụ trợ.
   * *Câu hỏi:* Với mô hình thuê theo % doanh thu, dữ liệu doanh thu của khách thuê sẽ được nhập thủ công hàng tháng hay tích hợp với máy POS của gian hàng?
4. **Về Quản lý Fit-out / Thi công:**
   * *Hiện trạng:* UAT đã có phân hệ `Facilities > Inspection` để kiểm tra hiện trạng.
   * *Câu hỏi:* NLE muốn nâng cấp `Inspection` này thành quy trình duyệt hồ sơ thiết kế thi công hay muốn một phân hệ Fit-out độc lập?
5. **Về Định giá Tài sản & Chỉ số Tài chính (ROI/ROE):**
   * *Hiện trạng:* NovaGMS hiện là hệ thống quản lý vận hành (Property Management), không phải phần mềm phân tích tài chính đầu tư.
   * *Câu hỏi:* Nguồn dữ liệu vốn đầu tư ban đầu để tính ROI/ROE sẽ lấy từ đâu (nhập tay hay đồng bộ từ SAP/kế toán)?
