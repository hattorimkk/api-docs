# Điều khoản (Terms)

> Phân hệ: API Reference > Terms (Điều khoản và Thỏa thuận tính năng).
> Hướng dẫn tra cứu nội dung thỏa thuận, ký kết điều khoản điều kiện và kiểm tra trạng thái ký kết trước khi sử dụng các tính năng quảng cáo yêu cầu cam kết pháp lý (chẳng hạn như Lead Generation Ads).

---

## Mục lục điều hướng
- [1. Tổng quan phân hệ Điều khoản (Terms)](#1-tong-quan-phan-he-dieu-khoan-terms)
- [2. Lấy nội dung điều khoản (`GET /open_api/v1.3/term/get/`)](#2-lay-noi-dung-dieu-khoan)
- [3. Ký kết điều khoản (`POST /open_api/v1.3/term/confirm/`)](#3-ky-ket-dieu-khoan)
- [4. Kiểm tra trạng thái ký kết điều khoản (`GET /open_api/v1.3/term/check/`)](#4-kiem-tra-trang-thai-ky-ket-dieu-khoan)
- [5. Mã nguồn mẫu Data Retrieval & Automation (Python & cURL)](#5-ma-nguon-mau-data-retrieval--automation)

---

<a id="doc-1737191804348417"></a>
<!-- doc_id: 1737191804348417 -->
<a id="1-tong-quan-phan-he-dieu-khoan-terms"></a>
## 1. Tổng quan phân hệ Điều khoản (Terms)

Trước khi có thể sử dụng một số tính năng quảng cáo đặc thù (như Quảng cáo tìm kiếm khách hàng tiềm năng - Lead Generation Ads), bạn cần phải ký thỏa thuận điều khoản dịch vụ với TikTok. 

Terms API cho phép:
* [Lấy nội dung điều khoản (`/term/get/`)](67-terms.md#doc-1737191909315585)
* [Ký kết chấp thuận điều khoản (`/term/confirm/`)](67-terms.md#doc-1737192284435457)
* [Kiểm tra trạng thái ký kết điều khoản (`/term/check/`)](67-terms.md#doc-1737192304571394)

---

<a id="doc-1737191909315585"></a>
<!-- doc_id: 1737191909315585 -->
<a id="2-lay-noi-dung-dieu-khoan"></a>
## 2. Lấy nội dung điều khoản (Get Terms)

Sử dụng endpoint này để lấy nội dung thỏa thuận điều khoản cho tính năng Lead Generation Ads. Bạn cần chỉ định tính năng muốn lấy điều khoản thông qua trường `term_type`.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/term/get/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `lang` | string | Không | Ngôn ngữ của bản thỏa thuận. Giá trị Enum: `EN` (Tiếng Anh), `JA` (Tiếng Nhật), `ZH` (Tiếng Trung). Mặc định: `EN`. |
| `term_type` | string | **Bắt buộc** | Loại thỏa thuận điều khoản. Giá trị Enum: `LeadAds`. |

### Cấu trúc phản hồi (Response)

| Field | Data Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). |
| `request_id` | string | ID duy nhất nhận diện request phục vụ tra cứu log. |
| `data` | object | Dữ liệu điều khoản trả về. |
| ↳ `terms` | string[] | Mảng chứa nội dung văn bản hoặc đường link dẫn đến văn bản thỏa thuận điều khoản chính thức. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000111",
  "data": {
    "terms": [
      "Vui lòng tham khảo chính sách và điều khoản tại liên kết sau:",
      "https://ads.tiktok.com/i18n/official/policy/lead-gen-terms"
    ]
  }
}
```

---

<a id="doc-1737192284435457"></a>
<!-- doc_id: 1737192284435457 -->
<a id="3-ky-ket-dieu-khoan"></a>
## 3. Ký kết điều khoản (Sign Terms)

Sử dụng endpoint này để xác nhận ký kết điện tử chấp thuận điều khoản cho tính năng quảng cáo Lead Generation. Sau khi ký kết, bạn có thể gọi [/term/check/](67-terms.md#doc-1737192304571394) để xác nhận trạng thái.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/term/confirm/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): `application/json`.

### Tham số (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `term_type` | string | **Bắt buộc** | Loại điều khoản cần ký kết. Giá trị Enum: `LeadAds`. |

### Cấu trúc phản hồi (Response)

| Field | Data Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu rỗng khi xác nhận ký kết thành công (`{}`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000112",
  "data": {}
}
```

---

<a id="doc-1737192304571394"></a>
<!-- doc_id: 1737192304571394 -->
<a id="4-kiem-tra-trang-thai-ky-ket-dieu-khoan"></a>
## 4. Kiểm tra trạng thái ký kết điều khoản (Check the status of Terms)

Sử dụng endpoint này để kiểm tra xem tài khoản quảng cáo đã hoàn tất việc ký kết thỏa thuận cho tính năng tương ứng hay chưa trước khi tạo chiến dịch.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/term/check/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `term_type` | string | **Bắt buộc** | Loại thỏa thuận cần kiểm tra. Giá trị Enum: `LeadAds`. |

### Cấu trúc phản hồi (Response)

| Field | Data Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trạng thái điều khoản. |
| ↳ `confirmed` | boolean | Trạng thái ký kết thỏa thuận: `true` = Đã ký thành công; `false` = Chưa ký kết. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000113",
  "data": {
    "confirmed": true
  }
}
```

---

<a id="5-ma-nguon-mau-data-retrieval--automation"></a>
## 5. Mã nguồn mẫu Data Retrieval & Automation (Python & cURL)

### cURL kiểm tra và ký thỏa thuận Lead Ads
```bash
# 1. Kiểm tra trạng thái ký kết điều khoản
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/term/check/?advertiser_id=YOUR_ADVERTISER_ID&term_type=LeadAds" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"

# 2. Xác nhận ký kết điều khoản
curl -s -X POST "https://business-api.tiktok.com/open_api/v1.3/term/confirm/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "term_type": "LeadAds"
  }'
```

### Python script tự động kiểm tra và ký thỏa thuận
```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def ensure_terms_signed(advertiser_id, term_type="LeadAds"):
    """Kiểm tra và tự động xác nhận ký kết điều khoản nếu chưa ký."""
    check_url = f"{BASE_URL}/term/check/"
    params = {"advertiser_id": advertiser_id, "term_type": term_type}
    
    res = requests.get(check_url, headers=headers, params=params).json()
    if res.get("code") == 0:
        is_signed = res.get("data", {}).get("confirmed", False)
        print(f"Trạng thái điều khoản '{term_type}': {'Đã ký' if is_signed else 'Chưa ký'}")
        
        if not is_signed:
            print(f"Đang tiến hành ký kết điều khoản '{term_type}'...")
            confirm_url = f"{BASE_URL}/term/confirm/"
            payload = {"advertiser_id": advertiser_id, "term_type": term_type}
            conf_res = requests.post(confirm_url, headers=headers, json=payload).json()
            if conf_res.get("code") == 0:
                print("Ký kết thỏa thuận thành công!")
                return True
            else:
                print(f"Lỗi ký thỏa thuận: {conf_res.get('code')} - {conf_res.get('message')}")
                return False
        return True
    else:
        print(f"Lỗi kiểm tra: {res.get('code')} - {res.get('message')}")
        return False

if __name__ == "__main__":
    ensure_terms_signed(ADVERTISER_ID, "LeadAds")
```

