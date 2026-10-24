# Video API — Quản Lý Video Quảng Cáo

> **Phân hệ**: Creative API > Video Management  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Video là định dạng tài nguyên sáng tạo quan trọng nhất trên TikTok. Video API cho phép bạn:
- Tải lên video quảng cáo từ tệp máy tính cục bộ (Multipart upload) hoặc từ đường dẫn URL công khai.
- Tải lên các video dung lượng lớn qua cơ chế phân đoạn (Chunked upload).
- Tự động phát hiện và sửa các lỗi video thường gặp (độ phân giải thấp, sai tỷ lệ khung hình) thông qua tính năng **Smart Fix**.
- Lấy thông tin chi tiết kỹ thuật của video (độ phân giải, thời lượng, tỷ lệ khung hình, định dạng, bitrate).
- Tìm kiếm và lọc video trong thư viện theo ngày tạo, tên tệp, trạng thái.
- Lấy danh sách ảnh bìa (thumbnail/cover) được thuật toán AI đề xuất để tăng tỷ lệ nhấp.

---

## 📋 2. Tiêu chuẩn kỹ thuật video trên TikTok

Khi tải video lên để sử dụng trong quảng cáo, bạn cần bảo đảm các thông số sau:
- **Tỷ lệ khung hình (Aspect Ratio)**: Khuyến nghị chuẩn **9:16** (dọc - 720x1280 px trở lên), **1:1** (vuông - 640x640 px), hoặc **16:9** (ngang - 1280x720 px).
- **Định dạng tệp hỗ trợ**: `.mp4`, `.mov`, `.mpeg`, `.3gp`, `.avi`.
- **Dung lượng tệp tối đa**: 500 MB cho tải trực tiếp (`UPLOAD_BY_FILE`). Đối với tệp lớn hơn, sử dụng cơ chế chunk upload.
- **Thời lượng video**: Từ 5 giây đến 60 giây (khuyến nghị hiệu quả cao nhất: 9 - 15 giây).

---

## 🚀 3. Danh sách Endpoints & Hướng dẫn cURL

### 3.1. Tải lên video quảng cáo (`/file/video/ad/upload/`)

Endpoint này hỗ trợ tải video lên thư viện tài nguyên của nhà quảng cáo. Kết quả trả về sẽ bao gồm `video_id` dùng để tạo quảng cáo.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/`
- **Phương thức**: `POST`

#### Cách 1: Tải lên bằng tệp cục bộ (`UPLOAD_BY_FILE`)

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -F "advertiser_id=7123456789012345678" \
  -F "upload_type=UPLOAD_BY_FILE" \
  -F "file_name=quang_cao_tet_2026.mp4" \
  -F "video_file=@/duong/dan/toi/video_quang_cao.mp4" \
  -F "flaw_detect=true" \
  -F "auto_fix_enabled=true" \
  -F "auto_bind_enabled=true"
```

#### Cách 2: Tải lên qua đường dẫn URL công khai (`UPLOAD_BY_URL`)

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "upload_type": "UPLOAD_BY_URL",
    "file_name": "video_banner_xuan.mp4",
    "video_url": "https://cdn.example.com/videos/banner_spring_2026.mp4",
    "flaw_detect": true,
    "auto_fix_enabled": true
  }'
```

#### Bảng tham số yêu cầu (Request Parameters)

| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
| :--- | :--- | :---: | :--- |
| `advertiser_id` | string | **Có** | ID tài khoản quảng cáo TikTok sở hữu video. |
| `upload_type` | string | Không | Phương thức tải lên. Mặc định `UPLOAD_BY_FILE`. Giá trị hỗ trợ: `UPLOAD_BY_FILE`, `UPLOAD_BY_URL`, `UPLOAD_BY_FILE_ID`, `UPLOAD_BY_VIDEO_ID`. |
| `file_name` | string | Không | Tên lưu trữ của video (1 - 100 ký tự). Không được trùng lặp trong cùng một `advertiser_id`. |
| `video_file` | binary file | Điều kiện | Bắt buộc khi `upload_type=UPLOAD_BY_FILE`. Đường dẫn tệp tin trên máy tính. |
| `video_url` | string | Điều kiện | Bắt buộc khi `upload_type=UPLOAD_BY_URL`. URL có thể truy cập công khai. |
| `flaw_detect` | boolean | Không | Bật tính năng tự động quét lỗi kỹ thuật video. Mặc định `false`. |
| `auto_fix_enabled`| boolean | Không | Tự động sửa lỗi độ phân giải thấp (`LOW_RESOLUTION`) và kích thước sai chuẩn (`ILLEGAL_VIDEO_SIZE`). |
| `auto_bind_enabled`| boolean | Không | Tự động thêm video đã sửa lỗi vào thư viện tài nguyên sáng tạo. |

#### Phản hồi mẫu thành công (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224800010245041042005A1B2C",
  "data": {
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "size": 15420310,
    "width": 720,
    "height": 1280,
    "video_cover_url": "https://p16-va.tiktokcdn.com/obj/tos-maliva-p-0068/cover_example.jpeg",
    "duration": 15.2,
    "format": "mp4",
    "bit_rate": 2048000,
    "flaw_types": []
  }
}
```

