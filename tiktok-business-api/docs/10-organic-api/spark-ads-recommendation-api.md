<a id="1-gioi-thieu-spark-ads-recommendation-api"></a>
<a id="5-danh-muc-endpoint-spark-ads-recommendation-api"></a>
# Organic API — Spark Ads Recommendation API

> Phân hệ: Organic API > Spark Ads Recommendation API (Gợi ý quảng cáo Spark Ads).
> Spark Ads Recommendation API hỗ trợ các doanh nghiệp và đối tác TikTok One (TTO) nhận các gợi ý video tối ưu nhất để chạy Spark Ads, giúp nâng cao hiệu quả chiến dịch cho thương hiệu và nhà sáng tạo nội dung.

---

## Mục lục điều hướng
- [1. Giới thiệu Spark Ads Recommendation API](#1-gioi-thieu-spark-ads-recommendation-api)
- [2. Lợi ích khi sử dụng](#2-loi-ich-khi-su-dung)
- [3. Cơ chế hoạt động](#3-co-che-hoat-dong)
- [4. Giới hạn tần suất gọi API (Rate Limits)](#4-gioi-han-tan-suat-goi-api-rate-limits)
- [5. Danh mục Endpoint Spark Ads Recommendation API](#5-danh-muc-endpoint-spark-ads-recommendation-api)
- [6. Mã nguồn mẫu truy vấn gợi ý video (Python & cURL)](#6-ma-nguon-mau-truy-van-goi-y-video)

---

<a id="doc-1825128359356417"></a>
<!-- doc_id: 1825128359356417 -->
## 1. Giới thiệu Spark Ads Recommendation API

Spark Ads Recommendation API cung cấp các thuật toán gợi ý video dựa trên dữ liệu tương tác thực tế của các bài đăng hữu cơ (organic posts). Điều này giúp nhà quảng cáo xác định chính xác những video nào có tiềm năng viral và khả năng chuyển đổi cao nhất trước khi chi ngân sách quảng cáo.

Khám phá tài liệu:
- Bắt đầu
  - [Tổng quan](spark-ads-recommendation-api.md#doc-1825128393150530): Tìm hiểu quy trình làm việc chung và chức năng của API.
- Triển khai
  - [Giới hạn tốc độ](spark-ads-recommendation-api.md#doc-1825128519531521): Làm quen với các quy định về giới hạn gọi API.
  - [Tham chiếu API](spark-ads-recommendation-api.md#doc-1825128562548930): Tài liệu chi tiết các endpoint con.

---

<a id="doc-1825128393150530"></a>
<!-- doc_id: 1825128393150530 -->
<a id="2-loi-ich-khi-su-dung"></a>
## 2. Lợi ích khi sử dụng

Tích hợp với Spark Ads Recommendation API mang lại cơ hội:
- **Tận dụng tín hiệu dữ liệu độc quyền:** Dựa trên các tín hiệu tương tác thời gian thực từ thuật toán TikTok để chọn video phù hợp nhất.
- **Tối đa hóa mức độ tương tác:** Chọn đúng nội dung tự nhiên đã được cộng đồng đón nhận, giúp giảm chỉ số CPA và tăng tỷ lệ giữ chân người xem.
- **Tối ưu hóa quy trình làm việc:** Tự động hóa việc đề xuất và phê duyệt video cho các đối tác Agency và Creator Marketplace.

---

<a id="3-co-che-hoat-dong"></a>
## 3. Cơ chế hoạt động

Hệ thống hỗ trợ 2 luồng tích hợp chính:

1. **Dành cho Doanh nghiệp (Businesses):**
   - Sử dụng endpoint [/business/video/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128684907522) để gửi **TikTok account identifier** và danh sách `video_ids` cần đánh giá.
   - API trả về danh sách video được đề xuất, kèm mức độ đề xuất (`recommendation_level`) thể hiện độ phù hợp của bài đăng khi chạy Spark Ads và mã `item_id` dùng trực tiếp để tạo quảng cáo Spark Ad.

2. **Dành cho Đối tác TikTok One (TTO Partners):**
   - Sử dụng endpoint [/spark_ad/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128700959746) để gửi **TTO Creator Marketplace account ID** và danh sách `video_ids` cần đánh giá cùng mục tiêu chiến dịch (`objective_type`).
   - API trả về mức độ đề xuất, thông tin chi tiết và `item_id` sẵn sàng đưa vào luồng tạo chiến dịch.

---

<a id="doc-1825128519531521"></a>
<!-- doc_id: 1825128519531521 -->
<a id="4-gioi-han-tan-suat-goi-api-rate-limits"></a>
## 4. Giới hạn tần suất gọi API (Rate Limits)

Các endpoint thuộc Spark Ads Recommendation API áp dụng chính sách giới hạn tốc độ chung của nền tảng (Global rate limits).
Chi tiết về giới hạn toàn cục theo từng cấp ứng dụng xem tại [Giới hạn tốc độ toàn cục](../04-get-started/bat-dau.md#doc-1740029171730433).

---

<a id="doc-1825128562548930"></a>
<!-- doc_id: 1825128562548930 -->
## 5. Danh mục Endpoint Spark Ads Recommendation API

Toàn bộ các endpoint được đặc tả chi tiết tại [Tài liệu API Reference — Gợi ý Spark Ads](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128584099841):

- [Lấy gợi ý video Spark Ads cho tài khoản TikTok (`GET /open_api/v1.3/business/video/recommend/`)](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128684907522)
- [Lấy gợi ý video Spark Ads cho tài khoản TikTok One (`POST /open_api/v1.3/spark_ad/recommend/`)](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128700959746)
- [Tạo nhanh chiến dịch, nhóm quảng cáo và Spark Ad trong một bước (`POST /open_api/v1.3/spark_ad/create/`)](../12-api-reference/63-spark-ads-recommendation.md#doc-1829744071179330)

---

<a id="6-ma-nguon-mau-truy-van-goi-y-video"></a>
## 6. Mã nguồn mẫu truy vấn gợi ý video (Python & cURL)

### cURL lấy gợi ý video cho tài khoản TikTok doanh nghiệp
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/business/video/recommend/?business_id=YOUR_BUSINESS_ID&tiktok_account_id=YOUR_TT_ACCOUNT_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script trích xuất danh sách video được gợi ý
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {"Access-Token": ACCESS_TOKEN}

def get_spark_ad_recommendations(business_id, tt_account_id):
    """Truy vấn các video được gợi ý chạy Spark Ads."""
    url = f"{BASE_URL}/business/video/recommend/"
    params = {
        "business_id": business_id,
        "tiktok_account_id": tt_account_id
    }
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        videos = res.get("data", {}).get("list", [])
        print(f"Có {len(videos)} video được đề xuất:")
        for v in videos:
            print(f" - Item ID: {v.get('item_id')} | Level: {v.get('recommendation_level')} | Title: {v.get('title')}")
        return videos
    else:
        print(f"Lỗi: {res.get('code')} - {res.get('message')}")
        return []

if __name__ == "__main__":
    get_spark_ad_recommendations("YOUR_BUSINESS_ID", "YOUR_TT_ACCOUNT_ID")
```

