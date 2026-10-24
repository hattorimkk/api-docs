# Creative Pre-review API — Tiền Kiểm Duyệt Nội Dung Sáng Tạo

> **Phân hệ**: Creative API > Pre-review & Ad Compliance  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Thông thường, khi bạn tạo mẫu quảng cáo trên TikTok Ads Manager, hệ thống mới tiến hành xét duyệt (Ad Review). Nếu video hoặc nội dung vi phạm chính sách (chứa từ cấm, bản quyền, nội dung nhạy cảm), quảng cáo sẽ bị từ chối (`DISAPPROVED`), gây gián đoạn kế hoạch marketing.

**Creative Pre-review API** cho phép bạn:
- Gửi tài nguyên sáng tạo (video, hình ảnh, văn bản quảng cáo, URL trang đích) đi kiểm duyệt trước **ngay từ khâu sản xuất nội dung**, trước khi đưa vào bất kỳ chiến dịch hay nhóm quảng cáo nào.
- Nhận kết quả đánh giá tuân thủ chính sách quảng cáo chỉ sau vài phút.
- Giúp chiến dịch khi khởi chạy sẽ được duyệt ngay lập tức, tiết kiệm tối đa thời gian triển khai.

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Khởi tạo tác vụ tiền kiểm duyệt (`/creative/pre_review/task/create/`)

Gửi thông tin video, văn bản quảng cáo và link đích đến đội ngũ xét duyệt tự động của TikTok.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "ad_text": "Trải nghiệm phong cách thời trang dẫn đầu xu hướng Tết 2026!",
    "landing_page_url": "https://example.com/landing_page_tet",
    "location_codes": ["VN", "TH"],
    "is_ecommerce": true
  }'
```

#### Bảng tham số yêu cầu (Request Parameters)

| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
| :--- | :--- | :---: | :--- |
| `advertiser_id` | string | **Có** | ID tài khoản quảng cáo. |
| `video_id` | string | **Có** | ID của video đã tải lên thư viện cần tiền kiểm duyệt. |
| `ad_text` | string | **Có** | Văn bản quảng cáo đi kèm video (tối đa 100 ký tự). |
| `landing_page_url`| string | Không | Đường dẫn URL của trang đích chuyển đổi. |
| `location_codes` | string[] | **Có** | Danh sách mã quốc gia mục tiêu (ví dụ `["VN"]`). |
| `is_ecommerce` | boolean | Không | Đánh dấu nếu quảng cáo phục vụ thương mại điện tử (TikTok Shop). |

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225040010245041042005C3D4E",
  "data": {
    "pre_review_task_id": "pr_task_987654321012345"
  }
}
```

---

### 2.2. Lấy kết quả tiền kiểm duyệt (`/creative/pre_review/task/get/`)

Tra cứu trạng thái và kết quả chi tiết của tác vụ tiền duyệt.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/get/?advertiser_id=7123456789012345678&pre_review_task_ids=%5B%22pr_task_987654321012345%22%5D" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

#### Các trạng thái xét duyệt (`pre_review_status`):
- `UNDER_REVIEW`: Đang trong tiến trình kiểm duyệt.
- `PASSED`: Đã thông qua kiểm duyệt thành công, sẵn sàng đưa vào quảng cáo.
- `FAILED`: Bị từ chối kiểm duyệt (kèm lý do chi tiết trong `reject_reasons`).

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225050010245041042005F5G6H",
  "data": {
    "list": [
      {
        "pre_review_task_id": "pr_task_987654321012345",
        "pre_review_status": "PASSED",
        "create_time": "2026-10-23 21:30:00",
        "reject_reasons": []
      }
    ]
  }
}
```
