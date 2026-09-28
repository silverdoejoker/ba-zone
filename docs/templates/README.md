# Thư Viện Templates & Tài Liệu Tham Khảo (BA Zone Template Library)

> Chào mừng đến với Thư viện Templates & Tài liệu Mẫu của **BA Zone**.  
> Toàn bộ các biểu mẫu đặc tả Business Analysis, Agile User Stories, UAT Test Plans và tài liệu thực tế của các hệ sinh thái lớn (GMS, CMS, LMS, TrọBill) được chuẩn hóa và lưu trữ tập trung tại đây để phục vụ cho các AI Agent Skills và BA trong dự án.

---

## 📑 Danh Mục Biểu Mẫu Chuẩn (Standard Specification Templates)

| Tên File | Chuẩn Áp Dụng | Mô Tả & Mục Đích Sử Dụng | Skill Tương Ứng |
|---|---|---|---|
| [`template_brd_standard.md`](file:///d:/repo/ba-zone/docs/templates/template_brd_standard.md) | `NVG-ITD-SOP14.F01` / BRD STD | Mẫu Đặc tả Yêu cầu Nghiệp vụ & Thiết kế Giải pháp tiêu chuẩn NVG (5 phần chính thức, Ma trận AM, tích hợp API vs DB, và ma trận test scenarios linh hoạt). | `doc-template-learner-skill` |
| [`template_thiet_ke_giai_phap_sop14.md`](file:///d:/repo/ba-zone/docs/templates/template_thiet_ke_giai_phap_sop14.md) | `NVG-ITD-SOP14.F01` | Mẫu Thiết kế Tài liệu Giải pháp (SAD) chính thức của NVG-ITC với tiền tố CSDL chuẩn và ranh giới Security L7 Data Scope. | `doc-template-learner-skill` |
| [`template_yeu_cau_ptud_sop01.md`](file:///d:/repo/ba-zone/docs/templates/template_yeu_cau_ptud_sop01.md) | `NVG-ITD-SOP01.F01` | Biểu mẫu Phiếu Yêu cầu Phát triển Ứng dụng chuẩn NVG (3 phần chính thức: Thông tin chung, Mô tả yêu cầu, Trình & Phê duyệt). | `doc-template-learner-skill` |
| [`template_blueprint_schema.md`](file:///d:/repo/ba-zone/docs/templates/template_blueprint_schema.md) | Blueprint Schema | Mẫu cấu trúc YAML chuẩn để trích xuất và bóc tách bố cục từ bất kỳ tài liệu gốc nào (BRD/SRS/FSD). | `doc-template-learner-skill` |
| [`template_use_case_16_fields.md`](file:///d:/repo/ba-zone/docs/templates/template_use_case_16_fields.md) | Karl Wiegers / IIBA BABOK | Mẫu đặc tả Use Case chuẩn mực 16 trường (Song ngữ EN / VI) với bảng luồng sự kiện chính, luồng thay thế và ngoại lệ. | `use-case-writer-skill` |
| [`template_user_story_invest.md`](file:///d:/repo/ba-zone/docs/templates/template_user_story_invest.md) | Agile INVEST & Gherkin | Mẫu User Story chuẩn Agile tích hợp bảng tự đánh giá 6 tiêu chí INVEST và 3 kịch bản Acceptance Criteria bắt buộc. | `user-story-writer-skill` |
| [`template_acceptance_criteria_gherkin.md`](file:///d:/repo/ba-zone/docs/templates/template_acceptance_criteria_gherkin.md) | Gherkin Given-When-Then | Mẫu chi tiết AC theo 3 kịch bản: Happy Path, Edge Case, Negative Path kèm checklist rà soát trước khi bàn giao. | `user-story-writer-skill` |
| [`template_uat_test_plan.md`](file:///d:/repo/ba-zone/docs/templates/template_uat_test_plan.md) | TrọBill Methodology | Mẫu Kế hoạch kiểm thử UAT xác định phạm vi, môi trường, ma trận tài khoản phân quyền và tiêu chuẩn xuất xưởng. | `web-app-uat-skill` |
| [`template_uat_acceptance_report.md`](file:///d:/repo/ba-zone/docs/templates/template_uat_acceptance_report.md) | 8-Phase UAT Protocol | Mẫu Biên bản nghiệm thu UAT toàn diện (Executive summary, test matrix, defect log, responsive viewports, console health, sign-off). | `web-app-uat-skill` |

---

## 🔍 Tài Liệu Mẫu Thực Tế (Practical Reference Samples)

| Tên File | Lĩnh Vực / Module | Đặc Điểm Nổi Bật |
|---|---|---|
| [`brd_semantic_search_template.md`](file:///d:/repo/ba-zone/docs/templates/brd_semantic_search_template.md) | Search Engine / AI Retrieval | Tài liệu BRD hoàn chỉnh: luồng xử lý AI Embedding, Ingestion Pipeline, Search Ranking Formula và Fallback Rules. |
| [`sample_use_case_contract_flow.md`](file:///d:/repo/ba-zone/docs/templates/sample_use_case_contract_flow.md) | Enterprise Contract Management | Chuỗi 4 Use Case hoàn chỉnh liên kết luồng hợp đồng: `MSA → SOW → PO → Billable Rate` kèm sơ đồ End-to-End Flow và State Transition. |
| [`sample_use_case_en.md`](file:///d:/repo/ba-zone/docs/templates/sample_use_case_en.md) | EdTech / User Onboarding | Mẫu Use Case tiếng Anh hoàn chỉnh: Đăng ký tài khoản học viên (Google SSO alternative, email collision exception). |
| [`sample_use_case_vi.md`](file:///d:/repo/ba-zone/docs/templates/sample_use_case_vi.md) | EdTech / Onboarding | Mẫu Use Case tiếng Việt hoàn chỉnh chuẩn 16 trường. |
| [`sample_user_story_en.md`](file:///d:/repo/ba-zone/docs/templates/sample_user_story_en.md) | Course Catalog Filtering | User Story tiếng Anh với đầy đủ bảng INVEST PASS và 3 kịch bản Gherkin AC. |
| [`sample_user_story_vi.md`](file:///d:/repo/ba-zone/docs/templates/sample_user_story_vi.md) | Lọc Khóa Học | User Story tiếng Việt hoàn chỉnh chuẩn INVEST. |
| [`sample_user_stories_epics.md`](file:///d:/repo/ba-zone/docs/templates/sample_user_stories_epics.md) | Multi-Domain Epics | Tuyển tập 7 User Stories thực chiến: Enrollment, Mentor booking, Progress tracking, Certificate, Live class, B2B batch upload, Forum report. |
| [`sample_uat_report_en.md`](file:///d:/repo/ba-zone/docs/templates/sample_uat_report_en.md) | Property Management UAT | Báo cáo nghiệm thu tiếng Anh đạt chuẩn 100% Production Ready theo TrọBill methodology. |
| [`sample_uat_report_vi.md`](file:///d:/repo/ba-zone/docs/templates/sample_uat_report_vi.md) | Nghiệm Thu TrọBill | Biên bản nghiệm thu UAT tiếng Việt chi tiết với phân lập ranh giới Camera OCR, Google Play IAP, và Google Drive SAF. |
| [`sample_uat_credentials.json`](file:///d:/repo/ba-zone/docs/templates/sample_uat_credentials.json) | Credential Matrix | File mẫu JSON cấu hình tài khoản kiểm thử UAT đa vai trò (Admin, Manager, Tenant) an toàn. |

---

## 📑 Tài Liệu Gốc Doanh Nghiệp (Original Client Specs & Sign-off PDFs)

Các file tài liệu gốc được lưu trữ phục vụ AI Agent bóc tách cấu trúc và tham khảo context hệ thống (được bảo vệ qua `.gitignore` để không rò rỉ dữ liệu nhạy cảm lên Git):

| Tên File | Định Dạng | Mô Tả Nghiệp Vụ | Trạng Thái Git |
|---|---|---|---|
| `[signed]3.URD_GMS_Full_Final 23.03.26.pdf` | PDF | Bản URD hoàn chỉnh có chữ ký phê duyệt của hệ thống GMS (General Mall System: Leasing, MTS, Billing, Promotion). | Ignored (Bảo mật) |
| `NLE-IT-Yeu cau PTUD-100926.pdf` | PDF | Phiếu yêu cầu phát triển ứng dụng (Change Request / CR) về điều chỉnh công thức và quy trình nghiệp vụ. | Ignored (Bảo mật) |
| `3.URD_GMS_Full_Final 23.03.26.docx` *(tại `docs/inputs/`)* | DOCX | Bản Word gốc của URD GMS. | Ignored (Bảo mật) |
| `NLE-IT-Yeu cau PTUD-100926.docx` *(tại `docs/inputs/`)* | DOCX | Bản Word gốc của yêu cầu phát triển ứng dụng IT. | Ignored (Bảo mật) |

---

## 🧭 Thư Viện Hướng Dẫn & Bộ Tiêu Chuẩn (`docs/guidelines/`)

Nếu bạn cần tìm hiểu sâu về lý thuyết và quy tắc chất lượng:
- [Hướng dẫn bóc tách Blueprint tài liệu](file:///d:/repo/ba-zone/docs/guidelines/blueprint_extraction_guide.md)
- [Bảng kiểm định chất lượng 20 điểm cho Use Case](file:///d:/repo/ba-zone/docs/guidelines/use_case_quality_checklist.md)
- [Quy chuẩn hành văn Use Case theo Cockburn](file:///d:/repo/ba-zone/docs/guidelines/use_case_writing_style.md)
- [Cẩm nang tiêu chuẩn INVEST cho User Story](file:///d:/repo/ba-zone/docs/guidelines/invest_criteria_guide.md)
- [Checklist tự rà soát User Story & AC](file:///d:/repo/ba-zone/docs/guidelines/user_story_quality_checklist.md)
