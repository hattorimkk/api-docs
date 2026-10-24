# 01. Giới Thiệu & Kiến Trúc Nền Tảng Shopee Open Platform v2

Tài liệu này cung cấp cái nhìn tổng quan về hệ thống **Shopee Open Platform (phiên bản Open API v2.0)**, mô hình kiến trúc kết nối giữa Đối tác (Partner/Developer), Người bán (Seller/Shop) và Hệ thống Máy chủ Shopee.

---

## 1. Shopee Open Platform Là Gì?

**Shopee Open Platform (`open.shopee.com`)** là cổng giao tiếp lập trình ứng dụng (API Gateway) chính thức của Shopee, cho phép các nhà phát triển phần mềm, đối tác kỹ thuật (ISV), doanh nghiệp thương mại điện tử và nhà bán hàng tự động hóa mọi hoạt động kinh doanh trên Shopee:
- **Trích xuất dữ liệu vận hành**: Đơn hàng, sản phẩm, tồn kho, doanh thu, phí sàn, vận chuyển, đánh giá, chat.
- **Tự động hóa xử lý**: Chuẩn bị hàng, in phiếu vận đơn (AWB), cập nhật số lượng tồn kho theo thời gian thực, đồng bộ giá đa sàn.
- **Nhận thông báo tức thì (Realtime Webhook)**: Nhận tin báo khi khách đặt hàng mới, hủy đơn, hoàn tất giao hàng qua cơ chế Push Mechanism.

---

## 2. Kiến Trúc Kết Nối Ba Bên (Three-Party Architecture)

Mô hình hoạt động của Shopee Open API v2 hoạt động dựa trên mối quan hệ giữa 3 thực thể:

