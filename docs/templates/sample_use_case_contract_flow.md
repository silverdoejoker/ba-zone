# Use Cases: Luồng tạo Contract (MSA → SOW → PO → Billable Rate)
> Tài liệu mẫu thực tế của **BA Zone** · Đặc tả Use Case chuẩn 16 trường (Karl Wiegers / IIBA Standard)  
> Bối cảnh hệ thống: Enterprise Contract Management & Billing System (CMS)  
> Chuẩn hóa theo: `enterprise-nda-sanitizer` (Generalize by Default)

> Tài liệu mô tả chi tiết các Use Case trong luồng tạo hợp đồng từ MSA → SOW → PO → Billable Rate trên hệ thống CMS.  
> Dựa trên SRS: TechPartner_Contract_System-Requirement-Specification_v3.0.1

---

## UC-CONTRACT-01: Tạo MSA (Master Service Agreement)

| **Mã Use Case:** | UC-CONTRACT-01 |
| ---: | :--- |
| **Tên Use Case:** | Tạo MSA |

| **Người tạo:** | Lead BA | **Người cập nhật cuối:** | AI Assistant |
| ---: | :--- | ---: | :--- |
| **Ngày tạo:** | 2025-05-17 | **Ngày cập nhật cuối:** | 2025-05-17 |

| **Tác nhân:** | **Chính:** SSC Member, SSC Team Lead. **Phụ:** Hệ thống CMS. |
| ---: | :--- |
| **Mô tả:** | Use case cho phép người dùng tạo mới một MSA (Master Service Agreement) — hợp đồng khung cấp cao nhất trong chuỗi contract. MSA là điều kiện tiên quyết để tạo SOW, PO và Billable Rate. |
| **Điều kiện tiên quyết:** | 1. Người dùng đã đăng nhập thành công với vai trò SSC Member hoặc SSC Team Lead.<br>2. Người dùng đang ở màn hình Default Contract list hoặc MSA list. |
| **Điều kiện hậu quyết:** | 1. MSA được tạo thành công với trạng thái "Draft" hoặc "Waiting for Sign off".<br>2. Hệ thống lưu lịch sử tạo MSA vào bảng History.<br>3. MSA hiển thị trong danh sách MSA. |
| **Độ ưu tiên:** | Cao - MSA là contract gốc, bắt buộc phải có trước khi tạo SOW/PO/BR. |
| **Tần suất sử dụng:** | Trung bình, khi có hợp đồng khung mới với khách hàng. |
| **Luồng chính:** | 1. Người dùng chọn "Create MSA" từ Default Contract list hoặc MSA list.<br>2. Hệ thống hiển thị màn hình Create MSA với các trường thông tin (BR 23).<br>3. Người dùng nhập thông tin MSA bao gồm: OB, Account Code, AM, Account Sales Supporter, Legal Company, Total MSA Value (LC), MSA Currency, MSA Name, MSA Official Code, MSA Sign With, MSA Legal Company, MSA Payment Terms, MSA Sales Supporter, MSA Signed Date, MSA Start Date, MSA End Date, MSA Description.<br>4. Người dùng nhấn "Save".<br>5. Hệ thống validate dữ liệu (BR 24).<br>6. Hệ thống kiểm tra các trường bắt buộc và lưu MSA (BR 25, BR 26).<br>7. Hệ thống hiển thị thông báo tạo thành công và chuyển sang màn hình MSA Detail. |
| **Luồng thay thế:** | **UC-CONTRACT-01.LTT.1: Lưu dạng Draft**<br>Tại bước 6, nếu các trường bắt buộc cho "Waiting for Sign off" chưa đầy đủ nhưng đã có tối thiểu: OB, Account Code, AM, Account Sales Supporter, MSA Name:<br>6a. Hệ thống lưu MSA với trạng thái "Draft".<br>6b. Hệ thống hiển thị thông báo lưu Draft thành công.<br>→ Tiếp tục từ bước 7 của Luồng chính.<br><br>**UC-CONTRACT-01.LTT.2: Tạo MSA từ Related tab của MSA khác**<br>Tại bước 1, người dùng chọn "Create" từ tab Related trong MSA Detail:<br>1a. Hệ thống mở màn hình Create MSA trong tab mới.<br>1b. Hệ thống tự động điền thông tin từ MSA hiện tại.<br>→ Tiếp tục từ bước 3 của Luồng chính. |
| **Ngoại lệ:** | **UC-CONTRACT-01.NL.1: Validate thất bại**<br>Điều kiện kích hoạt: Dữ liệu không hợp lệ (không mapping với master data, sai template).<br>Phản hồi: Hệ thống hiển thị thông báo lỗi MSG 1 cho các trường không hợp lệ.<br>Trạng thái cuối: Người dùng quay lại màn hình Create MSA để sửa dữ liệu.<br><br>**UC-CONTRACT-01.NL.2: Thiếu trường bắt buộc tối thiểu**<br>Điều kiện kích hoạt: Các trường bắt buộc tối thiểu (OB, Account Code, AM, Account Sales Supporter, MSA Name) chưa được điền.<br>Phản hồi: Hệ thống hiển thị MSG 1 yêu cầu điền đủ thông tin.<br>Trạng thái cuối: MSA không được lưu, người dùng ở lại màn hình Create. |
| **Bao gồm:** | UC-CONTRACT-01.SUB.1: Add Attachment file (UC 9) — có thể gọi tại bước 3. |
| **Yêu cầu đặc biệt:** | **Hiệu năng**: Màn hình Create MSA load trong < 3s.<br>**Bảo mật**: SSC Member chỉ xem/sửa MSA do mình tạo; Team Lead xem/sửa MSA của nhân viên mình.<br>**Độ tin cậy**: Mọi thay đổi phải được lưu vào bảng History. |
| **Giả định:** | 1. Master data (Account Code, OB, AM, Legal Company, Payment Terms, Currency, Sales Supporter, Signed With) đã được cấu hình sẵn trong hệ thống.<br>2. Người dùng có quyền tạo MSA theo Permission Matrix. |
| **Ghi chú và vấn đề mở:** | [NOTE-1] Trường bắt buộc cho Draft: OB, Account Code, AM, Account Sales Supporter, MSA Name.<br>[NOTE-2] Trường bắt buộc cho Waiting for Sign off: tất cả trường có dấu * trong SRS (15 trường).<br>[NOTE-3] Khi nội dung dài thì hiển thị "..." chứ không xuống dòng (CBR). |

