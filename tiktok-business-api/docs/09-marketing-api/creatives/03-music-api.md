# Music API — Quản Lý Âm Nhạc Thương Mại

> **Phân hệ**: Creative API > Music & Audio Management  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Âm nhạc là linh hồn của nền tảng TikTok ("Sound-On Platform"). Hơn 88% người dùng TikTok bật âm thanh khi xem video. Để video quảng cáo được phân phối hợp pháp mà không bị tắt tiếng hoặc vi phạm bản quyền thương mại:
- TikTok cung cấp **Thư viện nhạc thương mại (Commercial Music Library - CML)** với hàng triệu bài hát đã được cấp quyền sử dụng trong quảng cáo trên toàn cầu.
- Music API cho phép bạn duyệt danh mục nhạc, nghe thử, chọn bài hát theo thể loại/tâm trạng (genres, moods), tải nhạc riêng lên và ủy quyền quyền sử dụng âm nhạc.

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Lấy danh sách nhạc thương mại (`/file/music/get/`)

Tra cứu và lọc bài hát trong Thư viện nhạc thương mại của TikTok theo khu vực quảng cáo mục tiêu.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/music/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/music/get/?advertiser_id=7123456789012345678&page=1&page_size=20&country=VN&keyword=pop" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

#### Bảng tham số yêu cầu (Request Parameters)

| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
| :--- | :--- | :---: | :--- |
| `advertiser_id` | string | **Có** | ID tài khoản quảng cáo. |
| `country` | string | Không | Mã quốc gia mục tiêu (ví dụ `VN`, `US`, `TH`). Giúp đảm bảo bản quyền bài hát hợp lệ tại thị trường đó. |
| `keyword` | string | Không | Từ khóa tìm kiếm tên bài hát, nghệ sĩ. |
| `page` | integer | Không | Số trang truy vấn (mặc định: 1). |
| `page_size` | integer | Không | Số lượng bài hát mỗi trang (tối đa: 50). |

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224920010245041042005L1M2N",
  "data": {
    "list": [
      {
        "music_id": "7198273645123984512",
        "title": "Summer Vibes 2026",
        "author": "TikTok Sound Studio",
        "duration": 60,
        "play_url": "https://sf16-ies-music-va.tiktokcdn.com/obj/tos-useast2a-v-27dcd7/sample.mp3",
        "cover_url": "https://p16-va.tiktokcdn.com/obj/cover_music.jpeg"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 20,
      "total_number": 1500,
      "total_page": 75
    }
  }
}
```

---

### 2.2. Tải lên tệp âm thanh bản quyền riêng (`/file/music/upload/`)

Nếu doanh nghiệp của bạn sở hữu bài nhạc độc quyền (có đầy đủ giấy phép bản quyền thương mại), bạn có thể tải lên tệp âm thanh để ghép vào video quảng cáo.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/file/music/upload/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/music/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -F "advertiser_id=7123456789012345678" \
  -F "file_name=jingle_tet_thuong_hieu.mp3" \
  -F "music_file=@/duong/dan/toi/jingle_brand.mp3"
```

---

### 2.3. Quản lý ủy quyền âm nhạc (`/identity/music/authorization/`)

Kiểm tra và thiết lập quyền sử dụng bài nhạc giữa tài khoản thương hiệu và tài khoản nhà sáng tạo Creator (hỗ trợ cho Spark Ads).

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/identity/music/authorization/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/identity/music/authorization/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "music_id": "7198273645123984512",
    "action": "AUTHORIZE"
  }'
```
