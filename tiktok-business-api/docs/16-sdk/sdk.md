# Bộ công cụ phát triển phần mềm (SDK) — API for Business SDK

> Phân hệ: Hướng dẫn chung > Bộ công cụ phát triển phần mềm (SDK).
> **Truy cập trang [Kho lưu trữ chính thức API for Business SDK trên GitHub](https://github.com/tiktok/tiktok-business-api-sdk) để lấy mã nguồn và hướng dẫn cài đặt trong [README.md](https://github.com/tiktok/tiktok-business-api-sdk/blob/main/README.md).**

---

## Mục lục điều hướng
- [1. Giới thiệu API for Business SDK](#1-gioi-thieu-api-for-business-sdk)
- [2. Lợi ích khi sử dụng SDK](#2-loi-ich-khi-su-dung-sdk)
- [3. Thời gian tích hợp ước tính](#3-thoi-gian-tich-hop-uoc-tinh)
- [4. Ngôn ngữ lập trình hỗ trợ](#4-ngon-ngu-lap-trinh-ho-tro)
- [5. Các nhóm Endpoint hỗ trợ trong SDK](#5-cac-nhom-endpoint-ho-tro-trong-sdk)
- [6. Hướng dẫn cài đặt và sử dụng nhanh bằng Python](#6-huong-dan-cai-dat-va-su-dung-nhanh-bang-python)

---

<a id="doc-1764231376750658"></a>
<!-- doc_id: 1764231376750658 -->
<a id="1-gioi-thieu-api-for-business-sdk"></a>
## 1. Giới thiệu API for Business SDK

**API for Business SDK** cung cấp bộ sưu tập toàn diện các thư viện client mã nguồn mở giúp các nhà phát triển xây dựng phần mềm tích hợp với TikTok Business API nhanh hơn, chuẩn hóa hơn và ít lỗi hơn so với việc tự viết client HTTP thô.

---

<a id="2-loi-ich-khi-su-dung-sdk"></a>
## 2. Lợi ích khi sử dụng SDK

- **Tích hợp nhanh hơn và mượt mà hơn:** SDK chuẩn hóa toàn bộ quy trình gửi yêu cầu, xử lý xác thực token, mã hóa payload JSON và giải mã kết quả phản hồi, giúp giảm đáng kể thời gian đưa ứng dụng vào hoạt động thực tế.
- **Rút ngắn chu kỳ phát triển phần mềm:** SDK được thiết kế để cung cấp đầy đủ các phương thức tiện ích, lớp đối tượng (data models) có gợi ý cú pháp (type hints/autocomplete), giúp lập trình viên tập trung vào logic sản phẩm thay vì các chi tiết kỹ thuật tầng mạng.
- **Bảo trì mã nguồn dễ dàng hơn:** Cung cấp sẵn các thành phần, hàm và thư viện có thể tái sử dụng trên nhiều dự án khác nhau. Khi TikTok phát hành bản cập nhật API mới, việc cập nhật phiên bản SDK sẽ tự động tương thích mà không làm gián đoạn mã nguồn hiện có.

---

<a id="3-thoi-gian-tich-hop-uoc-tinh"></a>
## 3. Thời gian tích hợp ước tính

Dựa trên dữ liệu khảo sát thực tế và phỏng vấn các đối tác tích hợp, thời gian hoàn thành tích hợp khi sử dụng SDK giảm trung bình khoảng **40%** so với việc tự xây dựng client gọi trực tiếp API thông thường:

| Use case | Thời gian tích hợp bằng SDK | Thời gian tích hợp API thủ công |
|---|---|---|
| **Reporting (Báo cáo)** | **32 giờ** | **45 giờ** |

> **Lưu ý:** Kết quả trên mang tính chất tham khảo. Thời gian thực tế có thể thay đổi tùy thuộc vào kinh nghiệm của lập trình viên và mức độ phức tạp của hệ thống nội bộ.

---

<a id="4-ngon-ngu-lap-trinh-ho-tro"></a>
## 4. Ngôn ngữ lập trình hỗ trợ

SDK chính thức của TikTok Business API hiện hỗ trợ 3 ngôn ngữ lập trình phổ biến:
- **Python** (Yêu cầu Python >= 3.7)
- **JavaScript / TypeScript** (Node.js & Trình duyệt)
- **Java** (JDK >= 8)

---

<a id="5-cac-nhom-endpoint-ho-tro-trong-sdk"></a>
## 5. Các nhóm Endpoint hỗ trợ trong SDK

Bộ SDK cung cấp sẵn các client class bao phủ toàn diện các phân hệ chính của TikTok Business API:

### Xác thực & Tài khoản (Authentication)
- `/v1.3/oauth2/access_token/` (Cấp access token)
- `/v1.3/oauth2/advertiser/get/` (Danh sách tài khoản quảng cáo được ủy quyền)

### Quản lý Chiến dịch (Campaign Management)
- `/v1.3/campaign/create/` (Tạo chiến dịch)
- `/v1.3/campaign/get/` (Lấy danh sách chiến dịch)
- `/v1.3/campaign/update/` (Cập nhật chiến dịch)
- `/v1.3/campaign/status/update/` (Cập nhật trạng thái chiến dịch)

### Quản lý Nhóm quảng cáo (Ad Group Management)
- `/v1.3/adgroup/create/` (Tạo nhóm quảng cáo)
- `/v1.3/adgroup/get/` (Lấy thông tin nhóm quảng cáo)
- `/v1.3/adgroup/update/` (Cập nhật nhóm quảng cáo)
- `/v1.3/adgroup/status/update/` (Cập nhật trạng thái)
- `/v1.3/adgroup/quota/` (Kiểm tra hạn ngạch nhóm quảng cáo)

### Quản lý Quảng cáo (Ad Management & ACO)
- `/v1.3/ad/create/`, `/v1.3/ad/get/`, `/v1.3/ad/update/`, `/v1.3/ad/status/update/`
- Tối ưu hóa nội dung tự động (ACO): `/v1.3/ad/aco/create/`, `/get/`, `/update/`, `/material_status/update/`

### Báo cáo số liệu (Reporting)
- `/v1.3/report/integrated/get/` (Báo cáo tích hợp đồng bộ đa chiều dữ liệu)

### Trung tâm doanh nghiệp & Thanh toán (Business Center & Payment)
- `/v1.3/bc/get/`, `/v1.3/bc/image/upload/`, `/v1.3/bc/advertiser/create/`, `/v1.3/bc/asset/get/`
- `/v1.3/bc/transfer/`, `/v1.3/advertiser/balance/get/`, `/v1.3/bc/balance/get/`, `/v1.3/bc/transaction/get/`

### Quản lý Tệp & Thư viện nội dung (Files & Creatives)
- Upload và tra cứu video: `/v1.3/file/video/ad/upload/`, `/info/`, `/search/`
- Upload và tra cứu hình ảnh: `/v1.3/file/image/ad/upload/`, `/info/`
- Danh mục creative: `/v1.3/creative/portfolio/create/`

### Định danh (Identity) & Công cụ nhắm mục tiêu (Tools)
- Định danh tài khoản: `/v1.3/identity/create/`, `/get/`, `/video/get/`
- Công cụ nhắm mục tiêu: `/v1.3/tool/targeting/search/`, `/info/`, `/tool/region/`, `/tool/interest_category/`, `/tool/interest_keyword/recommend/`, `/tool/hashtag/recommend/`, `/tool/language/`, `/tool/device_model/`, `/tool/timezone/`, `/tool/bid/recommend/`

### Quản lý Đối tượng (Audience DMP)
- Upload file & tạo tệp: `/v1.3/dmp/custom_audience/file/upload/`, `/create/`, `/rule/create/`, `/lookalike/create/`
- Quản lý tệp: `/v1.3/dmp/custom_audience/list/`, `/get/`, `/delete/`, `/share/`, `/apply/`
- Đối tượng đã lưu: `/v1.3/dmp/saved_audience/create/`, `/list/`, `/delete/`

### Quản lý Ứng dụng & Sự kiện (App & Pixel Events)
- `/v1.3/app/list/`, `/v1.3/app/optimization_event/`
- `/v1.3/pixel/track/`, `/v1.3/pixel/batch/`

---

<a id="6-huong-dan-cai-dat-va-su-dung-nhanh-bang-python"></a>
## 6. Hướng dẫn cài đặt và sử dụng nhanh bằng Python

### Cài đặt qua pip
```bash
pip install tiktok-business-api-sdk
```

### Mã nguồn mẫu khởi tạo client và trích xuất dữ liệu
```python
from business_api_client import ApiClient, Configuration
from business_api_client.api import CampaignApi, ReportApi

# Cấu hình Access Token
config = Configuration()
config.access_token = "YOUR_ACCESS_TOKEN"

# Khởi tạo API client
client = ApiClient(configuration=config)

# 1. Lấy danh sách chiến dịch
campaign_api = CampaignApi(client)
campaigns = campaign_api.campaign_get(
    advertiser_id="YOUR_ADVERTISER_ID",
    page=1,
    page_size=20
)
print("Danh sách chiến dịch:", campaigns)

# 2. Truy vấn báo cáo tích hợp
report_api = ReportApi(client)
report_data = report_api.report_integrated_get(
    advertiser_id="YOUR_ADVERTISER_ID",
    report_type="BASIC",
    data_level="AUCTION_CAMPAIGN",
    dimensions='["stat_time_day", "campaign_id"]',
    metrics='["spend", "impressions", "clicks", "ctr", "cpc"]',
    start_date="2026-03-01",
    end_date="2026-03-07",
    page=1,
    page_size=100
)
print("Kết quả báo cáo:", report_data)
```

