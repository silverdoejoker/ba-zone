import os
import sys
import zipfile
import xml.etree.ElementTree as ET

file_path = r"d:\repo\ba-zone\docs\outputs\KPI - CVCC Phân tích Nghiệp vụ - 38108.xlsx"
backup_path = r"d:\repo\ba-zone\docs\outputs\KPI - CVCC Phân tích Nghiệp vụ - 38108_backup.xlsx"
log_path = r"d:\repo\ba-zone\scratch\fill_kpi.log"

def log(msg):
    print(msg)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

if os.path.exists(log_path):
    os.remove(log_path)

log(f"Starting KPI fill script for: {file_path}")

content_c13 = """Phân tích, Xác định Yêu cầu Nghiệp vụ của các dự án (Kỳ thử việc: 07/09/2026 - 05/11/2026):

1. Hệ thống Quản lý & Điểm danh Đào tạo (TAS - REF-TAS-2026):
- Khảo sát hiện trạng & phân tích Fit-Gap: Tiếp nhận bài toán, cài đặt App OneNova UAT; chủ trì họp Demo & khảo sát nhu cầu Khối Đào tạo; hoàn thành phân tích Fit-Gap (kế thừa PM Quản lý Cuộc họp) và Biên bản cuộc họp (MoM) (Hoàn thành trước 22/09/2026).
- Hoàn thành Yêu cầu Nghiệp vụ (BRD): Xây dựng và trình ký phê duyệt BRD Official v2.0 (REF-TAS-2026) được Giám đốc CĐS, PMO và Khối Đào tạo thống nhất nghiệm thu (Hoàn thành trước 02/10/2026).
- Hoàn thành Giải pháp Hệ thống (SRS): Biên soạn bộ Đặc tả SRS chi tiết (Use Cases, User Stories INVEST) cho các tính năng Core (Quản lý lịch đào tạo, Sinh trắc FaceID/NFC, Báo vắng Teams Bot, Đồng bộ E-Office) kèm Ma trận AM bàn giao Đội Dev (Hoàn thành trước 18/10/2026).
- Chuẩn bị Hồ sơ Kiểm thử Nghiệm thu (UAT Package): Xây dựng Ma trận kịch bản kiểm thử (UAT Test Cases Matrix phủ 100% Use Cases) và Tài liệu Hướng dẫn sử dụng (User Guide) sẵn sàng cho Khối Đào tạo nghiệm thu (Hoàn thành trước 05/11/2026).

2. Phân hệ BĐS Cho thuê Thương mại - Hệ thống GMS (GMS.NLE - REF-GMS-2026):
- Khảo sát ranh giới & chốt phạm vi: Nghiên cứu phiếu yêu cầu CR NLE, khảo sát thực tế As-Is phân hệ Rent & Rent trên UAT; xây dựng Clarification Checklist và chủ trì Workshop chốt Scope với TGĐ NLE & đại diện NAM, phát hành Gap Matrix (Hoàn thành trước 30/09/2026).
- Hoàn thành Yêu cầu Nghiệp vụ (URD/BRD): Biên soạn và trình ký duyệt URD/BRD CR Leasing bổ sung các luồng cốt lõi (Pipeline Dự án, CRM Phễu Leasing, Công thức thuê % Turnover Rent, Vòng đời Fit-out, Tenant Scoring) & chốt lộ trình Phasing (Hoàn thành trước 12/10/2026).
- Thiết kế Wireframe/Prototype & Ma trận Thẩm quyền: Xây dựng Ma trận Phân quyền & Thẩm quyền (Ma trận AM) chuẩn NVG và Prototype luồng CRM Leasing trình TGĐ NLE & PMO sign-off trực quan (Hoàn thành trước 22/10/2026).
- Hoàn thành Giải pháp Hệ thống (SRS Phase 1): Phân rã bộ Đặc tả chi tiết Use Cases & User Stories cho các phân hệ ưu tiên Phase 1 bàn giao Đội Dev (Hoàn thành trước 05/11/2026)."""

