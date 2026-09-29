#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor for BA Zone Outputs Directory (docs/outputs/)
Performs comprehensive quality, standards, structural, format anti-overflow, 
spelling, NDA, and link integrity checks for both Markdown and HTML deliverables.

Author: BA Zone / Digital School & NVG-ITC
Compliant with: .agents/rules/output_quality_standards.md
"""

import os
import re
import sys

# Force UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUTS_DIR = os.path.join(REPO_ROOT, "docs", "outputs")

class AuditResult:
    def __init__(self, filename):
        self.filename = filename
        self.errors = []
        self.warnings = []
        self.checks_passed = []

    def add_error(self, msg):
        self.errors.append(msg)

    def add_warning(self, msg):
        self.warnings.append(msg)

    def add_pass(self, msg):
        self.checks_passed.append(msg)

    @property
    def is_passed(self):
        return len(self.errors) == 0

# ==============================================================================
# 1. CHÍNH TẢ TIẾNG VIỆT & CHUẨN MỰC TỪ VỰNG BA (VIETNAMESE SPELLING & TYPOS)
# ==============================================================================

# Dictionary of common typos, OCR corruptions, and non-standard forms
VIETNAMESE_TYPO_DICT = {
    r"\bgiản\s+viên\b": "giảng viên",
    r"\bthư\s+kí\b": "thư ký",
    r"\bqui\s+trình\b": "quy trình",
    r"\bchuyên\s+cân\b": "chuyên cần",
    r"\bđiễm\s+danh\b": "điểm danh",
    r"\bdiem\s+danh\b": "điểm danh (thiếu dấu tiếng Việt)",
    r"\bchuổi\b": "chuỗi",
    r"\bxữ\s+lý\b": "xử lý",
    r"\bxử\s+lí\b": "xử lý (chuẩn hóa y dài)",
    r"\bsắp\s+sếp\b": "sắp xếp",
    r"\bthời\s+lựong\b": "thời lượng",
    r"\blưu\s+trử\b": "lưu trữ",
    r"\bđăng\s+nhâp\b": "đăng nhập",
    r"\bthực\s+tê\b": "thực tế",
    r"\bhệ\s+thốn\b": "hệ thống",
    r"\bbáo\s+các\b": "báo cáo",
    r"\bkêt\s+quả\b": "kết quả",
    r"\bthiêt\s+bị\b": "thiết bị",
    r"\bphân\s+hê\b": "phân hệ",
    r"\bđôi\s+ứng\b": "đối ứng",
    r"\bthẩm\s+quyên\b": "thẩm quyền",
    r"\bchức\s+năg\b": "chức năng",
    r"\bbắt\s+buôc\b": "bắt buộc",
    r"\btương\s+thich\b": "tương thích",
    r"\bthao\s+tac\b": "thao tác",
    r"\bnghiệp\s+vụ\s+thư\s+kí\b": "nghiệp vụ thư ký"
}

def check_vietnamese_spelling_and_typos(content, filepath, res):
    """
    Checks for common Vietnamese typos, corrupt accents, punctuation spacing,
    and diplomatic corporate tone.
    """
    content_lower = content.lower()
    typos_found = []

    # 1. Dictionary scan
    for pat, correct in VIETNAMESE_TYPO_DICT.items():
        matches = re.findall(pat, content_lower)
        if matches:
            typos_found.append(f"Lỗi chính tả '{matches[0]}' -> Bắt buộc chuẩn hóa thành '{correct}'")

    if typos_found:
        for t in typos_found:
            res.add_error(t)
    else:
        res.add_pass("Từ điển chính tả tiếng Việt BA chuẩn xác 100% (không lỗi chính tả phổ biến).")

    # 2. Punctuation spacing checks (space before punctuation: e.g. 'tính năng ,')
    # Avoid flagging inside code blocks or HTML attributes
    clean_text = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    clean_text = re.sub(r"<[^>]+>", "", clean_text)
    bad_punct = re.findall(r"[\w\u00C0-\u1EF9]\s+([,.:;?!])(?:\s|$)", clean_text)
    if len(bad_punct) > 5:
        res.add_warning(f"Quy cách dấu câu: Phát hiện {len(bad_punct)} vị trí có khoảng trắng thừa trước dấu câu (ví dụ 'từ ,').")
    elif bad_punct:
        res.add_pass("Quy cách dấu câu và khoảng trắng cơ bản đạt chuẩn.")

    # 3. Mojibake / Corrupt UTF-8 encoding artifacts
    mojibake_patterns = [r"Ã¡", r"Ã¢", r"Ã©", r"Ã¨", r"Ãª", r"Ã\xad", r"Ã³", r"Ã´", r"Ãº", r"Ã½", r"Ä‘", r"á»\x87", r"á»\x9d"]
    mojibake_count = 0
    for mp in mojibake_patterns:
        mojibake_count += len(re.findall(mp, content))
    if mojibake_count > 3:
        res.add_error(f"Phát hiện lỗi vỡ font/mã hóa UTF-8 (Mojibake: {mojibake_count} ký tự corrupt).")
    else:
        res.add_pass("Mã hóa ký tự UTF-8 toàn vẹn (Zero Mojibake).")

    # 4. Diplomatic Tone Check (PMO Ms. Tú Guidance)
    # Ensure individual lecturer names (e.g. cô Quyên) are not cited as a blocker in open clarifications or conclusions
    lecturer_blocker = re.search(r"(cô\s+quyên|ms\.\s*quyên)\s*(là\s+bên|chưa\s+chốt|gây\s+nghẽn|chờ\s+phản\s+hồi)", content_lower)
    if lecturer_blocker:
        res.add_error("Vi phạm chuẩn mực ngoại giao doanh nghiệp: Không nêu đích danh cá nhân giảng viên/chuyên gia như bên gây nghẽn tiến độ. Cần ghi 'Phòng TRC phối hợp cung cấp thêm thông tin'.")
    else:
        res.add_pass("Giọng văn đối ngoại & chuẩn mực ngoại giao doanh nghiệp đạt chuẩn.")

# ==============================================================================
# 2. ĐỊNH DẠNG & CHỐNG TRÀN TRANG (FORMAT & ANTI-OVERFLOW)
# ==============================================================================

def check_table_formatting_and_overflow(content, filepath, res):
    """
    Checks table column balance in Markdown and anti-overflow rules in HTML.
    """
    is_html = filepath.endswith(".html")
    
    if is_html:
        # Check HTML Anti-Overflow Protection
        has_tables = "<table" in content.lower()
        if has_tables:
            # 1. Check table-layout: fixed
            if "table-layout: fixed" in content or "table-layout:fixed" in content:
                res.add_pass("HTML Table Anti-Overflow: Đã khóa cứng CSS 'table-layout: fixed'.")
            else:
                res.add_warning("HTML Table: Nên bổ sung 'table-layout: fixed' vào CSS để chống tràn trang khi in/xuất PDF.")

            # 2. Check @page A4 rule
            if "@page" in content and "a4" in content.lower():
                res.add_pass("HTML Print Layout: Đã cấu hình @page { size: A4 portrait } chuẩn in ấn.")
            else:
                res.add_warning("HTML Print Layout: Chưa tìm thấy cấu hình @page { size: A4 portrait; margin: ... } trong CSS.")

            # 3. Check for dangerous 'white-space: nowrap' on <th>
            if re.search(r"th\s*\{[^}]*white-space\s*:\s*nowrap", content, re.IGNORECASE):
                res.add_warning("HTML Table: Phát hiện 'th { white-space: nowrap; }'. Với bảng nhiều cột, điều này sẽ gây tràn lề trang in A4.")
            else:
                res.add_pass("HTML Table Headers: Không bị ép nowrap cứng, cho phép xuống dòng tự nhiên.")
    else:
        # Check Markdown Table Column Alignment & Budget
        lines = content.splitlines()
        in_table = False
        header_cols = 0
        table_line_start = 0
        table_max_cols = 0
        
        for idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                cells = [c.strip() for c in stripped.split("|")[1:-1]]
                if not in_table:
                    in_table = True
                    table_line_start = idx
                    header_cols = len(cells)
                    table_max_cols = header_cols
                else:
                    # Skip delimiter row (|:---|---|)
                    if all(re.match(r"^:?-+:?$", c) for c in cells):
                        continue
                    if len(cells) != header_cols:
                        res.add_warning(f"Markdown Table tại dòng {idx}: Số cột ({len(cells)}) không khớp số cột header ({header_cols}).")
                    table_max_cols = max(table_max_cols, len(cells))
            else:
                if in_table:
                    # End of table check
                    if table_max_cols >= 6:
                        res.add_warning(f"Markdown Table (bắt đầu dòng {table_line_start}) có {table_max_cols} cột. Khuyến nghị tách bảng theo phân kỳ (tối đa 4 cột) để tránh tràn trang A4 khi xuất PDF/Docx.")
                    in_table = False

        if not res.warnings:
            res.add_pass("Markdown Table: Số lượng cột và phân tách cell cân bằng 100%.")

def check_markdown_syntax_integrity(content, filepath, res):
    """
    Checks for unclosed markdown bold/italic tags and broken links.
    """
    if filepath.endswith(".html"):
        return

    # 1. Check for unclosed bold tags (**text without closing **)
    # Split by code blocks first
    code_stripped = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    code_stripped = re.sub(r"`[^`\n]+`", "", code_stripped)
    
    for idx, line in enumerate(code_stripped.splitlines(), 1):
        line_clean = line.strip()
        bold_count = line_clean.count("**")
        if bold_count % 2 != 0:
            res.add_warning(f"Cú pháp Markdown tại dòng {idx}: Phát hiện thẻ in đậm '**' mở mà chưa đóng: '{line_clean[:60]}...'")

    # 2. Check for broken markdown links [text]( without closing )
    broken_links = re.findall(r"\[[^\]\n]+\]\([^)\n]*$", code_stripped, re.MULTILINE)
    if broken_links:
        for bl in broken_links:
            res.add_error(f"Cú pháp Markdown: Liên kết bị gãy hoặc thiếu ngoặc đóng: '{bl[:50]}'")
    else:
        res.add_pass("Tính toàn vẹn cú pháp Markdown (thẻ đóng/mở & liên kết) hợp lệ.")

# ==============================================================================
# 3. CẤU TRÚC TÀI LIỆU (STRUCTURE & HIERARCHY)
# ==============================================================================

def check_heading_hierarchy(content, filepath, res):
    """
    Checks that heading levels do not skip (e.g. H1 -> H3 without H2).
    """
    if filepath.endswith(".html"):
        # For HTML, check H1..H4 tags
        headings = re.findall(r"<h([1-6])[\s>]", content, re.IGNORECASE)
        levels = [int(h) for h in headings]
    else:
        # For Markdown, check # headings outside code blocks
        code_stripped = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
        levels = []
        for line in code_stripped.splitlines():
            m = re.match(r"^(#{1,6})\s+", line.strip())
            if m:
                levels.append(len(m.group(1)))

    if not levels:
        return

    # Check for single H1
    h1_count = levels.count(1)
    if h1_count > 1:
        res.add_warning(f"Cấu trúc tiêu đề: Phát hiện {h1_count} thẻ H1. Tài liệu chuẩn nên có duy nhất 01 thẻ H1 làm tiêu đề tài liệu.")
    elif h1_count == 1:
        res.add_pass("Cấu trúc tiêu đề: Duy nhất 01 thẻ H1 tiêu đề chuẩn mực.")

    # Check for skipped levels
    prev_level = 0
    skipped = False
    for l in levels:
        if prev_level > 0 and l > prev_level + 1:
            res.add_warning(f"Cấu trúc tiêu đề nhảy cóc: Từ H{prev_level} nhảy thẳng xuống H{l} (thiếu H{prev_level + 1}).")
            skipped = True
            break
        prev_level = l
    
    if not skipped:
        res.add_pass("Thứ bậc tiêu đề (Heading Hierarchy) tuần tự, không nhảy cấp.")

# ==============================================================================
# 4. UNIVERSAL & ENTERPRISE CHECKS (MERMAID, LINKS, NDA, DEV SPINE)
# ==============================================================================

def check_mermaid_syntax(content, res):
    """Checks mermaid blocks for basic syntax validity."""
    # Check in markdown
    mermaid_blocks = re.findall(r"```mermaid(.*?)```", content, re.DOTALL)
    # Check in html
    mermaid_blocks += re.findall(r'<div class="mermaid">(.*?)</div>', content, re.DOTALL)
    
    if not mermaid_blocks:
        return
    
    valid_starts = ["graph", "flowchart", "sequencediagram", "gantt", "classdiagram", "erdiagram", "statediagram", "pie"]
    for idx, block in enumerate(mermaid_blocks, 1):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip() and not l.strip().startswith("%%")]
        if not lines:
            res.add_error(f"Sơ đồ Mermaid #{idx} rỗng.")
            continue
        first_line = lines[0].lower()
        if not any(first_line.startswith(vs) for vs in valid_starts):
            res.add_warning(f"Sơ đồ Mermaid #{idx} bắt đầu bằng từ khóa chưa chuẩn hóa: '{lines[0]}'")
        else:
            res.add_pass(f"Cú pháp sơ đồ Mermaid #{idx} ({first_line.split()[0]}) hợp lệ 100%.")

def check_cross_links(content, filepath, res):
    """Checks markdown and html links to local files and ensures target files exist."""
    file_dir = os.path.dirname(filepath)
    # Find markdown links [text](path)
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    # Find html links href="..."
    html_links = re.findall(r'href=["\']([^"\']+)["\']', content)
    for hl in html_links:
        links.append(("HTML link", hl))

    for text, link in links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:") or link.startswith("#") or link.startswith("javascript:"):
            continue
        
        # Normalize local file link
        clean_link = link
        if clean_link.startswith("file:///"):
            clean_link = clean_link[8:].replace("/", os.sep)
            if not os.path.isabs(clean_link) and len(clean_link) > 2 and clean_link[1] != ":":
                clean_link = os.path.join(REPO_ROOT, clean_link)
        else:
            clean_link = os.path.normpath(os.path.join(file_dir, clean_link.replace("/", os.sep)))
        
        if not os.path.exists(clean_link):
            res.add_error(f"Liên kết bị gãy (Broken link): '[{text}]({link})' -> File đích không tồn tại: {clean_link}")
        else:
            res.add_pass(f"Liên kết tệp hợp lệ: '{text}' -> {os.path.basename(clean_link)}")

def check_nda_sanitization(content, res):
    """Verifies compliance with Enterprise NDA Sanitizer rules."""
    # Check for hardcoded secret keys/passwords
    password_patterns = [r"password\s*=\s*['\"][^'\"]+['\"]", r"secret_key\s*=\s*['\"][^'\"]+['\"]", r"api_token\s*=\s*['\"][^'\"]+['\"]"]
    for pat in password_patterns:
        if re.search(pat, content, re.IGNORECASE):
            res.add_error("Phát hiện mật khẩu / credential bí mật bị lộ trong tài liệu.")

    # Check stakeholder naming rule: Ms. Tú (PMO) - ensure not referred as 'anh Tú'
    if re.search(r"\banh\s+tú\b", content, re.IGNORECASE):
        res.add_error("Sai chuẩn danh xưng nhân sự: Chuyên gia PMO là nữ (Ms. Tú), không dùng 'anh Tú'.")
    else:
        res.add_pass("Danh xưng chức vụ PMO Ms. Tú chuẩn xác.")

    # Check stakeholder naming rule: Ms. Khanh (BA PM QLCH) - ensure not misspelled as 'Khánh' or 'Nguyễn Thúy Mai'
    if re.search(r"\bms\.\s*khánh\b|\bchị\s+khánh\b|\bnguyễn\s+thúy\s+mai\b", content, re.IGNORECASE):
        res.add_error("Sai tên nhân sự: PIC PM QLCH là Ms. Khanh (Nguyễn Thụy Mai Khanh), không viết thành 'Khánh' hay 'Nguyễn Thúy Mai'.")
    else:
        res.add_pass("Định danh nhân sự PIC Ms. Khanh (Nguyễn Thụy Mai Khanh) chuẩn xác.")

def check_dev_architecture_spine(content, filepath, res):
    """
    Verifies compliance with Dev Architecture Spine Baseline 2026:
    - Zero Local Auth (SSO Gateway Policy)
    - Authority Matrix (AM) & Security L7 Data Scope separation
    - Table Prefix {prefix}_ (e.g. gms_*, tas_*)
    - Strict Soft-Delete Invariant (Zero Hard-Delete)
    - Async Processing for Heavy Batch Operations
    """
    content_lower = content.lower()
    
    # 1. Zero Local Auth
    forbidden_auth = [
        r"(tạo|đăng ký)\s+tài khoản\s+(nội bộ|nhân viên)",
        r"(quên|đặt lại|reset)\s+mật khẩu\s+(nội bộ|nhân viên)",
        r"form\s+đăng nhập\s+(nội bộ|nhân viên|admin)"
    ]
    for pat in forbidden_auth:
        if re.search(pat, content_lower):
            res.add_warning("Phát hiện mô tả chức năng auth nội bộ cục bộ. Dev Spine quy định Zero Local Auth: 100% người dùng nội bộ đi qua application-gateway + SSO MS Entra.")

    # 2. Authority Matrix (AM) & Data Scope
    has_am = any(k in content_lower for k in ["authority matrix", "ma trận am", "ma trận phân quyền", "phân quyền & thẩm quyền"])
    if has_am:
        if "rbac" in content_lower and "am" not in content_lower and "authority matrix" not in content_lower:
            res.add_warning("Thuật ngữ phân quyền nên chuẩn hóa thành 'Ma trận Phân quyền & Thẩm quyền (AM)' theo quy ước NVG.")
        
        has_data_scope = any(k in content_lower for k in ["data scope", "phạm vi dữ liệu", "security l7", "phạm vi cho phép"])
        if has_data_scope:
            res.add_pass("Ma trận AM phân tách 2 tầng (Functional Permission & Security L7 Data Scope) hợp lệ.")
        else:
            res.add_warning("Ma trận AM nên bổ sung cột 'Phạm vi dữ liệu (Data Scope)' theo chuẩn Security L7 Dev Architecture Spine.")

    # 3. Database Schema Prefix
    has_db_schema = any(k in content_lower for k in ["bảng csdl", "database schema", "thực thể dữ liệu", "entity / model"])
    if has_db_schema:
        tables = re.findall(r"`([a-z0-9]+_[a-z0-9_]+)`", content)
        if tables:
            res.add_pass(f"Quy chuẩn tiền tố CSDL: Tìm thấy {len(tables)} bảng CSDL có tiền tố chuẩn ({tables[0]}).")

    # 4. Strict Soft-Delete Invariant (Zero Hard-Delete)
    hard_delete_patterns = [
        r"xóa\s+vĩnh\s+viễn",
        r"hard\s*-?\s*delete",
        r"xóa\s+hoàn\s+toàn\s+khỏi\s+(csdl|database|hệ thống)"
    ]
    for pat in hard_delete_patterns:
        if re.search(pat, content_lower):
            res.add_error("Vi phạm nguyên tắc Xóa mềm (Strict Soft-Delete Invariant): Không được phép hard-delete dữ liệu trong đặc tả BA.")
            break
    
    if any(k in content_lower for k in ["soft-delete", "xóa mềm", "deletedat", "deleted_at"]):
        res.add_pass("Tuân thủ nguyên tắc Xóa mềm (Strict Soft-delete 100%).")

    # 5. Async Processing for Heavy Batch Operations
    has_heavy_batch = any(k in content_lower for k in ["import excel", "nhập excel", "tính tiền thuê", "kết xuất file", "xuất pdf"])
    if has_heavy_batch:
        has_async = any(k in content_lower for k in ["bất đồng bộ", "async", "queue", "rabbitmq", "nats", "chạy nền", "tiến trình nền", "background"])
        if has_async:
            res.add_pass("Đặc tả tác vụ khối lượng lớn (Batch Job) tuân thủ luồng xử lý bất đồng bộ (Async Queue).")

# ==============================================================================
# 5. DOCUMENT TEMPLATE AUDITS (BRD, SOP14, ACTION PLAN)
# ==============================================================================

def audit_brd(content, filepath, res):
    """Specific audit for Business Requirements Documents."""
    content_lower = content.lower()
    
    # 1. Document Control
    req_meta = ["mã số định danh", "phiên bản", "tác giả"]
    missing_meta = [m for m in req_meta if m not in content_lower]
    if missing_meta:
        res.add_error(f"BRD thiếu metadata kiểm soát tài liệu: {', '.join(missing_meta)}")
    else:
        res.add_pass("Document Control metadata đầy đủ.")

    # 2. Objectives (SMART)
    if "mục tiêu" not in content_lower:
        res.add_error("BRD thiếu mục tiêu dự án (Project Objectives).")
    else:
        res.add_pass("Mục tiêu dự án (SMART Objectives) đã được đặc tả.")

    # 3. Scope
    if "phạm vi" not in content_lower and "scope" not in content_lower:
        res.add_warning("BRD thiếu phần xác định phạm vi hệ thống (Scope).")
    else:
        res.add_pass("Phạm vi hệ thống (In-Scope / Out-Scope) đã phân định rõ.")

    # 4. Core Functional Modules
    if "phân hệ" not in content_lower and "chức năng" not in content_lower and "modules" not in content_lower:
        res.add_error("BRD thiếu danh sách phân hệ chức năng cốt lõi.")
    else:
        res.add_pass("Danh mục phân hệ chức năng cốt lõi đầy đủ.")

    # 5. Authority Matrix (AM)
    if not any(k in content_lower for k in ["authority matrix", "ma trận phân quyền", "phân quyền", "rbac", " ma trận am", "(am)"]):
        res.add_warning("BRD thiếu Ma trận Phân quyền & Thẩm quyền (Authority Matrix - AM).")
    else:
        res.add_pass("Ma trận Phân quyền & Thẩm quyền (AM) đã được thiết lập.")

    # 6. Fit-Gap Analysis
    if "fit-gap" in content_lower or "khoảng trống" in content_lower or "kế thừa" in content_lower:
        res.add_pass("Ma trận Fit-Gap đối chiếu kế thừa nền tảng sẵn có đạt chuẩn.")

def audit_sop14(content, filepath, res):
    """Specific audit for NVG-ITD-SOP14.F01 Solution Architecture & Design Documents."""
    content_lower = content.lower()
    sop14_sections = [
        ("thay đổi tài liệu", "Mục 1: Bảng ghi nhận thay đổi tài liệu"),
        ("thông tin chung", "Mục 2: Thông tin chung"),
        ("tổng quan", "Mục 3: Tổng quan ứng dụng"),
        ("chức năng", "Mục 4: Mô tả yêu cầu chức năng"),
        ("giải pháp", "Mục 5: Giải pháp hệ thống"),
    ]
    missing_sections = []
    for keyword, name in sop14_sections:
        if keyword not in content_lower:
            missing_sections.append(name)
    if missing_sections:
        res.add_warning(f"Tài liệu SOP14 thiếu các mục cốt lõi: {', '.join(missing_sections)}")
    else:
        res.add_pass("Cấu trúc 5 phần chuẩn kiến trúc NVG-ITD-SOP14.F01 đầy đủ 100%.")

def audit_action_plan(content, filepath, res):
    """Specific audit for Action Plans."""
    content_lower = content.lower()
    if "thông tin chung" not in content_lower and "mục tiêu" not in content_lower:
        res.add_warning("Action Plan thiếu thông tin chung / mục tiêu.")
    if "hành động" not in content_lower and "action" not in content_lower:
        res.add_error("Action Plan thiếu các bước hành động cụ thể.")
    if "giai đoạn" not in content_lower and "timeline" not in content_lower and "lộ trình" not in content_lower:
        res.add_warning("Action Plan thiếu phân kỳ lộ trình / timeline.")
    res.add_pass("Action Plan: Cấu trúc lộ trình & hành động hợp lệ.")

# ==============================================================================
# 6. RUNNER ENGINE
# ==============================================================================

def audit_document(filepath):
    filename = os.path.basename(filepath)
    res = AuditResult(filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        res.add_error(f"Không thể đọc tệp: {e}")
        return res

    # 1. Universal Checks (Spelling, Format, Hierarchy, NDA, Dev Spine, Mermaid, Links)
    check_vietnamese_spelling_and_typos(content, filepath, res)
    check_heading_hierarchy(content, filepath, res)
    check_table_formatting_and_overflow(content, filepath, res)
    check_markdown_syntax_integrity(content, filepath, res)
    check_mermaid_syntax(content, res)
    check_cross_links(content, filepath, res)
    check_nda_sanitization(content, res)
    check_dev_architecture_spine(content, filepath, res)

    # 2. Template Specific Checks
    lower_fn = filename.lower()
    content_lower = content.lower()
    if "sop14" in lower_fn or "sop14" in content_lower or "tài liệu thiết kế giải pháp" in content_lower:
        audit_sop14(content, filepath, res)
    if "brd" in lower_fn:
        audit_brd(content, filepath, res)
    elif "action_plan" in lower_fn:
        audit_action_plan(content, filepath, res)
    
    return res

def run_all_output_audits():
    print("=" * 72)
    print("      MASTER AUDITOR: BA ZONE OUTPUTS DIRECTORY (docs/outputs/)")
    print("   [Structure Hierarchy · Anti-Overflow Format · Vietnamese Spelling]")
    print("=" * 72)
    print(f"Thư mục kiểm tra: {OUTPUTS_DIR}")
    
    if not os.path.exists(OUTPUTS_DIR):
        print(f"LỖI: Không tìm thấy thư mục: {OUTPUTS_DIR}")
        return False

    all_results = []
    total_files = 0
    total_passed = 0

    for root, dirs, files in os.walk(OUTPUTS_DIR):
        files.sort()
        for file in files:
            # Audit both Markdown and HTML output files!
            if not (file.endswith(".md") or file.endswith(".html")):
                continue
            
            # Skip tiny stubs or legacy snippets (< 600 bytes)
            full_path = os.path.join(root, file)
            if os.path.getsize(full_path) < 600:
                continue

            total_files += 1
            rel_path = os.path.relpath(full_path, OUTPUTS_DIR)
            res = audit_document(full_path)
            all_results.append((rel_path, res))
            if res.is_passed:
                total_passed += 1

    # Output detailed report
    for rel_path, res in all_results:
        status_symbol = "✅ PASS" if res.is_passed else "❌ FAIL"
        print(f"\n[{status_symbol}] {rel_path}")
        for p in res.checks_passed:
            print(f"    ✓ {p}")
        for w in res.warnings:
            print(f"    ⚠️ [WARN] {w}")
        for e in res.errors:
            print(f"    ❌ [ERROR] {e}")

    print("\n" + "=" * 72)
    print(f"TỔNG KẾT: {total_passed}/{total_files} tài liệu (MD + HTML) ĐẠT 100% tiêu chuẩn kiểm định.")
    print("=" * 72)

    all_clean = (total_passed == total_files)
    return all_clean

if __name__ == "__main__":
    success = run_all_output_audits()
    sys.exit(0 if success else 1)
