# Acceptance Criteria Standard Template · BA Zone
> Format: Given-When-Then (Gherkin syntax)  
> Tối thiểu 3 AC cho mỗi User Story: Happy path + Edge case + Negative path  
> Biên soạn: **Phúc NT** · BA Zone · Digital School

---

## AC1: [Tên scenario - Happy path]

**Given** [tiền điều kiện 1]  
**And** [tiền điều kiện 2 - nếu có]

**When** [hành động chính của user]

**Then** [kết quả chính - đo lường được]  
**And** [kết quả phụ 1 - nếu có]  
**And** [kết quả phụ 2 - nếu có]

---

## AC2: [Tên scenario - Edge case / Validation]

**Given** [bối cảnh edge case hoặc điều kiện biên]

**When** [hành động trigger edge case / nhập cận trên - cận dưới]

**Then** [hệ thống xử lý đúng quy định]  
**And** [thông báo / hành vi cụ thể hiển thị]

---

## AC3: [Tên scenario - Negative path / Error handling]

**Given** [bối cảnh lỗi hoặc trạng thái phiên hết hạn]

**When** [hành động dẫn đến lỗi / nhập sai dữ liệu]

**Then** [hệ thống xử lý lỗi đúng cách và an toàn]  
**And** [hiển thị thông báo lỗi thân thiện, cụ thể]  
**And** [không có side effect không mong muốn, rollback an toàn]

---

## Checklist trước khi commit AC (Pre-Commit AC Checklist)

- [ ] Mỗi AC chỉ kiểm thử 1 kịch bản (scenario) duy nhất.
- [ ] Given / When / Then đều có thể đo lường và xác minh được (có số liệu, trạng thái rõ ràng).
- [ ] Không chứa từ ngữ mơ hồ: *"nhanh"*, *"phù hợp"*, *"user-friendly"*, *"an toàn"*.
- [ ] Không chứa logic cài đặt kỹ thuật (API endpoint, database column, mã code nội bộ).
- [ ] Không mô tả chi tiết UI vụn vặt (mã màu HEX, kích thước pixel cụ thể).
- [ ] Đảm bảo tối thiểu đủ bộ 3: 1 Happy Path + 1 Edge Case + 1 Negative Path.
- [ ] QA / Tester có thể viết ngay Test Cases từ AC này mà không cần hỏi lại BA.
