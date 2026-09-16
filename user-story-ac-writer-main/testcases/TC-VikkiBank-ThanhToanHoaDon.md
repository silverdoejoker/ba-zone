# Test Cases – Thanh Toán Hóa Đơn · Vikki Bank

> Module: Thanh toán hóa đơn (Điện, Nước, Internet, Truyền hình, Điện thoại...)  
> App: Vikki Bank  
> Tác giả: QA Team  
> Ngày tạo: 29/05/2026

---

## TC-TTHD-001: Thanh toán hóa đơn điện thành công (Happy Path)

### 1. Objective
Kiểm tra user thanh toán hóa đơn điện thành công với số dư tài khoản đủ.

### 2. Preconditions
- User đã đăng nhập app Vikki Bank
- Tài khoản đã xác thực (eKYC hoàn tất)
- Số dư tài khoản ≥ số tiền hóa đơn
- Có hóa đơn điện chưa thanh toán (mã khách hàng hợp lệ)

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở app Vikki Bank → chọn "Thanh toán hóa đơn" | — | Màn hình danh sách loại hóa đơn hiển thị |
| 2 | Chọn loại hóa đơn "Điện" | — | Hiển thị form nhập mã khách hàng |
| 3 | Chọn nhà cung cấp "EVN Hà Nội" | — | Nhà cung cấp được chọn |
| 4 | Nhập mã khách hàng | "PE01012345678" | Hệ thống truy vấn và hiển thị thông tin hóa đơn |
| 5 | Xác nhận thông tin hóa đơn | — | Thông tin hiển thị đúng, nút "Thanh toán" active |
| 6 | Nhấn "Thanh toán" | — | Hiển thị màn hình xác nhận OTP/PIN |
| 7 | Nhập mã PIN / OTP | PIN 6 số hợp lệ | Giao dịch thành công |

### 4. Expected Result
- Hệ thống hiển thị thông báo "Thanh toán thành công"
- Số dư tài khoản bị trừ đúng số tiền hóa đơn
- Lịch sử giao dịch ghi nhận giao dịch mới với trạng thái "Thành công"
- User nhận notification xác nhận thanh toán
- Hóa đơn chuyển trạng thái "Đã thanh toán" trên hệ thống nhà cung cấp

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Mã KH | Nhà cung cấp | Số tiền | Kỳ TT |
|---|--------|--------------|---------|--------|
| 1 | PE01012345678 | EVN Hà Nội | 350,000 VND | 05/2026 |
| 2 | PE02098765432 | EVN HCM | 520,000 VND | 05/2026 |

### 7. Pass/Fail Criteria
- **Pass**: Giao dịch thành công, số dư trừ đúng, lịch sử ghi nhận, notification gửi trong ≤ 5 giây
- **Fail**: Giao dịch lỗi, số dư trừ sai, không ghi lịch sử, hoặc timeout > 30 giây

### 8. Notes
- Kiểm tra cả trường hợp thanh toán nhiều kỳ cùng lúc (nếu app hỗ trợ)
- Liên kết: US-TTHD-001

---

## TC-TTHD-002: Thanh toán hóa đơn khi số dư không đủ (Negative)

### 1. Objective
Kiểm tra hệ thống xử lý đúng khi user thanh toán hóa đơn nhưng số dư tài khoản không đủ.

### 2. Preconditions
- User đã đăng nhập app Vikki Bank
- Số dư tài khoản < số tiền hóa đơn (VD: dư 100,000 VND, hóa đơn 350,000 VND)
- Có hóa đơn chưa thanh toán hợp lệ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở "Thanh toán hóa đơn" → chọn "Điện" | — | Form nhập mã KH hiển thị |
| 2 | Nhập mã khách hàng hợp lệ | "PE01012345678" | Hiển thị hóa đơn 350,000 VND |
| 3 | Nhấn "Thanh toán" | — | Hệ thống kiểm tra số dư |

