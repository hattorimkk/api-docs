# Tham Khảo API: Media Space - Quản Lý Hình Ảnh & Video (Media Space APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** trong phân hệ **Media Space** của Shopee Open API v2, dùng để upload hình ảnh và video sản phẩm.

---

## 1. Tải Lên Hình Ảnh Sản Phẩm (Upload Image)

- **Tên Endpoint**: `v2.media_space.upload_image`
- **Đường dẫn**: `POST /api/v2/media_space/upload_image`
- **Định dạng dữ liệu**: `multipart/form-data`

### Tham số Form-data:
- `image`: File ảnh nhị phân (JPG, PNG, tối đa 10MB).
- `scene`: `normal` (ảnh vuông 1:1 cho đại diện sản phẩm) hoặc `desc` (ảnh mô tả chi tiết).

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/media_space/upload_image?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -F "image=@/path/to/product_image.jpg" \
  -F "scene=normal"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "76ba370b77c38587...",
  "response": {
    "image_info": {
      "image_id": "vn-11134207-7r98o-lst123456789ab",
      "image_url_list": [
        {
          "image_url_region": "VN",
          "image_url": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lst123456789ab"
        }
      ]
    }
  }
}
```

---

## 2. Quy Trình Tải Lên Video Đa Phân Đoạn (Chunk Video Upload)

### Bước 1: Khởi tạo phiên tải video (`init_video_upload`)
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/media_space/init_video_upload?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "file_size": 15728640,
    "file_md5": "9e107d9d372bb6826bd81d3542a419d6"
  }'
```
*(Lưu lại `video_upload_id` nhận được).*

---

### Bước 2: Tải lên từng mảnh video không quá 4MB (`upload_video_part`)
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/media_space/upload_video_part?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -F "video_upload_id=video_session_abc123" \
  -F "part_seq=0" \
  -F "content=@/path/to/video_part_0.mp4"
```

---

### Bước 3: Xác nhận hoàn tất ghép video (`complete_video_upload`)
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/media_space/complete_video_upload?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "video_upload_id": "video_session_abc123",
    "part_seq_list": [0, 1, 2, 3],
    "report_data": {}
  }'
```

---

### Bước 4: Kiểm tra trạng thái xử lý video (`get_video_upload_result`)
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/media_space/get_video_upload_result?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "video_upload_id": "video_session_abc123"
  }'
```
