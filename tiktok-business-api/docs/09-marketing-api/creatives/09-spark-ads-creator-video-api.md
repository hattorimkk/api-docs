# Spark Ads & Creator Video API — Quảng Cáo Video Tự Nhiên & Nhà Sáng Tạo

> **Phân hệ**: Creative API > Spark Ads & Creator Content  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

**Spark Ads** là định dạng quảng cáo đặc quyền của TikTok, cho phép bạn tận dụng chính các video tự nhiên (Organic TikTok posts) đã đăng tải trên kênh TikTok của thương hiệu hoặc từ các Nhà sáng tạo nội dung (KOL / KOC) để chạy quảng cáo:
- Giữ nguyên 100% lượt thích, bình luận, chia sẻ và theo dõi tài khoản TikTok gốc.
- Tăng tính chân thực, không tạo cảm giác gượng gạo như video quảng cáo truyền thống.
- Hỗ trợ ủy quyền qua **mã Spark Ads (Authorization Code)** do Creator cung cấp hoặc liên kết trực tiếp qua danh tính thương hiệu (Identity).

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Ủy quyền video bằng mã Spark Ads (`/tt_video/authorize/`)

Khi Creator bật tính năng quảng cáo trên ứng dụng TikTok và cung cấp mã ủy quyền (ví dụ `7182930491827364512_code`), nhà quảng cáo gọi API này để liên kết video vào tài khoản quảng cáo.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/tt_video/authorize/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/tt_video/authorize/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "auth_code": "7182930491827364512_auth_code_creator"
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225110010245041042005J9K0L",
  "data": {
    "item_id": "7182930491827364512",
    "video_id": "v10033g50000cf7m1g3c77u3g2spark",
    "author_name": "NguyenVanA_Creator",
    "status": "AUTHORIZED"
  }
}
```

---

### 2.2. Lấy danh sách video từ kênh TikTok đã liên kết (`/identity/video/get/`)

Nếu tài khoản quảng cáo đã liên kết kênh TikTok chính thức thông qua Business Center (Identity), bạn có thể trực tiếp lấy danh sách các video đã đăng trên kênh để chạy quảng cáo.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/identity/video/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/identity/video/get/?advertiser_id=7123456789012345678&identity_id=7192837465019283746&identity_type=CUSTOMIZED_USER&page=1&page_size=20" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.3. Lấy thông tin chi tiết một video tự nhiên (`/tt_video/info/`)

Tra cứu số lượt xem tự nhiên, bình luận, thả tim và nội dung mô tả của video trước khi quyết định chi ngân sách quảng cáo.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/tt_video/info/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/tt_video/info/?advertiser_id=7123456789012345678&item_id=7182930491827364512" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.4. Hủy liên kết video Spark Ads (`/tt_video/unbind/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/tt_video/unbind/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/tt_video/unbind/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "item_id": "7182930491827364512"
  }'
```
