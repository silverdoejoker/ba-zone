# Test Cases – Chuyển Tiền · Vikki Bank

> Module: Chuyển tiền (Nội bộ Vikki, Liên ngân hàng, Chuyển theo số điện thoại)  
> App: Vikki Bank  
> Tác giả: QA Team  
> Ngày tạo: 29/05/2026

---

## TC-CT-001: Chuyển tiền nội bộ Vikki Bank thành công (Happy Path)

### 1. Objective
Kiểm tra user chuyển tiền cho user khác trong cùng hệ thống Vikki Bank thành công.

### 2. Preconditions
- User A (người gửi) đã đăng nhập, eKYC hoàn tất
- Số dư tài khoản User A ≥ số tiền chuyển
- User B (người nhận) có tài khoản Vikki Bank hợp lệ, đang active

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở app → chọn "Chuyển tiền" | — | Màn hình chuyển tiền hiển thị |
| 2 | Chọn "Chuyển trong Vikki Bank" | — | Form nhập thông tin người nhận |
| 3 | Nhập số tài khoản / SĐT người nhận | "0901234567" | Hiển thị tên người nhận: "NGUYEN VAN B" |
| 4 | Nhập số tiền chuyển | 300,000 VND | Số tiền hiển thị, phí = 0 (nội bộ) |
| 5 | Nhập nội dung chuyển tiền | "Trả tiền ăn trưa" | Nội dung hiển thị |
| 6 | Nhấn "Tiếp tục" → xác nhận thông tin | — | Màn hình review: người nhận, số tiền, nội dung |
| 7 | Nhập PIN xác nhận | PIN 6 số hợp lệ | Giao dịch xử lý |

### 4. Expected Result
- Thông báo "Chuyển tiền thành công"
- Số dư User A giảm đúng 300,000 VND
- Số dư User B tăng đúng 300,000 VND (real-time)
- Lịch sử giao dịch User A: "Chuyển tiền đến NGUYEN VAN B", -300,000 VND
- Lịch sử giao dịch User B: "Nhận tiền từ [User A]", +300,000 VND
- Cả 2 user nhận notification trong ≤ 5 giây
- Thời gian xử lý giao dịch ≤ 3 giây (nội bộ = instant)

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Người gửi | Người nhận | Số tiền | Nội dung |
|---|-----------|-----------|---------|----------|
| 1 | User A (0909876543) | User B (0901234567) | 300,000 VND | "Trả tiền ăn trưa" |
| 2 | User A | User C (0912345678) | 50,000 VND (min) | "Test" |
| 3 | User A | User D (0923456789) | 50,000,000 VND (max nội bộ) | "Chuyển tiền" |

### 7. Pass/Fail Criteria
- **Pass**: Gửi thành công, nhận instant, số dư đúng cả 2 bên, lịch sử ghi nhận, notification ≤ 5s
- **Fail**: Tiền trừ nhưng không nhận, sai số tiền, delay > 30s, không notification

### 8. Notes
- Chuyển nội bộ = miễn phí, instant
- Kiểm tra chuyển cho chính mình (cùng SĐT) → phải chặn

---

## TC-CT-002: Chuyển tiền liên ngân hàng thành công (Happy Path)

### 1. Objective
Kiểm tra user chuyển tiền từ Vikki Bank sang tài khoản ngân hàng khác (Napas/IBFT).

### 2. Preconditions
- User đã đăng nhập, eKYC hoàn tất
- Số dư ≥ số tiền chuyển + phí (nếu có)
- Có thông tin TK ngân hàng người nhận hợp lệ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Chọn "Chuyển tiền" → "Liên ngân hàng" | — | Form chuyển tiền liên ngân hàng |
| 2 | Chọn ngân hàng nhận | "Vietcombank" | Ngân hàng được chọn |
| 3 | Nhập số tài khoản người nhận | "0011002233445" | Hệ thống verify tên chủ TK |
| 4 | Xác nhận tên người nhận | "TRAN VAN C" hiển thị | User xác nhận đúng người |
| 5 | Nhập số tiền | 1,000,000 VND | Hiển thị phí: 5,500 VND, tổng: 1,005,500 VND |
| 6 | Nhập nội dung | "Thanh toan don hang" | Nội dung hiển thị (không dấu nếu liên ngân hàng) |
| 7 | Xác nhận → nhập PIN/OTP | PIN hợp lệ | Giao dịch xử lý |

