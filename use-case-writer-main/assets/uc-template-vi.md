# Mẫu Use Case — Tiếng Việt (Copy-Ready Markdown)

Sao chép mẫu bên dưới và thay thế các placeholder `<...>` bằng nội dung thực tế.

> Mẫu bởi **Phúc NT** · BA Zone · Digital School

---

## UC-XX-YY: \<Tên Use Case\>

| **Mã Use Case:** | UC-XX-YY |
| ---: | :--- |
| **Tên Use Case:** | \<Động từ + Tân ngữ\> |

| **Người tạo:** | \<Họ tên - Vai trò\> | **Người cập nhật cuối:** | \<Họ tên - Vai trò\> |
| ---: | :--- | ---: | :--- |
| **Ngày tạo:** | YYYY-MM-DD | **Ngày cập nhật cuối:** | YYYY-MM-DD |

| **Tác nhân:** | **Chính:** \<vai trò cụ thể, ví dụ: Học viên, Mentor, Quản lý HR\>. **Phụ:** \<tác nhân hỗ trợ, ví dụ: Cổng thanh toán, LMS, Dịch vụ thông báo\>. |
| ---: | :--- |
| **Mô tả:** | \<2-3 câu: TẠI SAO + LÀM GÌ + KẾT QUẢ\> |
| **Điều kiện tiên quyết:** | 1. \<điều kiện 1, có thể kiểm chứng\><br>2. \<điều kiện 2\><br>3. \<...\> |
| **Điều kiện hậu quyết:** | 1. \<trạng thái 1 sau khi UC hoàn thành\><br>2. \<trạng thái 2\><br>3. \<...\> |
| **Độ ưu tiên:** | Cao / Trung bình / Thấp - \<lý do ngắn gọn\> |
| **Tần suất sử dụng:** | \<số lần / đơn vị thời gian\>, cao điểm: \<...\> |
| **Luồng chính:** | 1. \<Hành động của Tác nhân\><br>2. \<Phản hồi của Hệ thống\><br>3. \<...\><br>... |
| **Luồng thay thế:** | **UC-XX-YY.LTT.1: \<Tên luồng thay thế\>**<br>Tại bước \<N\>, nếu \<điều kiện\>:<br>Na. \<bước\><br>Nb. \<bước\><br>... → tiếp tục từ bước \<M\> của Luồng chính. |
| **Ngoại lệ:** | **UC-XX-YY.NL.1: \<Tên ngoại lệ\>**<br>Điều kiện kích hoạt: \<khi nào xảy ra\><br>Phản hồi: \<hệ thống làm gì\><br>Trạng thái cuối: \<trạng thái kết thúc\> |
| **Bao gồm:** | UC-AA-BB: \<tên UC con\> (được gọi tại bước \<N\>) |
| **Yêu cầu đặc biệt:** | **Hiệu năng**: \<...\><br>**Bảo mật**: \<...\><br>**Độ tin cậy**: \<...\><br>**Tuân thủ**: \<...\> |
| **Giả định:** | 1. \<giả định 1\><br>2. \<giả định 2\> |
| **Ghi chú và vấn đề mở:** | [TBD-1] \<câu hỏi\> \| Phụ trách: \<...\> \| Hạn: \<...\> \| Kết quả: \<...\> |

---

## Hướng dẫn dịch thuật field labels

Bảng đối chiếu Anh–Việt cho các field label trong template:

| Tiếng Anh | Tiếng Việt |
|---|---|
| Use Case ID | Mã Use Case |
| Use Case Name | Tên Use Case |
| Created By | Người tạo |
| Last Updated By | Người cập nhật cuối |
| Date Created | Ngày tạo |
| Date Last Updated | Ngày cập nhật cuối |
| Actor | Tác nhân |
| Description | Mô tả |
| Preconditions | Điều kiện tiên quyết |
| Postconditions | Điều kiện hậu quyết |
| Priority | Độ ưu tiên |
| Frequency of Use | Tần suất sử dụng |
| Normal Course of Events | Luồng chính |
| Alternative Courses | Luồng thay thế |
| Exceptions | Ngoại lệ |
| Includes | Bao gồm |
| Special Requirements | Yêu cầu đặc biệt |
| Assumptions | Giả định |
| Notes and Issues | Ghi chú và vấn đề mở |
| High / Medium / Low | Cao / Trung bình / Thấp |
| Primary / Secondary | Chính / Phụ |

## Quy ước viết tắt trong UC tiếng Việt

| Ký hiệu | Ý nghĩa |
|---|---|
| LTT.N | Luồng Thay Thế số N (tương đương AC.N trong bản tiếng Anh) |
| NL.N | Ngoại Lệ số N (tương đương EX.N trong bản tiếng Anh) |

> **Lưu ý**: Mã UC ID (`UC-XX-YY`), mã LTT/NL, và tên file vẫn giữ nguyên định dạng ASCII để đảm bảo tương thích với các công cụ quản lý yêu cầu (Jira, Confluence, Git).

---
*Mẫu bởi **Phúc NT** · BA Zone · Digital School*  
*Vui lòng giữ nguyên thông tin tác giả khi phân phối lại mẫu này.*