### 4. Expected Result
- Hệ thống hiển thị thông báo lỗi: "Số dư tài khoản không đủ. Vui lòng nạp thêm tiền."
- Giao dịch KHÔNG được thực hiện
- Số dư tài khoản KHÔNG thay đổi
- Có gợi ý nạp tiền hoặc chuyển sang nguồn thanh toán khác (nếu có)
- Không ghi nhận giao dịch lỗi vào lịch sử thanh toán thành công

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Số dư hiện tại | Số tiền hóa đơn | Chênh lệch |
|---|---------------|-----------------|------------|
| 1 | 100,000 VND | 350,000 VND | -250,000 VND |
| 2 | 0 VND | 150,000 VND | -150,000 VND |

### 7. Pass/Fail Criteria
- **Pass**: Thông báo lỗi rõ ràng, không trừ tiền, không tạo giao dịch ảo
- **Fail**: Trừ tiền dù không đủ, không hiển thị lỗi, hoặc app crash

### 8. Notes
- Kiểm tra edge case: số dư = đúng bằng số tiền hóa đơn (boundary)
- Kiểm tra khi số dư = 0

---

## TC-TTHD-003: Nhập mã khách hàng không tồn tại (Negative)

### 1. Objective
Kiểm tra hệ thống xử lý khi user nhập mã khách hàng không hợp lệ hoặc không tồn tại.

### 2. Preconditions
- User đã đăng nhập app Vikki Bank
- Đã chọn loại hóa đơn và nhà cung cấp

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Chọn "Thanh toán hóa đơn" → "Điện" → "EVN Hà Nội" | — | Form nhập mã KH hiển thị |
| 2 | Nhập mã khách hàng không tồn tại | "XX00000000000" | Hệ thống truy vấn nhà cung cấp |
| 3 | Chờ kết quả | — | Thông báo lỗi hiển thị |

### 4. Expected Result
- Hiển thị thông báo: "Không tìm thấy thông tin khách hàng. Vui lòng kiểm tra lại mã."
- Không cho phép tiếp tục bước thanh toán
- Nút "Thanh toán" ở trạng thái disabled
- Response time thông báo lỗi ≤ 5 giây

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Mã KH nhập | Loại lỗi | Expected Message |
|---|-----------|-----------|-----------------|
| 1 | XX00000000000 | Không tồn tại | "Không tìm thấy thông tin khách hàng" |
| 2 | (để trống) | Empty input | "Vui lòng nhập mã khách hàng" |
| 3 | ABC!@# | Ký tự đặc biệt | "Mã khách hàng không hợp lệ" |
| 4 | 12 | Quá ngắn | "Mã khách hàng phải có ít nhất X ký tự" |

### 7. Pass/Fail Criteria
- **Pass**: Thông báo lỗi chính xác theo từng loại input sai, không crash, không cho thanh toán
- **Fail**: App crash, cho phép thanh toán với mã sai, hoặc không hiển thị lỗi

### 8. Notes
- Test thêm SQL injection: `' OR 1=1 --`
- Test Unicode: mã KH chứa tiếng Việt có dấu

---

## TC-TTHD-004: Thanh toán hóa đơn khi mất kết nối mạng (Edge Case)

### 1. Objective
Kiểm tra hệ thống xử lý khi mất kết nối internet giữa quá trình thanh toán.

### 2. Preconditions
- User đã đăng nhập, đã nhập mã KH và xác nhận thông tin hóa đơn
- Số dư đủ thanh toán
- Chuẩn bị tắt WiFi/4G giữa chừng

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Thực hiện các bước thanh toán đến bước nhập PIN | — | Màn hình nhập PIN hiển thị |
| 2 | Tắt WiFi/4G trước khi nhấn xác nhận | — | Mất kết nối |
| 3 | Nhập PIN và nhấn xác nhận | PIN hợp lệ | Hệ thống xử lý timeout |