---

## UC-CONTRACT-02: Tạo SOW (Statement of Work)

| **Mã Use Case:** | UC-CONTRACT-02 |
| ---: | :--- |
| **Tên Use Case:** | Tạo SOW |

| **Người tạo:** | Lead BA | **Người cập nhật cuối:** | AI Assistant |
| ---: | :--- | ---: | :--- |
| **Ngày tạo:** | 2025-05-17 | **Ngày cập nhật cuối:** | 2025-05-17 |

| **Tác nhân:** | **Chính:** SSC Member, SSC Team Lead. **Phụ:** Hệ thống CMS. |
| ---: | :--- |
| **Mô tả:** | Use case cho phép người dùng tạo mới một SOW (Statement of Work) — hợp đồng chi tiết phạm vi công việc, thuộc về một MSA. SOW là điều kiện để tạo PO và Billable Rate. |
| **Điều kiện tiên quyết:** | 1. Người dùng đã đăng nhập thành công với vai trò SSC Member hoặc SSC Team Lead.<br>2. Người dùng đang ở màn hình Default Contract list hoặc SOW list.<br>3. Đã tồn tại ít nhất một MSA trong hệ thống (CMS-MSA ID khả dụng). |
| **Điều kiện hậu quyết:** | 1. SOW được tạo thành công với trạng thái "Draft" hoặc "Waiting for Sign off".<br>2. SOW được liên kết với MSA cha thông qua CMS-MSA ID.<br>3. Hệ thống lưu lịch sử tạo SOW vào bảng History.<br>4. SOW hiển thị trong danh sách SOW và tab Related của MSA cha. |
| **Độ ưu tiên:** | Cao - SOW là bước tiếp theo bắt buộc sau MSA trong luồng contract. |
| **Tần suất sử dụng:** | Trung bình, mỗi MSA có thể có nhiều SOW. |
| **Luồng chính:** | 1. Người dùng chọn "Create SOW" từ Default Contract list hoặc SOW list.<br>2. Hệ thống hiển thị màn hình Create SOW với các trường thông tin (BR 48).<br>3. Người dùng nhập thông tin SOW bao gồm: OB, Account Code, CMS-MSA ID (chọn MSA cha), Total Contract Value (LC), Contract Currency, Tax Amount (LC), Contract Name, Contract Official Code, SOW Order Type, Contract Temp Code, SOW Payment Terms, Contract Signed Date, Contract Start Date, Contract End Date, SOW Legal Company, SOW Signed With, SOW Sales Supporter, SOW Description.<br>4. Người dùng nhấn "Save".<br>5. Hệ thống validate dữ liệu — kiểm tra mapping với master data và contract data (BR 49).<br>6. Hệ thống kiểm tra các trường bắt buộc và lưu SOW (BR 50, BR 51).<br>7. Hệ thống hiển thị thông báo tạo thành công và chuyển sang màn hình SOW Detail. |
| **Luồng thay thế:** | **UC-CONTRACT-02.LTT.1: Lưu dạng Draft**<br>Tại bước 6, nếu các trường bắt buộc cho "Waiting for Sign off" chưa đầy đủ nhưng đã có tối thiểu: OB, Account Code, CMS-MSA ID, Contract Name:<br>6a. Hệ thống lưu SOW với trạng thái "Draft".<br>6b. Hệ thống hiển thị thông báo lưu Draft thành công.<br>→ Tiếp tục từ bước 7 của Luồng chính.<br><br>**UC-CONTRACT-02.LTT.2: Tạo SOW từ Related tab của MSA**<br>Tại bước 1, người dùng chọn tab "Related" trong MSA Detail → chọn loại SOW → nhấn "Create":<br>1a. Hệ thống mở màn hình Create SOW trong tab mới.<br>1b. Hệ thống tự động điền CMS-MSA ID, OB, Account Code từ MSA cha (BR 57).<br>→ Tiếp tục từ bước 3 của Luồng chính. |
| **Ngoại lệ:** | **UC-CONTRACT-02.NL.1: Validate thất bại**<br>Điều kiện kích hoạt: Dữ liệu không hợp lệ (không mapping với master data, CMS-MSA ID không tồn tại).<br>Phản hồi: Hệ thống hiển thị thông báo lỗi MSG 1 cho các trường không hợp lệ.<br>Trạng thái cuối: Người dùng quay lại màn hình Create SOW để sửa dữ liệu.<br><br>**UC-CONTRACT-02.NL.2: MSA cha chưa tồn tại**<br>Điều kiện kích hoạt: Không có MSA nào trong hệ thống để chọn CMS-MSA ID.<br>Phản hồi: Hệ thống không cho phép lưu, hiển thị MSG 1.<br>Trạng thái cuối: Người dùng cần tạo MSA trước (UC-CONTRACT-01). |
| **Bao gồm:** | UC-CONTRACT-02.SUB.1: Add Attachment file (UC 23) — có thể gọi tại bước 3. |
| **Yêu cầu đặc biệt:** | **Hiệu năng**: Màn hình Create SOW load trong < 3s.<br>**Bảo mật**: SSC Member chỉ xem/sửa SOW do mình tạo; Team Lead xem/sửa SOW của nhân viên mình.<br>**Độ tin cậy**: Mọi thay đổi phải được lưu vào bảng History. |
| **Giả định:** | 1. MSA cha đã được tạo và có trạng thái hợp lệ (không phải Deleted/Cancelled).<br>2. Master data (Order Type, Payment Terms, Legal Company, Signed With, Sales Supporter, Currency) đã được cấu hình. |
| **Ghi chú và vấn đề mở:** | [NOTE-1] CMS-MSA ID là trường bắt buộc — SOW phải thuộc về một MSA.<br>[NOTE-2] Trường bắt buộc cho Draft: OB, Account Code, CMS-MSA ID, Contract Name.<br>[NOTE-3] Trường bắt buộc cho Waiting for Sign off: tất cả 17 trường có dấu * trong SRS. |

