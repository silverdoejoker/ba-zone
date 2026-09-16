---
inclusion: manual
---

# Ví dụ User Story + AC mẫu cho EdTech & Digital School

> 7 ví dụ thực tế từ các domain phổ biến trong sản phẩm giáo dục trực tuyến.
> Biên soạn bởi **Phúc NT** · BA Zone · Digital School

---

## Ví dụ 1: Đăng ký và thanh toán khóa học

### US-ENROLL-001: Đăng ký khóa học và thanh toán qua ví điện tử

**As a** học viên đã có tài khoản BA Zone và liên kết ví điện tử  
**I want to** mua khóa học "Business Analysis Fundamentals" và thanh toán bằng ví  
**So that** có thể truy cập ngay nội dung học mà không cần chờ xác nhận thủ công

**AC1: Thanh toán và enroll thành công - happy path**
- **Given** học viên chọn khóa "BA Fundamentals" giá 1.500.000 VND
- **And** số dư ví ≥ 1.500.000 VND và khóa học còn slot
- **When** học viên ấn "Đăng ký ngay" → xác nhận thanh toán → nhập PIN ví
- **Then** hệ thống trừ 1.500.000 VND từ ví trong vòng 5 giây
- **And** tự động enroll học viên vào khóa học
- **And** gửi email xác nhận kèm link truy cập và lưu vào "Khóa học của tôi"

**AC2: Số dư ví không đủ**
- **Given** số dư ví là 800.000 VND, giá khóa học 1.500.000 VND
- **When** học viên ấn "Đăng ký ngay"
- **Then** hệ thống hiển thị "Số dư không đủ. Bạn cần thêm 700.000 VND"
- **And** cung cấp 2 lựa chọn: "Nạp tiền vào ví" và "Chọn phương thức khác"
- **And** không trừ tiền và không tạo enrollment

**AC3: Mất kết nối trong khi xử lý thanh toán**
- **Given** học viên đã xác nhận thanh toán và hệ thống đang xử lý
- **When** mạng bị ngắt trong vòng 30 giây
- **Then** hệ thống hiển thị "Đang xác thực giao dịch..."
- **And** sau khi có mạng lại, tự động kiểm tra trạng thái giao dịch
- **And** hiển thị kết quả cuối cùng mà không trừ tiền 2 lần

---

## Ví dụ 2: Đặt lịch 1-on-1 với Mentor

### US-MENTOR-BOOK-001: Đặt lịch tư vấn 1-on-1 với Mentor BA Zone

**As a** học viên Digital School đang theo học chương trình BA Advanced  
**I want to** đặt lịch tư vấn 1-on-1 với mentor có chuyên môn phù hợp  
**So that** nhận được hướng dẫn cụ thể cho bài tập thực hành mà không cần chờ buổi học chung

**AC1: Đặt lịch thành công**
- **Given** học viên chọn Mentor Phúc NT, slot trống ngày 15/06/2026 lúc 20:00
- **And** học viên còn 1 session 1-on-1 trong gói tháng
- **When** học viên xác nhận đặt lịch và nhập chủ đề cần tư vấn
- **Then** hệ thống tạo booking MNT20260615001 và gửi link Google Meet cho cả 2 bên
- **And** trừ 1 session khỏi quota tháng của học viên
- **And** gửi reminder 1 giờ trước buổi tư vấn qua email và app notification

**AC2: Race condition - slot bị người khác đặt trước**
- **Given** học viên đang ở màn hình xác nhận slot 20:00 ngày 15/06
- **When** học viên ấn "Đặt lịch" nhưng slot vừa được học viên khác đặt 3 giây trước
- **Then** hệ thống hiển thị "Slot này vừa được đặt. Vui lòng chọn slot khác"
- **And** không trừ session quota và không tạo booking

**AC3: Mentor hủy buổi tư vấn**
- **Given** học viên đã đặt lịch thành công với mentor
- **When** mentor hủy buổi tư vấn ít nhất 6 tiếng trước giờ hẹn
- **Then** hệ thống hoàn lại 1 session vào quota tháng của học viên
- **And** gửi thông báo lý do hủy và đề xuất 3 slot thay thế trong 7 ngày tới

---

## Ví dụ 3: Theo dõi tiến độ học

### US-PROGRESS-001: Xem báo cáo tiến độ học cá nhân