### 4. Expected Result
- Hiển thị thông báo: "Mất kết nối mạng. Vui lòng kiểm tra và thử lại."
- Giao dịch KHÔNG được thực hiện (hoặc ở trạng thái Pending)
- Số dư KHÔNG bị trừ khi giao dịch chưa hoàn tất
- Khi có mạng lại → user có thể kiểm tra trạng thái giao dịch
- Không tạo giao dịch trùng lặp (duplicate transaction)

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data
- Thời điểm ngắt mạng: sau khi nhấn "Xác nhận" nhưng trước khi server response
- Thời gian timeout: quan sát app chờ bao lâu trước khi báo lỗi

### 7. Pass/Fail Criteria
- **Pass**: Thông báo lỗi mạng rõ ràng, không trừ tiền sai, không duplicate, có thể retry
- **Fail**: Trừ tiền nhưng không ghi nhận, tạo giao dịch trùng, app crash/freeze

### 8. Notes
- Critical case: kiểm tra idempotency — retry không tạo 2 giao dịch
- Kiểm tra trạng thái "Pending" có tự resolve sau khi có mạng không

---

## TC-TTHD-005: Thanh toán hóa đơn nước thành công (Happy Path - loại hóa đơn khác)

### 1. Objective
Kiểm tra thanh toán hóa đơn nước hoạt động đúng (verify multi-provider support).

### 2. Preconditions
- User đã đăng nhập, eKYC hoàn tất
- Số dư ≥ số tiền hóa đơn nước
- Có hóa đơn nước chưa thanh toán

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Chọn "Thanh toán hóa đơn" → "Nước" | — | Danh sách nhà cung cấp nước hiển thị |
| 2 | Chọn "Nước sạch Hà Nội" | — | Form nhập mã KH |
| 3 | Nhập mã khách hàng | "HN2026051234" | Hiển thị hóa đơn: 180,000 VND |
| 4 | Xác nhận và nhập PIN | PIN hợp lệ | Thanh toán thành công |

### 4. Expected Result
- Thông báo "Thanh toán thành công"
- Số dư trừ đúng 180,000 VND
- Lịch sử ghi nhận: loại = "Hóa đơn nước", nhà CC = "Nước sạch Hà Nội"
- Notification push trong ≤ 5 giây

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Mã KH | Nhà cung cấp | Số tiền |
|---|--------|--------------|---------|
| 1 | HN2026051234 | Nước sạch Hà Nội | 180,000 VND |
| 2 | HCM2026067890 | Sawaco HCM | 220,000 VND |

### 7. Pass/Fail Criteria
- **Pass**: Thanh toán thành công, đúng nhà cung cấp, đúng số tiền
- **Fail**: Sai nhà cung cấp, sai số tiền, hoặc không hỗ trợ loại hóa đơn nước

### 8. Notes
- Verify danh sách nhà cung cấp nước đầy đủ theo vùng miền

---

## TC-TTHD-PERF-001: Performance Test – Thanh toán hóa đơn dưới tải cao

### 1. Objective
Đo lường hiệu năng luồng thanh toán hóa đơn khi nhiều user thanh toán đồng thời (peak cuối tháng).

### 2. Preconditions
- Môi trường: Staging (cấu hình tương đương production)
- Database: ≥ 50,000 hóa đơn chưa thanh toán
- Kết nối nhà cung cấp: sandbox EVN, Nước, Internet
- Tool đo: JMeter / k6
- Baseline sprint trước đã ghi nhận

### 3. Test Scenarios