---

## UC-CONTRACT-03: Tạo PO (Purchase Order)

| **Mã Use Case:** | UC-CONTRACT-03 |
| ---: | :--- |
| **Tên Use Case:** | Tạo PO |

| **Người tạo:** | Lead BA | **Người cập nhật cuối:** | AI Assistant |
| ---: | :--- | ---: | :--- |
| **Ngày tạo:** | 2025-05-17 | **Ngày cập nhật cuối:** | 2025-05-17 |

| **Tác nhân:** | **Chính:** SSC Member, SSC Team Lead. **Phụ:** Hệ thống CMS. |
| ---: | :--- |
| **Mô tả:** | Use case cho phép người dùng tạo mới một PO (Purchase Order) — đơn đặt hàng thuộc về MSA và có thể liên kết với SOW. PO là cơ sở để gán Resource, tạo Work Order và theo dõi Timesheet/Invoice. |
| **Điều kiện tiên quyết:** | 1. Người dùng đã đăng nhập thành công với vai trò SSC Member hoặc SSC Team Lead.<br>2. Người dùng đang ở màn hình Default Contract list hoặc PO list.<br>3. Đã tồn tại ít nhất một MSA trong hệ thống (CMS-MSA ID khả dụng).<br>4. (Tùy chọn) Đã tồn tại SOW nếu muốn liên kết PO với SOW (CMS-SOW ID). |
| **Điều kiện hậu quyết:** | 1. PO được tạo thành công với trạng thái "Draft" hoặc "Waiting for Sign off".<br>2. PO được liên kết với MSA cha (bắt buộc) và SOW (tùy chọn).<br>3. Hệ thống lưu lịch sử tạo PO vào bảng History.<br>4. PO hiển thị trong danh sách PO và tab Related của MSA/SOW cha. |
| **Độ ưu tiên:** | Cao - PO là đơn vị quản lý ngân sách và resource chính. |
| **Tần suất sử dụng:** | Cao, mỗi SOW/MSA có thể có nhiều PO. |
| **Luồng chính:** | 1. Người dùng chọn "Create PO" từ Default Contract list hoặc PO list.<br>2. Hệ thống hiển thị màn hình Create PO với các trường thông tin (BR 87).<br>3. Người dùng nhập thông tin PO bao gồm: OB, Account Code, CMS-MSA ID (chọn MSA cha), CMS-SOW ID (tùy chọn), Order Amount (LC), Order Extended Amount (LC), Tax Amount (LC), Order Name, Order Official Code, PO Opportunity, PO Opportunity ID (External), PO Legal Company, PO Signed With, PO Order Type, Order Payment Terms, PO Contract Temp Code, Order Adjustment (LC), Order Discount, Order Discount (%), Order Temp Code, Order Signed Date, Order Start Date, Order End Date, PO Sales Supporter, PO Currency, PO Description, Actual Start Date, Actual End Date, Total Order Amount.<br>4. Người dùng nhấn "Save".<br>5. Hệ thống validate dữ liệu — kiểm tra mapping với master data và contract data (BR 88).<br>6. Hệ thống kiểm tra các trường bắt buộc và lưu PO (BR 89, BR 90).<br>7. Hệ thống hiển thị thông báo tạo thành công và chuyển sang màn hình PO Detail. |
| **Luồng thay thế:** | **UC-CONTRACT-03.LTT.1: Lưu dạng Draft**<br>Tại bước 6, nếu các trường bắt buộc cho "Waiting for Sign off" chưa đầy đủ nhưng đã có tối thiểu: OB, Account Code, CMS-MSA ID, Order Name:<br>6a. Hệ thống lưu PO với trạng thái "Draft".<br>6b. Hệ thống hiển thị thông báo lưu Draft thành công.<br>→ Tiếp tục từ bước 7 của Luồng chính.<br><br>**UC-CONTRACT-03.LTT.2: Tạo PO từ Related tab của MSA/SOW**<br>Tại bước 1, người dùng chọn tab "Related" trong MSA Detail hoặc SOW Detail → chọn loại PO → nhấn "Create":<br>1a. Hệ thống mở màn hình Create PO trong tab mới.<br>1b. Hệ thống tự động điền CMS-MSA ID, CMS-SOW ID, OB, Account Code từ contract cha (BR 96).<br>→ Tiếp tục từ bước 3 của Luồng chính. |
| **Ngoại lệ:** | **UC-CONTRACT-03.NL.1: Validate thất bại**<br>Điều kiện kích hoạt: Dữ liệu không hợp lệ (không mapping với master data, CMS-MSA ID không tồn tại, giá trị số âm).<br>Phản hồi: Hệ thống hiển thị thông báo lỗi MSG 1 cho các trường không hợp lệ.<br>Trạng thái cuối: Người dùng quay lại màn hình Create PO để sửa dữ liệu.<br><br>**UC-CONTRACT-03.NL.2: MSA cha chưa tồn tại**<br>Điều kiện kích hoạt: Không có MSA nào trong hệ thống để chọn CMS-MSA ID.<br>Phản hồi: Hệ thống không cho phép lưu, hiển thị MSG 1.<br>Trạng thái cuối: Người dùng cần tạo MSA trước (UC-CONTRACT-01). |
| **Bao gồm:** | UC-CONTRACT-03.SUB.1: Add Attachment file (UC 37) — có thể gọi tại bước 3. |
| **Yêu cầu đặc biệt:** | **Hiệu năng**: Màn hình Create PO load trong < 3s.<br>**Bảo mật**: SSC Member chỉ xem/sửa PO do mình tạo; Team Lead xem/sửa PO của nhân viên mình.<br>**Độ tin cậy**: Mọi thay đổi phải được lưu vào bảng History. |
| **Giả định:** | 1. MSA cha đã được tạo và có trạng thái hợp lệ.<br>2. SOW (nếu liên kết) đã tồn tại và thuộc cùng MSA.<br>3. Master data (Opportunity, Order Type, Payment Terms, Legal Company, Signed With, Sales Supporter, Currency) đã được cấu hình. |
| **Ghi chú và vấn đề mở:** | [NOTE-1] CMS-MSA ID bắt buộc, CMS-SOW ID tùy chọn — PO có thể thuộc trực tiếp MSA mà không qua SOW.<br>[NOTE-2] Trường bắt buộc cho Draft: OB, Account Code, CMS-MSA ID, Order Name.<br>[NOTE-3] Trường bắt buộc cho Waiting for Sign off: tất cả 28 trường có dấu * trong SRS.<br>[NOTE-4] PO là đơn vị để gán Resource và Generate Work Order (UC 84). |

