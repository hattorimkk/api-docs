# 03. Môi Trường Thử Nghiệm (Sandbox) & Môi Trường Sản Xuất (Live)

Tài liệu này hướng dẫn cách cấu hình và chuyển đổi giữa hai môi trường: **Test-Stable (Sandbox)** phục vụ việc phát triển, kiểm thử và **Live (Production)** khi triển khai thực tế.

---

## 1. So Sánh Hai Môi Trường

| Tiêu Chí | Môi Trường Sandbox (Test-Stable) | Môi Trường Sản Xuất (Live) |
| :--- | :--- | :--- |
| **Mục đích** | Phát triển tính năng, kiểm thử luồng gọi API, chạy thử nghiệm mà không tốn chi phí thực tế. | Chạy ứng dụng thực tế với đơn hàng, sản phẩm, tiền tệ và khách hàng thật. |
| **Base URL** | `https://partner.test-stable.shopeemobile.com` | `https://partner.shopeemobile.com` |
| **Thông tin xác thực** | `partner_id` và `partner_key` của ứng dụng Test | `partner_id` và `partner_key` của ứng dụng Live chính thức |
| **Tài khoản Shop** | Tài khoản Shop ảo (Test Shop) do hệ thống cấp trong Console | Gian hàng thật của người bán trên sàn Shopee |
| **Đơn hàng & Tiền** | Dữ liệu giả lập, thanh toán ảo không phát sinh chi phí | Đơn hàng phát sinh giao dịch tiền tệ và vận chuyển thực tế |

---

## 2. Quản Lý Tài Khoản Kiểm Thử (Test Accounts)

Trong Shopee Open Platform Console, bạn vào mục **Test Account**:
1. **Tạo Test Shop**:
   - Chọn khu vực/quốc gia muốn thử nghiệm (ví dụ: `VN - Vietnam`).
   - Nhấn **Create Test Shop** để tạo gian hàng ảo. Hệ thống sẽ cung cấp cho bạn tên đăng nhập và mật khẩu của Shop thử nghiệm.
2. **Tạo Test Buyer**:
   - Tạo tài khoản người mua ảo để đặt hàng trên Test Shop.
   - Số dư ví ảo được nạp sẵn để thực hiện test luồng thanh toán đơn hàng.
3. **Mô phỏng chu trình đơn hàng hoàn chỉnh**:
   - Dùng tài khoản Test Buyer đặt mua sản phẩm từ Test Shop.
   - Ứng dụng của bạn gọi API lấy danh sách đơn `READY_TO_SHIP`.
   - Gọi API tạo vận đơn và giao hàng `v2.logistics.ship_order`.
   - Vào công cụ mô phỏng trạng thái hậu cần (Logistics Mock Tool) trong Console để chuyển trạng thái đơn hàng sang `DELIVERED` và `COMPLETED`.
   - Kiểm tra tiền quyết toán chảy vào API `v2.payment.get_escrow_detail`.

---

## 3. Cấu Hình Danh Sách Trắng Địa Chỉ IP (IP Whitelist)

Để bảo vệ an toàn cho hệ thống và tuân thủ các quy tắc bảo mật của Shopee:
- Trong phần cài đặt Ứng dụng (**App Detail > IP Whitelist**), bạn cần khai báo các địa chỉ IP tĩnh (Static Public IPv4) của các máy chủ backend sẽ thực hiện gửi request đến Shopee API.
- Shopee sẽ từ chối các request bắt nguồn từ IP không nằm trong danh sách trắng nếu chế độ IP Whitelist được kích hoạt.

> [!TIP]
> Trong quá trình code trên máy tính cá nhân ở môi trường Local/Development, nếu IP mạng nhà bạn là IP động (Dynamic IP), bạn có thể tạm thời bổ sung IP hiện tại của mạng vào danh sách hoặc sử dụng VPN máy chủ cố định.

---

## 4. Danh Sách Kiểm Tra Trước Khi Lên Production (Go-Live Checklist)

Trước khi chuyển đổi biến môi trường từ Sandbox sang Live, hãy rà soát kỹ các mục sau:

- [ ] Đã chuyển đổi `base_url` từ `partner.test-stable.shopeemobile.com` sang `partner.shopeemobile.com`.
- [ ] Đã thay thế `partner_id` và `partner_key` bằng bộ khóa chính thức của ứng dụng Live.
- [ ] Đã đăng ký đường dẫn `redirect_url` có chứng chỉ bảo mật HTTPS hợp lệ.
- [ ] Máy chủ chạy tác vụ định kỳ tự động đồng bộ giờ qua NTP để tránh lệch quá 5 phút so với đồng hồ chuẩn Shopee.
- [ ] Hệ thống lưu trữ `access_token` và `refresh_token` đã sẵn sàng với cơ chế tự động xoay vòng và làm mới trước 5 phút khi hết hạn.
- [ ] Máy chủ tiếp nhận Webhook (Push Mechanism) đã cài đặt thuật toán kiểm tra chữ ký xác thực `Authorization` header.

