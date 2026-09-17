# BA Zone Requirements & Documentation Toolkit 🚀
> **Bộ công cụ & Kỹ năng AI dành cho IT Business Analysts**  
> Dựa trên nghiên cứu & giáo trình bởi **Phúc NT** · **BA Zone** · **Digital School**

[![Standard: IIBA BABOK](https://img.shields.io/badge/Standard-IIBA%20BABOK-blue.svg)](https://www.iiba.org/)
[![Agile: INVEST & Gherkin](https://img.shields.io/badge/Agile-INVEST%20%26%20Gherkin-green.svg)](https://en.wikipedia.org/wiki/INVEST_(mnemonic))
[![Languages: English & Vietnamese](https://img.shields.io/badge/Language-EN%20%7C%20VI-orange.svg)](#hỗ-trợ-song-ngữ-output_language)
[![QA: Compounding Loop](https://img.shields.io/badge/Auditor-Compounding%20Loop-success.svg)](#kiểm-thử-chất-lượng-compounding-loop)

---

## 📌 Giới Thiệu

Repository này cung cấp hệ sinh thái kỹ năng AI (Antigravity Skills) và bộ công cụ kiểm thử chất lượng tự động, giúp IT Business Analysts, Product Owners và Technical Writers:
1. Đặc tả **Use Case** chuẩn mực 16 trường (Karl Wiegers / IIBA, Alistair Cockburn).
2. Viết **User Story & Acceptance Criteria** chuẩn Agile INVEST và cú pháp Gherkin Given-When-Then.
3. **Học cấu trúc (Reverse-engineer Blueprint)** từ bất kỳ tài liệu mẫu nào của doanh nghiệp (BRD, URD, SRS, FSD, PRD...) để sinh tài liệu mới chuẩn 1:1 theo template của dự án.
4. Kiểm soát chất lượng thông qua **Compounding Loop Master Auditor** tự động.

---

## 📂 Cấu Trúc Repository

```text
ba-zone/
├── use-case-writer-skill/           # [Skill 1] Đặc tả Use Case chuẩn IIBA 16 trường
│   ├── SKILL.md                     # Hướng dẫn chi tiết & workflow cho AI
│   ├── templates/                   # Template Use Case song ngữ EN & VI
│   └── samples/                     # File mẫu chuẩn đầu ra (sample_uc_en, sample_uc_vi)
│
├── user-story-writer-skill/         # [Skill 2] Viết User Story & AC chuẩn INVEST + Gherkin
│   ├── SKILL.md                     # Hướng dẫn chi tiết & workflow cho AI
│   ├── templates/                   # Template Story & AC song ngữ EN & VI
│   └── samples/                     # File mẫu chuẩn đầu ra (sample_us_en, sample_us_vi)
│
├── doc-template-learner-skill/      # [Skill 3] Học cấu trúc từ BRD, URD, SRS, FSD bất kỳ
│   ├── SKILL.md                     # Hướng dẫn bóc tách Blueprint và sinh tài liệu tương ứng
│   ├── references/                  # Hướng dẫn chi tiết cho các chuẩn tài liệu lớn
├── web-app-uat-skill/               # [Skill 4] Kiểm thử, nghiệm thu (UAT) & trải nghiệm App
│   ├── SKILL.md                     # Hướng dẫn chi tiết quy trình 8 bước theo TrọBill
│   ├── templates/                   # Template Kế hoạch & Biên bản nghiệm thu UAT, credentials.json
│   └── samples/                     # File mẫu báo cáo nghiệm thu chuẩn đầu ra (EN & VI)
│
├── scripts/                         # Bộ công cụ kiểm thử chất lượng tự động (Auditors)
│   ├── audit_uc.py                  # Script kiểm tra chuẩn 16 trường & quy tắc Cockburn
│   ├── audit_us.py                  # Script kiểm tra tiêu chuẩn INVEST & 3 kịch bản Gherkin
│   └── audit_uat.py                 # Script kiểm định báo cáo UAT & Live Web App Probe Runner
│
├── audit-all.ps1                    # Master Compounding Loop Auditor (PowerShell runner)
└── README.md                        # Tài liệu hướng dẫn sử dụng repository
```

---

## 🎯 Chi Tiết Các Kỹ Năng (AI Skills)

### 1. `use-case-writer-skill` — Chuyên Gia Đặc Tả Use Case
- **Tiêu chuẩn áp dụng**: 
  - **Karl Wiegers / IIBA BABOK**: 16 trường thông tin bắt buộc (Identity, Context, Flows, Supplementals).
  - **Alistair Cockburn**: Quy tắc kiểm tra cà phê (*Coffee-break test*), cấp độ mục tiêu người dùng (*User-goal level - Sea level*), nguyên tắc *1 Actor - 1 Goal - 1 Session*.
- **Quy trình sinh tài liệu**: Sinh tuần tự 5 nhóm trường, dừng chờ người dùng duyệt sau từng nhóm để đảm bảo không bị sai lệch logic nghiệp vụ.
- **Tự kiểm tra**: Bảng kiểm định chất lượng 20 tiêu chí (*20-point quality checklist*) trước khi bàn giao.
- **Cách kích hoạt**:
  > *"Viết Use Case cho tính năng đăng ký tài khoản"*, *"Đặc tả UC đăng ký học viên"*, *"Draft use case for user login"*, *"Split feature into UCs"*.

---

### 2. `user-story-writer-skill` — Chuyên Gia User Story & Acceptance Criteria
- **Tiêu chuẩn áp dụng**:
  - Cấu trúc 3 thành phần: `As a... I want to... So that...` (hoặc `Là một... Tôi muốn... Để...`).
  - Đánh giá chất lượng theo 6 tiêu chí **INVEST** (*Independent, Negotiable, Valuable, Estimable, Small, Testable*).
  - Tiêu chí nghiệm thu viết bằng cú pháp **Gherkin Given-When-Then**, bắt buộc bao phủ đủ **tối thiểu 3 loại kịch bản**:
    1. **Happy Path** (Kịch bản chuẩn khi dữ liệu hợp lệ).
    2. **Edge Case / Boundary** (Kịch bản biên, kiểm tra giới hạn hoặc trường tùy chọn).
    3. **Negative Path / Error** (Kịch bản lỗi, dữ liệu không hợp lệ hoặc sự cố hệ thống).
- **Cách kích hoạt**:
  > *"Viết User Story chuẩn INVEST cho tính năng lọc khóa học"*, *"Tạo AC Given-When-Then cho story này"*, *"Review US này giúp mình"*.

---

### 3. `doc-template-learner-skill` — Học & Nhân Bản Cấu Trúc Tài Liệu Doanh Nghiệp
- **Khả năng bóc tách**: Phân tích bất kỳ tài liệu mẫu nào (BRD, URD, SRS chuẩn IEEE 830, FSD màn hình, PRD sản phẩm) để trích xuất:
  - Cây đề mục (Heading Hierarchy H1, H2, H3...).
  - Cấu trúc bảng biểu, định dạng ma trận và metadata.
  - Quy ước đặt mã yêu cầu (`REQ-XX`, `FR-XX`, `NFR-XX`).
  - Sơ đồ trực quan (Mermaid Flowchart, Sequence, ERD).
  - Văn phong và thuật ngữ đặc thù của doanh nghiệp.
- **Cơ chế sinh**: 
  - *Interactive Mode*: Sinh cuốn chiếu từng chương, xác nhận với BA trước khi qua chương tiếp theo.
  - *Batch Mode*: Sinh trọn gói một lần đối với tài liệu ngắn.
- **Đối soát (Parity Audit)**: Kiểm tra đối chiếu đảm bảo tài liệu mới sinh khớp 100% về cấu trúc và các bảng so với tài liệu mẫu.
- **Cách kích hoạt**:
  > *"Học template từ file BRD này và viết BRD cho tính năng tìm kiếm mới..."*, *"Dựa vào cấu trúc file SRS mẫu để viết SRS cho hệ thống quản lý kho..."*.

---

### 4. `web-app-uat-skill` — Chuyên Gia Kiểm Thử & Nghiệm Thu App (TrọBill Methodology)
- **Tiêu chuẩn áp dụng**:
  - **Quy trình 8 bước nghiệm thu (8-Phase UAT Protocol)**: Pre-flight, Authentication & Session, Multi-Role RBAC, Happy Path, Edge Cases, Negative Scenarios, Responsive Viewports & Console Health, Hardware Isolation & Sign-off.
  - **Triết lý thực chiến TrọBill**: Token-preserving & Zero Retry Loops, bộ bảo vệ 3 giây cho headless browser, phân lập rõ ràng các ranh giới phần cứng không thể tự động hóa (Camera OCR, Google Play IAP, Android SAF).
  - **Ma trận quyết định**: Xuất biên bản bàn giao chính thức với khuyến nghị nghiệm thu rõ ràng: `GO`, `NO-GO`, hoặc `CONDITIONAL GO`.
- **Bộ công cụ tự động hóa**:
  - `scripts/audit_uat.py`: Chế độ kiểm định biên bản nghiệm thu (`--file`) và Chế độ thăm dò / smoke trực tiếp ứng dụng đang chạy khi có URL & Credentials (`--url`).
- **Cách kích hoạt**:
  > *"Mình có URL app và tài khoản admin/pass, hãy thực hiện UAT và xuất biên bản nghiệm thu"*, *"Kiểm thử kịch bản biên và phân quyền RBAC cho tính năng thu tiền phòng"*, *"Audit biên bản UAT này theo chuẩn TrọBill: sample_uat_report_vi.md"*.

---

## 🌐 Hỗ Trợ Song Ngữ (`output_language`)

Mọi skill đều hỗ trợ biến phiên làm việc `output_language` để kiểm soát ngôn ngữ của tài liệu đầu ra:

| Giá trị | Ý nghĩa | Hành vi |
|---|---|---|
| `output_language=en` | **Tiếng Anh** *(Mặc định)* | Toàn bộ tiêu đề, nhãn bảng biểu và nội dung tài liệu được sinh bằng tiếng Anh chuẩn IT BA quốc tế. |
| `output_language=vi` | **Tiếng Việt** | Toàn bộ nhãn trường và nội dung tài liệu được dịch/sinh bằng tiếng Việt chuẩn chuyên ngành BA. |

> [!TIP]
> **Nguyên tắc hội thoại:** Kỹ năng sẽ luôn trò chuyện, giải thích và hỏi đáp bằng chính ngôn ngữ mà bạn đang chat, trong khi `output_language` chỉ định đoạt ngôn ngữ của tài liệu markdown được xuất ra.

---

## 🧪 Kiểm Thử Chất Lượng (Compounding Loop)

Repository tích hợp sẵn kịch bản kiểm thử tự động theo tiêu chuẩn **Compounding Loop** (tương tự tiêu chuẩn tại dự án TrọBill) nhằm bảo đảm chất lượng tài liệu sinh ra luôn đáp ứng 100% tiêu chuẩn IIBA và Agile:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\audit-all.ps1
```

### Các Suite Kiểm Thử:
1. **Suite 1: Use Case Standard & Format Integrity (`scripts/audit_uc.py`)**
   - Kiểm tra đủ 16 trường bắt buộc (cả nhãn tiếng Anh lẫn tiếng Việt).
   - Kiểm tra định dạng mã `UC-[MODULE]-[NN]`.
   - Kiểm tra Normal Course đánh số thứ tự, phân định rõ Actor và System.
   - Ngăn chặn logic rẽ nhánh `if/else` bị nhồi nhét vào luồng chính.
   - Kiểm tra định dạng mã rẽ nhánh `AC` và ngoại lệ `EX`.
2. **Suite 2: User Story & AC Standard Integrity (`scripts/audit_us.py`)**
   - Kiểm tra cấu trúc 3 phần `As a... I want to... So that...`.
   - Phát hiện và cảnh báo anti-pattern persona chung chung (*"user"*, *"người dùng"*).
   - Kiểm tra sự hiện diện của bảng tự đánh giá INVEST.
   - Kiểm tra cú pháp Gherkin `Given-When-Then`.
   - Xác thực độ bao phủ đủ 3 loại kịch bản: Happy path, Edge case, Negative path.
3. **Suite 3: Web App UAT & Live Experience Integrity (`scripts/audit_uat.py`)**
   - Kiểm tra đủ 8 phần cấu trúc cốt lõi của biên bản nghiệm thu UAT.
   - Kiểm tra mã định danh Test Case chuẩn `TC-[MODULE]-[NN]`.
   - Kiểm tra độ bao phủ đầy đủ 3 loại kịch bản: Happy Path, Edge Case, Negative Path.
   - Kiểm tra phân loại mức độ nghiêm trọng lỗi (Critical, Major, Minor, Trivial).
   - Xác thực kiểm thử hiển thị đa màn hình (Desktop 1920x1080, Tablet 768x1024, Mobile 375x667).
   - Kiểm tra trạng thái sạch sẽ của Javascript Console và HTTP Network.
   - Kiểm tra danh mục phân lập ranh giới phần cứng và quyết định nghiệm thu xuất xưởng (GO / NO-GO).

---

## 🚀 Hướng Dẫn Bắt Đầu Nhanh

### 1. Sử dụng trong Antigravity IDE / Cursor / Claude Code
Sao chép các thư mục `*-skill` vào thư mục skills của dự án hoặc trỏ đường dẫn context vào file `SKILL.md` tương ứng.

### 2. Ví dụ Prompt Thử Nghiệm

#### Viết Use Case:
```text
Dùng skill use-case-writer, viết Use Case cho tính năng: "Học viên thanh toán học phí qua cổng VNPay".
output_language=vi
```

#### Viết User Story:
```text
Dùng skill user-story-writer, viết User Story cho tính năng: "Người dùng hủy đơn hàng trước khi đóng gói".
output_language=en
```

#### Học từ Template & Sinh Tài Liệu Mới:
```text
Dùng skill doc-template-learner, hãy đọc cấu trúc template từ file:
use-case-writer-main/BRD_Semantic_Search_527432316.md
Sau đó viết BRD cho tính năng: "Hệ thống gợi ý khóa học thông minh dựa trên kỹ năng của học viên".
output_language=vi
```

#### Kiểm Thử & Nghiệm Thu App (UAT):
```text
Dùng skill web-app-uat, mình có ứng dụng TrọBill đang chạy tại:
URL: http://localhost:8767/app/trobill/uat.html
Tài khoản: chutro_vip@trobill.vn / MatKhau123! (Vai trò: Landlord / Chủ trọ)
Hãy kiểm tra luồng đăng nhập, chốt chỉ số điện nước, sinh VietQR và xuất biên bản nghiệm thu UAT chuẩn cho mình.
output_language=vi
```

---

## 📜 Bản Quyền & Đóng Góp

- Được phát triển và hoàn thiện dựa trên tài liệu đào tạo của **Phúc NT** — **BA Zone** & **Digital School**.
- Chuẩn hóa cho môi trường agentic coding bởi cộng đồng IT BA Việt Nam.