# Try using openpyxl first
openpyxl_success = False
try:
    import openpyxl
    log("openpyxl is available! Using openpyxl to update workbook.")
    
    wb = openpyxl.load_workbook(file_path)
    log(f"Sheet names: {wb.sheetnames}")
    
    # Target sheet: 'KPI-CG PTNV' or first sheet
    ws = wb['KPI-CG PTNV'] if 'KPI-CG PTNV' in wb.sheetnames else wb.active
    log(f"Active sheet: {ws.title}")
    
    # Print old C13 value
    old_c13 = ws['C13'].value
    log(f"Old C13 value: {str(old_c13)[:100]}...")
    
    # Update C13
    ws['C13'].value = content_c13
    
    # Backup original
    import shutil
    if not os.path.exists(backup_path):
        shutil.copyfile(file_path, backup_path)
        log(f"Created backup at {backup_path}")
        
    wb.save(file_path)
    log("Successfully updated C13 using openpyxl!")
    openpyxl_success = True
except Exception as e:
    log(f"openpyxl approach failed or not installed: {e}")

if not openpyxl_success:
    log("Attempting direct ZIP/XML manipulation...")
    try:
        import shutil
        if not os.path.exists(backup_path):
            shutil.copyfile(file_path, backup_path)
            log(f"Created backup at {backup_path}")

        # Extract zip to temp
        temp_dir = r"d:\repo\ba-zone\scratch\xlsx_temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        log("Extracted xlsx contents.")

        # Read sharedStrings.xml
        ss_path = os.path.join(temp_dir, "xl", "sharedStrings.xml")
        sheet_path = os.path.join(temp_dir, "xl", "worksheets", "sheet1.xml")
        
        # Check if sharedStrings exists
        if os.path.exists(ss_path):
            log("sharedStrings.xml found. Modifying shared strings...")
            ET.register_namespace('', "http://schemas.openxmlformats.org/spreadsheetml/2006/main")
            tree = ET.parse(ss_path)
            root = tree.getroot()
            
            # Find the string corresponding to old C13 (starts with 'Phân tích, Xác định')
            updated = False
            for si in root.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                t = si.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                if t is not None and t.text and "Phân tích, Xác định" in t.text:
                    log(f"Found target shared string: {t.text[:60]}...")
                    t.text = content_c13
                    updated = True
                    break
                # Check rich text <r><t>
                r_list = si.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}r')
                if r_list:
                    full_text = "".join([r.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t').text or "" for r in r_list if r.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t') is not None])
                    if "Phân tích, Xác định" in full_text:
                        log(f"Found target rich-text shared string: {full_text[:60]}...")
                        # Remove all <r> and replace with single <t>
                        for r in r_list:
                            si.remove(r)
                        new_t = ET.SubElement(si, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                        new_t.text = content_c13
                        new_t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                        updated = True
                        break

            if updated:
                tree.write(ss_path, encoding='utf-8', xml_declaration=True)
                log("Updated sharedStrings.xml successfully.")
            else:
                log("Could not find matching shared string, inserting new string...")
                si = ET.SubElement(root, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si')
                t = ET.SubElement(si, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
                t.text = content_c13
                t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                new_idx = len(root) - 1
                root.set('count', str(int(root.get('count', '0')) + 1))
                root.set('uniqueCount', str(int(root.get('uniqueCount', '0')) + 1))
                tree.write(ss_path, encoding='utf-8', xml_declaration=True)
                
                # Now update sheet1.xml cell C13 to point to new_idx
                sheet_tree = ET.parse(sheet_path)
                sheet_root = sheet_tree.getroot()
                for c in sheet_root.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                    if c.get('r') == 'C13':
                        c.set('t', 's')
                        v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                        if v is not None:
                            v.text = str(new_idx)
                        else:
                            v = ET.SubElement(c, '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                            v.text = str(new_idx)
                        log(f"Updated sheet1.xml cell C13 to point to shared string index {new_idx}")
                        break
                sheet_tree.write(sheet_path, encoding='utf-8', xml_declaration=True)

        # Repack zip
        output_temp_zip = r"d:\repo\ba-zone\scratch\updated.zip"
        with zipfile.ZipFile(output_temp_zip, 'w', zipfile.ZIP_DEFLATED) as zip_out:
            for root_dir, dirs, files in os.walk(temp_dir):
                for f in files:
                    full_f = os.path.join(root_dir, f)
                    rel_f = os.path.relpath(full_f, temp_dir)
                    zip_out.write(full_f, rel_f)
                    
        shutil.copyfile(output_temp_zip, file_path)
        log("Repacked xlsx and overwritten file successfully!")
        
    except Exception as ex:
        log(f"Direct XML manipulation failed: {ex}")
        import traceback
        traceback.print_exc()

log("Script execution finished.")
