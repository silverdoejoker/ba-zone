# Test Cases – Ví Điện Tử · Vikki Bank

> Module: Ví điện tử (Nạp tiền, Rút tiền, Quản lý ví, Liên kết ngân hàng)  
> App: Vikki Bank  
> Tác giả: QA Team  
> Ngày tạo: 29/05/2026

---

## TC-VDT-001: Nạp tiền vào ví từ tài khoản ngân hàng liên kết (Happy Path)

### 1. Objective
Kiểm tra user nạp tiền từ tài khoản ngân hàng đã liên kết vào ví điện tử thành công.

### 2. Preconditions
- User đã đăng nhập app Vikki Bank
- Đã liên kết ít nhất 1 tài khoản ngân hàng
- Số dư tài khoản ngân hàng liên kết ≥ số tiền muốn nạp
- Ví điện tử đã được kích hoạt

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở app → chọn "Ví điện tử" | — | Màn hình ví hiển thị số dư hiện tại |
| 2 | Nhấn "Nạp tiền" | — | Hiển thị form nạp tiền |
| 3 | Chọn nguồn tiền: TK ngân hàng liên kết | "Vietcombank *1234" | Nguồn tiền được chọn |
| 4 | Nhập số tiền nạp | 500,000 VND | Số tiền hiển thị đúng, nút "Tiếp tục" active |
| 5 | Nhấn "Tiếp tục" → xác nhận thông tin | — | Màn hình xác nhận: nguồn, số tiền, phí |
| 6 | Nhập PIN xác nhận | PIN 6 số hợp lệ | Giao dịch xử lý |

### 4. Expected Result
- Thông báo "Nạp tiền thành công"
- Số dư ví tăng đúng 500,000 VND
- Số dư TK ngân hàng giảm tương ứng (+ phí nếu có)
- Lịch sử giao dịch ví ghi nhận: "Nạp tiền từ Vietcombank", +500,000 VND
- Notification push xác nhận trong ≤ 5 giây
- Thời gian xử lý giao dịch ≤ 10 giây

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Nguồn nạp | Số tiền | Phí dự kiến | Tổng trừ TK |
|---|-----------|---------|-------------|-------------|
| 1 | Vietcombank *1234 | 500,000 VND | 0 VND | 500,000 VND |
| 2 | Techcombank *5678 | 1,000,000 VND | 0 VND | 1,000,000 VND |
| 3 | BIDV *9012 | 50,000 VND (min) | 0 VND | 50,000 VND |

### 7. Pass/Fail Criteria
- **Pass**: Số dư ví tăng đúng, TK ngân hàng trừ đúng, lịch sử ghi nhận, thời gian ≤ 10s
- **Fail**: Số dư sai, không ghi lịch sử, timeout > 30s, hoặc trừ tiền nhưng ví không tăng

### 8. Notes
- Kiểm tra min/max nạp tiền theo policy (VD: min 50,000 – max 50,000,000)
- Kiểm tra nạp tiền ngoài giờ hành chính

---

## TC-VDT-002: Nạp tiền vượt hạn mức ví (Edge Case)

### 1. Objective
Kiểm tra hệ thống xử lý khi user nạp tiền vượt hạn mức tối đa của ví điện tử.

### 2. Preconditions
- User đã đăng nhập, ví đã kích hoạt
- Số dư ví hiện tại gần hạn mức tối đa (VD: hạn mức 20,000,000 VND, dư hiện tại 19,500,000 VND)
- TK ngân hàng liên kết có đủ tiền

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở "Ví điện tử" → "Nạp tiền" | — | Form nạp tiền hiển thị |
| 2 | Nhập số tiền vượt hạn mức còn lại | 1,000,000 VND (vượt 500K) | Hệ thống kiểm tra hạn mức |

### 4. Expected Result
- Hiển thị thông báo: "Số tiền nạp vượt hạn mức ví. Hạn mức còn lại: 500,000 VND"
- Không cho phép tiếp tục giao dịch
- Gợi ý nâng cấp hạn mức (nếu có tính năng)
- Số dư ví KHÔNG thay đổi

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Hạn mức ví | Dư hiện tại | Số tiền nạp | Hạn mức còn lại |
|---|-----------|-------------|-------------|-----------------|
| 1 | 20,000,000 | 19,500,000 | 1,000,000 | 500,000 |
| 2 | 20,000,000 | 20,000,000 | 100,000 | 0 |

