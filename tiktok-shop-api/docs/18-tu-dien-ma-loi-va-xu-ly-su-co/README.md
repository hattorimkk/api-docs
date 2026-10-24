# 18. Từ Điển Mã Lỗi & Xử Lý Sự Cố Hệ Thống (Error Codes & Troubleshooting)

Khi gọi API TikTok Shop, nếu kết quả trả về trường `code != 0`, yêu cầu của bạn đã gặp sự cố. Tài liệu này cung cấp bảng tra cứu toàn diện các mã lỗi hệ thống, mã lỗi nghiệp vụ và phương pháp xử lý giới hạn tần suất gọi (Rate Limit).

---

## 1. Bảng Tra Cứu Các Mã Lỗi Hệ Thống Phổ Biến (Gateway Error Codes)

| Mã lỗi (`code`) | Thông báo lỗi tiếng Anh | Ý nghĩa chi tiết | Giải pháp khắc phục triệt để |
| :--- | :--- | :--- | :--- |
| `0` | `success` | Thành công | Không có lỗi. |
| `36000001` | `Signature is invalid` | Chữ ký số `sign` không chính xác | 1. Kiểm tra `app_secret` có chính xác không.<br/>2. Đảm bảo đã bỏ `sign` và `access_token` ra khỏi chuỗi ký.<br/>3. Nếu có Body JSON, đảm bảo nối đúng chuỗi thô không chứa khoảng trắng thừa.<br/>4. Kiểm tra `timestamp` 10 số. |
| `36000002` | `Access token is invalid or expired` | Token không hợp lệ hoặc đã hết hạn | 1. `access_token` có hạn 7 ngày, gọi ngay API Refresh Token để cấp mới.<br/>2. Kiểm tra Header `x-tts-access-token` có bị thiếu hoặc sai chính tả không. |
| `36000003` | `App key does not exist` | App Key không tồn tại trên hệ thống | Kiểm tra lại giá trị `app_key` sao chép từ Partner Center. |
| `36000004` | `Request timestamp is invalid` | Dấu thời gian không hợp lệ | `timestamp` phải là Unix Epoch (10 chữ số) và không được lệch quá ±5 phút so với đồng hồ quốc tế UTC. |
| `36000005` | `Scope unauthorized` | Ứng dụng chưa được cấp quyền gọi API này | 1. Vào Partner Center thêm Scope tương ứng.<br/>2. Người dùng phải ủy quyền lại (Reauthorize) để cập nhật quyền mới. |
| `36000006` | `Shop cipher is invalid` | Mã định danh cửa hàng không hợp lệ | Gọi lại API `/authorization/202309/shops` để lấy đúng chuỗi `cipher` mới nhất của shop. |
| `98001004` | `Invalid parameters` | Tham số gửi lên không đúng định dạng | Kiểm tra tài liệu chi tiết của endpoint, đối chiếu các trường bắt buộc và kiểu dữ liệu (int/string). |
| `105001` | `Internal system error` | Lỗi nội bộ hệ thống TikTok | Lỗi phía máy chủ sàn. Áp dụng cơ chế thử lại tự động (Exponential Retry) sau 1 đến 3 giây. |
| `105002` | `Traffic limit exceeded` | Vượt quá giới hạn tần suất gọi (Rate Limit) | Giảm tần suất gọi, áp dụng thuật toán Rate Limiter và hàng đợi. |

---

## 2. Cơ Chế Kiểm Soát Tần Suất Gọi (API Rate Limits & HTTP 429)

TikTok Shop áp dụng cơ chế giới hạn tần suất theo mô hình Token Bucket:
- **Tần suất thông thường**: Từ **10 QPS đến 50 QPS** (Queries Per Second) tùy theo phân hệ và cấp độ ứng dụng (App Tier).
- **Các Header phản hồi kiểm tra tần suất**:
  - `x-tts-rate-limit-limit`: Số lượng request tối đa được phép trong 1 giây.
  - `x-tts-rate-limit-remaining`: Số lượt gọi còn lại trong cửa sổ hiện tại.
  - `x-tts-rate-limit-reset`: Thời gian còn lại (tính bằng mili-giây) trước khi hạn mức được hồi đầy.

### Code Mẫu Thử Lại Lũy Thừa (Exponential Backoff with Jitter)

```python
import time
import random
import requests

def call_tiktok_api_with_retry(url, headers, max_retries=4):
    for attempt in range(max_retries):
        resp = requests.get(url, headers=headers)
        data = resp.json()
        
        # Nếu thành công
        if data.get("code") == 0:
            return data
            
        # Nếu bị nghẽn tần suất (Rate limit) hoặc lỗi máy chủ tạm thời
        if data.get("code") in (105001, 105002) or resp.status_code == 429:
            # Chờ đợi tăng dần có ngẫu nhiên (Jitter) để tránh bão request
            wait_time = (2 ** attempt) + random.uniform(0.1, 1.0)
            time.sleep(wait_time)
            continue
            
        # Lỗi nghiệp vụ logic (không thể thử lại)
        raise Exception(f"Lỗi API: {data.get('code')} - {data.get('message')}")
        
    raise Exception("Vượt quá số lần thử lại tối đa!")
```

---

## 3. Kênh Hỗ Trợ Kỹ Thuật (Partner Assistant Ticket)

Khi gặp lỗi lạ hoặc vấn đề dữ liệu không khớp, nhà phát triển có thể gửi Ticket trực tiếp cho đội ngũ kỹ sư TikTok Shop:
- Truy cập Partner Center > Chọn mục **Partner Assistant** (ở góc dưới cùng bên phải màn hình).
- Chọn danh mục sự cố: **API & Integration Issues**.
- Cung cấp đủ 3 thông tin để kỹ sư xử lý trong 24h:
  1. `request_id` (Nằm trong JSON phản hồi lỗi).
  2. Thời điểm xảy ra lỗi (Timestamp UTC).
  3. URL Endpoint và cURL request đầy đủ (đã ẩn `app_secret`).