| # | Scenario | Load Condition | Threshold (SLA) |
|---|----------|---------------|-----------------|
| 1 | Thanh toán hóa đơn – single user | 1 user, 1 hóa đơn | End-to-end ≤ 10 giây |
| 2 | Tra cứu mã KH (lookup) | 100 requests/giây | Response ≤ 3 giây (P95) |
| 3 | Thanh toán concurrent – peak cuối tháng | 200 users đồng thời | ≤ 15 giây (P95), error < 1% |
| 4 | Thanh toán nhiều loại hóa đơn cùng lúc | 100 users, mix Điện/Nước/Internet | ≤ 15 giây (P95) |
| 5 | Sustained load 30 phút (mô phỏng peak) | 150 users liên tục | Stable, no degradation |

### 4. Metrics cần đo

| Metric | Mô tả | Ngưỡng Pass |
|--------|--------|-------------|
| Lookup Response (P95) | Tra cứu mã KH → hiển thị hóa đơn | ≤ 3 giây |
| Payment Response (P95) | Từ nhấn "Thanh toán" → thành công | ≤ 10 giây |
| Payment Response (P99) | 99th percentile | ≤ 15 giây |
| Throughput | Giao dịch thanh toán/giây | ≥ 20 TPS |
| Error Rate | % giao dịch lỗi (không tính lỗi business) | < 1% |
| Provider API Latency | Thời gian gọi API nhà cung cấp | < 5 giây |
| CPU / Memory | Server resource | < 80% |

### 5. Pass/Fail Criteria
- **Pass**: Tất cả metrics trong ngưỡng, không timeout hàng loạt, không mất giao dịch
- **Fail**: Response > SLA, error > 1%, hoặc provider connection pool exhausted
- **Warning**: Latency tăng > 30% so với baseline nhưng vẫn trong SLA

### 6. Notes
- Peak thanh toán hóa đơn thường vào ngày 25-30 hàng tháng
- Provider API có thể chậm vào peak → cần test với simulated latency
- Kiểm tra circuit breaker khi provider API down
- Đính kèm: JMeter report, resource monitoring dashboard

---

## TC-TTHD-PERF-002: Performance Test – Tra cứu hóa đơn (Provider Lookup)

### 1. Objective
Đo lường thời gian tra cứu thông tin hóa đơn từ nhà cung cấp (EVN, Nước, Internet) dưới tải.

### 2. Preconditions
- Kết nối sandbox các nhà cung cấp
- Tool đo: k6 / JMeter

### 3. Test Scenarios

| # | Provider | Load | Threshold |
|---|----------|------|-----------|
| 1 | EVN Hà Nội | 50 concurrent lookups | ≤ 3 giây (P95) |
| 2 | EVN HCM | 50 concurrent lookups | ≤ 3 giây (P95) |
| 3 | Nước sạch Hà Nội | 30 concurrent lookups | ≤ 5 giây (P95) |
| 4 | FPT Internet | 30 concurrent lookups | ≤ 3 giây (P95) |
| 5 | Mixed providers | 100 concurrent (random) | ≤ 5 giây (P95) |

### 4. Pass/Fail Criteria
- **Pass**: Tất cả provider response trong SLA, cache hoạt động đúng
- **Fail**: Provider timeout hàng loạt, response > 10 giây, hoặc trả sai data

### 5. Notes
- Kiểm tra caching: lookup cùng mã KH lần 2 phải nhanh hơn lần 1
- Kiểm tra fallback khi 1 provider down (circuit breaker)
- Provider có thể rate-limit → test với realistic rate

---

## TC-TTHD-REG-001: Regression Test – Thanh toán hóa đơn sau deploy

### 1. Objective
Xác nhận toàn bộ luồng thanh toán hóa đơn vẫn hoạt động đúng sau khi deploy code mới.

### 2. Preconditions
- Build mới đã deploy lên staging
- Thay đổi liên quan: [ghi rõ change log]
- Kết nối sandbox nhà cung cấp available
- Golden dataset đã chuẩn bị

### 3. Regression Scope