### 4. Expected Result
- Thông báo "Chuyển tiền thành công"
- Số dư giảm: 1,000,000 + 5,500 = 1,005,500 VND
- Lịch sử: "Chuyển tiền đến Vietcombank - TRAN VAN C", -1,005,500 VND
- Người nhận nhận tiền trong ≤ 15 phút (SLA Napas 24/7)
- Mã giao dịch (transaction ID) hiển thị để tra cứu

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Ngân hàng nhận | Số TK | Tên người nhận | Số tiền | Phí |
|---|---------------|-------|---------------|---------|-----|
| 1 | Vietcombank | 0011002233445 | TRAN VAN C | 1,000,000 | 5,500 |
| 2 | Techcombank | 19033456789 | LE THI D | 500,000 | 5,500 |
| 3 | Agribank | 4200123456789 | PHAM VAN E | 10,000,000 | 11,000 |

### 7. Pass/Fail Criteria
- **Pass**: Giao dịch thành công, phí tính đúng, người nhận nhận tiền trong SLA, có mã GD
- **Fail**: Sai phí, người nhận không nhận tiền, timeout, không có mã GD tra cứu

### 8. Notes
- Phí liên ngân hàng theo biểu phí Vikki Bank (có thể thay đổi theo chương trình KM)
- Kiểm tra chuyển ngoài giờ hành chính: Napas 24/7 vs IBFT giờ hành chính
- Nội dung chuyển tiền liên ngân hàng thường không hỗ trợ Unicode có dấu

---

## TC-CT-003: Chuyển tiền vượt hạn mức ngày (Edge Case)

### 1. Objective
Kiểm tra hệ thống chặn giao dịch khi user chuyển tiền vượt hạn mức trong ngày.

### 2. Preconditions
- User đã đăng nhập
- Đã chuyển tiền gần đạt hạn mức ngày (VD: hạn mức 100,000,000/ngày, đã chuyển 95,000,000)
- Số dư tài khoản vẫn đủ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Thực hiện chuyển tiền | — | Form chuyển tiền |
| 2 | Nhập số tiền vượt hạn mức còn lại | 10,000,000 VND (vượt 5M) | Hệ thống kiểm tra hạn mức |

### 4. Expected Result
- Thông báo: "Bạn đã vượt hạn mức chuyển tiền trong ngày. Hạn mức còn lại: 5,000,000 VND"
- Không cho phép tiếp tục giao dịch
- Hiển thị thông tin: hạn mức ngày, đã sử dụng, còn lại
- Gợi ý: "Hạn mức sẽ reset vào 00:00 ngày mai" hoặc "Nâng hạn mức tại..."

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Hạn mức ngày | Đã dùng | Số tiền chuyển | Hạn mức còn |
|---|-------------|---------|---------------|-------------|
| 1 | 100,000,000 | 95,000,000 | 10,000,000 | 5,000,000 |
| 2 | 100,000,000 | 100,000,000 | 100,000 | 0 |
| 3 | 100,000,000 | 95,000,000 | 5,000,000 | 5,000,000 (boundary - phải pass) |

### 7. Pass/Fail Criteria
- **Pass**: Chặn khi vượt, thông báo hạn mức rõ, boundary case (= hạn mức) vẫn pass
- **Fail**: Cho chuyển vượt hạn mức, không thông báo, hoặc chặn sai boundary

### 8. Notes
- Hạn mức có thể khác nhau theo loại: nội bộ vs liên ngân hàng
- Hạn mức theo cấp xác thực eKYC
- Kiểm tra reset hạn mức lúc 00:00

---

## TC-CT-004: Chuyển tiền đến số tài khoản không tồn tại (Negative)

### 1. Objective
Kiểm tra hệ thống xử lý khi user nhập số tài khoản người nhận không tồn tại.

