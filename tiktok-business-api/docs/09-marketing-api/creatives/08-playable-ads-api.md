# Playable Ads API — Quảng Cáo Tương Tác (Mini Game HTML5)

> **Phân hệ**: Creative API > Interactive & Playable Ads  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

**Playable Ads (Quảng cáo có thể chơi được)** là định dạng quảng cáo tương tác đặc biệt phổ biến trong ngành game di động và ứng dụng tiện ích. Người dùng có thể trải nghiệm trực tiếp một màn chơi mini (demo gameplay) ngay trong luồng lướt TikTok mà không cần cài đặt ứng dụng trước.

Playable Ads API cho phép bạn:
- Tải lên gói tệp zip chứa mã nguồn HTML5, JS, CSS và assets đồ họa.
- Xác thực tính hợp lệ của tệp theo chuẩn kỹ thuật của TikTok (kích thước file, số lượng request HTTP nội bộ).
- Lưu và liên kết tài liệu Playable với các chiến dịch cài đặt ứng dụng (App Install).

---

## 📋 2. Tiêu chuẩn kỹ thuật tệp Playable

- **Định dạng đóng gói**: Tệp nén `.zip`.
- **Dung lượng tối đa**: 5 MB (khuyến nghị dưới 2 MB để tải nhanh trên mạng di động).
- **Cấu trúc tệp**: Bắt buộc có tệp `index.html` tại thư mục gốc của file zip.
- **Tương thích**: Hỗ trợ đầy đủ cả hai hướng màn hình dọc (Portrait) và ngang (Landscape).

---

## 🚀 3. Danh sách Endpoints & Hướng dẫn cURL

### 3.1. Tải lên tệp Playable (`/playable/upload/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/playable/upload/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/playable/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -F "advertiser_id=7123456789012345678" \
  -F "playable_file=@/duong/dan/toi/mini_game_demo.zip" \
  -F "playable_name=Mini_Game_Tet_2026"
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225100010245041042005G7H8I",
  "data": {
    "playable_id": "pl_7291823746501928374",
    "playable_url": "https://ads.tiktok.com/playable/demo_preview/...",
    "status": "VALIDATING"
  }
}
```

---

### 3.2. Xác thực tính hợp lệ tệp Playable (`/playable/validate/`)

Kiểm tra xem tệp zip có đáp ứng đủ các tiêu chuẩn kỹ thuật về hiệu năng và bảo mật hay không.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/playable/validate/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/playable/validate/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "playable_id": "pl_7291823746501928374"
  }'
```

---

### 3.3. Lấy danh sách tài liệu Playable đã lưu (`/playable/get/`)

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/playable/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/playable/get/?advertiser_id=7123456789012345678&page=1&page_size=10" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 3.4. Xóa tài liệu Playable (`/playable/delete/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/playable/delete/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/playable/delete/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "playable_ids": ["pl_7291823746501928374"]
  }'
```
