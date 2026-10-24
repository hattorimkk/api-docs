# 05. Giới Hạn Tần Suất (Rate Limit) & Bảng Tra Cứu Mã Lỗi

Tài liệu này tổng hợp các quy định về giới hạn tần suất gọi API (Rate Limit), chiến lược xử lý khi bị nghẽn và bảng mã lỗi chuẩn từ Shopee Open Platform.

---

## 1. Quy Định Giới Hạn Tần Suất Gọi API (Rate Limits)

Shopee áp dụng cơ chế giới hạn tần suất theo số lượt gọi trên giây (Queries Per Second - QPS):

| Mức Giới Hạn | Giá Trị Mặc Định | Đối Tượng Áp Dụng |
| :--- | :--- | :--- |
| **Shop-level Limit** | **50 QPS** | Giới hạn số lượt gọi API trên cùng một gian hàng (`shop_id`). |
| **Partner-level Limit** | Phụ thuộc cấp bậc Partner (thường từ 100 - 500 QPS) | Giới hạn tổng số lượt gọi của toàn bộ ứng dụng (`partner_id`) trên toàn sàn. |
| **Endpoint-level Limit** | Giới hạn riêng cho một số API nặng | Các API như `get_order_detail`, tải phiếu giao hàng AWB có thể bị giới hạn tần suất thấp hơn. |

### Dấu hiệu khi vượt ngưỡng Rate Limit:
- Mã trạng thái HTTP: `429 Too Many Requests`.
- Hoặc HTTP `200` với body JSON:
  ```json
  {
    "error": "error_limit",
    "message": "Too many requests, please try again later.",
    "request_id": "90a9821f009b4..."
  }
  ```

---

## 2. Chiến Lược Xử Lý Giảm Tải (Rate Limit Mitigation)

Khi xây dựng các script quét dữ liệu lớn (Batch ETL/Sync):

1. **Thêm độ trễ chủ động (Sleep Interval)**:
   - Thêm khoảng nghỉ ngắn (ví dụ `time.sleep(0.1)` đến `0.2` giây) giữa các lần gọi phân trang lặp lại.
2. **Thuật toán Exponential Backoff (Độ trễ số mũ)**:
   - Khi nhận mã lỗi `error_limit`, không gửi lại ngay lập tức mà đợi $2^n$ giây (ví dụ: 1s, 2s, 4s, 8s) rồi mới gửi lại:
   ```python
   import time

   def call_with_retry(client, func, *args, max_retries=5, **kwargs):
       for attempt in range(max_retries):
           res = func(*args, **kwargs)
           if res.get("error") == "error_limit":
               wait_time = (2 ** attempt) * 0.5
               print(f"Bị chạm Rate limit, đợi {wait_time}s trước khi thử lại...")
               time.sleep(wait_time)
               continue
           return res
       return res
   ```
3. **Ưu tiên sử dụng Webhook (Shopee Push)**:
   - Thay vì chạy vòng lặp liên tục quét `get_order_list` mỗi 30 giây để tìm đơn mới (rất dễ bị khóa QPS), hãy cấu hình Webhook để Shopee tự động bắn sự kiện `order_status_push` sang server của bạn.

---

## 3. Bảng Tra Cứu Các Mã Lỗi Thường Gặp (Error Code Dictionary)

| Mã Lỗi (`error`) | Thông Điệp Tiêu Biểu (`message`) | Nguyên Nhân Cốt Lõi | Cách Khắc Phục |
| :--- | :--- | :--- | :--- |
| **`error_auth`** | `Wrong sign` | Chữ ký số `sign` không khớp với thuật toán mã hóa HMAC-SHA256. | - Kiểm tra lại thứ tự ghép chuỗi `base_string`.<br>- Đảm bảo không có dấu cách thừa.<br>- Kiểm tra xem đồng hồ server có bị lệch quá 5 phút so với giờ chuẩn NTP không. |
| **`error_auth`** | `Invalid access_token` hoặc `Access token has expired` | Access token bị sai hoặc đã vượt quá thời hạn 4 giờ. | Dùng `refresh_token` gọi API `/api/v2/auth/access_token/get` để lấy token mới. |
| **`error_auth`** | `The partner is not authorized to operate the shop` | Shop này chưa từng cấp quyền hoặc đã hủy cấp quyền cho ứng dụng. | Gửi lại link ủy quyền `/api/v2/shop/auth_partner` cho chủ shop bấm xác nhận lại. |
| **`error_param`** | `time_to - time_from should be <= 15 days` | Khoảng thời gian tìm kiếm vượt quá 15 ngày. | Chia nhỏ khoảng thời gian truy vấn thành các block tối đa 14 ngày. |
| **`error_param`** | `Missing required parameter` | Thiếu tham số bắt buộc trong URL hoặc Body JSON. | Kiểm tra lại tài liệu chi tiết của endpoint để bổ sung đủ tham số. |
| **`error_not_found`**| `Order does not exist` | Mã đơn hàng `order_sn` không tồn tại hoặc không thuộc quyền sở hữu của `shop_id` này. | Kiểm tra xem đơn hàng có thuộc đúng shop đang gọi API hay không. |
| **`error_limit`** | `Too many requests` | Vượt quá số lượt gọi cho phép trong 1 giây (QPS). | Giảm tốc độ gọi request, áp dụng Exponential Backoff. |
| **`error_server`** | `Internal server error` | Lỗi tạm thời phát sinh từ máy chủ nội bộ Shopee. | Thử lại sau 1 đến 5 giây. Nếu kéo dài, gửi ticket báo lỗi kèm mã `request_id` cho Shopee Open Platform Team. |