### 2. Preconditions
- User đã đăng nhập
- Đã chọn ngân hàng nhận

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Chọn "Chuyển tiền" → "Liên ngân hàng" → "Vietcombank" | — | Form nhập số TK |
| 2 | Nhập số TK không tồn tại | "9999999999999" | Hệ thống verify với ngân hàng |
| 3 | Chờ kết quả verify | — | Thông báo lỗi |

### 4. Expected Result
- Thông báo: "Không tìm thấy tài khoản. Vui lòng kiểm tra lại số tài khoản và ngân hàng."
- Không cho phép tiếp tục nhập số tiền
- Không hiển thị tên người nhận
- Response time verify ≤ 10 giây

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Số TK nhập | Ngân hàng | Loại lỗi |
|---|-----------|-----------|-----------|
| 1 | 9999999999999 | Vietcombank | TK không tồn tại |
| 2 | (để trống) | Vietcombank | Empty input |
| 3 | ABC123 | Vietcombank | Format sai (chứa chữ) |
| 4 | 12 | Vietcombank | Quá ngắn |
| 5 | 0901234567 (SĐT) | Vietcombank | Nhầm SĐT thành số TK |

### 7. Pass/Fail Criteria
- **Pass**: Thông báo lỗi chính xác, không cho chuyển, không trừ tiền
- **Fail**: Cho chuyển đến TK không tồn tại, trừ tiền mất, app crash

### 8. Notes
- Critical: tiền chuyển đến TK không tồn tại phải được hoàn trả (nếu lọt qua verify)
- Kiểm tra SQL injection trong field số TK

---

## TC-CT-005: Chuyển tiền khi nhập sai PIN 3 lần (Edge Case - Security)

### 1. Objective
Kiểm tra cơ chế bảo mật khi user nhập sai PIN nhiều lần trong quá trình chuyển tiền.

### 2. Preconditions
- User đã đăng nhập
- Đã điền đầy đủ thông tin chuyển tiền, đến bước nhập PIN

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Đến bước nhập PIN xác nhận chuyển tiền | — | Màn hình nhập PIN |
| 2 | Nhập sai PIN lần 1 | "000000" | "PIN không đúng. Còn 4 lần thử" |
| 3 | Nhập sai PIN lần 2 | "111111" | "PIN không đúng. Còn 3 lần thử" |
| 4 | Nhập sai PIN lần 3 | "222222" | "PIN không đúng. Còn 2 lần thử" |
| 5 | Nhập sai PIN lần 4 | "333333" | "PIN không đúng. Còn 1 lần thử" |
| 6 | Nhập sai PIN lần 5 | "444444" | Khóa giao dịch |

### 4. Expected Result
- Sau 5 lần sai: Khóa chức năng chuyển tiền tạm thời (30 phút)
- Thông báo: "Bạn đã nhập sai PIN 5 lần. Chức năng chuyển tiền tạm khóa 30 phút."
- Giao dịch hiện tại bị hủy
- Notification cảnh báo bảo mật gửi đến user
- Số dư KHÔNG bị trừ
- Các chức năng khác (xem số dư, lịch sử) vẫn hoạt động

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data
- PIN đúng: "654321" (không dùng)
- 5 PIN sai: "000000", "111111", "222222", "333333", "444444"

### 7. Pass/Fail Criteria
- **Pass**: Khóa sau 5 lần, hủy GD, notification bảo mật, không trừ tiền, unlock sau 30 phút
- **Fail**: Không khóa, cho thử vô hạn, trừ tiền dù PIN sai, khóa toàn bộ app

### 8. Notes
- Kiểm tra: sau 30 phút → nhập đúng PIN → chuyển tiền thành công
- Kiểm tra: nhập đúng PIN ở lần thứ 4 → reset counter, GD thành công

---

## TC-CT-006: Chuyển tiền theo số điện thoại (Happy Path)

### 1. Objective
Kiểm tra chuyển tiền bằng số điện thoại người nhận (không cần biết số TK).