### 7. Pass/Fail Criteria
- **Pass**: Chặn giao dịch, thông báo hạn mức rõ ràng, không trừ tiền TK ngân hàng
- **Fail**: Cho nạp vượt hạn mức, trừ tiền TK nhưng ví không nhận, app crash

### 8. Notes
- Kiểm tra boundary: nạp đúng bằng hạn mức còn lại → phải thành công
- Verify hạn mức theo cấp xác thực (eKYC level 1 vs level 2)

---

## TC-VDT-003: Rút tiền từ ví về tài khoản ngân hàng (Happy Path)

### 1. Objective
Kiểm tra user rút tiền từ ví điện tử về tài khoản ngân hàng liên kết thành công.

### 2. Preconditions
- User đã đăng nhập, ví đã kích hoạt
- Số dư ví ≥ số tiền muốn rút
- Đã liên kết TK ngân hàng nhận tiền

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở "Ví điện tử" → "Rút tiền" | — | Form rút tiền hiển thị |
| 2 | Chọn TK ngân hàng nhận | "Vietcombank *1234" | TK nhận được chọn |
| 3 | Nhập số tiền rút | 200,000 VND | Hiển thị phí rút (nếu có), tổng trừ ví |
| 4 | Xác nhận → nhập PIN | PIN hợp lệ | Giao dịch xử lý |

### 4. Expected Result
- Thông báo "Rút tiền thành công. Tiền sẽ về TK trong 1-5 phút"
- Số dư ví giảm đúng (200,000 + phí)
- Lịch sử ví ghi nhận: "Rút tiền về Vietcombank", -200,000 VND
- TK ngân hàng nhận tiền trong ≤ 5 phút (hoặc theo SLA)

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Số dư ví | Số tiền rút | Phí | TK nhận |
|---|---------|-------------|-----|---------|
| 1 | 1,000,000 | 200,000 | 0 | Vietcombank *1234 |
| 2 | 500,000 | 500,000 (max = dư) | 0 | Techcombank *5678 |

### 7. Pass/Fail Criteria
- **Pass**: Ví trừ đúng, TK nhận tiền đúng trong SLA, lịch sử ghi nhận
- **Fail**: Ví trừ nhưng TK không nhận, sai số tiền, timeout

### 8. Notes
- Kiểm tra thời gian nhận tiền thực tế vs SLA cam kết
- Kiểm tra rút tiền ngoài giờ hành chính (có thể delay T+1)

---

## TC-VDT-004: Rút tiền khi số dư ví không đủ (Negative)

### 1. Objective
Kiểm tra hệ thống chặn rút tiền khi số dư ví không đủ.

### 2. Preconditions
- User đã đăng nhập
- Số dư ví < số tiền muốn rút (VD: dư 50,000, muốn rút 200,000)

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở "Ví điện tử" → "Rút tiền" | — | Form rút tiền |
| 2 | Nhập số tiền rút > số dư | 200,000 VND | Hệ thống validate |

### 4. Expected Result
- Thông báo: "Số dư ví không đủ. Số dư hiện tại: 50,000 VND"
- Nút "Tiếp tục" disabled hoặc hiển thị lỗi inline
- Không cho phép tiến hành giao dịch
- Gợi ý nạp thêm tiền vào ví

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Số dư ví | Số tiền rút | Kết quả mong đợi |
|---|---------|-------------|-------------------|
| 1 | 50,000 | 200,000 | Chặn, báo lỗi |
| 2 | 0 | 100,000 | Chặn, báo lỗi |
| 3 | 100,000 | 100,000 | Cho phép (boundary) |

### 7. Pass/Fail Criteria
- **Pass**: Chặn giao dịch, thông báo rõ ràng, không trừ ví
- **Fail**: Cho rút vượt dư, ví âm, app crash

### 8. Notes
- Boundary: rút đúng bằng số dư → phải thành công (TC riêng)

---

## TC-VDT-005: Liên kết tài khoản ngân hàng mới (Happy Path)

### 1. Objective
Kiểm tra user liên kết thêm tài khoản ngân hàng vào ví thành công.