```
+-----------------------------------------------------------------------------------+
|                                                                                   |
|    +-------------------------+             1. Ủy quyền (OAuth)                    |
|    |                         |  ======================================>           |
|    |   Nhà Bán Hàng Shopee   |                                                    |
|    |      (Seller / Shop)    |  <======================================           |
|    |                         |             2. Trả Authorization Code              |
|    +-------------------------+                                                    |
|                 ^                                        |                        |
|                 |                                        |                        |
|                 | Quản lý gian hàng                      |                        |
|                 v                                        v                        |
|    +-------------------------+             3. Gọi API kèm HMAC Sign & Token       |
|    |  Ứng Dụng Của Bạn       |  ======================================>  +------+ |
|    |  (Partner / Developer)  |                                           |Shopee| |
|    |                         |  <======================================  |Server| |
|    |  - Quản lý Partner ID   |             4. Trả dữ liệu JSON           +------+ |
|    |  - Quản lý Token        |                                                    |
|    +-------------------------+                                                    |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### Các Khái Niệm Cốt Lõi:
1. **Partner (Nhà phát triển / Ứng dụng)**:
   - Được định danh bởi **`partner_id`** (dạng số nguyên, ví dụ: `1002345`).
   - Sở hữu một khóa bí mật duy nhất là **`partner_key`** (Secret string). Khóa này dùng để ký chữ ký số `sign` cho mọi request nhằm đảm bảo tính toàn vẹn dữ liệu.
2. **Shop (Gian hàng địa phương)**:
   - Mỗi gian hàng Shopee ở từng quốc gia (Việt Nam, Thái Lan, Singapore, Malaysia, Philippines, Đài Loan, Brazil...) được định danh bởi một **`shop_id`**.
   - Ứng dụng chỉ có thể đọc hoặc ghi dữ liệu của Shop khi chủ Shop đã thực hiện thao tác **Ủy quyền (Shop Authorization)**.
3. **Merchant (Tài khoản Người bán Toàn cầu / CNSC)**:
   - Dành cho các nhà bán hàng xuyên biên giới (Cross-border / China Seller Centre) quản lý nhiều shop ở nhiều quốc gia dưới một tài khoản mẹ định danh bằng **`merchant_id`**.
4. **Access Token & Refresh Token**:
   - `access_token`: Khóa phiên dùng để truy cập API của từng Shop, có thời hạn **4 giờ** (14.400 giây).
   - `refresh_token`: Khóa làm mới phiên, có thời hạn **30 ngày**. Được dùng để cấp phát một cặp `access_token` mới và `refresh_token` mới trước khi hết hạn (cơ chế Token Rotation).

---

## 3. Các Phân Nhóm API trong Shopee Open Platform

Shopee chia toàn bộ hệ thống API thành 3 phân nhóm phân quyền rõ rệt:

| Phân Nhóm API | Yêu Cầu Tham Số | Mục Đích Sử Dụng | Ví Dụ Endpoints |
| :--- | :--- | :--- | :--- |
| **Public API** | `partner_id`, `timestamp`, `sign` | Dùng cho các thao tác xác thực ban đầu, đổi token, kiểm tra cấu hình chung. | `/api/v2/auth/token/get`<br>`/api/v2/auth/access_token/get` |
| **Shop API** | `partner_id`, `timestamp`, `sign`, `access_token`, `shop_id` | Thao tác với dữ liệu của 1 gian hàng cụ thể (Đơn hàng, sản phẩm, kho bãi, doanh thu). | `/api/v2/order/get_order_list`<br>`/api/v2/product/get_item_base_info`<br>`/api/v2/payment/get_escrow_detail` |
| **Merchant API** | `partner_id`, `timestamp`, `sign`, `access_token`, `merchant_id` | Thao tác ở cấp độ tài khoản tổng Merchant (Sản phẩm toàn cầu CNSC). | `/api/v2/global_product/get_global_item_list` |

---

## 4. Chuẩn Giao Thức & Định Dạng Dữ Liệu

- **Giao thức truyền tải**: HTTPS bắt buộc (TLS 1.2+).
- **Phương thức HTTP**: Hỗ trợ `GET` (đọc dữ liệu) và `POST` (thay đổi dữ liệu hoặc truyền tham số phức tạp).
- **Định dạng dữ liệu**: Toàn bộ dữ liệu gửi và nhận đều ở định dạng **JSON** (`Content-Type: application/json; charset=utf-8`).
- **Quy tắc Query Parameters**:
  > [!IMPORTANT]
  > Khác với nhiều nền tảng REST khác, đối với Shopee Open API v2, **ngay cả khi gọi phương thức POST**, các tham số bảo mật bắt buộc (`partner_id`, `timestamp`, `sign`, `access_token`, `shop_id`) **vẫn phải được truyền dưới dạng URL Query Parameters** (trên thanh địa chỉ). Phần Payload thân request (Request Body) chỉ chứa các trường tham số nghiệp vụ.

---

## 5. Cấu Trúc Phản Hồi Chuẩn (Standard Response Format)

Mọi phản hồi từ Shopee Open API luôn trả về một đối tượng JSON có cấu trúc thống nhất:

### Trường hợp thành công:
```json
{
  "error": "",
  "message": "",
  "request_id": "76ba370b77c3858739191d9e798e4d1a",
  "response": {
    "order_list": [
      {
        "order_sn": "261023ABCD1234",
        "order_status": "READY_TO_SHIP"
      }
    ],
    "more": false,
    "next_cursor": ""
  }
}
```

### Trường hợp xảy ra lỗi:
```json
{
  "error": "error_auth",
  "message": "Wrong sign",
  "request_id": "8488e02511470ad46b3e8c95029e24b7"
}
```

- **`error`**: Chuỗi rỗng `""` nếu thành công; chuỗi mã lỗi (ví dụ: `error_auth`, `error_param`, `error_not_found`) nếu thất bại.
- **`message`**: Thông điệp mô tả chi tiết lỗi bằng tiếng Anh.
- **`request_id`**: Mã định danh duy nhất của từng lượt gọi API. Rất quan trọng khi cần gửi ticket hỗ trợ kỹ thuật cho đội ngũ Shopee Open Platform.
- **`response`**: Đối tượng chứa toàn bộ dữ liệu trả về theo nghiệp vụ của API đó.

