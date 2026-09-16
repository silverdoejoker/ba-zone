# Business Requirements Document (BRD)
# FPTShop Semantic Search

| Thông tin | Chi tiết |
|-----------|----------|
| **Dự án** | 3.22 FPTShop Semantic Search |
| **Đơn vị** | FPT Retail – AI ICT |
| **Space** | FRT-AI (FRTAI) |
| **Confluence** | [3.22 FPTShop Semantic Search](https://confluence.frt.vn/spaces/FRTAI/pages/214511972) |
| **Jira Project** | ASS (AI Semantic Search) |
| **Epic** | ASS-33 |
| **Phiên bản** | 2.0 |
| **Ngày tổng hợp** | 2026-05-13 |
| **Tác giả tổng hợp** | MinhTQA (AI-assisted) |

---

## 1. Tổng Quan Dự Án

### 1.1 Mục tiêu

Xây dựng hệ thống **Semantic Search** cho website FPTShop (fptshop.com.vn), kết hợp full-text search (Elasticsearch) và vector search (Milvus) để trả về kết quả sản phẩm **chính xác và phù hợp nhất** với ý định tìm kiếm của người dùng tiếng Việt.

### 1.2 Vấn đề cần giải quyết

- Hệ thống search cũ chỉ dựa trên keyword matching → không hiểu ngữ nghĩa
- ~15-20% query trả về 0 kết quả do lỗi chính tả
- Không xử lý được query theo nhu cầu ("điện thoại pin trâu", "laptop cho sinh viên")
- Không phân biệt được viết tắt, typo, synonym ("ss" = Samsung, "ip" = iPhone)
- Kết quả không ưu tiên sản phẩm đang kinh doanh, trả về sản phẩm đời cũ/ngừng KD

### 1.3 Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---------------|---------------|
| Search sản phẩm trên web FPTShop | Search dịch vụ (sim, thẻ, thu hộ) — Phase sau |
| Hỗ trợ tiếng Việt (có dấu/không dấu) | Đa ngôn ngữ |
| Auto-correct lỗi chính tả | Chatbot AI conversational |
| Synonym management từ CMS | Personalization theo user |
| Entity extraction (brand, price, attribute) | Recommendation engine |
| Business scoring & ranking | A/B testing framework |

---

## 2. Kiến Trúc Hệ Thống

### 2.1 Architecture Overview (v2.0)

Hệ thống áp dụng kiến trúc **Hybrid Search** kết hợp:
- **Elasticsearch** — tìm kiếm có cấu trúc (filter-based)
- **Milvus** — tìm kiếm ngữ nghĩa (vector-based)
- **FastAPI** — REST API, layered architecture với dependency injection

### 2.2 Search Pipeline

```
User Query
    ↓
┌─────────────────────────────────────┐
│ 1. PREPROCESSING                     │
│    • Auto-correct (Dictionary N-gram)│
│    • Remove stopwords                │
│    • Synonyms expansion              │
│    → Output: Query Rewritten         │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 2. ENTITY EXTRACTION (song song)     │
│                                       │
│  NER (Python):          Fuzzy Match: │
│  • fromPrice            • productType│
│  • toPrice              • brand      │
│  • approxPrice          • line       │
│  • attribute            • group      │
│  • target/demand                     │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 3. HYBRID SEARCH (song song)         │
│                                       │
│  Filter-based (ES):    Vector (Milvus)│
│  • Filter Builder      • Vectorize   │
│  • Rule-based Convert  • Embedding   │
│  • Search ES           • Search Milvus│
│  → ES Candidates       → Milvus Cand.│
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 4. MERGE, RE-RANK & BUSINESS SCORE   │
│    • Merge candidates                 │
│    • Re-rank (BGE model)             │
│    • Apply Business Score            │
│    • Filter & Group by UPC           │
│    → Final Result                    │
└─────────────────────────────────────┘
```

### 2.3 Tech Stack

| Component | Technology |
|-----------|-----------|
| API Framework | FastAPI (Python) |
| Full-text Search | Elasticsearch |
| Vector Search | Milvus |
| Embedding | Jina Embedding v5 (dim 1024) |
| Rerank | BGE Reranker m3 |
| NER | SpaCy v3 (custom trained) |
| Spell Check | Custom N-gram Dictionary |
| Cache | Redis |
| Monitoring | ELK LogCenter + Elastic APM |

### 2.4 External Services

| Service | Mô tả |
|---------|--------|
| NER API | Named Entity Recognition — trích xuất price, attribute, demand |
| Embedding API | Tạo vector embedding cho query |
| Rerank API | Re-rank candidates theo semantic relevance |
| SpellCheck API | Sửa lỗi chính tả |
| Redis | Cache embedding, NER, rerank results + reference data |

### 2.5 API Endpoints

| Method | Endpoint | Mô tả |
|--------|----------|--------|
| POST | `/search` | Tìm kiếm sản phẩm (endpoint chính) |
| POST | `/search/search_names` | Tìm kiếm tên sản phẩm |
| POST | `/search/spellcheck` | Kiểm tra chính tả |
| POST | `/search/preprocess` | Debug: xem kết quả tiền xử lý |
| POST | `/cache/clear` | Xóa/refresh cache |

### 2.6 Graceful Degradation

| Dependency | Khi không khả dụng |
|------------|---------------------|
| Redis | Bỏ qua cache, preprocess đơn giản hơn |
| Elasticsearch | FTS bị disable, trả kết quả rỗng |
| Milvus | Vector search bị skip, chỉ dùng FTS |
| NER API | Entity detection trả rỗng, chỉ dùng fuzzy |
| Embedding API | Skip vector search |
| Rerank API | Dùng merge score order + business rules |
| SpellCheck API | Trả về text gốc không sửa |

---

## 3. Business Scoring & Ranking

### 3.1 Nguyên tắc

Semantic Search giải quyết **đúng ngữ nghĩa**, còn Business Score quyết định **ưu tiên sản phẩm nào đứng trước** trong cùng một nhóm relevance.

### 3.2 Tiêu chí xếp hạng

| # | Tiêu chí | Mô tả |
|---|----------|--------|
| 1 | **Industry Boosting** | Ưu tiên: Điện thoại > Máy tính > Tablet > Phụ kiện > Đồng hồ > Điện máy > Gia dụng > Đồ chơi |
| 2 | **Status Boosting** | Ưu tiên: Mua ngay > Đặt cọc > Hàng sắp về > Sản phẩm chưa ra mắt > Ngừng KD > Không KD |
| 3 | **Release Time Boosting** | Sản phẩm ra mắt gần nhất đứng trước |
| 4 | **Price Weighting** | Điều chỉnh theo khoảng giá phù hợp intent |

### 3.3 Công thức

```
Business Score = industry_boosting_score + status_boosting_score + releaseTime_boosting_score
```

Kết quả search được classify thành clusters theo industry, sau đó apply Business Scoring cho từng cluster.

---

## 4. Use Cases

### 4.1 Tổng quan 9 Use Cases

| UC | Tên | Mô tả | Jira |
|----|-----|--------|------|
| UC-1 | Tìm kiếm sản phẩm trong đúng danh mục | Fulltext search cơ bản, match đúng category | — |
| UC-2 | Tự động sửa lỗi chính tả nhẹ | Spell check cho typo thông dụng | — |
| UC-3 | Điều chỉnh truy vấn bằng synonym từ CMS | Synonym expansion | ASS-98 |
| UC-4 | Trả đúng biến thể sản phẩm (SKU) theo UPC | Group kết quả theo UPC | — |
| UC-5 | Chuẩn hóa và tái cấu trúc truy vấn (Query Rewrite) | Core pipeline: preprocess → entity → search → rerank | ASS-97, ASS-101, ASS-103 |
| UC-6 | Đồng bộ từ khóa đồng nghĩa với CMS | Luồng sync synonym dictionary | ASS-98 |
| UC-7 | Nâng cao sửa lỗi chính tả phức tạp | Advanced spell check | ASS-99 |
| UC-8 | Tìm kiếm gần đúng theo model sản phẩm | Fuzzy matching model name | ASS-100 |
| UC-9 | Tracking keyword tìm kiếm của khách hàng | Logging & analytics | ASS-121 |

### 4.2 UC-5: Query Rewrite Layer (Core)

**Mục tiêu**: Chuẩn hóa và tái cấu trúc truy vấn người dùng trước khi đưa vào search engine.

**Pipeline**:
1. Preprocess câu query (normalize, remove stopwords)
2. Entity extraction (NER + Fuzzy)
3. Build câu query có filter và không filter
4. Ghép luồng semantic mới theo kiến trúc
5. Làm data cho Milvus (embedding)
6. Benchmark Rerank — ưu tiên sản phẩm theo semantic relevance
7. Fallback khi fulltext & semantic đều không có kết quả

---

## 5. Tiêu Chí Keyword Theo Nhu Cầu

### 5.1 Ngành hàng Điện thoại (từ 1,405 keyword thực tế)

| Demand | Tỷ lệ | Ví dụ keyword |
|--------|--------|---------------|
| **PIN** | ~35% (cao nhất) | "pin trâu", "pin lâu", "sạc nhanh", "pin 2-3 ngày" |
| **HIỆU NĂNG** | ~25% | "chơi game mạnh", "mượt", "chip mạnh" |
| **CAMERA** | ~20% | "chụp ảnh đẹp", "camera zoom", "quay video 4K" |
| **GIÁ** | ~15% | "giá rẻ", "dưới 5 triệu", "tầm 20 triệu" |
| **THIẾT KẾ** | ~5% | "mỏng nhẹ", "màu hồng", "gập" |

### 5.2 Ngành hàng Laptop & MacBook

Tương tự phân loại theo: hiệu năng, pin, màn hình, trọng lượng, giá.

### 5.3 Ngành hàng Máy tính bảng

Phân loại theo: học tập, giải trí, pin, màn hình lớn, có bút.

---

## 6. Kết Quả Benchmark & Testing

### 6.1 Test Round 1 — 92 keywords (CI Environment)

| Kết quả | Số case | Tỷ lệ |
|---------|---------|--------|
| ✅ Passed (100% relevant) | 31 | ~34% |
| 🟡 Partial (đúng category, lẫn sản phẩm) | 28 | ~30% |
| 🔴 Failed (sai hoàn toàn) | 33 | ~36% |

### 6.2 Test Round BU — 195 keywords (CI Environment)

| Kết quả | Số case | Tỷ lệ |
|---------|---------|--------|
| ✅ OK / Partial | 181 | 92.8% |
| 🔴 Failed | 14 | 7.2% |

### 6.3 Phân loại nguyên nhân lỗi chính

| Nhóm lỗi | Mô tả | Ví dụ |
|----------|--------|-------|
| **Không lọc được giá** | Query có giá nhưng không filter | "tab dưới 5tr", "nồi dưới 500k" |
| **Match sai từ khóa** | Match attribute thay vì category | "sạc ip 15" → match "15W", "Key office" → match bàn phím |
| **Thiếu sản phẩm / 0-1 kết quả** | Query hợp lệ nhưng trả quá ít | "đồng hồ định vị trẻ em" → 1 kết quả |
| **Lẫn sản phẩm sai category** | Trả sản phẩm khác loại | "điện thoại pin khoẻ" → pin sạc dự phòng |
| **Sản phẩm đời cũ/ngừng KD** | Không ưu tiên sản phẩm hiện hành | "Samsung" → J7 Prime, C9 Pro |
| **Sai brand** | Đúng category nhưng sai thương hiệu | "ss watch" → OPPO Watch |
| **Typo không xử lý** | Typo phức tạp không được map | "máy tính bản samsung", "ảipod" |
| **Trả máy thay vì phụ kiện** | Ngược lại intent | "Dây sạc iphone 14" → iPhone 14 |

---

## 7. Roadmap & Phases

### Phase 1 (Completed)
- Fulltext search cơ bản trên Elasticsearch
- Các issue: viết tắt dính liền ("zfold"), thiếu model name, sort sai giá

### Phase 2 (Current — Sprint 2)
- Tích hợp Semantic Search (Milvus + Embedding)
- Query Rewrite Layer (UC-5)
- Spell Check nâng cao (UC-7)
- Fuzzy matching model (UC-8)
- Synonym management (UC-6)
- Keyword tracking (UC-9)

### Phase 3 (Planned)
- Search ngữ nghĩa nâng cao cho máy mới
- Search cho dịch vụ (Sim, FPT Play, thu hộ)
- Agentic Data Generation Pipeline
- Attribute classification per category (Filter Builder vs Vectorize)

---

## 8. Document Tree — Confluence

```
3.22 FPTShop Semantic Search (ID: 214511972)
├── 3.22.1 Architecture (218015059)
│   └── 3.22.1.1 Architecture version 2.0 (283251244)
├── 3.22.2 Service API (271209688)
├── 3.22.3 Proposal (233158465)
│   ├── Agentic Data Generation Pipeline (not approved) (263586550)
│   ├── Hybrid Search Solution (not approved) (216798110)
│   └── Workflow & Architecture Phase 2 (approved) (257334007)
├── 3.22.4 Technical Document (233158457)
│   ├── 1. Search Pipeline (271209727)
│   ├── 2. Vietnamese Spell Check (255925759)
│   ├── 3. Query Elastics Search Document (230294032)
│   ├── Embedding Service (273024878)
│   ├── Entity (278692761)
│   ├── NER Service (273024836)
│   └── Rerank Serving (273024834)
├── 3.22.5 Benchmark (233158468)
│   ├── Benchmark Embedding Jina v5 (271198499)
│   ├── Benchmark Rerank BGE m3 (271208559)
│   ├── Display Criteria: Tiêu chí hiển thị (220794254)
│   ├── Kết quả benchmark Milvus (241440102)
│   ├── Kết quả finetune SpaCy-v3-ner (246489625)
│   ├── Metrics đánh giá (216806079)
│   ├── Root Cause Analysis Report (276597591)
│   ├── Search Benchmark (218936635)
│   └── Tiêu chí Rubric đánh giá kết quả search (224434893)
├── 3.22.6 BA Documents (273023014)
│   ├── 3.22.6.1 Business Scoring & Total Scoring (225353367)
│   ├── 3.22.6.2 Roadmap Semantic Search (218016247)
│   ├── 3.22.6.3 Auto Correct: Sửa lỗi Typo (241436410)
│   ├── 3.22.6.4 Quản lý từ khóa đồng nghĩa CMS (246480916)
│   ├── 3.22.6.5 Quản lý luồng cập nhật Dictionary (246483415)
│   ├── 3.22.6.6 Tìm kiếm theo nhu cầu v1.0 (254905125)
│   └── 3.22.6.7 Use Cases (273023035)
│       ├── UC-1: Tìm kiếm đúng danh mục (273023272)
│       ├── UC-2: Sửa lỗi chính tả nhẹ (273023274)
│       ├── UC-3: Synonym từ CMS (273023275)
│       ├── UC-4: Trả đúng SKU/UPC (273023276)
│       ├── UC-5: Query Rewrite Layer (273023277)
│       ├── UC-6: Đồng bộ synonym CMS (273023278)
│       ├── UC-7: Sửa lỗi chính tả phức tạp (273023279)
│       ├── UC-8: Tìm kiếm gần đúng model (273023280)
│       └── UC-9: Tracking keyword (273023410)
├── 3.22.7 Tiêu chí keyword — Điện thoại (281939338)
├── 3.22.8 Tiêu chí keyword — Laptop & MacBook (281942973)
├── 3.22.9 Phân loại Attributes Điện thoại (281943123)
├── 3.22.10 Phân loại Attributes Laptop (281943211)
├── 3.22.11 Phân loại Attributes Máy tính bảng (281943940)
└── 3.22.12 Tiêu chí keyword — Máy tính bảng (281944885)
```

---

## 9. Jira Sprint Status

### Sprint 2 — [AI Semantic Search] Sprint 2

| Metric | Giá trị |
|--------|---------|
| Tổng tickets | 34 |
| Completed | 12 (35.3%) |
| In CI Testing | 4 |
| Analyzing (bug chưa xử lý) | 15 |
| Re-open | 1 |
| Dự kiến Go-live | 2026-05-15 |

### Bug Backlog

- 15 bug đang ANALYZING — toàn bộ assign Trịnh Xuân Lương
- ~25 bug mới dự kiến từ testing R1 (50 case failed, ~50% valid)
- Tổng bug cần fix ước tính: ~40

---

## 10. Stakeholders & Team

| Vai trò | Người |
|---------|-------|
| Product Owner | DienLQ2 |
| Tech Lead | Trịnh Xuân Lương (luongtx2) |
| QA Lead | LuyenNTT, PhongVV2 |
| BA | MinhTQA |
| Dev | Trịnh Xuân Lương, Lê Ngọc Tường |

---

## 11. Rủi Ro & Đề Xuất

| # | Rủi ro | Mức độ | Đề xuất |
|---|--------|--------|---------|
| 1 | 15 bug ANALYZING dồn 1 người | 🔴 Cao | Phân tải bug cho thêm dev |
| 2 | ~25 bug mới sắp vào từ R1 | 🔴 Cao | Tăng capacity hoặc dời go-live |
| 3 | Typo phức tạp chưa xử lý được | 🟡 TB | Mở rộng dictionary, thêm rule |
| 4 | Không filter được giá trong query | 🟡 TB | Cải thiện NER price extraction |
| 5 | Match sai category (pin khoẻ → pin sạc) | 🟡 TB | Cải thiện entity disambiguation |
| 6 | Sản phẩm đời cũ vẫn xuất hiện | 🟢 Thấp | Tăng weight status_boosting |

---

## 12. Tham Chiếu

| Tài liệu | Link |
|-----------|------|
| Confluence Space | https://confluence.frt.vn/spaces/FRTAI |
| Jira Project ASS | https://reqs.frt.vn/projects/ASS |
| CI Environment | https://ci-estore-v2.fptshop.com.vn |
| Search API (CI) | http://ci-semantic-search.ict.frt.local/search |
| Architecture v2.0 | https://confluence.frt.vn/spaces/FRTAI/pages/283251244 |
| Use Cases | https://confluence.frt.vn/spaces/FRTAI/pages/273023035 |
| Benchmark Results | https://confluence.frt.vn/spaces/FRTAI/pages/233158468 |

---

*Tài liệu này được tổng hợp tự động từ Confluence space FRTAI, Jira project ASS, và dữ liệu test trong workspace. Nội dung phản ánh trạng thái dự án tính đến ngày 2026-05-13.*