**As a** học viên đang theo học nhiều khóa học song song trên BA Zone  
**I want to** xem dashboard tiến độ học cá nhân theo từng khóa  
**So that** biết mình đang ở đâu trong lộ trình và ưu tiên ôn tập những phần chưa hoàn thành

**AC1: Hiển thị dashboard tiến độ đúng**
- **Given** học viên đang theo học 2 khóa: "BA Fundamentals" (60%) và "Agile for BA" (20%)
- **When** học viên vào mục "Tiến độ học của tôi"
- **Then** hệ thống hiển thị % hoàn thành từng khóa, số bài đã xem, số bài còn lại
- **And** dữ liệu được cập nhật trong vòng 1 phút sau khi học viên hoàn thành bài học

**AC2: Học viên chưa bắt đầu khóa học**
- **Given** học viên đã mua khóa "SQL for BA" nhưng chưa vào học bài nào
- **When** học viên xem tiến độ của khóa đó
- **Then** hiển thị "0% hoàn thành - Bắt đầu học ngay!" với CTA rõ ràng

**AC3: Dữ liệu tiến độ không đồng bộ sau khi học offline**
- **Given** học viên đã hoàn thành 3 bài học khi không có mạng
- **When** học viên kết nối lại internet
- **Then** hệ thống đồng bộ tiến độ trong vòng 60 giây, không bị reset về số cũ

---

## Ví dụ 4: Cấp phát chứng chỉ

### US-CERT-001: Cấp chứng chỉ hoàn thành khóa học

**As a** học viên vừa hoàn thành 100% khóa học và đạt điểm kiểm tra cuối khóa  
**I want to** nhận chứng chỉ hoàn thành có tên tôi, tên khóa học và mã xác thực  
**So that** có bằng chứng cụ thể để cập nhật vào LinkedIn và hồ sơ xin việc

**AC1: Cấp chứng chỉ tự động khi đủ điều kiện**
- **Given** học viên hoàn thành 100% bài học và đạt ≥ 70% điểm kiểm tra cuối khóa
- **When** hệ thống xác nhận kết quả kiểm tra
- **Then** tự động sinh chứng chỉ PDF có mã xác thực CERT-BAF-2026-00123
- **And** gửi file chứng chỉ qua email trong vòng 5 phút

**AC2: Học viên chưa đủ điều kiện**
- **Given** học viên hoàn thành 100% bài học nhưng điểm kiểm tra là 55%
- **When** hệ thống xử lý kết quả
- **Then** không cấp chứng chỉ và hiển thị "Bạn cần đạt tối thiểu 70%. Điểm hiện tại: 55%"
- **And** cho phép làm lại bài kiểm tra sau 24 giờ

**AC3: Xác thực chứng chỉ từ bên ngoài**
- **Given** nhà tuyển dụng nhập mã CERT-BAF-2026-00123 vào trang verify.bazone.vn
- **When** hệ thống tra cứu mã
- **Then** hiển thị: tên học viên, tên khóa học, ngày cấp, kết quả
- **And** nếu mã không tồn tại, hiển thị "Mã chứng chỉ không hợp lệ"

---

## Ví dụ 5: Live Class & Q&A

### US-LIVE-001: Đặt câu hỏi trong buổi Live Class

**As a** học viên đang tham dự live class trực tuyến  
**I want to** gửi câu hỏi bằng văn bản trong khi giảng viên đang trình bày  
**So that** không làm gián đoạn bài giảng nhưng vẫn được giải đáp vào phần Q&A cuối buổi

**AC1: Gửi câu hỏi thành công**
- **Given** học viên đang trong buổi live class đang diễn ra
- **When** học viên nhập câu hỏi (tối đa 500 ký tự) và ấn "Gửi"
- **Then** câu hỏi xuất hiện trong hàng đợi Q&A hiển thị cho giảng viên
- **And** các học viên khác có thể vote "+1"

**AC2: Câu hỏi trùng lặp**
- **Given** câu hỏi trùng nội dung với câu hỏi đã có (similarity ≥ 80%)
- **When** học viên ấn "Gửi"
- **Then** hệ thống gợi ý "Câu hỏi tương tự đã được gửi. Bạn có muốn vote ủng hộ không?"