---

## UC-CONTRACT-04: Tạo Billable Rate

| **Mã Use Case:** | UC-CONTRACT-04 |
| ---: | :--- |
| **Tên Use Case:** | Tạo Billable Rate |

| **Người tạo:** | Lead BA | **Người cập nhật cuối:** | AI Assistant |
| ---: | :--- | ---: | :--- |
| **Ngày tạo:** | 2025-05-17 | **Ngày cập nhật cuối:** | 2025-05-17 |

| **Tác nhân:** | **Chính:** SSC Member, SSC Team Lead. **Phụ:** Hệ thống CMS. |
| ---: | :--- |
| **Mô tả:** | Use case cho phép người dùng tạo mới một Billable Rate — bảng giá dịch vụ chi tiết theo từng loại resource/product, thuộc về MSA và có thể liên kết với SOW/PO. Billable Rate là cơ sở để tính toán Timesheet và Invoice. |
| **Điều kiện tiên quyết:** | 1. Người dùng đã đăng nhập thành công với vai trò SSC Member hoặc SSC Team Lead.<br>2. Người dùng đang ở màn hình Default Contract list hoặc Billable Rate list.<br>3. Đã tồn tại ít nhất một MSA trong hệ thống (CMS-MSA ID khả dụng).<br>4. (Tùy chọn) Đã tồn tại SOW và/hoặc PO nếu muốn liên kết. |
| **Điều kiện hậu quyết:** | 1. Billable Rate được tạo thành công với trạng thái "Draft" hoặc "Waiting for Sign off".<br>2. Billable Rate được liên kết với MSA (bắt buộc), SOW và PO (tùy chọn).<br>3. Hệ thống lưu lịch sử tạo Billable Rate vào bảng History.<br>4. Billable Rate hiển thị trong danh sách Billable Rate và tab Related của contract cha. |
| **Độ ưu tiên:** | Cao - Billable Rate là cơ sở tính giá cho Timesheet và Invoice. |
| **Tần suất sử dụng:** | Cao, mỗi PO/SOW có thể có nhiều Billable Rate cho các loại resource khác nhau. |
| **Luồng chính:** | 1. Người dùng chọn "Create Billable Rate" từ Default Contract list hoặc Billable Rate list.<br>2. Hệ thống hiển thị màn hình Create Billable Rate với các trường thông tin (BR 127).<br>3. Người dùng nhập thông tin Billable Rate bao gồm:<br>— **Thông tin chung**: OB, Account Code, CMS-MSA ID (chọn MSA cha), CMS-SOW ID (tùy chọn), CMS-PO ID (tùy chọn), Billable Rate Name, Billable Rate Official Code, Billable Rate Opportunity, Billable Rate Opportunity ID (External), Billable Rate Currency, Billable Rate Signed Date, Billable Rate Start Date, Billable Rate End Date, Billable Rate Description, Billable Rate Sales Supporter.<br>— **Thông tin Rate Item**: Product ID, Product, Resource Type, Sub-Resource Type, Unit, Resource Location, Sale Price, PO Line, PO Line Description, Billable Role, Billable Seniority, Billable Level, Billable Unit, Billable Rate, Billable Rate Start Date, Billable Rate End Date, Billable Effort (%), Billable Quantity, Billable Location, Billable Resource Type, Billable Sub-Resource Type, Billable Product DC, Adjustment (LC), Description.<br>4. Người dùng nhấn "Save".<br>5. Hệ thống validate dữ liệu — kiểm tra mapping với master data và contract data (BR 128).<br>6. Hệ thống kiểm tra các trường bắt buộc và lưu Billable Rate (BR 129, BR 130).<br>7. Hệ thống hiển thị thông báo tạo thành công và chuyển sang màn hình Billable Rate Detail. |
| **Luồng thay thế:** | **UC-CONTRACT-04.LTT.1: Lưu dạng Draft**<br>Tại bước 6, nếu các trường bắt buộc cho "Waiting for Sign off" chưa đầy đủ nhưng đã có tối thiểu: OB, Account Code, CMS-MSA ID, Billable Rate Name:<br>6a. Hệ thống lưu Billable Rate với trạng thái "Draft".<br>6b. Hệ thống hiển thị thông báo lưu Draft thành công.<br>→ Tiếp tục từ bước 7 của Luồng chính.<br><br>**UC-CONTRACT-04.LTT.2: Tạo Billable Rate từ Related tab của MSA/SOW/PO**<br>Tại bước 1, người dùng chọn tab "Related" trong MSA/SOW/PO Detail → chọn loại Billable Rate → nhấn "Create":<br>1a. Hệ thống mở màn hình Create Billable Rate trong tab mới.<br>1b. Hệ thống tự động điền CMS-MSA ID, CMS-SOW ID, CMS-PO ID, OB, Account Code từ contract cha.<br>→ Tiếp tục từ bước 3 của Luồng chính. |
| **Ngoại lệ:** | **UC-CONTRACT-04.NL.1: Validate thất bại**<br>Điều kiện kích hoạt: Dữ liệu không hợp lệ (không mapping với master data, CMS-MSA ID không tồn tại, Product không hợp lệ).<br>Phản hồi: Hệ thống hiển thị thông báo lỗi MSG 1 cho các trường không hợp lệ.<br>Trạng thái cuối: Người dùng quay lại màn hình Create Billable Rate để sửa dữ liệu.<br><br>**UC-CONTRACT-04.NL.2: MSA cha chưa tồn tại**<br>Điều kiện kích hoạt: Không có MSA nào trong hệ thống để chọn CMS-MSA ID.<br>Phản hồi: Hệ thống không cho phép lưu, hiển thị MSG 1.<br>Trạng thái cuối: Người dùng cần tạo MSA trước (UC-CONTRACT-01). |
| **Bao gồm:** | UC-CONTRACT-04.SUB.1: Add Attachment file (UC 53) — có thể gọi tại bước 3.<br>UC-CONTRACT-04.SUB.2: Update Contract Configuration (UC 58) — có thể gọi sau bước 7 để cấu hình Term & Period cho Timesheet/Invoice. |
| **Yêu cầu đặc biệt:** | **Hiệu năng**: Màn hình Create Billable Rate load trong < 3s.<br>**Bảo mật**: SSC Member chỉ xem/sửa Billable Rate do mình tạo; Team Lead xem/sửa của nhân viên mình.<br>**Độ tin cậy**: Mọi thay đổi phải được lưu vào bảng History. |
| **Giả định:** | 1. MSA cha đã được tạo và có trạng thái hợp lệ.<br>2. SOW và PO (nếu liên kết) đã tồn tại và thuộc cùng MSA.<br>3. Master data (Product, Resource Type, Currency, Sales Supporter, Opportunity) đã được cấu hình.<br>4. Billable Rate Item (chi tiết giá) được nhập cùng lúc với Billable Rate header. |
| **Ghi chú và vấn đề mở:** | [NOTE-1] CMS-MSA ID bắt buộc; CMS-SOW ID và CMS-PO ID tùy chọn.<br>[NOTE-2] Trường bắt buộc cho Draft: OB, Account Code, CMS-MSA ID, Billable Rate Name.<br>[NOTE-3] Trường bắt buộc cho Waiting for Sign off: tất cả trường có dấu * (khoảng 30+ trường bao gồm cả Rate Item).<br>[NOTE-4] Sau khi tạo Billable Rate, cần cấu hình Configuration (UC 58/107/108) để hệ thống generate Timesheet và Invoice tự động. |