---

### 3.2. Lấy thông tin chi tiết video (`/file/video/ad/info/`)

Tra cứu các thuộc tính kỹ thuật và trạng thái của danh sách `video_id`.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/video/ad/info/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/info/?advertiser_id=7123456789012345678&video_ids=%5B%22v10033g50000cf7m1g3c77u3g2example%22%5D" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224810010245041042005D3E4F",
  "data": {
    "list": [
      {
        "video_id": "v10033g50000cf7m1g3c77u3g2example",
        "file_name": "quang_cao_tet_2026.mp4",
        "signature": "d41d8cd98f00b204e9800998ecf8427e",
        "width": 720,
        "height": 1280,
        "duration": 15.2,
        "format": "mp4",
        "size": 15420310,
        "video_cover_url": "https://p16-va.tiktokcdn.com/obj/cover_example.jpeg",
        "create_time": "2026-10-23 21:00:00"
      }
    ]
  }
}
```

---

### 3.3. Tìm kiếm video trong tài khoản (`/file/video/ad/search/`)

Hỗ trợ phân trang và lọc video theo nhiều tiêu chí (tên file, khoảng thời gian tạo).

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/video/ad/search/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/search/?advertiser_id=7123456789012345678&page=1&page_size=20&start_time=2026-10-01+00%3A00%3A00&end_time=2026-10-23+23%3A59%3A59" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 3.4. Cập nhật tên video (`/file/video/ad/update/`)

Đổi tên video đã lưu trữ trong thư viện để dễ quản lý.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/file/video/ad/update/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/update/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "file_name": "quang_cao_tet_2026_da_chinh_sua.mp4"
  }'
```

---

### 3.5. Lấy danh sách ảnh bìa đề xuất (`/file/video/suggestcover/`)

Hệ thống AI tự động phân tích khung hình video và đề xuất các ảnh bìa có tiềm năng thu hút tương tác cao nhất.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/file/video/suggestcover/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/suggestcover/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "video_id": "v10033g50000cf7m1g3c77u3g2example"
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224820010245041042005G5H6I",
  "data": {
    "list": [
      {
        "id": "cover_hash_01",
        "url": "https://p16-va.tiktokcdn.com/obj/tos-maliva-p-0068/frame_3s.jpeg"
      },
      {
        "id": "cover_hash_02",
        "url": "https://p16-va.tiktokcdn.com/obj/tos-maliva-p-0068/frame_7s.jpeg"
      }
    ]
  }
}
```

---

### 3.6. Kiểm tra tên tệp có bị trùng lặp (`/file/name/check/`)

Kiểm tra xem tên video hoặc hình ảnh đã tồn tại trong tài khoản quảng cáo hay chưa trước khi tiến hành tải lên.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/name/check/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/name/check/?advertiser_id=7123456789012345678&file_name=quang_cao_tet_2026.mp4&file_type=VIDEO" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 3.7. Tải lên tệp video lớn theo phân đoạn (Chunk Upload)

Khi video có dung lượng lớn hơn 100MB hoặc đường truyền mạng không ổn định, hãy sử dụng quy trình 3 bước:

#### Bước 1: Khởi tạo phiên tải lên (`/file/start/upload/`)

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/start/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "file_name": "video_sieu_net_4k.mp4",
    "file_type": "VIDEO",
    "file_size": 209715200
  }'
```
*Nhận về `upload_id`.*

#### Bước 2: Tải lên từng phân đoạn (`/file/transfer/upload/`)

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/transfer/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -F "advertiser_id=7123456789012345678" \
  -F "upload_id=UPLOAD_ID_BUOC_1" \
  -F "chunk_index=0" \
  -F "chunk_file=@/duong/dan/toi/part_0.bin"
```

#### Bước 3: Hoàn tất phiên tải lên (`/file/finish/upload/`)

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/finish/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "upload_id": "UPLOAD_ID_BUOC_1"
  }'
```
*Hệ thống ghép nối các khối và trả về `video_id` hoàn chỉnh.*
