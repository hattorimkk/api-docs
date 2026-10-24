# Creative Reports & Fatigue API — Đo Lường Hiệu Suất & Độ Bão Hòa Sáng Tạo

> **Phân hệ**: Creative API > Creative Performance & Fatigue Analytics  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Trên TikTok, vòng đời hiệu quả của một video quảng cáo thường kéo dài từ 7 đến 14 ngày trước khi đối tượng khán giả bị "nhờn quảng cáo" (Ad Fatigue), dẫn đến CTR giảm mạnh và CPA tăng cao. 

Phân hệ Creative Reports & Fatigue API cung cấp cho bạn 2 công cụ quan trọng bậc nhất:
1. **Phân tích giữ chân người xem (Video Retention Analytics)**: Đo lường chi tiết tỷ lệ người dùng bỏ qua video sau 2 giây đầu tiên (2s Drop-off Rate), sau 6 giây, và tỷ lệ xem trọn vẹn 100% video.
2. **Phát hiện sớm độ mệt mỏi sáng tạo (Creative Fatigue Detection)**: Thuật toán AI của TikTok tự động gắn nhãn các video đang có dấu hiệu suy giảm hiệu suất (`FATIGUE`, `POTENTIAL_FATIGUE`, `HEALTHY`) để bạn có kế hoạch thay mới tài nguyên trước khi lãng phí ngân sách.

---

## 📊 2. Các chỉ số đo lường hiệu suất Video quan trọng

| Chỉ số (Metric Code) | Tên chỉ số tiếng Việt | Ý nghĩa phân tích dữ liệu |
| :--- | :--- | :--- |
| `video_play_actions` | Tổng số lượt phát video | Số lần video bắt đầu phát trên màn hình người dùng. |
| `video_watched_2s` | Lượt xem tối thiểu 2 giây | Thước đo mức độ hấp dẫn của 2 giây mở đầu ("Hook" video). |
| `video_watched_6s` | Lượt xem tối thiểu 6 giây | Thước đo khả năng giữ chân người xem sau phần mở đầu. |
| `video_views_p25` | Lượt xem đạt 25% thời lượng | Tỷ lệ người dùng tiếp tục xem đến 1/4 video. |
| `video_views_p50` | Lượt xem đạt 50% thời lượng | Tỷ lệ người dùng xem qua nửa video. |
| `video_views_p75` | Lượt xem đạt 75% thời lượng | Khán giả có mức độ quan tâm cao đến thông điệp sản phẩm. |
| `video_views_p100` | Lượt xem hết toàn bộ 100% | Khán giả xem trọn vẹn thông điệp quảng cáo. |
| `average_video_play` | Thời lượng xem trung bình | Thời gian bình quân (giây) mỗi lượt xem. |
| `average_video_play_per_user`| Thời gian xem bình quân/người | Tổng thời gian xem chia cho số người tiếp cận duy nhất. |

---

## 🚀 3. Danh sách Endpoints & Hướng dẫn cURL

### 3.1. Báo cáo phân tích hiệu suất nội dung sáng tạo (`/creative/report/get/`)

Endpoint chuyên dụng để trích xuất dữ liệu phân tích từng giây của video quảng cáo.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/creative/report/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/report/get/?advertiser_id=7123456789012345678&start_date=2026-10-01&end_date=2026-10-23&page=1&page_size=20&metrics=%5B%22video_watched_2s%22%2C%22video_watched_6s%22%2C%22video_views_p100%22%2C%22average_video_play%22%5D" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225020010245041042005W9X0Y",
  "data": {
    "list": [
      {
        "material_id": "v10033g50000cf7m1g3c77u3g2example",
        "material_name": "quang_cao_tet_2026.mp4",
        "metrics": {
          "video_watched_2s": "125400",
          "video_watched_6s": "84300",
          "video_views_p100": "32100",
          "average_video_play": "8.75"
        }
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 20,
      "total_number": 45,
      "total_page": 3
    }
  }
}
```

---

### 3.2. Báo cáo độ bão hòa / suy giảm sáng tạo — Creative Fatigue (`/creative_fatigue/get/`)

API này quét toàn bộ các video đang phân phối và cảnh báo các video đã bắt đầu có dấu hiệu bão hòa.

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/?advertiser_id=7123456789012345678&page=1&page_size=20" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

#### Ý nghĩa trạng thái bão hòa (`fatigue_status`):
- `HEALTHY`: Video đang phân phối tốt, tỷ lệ giữ chân và chuyển đổi ổn định.
- `POTENTIAL_FATIGUE`: Có dấu hiệu suy giảm trong 3 ngày gần nhất. Cần chuẩn bị video thay thế.
- `FATIGUE`: Video đã bão hòa nghiêm trọng. Khuyến nghị tạm dừng hoặc thay thế ngay lập tức.

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225030010245041042005Z1A2B",
  "data": {
    "list": [
      {
        "material_id": "v10033g50000cf7m1g3c77u3g2example",
        "ad_id": "1782345678901234",
        "fatigue_status": "POTENTIAL_FATIGUE",
        "fatigue_metric_trends": {
          "ctr_trend": "-18.5%",
          "cpa_trend": "+24.2%"
        },
        "recommendation": "Thay thế bằng video mới có mở đầu khác biệt hoặc điều chỉnh tệp đối tượng."
      }
    ]
  }
}
```

---

### 3.3. Trích xuất chỉ số giữ chân người xem video theo phân cấp chiến dịch (`/report/integrated/get/`)

Bạn cũng có thể kết hợp các chỉ số Video Retention vào báo cáo hiệu suất tổng hợp cùng các chỉ số doanh thu (Spend, Impressions, Clicks, Conversions, ROAS):

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/?advertiser_id=7123456789012345678&service_type=AUCTION&report_type=BASIC&data_level=AUCTION_AD&dimensions=%5B%22ad_id%22%2C%22stat_time_day%22%5D&metrics=%5B%22spend%22%2C%22impressions%22%2C%22clicks%22%2C%22video_watched_2s%22%2C%22video_watched_6s%22%2C%22video_views_p100%22%5D&start_date=2026-10-15&end_date=2026-10-23&page=1&page_size=50" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```
