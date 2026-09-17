# Writing Style Guide — Quy Chuẩn Hành Văn Cho Use Case
> Biên soạn theo nguyên lý Alistair Cockburn (*"Writing Effective Use Cases"*) & IIBA BABOK  
> Tác giả: **Phúc NT** · BA Zone · Digital School

## Nguyên tắc tối thượng: KHẢ NĂNG ĐỌC HIỂU ĐẶT LÊN HÀNG ĐẦU (Readability First)

Một Use Case chất lượng cao phải thỏa mãn:
1. Stakeholder phi kỹ thuật (PO, Business Owner) hiểu đúng bản chất nghiệp vụ.
2. Đội ngũ Lập trình viên (Developers) có đủ thông tin để xây dựng luồng xử lý.
3. Đội ngũ Kiểm thử viên (QA/Testers) có đủ dữ kiện để viết kịch bản Test Cases.
4. Một BA mới tiếp nhận dự án có thể đọc hiểu và bảo trì dễ dàng khi có Change Request.

---

## 5 Quy tắc cốt lõi

### Quy tắc 1: Thể chủ động & Thì hiện tại (Active Voice + Present Tense)
- ✅ "Người dùng nhấn nút **Xác nhận đặt hàng**"
- ❌ "Nút **Xác nhận đặt hàng** được nhấn bởi người dùng"
- ✅ "Hệ thống hiển thị màn hình tóm tắt hóa đơn"
- ❌ "Hệ thống sẽ hiển thị màn hình tóm tắt hóa đơn"

### Quy tắc 2: Chủ ngữ rõ ràng (Subject + Verb + Object)
Mọi bước trong luồng sự kiện phải chỉ định chủ ngữ cụ thể: tên Tác nhân hoặc "Hệ thống".
- ✅ "Học viên chọn phương thức thanh toán ví điện tử"
- ❌ "Chọn phương thức thanh toán ví điện tử" (thiếu chủ thể)

### Quy tắc 3: Mỗi bước đúng một hành vi (One Step = One Action)
Mỗi bước trong Luồng chính chỉ thể hiện một hành vi duy nhất. Nếu có liên từ "và" nối hai hành vi khác bản chất -> Tách thành 2 bước riêng biệt.
- Bước nhập liệu (Input form) tách riêng với bước nhấn nút gửi (Submit trigger).

### Quy tắc 4: Không lồng ghép điều kiện rẽ nhánh (No Embedded If/Else)
Luồng sự kiện chính (Normal Course) chỉ phản ánh kịch bản thành công lý tưởng (Happy Path). Mọi điều kiện rẽ nhánh (If/Else) phải đưa sang Luồng thay thế (Alternative Course) hoặc Luồng ngoại lệ (Exceptions).

### Quy tắc 5: Độc lập với chi tiết giao diện đồ họa (UI Agnostic)
Mô tả ý định người dùng (User Intent) và kết quả hệ thống thay vì mô tả chi tiết pixel, màu sắc hay bố cục layout giao diện.
