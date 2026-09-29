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
├── .agents/                         # Sổ tay quản lý AI Agents & Kỹ năng
│   ├── skills/                      # Nơi đăng ký tự động các AI Skills
│   │   ├── doc-template-learner-skill/
│   │   ├── enterprise-nda-sanitizer/
│   │   ├── use-case-writer-skill/
│   │   ├── user-story-writer-skill/
│   │   └── web-app-uat-skill/
│   └── AGENTS.md                    # Registry & Hướng dẫn sử dụng Skills
│
├── docs/                            # Thư viện tài liệu & Knowledge Base
│   ├── templates/                   # 19+ File mẫu chuẩn: BRD, Use Cases, User Stories, UAT Reports, PDF/DOCX
│   │   └── README.md                # Master Catalog & Index tra cứu biểu mẫu
│   ├── guidelines/                  # Bộ cẩm nang: INVEST, Cockburn Style, 20-Point Quality Checklists
│   └── inputs/                      # Tài liệu đầu vào gốc (được bảo vệ bởi .gitignore)
│
├── prototypes/                      # Khu vực Interactive Mockup / UI Prototype (Không commit Git)
├── artifacts/                       # Thư mục chứa tài liệu đặc tả hoàn thiện xuất ra từ AI Skills
├── scratch/                         # Vùng nháp tạm thời (Scratchpad - Drop sau khi hoàn thành task)
│
├── scripts/                         # Bộ công cụ kiểm thử chất lượng tự động (Auditors)
│   ├── audit_hygiene.py             # Script kiểm định chống rò rỉ mockup build & bảo vệ NDA
│   ├── audit_uc.py                  # Script kiểm tra chuẩn 16 trường & quy tắc Cockburn
│   ├── audit_us.py                  # Script kiểm tra tiêu chuẩn INVEST & 3 kịch bản Gherkin
│   └── audit_uat.py                 # Script kiểm định báo cáo UAT & Live Web App Probe Runner
│
├── audit-all.ps1                    # Master Compounding Loop Auditor (PowerShell runner)
├── CHANGELOG.md                     # Lịch sử phiên bản & thay đổi
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

### Các Suite Kiểm Thử (5-Tier Master Auditor):
1. **Suite 1: Repo Hygiene & Zero Leakage (`scripts/audit_hygiene.py`)**
   - Kiểm tra `git ls-files` đảm bảo 0 prototype/build files và 0 file nhạy cảm nội bộ bị commit.
   - Xác thực cấu hình `.gitignore` bảo vệ tuyệt đối thư mục `docs/inputs/`, `docs/outputs/`, `artifacts/`.
2. **Suite 2: Use Case Standard & Format Integrity (`scripts/audit_uc.py`)**
   - Kiểm tra đủ 16 trường bắt buộc (Karl Wiegers / IIBA Babok).
   - Kiểm tra mã `UC-[MODULE]-[NN]`, Normal Course tuần tự, phân tách rõ ràng Actor và System.
3. **Suite 3: User Story & AC Standard Integrity (`scripts/audit_us.py`)**
   - Kiểm tra cấu trúc `As a... I want to... So that...` và bảng tự đánh giá INVEST.
   - Kiểm tra cú pháp Gherkin `Given-When-Then` đủ 3 kịch bản: Happy path, Edge case, Negative path.
4. **Suite 4: Web App UAT & Live Experience Integrity (`scripts/audit_uat.py`)**
   - Kiểm tra cấu trúc 8 phần của biên bản nghiệm thu UAT TrọBill.
   - Kiểm tra độ bao phủ Test Cases, viewport đa thiết bị và Hardware Isolation Registry (GO / NO-GO).
5. **Suite 5: Output Quality, Anti-Overflow, Word-Friendly & Vietnamese Spelling (`scripts/audit_outputs.py`)**
   - Kiểm tra toàn diện tài liệu trong `docs/outputs/` (cả `.md` và `.html`) theo [`.agents/rules/output_quality_standards.md`](file:///d:/repo/ba-zone/.agents/rules/output_quality_standards.md).
   - Bắt buộc khóa cứng CSS chống tràn A4 (`table-layout: fixed; width: 100%;` và `@page { size: A4 portrait; margin: 12mm 10mm; }`).
   - Chuẩn hóa Text-First & Word-Friendly: Cấm CSS Grid, card decks trôi nổi và badge viên thuốc bo tròn lớn; bắt buộc dùng `<table>` chuẩn cho Metadata/KPI metrics; luôn đính kèm Text Fallback Table dưới sơ đồ Mermaid để chuyển PDF $\rightarrow$ DOCX không bị vỡ layout hoặc phải sửa manual.
   - Kiểm soát ngân sách cột bảng: Tối đa 4 cột cho text dài, bắt buộc tách bảng theo từng phân kỳ.
   - Rà soát từ điển lỗi chính tả BA (26+ cặp từ: `giảng viên`, `thư ký`, `quy trình`, `chuyên cần`, `điểm danh`, `xử lý`...).
   - Kiểm tra giọng văn ngoại giao doanh nghiệp, chuẩn hóa Ma trận `AM (Authority Matrix)` và Dev Architecture Spine Baseline 2026.

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