### 2. Preconditions
- User đã đăng nhập, ví đã kích hoạt
- Có thông tin TK ngân hàng hợp lệ chưa liên kết
- Ngân hàng nằm trong danh sách hỗ trợ

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Mở "Ví điện tử" → "Quản lý" → "Liên kết ngân hàng" | — | Danh sách ngân hàng hỗ trợ |
| 2 | Chọn ngân hàng | "Vietcombank" | Form nhập thông tin TK |
| 3 | Nhập số tài khoản | "0123456789" | Validate format |
| 4 | Nhập tên chủ TK | "NGUYEN VAN A" | Tên hiển thị |
| 5 | Xác thực OTP từ ngân hàng | OTP 6 số | Xác thực thành công |

### 4. Expected Result
- Thông báo "Liên kết tài khoản thành công"
- TK mới xuất hiện trong danh sách TK liên kết
- Có thể sử dụng TK mới để nạp/rút tiền ngay
- Hiển thị TK dạng mask: "Vietcombank *6789"

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data

| # | Ngân hàng | Số TK | Tên chủ TK |
|---|-----------|-------|------------|
| 1 | Vietcombank | 0123456789 | NGUYEN VAN A |
| 2 | Techcombank | 19033456789 | TRAN THI B |

### 7. Pass/Fail Criteria
- **Pass**: Liên kết thành công, hiển thị trong danh sách, sử dụng được ngay
- **Fail**: Liên kết lỗi, không hiển thị, hoặc không dùng được sau liên kết

### 8. Notes
- Kiểm tra giới hạn số TK liên kết tối đa
- Kiểm tra liên kết TK đã liên kết trước đó (duplicate check)

---

## TC-VDT-006: Nhập sai PIN 5 lần liên tiếp (Edge Case - Security)

### 1. Objective
Kiểm tra cơ chế khóa ví khi nhập sai PIN quá số lần cho phép.

### 2. Preconditions
- User đã đăng nhập
- Đang ở bước xác nhận giao dịch (nạp/rút tiền)

### 3. Test Steps

| Step | Action | Input Data | Expected Result |
|------|--------|-----------|-----------------|
| 1 | Thực hiện giao dịch → đến bước nhập PIN | — | Màn hình nhập PIN |
| 2 | Nhập sai PIN lần 1 | "000000" | "PIN không đúng. Còn 4 lần thử" |
| 3 | Nhập sai PIN lần 2 | "111111" | "PIN không đúng. Còn 3 lần thử" |
| 4 | Nhập sai PIN lần 3 | "222222" | "PIN không đúng. Còn 2 lần thử" |
| 5 | Nhập sai PIN lần 4 | "333333" | "PIN không đúng. Còn 1 lần thử" |
| 6 | Nhập sai PIN lần 5 | "444444" | Khóa ví / khóa giao dịch |

### 4. Expected Result
- Sau lần 5: Ví bị khóa tạm thời (15-30 phút) hoặc yêu cầu xác thực lại
- Thông báo: "Bạn đã nhập sai PIN 5 lần. Ví tạm khóa trong 30 phút."
- Mọi giao dịch bị chặn trong thời gian khóa
- Gửi notification cảnh báo bảo mật đến user
- Ghi log security event

### 5. Actual Result
- _(Điền khi thực hiện test)_
- Pass ✅ / Fail ❌ / Blocked ⚠️

### 6. Test Data
- PIN đúng: "123456" (không dùng trong test này)
- 5 PIN sai liên tiếp: "000000", "111111", "222222", "333333", "444444"

### 7. Pass/Fail Criteria
- **Pass**: Khóa ví sau 5 lần sai, thông báo rõ, notification bảo mật, không cho giao dịch
- **Fail**: Không khóa, cho thử vô hạn, hoặc khóa vĩnh viễn không có cách mở

### 8. Notes
- Kiểm tra sau khi hết thời gian khóa → nhập đúng PIN → mở khóa thành công
- Kiểm tra đếm lần sai có reset sau khi nhập đúng 1 lần không

---

## TC-VDT-PERF-001: Performance Test – Nạp/Rút tiền ví dưới tải cao

### 1. Objective
Đo lường hiệu năng hệ thống ví điện tử khi nhiều user nạp/rút tiền đồng thời.

### 2. Preconditions
- Môi trường: Staging (cấu hình tương đương production)
- Database: ≥ 50,000 ví active, mỗi ví có ≥ 1 TK ngân hàng liên kết
- Tool đo: JMeter / k6 / Gatling
- Baseline sprint trước đã ghi nhận

### 3. Test Scenarios