### 2. Preconditions
- User đã đăng nhập
- Người nhận đã đăng ký nhận tiền qua SĐT trên Vikki Bank
- Số dư đủ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Chọn "Chuyển tiền" → "Theo số điện thoại" | — | Form nhập SĐT |
| 2 | Nhập SĐT người nhận | "0901234567" | Hiển thị tên: "NGUYEN VAN B" (mask: N****B) |
| 3 | Xác nhận người nhận | — | Đúng người, tiếp tục |
| 4 | Nhập số tiền | 200,000 VND | Phí = 0 (nội bộ) |
| 5 | Nhập nội dung | "Gửi bạn" | OK |
| 6 | Xác nhận PIN | PIN hợp lệ | Thành công |

### 4. Expected Result
- Chuyển tiền thành công, instant
- Người nhận nhận tiền vào TK mặc định liên kết với SĐT
- Tên người nhận hiển thị dạng mask để bảo mật (N**** B)
- Lịch sử ghi nhận đúng

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | SĐT người nhận | Tên (mask) | Số tiền |
|---|----------------|-----------|---------|
| 1 | 0901234567 | N****B | 200,000 |
| 2 | 0912345678 | T****D | 1,000,000 |

### 7. Pass/Fail Criteria
- **Pass**: Chuyển thành công qua SĐT, tên mask đúng, instant, lịch sử ghi nhận
- **Fail**: Không tìm thấy SĐT dù đã đăng ký, chuyển nhầm người, delay

### 8. Notes
- Kiểm tra SĐT chưa đăng ký Vikki → thông báo "SĐT chưa đăng ký nhận tiền"
- Kiểm tra chuyển cho chính mình (cùng SĐT) → chặn

---

## TC-CT-007: Chuyển tiền với nội dung chứa ký tự đặc biệt (Edge Case)

### 1. Objective
Kiểm tra hệ thống xử lý nội dung chuyển tiền chứa ký tự đặc biệt, emoji, Unicode.

### 2. Preconditions
- User đã đăng nhập
- Thông tin người nhận và số tiền hợp lệ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Điền thông tin chuyển tiền hợp lệ | — | OK |
| 2 | Nhập nội dung chứa ký tự đặc biệt | Xem Test Data | Hệ thống validate |

### 4. Expected Result
- Ký tự đặc biệt bị filter hoặc thông báo "Nội dung chỉ chấp nhận chữ cái và số"
- Emoji bị loại bỏ hoặc báo lỗi
- Không gây lỗi hệ thống / crash
- Nội dung hợp lệ (chữ + số + dấu cách) → chấp nhận bình thường

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Nội dung nhập | Expected |
|---|--------------|----------|
| 1 | "Tra tien an trua" | Chấp nhận ✅ |
| 2 | "Trả tiền ăn trưa 🍜" | Filter emoji hoặc báo lỗi |
| 3 | "<script>alert('xss')</script>" | Chặn, không execute |
| 4 | "' OR 1=1 --" | Chặn injection |
| 5 | "" (để trống) | Chấp nhận (nội dung không bắt buộc) hoặc default text |
| 6 | 500 ký tự liên tục | Giới hạn max length, cắt hoặc báo lỗi |

### 7. Pass/Fail Criteria
- **Pass**: Filter/chặn ký tự nguy hiểm, không crash, không XSS/injection
- **Fail**: App crash, execute script, SQL injection thành công, hiển thị sai

### 8. Notes
- Liên ngân hàng thường chỉ chấp nhận ASCII không dấu
- Nội bộ Vikki có thể chấp nhận Unicode tiếng Việt có dấu
- Max length nội dung: thường 140-210 ký tự

---

## TC-CT-PERF-001: Performance Test – Chuyển tiền nội bộ dưới tải cao

### 1. Objective
Đo lường hiệu năng hệ thống chuyển tiền nội bộ Vikki Bank dưới điều kiện tải cao (concurrent users).

### 2. Preconditions
- Môi trường: Staging (cấu hình tương đương production)
- Database: ≥ 100,000 tài khoản active
- Tool đo: JMeter / k6 / Gatling
- Baseline đã ghi nhận từ sprint trước

### 3. Test Scenarios

