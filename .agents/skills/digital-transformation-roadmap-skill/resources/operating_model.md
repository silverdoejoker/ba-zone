# OPERATING MODEL & TASK-FORCE INTERACTION FRAMEWORK

## 1. MÔ HÌNH VẬN HÀNH IT-AS-A-BUSINESS

Trung tâm Công nghệ (TTCN) được tổ chức theo mô hình đơn vị dịch vụ chuyên nghiệp, phân tách rõ ràng giữa **Quản trị Chiến lược (Front Office)**, **Khối Triển khai Kỹ thuật (Back Office)** và **Dịch vụ Chia sẻ (Shared Services)**:

```mermaid
graph TD
    subgraph FrontOffice["FRONT OFFICE (Giao tiếp & Quản trị Chiến lược)"]
        TMO["Văn phòng Quản lý CĐS (TMO)<br/>- Strategic Governance<br/>- Tech Business Partners<br/>- Innovation & Consultancy"]
        DO["Văn phòng Điều phối Triển khai (DO)<br/>- PMO / Delivery Management<br/>- Change Management & Adoption<br/>- Value Realization"]
    end

    subgraph BackOffice["BACK OFFICE (Khối Triển khai Kỹ thuật)"]
        DataAI["Data, AI & Analytics<br/>- Data Governance & MDM<br/>- Data Platform & Engineering<br/>- AI/ML Ops & Analytics"]
        AppDev["Nền tảng & Phát triển Ứng dụng<br/>- Enterprise Platform & ESB<br/>- Software Engineering (BA/Dev/QC)<br/>- DevOps & SRE"]
        InfraSec["Hạ tầng & Bảo mật<br/>- Cloud/On-Prem System Ops<br/>- Identity & Access (IAM)<br/>- SOC & Threat Intelligence"]
    end

    subgraph CoE_GSS["KHỐI HỖ TRỢ & CHUYÊN MÔN CHUYÊN SÂU"]
        CoE["Centre of Excellence (CoE)<br/>- Solution Architecture Standards<br/>- Training & Capabilities"]
        GSS["Global Shared Services (GSS)<br/>- 24/7 IT Service Desk<br/>- Operations & Maintenance"]
    end

    FrontOffice --> BackOffice
    BackOffice --> CoE_GSS
```

---

## 2. QUY TRÌNH 6 BƯỚC INTERACTION GIỮA BUSINESS VÀ TTCN

Nhu cầu chuyển đổi số từ các Ban/Phòng/TCT nghiệp vụ được tiếp nhận và xử lý qua **6 Task-Forces chuyên trách** (Finance/Investment, Procurement, Operations/GMS, HR/RPC, Sales/Marketing, Security/Digital Library):

```mermaid
sequenceDiagram
    autonumber
    actor Business as Ban/Phòng Hệ thống (BU / TCT)
    participant TMO as TMO / Kế hoạch CĐS
    actor BOD as Ban Chỉ Đạo CĐS
    participant TaskForce as Task-Force Chuyên trách (PMO + BA + Dev + QC)
    participant Ops as Đội ngũ Triển khai & Vận hành

    Business->>TMO: 1. Nộp Yêu cầu Chuyển đổi số / Hệ thống phần mềm
    TMO->>Business: 2. Phân tích 2 chiều: Làm rõ Yêu cầu, SOP & Flow toàn trình
    TMO->>BOD: 3. Trình Đề xuất Danh mục Hệ thống Số hóa / CĐS
    BOD-->>TMO: 4. Phê duyệt Danh mục & Ngân sách thực thi
    TMO->>TaskForce: 5. Giao việc cho Task-Force tương ứng (Task-Force 1 -> 6)
    TaskForce->>Ops: 6. Xây dựng, QC, Chuyển giao Đào tạo & Đưa vào Vận hành
```

---

## 3. CƠ CHẾ NGÂN SÁCH VÀ THỎA THUẬN DỊCH VỤ (SLA & CHARGEBACK)

1. **Tổng Ngân sách CNTT**: Xây dựng dựa trên Kế hoạch Ngân sách Hàng năm (AOP) / Kế hoạch Dài hạn (LTP) ở mức Consolidation Tập đoàn.
2. **Chi phí Triển khai Dự án mới**: Tính theo dự toán ngân sách thực tế + Thỏa thuận SLA phê duyệt theo từng yêu cầu.
3. **Chi phí Vận hành Hàng ngày (BAU)**: Chargeback cho các TCT/BU theo thỏa thuận mức dịch vụ (SLA) dựa trên tỷ lệ % phân bổ hoặc Chi phí Thực tế + Mark-up chuẩn.