| # | Scenario | Load Condition | Threshold (SLA) |
|---|----------|---------------|-----------------|
| 1 | Nạp tiền vào ví – single user | 1 user | End-to-end ≤ 10 giây |
| 2 | Nạp tiền concurrent | 100 users đồng thời | ≤ 12 giây (P95) |
| 3 | Rút tiền từ ví – single user | 1 user | End-to-end ≤ 10 giây |
| 4 | Rút tiền concurrent | 100 users đồng thời | ≤ 12 giây (P95) |
| 5 | Mix nạp + rút đồng thời | 200 users (50% nạp, 50% rút) | ≤ 15 giây (P95), error < 1% |
| 6 | Sustained load 15 phút | 100 users liên tục nạp/rút | Stable, no memory leak |
| 7 | Balance check (xem số dư) | 500 requests/giây | ≤ 500ms (P95) |

### 4. Metrics cần đo

| Metric | Mô tả | Ngưỡng Pass |
|--------|--------|-------------|
| Nạp tiền Response (P95) | Từ nhấn xác nhận → thành công | ≤ 10 giây |
| Rút tiền Response (P95) | Từ nhấn xác nhận → thành công | ≤ 10 giây |
| Balance Query (P95) | Xem số dư ví | ≤ 500ms |
| Throughput | Giao dịch ví/giây | ≥ 30 TPS |
| Error Rate | % giao dịch lỗi hệ thống | < 1% |
| Balance Consistency | Số dư đúng sau concurrent operations | 100% consistent |
| CPU / Memory | Server resource | < 80% |
| DB Lock Wait | Thời gian chờ lock trên balance table | < 100ms |

### 5. Pass/Fail Criteria
- **Pass**: Tất cả metrics trong ngưỡng, balance luôn consistent, không deadlock
- **Fail**: Balance inconsistency (tiền mất/thừa), deadlock, error > 1%
- **Critical Fail**: Race condition dẫn đến số dư âm hoặc nạp/rút trùng

### 6. Notes
- **CRITICAL**: Kiểm tra race condition khi cùng 1 ví bị nạp + rút đồng thời
- Verify: tổng tiền trong hệ thống trước và sau test phải bằng nhau (conservation)
- Kiểm tra DB lock contention trên bảng balance
- So sánh với baseline sprint trước
- Đính kèm: performance report, resource monitoring

---

## TC-VDT-PERF-002: Performance Test – Liên kết ngân hàng & OTP verification

### 1. Objective
Đo lường hiệu năng luồng liên kết ngân hàng và xác thực OTP dưới tải.

### 2. Preconditions
- Sandbox ngân hàng available
- Tool đo: k6 / JMeter

### 3. Test Scenarios

| # | Scenario | Load Condition | Threshold |
|---|----------|---------------|-----------|
| 1 | Liên kết TK ngân hàng – single | 1 user | ≤ 15 giây (bao gồm OTP) |
| 2 | Liên kết concurrent | 30 users đồng thời | ≤ 20 giây (P95) |
| 3 | OTP verification | 50 requests/giây | ≤ 3 giây (P95) |
| 4 | Bank account validation | 100 requests/giây | ≤ 5 giây (P95) |

### 4. Pass/Fail Criteria
- **Pass**: Liên kết thành công trong SLA, OTP verify nhanh, không timeout
- **Fail**: OTP expired do latency, liên kết fail hàng loạt, bank API timeout

### 5. Notes
- OTP thường có TTL 60-120 giây → nếu flow chậm hơn → OTP expired
- Kiểm tra retry khi bank API timeout
- Rate limit từ phía ngân hàng có thể ảnh hưởng kết quả

---

## TC-VDT-REG-001: Regression Test – Ví điện tử sau deploy

### 1. Objective
Xác nhận toàn bộ luồng ví điện tử (nạp, rút, liên kết, hạn mức) vẫn hoạt động đúng sau deploy.

### 2. Preconditions
- Build mới đã deploy lên staging
- Thay đổi liên quan: [ghi rõ change log]
- TK ngân hàng sandbox available
- Golden dataset đã chuẩn bị

### 3. Regression Scope