| # | Scenario | Load Condition | Threshold (SLA) |
|---|----------|---------------|-----------------|
| 1 | Chuyển tiền nội bộ – single user | 1 user, 1 request | Response ≤ 3 giây end-to-end |
| 2 | Chuyển tiền nội bộ – concurrent | 100 users đồng thời | Response ≤ 5 giây (P95) |
| 3 | Chuyển tiền nội bộ – peak load | 500 users đồng thời | Response ≤ 8 giây (P95), error < 1% |
| 4 | Verify tên người nhận (name lookup) | 200 requests/giây | Response ≤ 2 giây (P95) |
| 5 | Sustained load 15 phút | 100 users liên tục | Stable response, no memory leak |

### 4. Metrics cần đo

| Metric | Mô tả | Ngưỡng Pass |
|--------|--------|-------------|
| Response Time (P50) | Median thời gian hoàn tất GD | ≤ 2 giây |
| Response Time (P95) | 95th percentile | ≤ 5 giây |
| Response Time (P99) | 99th percentile | ≤ 8 giây |
| Throughput | Giao dịch thành công/giây | ≥ 50 TPS |
| Error Rate | % giao dịch lỗi | < 1% |
| CPU Usage (server) | Tải CPU | < 80% |
| Memory Usage | RAM server | < 80%, no leak |
| DB Connection Pool | Số connection active | < 80% pool size |

### 5. Pass/Fail Criteria
- **Pass**: Tất cả metrics trong ngưỡng SLA, không có error spike, không memory leak
- **Fail**: Bất kỳ metric vượt ngưỡng, error rate > 1%, hoặc system crash
- **Warning**: Response tăng > 50% so với baseline nhưng vẫn trong SLA

### 6. Notes
- Đặc biệt chú ý: race condition khi 2 user chuyển tiền cho nhau cùng lúc
- Kiểm tra deadlock trên DB khi concurrent update balance
- So sánh kết quả với baseline sprint trước
- Đính kèm report: JMeter HTML report / k6 summary

---

## TC-CT-PERF-002: Performance Test – Chuyển tiền liên ngân hàng (Napas)

### 1. Objective
Đo lường hiệu năng luồng chuyển tiền liên ngân hàng qua Napas/IBFT dưới tải.

### 2. Preconditions
- Môi trường: Staging kết nối Napas sandbox
- Tool đo: JMeter / k6
- SLA Napas: response ≤ 15 giây cho 1 giao dịch

### 3. Test Scenarios

| # | Scenario | Load Condition | Threshold (SLA) |
|---|----------|---------------|-----------------|
| 1 | Chuyển liên ngân hàng – single | 1 user | End-to-end ≤ 15 giây |
| 2 | Chuyển liên ngân hàng – concurrent | 50 users đồng thời | ≤ 20 giây (P95) |
| 3 | Name lookup liên ngân hàng | 100 requests/giây | ≤ 5 giây (P95) |
| 4 | Peak hour simulation | 200 users, 5 phút | Error < 2%, no timeout |

### 4. Metrics cần đo

| Metric | Ngưỡng Pass |
|--------|-------------|
| Response Time (P95) | ≤ 15 giây (phụ thuộc Napas) |
| Timeout Rate | < 2% |
| Retry Success Rate | > 95% (auto-retry khi Napas timeout) |
| Queue Depth | < 1000 pending transactions |

### 5. Pass/Fail Criteria
- **Pass**: GD hoàn tất trong SLA Napas, retry mechanism hoạt động, không mất tiền
- **Fail**: Timeout > 5%, tiền trừ nhưng không đến người nhận, queue overflow

### 6. Notes
- Napas có thể chậm hơn vào peak hours (11h-13h, 17h-19h)
- Kiểm tra cơ chế retry & reconciliation khi Napas timeout
- Verify: tiền không bị trừ 2 lần khi retry

---

## TC-CT-REG-001: Regression Test – Chuyển tiền nội bộ sau deploy

### 1. Objective
Xác nhận luồng chuyển tiền nội bộ Vikki Bank vẫn hoạt động đúng sau khi deploy code mới.

### 2. Preconditions
- Build mới đã deploy lên staging
- Thay đổi liên quan: [ghi rõ change log của sprint]
- Sử dụng bộ test data regression chuẩn (golden dataset)

### 3. Regression Scope

