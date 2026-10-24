# 15. Từ Điển Mã Lỗi, Giới Hạn Tần Suất (Rate Limits) & Chiến Lược Phục Hồi

Khi vận hành hệ thống kết nối với Meta Marketing API ở quy mô lớn, việc gặp phải giới hạn tần suất (Rate Limit) hoặc các mã lỗi hệ thống là điều không thể tránh khỏi. Tài liệu này cung cấp bảng tra cứu toàn diện và thuật toán xử lý lỗi tự động (Resilience Engineering).

---

## 1. Cơ Chế Kiểm Soát Tần Suất Gọi API (Rate Limiting)

Meta kiểm soát giới hạn gọi API thông qua các Header trả về trong phản hồi HTTP:

### 1.1. Header `X-Business-Use-Case-Usage` (Dành cho Marketing API)
Đây là header quan trọng nhất, thể hiện mức độ tiêu thụ tài nguyên của từng loại tác vụ:

```http
X-Business-Use-Case-Usage: {
  "102030405060708": [
    {
      "type": "ads_management",
      "call_count": 65,
      "total_cputime": 45,
      "total_time": 50,
      "estimated_time_to_regain_access": 0
    }
  ]
}
```

> **Nguyên tắc hành động theo % chỉ số:**
> - `< 80%`: Hệ thống an toàn, tiếp tục gửi request bình thường.
> - `80% - 95%`: Cảnh báo nguy hiểm. Phải chủ động giảm tốc độ gửi request, tăng thời gian trễ giữa các lần gọi (Delay).
> - `> 95%`: Nguy cơ bị khóa tạm thời. Dừng ngay lập tức các cron job không quan trọng và chờ `estimated_time_to_regain_access` (tính bằng phút) giảm về 0.

### 1.2. Header `X-App-Usage` (Dành cho cấp ứng dụng)
```http
X-App-Usage: {"call_count": 28, "total_cputime": 15, "total_time": 20}
```

---

## 2. Từ Điển Mã Lỗi Thường Gặp (Error Dictionary)

| Mã lỗi (`code`) | Mã phụ (`subcode`) | Tên lỗi & Ý nghĩa | Nguyên nhân thực tế | Giải pháp khắc phục triệt để |
| :--- | :--- | :--- | :--- | :--- |
| **`100`** | - | `Invalid Parameter` | Thiếu trường bắt buộc, sai định dạng enum hoặc sai cấu trúc JSON | Kiểm tra kỹ payload với schema chuẩn. Đọc chi tiết `error.error_user_msg`. |
| **`190`** | `463` | `Session Expired` | Token 60 ngày đã hết hạn | Yêu cầu người dùng đăng nhập lại hoặc chuyển sang dùng **System User Token vĩnh viễn**. |
| **`190`** | `467` | `Invalid Access Token` | Token bị thu hồi do người dùng đổi mật khẩu hoặc xóa ứng dụng | Xóa token trong DB và gửi thông báo yêu cầu ủy quyền lại. |
| **`190`** | `458` | `App Not Installed` | Người dùng đã hủy liên kết ứng dụng trên trang cá nhân | Chuyển trạng thái kết nối tài khoản sang `DISCONNECTED`. |
| **`17`** / **`613`** | - | `Rate Limit Reached` | Gọi quá số lượt cho phép trong 1 giờ | Áp dụng thuật toán **Exponential Backoff** và tạm dừng trong số phút quy định. |
| **`200`** | - | `Permission Denied` | Token thiếu scope hoặc tài khoản không có quyền trên Ad Account/Page | Vào Business Manager gán quyền Quản trị viên (Admin) cho System User trên Ad Account. |
| **`80004`** | - | `There are too many calls` | Quá nhiều tác vụ Async Insights chạy đồng thời trên một Ad Account | Giới hạn tối đa 3-5 tiến trình Async Insights đồng thời cho mỗi Ad Account. |
| **`1487390`** | - | `SAC Terms Not Certified` | Tạo Ad Set có danh sách khách hàng (CLCA) nhưng chưa xác nhận điều khoản v22.0 | Truyền thêm trường `is_sac_cfca_terms_certified: true` vào request tạo Ad Set. |
| **`1487000+`** | - | `Ad Policy Disapproved` | Bài quảng cáo vi phạm chính sách của Meta (từ ngữ cấm, hình ảnh nhạy cảm) | Kiểm tra trường `ad_review_feedback` để biết lý do cụ thể và thay đổi nội dung Creative. |

---

## 3. Thuật Toán Thử Lại Thông Minh (Exponential Backoff With Jitter)

Khi nhận được lỗi Rate Limit (`17`, `613`, `80004`) hoặc lỗi mạng `5xx`, máy chủ **tuyệt đối không được gửi lại request ngay lập tức** vì sẽ làm lỗi nặng hơn. Hãy triển khai thuật toán Exponential Backoff kèm độ trễ ngẫu nhiên (Jitter):

$$\text{Delay} = 2^{\text{attempt}} \times \text{base\_delay} + \text{random\_jitter}$$

### Mã nguồn triển khai sẵn (Python):

```python
import time
import random
import requests

def call_graph_api_with_retry(url: str, params: dict, max_retries: int = 5):
    attempt = 0
    base_delay = 2  # giây
    
    while attempt < max_retries:
        response = requests.get(url, params=params)
        
        # Thành công
        if response.status_code == 200:
            return response.json()
            
        data = response.json()
        error = data.get("error", {})
        code = error.get("code")
        
        # Bắt các mã lỗi Rate Limit hoặc lỗi nội bộ Meta
        if code in [17, 613, 80004] or response.status_code in [500, 502, 503, 504]:
            attempt += 1
            # Tính toán thời gian ngủ lũy thừa + Jitter
            sleep_time = (base_delay ** attempt) + random.uniform(0.5, 2.0)
            print(f"[!] Gặp lỗi Rate Limit (Code: {code}). Thử lại lần {attempt}/{max_retries} sau {sleep_time:.2f}s...")
            time.sleep(sleep_time)
        else:
            # Các lỗi logic nghiệp vụ khác (100, 190, 200) -> Không thử lại vô ích, ném lỗi ra ngoài
            raise Exception(f"Graph API Error: {error.get('message')} (Code: {code})")
            
    raise Exception(f"Đã thử lại {max_retries} lần nhưng vẫn thất bại do quá tải Rate Limit!")
```

