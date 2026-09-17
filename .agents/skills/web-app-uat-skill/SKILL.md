---
name: web-app-uat
description: |
  Hướng dẫn chuyên sâu và quy trình tự động/bán tự động kiểm thử, nghiệm thu (UAT) và trải nghiệm sản phẩm (Exploratory / Dogfooding QA) cho ứng dụng Web / Mobile Web khi có sẵn URL & Credentials (dựa trên thực tiễn chuẩn hóa tại TrọBill).
  Hỗ trợ xác thực kết nối, luồng đăng nhập đa vai trò (RBAC), kiểm tra DOM/Modal binding, Happy Path, Edge Cases, Negative Scenarios, Cross-device viewports, Console/Network error sniffing, phân lập ranh giới phần cứng (Camera OCR/IAP/Biometrics) và lập biên bản nghiệm thu UAT chuẩn mực.
author: Phúc NT @ BA Zone & Kiro Engineering
source: https://github.com/ba-zone
---

# Web Application UAT & Exploratory Testing Skill (TrọBill Methodology)
> by **Phúc NT** · BA Zone · Digital School · Kiro Engineering

Kỹ năng này cung cấp quy trình toàn diện, các nguyên tắc thực chiến và bộ công cụ tự động hóa để **kiểm thử chấp nhận người dùng (User Acceptance Testing - UAT)**, **trải nghiệm thực tế (Dogfooding / Exploratory Testing)** và **nghiệm thu chức năng** cho bất kỳ ứng dụng Web / Mobile Web nào khi đã được cung cấp **URL** và **Credentials** (tài khoản đăng nhập / vai trò).

---

## 🎯 Giá Trị Cốt Lõi & Triết Lý Thực Chiến (TrọBill Principles)

1. **Token-Preserving & Zero Retry Loops (Bảo toàn token AI)**: Fail-fast khi gặp lỗi.
2. **3-Second Fail-Fast Guard for Headless Browser**: Không để loader treo tiến trình.
3. **Hardware / Non-Automatable Boundary Isolation**: Cô lập Camera OCR/IAP/Biometrics vào Manual Registry.
4. **Bi-Directional Traceability**: Traceability rõ ràng giữa Test Cases và User Stories/Use Cases.
