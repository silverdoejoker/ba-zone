# ONE NOVA PLATFORM & EMPLOYEE JOURNEY SPECIFICATION

## 1. NỀN TẢNG THỰC THI NGHIỆP VỤ TẬP TRUNG ONE NOVA

One Nova là Cổng Quản trị & Vận hành Tập trung (Enterprise Operating System) duy nhất cho toàn thể cán bộ nhân viên Tập đoàn, tích hợp **SSO (Single Sign-On)**, **Org Chart**, **Personal Dashboard**, **AI Copilot**, và **Task-to-Performance Engine**.

```mermaid
flowchart TD
    subgraph UserExperience["TẦNG TRẢI NGHIỆM NGUỜI DÙNG (One Nova Portal)"]
        SSO["Đăng nhập 1 cổng duy nhất (SSO / MFA)"]
        OrgChart["Sơ đồ Tổ chức Dynamic Org Chart"]
        Dashboard["My Dashboard (Tasks, OKRs, SLA, Attendance)"]
        AICopilot["Nova AI Assistant (Chatbot & Task Automation)"]
    end

    subgraph CoreFlow["TẦNG VẬN HÀNH CÔNG VIỆC (Task-to-Performance Flow)"]
        Step1["1. Nhận việc (Task Assigned)"] --> Step2["2. Thực hiện & Evidence Check"]
        Step2 --> Step3["3. Trình Phê duyệt (Approval Flow)"]
        Step3 --> Step4["4. Hoàn thành (Done)"]
        Step4 --> Step5["5. Tính KPI & Hiển thị Performance"]
    end

    subgraph IntegrationLayer["TẦNG TÍCH HỢP HỆ THỐNG LÕI (Integration & Data)"]
        API["API Gateway / Enterprise Service Bus (ESB)"]
        EDP["Enterprise Data Platform (EDP Lakehouse)"]
        Systems["ERP (SAP) | SuccessFactors | CRM | DMS | Property Systems"]
    end

    UserExperience --> CoreFlow
    CoreFlow --> IntegrationLayer
```

---

## 2. CHUẨN HOÁ EMPLOYEE JOURNEY 12 BƯỚC

Mọi hệ thống Quản trị Nhân sự & Vận hành Công việc phải kết nối nhất quán theo hành trình 12 bước của Nhân viên:

```mermaid
timeline
    title Hành trình Nhân viên 12 Bước (Employee Journey)
    section Thu hút & Bắt đầu
        1. Thu hút & Tuyển dụng : ATS / AI Sourcing / Talent Pool
        2. Offer & Nhận việc : E-Offer / E-Signature / Background Check
        3. Onboarding : Welcome Kit / Buddy Program / Task 30-60-90
    section Phát triển & Vận hành
        4. Đào tạo & Phát triển : LMS / Learning Path / Certification
        5. Làm việc hàng ngày : Task Management / Knowledge Base / Collaboration
        6. Đánh giá Hiệu suất : KPI/OKR / 360 Feedback / Calibration
    section Ghi nhận & Thăng tiến
        7. Ghi nhận & Khen thưởng : NovaPoint Reward / Leader Board
        8. Phát triển & Luân chuyển : Career Path / Succession Plan / Talent Review
        9. Chăm sóc & Phúc lợi : Benefit Portal / Health Survey / Well-being
    section Thay đổi & Alumni
        10. Thay đổi Vai trò : Role Change / Re-onboarding / Goal Update
        11. Chia tay (Offboarding) : Exit Survey / Asset Return / Handover
        12. Alumni & Đại sứ : Rehire Network / Referral Program / Community
```

---

## 3. CƠ CHẾ PHÂN RÃ KPI CASCADE & MA TRẬN PHÂN QUYỀN / THẨM QUYỀN (AM)

### 3.1 Quy tắc Cascade KPI
- Target chỉ số AOP (Annual Operating Plan) từ Tập đoàn được phân rã tuần tự xuống các cấp:  
  `Cấp Tập đoàn` $\rightarrow$ `Cấp TCT/BU` $\rightarrow$ `Cấp Khối/Ban` $\rightarrow$ `Cấp Phòng/Trung tâm` $\rightarrow$ `Cấp Nhóm/Team` $\rightarrow$ `Cấp Cá nhân`.
- **Nguyên tắc Ràng buộc Trọng số**: Tổng trọng số KPI của các mục tiêu tại bất kỳ cấp nào **phải tròn 100%**.

### 3.2 Quy chuẩn Ma trận Phân quyền & Thẩm quyền (Authority Matrix - AM)
Mọi tài liệu thiết kế hệ thống, SRS và Use Case trên One Nova bắt buộc phải định nghĩa **Bảng AM (Authority Matrix)** thay thế cho khái niệm phân quyền thông thường:

| Vai trò / Chức danh | Hạn mức Thẩm quyền Phê duyệt | Quyền Thao tác trên System | Luồng Ủy quyền / Thay thế |
|---|---|---|---|
| **Trưởng Ban / GĐ Khối** | Phê duyệt ngân sách/hợp đồng > 1 tỷ VNĐ | Create, Approve, Reject, Delegate | Ủy quyền cho Phó Ban khi Vắng mặt |
| **Trưởng Phòng / Team Lead** | Phê duyệt task/ngân sách < 1 tỷ VNĐ | Create, Review, Approve Task | Ủy quyền Senior BA / Senior Dev |
| **Chuyên viên / BA / Dev** | Thực thi tác nghiệp chuyên môn | Create Task, Submit Evidence, Update Status | N/A |
