# Gợi ý Spark Ads (Spark Ads Recommendation)

Tài liệu này cung cấp hướng dẫn và đặc tả kỹ thuật cho nhóm API Gợi ý Spark Ads (Spark Ads Recommendation API) của TikTok for Business.

Spark Ads Recommendation API giúp bạn phát hiện những video có tiềm năng thương mại cao nhất từ tài khoản TikTok hoặc tài khoản TikTok One (TTO) Creator Marketplace, đồng thời cung cấp giải pháp khởi tạo trọn gói một bước (All-in-One) bao gồm Chiến dịch, Nhóm quảng cáo và Mẫu quảng cáo Spark Ad.

## Danh sách endpoint trong tài liệu

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/open_api/v1.3/business/video/recommend/` | Lấy gợi ý video phù hợp làm Spark Ads từ tài khoản TikTok cá nhân / doanh nghiệp |
| `GET` | `/open_api/v1.3/spark_ad/recommend/` | Lấy gợi ý video phù hợp làm Spark Ads từ tài khoản TTO Creator Marketplace |
| `POST` | `/open_api/v1.3/business/spark_ad/create/` | Khởi tạo đồng thời Chiến dịch, Nhóm quảng cáo và Spark Ad trong một yêu cầu duy nhất |

---

## Tổng quan về Gợi ý Spark Ads (Spark Ads Recommendation Overview)
<a id="doc-1825128584099841"></a>
<!-- doc_id: 1825128584099841 -->

Tính năng Gợi ý Spark Ads (Spark Ads Recommendation) ứng dụng mô hình học máy thông minh nhằm đánh giá và phân loại các video tự nhiên (organic videos) có xác suất chuyển đổi hoặc tương tác cao nhất để chạy quảng cáo Spark Ads.

Mô hình phân tích video dựa trên:
- **Tương tác của người xem**: Lượt thích, bình luận, chia sẻ, thời lượng xem trung bình và tỷ lệ xem hết.
- **Thuộc tính nội dung**: Thể loại video, phong cách âm thanh, thời lượng và định dạng khung hình.
- **Dữ liệu đối sánh lịch sử**: So sánh hiệu suất của video với các video cùng danh mục ngành hàng trên TikTok.

Mỗi video được gán điểm số gợi ý và xếp loại mức độ đề xuất (`recommendation_level`): `HIGH`, `MEDIUM`, hoặc `LOW`.

Các tài liệu liên kết trong nhóm:
* [Lấy gợi ý video Spark Ads cho tài khoản TikTok](63-spark-ads-recommendation.md#doc-1825128684907522)
* [Lấy gợi ý video Spark Ads cho tài khoản TTO](63-spark-ads-recommendation.md#doc-1825128700959746)
* [Tạo chiến dịch, nhóm quảng cáo và Spark Ad trong một bước](63-spark-ads-recommendation.md#doc-1829744071179330)
* [Cài đặt mặc định cho All-in-One Spark Ads](63-spark-ads-recommendation.md#doc-1829744101665810)

---

## Lấy gợi ý video Spark Ads cho tài khoản TikTok (Get Spark Ads video recommendations for a TikTok account)
<a id="doc-1825128684907522"></a>
<!-- doc_id: 1825128684907522 -->

Sử dụng endpoint này để lấy kết quả gợi ý video Spark Ads cho tối đa **20 bài đăng video** thuộc tài khoản TikTok của bạn.

Kết quả đề xuất được tạo bằng cách so sánh các bài đăng video với tiêu chuẩn đánh giá kết hợp dữ liệu tương tác của khán giả, sở thích, thuộc tính bài đăng (thể loại, độ dài) và hiệu suất lịch sử. Video có điểm số cao hơn biểu thị khả năng thành công quảng cáo lớn hơn và nhận mức độ gợi ý cao hơn.

> **Khuyến nghị:**
> Để đảm bảo độ chính xác của kết quả phân tích, tài khoản TikTok nên có ít nhất 20 video đã đăng. Nếu tài khoản có hơn 20 video, hệ thống sẽ lọc và trả về tối đa 20 video có tiềm năng Spark Ads cao nhất.

### Điều kiện tiên quyết
- Đảm bảo tài khoản TikTok là tài khoản có Quyền truy cập nâng cao (Advanced Access) hoặc Tài khoản doanh nghiệp đã xác minh (Verified Business Account). Xem [quyền lợi tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Có thể xác nhận qua endpoint [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra trường `has_advanced_access` có giá trị `true`.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/business/video/recommend/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã Access token được ủy quyền bởi tài khoản TikTok. Để lấy token, xem [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/mentions-api-authentication/v1.3#anchor-1). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `business_id` **(Bắt buộc)** | string | Mã định danh duy nhất của tài khoản TikTok doanh nghiệp. |
| `video_ids` | string[] | Danh sách ID các video cụ thể muốn đưa vào phân tích gợi ý. Bỏ trống nếu muốn phân tích toàn bộ video. |
| `exclude_video_ids` | string[] | Danh sách ID các video muốn loại trừ khỏi phân tích gợi ý. |
| `time` | string | Khoảng thời gian video được đăng tải. Enum: `LAST_7_DAYS`, `LAST_14_DAYS`, `LAST_30_DAYS`, `LAST_90_DAYS`, `ALL_TIME`. |
| `objective_type` | string | Mục tiêu quảng cáo dự kiến áp dụng. Enum: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/business/video/recommend/?business_id=7123456789012345678&time=LAST_30_DAYS&objective_type=TRAFFIC' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BUSINESS_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/business/video/recommend/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "business_id": BUSINESS_ID,
    "time": "LAST_30_DAYS",
    "objective_type": "TRAFFIC"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ videos` | object[] | Danh sách tối đa 20 video TikTok kèm kết quả gợi ý Spark Ads. |
