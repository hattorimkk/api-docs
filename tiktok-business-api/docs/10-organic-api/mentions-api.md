# Organic API — Mentions API (Lượt nhắc)

> Phân hệ: Organic API > Mentions API (Giám sát lượt nhắc thương hiệu).
> Mentions API là công cụ đắc lực giúp doanh nghiệp giám sát toàn bộ các video TikTok có gắn thẻ (@mention) hoặc nhắc đến tài khoản doanh nghiệp, phân tích phản hồi và mức độ gắn kết của cộng đồng người dùng theo thời gian thực.

---

## Mục lục điều hướng
- [1. Giới thiệu Mentions API](#1-gioi-thieu-mentions-api)
- [2. Tổng quan lợi ích và cơ chế hoạt động](#2-tong-quan-loi-ich-va-co-che-hoat-dong)
- [3. Hướng dẫn bắt đầu từng bước](#3-huong-dan-bat-dau-tung-buoc)
- [4. Quy trình Ủy quyền tài khoản TikTok (Authorization)](#4-quy-trinh-uy-quyen-tai-khoan-tiktok-authorization)
- [5. Xác thực và Cấp phát Access Token (Authentication)](#5-xac-thuc-va-cap-phat-access-token-authentication)
- [6. Giới hạn tần suất gọi API (Rate Limits)](#6-gioi-han-tan-suat-goi-api-rate-limits)
- [7. Câu hỏi thường gặp (FAQs)](#7-cau-hoi-thuong-gap-faqs)
- [8. Phụ lục bảng mã Enum (Appendix)](#8-phu-luc-bang-ma-enum-appendix)
- [9. Danh mục Endpoint API Reference](#9-danh-muc-endpoint-api-reference)
- [10. Mã nguồn mẫu trích xuất video nhắc đến thương hiệu (Python & cURL)](#10-ma-nguon-mau-trich-xuat-video-nhac-den-thuong-hieu)

---

<a id="doc-1825103301081169"></a>
<!-- doc_id: 1825103301081169 -->
<a id="1-gioi-thieu-mentions-api"></a>
## 1. Giới thiệu Mentions API

Mentions API cho phép các thương hiệu và đối tác tích hợp tự động thu thập danh sách các video công khai có đề cập đến tài khoản TikTok của doanh nghiệp. Qua đó, doanh nghiệp có thể:
- Phát hiện kịp thời các nội dung do người dùng sáng tạo (UGC) tích cực để xin quyền chạy Spark Ads.
- Theo dõi khủng hoảng truyền thông hoặc giải đáp thắc mắc của khách hàng kịp thời.
- Đo lường mức độ viral và độ nhận diện thương hiệu trên TikTok.

---

<a id="doc-1825103341635586"></a>
<!-- doc_id: 1825103341635586 -->
<a id="2-tong-quan-loi-ich-va-co-che-hoat-dong"></a>
## 2. Tổng quan lợi ích và cơ chế hoạt động

Thấu hiểu các cuộc trò chuyện của cộng đồng về doanh nghiệp là chìa khóa then chốt cho tiếp thị hiện đại. Mentions API giúp:
- **Tập trung hóa dữ liệu phản hồi:** Tự động đồng bộ các video nhắc đến thương hiệu vào hệ thống CRM hoặc phần mềm Social Listening nội bộ.
- **Phân tích chỉ số chuyên sâu:** Thu thập lượt thích, lượt bình luận, lượt chia sẻ và lượt xem của từng video được nhắc đến.
- **Chuyển đổi thành tài sản quảng cáo:** Kết hợp trực tiếp với Spark Ads để biến video UGC chất lượng thành quảng cáo trả phí chỉ qua vài bước gọi API.

---

<a id="doc-1825103402321025"></a>
<!-- doc_id: 1825103402321025 -->
<a id="doc-1825103422736385"></a>
<!-- doc_id: 1825103422736385 -->
<a id="3-huong-dan-bat-dau-tung-buoc"></a>
## 3. Hướng dẫn bắt đầu từng bước

Quy trình tích hợp Mentions API bao gồm 5 bước cốt lõi:
1. **Chuẩn bị tài khoản:** Đảm bảo bạn đã có tài khoản TikTok For Business và tài khoản nhà phát triển đã được phê duyệt.
2. **Cấu hình ứng dụng:** Đăng ký ứng dụng nhà phát triển, chọn quyền hạn thuộc nhóm **TikTok Accounts**.
3. **Ủy quyền từ chủ tài khoản TikTok:** Chia sẻ đường dẫn ủy quyền để chủ sở hữu tài khoản TikTok cấp quyền truy cập.
4. **Đổi mã ủy quyền lấy Token:** Gọi endpoint xác thực `/tt_user/oauth2/token/` để lấy `access_token` và `refresh_token`.
5. **Gọi API trích xuất dữ liệu Mentions:** Sử dụng `access_token` để truy vấn danh sách video và chỉ số chi tiết.

---

<a id="doc-1825103730490434"></a>
<!-- doc_id: 1825103730490434 -->
<a id="4-quy-trinh-uy-quyen-tai-khoan-tiktok-authorization"></a>
## 4. Quy trình Ủy quyền tài khoản TikTok (Authorization)

Trước khi gọi Mentions API, nhà phát triển cần được sự đồng ý ủy quyền từ tài khoản TikTok của doanh nghiệp.

### Điều kiện tiên quyết:
- Tài khoản TikTok phải là **TikTok Account with Advanced Access** hoặc **Verified Business Account** (xác minh dấu tích xanh doanh nghiệp).
- Để kiểm tra điều kiện này, gọi endpoint `/business/get/` và xác nhận trường phản hồi `has_advanced_access` có giá trị `true`.

### Quy tắc cấu hình Redirect URL:
Bạn có thể cấu hình tối đa 10 URL chuyển hướng (Redirect URL) trong trang cài đặt ứng dụng. URL bắt buộc phải tuân theo các quy chuẩn an toàn:

| No. | Quy tắc cấu hình | Ví dụ hợp lệ | Ví dụ không hợp lệ |
|---|---|---|---|
| 1 | URL phải là đường dẫn tuyệt đối và kết thúc bằng dấu `/` | `https://dev.example.com/auth/callback/` | `https://dev.example.com/auth/callback` (thiếu dấu `/` ở cuối) |
| 2 | URL phải là đường dẫn tĩnh, không chứa tham số query | `https://dev.example.com/auth/callback/` | `https://dev.example.com/auth/callback/?id=1` (chứa tham số query) |
| 3 | URL không được chứa ký tự neo `#` (fragment) | `https://dev.example.com/auth/callback/` | `https://dev.example.com/auth/callback/#1` (chứa fragment) |
| 4 | URL bắt buộc phải sử dụng giao thức bảo mật `https://` | `https://dev.example.com/auth/callback/` | `http://dev.example.com/auth/callback/` (dùng `http`) |
| 5 | URL không được chứa cổng chỉ định (port number) | `https://dev.example.com/auth/callback/` | `https://dev.example.com:3000/auth/callback/` (chứa `:3000`) |
| 6 | Độ dài ký tự phải nằm trong khoảng từ 10 đến 512 ký tự | N/A | N/A |

> **Chống tấn công CSRF bằng tham số `state`:** Khuyến nghị luôn thêm tham số `state` duy nhất vào URL ủy quyền. Giá trị này sẽ được trả nguyên vẹn về callback URL để ứng dụng kiểm tra tính hợp lệ trước khi cấp token.

---

<a id="doc-1825105003772930"></a>
<!-- doc_id: 1825105003772930 -->
<a id="5-xac-thuc-va-cap-phat-access-token-authentication"></a>
## 5. Xác thực và Cấp phát Access Token (Authentication)

Sau khi chủ tài khoản TikTok đồng ý ủy quyền, hệ thống sẽ chuyển hướng về callback URL kèm theo mã `auth_code`. Bạn sử dụng mã này để đổi lấy `access_token` dài hạn và `refresh_token`.

> **Quy định thời hạn Token:**
> - `access_token` có hiệu lực trong vòng **24 giờ** (86.400 giây).
> - `refresh_token` có hiệu lực trong vòng **1 năm** (31.536.000 giây). Dùng để gia hạn `access_token` mà người dùng không cần đăng nhập ủy quyền lại.

### 5.1. Lấy Access Token lần đầu (`POST /open_api/v1.3/tt_user/oauth2/token/`)

**Header:**
- `Content-Type`: `application/json`

**Tham số Body:**

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `client_id` | string | **Bắt buộc** | App ID của ứng dụng nhà phát triển. Lấy tại **My Apps > App Detail > Basic Information**. |
| `client_secret` | string | **Bắt buộc** | Secret key của ứng dụng nhà phát triển. |
| `grant_type` | string | **Bắt buộc** | Phương thức tạo token. Giá trị Enum: `authorization_code`. |
| `auth_code` | string | **Bắt buộc** | Mã ủy quyền nhận được trong query string của callback URL sau khi người dùng phê duyệt. |
| `redirect_uri` | string | **Bắt buộc** | URL chuyển hướng đã đăng ký và khớp chính xác với URL lúc khởi tạo ủy quyền. |

**Cấu trúc phản hồi:**

| Field | Data Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). |
| `request_id` | string | ID duy nhất nhận diện request. |
| `data` | object | Dữ liệu phiên xác thực. |
| ↳ `access_token` | string | Access token đại diện cho tài khoản TikTok của doanh nghiệp, dùng để gọi các endpoint Mentions. |
| ↳ `token_type` | string | Loại token. Giá trị: `Bearer`. |
| ↳ `scope` | string | Danh sách các quyền hạn được cấp (phân cách bởi dấu phẩy). |
| ↳ `expires_in` | number | Thời gian hết hạn của access token tính bằng giây (86400). |
| ↳ `refresh_token` | string | Token dùng để làm mới access token khi hết hạn. Cần lưu trữ bảo mật. |
| ↳ `refresh_token_expires_in` | number | Thời gian hết hạn của refresh token (31536000 giây). |
| ↳ `open_id` | string | Định danh duy nhất của tài khoản TikTok đối với ứng dụng này. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000109",
  "data": {
    "access_token": "act.example_token_abcdef123456",
    "token_type": "Bearer",
    "expires_in": 86400,
    "refresh_token": "rft.example_refresh_token_987654",
    "refresh_token_expires_in": 31536000,
    "open_id": "_000abc123def456ghi",
    "scope": "video.list,video.insights,user.info.basic,biz.brand.insights,biz.spark.auth"
  }
}
```

### 5.2. Làm mới Access Token (`POST /open_api/v1.3/tt_user/oauth2/refresh_token/`)

Khi `access_token` hết hạn (sau 24h), sử dụng `refresh_token` để lấy token mới:

**Tham số Body:**
- `client_id`: App ID của ứng dụng.
- `client_secret`: Secret key của ứng dụng.
- `grant_type`: `refresh_token`.
- `refresh_token`: Chuỗi refresh token đã lưu trước đó.

---

<a id="doc-1825107305621506"></a>
<!-- doc_id: 1825107305621506 -->
<a id="6-gioi-han-tan-suat-goi-api-rate-limits"></a>
## 6. Giới hạn tần suất gọi API (Rate Limits)

Mentions API áp dụng chính sách giới hạn tốc độ chung của nền tảng (Global rate limits).
Chi tiết tra cứu tại [Giới hạn tốc độ toàn cục](../04-get-started/bat-dau.md#doc-1740029171730433).

---

<a id="doc-1825107469360130"></a>
<!-- doc_id: 1825107469360130 -->
<a id="7-cau-hoi-thuong-gap-faqs"></a>
## 7. Câu hỏi thường gặp (FAQs)

### Q: Có độ trễ nào giữa thời điểm video được đăng và thời điểm xuất hiện trên Mentions API không?
- Video công khai nhắc đến tài khoản thường xuất hiện trong dữ liệu Mentions trong vòng **15 đến 30 phút** sau khi đăng tải. Các chỉ số tương tác (views, likes, shares) được làm mới định kỳ mỗi vài giờ.

### Q: Có thể lấy được video ở chế độ riêng tư (Private) không?
- Không. API chỉ hỗ trợ các video được người dùng xuất bản ở chế độ công khai (Public).

---

<a id="doc-1825107519114241"></a>
<!-- doc_id: 1825107519114241 -->
<a id="8-phu-luc-bang-ma-enum-appendix"></a>
## 8. Phụ lục bảng mã Enum (Appendix)

Bảng tổng hợp các giá trị enum phổ biến được sử dụng trong các endpoint Mentions API:
- `mention_type`: Loại đề cập (`MENTION` = gắn thẻ @, `HASHTAG` = dùng thẻ hashtag thương hiệu).
- `post_status`: Trạng thái bài đăng (`NORMAL` = hiển thị bình thường, `DELETED` = đã xóa).

---

<a id="doc-1825107783639042"></a>
<!-- doc_id: 1825107783639042 -->
<a id="9-danh-muc-endpoint-api-reference"></a>
## 9. Danh mục Endpoint API Reference

Toàn bộ các endpoint thao tác dữ liệu chi tiết của Mentions API được quy định tại [API Reference — Lượt nhắc (Mentions)](../12-api-reference/51-mentions.md#doc-1825107837430850):
- Lấy danh sách video nhắc đến thương hiệu (`/business/video/mention/list/`)
- Lấy thông tin chi tiết video nhắc đến thương hiệu (`/business/video/mention/get/`)
- Lấy danh sách bình luận trên video nhắc đến thương hiệu (`/business/video/mention/comment/list/`)

---

<a id="10-ma-nguon-mau-trich-xuat-video-nhac-den-thuong-hieu"></a>
## 10. Mã nguồn mẫu trích xuất video nhắc đến thương hiệu (Python & cURL)

### cURL trích xuất danh sách video nhắc đến tài khoản
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/business/video/mention/list/?business_id=YOUR_BUSINESS_ID&page=1&page_size=20" \
  -H "Access-Token: YOUR_BUSINESS_ACCESS_TOKEN"
```

### Python script trích xuất và lưu trữ video mentions
```python
import requests
import json

ACCESS_TOKEN = "YOUR_BUSINESS_ACCESS_TOKEN"
BUSINESS_ID = "YOUR_BUSINESS_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN
}

def get_brand_mentions(business_id, page=1, page_size=20):
    """Trích xuất danh sách video công khai nhắc đến tài khoản thương hiệu."""
    url = f"{BASE_URL}/business/video/mention/list/"
    params = {
        "business_id": business_id,
        "page": page,
        "page_size": page_size
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if data.get("code") == 0:
        mentions = data.get("data", {}).get("list", [])
        print(f"Thu thập được {len(mentions)} video đề cập đến thương hiệu:")
        for video in mentions:
            item_id = video.get("item_id")
            author = video.get("author_name")
            views = video.get("view_count")
            likes = video.get("like_count")
            desc = video.get("title", "")
            print(f" - [{item_id}] Tác giả: @{author} | Views: {views} | Likes: {likes}")
            print(f"   Mô tả: {desc[:60]}...")
        return mentions
    else:
        print(f"Lỗi truy vấn: {data.get('code')} - {data.get('message')}")
        return []

if __name__ == "__main__":
    get_brand_mentions(BUSINESS_ID)
```

