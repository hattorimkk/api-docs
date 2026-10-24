# GMV Max — phần 3/3: Danh mục Chỉ số Báo cáo (Metrics Reference)

> Phân hệ: API Reference > GMV Max > Run a GMV Max Campaign report > Metrics in GMV Max Campaign reports.
> Tài liệu này tổng hợp toàn bộ các chỉ số thuộc tính (Attribute metrics) và chỉ số phân phối/hiệu suất (Delivery metrics) được hỗ trợ trong các báo cáo chiến dịch GMV Max (Product GMV Max và LIVE GMV Max) trên TikTok Shop.

---

## Mục lục điều hướng
- [1. Tổng quan về các chỉ số chiến dịch GMV Max](#tong-quan-ve-cac-chi-so-chien-dich-gmv-max)
  - [Chỉ số thuộc tính (Attribute metrics)](#chi-so-thuoc-tinh-attribute-metrics)
  - [Chỉ số phân phối (Delivery metrics)](#chi-so-phan-phoi-delivery-metrics)
- [2. Dành cho tất cả Chiến dịch GMV Max (For all GMV Max Campaigns)](#danh-cho-tat-ca-chien-dich-gmv-max)
  - [Chỉ số tổng quan cấp tài khoản quảng cáo (Overview metrics)](#chi-so-tong-quan-overview-metrics)
- [3. Dành cho Chiến dịch GMV Max Sản phẩm (For Product GMV Max Campaigns)](#danh-cho-chien-dich-gmv-max-san-pham)
  - [Chỉ số cấp chiến dịch (Campaign-level metrics)](#chi-so-cap-chien-dich-product)
  - [Chỉ số cấp sản phẩm (Product-level metrics)](#chi-so-cap-san-pham)
  - [Chỉ số cấp mẫu quảng cáo (Creative-level metrics)](#chi-so-cap-mau-quang-cao)
    - [Dành cho mẫu quảng cáo kèm trạng thái (For creatives with statuses)](#mau-quang-cao-kem-trang-thai)
    - [(Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo trả phí & tự nhiên (For ads and organic creatives)](#mau-quang-cao-tra-phi-va-tu-nhien)
    - [(Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo chỉ tự nhiên (For organic only creatives)](#mau-quang-cao-chi-tu-nhien)
    - [(Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo đã bị gỡ (For removed creatives)](#mau-quang-cao-da-bi-go)
  - [Chỉ số cấp khoảng thời gian (Duration-level metrics)](#chi-so-cap-khoang-thoi-gian-product)
- [4. Dành cho Chiến dịch GMV Max LIVE (For LIVE GMV Max Campaigns)](#danh-cho-chien-dich-gmv-max-live)
  - [Chỉ số cấp chiến dịch (Campaign-level metrics)](#chi-so-cap-chien-dich-live)
  - [Chỉ số cấp phòng livestream (Livestream-level metrics)](#chi-so-cap-phong-livestream)
  - [Chỉ số cấp khoảng thời gian (Duration-level metrics)](#chi-so-cap-khoang-thoi-gian-live)
- [5. Mã nguồn mẫu truy xuất dữ liệu (Data Retrieval - Python & cURL)](#ma-nguon-mau-truy-xuat-du-lieu)

---

<a id="doc-1824722485971009"></a>
<!-- doc_id: 1824722485971009 -->
# Các chỉ số trong báo cáo Chiến dịch GMV Max (Metrics in GMV Max Campaign reports)
> Đường dẫn: API Reference > GMV Max > Run a GMV Max Campaign report > Metrics in GMV Max Campaign reports
Tài liệu này tổng hợp toàn bộ các loại chỉ số được hỗ trợ trong các báo cáo Chiến dịch GMV Max.

<a id="tong-quan-ve-cac-chi-so-chien-dich-gmv-max"></a>
# Tổng quan về các chỉ số chiến dịch GMV Max (GMV Max Campaign metrics overview)
Các phần dưới đây phác thảo toàn bộ chỉ số thuộc tính (Attribute metrics) và chỉ số phân phối (Delivery metrics) khả dụng.

Để tìm hiểu mô tả chi tiết của từng chỉ số cùng với các nhóm chiều dữ liệu và bộ lọc khả dụng cho các cấp độ chỉ số khác nhau trên toàn bộ Chiến dịch GMV Max, cho Chiến dịch GMV Max Sản phẩm, hoặc cho Chiến dịch GMV Max LIVE, xem các phần [Dành cho tất cả Chiến dịch GMV Max](#danh-cho-tat-ca-chien-dich-gmv-max), [Dành cho Chiến dịch GMV Max Sản phẩm](#danh-cho-chien-dich-gmv-max-san-pham), và [Dành cho Chiến dịch GMV Max LIVE](#danh-cho-chien-dich-gmv-max-live).

<a id="chi-so-thuoc-tinh-attribute-metrics"></a>
## Chỉ số thuộc tính (Attribute metrics)
Chỉ số thuộc tính thể hiện các đặc tính thiết yếu của chiến dịch, sản phẩm, mẫu quảng cáo, phiên livestream và các khoảng thời gian chạy. Ví dụ bao gồm ID chiến dịch quảng cáo (`campaign_id`), tên chiến dịch (`campaign_name`) và tên mẫu quảng cáo (`title`).

> **Lưu ý (Note):** 
> Bạn có thể truy xuất các chỉ số thuộc tính trong bất kỳ trường hợp nào sau đây: 
> - Khi truy vấn dữ liệu ở cấp chiến dịch (campaign level)
> - Khi truy vấn dữ liệu ở cấp sản phẩm, phiên livestream hoặc khoảng thời gian (duration level) đồng thời chỉ định một ID duy nhất trong bộ lọc `campaign_ids`, `item_group_ids` hoặc `room_ids` và chỉ bao gồm đúng một chiều ID trong tham số `dimensions`
> 
> Tuy nhiên, bạn KHÔNG THỂ truy xuất các chỉ số thuộc tính trong bất kỳ trường hợp nào sau đây:
> - Khi truy vấn dữ liệu ở cấp sản phẩm, mẫu quảng cáo, phiên livestream hoặc khoảng thời gian đồng thời chỉ định nhiều ID trong bộ lọc `campaign_ids`, `item_group_ids` hoặc `room_ids`
> - Khi truy vấn dữ liệu ở cấp sản phẩm, mẫu quảng cáo, phiên livestream hoặc khoảng thời gian đồng thời bao gồm nhiều chiều ID trong tham số `dimensions`

Loại chiến dịch GMV Max và cấp độ chỉ số được hỗ trợ (Supported GMV Max Campaign type and metric level)
Trường chỉ số (Metric field)
Mô tả (Description)

### Chiến dịch GMV Max Sản phẩm, Cấp chiến dịch (Product GMV Max Campaign, Campaign-level)
- `campaign_id`: ID chiến dịch quảng cáo (Campaign ID)
- `operation_status`: Trạng thái bật/tắt chiến dịch (Campaign on/off status)
- `campaign_name`: Tên chiến dịch (Campaign name)
- `schedule_type`: Loại lịch chạy (Schedule type)
- `schedule_start_time`: Thời gian bắt đầu theo lịch (Schedule start time)
- `schedule_end_time`: Thời gian kết thúc theo lịch (Schedule end time)
- `target_roi_budget`: Ngân sách mục tiêu ROI (Target ROI budget)
- `bid_type`: Chế độ tối ưu hóa (Optimization mode)
- `max_delivery_budget`: Ngân sách phân phối tối đa (Max delivery budget)

### Chiến dịch GMV Max Sản phẩm, Cấp sản phẩm (Product GMV Max Campaign, Product-level)
- `product_name`: Tên sản phẩm (Product name)
- `item_group_id`: ID SPU sản phẩm (Product SPU ID)
- `product_image_url`: URL hình ảnh sản phẩm (Product image URL)
- `bid_type`: Chế độ tối ưu hóa (Optimization mode)

### Chiến dịch GMV Max Sản phẩm, Cấp mẫu quảng cáo (Product GMV Max Campaign, Creative-level)
- `title`: Tên mẫu quảng cáo (Creative name)
- `item_id`: ID bài đăng TikTok (TikTok post ID)
- `tt_account_name`: Tên tài khoản TikTok (TikTok account name)
- `tt_account_profile_image_url`: URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL)
- `tt_account_authorization_type`: Loại ủy quyền tài khoản TikTok (Authorization type)
- `shop_content_type`: Loại nội dung cửa hàng (Shop content type)

### Chiến dịch GMV Max Sản phẩm, Cấp khoảng thời gian (Product GMV Max Campaign, Duration-level)
- `bid_type`: Chế độ tối ưu hóa (Optimization mode)

### Chiến dịch GMV Max LIVE, Cấp chiến dịch (LIVE GMV Max Campaign, Campaign-level)
- `campaign_id`: ID chiến dịch quảng cáo (Campaign ID)
- `operation_status`: Trạng thái bật/tắt chiến dịch (Campaign on/off status)
- `campaign_name`: Tên chiến dịch (Campaign name)
- `tt_account_name`: Tên tài khoản TikTok (TikTok account name)
- `tt_account_profile_image_url`: URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL)
- `identity_id`: ID danh tính tài khoản TikTok (Identity ID / TikTok account ID)
- `bid_type`: Chế độ tối ưu hóa (Optimization mode)
- `schedule_type`: Loại lịch chạy (Schedule type)
- `schedule_start_time`: Thời gian bắt đầu theo lịch (Schedule start time)
- `schedule_end_time`: Thời gian kết thúc theo lịch (Schedule end time)
- `target_roi_budget`: Ngân sách mục tiêu ROI (Target ROI budget)
- `max_delivery_budget`: Ngân sách phân phối tối đa (Max delivery budget)

### Chiến dịch GMV Max LIVE, Cấp phòng livestream (LIVE GMV Max Campaign, Livestream-level)
- `live_name`: Tên phiên LIVE (LIVE name)
- `live_status`: Trạng thái phiên livestream (Livestream status)
- `live_launched_time`: Thời gian bắt đầu phát livestream (Livestream launched time)
- `live_duration`: Thời lượng phát livestream (Livestream duration)

### Chiến dịch GMV Max LIVE, Cấp khoảng thời gian (LIVE GMV Max Campaign, Duration-level)
- `bid_type`: Chế độ tối ưu hóa (Optimization mode)

<a id="chi-so-phan-phoi-delivery-metrics"></a>
## Chỉ số phân phối (Delivery metrics)
Chỉ số phân phối cung cấp thông tin chi tiết nền tảng về hiệu suất hoạt động của các chiến dịch, sản phẩm, mẫu quảng cáo, phiên livestream và các khoảng thời gian chạy, chẳng hạn như Chi phí (Cost) và Tổng doanh thu (Gross Revenue).

Loại chiến dịch GMV Max và cấp độ chỉ số được hỗ trợ (Supported GMV Max Campaign type and metric level)
Trường chỉ số (Metric field)
Mô tả (Description)

### Tất cả Chiến dịch GMV Max, Cấp tài khoản quảng cáo (All GMV Max Campaigns, Ad account-level)
- `cost`: Chi phí quảng cáo (Cost)
- `orders`: Số lượng đơn hàng SKU (Orders - SKU)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)
- `net_cost`: Chi phí ròng (Net cost)

### Chiến dịch GMV Max Sản phẩm, Cấp chiến dịch (Product GMV Max Campaign, Campaign-level)
- `roas_bid`: Mục tiêu ROI (Target ROI)
- `cost`: Chi phí quảng cáo (Cost)
- `net_cost`: Chi phí ròng (Net cost)
- `orders`: Số lượng đơn hàng SKU (Orders - SKU)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)

### Chiến dịch GMV Max Sản phẩm, Cấp sản phẩm (Product GMV Max Campaign, Product-level)
- `product_status`: Trạng thái sản phẩm (Product status)
- `orders`: Số lượng đơn hàng SKU (Orders - SKU)
- `gross_revenue`: Tổng doanh thu (Gross revenue)

### Chiến dịch GMV Max Sản phẩm, Cấp mẫu quảng cáo (Product GMV Max Campaign, Creative-level)
- `creative_delivery_status`: Trạng thái phân phối mẫu quảng cáo (Status)
- `orders`: Số lượng đơn hàng SKU (Orders - SKU)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `product_impressions`: Lượt hiển thị quảng cáo sản phẩm (Product ad impressions)
- `product_clicks`: Lượt nhấp quảng cáo sản phẩm (Product ad clicks)
- `product_click_rate`: Tỷ lệ nhấp quảng cáo sản phẩm (Product ad click rate)
- `ad_click_rate`: Tỷ lệ nhấp quảng cáo (Ad click rate)
- `ad_conversion_rate`: Tỷ lệ chuyển đổi quảng cáo (Ad conversion rate)
- `ad_video_view_rate_2s`: Tỷ lệ xem video quảng cáo 2 giây (2-second ad video view rate)
- `ad_video_view_rate_6s`: Tỷ lệ xem video quảng cáo 6 giây (6-second ad video view rate)
- `ad_video_view_rate_p25`: Tỷ lệ xem video quảng cáo đạt 25% (25% ad video view rate)
- `ad_video_view_rate_p50`: Tỷ lệ xem video quảng cáo đạt 50% (50% ad video view rate)
- `ad_video_view_rate_p75`: Tỷ lệ xem video quảng cáo đạt 75% (75% ad video view rate)
- `ad_video_view_rate_p100`: Tỷ lệ xem video quảng cáo đạt 100% (100% ad video view rate)

### Chiến dịch GMV Max Sản phẩm, Cấp khoảng thời gian (Product GMV Max Campaign, Duration-level)
- `cost`: Chi phí quảng cáo (Cost)
- `orders`: Số lượng đơn hàng SKU (Orders - SKU)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)
- `roas_bid`: Mục tiêu ROI (Target ROI)

### Chiến dịch GMV Max LIVE, Cấp chiến dịch (LIVE GMV Max Campaign, Campaign-level)
- `cost`: Chi phí quảng cáo (Cost)
- `net_cost`: Chi phí ròng (Net cost)
- `orders`: Số lượng đơn hàng (Orders)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)
- `live_views`: Lượt xem phiên LIVE (LIVE views)
- `cost_per_live_view`: Chi phí trên mỗi lượt xem LIVE (Cost per LIVE view)
- `10_second_live_views`: Lượt xem LIVE từ 10 giây trở lên (10-second LIVE views)
- `cost_per_10_second_live_view`: Chi phí trên mỗi lượt xem LIVE 10 giây (Cost per 10-second LIVE view)
- `live_follows`: Lượt theo dõi qua phiên LIVE (LIVE follows)

### Chiến dịch GMV Max LIVE, Cấp phòng livestream (LIVE GMV Max Campaign, Livestream-level)
- `cost`: Chi phí quảng cáo (Cost)
- `net_cost`: Chi phí ròng (Net cost)
- `orders`: Số lượng đơn hàng (Orders)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)
- `live_views`: Lượt xem phiên LIVE (LIVE views)
- `cost_per_live_view`: Chi phí trên mỗi lượt xem LIVE (Cost per LIVE view)
- `10_second_live_views`: Lượt xem LIVE từ 10 giây trở lên (10-second LIVE views)
- `cost_per_10_second_live_view`: Chi phí trên mỗi lượt xem LIVE 10 giây (Cost per 10-second LIVE view)
- `live_follows`: Lượt theo dõi qua phiên LIVE (LIVE follows)

### Chiến dịch GMV Max LIVE, Cấp khoảng thời gian (LIVE GMV Max Campaign, Duration-level)
- `cost`: Chi phí quảng cáo (Cost)
- `orders`: Số lượng đơn hàng (Orders)
- `cost_per_order`: Chi phí trên mỗi đơn hàng (Cost per order)
- `gross_revenue`: Tổng doanh thu (Gross revenue)
- `roi`: Tỷ suất hoàn vốn đầu tư (ROI)

---

<a id="danh-cho-tat-ca-chien-dich-gmv-max"></a>
# Dành cho tất cả Chiến dịch GMV Max (For all GMV Max Campaigns)
Dữ liệu chỉ số báo cáo cho tất cả Chiến dịch GMV Max liên kết với một TikTok Shop sẽ khả dụng khi bạn đặt trường bộ lọc `gmv_max_promotion_types` thành `["PRODUCT", "LIVE"]` hoặc để trống không chỉ định `gmv_max_promotion_types`.

<a id="chi-so-tong-quan-overview-metrics"></a>
## Chỉ số tổng quan (Overview metrics)
Các chỉ số này hiển thị hiệu suất tổng thể của các Chiến dịch GMV Max được liên kết với một TikTok Shop, bất kể chiến dịch được tạo trên TikTok Ads Manager hay TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số này, hãy chỉ định bất kỳ nhóm chiều dữ liệu nào sau đây qua tham số `dimensions`:
- `["advertiser_id"]`
- `["advertiser_id","stat_time_day"]`
- `["advertiser_id","stat_time_hour"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| gmv_max_promotion_types | Tùy chọn (Optional) | Không áp dụng (N/A) | Chỉ định bất kỳ giá trị nào sau đây:<br>• `PRODUCT`: Chiến dịch GMV Max Sản phẩm (Product GMV Max Campaign).<br>• `LIVE`: Chiến dịch GMV Max LIVE (LIVE GMV Max Campaign). |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền ước tính bạn đã chi tiêu cho quảng cáo trong suốt lịch chạy, tính theo loại tiền tệ của tài khoản quảng cáo. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ đã hoàn thành trong suốt Chiến dịch GMV Max. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cost per order) | Chi phí trung bình phát sinh cho mỗi đơn hàng được đặt, tính theo loại tiền tệ của tài khoản quảng cáo. Chỉ số này được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo (Chi phí / Đơn hàng). |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop được ghi nhận đóng góp cho chiến dịch của bạn, tính theo loại tiền tệ của tài khoản quảng cáo. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp từ nền tảng TikTok Shop dành cho người dùng đó. |
| roi | string | Tỷ suất hoàn vốn đầu tư (ROI) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng TikTok Shop được ghi nhận đóng góp cho chiến dịch của bạn. |
| net_cost | string | Chi phí ròng (Net cost) | Số tiền đã chi tiêu, không bao gồm tín dụng quảng cáo hoặc phiếu giảm giá đã sử dụng, tính theo loại tiền tệ của tài khoản quảng cáo. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["advertiser_id", "stat_time_day"]&metrics=["cost", "orders", "cost_per_order", "gross_revenue", "roi", "net_cost"]&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "advertiser_id": "{{advertiser_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "cost": "9387.58",
                    "cost_per_order": "1.41",
                    "gross_revenue": "43117.68",
                    "net_cost": "6550.08",
                    "orders": "6674",
                    "roi": "4.59"
                }
            },
            {
                "dimensions": {
                    "advertiser_id": "{{advertiser_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "cost": "7230.56",
                    "cost_per_order": "1.44",
                    "gross_revenue": "31547.59",
                    "net_cost": "7230.56",
                    "orders": "5036",
                    "roi": "4.36"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="danh-cho-chien-dich-gmv-max-san-pham"></a>
# Dành cho Chiến dịch GMV Max Sản phẩm (For Product GMV Max Campaigns)
Dữ liệu chỉ số báo cáo cho các Chiến dịch GMV Max Sản phẩm liên kết với một TikTok Shop được hỗ trợ ở 4 cấp độ: cấp chiến dịch (campaign), cấp sản phẩm (product), cấp mẫu quảng cáo (creative), và cấp khoảng thời gian (duration).

<a id="chi-so-cap-chien-dich-product"></a>
## Chỉ số cấp chiến dịch (Campaign-level metrics for Product GMV Max)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất của các Chiến dịch GMV Max Sản phẩm được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp chiến dịch cho Chiến dịch GMV Max Sản phẩm, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["campaign_id"]`
- `["campaign_id","stat_time_day"]`
- `["campaign_id","stat_time_hour"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| gmv_max_promotion_types | Bắt buộc (Required) | Không áp dụng (N/A) | `["PRODUCT"]` |
| campaign_ids | Tùy chọn (Optional) | 100 | Chỉ định danh sách ID của các Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID của các Chiến dịch GMV Max Sản phẩm, hãy sử dụng endpoint [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177). Đặt `gmv_max_promotion_types` thành `["PRODUCT_GMV_MAX"]` và chỉ định ID của TikTok Shop qua tham số `store_ids`. |
| campaign_name | Tùy chọn (Optional) | Không áp dụng (N/A) | Không áp dụng (N/A) |
| campaign_statuses | Tùy chọn (Optional) | Không áp dụng (N/A) | Chỉ định bất kỳ giá trị nào sau đây:<br>• `STATUS_DELIVERY_OK`: Đang hoạt động (Active).<br>• `STATUS_DISABLE`: Tắt/Không hoạt động (Inactive).<br>• `STATUS_DELETE`: Đã xóa (Deleted).<br>• `STATUS_NOT_DELIVERY`: Không phân phối (Not delivering).<br>• `STATUS_ALL`: Tất cả trạng thái (All statuses). |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| campaign_id | string | ID chiến dịch quảng cáo | Không áp dụng (N/A) |
| operation_status | string | Trạng thái bật/tắt chiến dịch (Campaign on/off status) | Các giá trị enum hỗ trợ:<br>• `ENABLE`: Đang bật (on).<br>• `DISABLE`: Đang tắt (off). |
| campaign_name | string | Tên chiến dịch (Campaign name) | Không áp dụng (N/A) |
| schedule_type | string | Loại lịch chạy (Schedule type) | Giá trị enum:<br>• `Continuously`: Chạy chiến dịch liên tục kể từ thời gian bắt đầu đã lên lịch. |
| schedule_start_time | string | Thời gian bắt đầu theo lịch (Schedule start time) | Múi giờ: UTC+0. |
| schedule_end_time | string | Thời gian kết thúc theo lịch (Schedule end time) | Múi giờ: UTC+0. |
| target_roi_budget | string | Ngân sách mục tiêu ROI (Target ROI budget) | Không áp dụng (N/A) |
| bid_type | string | Chế độ tối ưu hóa (Optimization mode) | Các giá trị enum hỗ trợ:<br>• `CUSTOM`: Mục tiêu ROI (Target ROI).<br>• `NO_BID`: Phân phối tối đa (Maximum delivery). |
| max_delivery_budget | string | Ngân sách phân phối tối đa (Max delivery budget) | Không áp dụng (N/A) |
| roas_bid | string | Mục tiêu ROI (Target ROI) | Không áp dụng (N/A) |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền ước tính bạn đã chi tiêu cho quảng cáo trong suốt lịch chạy, tính theo loại tiền tệ của tài khoản quảng cáo. |
| net_cost | string | Chi phí ròng (Net cost) | Số tiền đã chi tiêu, không bao gồm tín dụng quảng cáo hoặc phiếu giảm giá đã sử dụng, tính theo loại tiền tệ của tài khoản quảng cáo. Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 01 tháng 09 năm 2023. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cost per order) | Chi phí quảng cáo trung bình cho mỗi đơn hàng được đặt trong Chiến dịch GMV Max này, tính theo loại tiền tệ của tài khoản quảng cáo (không bao gồm đơn hàng LIVE), được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| roi | string | Tỷ suất hoàn vốn đầu tư (ROI) | ROI sản phẩm, được tính bằng tổng doanh số (cả trả phí và tự nhiên) được ghi nhận đóng góp cho Chiến dịch GMV Max đang hoạt động (không bao gồm đơn hàng LIVE) chia cho tổng chi phí quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["campaign_id", "stat_time_day"]&metrics=["campaign_id", "operation_status", "campaign_name", "schedule_type", "schedule_start_time", "schedule_end_time", "target_roi_budget", "bid_type", "max_delivery_budget", "roas_bid", "cost", "net_cost", "orders", "cost_per_order", "gross_revenue", "roi"]&filtering={"gmv_max_promotion_types": ["PRODUCT"]}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "campaign_id": "{{campaign_id}}",
                    "campaign_name": "{{campaign_name}}",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "max_delivery_budget": "0.00",
                    "net_cost": "0.00",
                    "operation_status": "ENABLE",
                    "orders": "0",
                    "roas_bid": "5.50",
                    "roi": "0.00",
                    "schedule_end_time": "{{schedule_end_time}}",
                    "schedule_start_time": "{{schedule_start_time}}",
                    "schedule_type": "Continuously",
                    "target_roi_budget": "20000.00"
                }
            },
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "campaign_id": "{{campaign_id}}",
                    "campaign_name": "{{campaign_name}}",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "max_delivery_budget": "0.00",
                    "net_cost": "0.00",
                    "operation_status": "DISABLE",
                    "orders": "0",
                    "roas_bid": "4.50",
                    "roi": "0.00",
                    "schedule_end_time": "{{schedule_end_time}}",
                    "schedule_start_time": "{{schedule_start_time}}",
                    "schedule_type": "Continuously",
                    "target_roi_budget": "1500.00"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="chi-so-cap-san-pham"></a>
## Chỉ số cấp sản phẩm (Product-level metrics)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất cho từng sản phẩm nằm trong Chiến dịch GMV Max Sản phẩm được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp sản phẩm cho Chiến dịch GMV Max Sản phẩm, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["item_group_id"]`
- `["item_group_id","stat_time_day"]`
- `["item_group_id","stat_time_hour"]`
- `["campaign_id","item_group_id"]`
- `["campaign_id","item_group_id","stat_time_day"]`
- `["campaign_id","item_group_id","stat_time_hour"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| campaign_ids | Bắt buộc (Required) | 100 | Chỉ định ID của Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `campaign_id` để truy vấn các chỉ số cấp chiến dịch. |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| product_name | string | Tên sản phẩm (Product name) | Không áp dụng (N/A) |
| item_group_id | string | ID SPU sản phẩm (Product SPU ID) | Không áp dụng (N/A) |
| product_image_url | string | URL hình ảnh sản phẩm (Product image URL) | Không áp dụng (N/A) |
| product_status | string | Trạng thái sản phẩm (Product status) | Các giá trị enum hỗ trợ: `available` (khả dụng), `unavailable` (không khả dụng).<br>Ví dụ: `available`. |
| bid_type | string | Chế độ tối ưu hóa (Optimization mode) | Các giá trị enum hỗ trợ:<br>• `CUSTOM`: Mục tiêu ROI (Target ROI).<br>• `NO_BID`: Phân phối tối đa (Maximum delivery). |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền bạn đã chi tiêu cho quảng cáo cho sản phẩm này trong suốt Chiến dịch GMV Max Sản phẩm. Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max cho sản phẩm này, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cost per order) | Chi phí quảng cáo trung bình cho mỗi đơn hàng được đặt cho sản phẩm này trong Chiến dịch GMV Max, không bao gồm đơn hàng LIVE, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó. |
| roi | string | Tỷ suất hoàn vốn đầu tư (ROI) | ROI sản phẩm, được tính bằng tổng doanh số (cả trả phí và tự nhiên) được ghi nhận đóng góp cho Chiến dịch GMV Max đang hoạt động (không bao gồm đơn hàng LIVE) chia cho tổng chi phí quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["item_group_id","stat_time_day"]&metrics=["product_name", "item_group_id", "product_image_url", "product_status", "bid_type","cost","orders","cost_per_order", "gross_revenue", "roi"]&filtering={"campaign_ids":["{{campaign_id}}"]}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "item_group_id": "{{item_group_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "cost": "13.86",
                    "cost_per_order": "2.77",
                    "currency": "0",
                    "gross_revenue": "55.47",
                    "item_group_id": "{{item_group_id}}",
                    "orders": "5",
                    "product_image_url": "{{product_image_url}}",
                    "product_name": "{{product_name}}",
                    "product_status": "available",
                    "roi": "4.00"
                }
            },
            {
                "dimensions": {
                    "item_group_id": "{{item_group_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "cost": "12.11",
                    "cost_per_order": "2.02",
                    "currency": "0",
                    "gross_revenue": "69.49",
                    "item_group_id": "{{item_group_id}}",
                    "orders": "6",
                    "product_image_url": "{{product_image_url}}",
                    "product_name": "{{product_name}}",
                    "product_status": "available",
                    "roi": "5.74"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="chi-so-cap-mau-quang-cao"></a>
## Chỉ số cấp mẫu quảng cáo (Creative-level metrics)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất cho từng mẫu quảng cáo nằm trong Chiến dịch GMV Max Sản phẩm được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp mẫu quảng cáo cho Chiến dịch GMV Max Sản phẩm, hãy chỉ định các nhóm chiều sau bằng tham số `dimensions`:
- `["campaign_id","item_group_id","item_id"]`
- `["campaign_id","item_group_id","item_id","stat_time_day"]`
- `["item_id","stat_time_day"]`

> **Lưu ý (Note):** 
> Nếu bạn chỉ định nhóm chiều `["campaign_id","item_group_id","item_id","stat_time_day"]`, API sẽ chỉ trả về các bản ghi có dữ liệu chi phí tương ứng. Ví dụ, đối với một chiến dịch có 100 mẫu quảng cáo nhưng chỉ có 20 mẫu phát sinh chi phí, bạn sẽ chỉ nhận được dữ liệu báo cáo cho 20 mẫu quảng cáo đó.

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn/Có điều kiện (Required/Optional/Conditional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| campaign_ids | Bắt buộc (Required) | 100 | Chỉ định ID của Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `campaign_id` để truy vấn các chỉ số cấp chiến dịch.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |
| item_group_ids | Bắt buộc (Required) | 100 | Chỉ định ID của SPU được sử dụng trong Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `item_group_id` để truy vấn các chỉ số cấp sản phẩm.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |
| creative_types {-to-be-deprecated} | Có điều kiện (Conditional) | 1 | • Bắt buộc khi bạn lọc một SPU ID duy nhất bằng `campaign_ids` và `item_group_ids`.<br>• Không được hỗ trợ khi bạn chỉ định nhiều ID trong bộ lọc `campaign_ids` hoặc `item_group_ids` (hoặc cả hai), hoặc chỉ định nhiều chiều ID.<br>Chỉ định bất kỳ giá trị nào sau đây:<br>• `ADS_AND_ORGANIC`: Quảng cáo trả phí và tự nhiên (Ads and organic).<br>• `ORGANIC`: Chỉ tự nhiên (Organic only).<br>• `REMOVED`: Đã gỡ (Removed).<br>**Lưu ý**: Bộ lọc này không thể dùng đồng thời với `creative_delivery_statuses`. |
| creative_delivery_statuses | Tùy chọn (Optional) | Không áp dụng (N/A) | • Bạn chỉ có thể sử dụng bộ lọc này trong các trường hợp sau:<br>  - Khi bạn chỉ định nhiều ID trong bộ lọc `campaign_ids` hoặc `item_group_ids` (hoặc cả hai)<br>  - Khi bạn chỉ định một ID trong bộ lọc `campaign_ids` hoặc `item_group_ids` (hoặc cả hai)<br>  - Khi bạn chỉ định nhiều chiều ID<br>• Bộ lọc này không thể sử dụng cùng lúc với `creative_types`.<br>Chỉ định một hoặc nhiều giá trị sau:<br>• `IN_QUEUE`: Đang xếp hàng (In queue). Bài đăng đã sẵn sàng để được kiểm thử tiềm năng thúc đẩy chuyển đổi.<br>• `LEARNING`: Đang học máy (Learning). Bài đăng đang trong giai đoạn kiểm thử tiềm năng chuyển đổi.<br>• `DELIVERING`: Đang phân phối (Delivering). Bài đăng đang được đẩy quảng cáo đều đặn như một phần của chiến dịch.<br>• `NOT_DELIVERYING`: Không phân phối (Not delivering). Bài đăng không thể hiện tiềm năng chuyển đổi tốt trong giai đoạn thử nghiệm và sẽ không được đẩy thường xuyên.<br>• `AUTHORIZATION_NEEDED`: Cần ủy quyền (Authorization needed). Video này chưa được ủy quyền để dùng chạy quảng cáo. Bạn có thể tự ủy quyền video từ tài khoản TikTok của mình hoặc yêu cầu ủy quyền từ nhà sáng tạo khác. Trạng thái sẽ cập nhật tại đây trong vòng 20 phút sau khi hoàn tất ủy quyền.<br>• `EXCLUDED`: Đã loại trừ (Excluded). Bài đăng đã được gỡ thủ công và không được đẩy quảng cáo. Bạn có thể thêm lại bài đăng vào chiến dịch bất cứ lúc nào.<br>• `UNAVAILABLE`: Không khả dụng (Unavailable). Video riêng tư, video bị từ chối, video bị xóa hoặc video từ tài khoản TikTok bị đình chỉ sẽ không thể dùng chạy quảng cáo. Đôi khi bạn vẫn thấy chi phí từ các video không khả dụng do video bị hệ thống duyệt nội dung từ chối giữa chừng vẫn có thể đã kịp phân phối trước đó.<br>• `REJECTED`: Bị từ chối (Rejected). Video đã bị đội ngũ kiểm duyệt nội dung từ chối. Nếu bạn đã khiếu nại, trạng thái vẫn là "rejected" cho đến khi xét duyệt xong.<br>• `NOT_ACTIVE`: Không hoạt động (Not active). Bài đăng bị hạ mức ưu tiên vì đã được đăng hơn 30 ngày trước và không phát sinh bất kỳ doanh thu nào trong 30 ngày qua. |
| search_word | Tùy chọn (Optional) | Không áp dụng (N/A) | Không áp dụng (N/A) |

<a id="mau-quang-cao-kem-trang-thai"></a>
### Dành cho mẫu quảng cáo kèm trạng thái (For creatives with statuses)
Chỉ số cấp mẫu quảng cáo kèm trạng thái là các chỉ số thể hiện tiến trình và hiệu quả thử nghiệm của từng mẫu quảng cáo trong suốt quá trình phân phối.

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| title | string | Tên mẫu quảng cáo (Creative name) | Không áp dụng (N/A) |
| item_id | string | ID bài đăng TikTok (TikTok post ID) | **Lưu ý**: Thẻ sản phẩm không có ID bài đăng. Khi `shop_content_type` là `PRODUCT_CARD`, giá trị của chỉ số này sẽ là `-1`. |
| tt_account_name | string | Tên tài khoản TikTok (TikTok account name) | **Lưu ý**: Nếu access token của bạn thiếu quyền truy cập tài khoản TikTok, giá trị của chỉ số này sẽ là `0` hoặc `-1`. |
| tt_account_profile_image_url | string | URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL) | Không áp dụng (N/A) |
| tt_account_authorization_type | string | Loại ủy quyền (Authorization type) | Các giá trị enum hỗ trợ:<br>• `TTS_TT`: Tài khoản chính thức của TikTok Shop (TikTok Shop official account).<br>• `AFFILIATE`: Ủy quyền hàng loạt qua tiếp thị liên kết (Affiliate mass authorization).<br>• `TT_USER`: Tài khoản doanh nghiệp (Business Account).<br>• `BC_AUTH_TT`: Business Center (Trung tâm Doanh nghiệp).<br>• `AUTH_CODE`: Mã ủy quyền video (Video code).<br>• `UNSET`: Chưa thiết lập (N/A). |
| shop_content_type | string | Loại nội dung cửa hàng (Shop content type) | Các giá trị enum hỗ trợ:<br>• `VIDEO`: Video.<br>• `PRODUCT_CARD`: Thẻ sản phẩm (Product Card). |
| creative_delivery_status | string | Trạng thái phân phối (Status) | Các giá trị enum hỗ trợ:<br>• `IN_QUEUE`: Đang xếp hàng (In queue). Bài đăng đã sẵn sàng để kiểm thử tiềm năng chuyển đổi.<br>• `LEARNING`: Đang học máy (Learning). Bài đăng đang được kiểm thử tiềm năng chuyển đổi.<br>• `DELIVERING`: Đang phân phối (Delivering). Bài đăng được đẩy thường xuyên như một phần chiến dịch.<br>• `NOT_DELIVERYING`: Không phân phối (Not delivering). Bài đăng không thể hiện tiềm năng tốt và sẽ không được đẩy thường xuyên.<br>• `AUTHORIZATION_NEEDED`: Cần ủy quyền (Authorization needed). Video chưa được cấp phép chạy quảng cáo. Bạn có thể tự ủy quyền từ tài khoản TikTok hoặc yêu cầu cấp phép từ nhà sáng tạo khác (cập nhật sau 20 phút).<br>• `EXCLUDED`: Đã loại trừ (Excluded). Bài đăng bị gỡ thủ công khỏi chiến dịch (có thể thêm lại bất kỳ lúc nào).<br>• `UNAVAILABLE`: Không khả dụng (Unavailable). Video riêng tư, bị từ chối, bị xóa hoặc tài khoản bị khóa.<br>• `REJECTED`: Bị từ chối (Rejected). Video bị kiểm duyệt từ chối.<br>• `NOT_ACTIVE`: Không hoạt động (Not active). Đăng quá 30 ngày và không có doanh thu trong 30 ngày qua. |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền bạn đã chi tiêu cho quảng cáo sử dụng video này trong suốt Chiến dịch GMV Max Sản phẩm. Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cost per order) | Chi phí quảng cáo trung bình cho mỗi đơn hàng được đặt trong Chiến dịch GMV Max này, tính theo loại tiền tệ của tài khoản quảng cáo (không bao gồm đơn hàng LIVE), được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó. |
| roi | string | Tỷ suất hoàn vốn đầu tư (ROI) | ROI sản phẩm, được tính bằng tổng doanh số (cả trả phí và tự nhiên) được ghi nhận đóng góp cho Chiến dịch GMV Max đang hoạt động (không bao gồm đơn hàng LIVE) chia cho tổng chi phí quảng cáo.<br>Chỉ số ROI kết hợp cả kết quả GMV tự nhiên và trả phí. Chi phí quảng cáo cao có thể làm giảm ROI tổng thể dù hiệu quả bán hàng tốt. Hãy dùng tổng doanh thu gộp để đánh giá chất lượng video một cách chính xác. |
| product_impressions | string | Lượt hiển thị quảng cáo sản phẩm (Product ad impressions) | Tổng số lượt xem sản phẩm trả phí trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt xem sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_clicks | string | Lượt nhấp quảng cáo sản phẩm (Product ad clicks) | Tổng số lượt nhấp sản phẩm trả phí trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt nhấp sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_click_rate | string | Tỷ lệ nhấp quảng cáo sản phẩm (Product ad click rate) | Tỷ lệ nhấp cho các lượt nhấp sản phẩm trả phí trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này (không bao gồm lượt nhấp LIVE), được tính bằng cách lấy tổng lượt nhấp sản phẩm chia cho tổng lượt xem sản phẩm.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_click_rate | string | Tỷ lệ nhấp quảng cáo (Ad click rate) | Tỷ lệ nhấp (CTR) từ các lượt xem trả phí của video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt xem LIVE trả phí), được tính bằng cách lấy tổng lượt nhấp quảng cáo chia cho tổng lượt xem quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_conversion_rate | string | Tỷ lệ chuyển đổi quảng cáo (Ad conversion rate) | Tỷ lệ chuyển đổi (CVR) của các lượt nhấp trả phí từ video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt nhấp LIVE trả phí), được tính bằng cách lấy tổng lượt chuyển đổi chia cho tổng lượt nhấp.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_2s | string | Tỷ lệ xem video quảng cáo 2 giây (2-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 2 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 2 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_6s | string | Tỷ lệ xem video quảng cáo 6 giây (6-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 6 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 6 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p25 | string | Tỷ lệ xem video quảng cáo đạt 25% (25% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 25% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p50 | string | Tỷ lệ xem video quảng cáo đạt 50% (50% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 50% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p75 | string | Tỷ lệ xem video quảng cáo đạt 75% (75% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 75% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p100 | string | Tỷ lệ xem video quảng cáo đạt 100% (100% ad video view rate) | Tỷ lệ phần trăm số lần video được phát đủ 100% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

**Truy vấn các chỉ số phân phối bằng cách lọc theo nhiều SPU ID**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&metrics=["creative_delivery_status","cost","orders","cost_per_order","gross_revenue","roi","product_impressions","product_clicks","product_click_rate","ad_click_rate","ad_conversion_rate","ad_video_view_rate_2s","ad_video_view_rate_6s","ad_video_view_rate_p25","ad_video_view_rate_p50","ad_video_view_rate_p75","ad_video_view_rate_p100"]&dimensions=["campaign_id","item_group_id","item_id"]&filtering={"campaign_ids":["{{campaign_id}}"],"item_group_ids":["{{item_group_id}}","{{item_group_id}}"]}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
 {
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "item_group_id": "{{item_group_id}}",
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "16.67",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "40.00",
                    "ad_video_view_rate_6s": "40.00",
                    "ad_video_view_rate_p100": "20.00",
                    "ad_video_view_rate_p25": "40.00",
                    "ad_video_view_rate_p50": "20.00",
                    "ad_video_view_rate_p75": "20.00",
                    "creative_delivery_status": "UNAVAILABLE",
                    "currency": "USD",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "orders": "0",
                    "roi": "0.00"
                    "product_click_rate": "16.67",
                    "product_clicks": "1",
                    "product_impressions": "6"
                }
            },
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "item_group_id": "{{item_group_id}}",
                    "item_id": "{{item_id}}0"
                },
                "metrics": {
                    "ad_click_rate": "0.00",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "0.00",
                    "ad_video_view_rate_6s": "0.00",
                    "ad_video_view_rate_p100": "0.00",
                    "ad_video_view_rate_p25": "0.00",
                    "ad_video_view_rate_p50": "0.00",
                    "ad_video_view_rate_p75": "0.00",
                    "creative_delivery_status": "UNAVAILABLE",
                    "currency": "USD",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "orders": "0",
                    "roi": "0.00"
                    "product_click_rate": "0.00",
                    "product_clicks": "0",
                    "product_impressions": "0"
                }
            },
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "item_group_id": "{{item_group_id}}",
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "0.00",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "0.00",
                    "ad_video_view_rate_6s": "0.00",
                    "ad_video_view_rate_p100": "0.00",
                    "ad_video_view_rate_p25": "0.00",
                    "ad_video_view_rate_p50": "0.00",
                    "ad_video_view_rate_p75": "0.00",
                    "creative_delivery_status": "UNAVAILABLE",
                    "currency": "USD",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "orders": "0",
                    "roi": "0.00"
                    "product_click_rate": "0.00",
                    "product_clicks": "0",
                    "product_impressions": "0"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 3,
            "total_page": 1
        }
    }
}
```

---

<a id="mau-quang-cao-tra-phi-va-tu-nhien"></a>
### (Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo trả phí & tự nhiên (For ads and organic creatives)
Chỉ số cấp mẫu quảng cáo trả phí và tự nhiên là các chỉ số áp dụng cho tất cả mẫu quảng cáo đã được ủy quyền và đang được sử dụng chạy quảng cáo. Tổng doanh thu gộp từ video bao gồm doanh số bán hàng từ cả video quảng cáo và video tự nhiên.

Để truy xuất các chỉ số này, hãy đặt trường bộ lọc `creative_types` thành `["ADS_AND_ORGANIC"]`.

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| title | string | Tên mẫu quảng cáo (Creative name) | Không áp dụng (N/A) |
| item_id | string | ID bài đăng TikTok (TikTok post ID) | **Lưu ý**: Thẻ sản phẩm không có ID bài đăng. Khi `shop_content_type` là `PRODUCT_CARD`, giá trị của chỉ số này sẽ là `-1`. |
| tt_account_name | string | Tên tài khoản TikTok (TikTok account name) | **Lưu ý**: Nếu access token của bạn thiếu quyền truy cập tài khoản TikTok, giá trị của chỉ số này sẽ là `0` hoặc `-1`. |
| tt_account_profile_image_url | string | URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL) | Không áp dụng (N/A) |
| tt_account_authorization_type | string | Loại ủy quyền (Authorization type) | Các giá trị enum hỗ trợ:<br>• `TTS_TT`: Tài khoản chính thức của TikTok Shop (TikTok Shop official account).<br>• `AFFILIATE`: Ủy quyền hàng loạt qua tiếp thị liên kết (Affiliate mass authorization).<br>• `TT_USER`: Tài khoản doanh nghiệp (Business Account).<br>• `BC_AUTH_TT`: Business Center (Trung tâm Doanh nghiệp).<br>• `AUTH_CODE`: Mã ủy quyền video (Video code).<br>• `UNSET`: Chưa thiết lập (N/A). |
| shop_content_type | string | Loại nội dung cửa hàng (Shop content type) | Các giá trị enum hỗ trợ:<br>• `VIDEO`: Video.<br>• `PRODUCT_CARD`: Thẻ sản phẩm (Product Card). |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó. |
| product_impressions | string | Lượt hiển thị quảng cáo sản phẩm (Product ad impressions) | Tổng số lượt xem sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt xem sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_clicks | string | Lượt nhấp quảng cáo sản phẩm (Product ad clicks) | Tổng số lượt nhấp sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt nhấp sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_click_rate | string | Tỷ lệ nhấp quảng cáo sản phẩm (Product ad click rate) | Tỷ lệ nhấp cho các lượt nhấp sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này (không bao gồm lượt nhấp LIVE), được tính bằng cách lấy tổng số lượt nhấp sản phẩm chia cho tổng số lượt xem sản phẩm.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_click_rate | string | Tỷ lệ nhấp quảng cáo (Ad click rate) | Tỷ lệ nhấp (CTR) từ các lượt xem trả phí của video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt xem LIVE trả phí), được tính bằng cách lấy tổng lượt nhấp quảng cáo chia cho tổng lượt xem quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_conversion_rate | string | Tỷ lệ chuyển đổi quảng cáo (Ad conversion rate) | Tỷ lệ chuyển đổi (CVR) của các lượt nhấp trả phí từ video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt nhấp LIVE trả phí), được tính bằng cách lấy tổng lượt chuyển đổi chia cho tổng lượt nhấp.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_2s | string | Tỷ lệ xem video quảng cáo 2 giây (2-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 2 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 2 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_6s | string | Tỷ lệ xem video quảng cáo 6 giây (6-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 6 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 6 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p25 | string | Tỷ lệ xem video quảng cáo đạt 25% (25% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 25% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p50 | string | Tỷ lệ xem video quảng cáo đạt 50% (50% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 50% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p75 | string | Tỷ lệ xem video quảng cáo đạt 75% (75% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 75% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p100 | string | Tỷ lệ xem video quảng cáo đạt 100% (100% ad video view rate) | Tỷ lệ phần trăm số lần video được phát đủ 100% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["item_id"]&metrics=["title","item_id","tt_account_name","tt_account_profile_image_url","tt_account_authorization_type","shop_content_type","orders","gross_revenue","product_impressions","product_clicks","product_click_rate","ad_click_rate","ad_conversion_rate","ad_video_view_rate_2s","ad_video_view_rate_6s","ad_video_view_rate_p25","ad_video_view_rate_p50","ad_video_view_rate_p75","ad_video_view_rate_p100"]&filtering={"campaign_ids":["{{campaign_id}}"], "item_group_ids": ["{{item_group_id}}"], "creative_types": ["ADS_AND_ORGANIC"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "0.94",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "11.92",
                    "ad_video_view_rate_6s": "3.97",
                    "ad_video_view_rate_p100": "0.70",
                    "ad_video_view_rate_p25": "7.71",
                    "ad_video_view_rate_p50": "3.27",
                    "ad_video_view_rate_p75": "1.87",
                    "gross_revenue": "0.00",
                    "item_id": "{{item_id}}",
                    "orders": "0",
                    "product_click_rate": "0.94",
                    "product_clicks": "5",
                    "product_impressions": "531",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_authorization_type": "BC_AUTH_TT",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            },
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "0.00",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "8.33",
                    "ad_video_view_rate_6s": "0.00",
                    "ad_video_view_rate_p100": "0.00",
                    "ad_video_view_rate_p25": "0.00",
                    "ad_video_view_rate_p50": "0.00",
                    "ad_video_view_rate_p75": "0.00",
                    "gross_revenue": "0.00",
                    "item_id": "{{item_id}}",
                    "orders": "0",
                    "product_click_rate": "0.00",
                    "product_clicks": "0",
                    "product_impressions": "15",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_authorization_type": "AFFILIATE",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="mau-quang-cao-chi-tu-nhien"></a>
### (Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo chỉ tự nhiên (For organic only creatives)
Chỉ số cấp mẫu quảng cáo chỉ tự nhiên là các chỉ số áp dụng cho các video chỉ nhận lưu lượng truy cập tự nhiên. Tổng doanh thu gộp từ video chỉ bao gồm doanh số bán hàng từ các video tự nhiên.

Để truy xuất các chỉ số này, hãy đặt trường bộ lọc `creative_types` thành `["ORGANIC"]`.

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| title | string | Tên mẫu quảng cáo (Creative name) | Không áp dụng (N/A) |
| item_id | string | ID bài đăng TikTok (TikTok post ID) | Không áp dụng (N/A) |
| tt_account_name | string | Tên tài khoản TikTok (TikTok account name) | Không áp dụng (N/A) |
| tt_account_profile_image_url | string | URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL) | Không áp dụng (N/A) |
| shop_content_type | string | Loại nội dung cửa hàng (Shop content type) | Giá trị enum:<br>• `VIDEO`: Video. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["item_id"]&metrics=["title","item_id","tt_account_name","tt_account_profile_image_url","shop_content_type","orders","gross_revenue"]&filtering={"campaign_ids":["{{campaign_id}}"], "item_group_ids": ["{{item_group_id}}"], "creative_types": ["ORGANIC"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "gross_revenue": "0.00",
                    "item_id": "{{item_id}}",
                    "orders": "0",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            },
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "gross_revenue": "13.56",
                    "item_id": "{{item_id}}",
                    "orders": "2",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="mau-quang-cao-da-bi-go"></a>
### (Sắp ngừng hỗ trợ) Dành cho mẫu quảng cáo đã bị gỡ (For removed creatives)
Chỉ số cấp mẫu quảng cáo đã bị gỡ là các chỉ số dành cho các video được hệ thống tự động chọn nhưng sau đó đã bị bạn gỡ thủ công khỏi chiến dịch.

Để truy xuất các chỉ số này, hãy đặt trường bộ lọc `creative_types` thành `["REMOVED"]`.

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| title | string | Tên mẫu quảng cáo (Creative name) | Không áp dụng (N/A) |
| item_id | string | ID bài đăng TikTok (TikTok post ID) | **Lưu ý**: Thẻ sản phẩm không có ID bài đăng. Khi `shop_content_type` là `PRODUCT_CARD`, giá trị của chỉ số này sẽ là `-1`. |
| tt_account_name | string | Tên tài khoản TikTok (TikTok account name) | **Lưu ý**: Nếu access token của bạn thiếu quyền truy cập tài khoản TikTok, giá trị của chỉ số này sẽ là `0` hoặc `-1`. |
| tt_account_profile_image_url | string | URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL) | Không áp dụng (N/A) |
| tt_account_authorization_type | string | Loại ủy quyền (Authorization type) | Các giá trị enum hỗ trợ:<br>• `TTS_TT`: Tài khoản chính thức của TikTok Shop (TikTok Shop official account).<br>• `AFFILIATE`: Ủy quyền hàng loạt qua tiếp thị liên kết (Affiliate mass authorization).<br>• `TT_USER`: Tài khoản doanh nghiệp (Business Account).<br>• `BC_AUTH_TT`: Business Center (Trung tâm Doanh nghiệp).<br>• `AUTH_CODE`: Mã ủy quyền video (Video code).<br>• `UNSET`: Chưa thiết lập (N/A). |
| shop_content_type | string | Loại nội dung cửa hàng (Shop content type) | Các giá trị enum hỗ trợ:<br>• `VIDEO`: Video.<br>• `PRODUCT_CARD`: Thẻ sản phẩm (Product Card). |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max, không bao gồm các đơn hàng SKU phát sinh từ phiên LIVE. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, không bao gồm đơn hàng LIVE. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp sản phẩm từ nền tảng TikTok Shop dành cho người dùng đó. |
| product_impressions | string | Lượt hiển thị quảng cáo sản phẩm (Product ad impressions) | Tổng số lượt xem sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt xem sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_clicks | string | Lượt nhấp quảng cáo sản phẩm (Product ad clicks) | Tổng số lượt nhấp sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này, không bao gồm lượt nhấp sản phẩm trong phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| product_click_rate | string | Tỷ lệ nhấp quảng cáo sản phẩm (Product ad click rate) | Tỷ lệ nhấp cho các lượt nhấp sản phẩm (cả tự nhiên và trả phí) trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn từ video này (không bao gồm lượt nhấp LIVE), được tính bằng cách lấy tổng số lượt nhấp sản phẩm chia cho tổng số lượt xem sản phẩm.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_click_rate | string | Tỷ lệ nhấp quảng cáo (Ad click rate) | Tỷ lệ nhấp (CTR) từ các lượt xem trả phí của video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt xem LIVE trả phí), được tính bằng cách lấy tổng lượt nhấp quảng cáo chia cho tổng lượt xem quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_conversion_rate | string | Tỷ lệ chuyển đổi quảng cáo (Ad conversion rate) | Tỷ lệ chuyển đổi (CVR) của các lượt nhấp trả phí từ video này trong suốt Chiến dịch GMV Max Sản phẩm cho sản phẩm đã chọn (không bao gồm lượt nhấp LIVE trả phí), được tính bằng cách lấy tổng lượt chuyển đổi chia cho tổng lượt nhấp.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_2s | string | Tỷ lệ xem video quảng cáo 2 giây (2-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 2 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 2 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_6s | string | Tỷ lệ xem video quảng cáo 6 giây (6-second ad video view rate) | Tỷ lệ phần trăm số lần video của bạn được phát ít nhất 6 giây trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn, được tính bằng cách lấy số lượt xem video 6 giây chia cho tổng số lượt xem video. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại (replays).<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p25 | string | Tỷ lệ xem video quảng cáo đạt 25% (25% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 25% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p50 | string | Tỷ lệ xem video quảng cáo đạt 50% (50% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 50% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p75 | string | Tỷ lệ xem video quảng cáo đạt 75% (75% ad video view rate) | Tỷ lệ phần trăm số lần video được phát ít nhất 75% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| ad_video_view_rate_p100 | string | Tỷ lệ xem video quảng cáo đạt 100% (100% ad video view rate) | Tỷ lệ phần trăm số lần video được phát đủ 100% thời lượng trong suốt Chiến dịch GMV Max cho sản phẩm đã chọn trong các lượt xem trả phí. Đối với mỗi lượt xem video, các lần phát được tính riêng và không bao gồm lượt phát lại.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["item_id"]&metrics=["title","item_id","tt_account_name","tt_account_profile_image_url","tt_account_authorization_type","shop_content_type","orders","gross_revenue","product_impressions","product_clicks","product_click_rate","ad_click_rate","ad_conversion_rate","ad_video_view_rate_2s","ad_video_view_rate_6s","ad_video_view_rate_p25","ad_video_view_rate_p50","ad_video_view_rate_p75","ad_video_view_rate_p100"]&filtering={"campaign_ids":["{{campaign_id}}"], "item_group_ids": ["{{item_group_id}}"], "creative_types": ["REMOVED"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "1.02",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "25.00",
                    "ad_video_view_rate_6s": "9.38",
                    "ad_video_view_rate_p100": "1.04",
                    "ad_video_view_rate_p25": "4.17",
                    "ad_video_view_rate_p50": "2.08",
                    "ad_video_view_rate_p75": "2.08",
                    "gross_revenue": "0.00",
                    "item_id": "{{item_id}}",
                    "orders": "0",
                    "product_click_rate": "1.02",
                    "product_clicks": "1",
                    "product_impressions": "98",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_authorization_type": "AFFILIATE",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            },
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "1.73",
                    "ad_conversion_rate": "8.33",
                    "ad_video_view_rate_2s": "35.09",
                    "ad_video_view_rate_6s": "7.67",
                    "ad_video_view_rate_p100": "0.85",
                    "ad_video_view_rate_p25": "5.28",
                    "ad_video_view_rate_p50": "3.24",
                    "ad_video_view_rate_p75": "1.70",
                    "gross_revenue": "0.00",
                    "item_id": "{{item_id}}",
                    "orders": "0",
                    "product_click_rate": "1.73",
                    "product_clicks": "12",
                    "product_impressions": "692",
                    "shop_content_type": "VIDEO",
                    "title": "{{title}}",
                    "tt_account_authorization_type": "AFFILIATE",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="chi-so-cap-khoang-thoi-gian-product"></a>
## Chỉ số cấp khoảng thời gian (Duration-level metrics - Product GMV Max)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất cho từng khoảng thời gian cấu hình của Chiến dịch GMV Max Sản phẩm được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.
- Nếu chế độ tối ưu hóa không thay đổi trong suốt chiến dịch, bạn sẽ thấy một bản ghi duy nhất tương ứng với chế độ tối ưu hóa đã cấu hình.
- Nếu chế độ tối ưu hóa bị thay đổi trong quá trình chạy chiến dịch, bạn sẽ thấy nhiều bản ghi, với mỗi bản ghi tương ứng với một chế độ tối ưu hóa được sử dụng trong giai đoạn đó.

Ví dụ: nếu ban đầu bạn đặt chế độ tối ưu hóa là Mục tiêu ROI (Target ROI) và sau đó chuyển sang Phân phối tối đa (Maximum Delivery), bạn sẽ nhận được 2 bản ghi riêng biệt: một bản ghi cho khoảng thời gian dùng Target ROI và một bản ghi cho khoảng thời gian dùng Maximum Delivery.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp khoảng thời gian cho Chiến dịch GMV Max Sản phẩm, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["duration"]`
- `["campaign_id","duration"]`
- `["item_group_id","duration"]`
- `["campaign_id","item_group_id","duration"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| campaign_ids | Bắt buộc (Required) | 100 | Chỉ định ID của Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `campaign_id` để truy vấn các chỉ số cấp chiến dịch.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |
| item_group_ids | Bắt buộc (Required) | 100 | Chỉ định ID của SPU được sử dụng trong Chiến dịch GMV Max Sản phẩm.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `item_group_id` để truy vấn các chỉ số cấp sản phẩm.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| bid_type | string | Chế độ tối ưu hóa (Optimization mode) | Các giá trị enum hỗ trợ:<br>• `CUSTOM`: Mục tiêu ROI (Target ROI).<br>• `NO_BID`: Phân phối tối đa (Maximum delivery). |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền bạn đã chi tiêu cho quảng cáo cho sản phẩm này trong suốt Chiến dịch GMV Max Sản phẩm, tính theo loại tiền tệ của tài khoản quảng cáo.<br>Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| orders | string | Số lượng đơn hàng SKU (Orders - SKU) | Số lượng đơn hàng SKU riêng lẻ (cả trả phí và tự nhiên) đã hoàn thành trong suốt Chiến dịch GMV Max cho sản phẩm này, không bao gồm các đơn hàng SKU phát sinh từ phiên livestream. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cost per order) | Chi phí quảng cáo trung bình cho mỗi đơn hàng được đặt cho sản phẩm này trong Chiến dịch GMV Max Sản phẩm, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng SKU phát sinh trong khi chiến dịch đang chạy.<br>Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ. |
| gross_revenue | string | Tổng doanh thu (Gross revenue) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop (cả trả phí và tự nhiên) được đặt trong Chiến dịch GMV Max Sản phẩm này, tính theo loại tiền tệ của tài khoản quảng cáo. Đây là số tiền người dùng thanh toán cộng với các khoản trợ cấp giá từ nền tảng TikTok Shop dành cho người dùng đó. |
| roi | string | Tỷ suất hoàn vốn đầu tư (ROI) | ROI sản phẩm, được tính bằng tổng doanh số (cả trả phí và tự nhiên) được ghi nhận đóng góp cho Chiến dịch GMV Max đang hoạt động (không bao gồm đơn hàng LIVE) chia cho tổng chi phí quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["duration"]&metrics=["bid_type", "cost", "orders", "cost_per_order", "gross_revenue", "roi"]&filtering={"campaign_ids":["{{campaign_id}}"], "item_group_ids": ["{{item_group_id}}"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "duration": "{{duration}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "cost": "1428.80",
                    "cost_per_order": "2.62",
                    "gross_revenue": "6141.15",
                    "orders": "545",
                    "roi": "4.30"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 1,
            "total_page": 1
        }
    }
}
```

---

<a id="danh-cho-chien-dich-gmv-max-live"></a>
# Dành cho Chiến dịch GMV Max LIVE (For LIVE GMV Max Campaigns)
Dữ liệu chỉ số báo cáo cho các Chiến dịch GMV Max LIVE liên kết với một TikTok Shop được hỗ trợ ở 3 cấp độ: cấp chiến dịch (campaign), cấp phòng livestream (livestream), và cấp khoảng thời gian (duration).

<a id="chi-so-cap-chien-dich-live"></a>
## Chỉ số cấp chiến dịch (Campaign-level metrics for LIVE GMV Max)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất của các Chiến dịch GMV Max LIVE được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp chiến dịch cho Chiến dịch GMV Max LIVE, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["campaign_id"]`
- `["campaign_id","stat_time_day"]`
- `["campaign_id","stat_time_hour"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| gmv_max_promotion_types | Bắt buộc (Required) | Không áp dụng (N/A) | `["LIVE"]` |
| campaign_ids | Tùy chọn (Optional) | 100 | Chỉ định danh sách ID của các Chiến dịch GMV Max LIVE.<br>Để lấy ID của các Chiến dịch GMV Max LIVE, hãy sử dụng endpoint [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177). Đặt `gmv_max_promotion_types` thành `["LIVE_GMV_MAX"]` và chỉ định ID của TikTok Shop qua tham số `store_ids`. |
| campaign_name | Tùy chọn (Optional) | Không áp dụng (N/A) | Không áp dụng (N/A) |
| campaign_statuses | Tùy chọn (Optional) | Không áp dụng (N/A) | Chỉ định bất kỳ giá trị nào sau đây:<br>• `STATUS_DELIVERY_OK`: Đang hoạt động (Active).<br>• `STATUS_DISABLE`: Tắt/Không hoạt động (Inactive).<br>• `STATUS_DELETE`: Đã xóa (Deleted).<br>• `STATUS_NOT_DELIVERY`: Không phân phối (Not delivering).<br>• `STATUS_ALL`: Tất cả trạng thái (All statuses). |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| campaign_id | string | ID chiến dịch quảng cáo. | Không áp dụng (N/A) |
| operation_status | string | Trạng thái bật/tắt chiến dịch (Campaign on/off status) | Các giá trị enum hỗ trợ:<br>• `ENABLE`: Đang bật (on).<br>• `DISABLE`: Đang tắt (off). |
| campaign_name | string | Tên chiến dịch (Campaign name) | Không áp dụng (N/A) |
| tt_account_name | string | Tên tài khoản TikTok (TikTok account name) | **Lưu ý**: Nếu access token của bạn thiếu quyền truy cập tài khoản TikTok, giá trị của chỉ số này sẽ là `0` hoặc `-1`. |
| tt_account_profile_image_url | string | URL ảnh hồ sơ tài khoản TikTok (TikTok account profile image URL) | Không áp dụng (N/A) |
| identity_id | string | ID danh tính (Identity ID / TikTok account ID) | **Lưu ý**: Nếu access token của bạn thiếu quyền truy cập tài khoản TikTok, giá trị của chỉ số này sẽ là `0` hoặc `-1`. |
| bid_type | string | Chế độ tối ưu hóa (Optimization mode) | Các giá trị enum hỗ trợ:<br>• `CUSTOM`: Mục tiêu ROI (Target ROI).<br>• `NO_BID`: Phân phối tối đa (Maximum delivery). |
| schedule_type | string | Loại lịch chạy (Schedule type) | Giá trị enum:<br>• `Continuously`: Chạy chiến dịch liên tục kể từ thời gian bắt đầu đã lên lịch. |
| schedule_start_time | string | Thời gian bắt đầu theo lịch (Schedule start time) | Múi giờ: UTC+0. |
| schedule_end_time | string | Thời gian kết thúc theo lịch (Schedule end time) | Múi giờ: UTC+0. |
| target_roi_budget | string | Ngân sách mục tiêu ROI (Target ROI budget) | Không áp dụng (N/A) |
| max_delivery_budget | string | Ngân sách phân phối tối đa (Max delivery budget) | Không áp dụng (N/A) |
| roas_bid | string | Mục tiêu ROI (Target ROI) | Không áp dụng (N/A) |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền ước tính bạn đã chi tiêu cho quảng cáo trong suốt lịch chạy, tính theo loại tiền tệ của tài khoản quảng cáo. |
| net_cost | string | Chi phí ròng (Net cost) | Số tiền đã chi tiêu, không bao gồm tín dụng quảng cáo hoặc phiếu giảm giá đã sử dụng, tính theo loại tiền tệ của tài khoản quảng cáo.<br>Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ. Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 01 tháng 09 năm 2023. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cửa hàng hiện tại) (Cost per order - Current shop) | Chi phí trung bình phát sinh cho mỗi đơn hàng được đặt, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| orders | string | Số lượng đơn hàng (Cửa hàng hiện tại) (Orders - Current shop) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| gross_revenue | string | Tổng doanh thu (Cửa hàng hiện tại) (Gross revenue - Current shop) | Tổng doanh thu gộp từ các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp giá từ Cửa hàng dành cho người dùng. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| roi | string | Tỷ suất hoàn vốn đầu tư (Cửa hàng hiện tại) (ROI - Current shop) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| all_shops_cost_per_order | double | Chi phí trên mỗi đơn hàng (Tất cả cửa hàng) (Cost per order - All shops) | Chi phí quảng cáo trung bình cho mỗi đơn hàng LIVE được đặt trong Chiến dịch GMV Max này, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_orders | integer | Số lượng đơn hàng (Tất cả cửa hàng) (Orders - All shops) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_gross_revenue | double | Tổng doanh thu (Tất cả cửa hàng) (Gross revenue - All shops) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max của bạn, tính theo loại tiền tệ của tài khoản quảng cáo. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp từ nền tảng TikTok Shop dành cho người dùng đó.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_roi | double | Tỷ suất hoàn vốn đầu tư (Tất cả cửa hàng) (ROI - All shops) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max này.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| live_views | string | Lượt xem phiên LIVE (LIVE views) | Số lần phiên LIVE của bạn được xem trong suốt Chiến dịch GMV Max. Nhiều lượt xem từ cùng một người dùng được tính riêng biệt.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| cost_per_live_view | string | Chi phí trên mỗi lượt xem LIVE (Cost per LIVE view) | Chi phí trung bình cho mỗi lượt xem LIVE trong suốt Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí chia cho tổng số lượt xem LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| 10_second_live_views | string | Lượt xem LIVE từ 10 giây (10-second LIVE views) | Số lần phiên LIVE của bạn được xem ít nhất 10 giây từ Chiến dịch GMV Max. Nhiều lượt xem từ cùng một người dùng được tính riêng biệt.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| cost_per_10_second_live_view | string | Chi phí trên mỗi lượt xem LIVE 10 giây (Cost per 10-second LIVE view) | Chi phí trung bình cho mỗi lượt xem LIVE từ 10 giây trở lên, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí chia cho tổng số lượt xem LIVE 10 giây.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| live_follows | string | Lượt theo dõi qua phiên LIVE (LIVE follows) | Tổng số người dùng đã nhấn theo dõi trang hồ sơ của bạn trong suốt phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["campaign_id","stat_time_day"]&metrics=["campaign_id", "operation_status", "campaign_name", "tt_account_name", "tt_account_profile_image_url", "identity_id", "bid_type", "schedule_type", "schedule_start_time", "schedule_end_time", "target_roi_budget", "max_delivery_budget", "roas_bid", "cost", "net_cost", "orders", "cost_per_order", "gross_revenue", "roi", "live_views", "cost_per_live_view", "10_second_live_views", "cost_per_10_second_live_view", "live_follows"]&filtering={"gmv_max_promotion_types": ["LIVE"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "10_second_live_views": "739",
                    "bid_type": "CUSTOM",
                    "campaign_id": "{{campaign_id}}",
                    "campaign_name": "{{campaign_name}}",
                    "cost": "57.75",
                    "cost_per_10_second_live_view": "0.08",
                    "cost_per_live_view": "0.01",
                    "cost_per_order": "1.15",
                    "gross_revenue": "313.17",
                    "identity_id": "",
                    "live_follows": "8",
                    "live_views": "4120",
                    "max_delivery_budget": "0.00",
                    "net_cost": "57.75",
                    "operation_status": "ENABLE",
                    "orders": "50",
                    "roas_bid": "5.50",
                    "roi": "5.42",
                    "schedule_end_time": "{{schedule_end_time}}",
                    "schedule_start_time": "{{schedule_start_time}}",
                    "schedule_type": "Continuously",
                    "target_roi_budget": "10000.00",
                    "tt_account_name": "{{tt_account_name}}",
                    "tt_account_profile_image_url": "{{tt_account_profile_image_url}}"
                }
            },
            {
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "10_second_live_views": "0",
                    "bid_type": "CUSTOM",
                    "campaign_id": "{{campaign_id}}",
                    "campaign_name": "{{campaign_name}}",
                    "cost": "0.00",
                    "cost_per_10_second_live_view": "0.00",
                    "cost_per_live_view": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "identity_id": "",
                    "live_follows": "0",
                    "live_views": "0",
                    "max_delivery_budget": "0.00",
                    "net_cost": "0.00",
                    "operation_status": "DISABLE",
                    "orders": "0",
                    "roas_bid": "5.00",
                    "roi": "0.00",
                    "schedule_end_time": "{{schedule_end_time}}1",
                    "schedule_start_time": "{{schedule_start_time}}",
                    "schedule_type": "Continuously",
                    "target_roi_budget": "1000.00",
                    "tt_account_name": "0",
                    "tt_account_profile_image_url": "0"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="chi-so-cap-phong-livestream"></a>
## Chỉ số cấp phòng livestream (Livestream-level metrics)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất cho từng phòng livestream (livestream room) trong Chiến dịch GMV Max LIVE của bạn được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp phòng livestream cho Chiến dịch GMV Max LIVE, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["room_id"]`
- `["room_id","stat_time_day"]`
- `["room_id","stat_time_hour"]`
- `["campaign_id","room_id"]`
- `["campaign_id","room_id","stat_time_day"]`
- `["campaign_id","room_id","stat_time_hour"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| campaign_ids | Bắt buộc (Required) | 100 | Chỉ định ID của Chiến dịch GMV Max LIVE.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `campaign_id` để truy vấn các chỉ số cấp chiến dịch. |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| live_name | string | Tên phiên LIVE (LIVE name) | Không áp dụng (N/A) |
| live_status | string | Trạng thái phiên livestream (Livestream status) | Các giá trị enum hỗ trợ:<br>• `ONGOING`: Đang diễn ra (Ongoing).<br>• `END`: Đã kết thúc (Ended). |
| live_launched_time | string | Thời gian bắt đầu phát livestream (Livestream launched time) | Múi giờ: múi giờ của tài khoản quảng cáo. |
| live_duration | string | Thời lượng phát livestream (Livestream duration) | Không áp dụng (N/A) |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền ước tính bạn đã chi tiêu cho quảng cáo trong suốt lịch chạy, tính theo loại tiền tệ của tài khoản quảng cáo. |
| net_cost | string | Chi phí ròng (Net cost) | Số tiền đã chi tiêu, không bao gồm tín dụng quảng cáo hoặc phiếu giảm giá đã sử dụng, tính theo loại tiền tệ của tài khoản quảng cáo.<br>Lưu ý rằng độ trễ dữ liệu của chỉ số này có thể lên tới 11 giờ. Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 01 tháng 09 năm 2023. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cửa hàng hiện tại) (Cost per order - Current shop) | Chi phí trung bình phát sinh cho mỗi đơn hàng được đặt, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| orders | string | Số lượng đơn hàng (Cửa hàng hiện tại) (Orders - Current shop) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| gross_revenue | string | Tổng doanh thu (Cửa hàng hiện tại) (Gross revenue - Current shop) | Tổng doanh thu gộp từ các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp giá từ Cửa hàng dành cho người dùng. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| roi | string | Tỷ suất hoàn vốn đầu tư (Cửa hàng hiện tại) (ROI - Current shop) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| all_shops_cost_per_order | double | Chi phí trên mỗi đơn hàng (Tất cả cửa hàng) (Cost per order - All shops) | Chi phí quảng cáo trung bình cho mỗi đơn hàng LIVE được đặt trong Chiến dịch GMV Max này, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_orders | integer | Số lượng đơn hàng (Tất cả cửa hàng) (Orders - All shops) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_gross_revenue | double | Tổng doanh thu (Tất cả cửa hàng) (Gross revenue - All shops) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max của bạn, tính theo loại tiền tệ của tài khoản quảng cáo. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp từ nền tảng TikTok Shop dành cho người dùng đó.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_roi | double | Tỷ suất hoàn vốn đầu tư (Tất cả cửa hàng) (ROI - All shops) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max này.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| live_views | string | Lượt xem phiên LIVE (LIVE views) | Số lần phiên LIVE của bạn được xem trong suốt Chiến dịch GMV Max. Nhiều lượt xem từ cùng một người dùng được tính riêng biệt.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| cost_per_live_view | string | Chi phí trên mỗi lượt xem LIVE (Cost per LIVE view) | Chi phí trung bình cho mỗi lượt xem LIVE trong suốt Chiến dịch GMV Max, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí chia cho tổng số lượt xem LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| 10_second_live_views | string | Lượt xem LIVE từ 10 giây (10-second LIVE views) | Số lần phiên LIVE của bạn được xem ít nhất 10 giây từ Chiến dịch GMV Max. Nhiều lượt xem từ cùng một người dùng được tính riêng biệt.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| cost_per_10_second_live_view | string | Chi phí trên mỗi lượt xem LIVE 10 giây (Cost per 10-second LIVE view) | Chi phí trung bình cho mỗi lượt xem LIVE từ 10 giây trở lên, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí chia cho tổng số lượt xem LIVE 10 giây.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| live_follows | string | Lượt theo dõi qua phiên LIVE (LIVE follows) | Tổng số người dùng đã nhấn theo dõi trang hồ sơ của bạn trong suốt phiên LIVE.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["room_id","stat_time_day"]&metrics=["live_name", "live_status", "live_launched_time", "live_duration", "cost", "net_cost", "orders", "cost_per_order", "gross_revenue", "roi", "live_views", "cost_per_live_view", "10_second_live_views", "cost_per_10_second_live_view", "live_follows"]&filtering={"campaign_ids":["{{campaign_id}}"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "room_id": "{{room_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "10_second_live_views": "0",
                    "cost": "0.00",
                    "cost_per_10_second_live_view": "0.00",
                    "cost_per_live_view": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "11.84",
                    "live_duration": "14h 1m",
                    "live_follows": "0",
                    "live_launched_time": "{{live_launched_time}}",
                    "live_name": "{{live_name}}",
                    "live_status": "END",
                    "live_views": "0",
                    "net_cost": "0.00",
                    "orders": "1",
                    "roi": "0.00"
                }
            },
            {
                "dimensions": {
                    "room_id": "{{room_id}}",
                    "stat_time_day": "{{stat_time_day}}"
                },
                "metrics": {
                    "10_second_live_views": "0",
                    "cost": "0.00",
                    "cost_per_10_second_live_view": "0.00",
                    "cost_per_live_view": "0.00",
                    "cost_per_order": "0.00",
                    "gross_revenue": "0.00",
                    "live_duration": "11h 29m",
                    "live_follows": "0",
                    "live_launched_time": "{{live_launched_time}}",
                    "live_name": "{{live_name}}",
                    "live_status": "END",
                    "live_views": "0",
                    "net_cost": "0.00",
                    "orders": "0",
                    "roi": "0.00"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="chi-so-cap-khoang-thoi-gian-live"></a>
## Chỉ số cấp khoảng thời gian (Duration-level metrics - LIVE GMV Max)
Các chỉ số này hiển thị các thuộc tính cơ bản và hiệu suất cho từng khoảng thời gian cấu hình của Chiến dịch GMV Max LIVE được tạo trên TikTok Ads Manager hoặc TikTok Seller Center.
- Nếu chế độ tối ưu hóa không đổi trong suốt chiến dịch, bạn sẽ thấy một bản ghi duy nhất tương ứng với chế độ tối ưu hóa đã cấu hình.
- Nếu chế độ tối ưu hóa bị thay đổi trong quá trình chạy, bạn sẽ thấy nhiều bản ghi, với mỗi bản ghi tương ứng với một chế độ tối ưu hóa được sử dụng trong giai đoạn đó.

Ví dụ: nếu ban đầu bạn đặt chế độ tối ưu hóa là Mục tiêu ROI (Target ROI) và sau đó chuyển sang Phân phối tối đa (Maximum Delivery), bạn sẽ nhận được 2 bản ghi riêng biệt: một bản ghi cho khoảng thời gian dùng Target ROI và một bản ghi cho khoảng thời gian dùng Maximum Delivery.

**Nhóm chiều dữ liệu được hỗ trợ (Supported dimension groupings)**

Để truy xuất các chỉ số cấp khoảng thời gian cho Chiến dịch GMV Max LIVE, hãy chỉ định bất kỳ nhóm chiều nào sau đây bằng tham số `dimensions`:
- `["duration"]`
- `["campaign_id","duration"]`
- `["room_id","duration"]`
- `["campaign_id","room_id","duration"]`

**Bộ lọc được hỗ trợ (Supported filters)**

| Filter field (Trường bộ lọc) | Bắt buộc/Tùy chọn (Required/Optional) | Kích thước tối đa (Max size) | Yêu cầu (Requirement) |
|---|---|---|---|
| campaign_ids | Bắt buộc (Required) | 100 | Chỉ định ID của Chiến dịch GMV Max LIVE.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `campaign_id` để truy vấn các chỉ số cấp chiến dịch.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |
| room_ids | Bắt buộc (Required) | 100 | Chỉ định ID của phòng livestream được sử dụng trong Chiến dịch GMV Max LIVE.<br>Để lấy ID này, trước tiên hãy sử dụng chiều `room_id` để truy vấn các chỉ số cấp phòng livestream.<br>**Lưu ý**: Khi bạn lọc nhiều ID bằng trường này, bạn sẽ không thể truy xuất các chỉ số thuộc tính. |

**Chỉ số được hỗ trợ (Supported metrics)**

| Metric field (Trường chỉ số) | Kiểu (Type) | Mô tả (Description) | Chi tiết (Detail) |
|---|---|---|---|
| bid_type | string | Chế độ tối ưu hóa (Optimization mode) | Các giá trị enum hỗ trợ:<br>• `CUSTOM`: Mục tiêu ROI (Target ROI).<br>• `NO_BID`: Phân phối tối đa (Maximum delivery). |
| cost | string | Chi phí quảng cáo (Cost) | Tổng số tiền ước tính bạn đã chi tiêu cho quảng cáo trong suốt lịch chạy, tính theo loại tiền tệ của tài khoản quảng cáo. |
| cost_per_order | string | Chi phí trên mỗi đơn hàng (Cửa hàng hiện tại) (Cost per order - Current shop) | Chi phí trung bình phát sinh cho mỗi đơn hàng được đặt, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| orders | string | Số lượng đơn hàng (Cửa hàng hiện tại) (Orders - Current shop) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| gross_revenue | string | Tổng doanh thu (Cửa hàng hiện tại) (Gross revenue - Current shop) | Tổng doanh thu gộp từ các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp giá từ Cửa hàng dành cho người dùng. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| roi | string | Tỷ suất hoàn vốn đầu tư (Cửa hàng hiện tại) (ROI - Current shop) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng Cửa hàng được ghi nhận đóng góp cho chiến dịch của bạn. Chỉ tính các đơn hàng từ cửa hàng hiện tại của bạn, ngay cả khi phiên livestream có quảng bá sản phẩm từ các cửa hàng khác. |
| all_shops_cost_per_order | double | Chi phí trên mỗi đơn hàng (Tất cả cửa hàng) (Cost per order - All shops) | Chi phí quảng cáo trung bình cho mỗi đơn hàng LIVE được đặt trong Chiến dịch GMV Max này, tính theo loại tiền tệ của tài khoản quảng cáo, được tính bằng cách lấy tổng chi phí quảng cáo chia cho số lượng đơn hàng được tạo trong lịch chạy quảng cáo.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_orders | integer | Số lượng đơn hàng (Tất cả cửa hàng) (Orders - All shops) | Số lượng đơn hàng SKU LIVE riêng lẻ (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_gross_revenue | double | Tổng doanh thu (Tất cả cửa hàng) (Gross revenue - All shops) | Tổng doanh thu gộp từ các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max của bạn, tính theo loại tiền tệ của tài khoản quảng cáo. Đây là số tiền người dùng thanh toán cộng với tất cả các khoản trợ cấp từ nền tảng TikTok Shop dành cho người dùng đó.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |
| all_shops_roi | double | Tỷ suất hoàn vốn đầu tư (Tất cả cửa hàng) (ROI - All shops) | Tổng tỷ suất hoàn vốn đầu tư (ROI) từ tất cả các đơn hàng TikTok Shop LIVE (cả trả phí và tự nhiên) trong suốt Chiến dịch GMV Max này.<br>Dữ liệu chiến dịch cho chỉ số này khả dụng từ ngày 27 tháng 09 năm 2024. |

**Ví dụ minh họa (Example)**

Yêu cầu gọi (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date={{start_date}}&end_date={{end_date}}&dimensions=["duration"]&metrics=["bid_type", "cost", "orders", "cost_per_order", "gross_revenue", "roi"]&filtering={"campaign_ids":["{{campaign_id}}"],"room_ids":["{{room_id}}"]}&page_size=1000&page=1' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "duration": "{{duration}}"
                },
                "metrics": {
                    "bid_type": "CUSTOM",
                    "cost": "763.83",
                    "cost_per_order": "1.43",
                    "gross_revenue": "3749.91",
                    "orders": "535",
                    "roi": "4.91"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 1,
            "total_page": 1
        }
    }
}
```

---

<a id="ma-nguon-mau-truy-xuat-du-lieu"></a>
## 5. Mã nguồn mẫu truy xuất dữ liệu (Data Retrieval - Python & cURL)

### cURL truy vấn báo cáo chiến dịch GMV Max
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id=YOUR_ADVERTISER_ID&report_type=CAMPAIGN&start_date=2026-03-01&end_date=2026-03-07&metrics=%5B%22cost%22%2C%22all_shops_gross_revenue%22%2C%22all_shops_roi%22%2C%22all_shops_orders%22%5D" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script trích xuất dữ liệu GMV Max
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {"Access-Token": ACCESS_TOKEN}

def get_gmv_max_report(advertiser_id, start_date, end_date):
    """Truy vấn các chỉ số doanh thu và ROI của chiến dịch GMV Max."""
    url = f"{BASE_URL}/gmv_max/report/get/"
    params = {
        "advertiser_id": advertiser_id,
        "report_type": "CAMPAIGN",
        "start_date": start_date,
        "end_date": end_date,
        "metrics": json.dumps([
            "cost",
            "all_shops_gross_revenue",
            "all_shops_roi",
            "all_shops_orders",
            "all_shops_cost_per_order"
        ])
    }
    
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        records = res.get("data", {}).get("list", [])
        print(f"Lấy thành công {len(records)} dòng số liệu:")
        for r in records:
            print(f" - Chiến dịch: {r.get('campaign_name')} | Chi phí: {r.get('cost')} | Doanh thu: {r.get('all_shops_gross_revenue')} | ROI: {r.get('all_shops_roi')}")
        return records
    else:
        print(f"Lỗi truy vấn: {res.get('code')} - {res.get('message')}")
        return []

if __name__ == "__main__":
    get_gmv_max_report(ADVERTISER_ID, "2026-03-01", "2026-03-07")
```