| # | Feature/Flow | Liên quan change? | Priority |
|---|-------------|-------------------|----------|
| 1 | Nạp tiền vào ví | Kiểm tra mọi deploy | P1 |
| 2 | Rút tiền từ ví | Kiểm tra mọi deploy | P1 |
| 3 | Xem số dư ví | Kiểm tra mọi deploy | P1 |
| 4 | Hạn mức ví | Trực tiếp nếu đổi config | P1 |
| 5 | Liên kết ngân hàng | Gián tiếp | P2 |
| 6 | Hủy liên kết ngân hàng | Gián tiếp | P2 |
| 7 | Lịch sử giao dịch ví | Gián tiếp | P2 |
| 8 | Khóa ví khi sai PIN | Gián tiếp | P2 |
| 9 | Notification sau GD | Gián tiếp | P3 |

### 4. Golden Dataset (Regression Baseline)

| # | Scenario | Input | Expected (Baseline) | Sprint |
|---|----------|-------|---------------------|--------|
| 1 | Nạp 500K từ VCB | Vietcombank *1234, 500,000 | Thành công, ví +500K, TK -500K | Sprint 2 |
| 2 | Nạp min amount | BIDV *9012, 50,000 | Thành công | Sprint 2 |
| 3 | Nạp vượt hạn mức | Dư 19.5M, nạp 1M (hạn mức 20M) | Chặn, báo hạn mức còn 500K | Sprint 3 |
| 4 | Rút 200K về VCB | Ví dư 1M, rút 200K | Thành công, ví -200K | Sprint 2 |
| 5 | Rút khi dư không đủ | Ví dư 50K, rút 200K | Chặn, báo "Số dư không đủ" | Sprint 2 |
| 6 | Liên kết TK mới | Techcombank, TK hợp lệ | Liên kết thành công | Sprint 3 |
| 7 | Sai PIN 5 lần | 5 PIN sai liên tiếp | Khóa ví 30 phút | Sprint 3 |
| 8 | Xem số dư | — | Hiển thị đúng số dư real-time | Sprint 2 |

### 5. Pass/Fail Criteria
- **Pass**: 100% golden dataset cho kết quả đúng baseline
- **Fail**: Bất kỳ scenario nào fail mà trước đó pass
- **Critical Fail**: Nạp/rút tiền sai số dư, balance inconsistency

### 6. Quy trình khi Regression Fail
1. Log bug với tag [Regression][Ví điện tử]
2. Xác định flow nào bị ảnh hưởng (nạp/rút/liên kết)
3. Kiểm tra: lỗi do code change hay bank API thay đổi?
4. Verify balance consistency: tổng tiền hệ thống có đúng không?
5. Quyết định: rollback / hotfix

### 7. Notes
- **CRITICAL**: Luôn verify balance consistency sau regression run
- Chạy regression sau mỗi deploy staging
- Đặc biệt chú ý khi thay đổi logic tính balance hoặc hạn mức
- Automate bằng API test (Postman + Newman / k6)

---

## TC-VDT-REG-002: Regression Test – Balance consistency sau concurrent operations

### 1. Objective
Xác nhận số dư ví luôn chính xác sau khi thực hiện nhiều giao dịch nạp/rút đồng thời (data integrity).

### 2. Preconditions
- Staging environment
- Ví test có số dư ban đầu xác định (VD: 5,000,000 VND)
- Script tự động thực hiện nhiều GD đồng thời

### 3. Test Scenarios

| # | Scenario | Operations | Expected Balance |
|---|----------|-----------|-----------------|
| 1 | Nạp 3 lần liên tiếp | +100K, +200K, +300K | Ban đầu + 600K |
| 2 | Rút 3 lần liên tiếp | -100K, -150K, -200K | Ban đầu - 450K |
| 3 | Nạp + Rút đồng thời | +500K và -300K cùng lúc | Ban đầu + 200K |
| 4 | 10 GD random concurrent | Mix nạp/rút | Tổng đúng toán học |
| 5 | Nạp đến sát hạn mức + rút | Nạp 19.9M, rút 100K | 19,800,000 |

### 4. Pass/Fail Criteria
- **Pass**: Số dư cuối = Số dư đầu + Σ(nạp) - Σ(rút), chính xác 100%
- **Fail**: Sai lệch bất kỳ đồng nào → race condition / data corruption
- **Critical**: Số dư âm hoặc vượt hạn mức → logic error

### 5. Notes
- Test này verify data integrity, không phải performance
- Chạy sau mỗi lần thay đổi logic balance/transaction
- Nếu fail → khả năng cao là race condition hoặc missing DB lock
- Recommend: chạy 100 lần để detect intermittent issues

---
*Vikki Bank · QA Test Cases · Ví điện tử · Updated with Performance & Regression*