| # | Feature/Flow | Liên quan change? | Priority |
|---|-------------|-------------------|----------|
| 1 | Thanh toán hóa đơn điện (EVN) | Kiểm tra mọi deploy | P1 |
| 2 | Thanh toán hóa đơn nước | Kiểm tra mọi deploy | P1 |
| 3 | Tra cứu mã KH (lookup) | Trực tiếp nếu đổi API | P1 |
| 4 | Xử lý số dư không đủ | Gián tiếp | P2 |
| 5 | Mã KH không tồn tại | Gián tiếp | P2 |
| 6 | Mất kết nối giữa chừng | Gián tiếp | P3 |
| 7 | Notification sau thanh toán | Gián tiếp | P2 |
| 8 | Lịch sử giao dịch | Gián tiếp | P2 |

### 4. Golden Dataset (Regression Baseline)

| # | Scenario | Input | Expected (Baseline) | Sprint |
|---|----------|-------|---------------------|--------|
| 1 | TT điện EVN HN thành công | Mã PE01012345678, 350K | Thành công, trừ đúng | Sprint 2 |
| 2 | TT nước HN thành công | Mã HN2026051234, 180K | Thành công, trừ đúng | Sprint 3 |
| 3 | Mã KH không tồn tại | Mã XX00000000000 | Báo lỗi "Không tìm thấy" | Sprint 2 |
| 4 | Số dư không đủ | Dư 100K, hóa đơn 350K | Chặn, báo "Số dư không đủ" | Sprint 2 |
| 5 | Thanh toán Internet FPT | Mã hợp lệ, 200K | Thành công | Sprint 3 |
| 6 | Mã KH chứa ký tự đặc biệt | "ABC!@#" | Báo lỗi format | Sprint 3 |

### 5. Pass/Fail Criteria
- **Pass**: 100% golden dataset cho kết quả đúng baseline
- **Fail**: Bất kỳ scenario nào fail mà trước đó pass
- **Acceptable Change**: Thêm provider mới, message text thay đổi nhỏ → update baseline

### 6. Quy trình khi Regression Fail
1. Log bug với tag [Regression][Thanh toán hóa đơn]
2. Xác định provider nào bị ảnh hưởng
3. Kiểm tra: lỗi do code change hay provider API thay đổi?
4. Quyết định: rollback / hotfix / liên hệ provider

### 7. Notes
- Chạy regression sau mỗi deploy staging
- Đặc biệt chú ý khi thêm/sửa provider integration
- Golden dataset cần update khi thêm nhà cung cấp mới
- Automate bằng Postman collection + Newman CLI

---

## TC-TTHD-REG-002: Regression Test – Multi-provider support sau khi thêm provider mới

### 1. Objective
Xác nhận các provider cũ (EVN, Nước, Internet) vẫn hoạt động đúng sau khi integrate thêm provider mới.

### 2. Preconditions
- Đã thêm provider mới vào hệ thống (VD: thêm Truyền hình cáp)
- Các provider cũ vẫn kết nối sandbox

### 3. Golden Dataset

| # | Provider | Mã KH test | Expected | Status |
|---|----------|-----------|----------|--------|
| 1 | EVN Hà Nội | PE01012345678 | Lookup thành công, hiển thị hóa đơn | |
| 2 | EVN HCM | PE02098765432 | Lookup thành công | |
| 3 | Nước sạch HN | HN2026051234 | Lookup thành công | |
| 4 | FPT Internet | FPT123456 | Lookup thành công | |
| 5 | Provider mới | [mã test] | Lookup thành công (verify integration) | |

### 4. Pass/Fail Criteria
- **Pass**: Tất cả provider cũ vẫn hoạt động, provider mới integrate đúng
- **Fail**: Provider cũ bị ảnh hưởng bởi code thêm provider mới

### 5. Notes
- Kiểm tra: danh sách provider hiển thị đúng thứ tự
- Kiểm tra: UI không bị vỡ khi thêm provider (scroll, layout)

---
*Vikki Bank · QA Test Cases · Thanh toán hóa đơn · Updated with Performance & Regression*