---

## Tổng quan luồng tạo Contract (End-to-End Flow)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    LUỒNG TẠO CONTRACT: MSA → SOW → PO → BR             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────────┐  │
│  │  Tạo MSA │────▶│  Tạo SOW │────▶│  Tạo PO  │────▶│ Tạo Billable │  │
│  │  (UC-01) │     │  (UC-02) │     │  (UC-03) │     │  Rate (UC-04)│  │
│  └────┬─────┘     └────┬─────┘     └────┬─────┘     └──────┬───────┘  │
│       │                 │                 │                   │          │
│       ▼                 ▼                 ▼                   ▼          │
│  Draft/Waiting     Draft/Waiting     Draft/Waiting      Draft/Waiting   │
│  for Sign off      for Sign off      for Sign off       for Sign off   │
│       │                 │                 │                   │          │
│       ▼                 ▼                 ▼                   ▼          │
│  Sign off ──▶      Sign off ──▶      Sign off ──▶      Submitted ──▶   │
│  Finished          Finished          Finished           Finished        │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  QUAN HỆ PHỤ THUỘC:                                                    │
│  • MSA (bắt buộc) ← SOW ← PO ← Billable Rate                         │
│  • SOW cần CMS-MSA ID                                                   │
│  • PO cần CMS-MSA ID (bắt buộc) + CMS-SOW ID (tùy chọn)               │
│  • BR cần CMS-MSA ID (bắt buộc) + CMS-SOW ID + CMS-PO ID (tùy chọn)   │
├─────────────────────────────────────────────────────────────────────────┤
│  COMMON BUSINESS RULES:                                                 │
│  • Stage chỉ tiến lên, không lùi                                        │
│  • Chỉ Draft/Waiting for Sign off/Waiting for Submit mới Edit được      │
│  • Mọi thay đổi lưu vào History                                         │
│  • Nội dung dài hiển thị "..." không xuống dòng                          │
└─────────────────────────────────────────────────────────────────────────┘
```

## State Transition chung cho Contract

| Trạng thái | Mô tả | Điều kiện chuyển tiếp |
|---|---|---|
| **Draft** | Mới tạo, chưa đủ thông tin bắt buộc | Điền đủ mandatory fields → Waiting for Sign off |
| **Waiting for Sign off** | Đủ thông tin, chờ ký | Có Signed Date → Signed off |
| **Signed off** | Đã ký | Có Finish Date → Finished |
| **Finished** | Hoàn thành | — (trạng thái cuối) |
| **Cancelled** | Bị hủy | Từ bất kỳ trạng thái nào (nếu chưa có invoiced TS/Invoice) |
| **Stopped** | Bị dừng | Từ bất kỳ trạng thái nào |
| **Deleted** | Bị xóa | Chỉ từ Draft |

> **Lưu ý đặc biệt cho Billable Rate**: State transition có thêm trạng thái "Submitted" (giữa Waiting for Sign off và Finished).
