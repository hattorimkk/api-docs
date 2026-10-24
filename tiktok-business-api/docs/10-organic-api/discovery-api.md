# Organic API — Discovery API

> Phân hệ: Organic API > Discovery API (Khám phá xu hướng).
> Discovery API cho phép bạn khám phá các hashtag phổ biến nhất trên TikTok để định hướng sáng tạo nội dung, đồng thời tìm kiếm các bản nhạc thịnh hành từ Thư viện Âm nhạc Thương mại (Commercial Music Library - CML) phục vụ cả nội dung tự nhiên và tạo quảng cáo.

---

## Mục lục điều hướng
- [1. Giới thiệu tổng quan Discovery API](#1-gioi-thieu-tong-quan-discovery-api)
- [2. Quy trình tích hợp từng bước](#2-quy-trinh-tich-hop-tung-buoc)
- [3. Giới hạn tần suất gọi API (Rate Limits)](#3-gioi-han-tan-suat-goi-api-rate-limits)
- [4. Danh mục Endpoint Discovery API](#4-danh-muc-endpoint-discovery-api)
- [5. Mã nguồn mẫu trích xuất xu hướng (Python & cURL)](#5-ma-nguon-mau-trich-xuat-xu-huong)

---

<a id="doc-1825127388184577"></a>
<!-- doc_id: 1825127388184577 -->
<a id="1-gioi-thieu-tong-quan-discovery-api"></a>
## 1. Giới thiệu tổng quan Discovery API

Discovery API là công cụ cung cấp danh sách các hashtag và bản nhạc thịnh hành nhất trên TikTok trong một khoảng thời gian cụ thể (theo ngày, tuần hoặc tháng). Công cụ này giúp các nhà quảng cáo nắm bắt thị hiếu người dùng, lập kế hoạch chiến dịch, thiết kế sản phẩm và tối ưu hóa nội dung quảng cáo.

Cùng với danh sách thịnh hành, API trả về các chỉ số phân tích chuyên sâu cho từng hashtag hoặc bài hát như:
- Tỷ lệ tăng trưởng lượt xem.
- Phân khúc độ tuổi và giới tính của khán giả quan tâm.
- Danh sách các video xu hướng đang sử dụng hashtag hoặc bản nhạc đó.

---

<a id="doc-1825127469285442"></a>
<!-- doc_id: 1825127469285442 -->
<a id="2-quy-trinh-tich-hop-tung-buoc"></a>
## 2. Quy trình tích hợp từng bước

Để thực hiện cuộc gọi API đầu tiên, bạn cần hoàn thành các bước thiết lập cơ bản:

1. **Tạo tài khoản TikTok For Business:** Chi tiết tại [Tạo tài khoản](../04-get-started/bat-dau.md#doc-1738855099573250).
2. **Đăng ký tài khoản Nhà phát triển:** Chi tiết tại [Đăng ký nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. **Tạo ứng dụng nhà phát triển (Developer App):** Chi tiết tại [Tạo ứng dụng](../04-get-started/bat-dau.md#doc-1738855242728450).
4. **Xác thực và Ủy quyền (Authorization & Authentication):**
   - *Đối với các endpoint liên quan đến Hashtag* ([/discovery/trending_list/](../12-api-reference/40-discovery.md#doc-1825119032526849), [/discovery/detail/](../12-api-reference/40-discovery.md#doc-1825119047070721), và [/discovery/video_list/](../12-api-reference/40-discovery.md#doc-1825119056527362)): Yêu cầu ủy quyền từ tài khoản quảng cáo. Xem [Lấy ủy quyền từ tài khoản quảng cáo](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378) và [Tạo access token nhà quảng cáo](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
   - *Đối với các endpoint liên quan đến Bản nhạc CML* ([/discovery/cml/trending_list/](../12-api-reference/40-discovery.md#doc-1825119063013505) và [/discovery/cml/video_list/](../12-api-reference/40-discovery.md#doc-1825119068941314)): Yêu cầu ủy quyền từ tài khoản người dùng TikTok. Xem [Lấy ủy quyền tài khoản TikTok](accounts-api.md#doc-1738083939371009) và [Tạo TikTok user access token](accounts-api.md#doc-1738084387220481).
5. **Thực hiện lệnh gọi API trích xuất dữ liệu.**

---

<a id="doc-1825127824570434"></a>
<!-- doc_id: 1825127824570434 -->
<a id="3-gioi-han-tan-suat-goi-api-rate-limits"></a>
## 3. Giới hạn tần suất gọi API (Rate Limits)

Giới hạn tốc độ cho mỗi endpoint thuộc Discovery API là **10 truy vấn mỗi giây (10 QPS)** tính trên mỗi ứng dụng nhà phát triển (Developer App).

---

<a id="doc-1825127842289729"></a>
<!-- doc_id: 1825127842289729 -->
<a id="4-danh-muc-endpoint-discovery-api"></a>
## 4. Danh mục Endpoint Discovery API

Tất cả các endpoint Discovery API được đặc tả chi tiết tại [Tài liệu API Reference — Khám phá (Discovery)](../12-api-reference/40-discovery.md#doc-1825119005427714):

- [Lấy danh sách Hashtag thịnh hành (`GET /open_api/v1.3/discovery/trending_list/`)](../12-api-reference/40-discovery.md#doc-1825119032526849)
- [Lấy chi tiết và chỉ số của Hashtag (`GET /open_api/v1.3/discovery/detail/`)](../12-api-reference/40-discovery.md#doc-1825119047070721)
- [Lấy danh sách video thịnh hành theo Hashtag (`GET /open_api/v1.3/discovery/video_list/`)](../12-api-reference/40-discovery.md#doc-1825119056527362)
- [Lấy danh sách bản nhạc thương mại thịnh hành (`GET /open_api/v1.3/discovery/cml/trending_list/`)](../12-api-reference/40-discovery.md#doc-1825119063013505)
- [Lấy danh sách video thịnh hành theo bản nhạc (`GET /open_api/v1.3/discovery/cml/video_list/`)](../12-api-reference/40-discovery.md#doc-1825119068941314)
- [Lấy từ khóa tìm kiếm thịnh hành (`GET /open_api/v1.3/discovery/search/trending_list/`)](../12-api-reference/40-discovery.md#doc-1832798345014338)
- [Lấy từ khóa tìm kiếm được gợi ý (`GET /open_api/v1.3/discovery/search/recommend_list/`)](../12-api-reference/40-discovery.md#doc-1832798361818114)

---

<a id="5-ma-nguon-mau-trich-xuat-xu-huong"></a>
## 5. Mã nguồn mẫu trích xuất xu hướng (Python & cURL)

### cURL trích xuất top hashtag thịnh hành tại Việt Nam
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/discovery/trending_list/?advertiser_id=YOUR_ADVERTISER_ID&country_code=VN&page=1&page_size=20" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script trích xuất Hashtag và Video thịnh hành
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {"Access-Token": ACCESS_TOKEN}

def get_trending_hashtags(country_code="VN", page=1, page_size=20):
    """Trích xuất danh sách hashtag thịnh hành theo quốc gia."""
    url = f"{BASE_URL}/discovery/trending_list/"
    params = {
        "advertiser_id": advertiser_id,
        "country_code": country_code,
        "page": page,
        "page_size": page_size
    }
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        hashtags = res.get("data", {}).get("list", [])
        print(f"Top {len(hashtags)} Hashtags tại {country_code}:")
        for tag in hashtags:
            print(f" - #{tag.get('hashtag_name')} | Rank: {tag.get('rank')} | Lượt xem: {tag.get('video_views')}")
        return hashtags
    else:
        print(f"Lỗi: {res.get('code')} - {res.get('message')}")
        return []

if __name__ == "__main__":
    get_trending_hashtags("VN")
```