**AC3: Buổi live class đã kết thúc**
- **Given** buổi live class đã kết thúc (trạng thái "Ended")
- **When** học viên cố gắng gửi câu hỏi
- **Then** hệ thống ẩn ô nhập câu hỏi và hiển thị link đến forum của khoá học

---

## Ví dụ 6: B2B - Cấp phát khóa học theo lô

### US-B2B-ENROLL-001: Doanh nghiệp cấp phát khóa học cho nhân viên theo lô

**As a** HR Manager của doanh nghiệp đối tác đã ký hợp đồng với BA Zone  
**I want to** cấp phát khóa học cho danh sách nhân viên bằng cách upload file Excel  
**So that** không phải enroll từng người một khi số lượng nhân viên lớn (> 20 người)

**AC1: Upload và enroll thành công**
- **Given** HR Manager upload file Excel đúng template với 50 nhân viên
- **And** tài khoản doanh nghiệp còn đủ 50 license chưa kích hoạt
- **When** HR Manager ấn "Xác nhận cấp phát"
- **Then** hệ thống enroll 50 nhân viên vào khóa học trong vòng 2 phút
- **And** hiển thị báo cáo kết quả: 50/50 thành công

**AC2: File có dữ liệu không hợp lệ**
- **Given** file Excel có 50 dòng, trong đó 3 dòng email sai định dạng và 2 dòng trùng email
- **When** HR Manager upload file
- **Then** hệ thống highlight 5 dòng lỗi với mô tả lỗi cụ thể từng dòng
- **And** cho phép tiếp tục enroll 45 dòng hợp lệ hoặc sửa file và upload lại

**AC3: Không đủ license**
- **Given** tài khoản doanh nghiệp còn 30 license, file upload có 50 nhân viên
- **When** HR Manager ấn "Xác nhận cấp phát"
- **Then** hệ thống thông báo "Bạn cần thêm 20 license" và không enroll bất kỳ ai

---

## Ví dụ 7: Báo cáo vi phạm trong diễn đàn

### US-FORUM-COMPLAINT-001: Báo cáo nội dung vi phạm trong diễn đàn

**As a** thành viên cộng đồng BA Zone đang tham gia thảo luận trong diễn đàn  
**I want to** báo cáo bài viết hoặc bình luận có nội dung vi phạm quy tắc cộng đồng  
**So that** được xem xét và xử lý kịp thời, giữ chất lượng thảo luận trong cộng đồng

**AC1: Gửi báo cáo vi phạm thành công**
- **Given** thành viên đang xem bài viết có nội dung spam
- **When** thành viên ấn "Báo cáo" → chọn lý do → gửi
- **Then** hệ thống tạo ticket RPT20260506001 và xác nhận "Báo cáo đã được ghi nhận"
- **And** nếu bài viết nhận ≥ 5 báo cáo trong 1 giờ, tạm ẩn chờ Moderator duyệt

**AC2: Theo dõi trạng thái xử lý**
- **Given** thành viên đã gửi báo cáo thành công
- **When** Moderator cập nhật trạng thái (Đang xem xét → Đã xử lý / Không vi phạm)
- **Then** thành viên nhận notification về kết quả và lý do quyết định

**AC3: Báo cáo không có phản hồi sau 48 giờ**
- **Given** ticket báo cáo chưa được xử lý sau 48 giờ
- **When** hệ thống kiểm tra SLA tự động
- **Then** escalate ticket lên Community Manager
- **And** gửi thông báo xin lỗi đến người báo cáo, cam kết xử lý trong 12 giờ tiếp theo

---

## Patterns rút ra từ 7 ví dụ

1. **Persona luôn cụ thể** — luôn có context (học viên đang theo học BA Advanced, HR Manager đã ký hợp đồng...)
2. **Goal đo lường được** — có số liệu cụ thể (50 nhân viên, ≥ 70% điểm, 500 ký tự)
3. **So that focus business outcome** — nhận doanh thu ngay, giảm thao tác thủ công
4. **AC luôn có 3 path** — Happy + Edge case + Negative/Error
5. **Edge case mang tính domain** — race condition lịch mentor, license không đủ, câu hỏi trùng lặp
6. **Số liệu trong AC** — thời gian phản hồi (5 phút, 60 giây), ngưỡng điểm (≥ 70%)
7. **Tránh implementation detail** — không nói API name, DB schema, framework

---
*Biên soạn bởi **Phúc NT** · BA Zone · Digital School*
