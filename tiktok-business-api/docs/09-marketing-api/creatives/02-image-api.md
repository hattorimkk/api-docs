# Image API — Quản Lý Hình Ảnh Quảng Cáo

> **Phân hệ**: Creative API > Image Management  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Hình ảnh được sử dụng rộng rãi trên TikTok trong các định dạng:
- Quảng cáo xoay vòng (Carousel Ads / Collection Ads).
- Quảng cáo hiển thị trên mạng lưới Pangle hoặc trang tin tức BuzzVideo.
- Ảnh đại diện thương hiệu (Avatar), ảnh bìa video (Video Cover), hình ảnh trang đích tức thì (Instant Pages).

Image API cung cấp các chức năng:
- Tải lên hình ảnh từ tệp cục bộ (`UPLOAD_BY_FILE`) hoặc đường dẫn URL (`UPLOAD_BY_URL`).
- Tra cứu thông tin hình ảnh theo `image_id` (kích thước, tỷ lệ, định dạng, chữ ký MD5).
- Tìm kiếm và lọc hình ảnh trong thư viện quảng cáo theo thời gian tạo.
- Công cụ chỉnh sửa và cắt cúp hình ảnh thông minh theo tỷ lệ chuẩn.

---

## 📋 2. Tiêu chuẩn kỹ thuật hình ảnh

- **Định dạng hỗ trợ**: `.jpg`, `.jpeg`, `.png`.
- **Dung lượng tối đa**: 100 MB cho mỗi tệp.
- **Tỷ lệ khuyến nghị**:
  - Dọc: **9:16** (ví dụ 720x1280 px)
  - Vuông: **1:1** (ví dụ 1200x1200 px, 640x640 px)
  - Ngang: **16:9** (ví dụ 1200x628 px trên Pangle)

---

## 🚀 3. Danh sách Endpoints & Hướng dẫn cURL

### 3.1. Tải lên hình ảnh quảng cáo (`/file/image/ad/upload/`)

Endpoint nhận ảnh và lưu trữ vào thư viện tài nguyên, trả về `image_id` để sử dụng tạo quảng cáo.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/file/image/ad/upload/`
- **Phương thức**: `POST`

#### Cách 1: Tải lên từ tệp máy tính cục bộ

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/image/ad/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -F "advertiser_id=7123456789012345678" \
  -F "upload_type=UPLOAD_BY_FILE" \
  -F "file_name=banner_khuyen_mai_tet.png" \
  -F "image_file=@/duong/dan/toi/banner_tet.png"
```

#### Cách 2: Tải lên qua đường dẫn URL

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/image/ad/upload/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "upload_type": "UPLOAD_BY_URL",
    "file_name": "san_pham_chinh.jpg",
    "image_url": "https://cdn.example.com/images/product_main.jpg"
  }'
```

#### Bảng tham số yêu cầu (Request Parameters)

| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
| :--- | :--- | :---: | :--- |
| `advertiser_id` | string | **Có** | ID tài khoản quảng cáo TikTok sở hữu ảnh. |
| `upload_type` | string | Không | Phương thức tải: `UPLOAD_BY_FILE` (mặc định) hoặc `UPLOAD_BY_URL`. |
| `file_name` | string | Không | Tên hiển thị của hình ảnh (tối đa 100 ký tự). |
| `image_file` | binary file | Điều kiện | Bắt buộc nếu chọn `upload_type=UPLOAD_BY_FILE`. |
| `image_url` | string | Điều kiện | Bắt buộc nếu chọn `upload_type=UPLOAD_BY_URL`. |
| `image_signature` | string | Không | Mã băm MD5 của ảnh để máy chủ đối soát toàn vẹn dữ liệu. |

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224900010245041042005I9J0K",
  "data": {
    "image_id": "tos-maliva-i-0068/1a2b3c4d5e6f7g8h9i0j",
    "size": 524288,
    "width": 1200,
    "height": 1200,
    "format": "png",
    "signature": "c4ca4238a0b923820dcc509a6f75849b",
    "image_url": "https://p16-va.tiktokcdn.com/obj/tos-maliva-i-0068/1a2b3c4d5e6f7g8h9i0j"
  }
}
```

---

### 3.2. Lấy thông tin chi tiết hình ảnh (`/file/image/ad/info/`)

Truy vấn thông số kỹ thuật của một hoặc nhiều hình ảnh dựa vào `image_ids`.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/image/ad/info/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/image/ad/info/?advertiser_id=7123456789012345678&image_ids=%5B%22tos-maliva-i-0068%2F1a2b3c4d5e6f7g8h9i0j%22%5D" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 3.3. Tìm kiếm hình ảnh trong thư viện (`/file/image/ad/search/`)

Tìm kiếm ảnh có hỗ trợ lọc theo ngày và phân trang.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/file/image/ad/search/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/file/image/ad/search/?advertiser_id=7123456789012345678&page=1&page_size=30" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 3.4. Chỉnh sửa và cắt ảnh thông minh (`/creative/image/edit/`)

Tự động cắt hoặc điều chỉnh kích thước ảnh để phù hợp với các vị trí đặt quảng cáo trên TikTok.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/image/edit/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/image/edit/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "image_id": "tos-maliva-i-0068/1a2b3c4d5e6f7g8h9i0j",
    "target_aspect_ratio": "9:16",
    "edit_type": "SMART_CROP"
  }'
```