| `↳↳ item_id` | string | ID của video TikTok. |
| `↳↳ title` | string | Tiêu đề hoặc mô tả bài đăng của video. |
| `↳↳ video_cover_url` | string | Đường dẫn ảnh bìa (cover) của video. |
| `↳↳ video_duration` | number | Thời lượng của video (giây). |
| `↳↳ create_time` | string | Thời điểm đăng tải video. |
| `↳↳ recommendation_level` | string | Mức độ phù hợp gợi ý Spark Ads: `HIGH` (Rất phù hợp), `MEDIUM` (Phù hợp), `LOW` (Ít phù hợp). |
| `↳↳ recommendation_reason` | string | Lý do gợi ý chi tiết dựa trên dữ liệu đối sánh. |
| `↳↳ view_count` | number | Tổng số lượt xem tự nhiên của video. |
| `↳↳ like_count` | number | Lượt thích video. |
| `↳↳ comment_count` | number | Lượt bình luận video. |
| `↳↳ share_count` | number | Lượt chia sẻ video. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "videos": [
      {
        "item_id": "7123456789012345678",
        "title": "Summer outfit inspiration #fashion",
        "video_cover_url": "https://p16-va.tiktokcdn.com/cover/xyz.jpg",
        "video_duration": 18,
        "create_time": "2024-03-25T10:00:00Z",
        "recommendation_level": "HIGH",
        "recommendation_reason": "High engagement rate and strong completion rate compared to industry benchmarks.",
        "view_count": 150000,
        "like_count": 12500,
        "comment_count": 320,
        "share_count": 450
      }
    ]
  }
}
```

---

## Lấy gợi ý video Spark Ads cho tài khoản TTO (Get Spark Ads video recommendations for a TTO account)
<a id="doc-1825128700959746"></a>
<!-- doc_id: 1825128700959746 -->

Sử dụng endpoint này để lấy kết quả gợi ý video Spark Ads cho tối đa **100 bài đăng video** liên kết với tài khoản TikTok One (TTO) Creator Marketplace của bạn.

Endpoint này phân tích các bài đăng video liên kết với tài khoản TTO Creator Marketplace trong vòng 1 năm qua để đưa ra đề xuất.

> **Khuyến nghị:**
> Để đảm bảo ý nghĩa phân tích, tài khoản TTO Creator Marketplace nên có ít nhất 10 bài đăng video trong năm qua. Nếu có hơn 100 video, phản hồi chỉ bao gồm top 100 video có tiềm năng cao nhất.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/spark_ad/recommend/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã Access token được ủy quyền bởi tài khoản TTO Creator Marketplace. Xem [Obtain authorization and authentication from your TTO Creator Marketplace account](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `tcm_account_id` **(Bắt buộc)** | string | ID của tài khoản TTO Creator Marketplace. |
| `video_ids` | string[] | Danh sách ID video bài đăng cụ thể cần phân tích. |
| `exclude_video_ids` | string[] | Danh sách ID video bài đăng cần loại trừ khỏi phân tích. |
| `time` | string | Thời điểm video được đăng tải. Enum: `LAST_30_DAYS`, `LAST_90_DAYS`, `LAST_180_DAYS`, `PAST_YEAR`. |
| `objective_type` | string | Mục tiêu quảng cáo dự kiến. Enum: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/spark_ad/recommend/?tcm_account_id=7123456789012345678&time=LAST_30_DAYS&objective_type=TRAFFIC' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
TCM_ACCOUNT_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/spark_ad/recommend/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "tcm_account_id": TCM_ACCOUNT_ID,
    "time": "LAST_30_DAYS",
    "objective_type": "TRAFFIC"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ videos` | object[] | Danh sách tối đa 100 video kèm kết quả gợi ý Spark Ads. |
