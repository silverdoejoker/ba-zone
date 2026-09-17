---
name: enterprise-nda-sanitizer
description: |
  Quy tắc và bộ lọc bắt buộc để tự động ẩn danh hóa (Sanitize / Generalize) toàn bộ thực thể doanh nghiệp nhạy cảm khi viết tài liệu, báo cáo context, Use Cases, User Stories hoặc phân tích hệ thống.
  Đảm bảo mọi tài liệu lưu trữ trong workspace đều tuân thủ nguyên tắc "Strict Documentation Only / Zero Data Leakage", cho phép đồng bộ Git và làm việc từ xa an toàn.
  Chỉ hiển thị tên tổ chức, định danh hợp đồng hoặc thông tin PII thực tế khi có cờ xuất bản chính thức (official_export=true).
author: Phúc NT @ BA Zone
source: https://github.com/ba-zone
---

# Enterprise NDA Sanitizer & Entity Generalization Rule
> by **Phúc NT** · BA Zone · Digital School

Quy tắc này thiết lập **chế độ bảo vệ dữ liệu mặc định** cho mọi tài liệu, spec, báo cáo phân tích kiến trúc được lưu trữ hoặc tạo ra trong repository `ba-zone`.

---

## 🎯 Triết Lý Cốt Lõi: "Generalize by Default, Specialize only on Export"

Khi phân tích nghiệp vụ, reverse-engineer tài liệu hoặc lưu trữ context hệ thống:
1. **Giá trị cốt lõi cần giữ**: Luồng nghiệp vụ, logic tính toán, kiến trúc tích hợp (API/Middleware), sơ đồ phân quyền, tiêu chí đánh giá, checklist vận hành, công thức SLA.
2. **Giá trị cần ẩn danh hóa (Generalize)**: Tên công ty, tên khách hàng, mã dự án/hợp đồng nội bộ, URL/IP nội bộ, họ tên nhân sự (PII).

---

## 🛡️ Bảng Quy Chuẩn Ánh Xạ Thực Thể Ẩn Danh (Generalization Mapping)

| Loại thực thể | Dữ liệu nhạy cảm thực tế | Quy chuẩn thay thế an toàn (Generalized) |
|---|---|---|
| **Tập đoàn / Khách hàng lớn** | Tên tập đoàn thực tế (FPT, Nova, Vingroup, Viettel...) | `Tập đoàn Bất động sản & Dịch vụ Đa ngành (MegaCorp / RetailCorp / Enterprise Group)` |
| **Đơn vị / Công ty thành viên** | Nova Service, Nova Land, FPT Retail... | `Mega Service, Mega Land, Retail Corp (MSG / MGLG / RTC)` |
| **Đơn vị phát triển / Vendor** | Tên cty phần mềm / vendor cụ thể (eChain, FPT Software...) | `Công ty Giải pháp Phần mềm Doanh nghiệp (TechPartner / SolutionVendor)` |
| **Mã định danh bảo mật** | Số hợp đồng, số công văn, mã URD (`0032/NVG/2026`) | `Mã tham chiếu chuẩn hóa: REF-[SYSTEM]-[YEAR] (vd: REF-GMS-2026)` |
| **Đường dẫn nội bộ (URLs / IPs)** | `*.frt.vn`, `*.frt.local`, IP nội bộ `192.168.x.x` | `https://confluence.example.com`, `http://api.internal.local` |
| **Nhân sự & Chức danh (PII)** | Họ tên thật của BOD, PO, BA, Dev, Tech Lead | `BOM Representative, Product Owner Lead, Senior IT BA, Technical Architecture Lead` |
| **Mã quy trình nội bộ** | `NSG-CS-SOP02`, `NSG-FNB-WI10.F01` | `SOP-CS-02`, `SOP-FNB-WI10.F01` |

---

## ⚙️ Cơ Chế Kích Hoạt Xuất Bản Chính Thức: `official_export`

Mặc định biến `official_export=false`:
- Toàn bộ tài liệu soạn thảo trong `docs/`, `artifacts/`, `.agents/` luôn áp dụng bảng ánh xạ ẩn danh ở trên.
- Khi người dùng yêu cầu rõ ràng: *"Xuất bản tài liệu chính thức gửi khách hàng"* kèm lệnh:
  ```text
  official_export=true
  entity_target="Tên Khách Hàng / Dự Án"
  ```
  AI Agent mới tiến hành nạp tên thực thể cụ thể vào bản xuất bản cuối cùng (và lưu ý người dùng không commit bản đó lên Git công cộng).

---

## 📋 Checklist Tự Động Rà Soát Trước Khi Lưu File (Sanitization Checklist)

Trước khi ghi bất kỳ tài liệu nào vào `docs/` hoặc `artifacts/`:
- [ ] 0 tên tập đoàn / công ty khách hàng thật trong văn bản.
- [ ] 0 mã hợp đồng hoặc mã số văn bản bảo mật nội bộ.
- [ ] 0 đường dẫn web/server nội bộ (`.local`, intranet domain).
- [ ] 0 họ tên nhân viên / đối tác cụ thể (chuyển thành tên chức danh).
- [ ] File đã sẵn sàng để commit Git an toàn và đồng bộ về máy cá nhân làm việc.