| # | Feature/Flow | Liên quan change? | Priority |
|---|-------------|-------------------|----------|
| 1 | Chuyển nội bộ – happy path | Kiểm tra mọi deploy | P1 |
| 2 | Verify tên người nhận | Trực tiếp nếu đổi API | P1 |
| 3 | Tính phí (nội bộ = 0) | Gián tiếp | P2 |
| 4 | Hạn mức ngày | Trực tiếp nếu đổi config | P1 |
| 5 | Notification sau GD | Gián tiếp | P2 |
| 6 | Lịch sử giao dịch | Gián tiếp | P2 |

### 4. Golden Dataset (Regression Baseline)

| # | Scenario | Input | Expected (Baseline) | Sprint ghi nhận |
|---|----------|-------|---------------------|-----------------|
| 1 | Chuyển 300K nội bộ | User A → User B, 300,000 VND | Thành công, instant, phí 0 | Sprint 3 |
| 2 | Chuyển min amount | User A → User C, 50,000 VND | Thành công | Sprint 3 |
| 3 | Chuyển max amount | User A → User D, 50,000,000 VND | Thành công | Sprint 3 |
| 4 | Chuyển vượt hạn mức | Đã dùng 100M, chuyển thêm 1M | Chặn, thông báo hạn mức | Sprint 4 |
| 5 | TK người nhận không tồn tại | SĐT "0999999999" | Báo lỗi "Không tìm thấy" | Sprint 3 |
| 6 | Sai PIN 5 lần | 5 PIN sai liên tiếp | Khóa 30 phút | Sprint 4 |

### 5. Pass/Fail Criteria
- **Pass**: 100% golden dataset trả kết quả đúng baseline
- **Fail**: Bất kỳ scenario nào cho kết quả khác baseline theo hướng xấu
- **Acceptable Change**: Kết quả khác nhưng TỐT HƠN → update baseline

### 6. Quy trình khi Regression Fail
1. Log bug với tag [Regression][Chuyển tiền]
2. Link đến TC regression bị fail
3. So sánh: baseline vs actual
4. Đánh giá impact: 1 case hay pattern rộng?
5. Quyết định: rollback / hotfix / accept

### 7. Notes
- Chạy regression suite sau MỖI lần deploy staging
- Golden dataset review & update mỗi sprint
- Ưu tiên automate bằng API test script (Postman collection / k6)

---

## TC-CT-REG-002: Regression Test – Chuyển tiền liên ngân hàng sau deploy

### 1. Objective
Xác nhận luồng chuyển tiền liên ngân hàng (Napas) vẫn hoạt động đúng sau deploy.

### 2. Preconditions
- Build mới đã deploy staging
- Napas sandbox available
- Golden dataset liên ngân hàng đã chuẩn bị

### 3. Golden Dataset (Regression Baseline)

| # | Scenario | Input | Expected (Baseline) | Sprint |
|---|----------|-------|---------------------|--------|
| 1 | Chuyển 1M → Vietcombank | TK hợp lệ, 1,000,000 VND | Thành công, phí 5,500 | Sprint 3 |
| 2 | Chuyển 500K → Techcombank | TK hợp lệ, 500,000 VND | Thành công, phí 5,500 | Sprint 3 |
| 3 | TK không tồn tại | TK "9999999999999" | Báo lỗi, không trừ tiền | Sprint 3 |
| 4 | Nội dung Unicode | "Trả tiền" (có dấu) | Convert sang không dấu hoặc chặn | Sprint 4 |
| 5 | Phí tính đúng theo biểu phí | Các mức: <500K, 500K-2M, >2M | Phí đúng từng mức | Sprint 4 |

### 4. Pass/Fail Criteria
- **Pass**: Tất cả golden dataset đúng baseline, phí tính chính xác
- **Fail**: Sai phí, GD lỗi mà trước đó pass, hoặc tiền mất

### 5. Notes
- Đặc biệt chú ý khi update biểu phí → cần update golden dataset tương ứng
- Kiểm tra cả flow retry khi Napas timeout

---
*Vikki Bank · QA Test Cases · Chuyển tiền · Updated with Performance & Regression*