| `↳↳ item_id` | string | ID bài đăng video TikTok. |
| `↳↳ title` | string | Tiêu đề hoặc chú thích của video. |
| `↳↳ video_cover_url` | string | URL ảnh bìa của video. |
| `↳↳ video_duration` | number | Độ dài video (giây). |
| `↳↳ create_time` | string | Thời gian đăng bài. |
| `↳↳ recommendation_level` | string | Xếp loại gợi ý Spark Ads: `HIGH`, `MEDIUM`, hoặc `LOW`. |
| `↳↳ recommendation_reason` | string | Lý do gợi ý chi tiết. |
| `↳↳ view_count` | number | Lượt xem video. |
| `↳↳ like_count` | number | Lượt thích video. |
| `↳↳ comment_count` | number | Lượt bình luận video. |
| `↳↳ share_count` | number | Lượt chia sẻ video. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "videos": [
      {
        "item_id": "7123456789012345678",
        "title": "Unboxing new skincare products #review",
        "video_cover_url": "https://p16-va.tiktokcdn.com/cover/skincare.jpg",
        "video_duration": 25,
        "create_time": "2024-03-20T08:15:00Z",
        "recommendation_level": "HIGH",
        "recommendation_reason": "Audience retention is above 80th percentile for beauty category.",
        "view_count": 89000,
        "like_count": 7200,
        "comment_count": 210,
        "share_count": 180
      }
    ]
  }
}
```


---

## Tạo chiến dịch, nhóm quảng cáo và Spark Ad trong một bước (Create a campaign, an ad group, and a Spark Ad in one step)
<a id="doc-1829744071179330"></a>
<!-- doc_id: 1829744071179330 -->

Sử dụng endpoint này để đồng thời khởi tạo một Chiến dịch (Campaign), một Nhóm quảng cáo (Ad group) trên vị trí phân phối TikTok và một Mẫu quảng cáo Spark Ad (single video Spark Ad) bên trong nhóm quảng cáo chỉ bằng **một yêu cầu API duy nhất**.

### Trước khi bắt đầu
Xem lại các cài đặt mặc định ở cấp chiến dịch, nhóm quảng cáo và mẫu quảng cáo tại [Default settings for All-in-One Spark Ads](63-spark-ads-recommendation.md#doc-1829744101665810) để hiểu rõ các giá trị ngầm định dựa trên mục tiêu quảng cáo (`objective_type`) và mục tiêu tối ưu hóa (`optimization_goal`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/business/spark_ad/create/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `campaign_name` | string | Tên chiến dịch (tối đa 512 ký tự, không hỗ trợ biểu tượng cảm xúc emoji). |
| `objective_type` | string | Mục tiêu quảng cáo. Enum: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`. Xem [Advertising objective](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
| `adgroup_name` | string | Tên nhóm quảng cáo (tối đa 512 ký tự, không hỗ trợ emoji). |
| `saved_audience_id` | string | Bắt buộc truyền `saved_audience_id` hoặc `location_ids`. ID của tệp đối tượng đã lưu (Saved Audience). Xem [Create a Saved Audience](../09-marketing-api/audience.md#doc-1780156510696449). |
| `location_ids` | string[] | Bắt buộc truyền `saved_audience_id` hoặc `location_ids`. Danh sách ID địa điểm nhắm mục tiêu (tối đa 3.000 ID). Bị bỏ qua nếu chỉ định `saved_audience_id`. Xem **Location IDs**. |
| `gender` | string | Giới tính mục tiêu. Enum: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. Bị bỏ qua nếu dùng `saved_audience_id`. |
| `age_groups` | string[] | Mảng các nhóm độ tuổi mục tiêu. Enum xem tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Bị bỏ qua nếu dùng `saved_audience_id`. |
| `budget_mode` | string | Chế độ ngân sách của nhóm quảng cáo. Enum: `BUDGET_MODE_TOTAL` (ngân sách trọn đời), `BUDGET_MODE_DAY` (ngân sách hàng ngày). Xem [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). |
| `budget` | float | Số tiền ngân sách của nhóm quảng cáo. |
| `schedule_type` | string | Loại lịch chạy. Enum: `SCHEDULE_START_END` (có ngày bắt đầu và kết thúc), `SCHEDULE_FROM_NOW` (chạy liên tục từ thời điểm tạo). Nếu `budget_mode` là `BUDGET_MODE_TOTAL`, bắt buộc là `SCHEDULE_START_END`. |
| `schedule_start_time` | string | Thời gian bắt đầu lịch chạy theo định dạng UTC `YYYY-MM-DD HH:MM:SS`. |
| `schedule_end_time` | string | Thời gian kết thúc lịch chạy theo định dạng UTC `YYYY-MM-DD HH:MM:SS`. Bắt buộc khi `schedule_type` là `SCHEDULE_START_END`. |
| `optimization_goal` | string | Mục tiêu tối ưu hóa. Phụ thuộc vào `objective_type`: `REACH` (Reach), `CLICK` (Traffic), `VIDEO_VIEW` (Video Views), `ENGAGEMENT` (Engagement). |
| `frequency` | number | Giới hạn tần suất hiển thị (chỉ áp dụng cho mục tiêu `REACH`). |
| `frequency_schedule` | number | Chu kỳ ngày để áp dụng giới hạn tần suất hiển thị. |
| `bid_type` | string | Loại giá thầu. Enum: `BID_TYPE_NO_BID` (Phân phối tối đa), `BID_TYPE_CUSTOM` (Giá thầu tùy chỉnh). |
| `bid_price` | float | Giá thầu mục tiêu khi `bid_type` là `BID_TYPE_CUSTOM`. |
| `conversion_bid_price` | float | Giá thầu chuyển đổi khi tối ưu hóa theo sự kiện chuyển đổi. |
| `identity_id` **(Bắt buộc)** | string | ID danh tính tài khoản TikTok sử dụng để chạy Spark Ad. |
| `identity_type` **(Bắt buộc)** | string | Loại danh tính. Enum: `AUTH_CODE` (Mã ủy quyền bài đăng), `TT_USER` (Người dùng tài khoản TikTok liên kết), `BC_AUTH_TT` (Ủy quyền qua Business Center). |
| `identity_authorized_bc_id` | string | ID Business Center ủy quyền danh tính (bắt buộc khi `identity_type` là `BC_AUTH_TT`). |
| `tiktok_item_id` **(Bắt buộc)** | string | ID của bài đăng video TikTok tự nhiên làm nội dung cho Spark Ad. |
| `ad_name` | string | Tên mẫu quảng cáo Spark Ad (tối đa 512 ký tự). |
| `landing_page_url` | string | URL trang đích của quảng cáo (bắt buộc đối với mục tiêu `TRAFFIC`). |
| `call_to_action` | string | Nút kêu gọi hành động (Call To Action). Enum xem tại [Enumeration - Call To Action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/business/spark_ad/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "campaign_name": "Summer_Promotion_SparkAds",
    "objective_type": "TRAFFIC",
    "adgroup_name": "Traffic_AdGroup_01",
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "age_groups": ["AGE_18_24", "AGE_25_34"],
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 50.0,
    "schedule_type": "SCHEDULE_FROM_NOW",
    "schedule_start_time": "2024-04-01 10:00:00",
    "optimization_goal": "CLICK",
    "bid_type": "BID_TYPE_NO_BID",
    "identity_id": "7123456789012345678",
    "identity_type": "TT_USER",
    "tiktok_item_id": "7123456789012345678",
    "ad_name": "SparkAd_Summer_01",
    "landing_page_url": "https://example.com/summer-sale",
    "call_to_action": "SHOP_NOW"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/business/spark_ad/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "campaign_name": "Summer_Promotion_SparkAds",
    "objective_type": "TRAFFIC",
    "adgroup_name": "Traffic_AdGroup_01",
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "age_groups": ["AGE_18_24", "AGE_25_34"],
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 50.0,
    "schedule_type": "SCHEDULE_FROM_NOW",
    "schedule_start_time": "2024-04-01 10:00:00",
    "optimization_goal": "CLICK",
    "bid_type": "BID_TYPE_NO_BID",
    "identity_id": "7123456789012345678",
    "identity_type": "TT_USER",
    "tiktok_item_id": "7123456789012345678",
    "ad_name": "SparkAd_Summer_01",
    "landing_page_url": "https://example.com/summer-sale",
    "call_to_action": "SHOP_NOW"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về chứa các ID tài nguyên vừa tạo. |
| `↳ campaign_id` | string | ID của chiến dịch quảng cáo vừa tạo. |
| `↳ adgroup_id` | string | ID của nhóm quảng cáo vừa tạo. |
| `↳ ad_id` | string | ID của mẫu quảng cáo Spark Ad vừa tạo. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "campaign_id": "1765432109876543",
    "adgroup_id": "1765432109876588",
    "ad_id": "1765432109876599"
  }
}
```

---

## Cài đặt mặc định cho All-in-One Spark Ads (Default settings for All-in-One Spark Ads)
<a id="doc-1829744101665810"></a>
<!-- doc_id: 1829744101665810 -->

Bảng dưới đây tổng hợp các thiết lập mặc định cho All-in-One Spark Ads (quảng cáo tạo thông qua endpoint `/business/spark_ad/create/` [chi tiết](#doc-1829744071179330)). Các cài đặt mặc định này sẽ thay đổi tùy thuộc vào `objective_type` và `optimization_goal` được chọn.

Để tìm hiểu chi tiết các trường với giá trị mặc định, xem mô tả tại [/campaign/get/](24-campaign.md#doc-1739315828649986), [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922), và [/ad/get/](02-ads-p1.md#doc-1735735588640770).

| Cấp độ (Level) | Trường (Field) | Cài đặt mặc định (Default settings) |
|---|---|---|
| Campaign | `objective_type` | `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT` |
| Campaign | `operation_status` | `ENABLE` |
| Campaign | `budget_mode` | `BUDGET_MODE_INFINITE` |
| Campaign | `postbacks_mode` | `DEFAULT` |
| Ad Group | `placement_type` | `PLACEMENT_TYPE_NORMAL` |
| Ad Group | `placements` | `["PLACEMENT_TIKTOK"]` |
| Ad Group | `operation_status` | `ENABLE` |
| Ad Group | `budget_mode` | `BUDGET_MODE_DAY` (nếu không chỉ định) |
| Ad Group | `billing_event` | `CPM` (cho `REACH`, `VIDEO_VIEWS`), `CPC` (cho `TRAFFIC`, `ENGAGEMENT`) |
| Ad Group | `pacing` | `PACING_MODE_SMOOTH` |
| Ad Group | `bid_type` | `BID_TYPE_NO_BID` (nếu không chỉ định) |
| Ad | `operation_status` | `ENABLE` |
| Ad | `ad_format` | `SINGLE_VIDEO` |
| Ad | `is_spark_ads` | `true` |
