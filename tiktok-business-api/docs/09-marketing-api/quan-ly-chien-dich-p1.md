# Hướng dẫn quản lý chiến dịch — phần 1/2

Tài liệu này cung cấp hướng dẫn toàn diện về cấu trúc quảng cáo và quản lý chiến dịch thông qua TikTok Marketing API (phần 1/2). Bạn sẽ tìm hiểu về hệ thống phân cấp 3 cấp độ (Chiến dịch, Nhóm quảng cáo, Quảng cáo), bảng đối chiếu giữa giao diện TikTok Ads Manager và các tham số gọi API, quy trình khởi tạo và sao chép chiến dịch thủ công cũng như chiến dịch Upgraded Smart+. Tài liệu cũng trình bày chi tiết về các mục tiêu quảng cáo, chiến dịch Reach & Frequency, TopView, Dedicated Campaign cho iOS 14/SKAN 4.0, Super Split Test và các quy tắc thiết lập ngân sách đa tiền tệ.

## Quản lý chiến dịch (`Campaign Management`)
<a id="doc-1735713781404673"></a>
<!-- doc_id: 1735713781404673 -->

> Đường dẫn: Marketing API > Campaign Management

Bạn có thể sử dụng Campaign Management API để thiết lập và quản lý các chiến dịch (campaigns), nhóm quảng cáo (ad groups) và quảng cáo (ads) của mình.

> [!IMPORTANT]
> Để tìm hiểu chi tiết về việc tạo quảng cáo qua API theo từng trường hợp cụ thể, vui lòng tham khảo [Các tình huống sử dụng (Use Cases)](../08-use-cases/use-cases.md#doc-1735713713137730).

- Để tìm hiểu về cấu trúc chiến dịch và quy trình làm việc chung, xem [Tổng quan (Overview)](quan-ly-chien-dich-p1.md#doc-1737585544915970).
- Để tìm hiểu về các thiết lập chính và tính năng ở cấp chiến dịch, nhóm quảng cáo và quảng cáo, xem [Hướng dẫn quy trình (Guides)](quan-ly-chien-dich-p1.md#doc-1739381695768577). **Xem thêm** [tại đây](quan-ly-chien-dich-p1.md#doc-1740673047618561) để tìm hiểu mối quan hệ ánh xạ giữa các tính năng trên TikTok Ads Manager và cấu hình API.
- [Chiến dịch (Campaign)](quan-ly-chien-dich-p1.md#doc-1745292231199745): Chiến dịch là cấp độ cao nhất của quảng cáo. Để quảng bá trên TikTok for Business, trước tiên bạn cần tạo một chiến dịch và thiết lập mục tiêu quảng cáo của mình.

### Các tình huống sử dụng liên quan (Related use cases)
- [Tạo Quảng cáo Mua sắm (Shopping Ads)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942179356738)
- [Tạo Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298)
- [Tạo quảng cáo Thu thập khách hàng tiềm năng (Lead Generation)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1739470742024193)
- [Tạo quảng cáo hình ảnh đơn (Single image ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1777633230937090)
- [Tạo quảng cáo xoay vòng (Carousel Ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713)
- [Tạo chiến dịch Upgraded Smart+](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1843309449749698)
- [Tạo quảng cáo Tìm kiếm (Search Ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1780164603696130)
- [Thiết lập chiến dịch Tiếp cận & Tần suất (Reach & Frequency)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1758528372513794)

## Tổng quan (`Overview`)
<a id="doc-1737585544915970"></a>
<!-- doc_id: 1737585544915970 -->

> Đường dẫn: Marketing API > Campaign Management > Overview

Bài viết này cung cấp cái nhìn tổng quan về quản lý chiến dịch quảng cáo.

Bạn có thể sử dụng Campaign Management API để thúc đẩy hiệu suất chiến dịch, nâng cao hiệu quả vận hành, khả năng mở rộng quy mô và đạt được các mục tiêu kinh doanh đã đề ra.

## Cấu trúc quảng cáo (`Ads structure`)
<a id="doc-1739381193120770"></a>
<!-- doc_id: 1739381193120770 -->

> Đường dẫn: Marketing API > Campaign Management > Overview > Ads structure

Cấu trúc quảng cáo của TikTok bao gồm 3 cấp độ phân cấp:

* **Chiến dịch (Campaign):** Cấp độ cao nhất trong cấu trúc quảng cáo, được dùng để thiết lập mục tiêu quảng cáo chung. Một tài khoản quảng cáo có thể có tối đa 999 chiến dịch (không bao gồm [chiến dịch Promote](quan-ly-chien-dich-p1.md#doc-1785880454546433)), và mỗi chiến dịch có thể chứa tối đa 999 nhóm quảng cáo.
* **Nhóm quảng cáo (Ad group):** Cấp độ trung gian, được dùng để lên kế hoạch phân phối các quảng cáo chiến lược. Một nhóm quảng cáo có thể chứa tối đa 20 hoặc 50 quảng cáo:
  - Nếu [mục tiêu quảng cáo](quan-ly-chien-dich-p1.md#doc-1737585562434561) của chiến dịch là `RF_REACH`, nhóm quảng cáo chỉ có thể chứa tối đa **20** quảng cáo.
  - Nếu mục tiêu quảng cáo là `PRODUCT_SALES`, nhóm quảng cáo có thể chứa tối đa **20** quảng cáo (khi `campaign_product_source` là `STORE`) hoặc **50** quảng cáo (khi `campaign_product_source` là `CATALOG`).
  - Nếu mục tiêu quảng cáo **không phải** là `PRODUCT_SALES` hoặc `RF_REACH`, nhóm quảng cáo có thể chứa tối đa **50** quảng cáo.
* **Quảng cáo (Ad):** Đơn vị quảng cáo nhỏ nhất, quyết định thông tin nội dung sáng tạo sẽ được hiển thị đến người dùng.

### Chiến dịch (Campaign)
Tạo chiến dịch là bước đầu tiên, nơi bạn thiết lập mục tiêu quảng cáo và ngân sách chiến dịch. Xem chi tiết tại [Tạo chiến dịch](quan-ly-chien-dich-p1.md#doc-1737719523561474).

### Nhóm quảng cáo (Ad group)
Ở cấp nhóm quảng cáo, bạn có thể thiết lập các cấu hình sau cho các quảng cáo thuộc nhóm. Xem chi tiết tại [Tạo nhóm quảng cáo](quan-ly-chien-dich-p2.md#doc-1738857874837506):
- Vị trí hiển thị quảng cáo (Ad placement)
- Tệp đối tượng mục tiêu (Target audience)
- Thiết lập ngân sách (Budget settings)
- Lịch phân phối quảng cáo (Ad delivery schedule)
- Mục tiêu tối ưu hóa (Optimization goal)
- Chiến lược giá thầu (Bidding strategies)

> [!NOTE]
> - Mục tiêu quảng cáo đặt ở cấp chiến dịch sẽ ảnh hưởng trực tiếp đến mục tiêu tối ưu hóa, phương thức đấu thầu và tối ưu hóa ở cấp nhóm quảng cáo. Khi thêm quảng cáo vào chiến dịch, hệ thống đảm bảo tất cả quảng cáo trong cùng chiến dịch đều có chung mục tiêu quảng cáo.
> - Tùy thuộc vào quốc gia hoặc khu vực đăng ký tài khoản quảng cáo, các vị trí hiển thị và địa điểm phân phối có thể khác nhau.
> - Để đảm bảo tính toàn vẹn dữ liệu, cơ chế khóa lạc quan (optimistic locking) được áp dụng khi tạo hoặc cập nhật tài nguyên Tối ưu hóa Sáng tạo Tự động (ACO). Nếu gặp thông báo lỗi khóa lạc quan, hãy thực hiện tuần tự các yêu cầu hoặc giảm tần suất gọi API.

### Quảng cáo (Ad)
Quảng cáo là nội dung được trình bày trực tiếp tới đối tượng mục tiêu, bao gồm video hoặc hình ảnh, văn bản quảng cáo và nút kêu gọi hành động (CTA). Xem chi tiết tại [Tạo quảng cáo](quan-ly-chien-dich-p2.md#doc-1745292553358338).

## Hướng dẫn quy trình (`Guides`)
<a id="doc-1739381695768577"></a>
<!-- doc_id: 1739381695768577 -->

> Đường dẫn: Marketing API > Campaign Management > Guides

Các hướng dẫn này sẽ dẫn dắt bạn qua các bước thực hiện các tác vụ phổ biến để quản lý chiến dịch, nhóm quảng cáo và quảng cáo của mình:
- [Chiến dịch (Campaign)](quan-ly-chien-dich-p1.md#doc-1745292231199745): Cấp độ cao nhất của quảng cáo trên TikTok for Business.
  - [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458): Lợi ích của chiến dịch Upgraded Smart+.
  - [Sao chép chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1866529015923713): Cách sao chép chiến dịch Upgraded Smart+.
- [Mục tiêu quảng cáo (Advertising objective)](quan-ly-chien-dich-p1.md#doc-1737585562434561): Giới thiệu các mục tiêu quảng cáo được hỗ trợ cho quảng cáo đấu giá và quảng cáo Reach & Frequency.
- [Tiếp cận & Tần suất (Reach & Frequency)](quan-ly-chien-dich-p1.md#doc-1739470723315713): Cách tạo và quản lý chiến dịch Reach & Frequency.
  - [TopView](quan-ly-chien-dich-p1.md#doc-1804258360285186): Giới thiệu về quảng cáo TopView trong API.
  - [Dedicated Campaign](quan-ly-chien-dich-p1.md#doc-1740029173531649): Giới thiệu chiến dịch chuyên dụng iOS 14 và SKAN 4.0, các bước tạo và truy xuất.
  - [Super Split Testing](quan-ly-chien-dich-p1.md#doc-1742668394531842): Thử nghiệm phân tách và [tình huống sử dụng](quan-ly-chien-dich-p1.md#doc-1742668948278274).
  - [Ngân sách (Budget)](quan-ly-chien-dich-p1.md#doc-1739381246298114): Các chế độ và sự kết hợp ngân sách ở cấp chiến dịch và nhóm quảng cáo.
  - [Chiến dịch Promote](quan-ly-chien-dich-p1.md#doc-1785880454546433): Trạng thái, bộ lọc và dữ liệu báo cáo cho quảng cáo Promote.
  - [Realtime API (RTA)](quan-ly-chien-dich-p2.md#doc-1805437148769281): Kích hoạt Realtime API cho quảng cáo.
  - [Tạo chiến dịch thủ công](quan-ly-chien-dich-p1.md#doc-1737719523561474): Các bước tạo Manual Campaign.
  - [Sao chép chiến dịch thủ công](quan-ly-chien-dich-p1.md#doc-1788434533212162): Các bước sao chép Manual Campaign.
- [Nhóm quảng cáo (Ad group)](quan-ly-chien-dich-p2.md#doc-1745292233615362): Cấu hình vị trí, đối tượng, ngân sách, lịch trình và giá thầu.
  - [Tạo nhóm quảng cáo](quan-ly-chien-dich-p2.md#doc-1738857874837506): Quy trình tạo ad group.
  - [Vị trí hiển thị (Placements)](quan-ly-chien-dich-p2.md#doc-1745292441739265): Các loại vị trí hiển thị được hỗ trợ.
  - [Nhắm mục tiêu (Targeting)](quan-ly-chien-dich-p2.md#doc-1745292439329793): Nhắm mục tiêu theo đối tượng và theo ngữ cảnh.
  - [An toàn thương hiệu (Brand safety)](quan-ly-chien-dich-tom-tat.md#doc-1739381752981505): Các giải pháp bảo vệ uy tín thương hiệu trực tuyến.
  - [Sự kiện chuyển đổi (Conversion events)](quan-ly-chien-dich-p2.md#doc-1739361474981889): Bảng giá trị enum cho sự kiện chuyển đổi.
  - [Đấu thầu (Bidding)](quan-ly-chien-dich-p2.md#doc-1745292444424193): Chiến lược đặt giá thầu và tối ưu hóa giá trị (Value optimization).
  - [Cửa sổ phân bổ và cách tính sự kiện](quan-ly-chien-dich-tom-tat.md#doc-1777694366654465): Thiết lập cửa sổ phân bổ nhấp chuột/lượt xem.
  - [Trạng thái phụ được hỗ trợ](quan-ly-chien-dich-tom-tat.md#doc-1757239620352002): Danh sách trạng thái phụ tương ứng với trạng thái chính.
  - [Ước tính kết quả phân phối (EDR)](quan-ly-chien-dich-p1.md#doc-1742668394531842): Đề xuất giá thầu và ngân sách để cải thiện hiệu suất.
- [Quảng cáo (Ad)](quan-ly-chien-dich-p2.md#doc-1745292235571201): Nội dung hiển thị tới người dùng.
  - [Tạo quảng cáo](quan-ly-chien-dich-p2.md#doc-1745292553358338): Hướng dẫn tạo ad.
  - [Smart Creative](quan-ly-chien-dich-p2.md#doc-1767322784934914): Cách sử dụng Smart Creative.
  - [Danh tính (Identities)](quan-ly-chien-dich-p2.md#doc-1738958351620097): Danh tính được ủy quyền và các endpoint liên quan.
  - [Deeplink](quan-ly-chien-dich-tom-tat.md#doc-1779541971843073): Các loại liên kết sâu và cơ chế dự phòng (fallback).
  - [Trang sản phẩm tùy chỉnh (Custom Product Pages)](quan-ly-chien-dich-tom-tat.md#doc-1798658439859202): Áp dụng CPP trong quảng cáo iOS.
  - [Nút tự công bố nội dung do AI tạo (AIGC)](quan-ly-chien-dich-p2.md#doc-1799186631031809): Công bố nội dung nhân tạo AI.
  - [Tự động nâng cao (Automatic Enhancements)](quan-ly-chien-dich-p2.md#doc-1855450880142402): Tự động cải thiện chất lượng quảng cáo.

## Ánh xạ giữa tính năng TikTok Ads Manager và cấu hình API (`Mapping between campaign features in TikTok Ads Manager and API configurations`)
<a id="doc-1740673047618561"></a>
<!-- doc_id: 1740673047618561 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Mapping between campaign features in TikTok Ads Manager and API configurations

Bài viết này cung cấp bảng ánh xạ giữa các tính năng trên giao diện TikTok Ads Manager (TTAM) ở cả 3 cấp độ (Chiến dịch, Nhóm quảng cáo, Quảng cáo) và các cấu hình tham số API tương ứng.

### 1. Cấp chiến dịch (Campaign level)
Để tạo chiến dịch, sử dụng endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).

| Phân hệ TTAM | Thiết lập TTAM | Cấu hình API tương ứng |
|---|---|---|
| Mục tiêu quảng cáo | Advertising objective | `objective_type` |
| Mục tiêu quảng cáo | Doanh số (Sales) | `virtual_objective_type` (xem [Nâng cấp lên mục tiêu Sales](quan-ly-chien-dich-p1.md#doc-1834189985160193)) |
| Điểm đến bán hàng | Sales destination | `sales_destination` |
| Loại chiến dịch | App promotion type | `app_promotion_type` |
| Chiến dịch Smart+ | Smart+ campaign | Sử dụng [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) |
| Chiến dịch chuyên dụng | iOS 14 dedicated campaign | `campaign_type` |
| Ứng dụng | App | `app_id` |
| Tối ưu hóa ngân sách chiến dịch | Campaign Budget Optimization (CBO) | `budget_optimize_switch` |
| Ngân sách chiến dịch | Campaign budget | `budget` và `budget_mode` (`BUDGET_MODE_DAY` hoặc `BUDGET_MODE_TOTAL`) |

### 2. Cấp nhóm quảng cáo (Ad group level)
Để tạo nhóm quảng cáo, sử dụng endpoint [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).

| Phân hệ TTAM | Thiết lập TTAM | Cấu hình API tương ứng |
|---|---|---|
| Vị trí hiển thị | Placements (Tự động / Thủ công) | `placement_type` (`PLACEMENT_TYPE_AUTOMATIC` hoặc `PLACEMENT_TYPE_NORMAL`), `placements` |
| Nhắm mục tiêu | Địa điểm (Location) | `location_ids` |
| Nhắm mục tiêu | Giới tính (Gender) | `gender` |
| Nhắm mục tiêu | Độ tuổi (Age) | `age_groups` |
| Nhắm mục tiêu | Ngôn ngữ (Languages) | `languages` |
| Tệp đối tượng | Đối tượng tùy chỉnh / Đối tượng tương tự | `audience_ids`, `excluded_audience_ids` |
| Ngân sách & Lịch trình | Ngân sách nhóm quảng cáo | `budget`, `budget_mode` |
| Ngân sách & Lịch trình | Lịch chạy và khung giờ | `schedule_type`, `schedule_start_time`, `schedule_end_time`, `dayparting` |
| Đấu thầu & Tối ưu hóa | Mục tiêu tối ưu hóa (Optimization Goal) | `optimization_goal` |
| Đấu thầu & Tối ưu hóa | Chiến lược giá thầu (Bidding Strategy) | `bid_type`, `bid_price` |
| Cửa sổ phân bổ | Attribution window | `attribution_window_type` |

### 3. Cấp quảng cáo (Ad level)
Để tạo quảng cáo, sử dụng endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

| Phân hệ TTAM | Thiết lập TTAM | Cấu hình API tương ứng |
|---|---|---|
| Định dạng quảng cáo | Ad format | `ad_format` |
| Nội dung sáng tạo | Video / Hình ảnh | `video_id`, `image_ids` |
| Văn bản quảng cáo | Ad text | `ad_name`, `text` |
| Lời kêu gọi hành động | Call to action (CTA) | `call_to_action`, `call_to_action_id` |
| Danh tính | Identity (Spark Ads / Custom) | `identity_type`, `identity_id`, `identity_authorized_bc_id` |
| Trang đích | Landing Page URL / Deeplink | `landing_page_url`, `deeplink`, `deeplink_type` |
| Theo dõi | Tracking URLs (Impression / Click) | `tracking_pixel_id`, `impression_tracking_url`, `click_tracking_url` |


## Chiến dịch (`Campaign`)
<a id="doc-1745292231199745"></a>
<!-- doc_id: 1745292231199745 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign

Chiến dịch là cấp độ cao nhất của cấu trúc quảng cáo. Để quảng bá trên TikTok for Business, trước tiên bạn cần tạo một chiến dịch và thiết lập mục tiêu quảng cáo phù hợp.

Khám phá các tài nguyên sau để tìm hiểu chi tiết về các loại chiến dịch trên TikTok for Business:
- [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458): Lợi ích của chiến dịch Upgraded Smart+.
- [Sao chép chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1866529015923713): Cách sao chép chiến dịch Upgraded Smart+.
- [Mục tiêu quảng cáo (Advertising objective)](quan-ly-chien-dich-p1.md#doc-1737585562434561): Các mục tiêu quảng cáo đấu giá và quảng cáo Reach & Frequency.
- [Tiếp cận & Tần suất (Reach & Frequency)](quan-ly-chien-dich-p1.md#doc-1739470723315713): Tạo và quản lý chiến dịch Reach & Frequency.
- [TopView](quan-ly-chien-dich-p1.md#doc-1804258360285186): Giới thiệu về quảng cáo TopView trong API.
- [Dedicated Campaign](quan-ly-chien-dich-p1.md#doc-1740029173531649): Chiến dịch chuyên dụng iOS 14 và SKAN 4.0.
- [Super Split Test](quan-ly-chien-dich-p1.md#doc-1742668394531842): Thử nghiệm phân tách và [tình huống sử dụng](quan-ly-chien-dich-p1.md#doc-1742668948278274).
- [Ngân sách (Budget)](quan-ly-chien-dich-p1.md#doc-1739381246298114): Các chế độ và sự kết hợp ngân sách chiến dịch và nhóm quảng cáo.
- [Chiến dịch Promote](quan-ly-chien-dich-p1.md#doc-1785880454546433): Trạng thái, bộ lọc và báo cáo quảng cáo Promote.
- [Realtime API (RTA)](quan-ly-chien-dich-p2.md#doc-1805437148769281): Kích hoạt Realtime API cho quảng cáo.
- [Tạo chiến dịch thủ công](quan-ly-chien-dich-p1.md#doc-1737719523561474): Quy trình tạo Manual Campaign.
- [Sao chép chiến dịch thủ công](quan-ly-chien-dich-p1.md#doc-1788434533212162): Quy trình sao chép Manual Campaign.

## Tạo chiến dịch thủ công (`Create a Manual Campaign`)
<a id="doc-1737719523561474"></a>
<!-- doc_id: 1737719523561474 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Create a Manual Campaign

Bài viết này hướng dẫn cách tạo chiến dịch thủ công thông thường.

### Các bước thực hiện (Steps)
Sử dụng endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) để tạo chiến dịch thông thường. Bạn có thể định nghĩa các thiết lập sau ở cấp chiến dịch:
- `advertiser_id`: ID tài khoản quảng cáo của bạn.
- `campaign_name`: Tên mang tính mô tả của chiến dịch.
- `objective_type`: Mục tiêu quảng cáo của chiến dịch. Xem [Mục tiêu quảng cáo](quan-ly-chien-dich-p1.md#doc-1737585562434561).
- `budget_mode`: Chế độ ngân sách bao gồm ngân sách tổng (`BUDGET_MODE_TOTAL`), ngân sách ngày (`BUDGET_MODE_DAY`), ngân sách ngày động (`BUDGET_MODE_DYNAMIC_DAILY_BUDGET`) hoặc không giới hạn (`BUDGET_MODE_INFINITE`).
- `budget`: Số tiền ngân sách nếu `budget_mode` là tổng, ngày hoặc ngày động.
- `budget_optimize_on`: Bật tính năng Tối ưu hóa ngân sách chiến dịch (CBO) (`TRUE`/`FALSE`). Khi bật CBO, bạn cần đặt `budget_mode` và `budget` ở cấp chiến dịch.

### Bước tiếp theo (Next step)
[Tạo nhóm quảng cáo](quan-ly-chien-dich-p2.md#doc-1738857874837506).

## Sao chép chiến dịch thủ công (`Copy a Manual Campaign`)
<a id="doc-1788434533212162"></a>
<!-- doc_id: 1788434533212162 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Copy a Manual Campaign

Bài viết này hướng dẫn cách sao chép chiến dịch thủ công (Manual Campaign). Để sao chép chiến dịch Upgraded Smart+, xem [Sao chép chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1866529015923713).

### Giới thiệu (Introduction)
Tính năng sao chép chiến dịch cho phép bạn nhân bản nhanh chóng toàn bộ chiến dịch thủ công, bao gồm nhiều nhóm quảng cáo và quảng cáo.

**Bạn có thể sử dụng Asynchronous Campaign Copy API để sao chép chiến dịch thủ công đồng thời điều chỉnh các thiết lập ở cấp chiến dịch, nhóm quảng cáo và quảng cáo theo nhu cầu, tiết kiệm thời gian vận hành.**

### Điều kiện tiên quyết (Prerequisites)
- Đã được cấp quyền truy cập TikTok API for Business.
- Asynchronous Campaign Copy API hiện là tính năng cho danh sách cho phép (allowlist-only). Vui lòng liên hệ đại diện TikTok nếu muốn đăng ký.
- Tài khoản quảng cáo đã có sẵn các chiến dịch hợp lệ để nhân bản.

### Các bước thực hiện (Steps)

1. **Xác định các chiến dịch, nhóm quảng cáo và quảng cáo cần sao chép:**
   - Lọc chiến dịch hợp lệ bằng **/campaign/get/**.
   - Lọc nhóm quảng cáo bằng **/adgroup/get/**.
   - Lọc quảng cáo bằng [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770).

2. **Tạo tác vụ sao chép chiến dịch bất đồng bộ:** Gọi endpoint [/campaign/copy/task/create/](../12-api-reference/24-campaign.md#doc-1788434394151938).
   - Cung cấp `campaign_id`, `advertiser_id`, `request_id`, và tùy chọn tùy biến `operation_status`, `campaign_name`, `budget`.
   - Chọn chế độ sao chép qua `deep_copy_mode`:
     - **Default copy mode (`DEFAULT`):** Sao chép toàn bộ các nhóm quảng cáo và quảng cáo chưa bị xóa.
     - **Custom copy mode (`CUSTOM`):** Chỉ sao chép các nhóm quảng cáo và quảng cáo được chỉ định trong `adgroup_list` và `ad_list`.

Bảng các thiết lập có thể tùy biến khi sao chép:

| Level | Customizable settings |
|---|---|
| Ad group | • `operation_status` • `adgroup_name` • `location_ids` • `zipcode_ids` • `audience_ids` • `excluded_audience_ids` • `budget` • `schedule_type` • `schedule_start_time` • `schedule_end_time` |
| Ad | • `operation_status` • `ad_name` • `identity_type` • `identity_id` • `identity_authorized_bc_id` • `video_id` • `image_ids` • `music_id` • `tiktok_item_id` • `ad_text` • `aigc_disclosure_type` • `tracking_pixel_id` • `tracking_app_id` |

Sau khi tạo tác vụ, bạn sẽ nhận được mã tác vụ `task_id`.

3. **Kiểm tra kết quả tác vụ sao chép:** Truyền `task_id` vào endpoint [/campaign/copy/task/check/](../12-api-reference/24-campaign.md#doc-1788434463507458). Khuyến nghị chờ khoảng 1 phút trước khi kiểm tra kết quả.

## Sao chép chiến dịch Upgraded Smart+ (`Copy an Upgraded Smart+ Campaign`)
<a id="doc-1866529015923713"></a>
<!-- doc_id: 1866529015923713 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Copy an Upgraded Smart+ Campaign

Bài viết này hướng dẫn cách sao chép chiến dịch Upgraded Smart+.

### Giới thiệu (Introduction)
Với tính năng sao chép chiến dịch, bạn có thể nhân bản hiệu quả toàn bộ chiến dịch Upgraded Smart+, bao gồm nhiều nhóm quảng cáo và quảng cáo (nhóm tài sản).

### Điều kiện tiên quyết (Prerequisites)
- Quyền truy cập API và được đưa vào allowlist cho Asynchronous Campaign Copy API.
- Có sẵn chiến dịch Upgraded Smart+ trong tài khoản quảng cáo.

### Các bước thực hiện (Steps)

1. **Xác định các chiến dịch, nhóm quảng cáo và quảng cáo Upgraded Smart+ cần sao chép:**
   - Lọc bằng [/smart_plus/campaign/get/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312818332930), [/smart_plus/adgroup/get/](../12-api-reference/62-upgraded-smartplus-p2.md#doc-1843314879617026) và [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914).

Yêu cầu hợp lệ đối với các cấp độ:

| Level | Setting | Requirement | Parameters | Eligible configuration |
|---|---|---|---|---|
| Campaign | Advertising objective | Một trong các mục tiêu: App promotion, Lead generation, Website conversions | `objective_type` | `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS` |
| Ad group | Số lượng nhóm quảng cáo chưa bị xóa trong mỗi chiến dịch nguồn | 1 - 10 | / | / |
| Ad | Số lượng quảng cáo chưa bị xóa trong mỗi nhóm quảng cáo | 1 - 30 (tối đa 200 quảng cáo cho toàn chiến dịch mục tiêu) | / | / |
| Creative | Số lượng nội dung sáng tạo trong mỗi quảng cáo | 1 - 50 (tối đa 1.000 creative cho toàn chiến dịch mục tiêu) | / | / |

2. **Tạo tác vụ sao chép bất đồng bộ:** Gọi endpoint [/smart_plus/campaign/copy/task/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866528879472641).
   - Chọn chế độ `DEFAULT` (sao chép toàn bộ) hoặc `CUSTOM` (sao chép tùy chỉnh).

Các thiết lập có thể tùy biến khi sao chép:

| Level | Customizable settings |
|---|---|
| Ad group | • `operation_status` • `adgroup_name` • `budget` • `min_budget` • `location_ids` • `zipcode_ids` • `audience_ids` • `excluded_audience_ids` • `saved_audience_id` |
| Ad | • `operation_status` • `ad_name` • `ad_format` • `video_info` • `image_info` • `music_info` • `aigc_disclosure_type` • `tiktok_item_id` • `identity_type` • `identity_id` • `identity_authorized_bc_id` • `ad_text_list` • `call_to_action_list` • `landing_page_url_list` • `utm_params` • `call_to_action_id` |

3. **Kiểm tra kết quả tác vụ:** Truyền `task_id` vào [/smart_plus/campaign/copy/task/check/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866529943741441) (khuyến nghị chờ khoảng 5 phút).

## Mục tiêu quảng cáo (`Advertising objective`)
<a id="doc-1737585562434561"></a>
<!-- doc_id: 1737585562434561 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Advertising objective

Mục tiêu quảng cáo (Advertising objective) là đích đến kinh doanh mà bạn muốn chiến dịch đạt được (ví dụ tăng lưu lượng truy cập trang web, lượt tải ứng dụng hoặc tạo doanh số). Mục tiêu quảng cáo được thiết lập ở cấp chiến dịch và không thể thay đổi sau khi tạo.

### Mục tiêu quảng cáo cho Quảng cáo Đấu giá (Auction ads)

| Advertising objective (`objective_type`) | API Value | Description |
|---|---|---|
| [Tiếp cận (Reach)](https://ads.tiktok.com/help/article?aid=836189882076656982) | `REACH` | Hiển thị quảng cáo với số lượt hiển thị tối đa trong tệp đối tượng với chi phí tối ưu nhất. |
| [Lưu lượng truy cập (Traffic)](https://ads.tiktok.com/help/article?aid=6715316029142073350) | `TRAFFIC` | Thúc đẩy người dùng truy cập trang đích, bài viết blog hoặc ứng dụng. |
| [Lượt xem video (Video views)](https://ads.tiktok.com/help/article?aid=834107546545412106) | `VIDEO_VIEWS` | Tối đa hóa số lượt phát video quảng cáo từ những người dùng có khả năng tương tác cao nhất. |
| [Tìm kiếm khách hàng tiềm năng (Lead generation)](https://ads.tiktok.com/help/article?aid=10001624) | `LEAD_GENERATION` | Thu thập thông tin khách hàng tiềm năng qua biểu mẫu tức thì tải nhanh trong ứng dụng TikTok. |
| [Tương tác cộng đồng (Community interaction)](https://ads.tiktok.com/help/article?aid=10008245) | `ENGAGEMENT` | Tăng lượng người theo dõi tài khoản TikTok hoặc tăng lượt ghé thăm trang hồ sơ. |
| [Quảng bá ứng dụng (App promotion)](https://ads.tiktok.com/help/article?aid=10013496) | `APP_PROMOTION` | Thúc đẩy lượt cài đặt ứng dụng, tái tương tác người dùng hiện tại hoặc đăng ký trước khi phát hành. |
| [Chuyển đổi trang web (Website conversions)](https://ads.tiktok.com/help/article?aid=10013497) | `WEB_CONVERSIONS` | Thúc đẩy người dùng thực hiện hành động cụ thể trên trang web (mua hàng, thêm giỏ hàng). |
| Doanh số sản phẩm (Product sales) | `PRODUCT_SALES` | Hợp nhất các giải pháp quảng cáo video, hình ảnh và mua sắm trực tiếp (Live Shopping) để bán sản phẩm từ TikTok Shop, web và app. |
| Doanh số (Sales) | `WEB_CONVERSIONS` hoặc `PRODUCT_SALES` | Hợp nhất chuyển đổi trang web và doanh số sản phẩm vào mục tiêu Sales duy nhất. Xem [Mục tiêu Sales](quan-ly-chien-dich-p1.md#doc-1834189283112962). |

### Mục tiêu quảng cáo cho Tiếp cận & Tần suất (Reach & Frequency ads)

| Objective | API Value | Description |
|---|---|---|
| [Reach](https://ads.tiktok.com/help/article?aid=836189882076656982) | `RF_REACH` | Hiển thị quảng cáo với số lượt hiển thị tối đa tới đối tượng mục tiêu ở mức giá hiệu quả và tần suất cố định (cần duyệt allowlist). |


## Quảng bá ứng dụng (`App promotion`)
<a id="doc-1747553433902082"></a>
<!-- doc_id: 1747553433902082 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Advertising objective > App promotion

Với mục tiêu Quảng bá ứng dụng (App promotion), bạn có thể tìm kiếm người dùng mới cài đặt ứng dụng di động hoặc tái tương tác với người dùng hiện tại của ứng dụng.

Hiện tại, App promotion hỗ trợ 3 loại quảng bá ứng dụng sau:
- **Cài đặt ứng dụng (`APP_INSTALL`):** Thúc đẩy người dùng mới cài đặt và thực hiện hành động trong ứng dụng.
- **Tiếp thị lại ứng dụng (`APP_RETARGETING`):** Tái tương tác với người dùng hiện tại để họ mở ứng dụng và thực hiện hành động. (Lưu ý: Không hỗ trợ trong chiến dịch iOS 14 Dedicated Campaign).
- **Đăng ký trước ứng dụng (`APP_PREREGISTRATION`):** Thu hút người dùng đăng ký trước khi ứng dụng chính thức phát hành. (Tính năng allowlist; không hỗ trợ trong iOS 14 Dedicated Campaign). Xem thêm tại [Tạo quảng cáo đăng ký trước ứng dụng](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1772549012687873).

### Tạo quảng cáo App promotion
1. Sử dụng endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) để tạo chiến dịch với `objective_type` là `APP_PROMOTION` và `app_promotion_type` là một trong các giá trị: `APP_INSTALL`, `APP_RETARGETING`, `APP_PREREGISTRATION`.
2. Sử dụng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) để tạo nhóm quảng cáo. Nếu chiến dịch là iOS 14 Dedicated Campaign, hãy chỉ định `ios14_targeting` tương thích và `app_id`.
3. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) để tạo quảng cáo.

## Chuyển đổi trang web (`Website conversions`)
<a id="doc-1747553507237889"></a>
<!-- doc_id: 1747553507237889 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Advertising objective > Website conversions

Với mục tiêu Chuyển đổi trang web (Website conversions), bạn có thể thúc đẩy các hành động có giá trị của khách hàng trên trang web của mình hoặc Trang tức thì TikTok (TikTok Instant Page), chẳng hạn như mua hàng, điền thông tin đăng ký hoặc thêm sản phẩm vào giỏ hàng.

Để tạo chiến dịch chuyển đổi trang web, đặt `objective_type` thành `WEB_CONVERSIONS` khi gọi endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).

## Doanh số (`Sales`)
<a id="doc-1834189283112962"></a>
<!-- doc_id: 1834189283112962 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Advertising objective > Sales

Mục tiêu Doanh số (Sales) hợp nhất hai mục tiêu trước đây là Chuyển đổi trang web (Website Conversions) và Doanh số sản phẩm (Product Sales) thành một cấu trúc mục tiêu duy nhất.

Mục tiêu Sales hỗ trợ 3 điểm đến bán hàng (`sales_destination`):
- **TikTok Shop (`TIKTOK_SHOP`):** Thúc đẩy doanh số trực tiếp trên TikTok Shop.
- **Trang web (`WEBSITE`):** Thúc đẩy doanh số trên trang web của bạn.
- **Ứng dụng (`APP`):** Thúc đẩy doanh số trong ứng dụng di động của bạn.

## Nâng cấp lên mục tiêu Doanh số (`Upgrade from Product Sales or Website Conversions to the Sales objective`)
<a id="doc-1834189985160193"></a>
<!-- doc_id: 1834189985160193 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Advertising objective > Upgrade from Product Sales or Website Conversions to the Sales objective

Bài viết này cung cấp hướng dẫn và các ánh xạ trường bắt buộc để nâng cấp các quảng cáo [Chuyển đổi trang web](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1775548501843970) hoặc [Quảng cáo mua sắm (Shopping Ads)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942179356738) sang cấu trúc mục tiêu Doanh số (Sales).

### Tổng quan về nâng cấp (Upgrade overview)
**Việc nâng cấp lên mục tiêu Sales không ảnh hưởng đến cấu hình nhóm quảng cáo hay quảng cáo hiện có, đồng thời không làm thay đổi kết quả phân phối quảng cáo. Thay đổi này chỉ điều chỉnh cách hiển thị chiến dịch trên TikTok Ads Manager.**

Để nâng cấp lên mục tiêu Sales, bạn cần bổ sung 2 trường mới ở cấp Chiến dịch (Campaign):
- `virtual_objective_type`: Đặt là `SALES`.
- `sales_destination`: Giá trị cụ thể phụ thuộc vào cấu hình hiện tại (`TIKTOK_SHOP`, `WEBSITE` hoặc `APP`).

### Bảng ánh xạ nâng cấp

#### Nâng cấp mục tiêu Product Sales có nguồn sản phẩm là TikTok Shop

| Level | Before upgrade | After upgrade (add fields) |
|---|---|---|
| Campaign | • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `STORE` | • **`virtual_objective_type` là `SALES`** <br> • **`sales_destination` là `TIKTOK_SHOP`** <br> • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `STORE` |

#### Nâng cấp Product Sales nguồn Catalog với địa điểm tối ưu hóa là Website

| Level | Before upgrade | After upgrade (add fields) |
|---|---|---|
| Campaign | • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `CATALOG` | • **`virtual_objective_type` là `SALES`** <br> • **`sales_destination` là `WEBSITE`** <br> • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `CATALOG` |
| Ad group | • `promotion_type` là `WEBSITE` | • `promotion_type` là `WEBSITE` |

#### Nâng cấp Product Sales nguồn Catalog với địa điểm tối ưu hóa là App

| Level | Before upgrade | After upgrade (add fields) |
|---|---|---|
| Campaign | • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `CATALOG` | • **`virtual_objective_type` là `SALES`** <br> • **`sales_destination` là `APP`** <br> • `objective_type` là `PRODUCT_SALES` <br> • `campaign_product_source` là `CATALOG` |
| Ad group | • `promotion_type` là `APP_ANDRIOD` hoặc `APP_IOS` | • `promotion_type` là `APP_ANDRIOD` hoặc `APP_IOS` |

#### Nâng cấp mục tiêu Website Conversions

| Level | Before upgrade | After upgrade (add fields) |
|---|---|---|
| Campaign | • `objective_type` là `WEB_CONVERSIONS` | • **`virtual_objective_type` là `SALES`** <br> • **`sales_destination` là `WEBSITE`** <br> • `objective_type` là `WEB_CONVERSIONS` |

### Ví dụ: Nâng cấp chiến dịch Website Conversions lên Sales

Trước khi nâng cấp:
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "objective_type": "WEB_CONVERSIONS",
    "campaign_name": "{{campaign_name}}",
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": {{budget}}
}'
```

Sau khi nâng cấp:
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "virtual_objective_type": "SALES",
    "sales_destination": "WEBSITE",
    "objective_type": "WEB_CONVERSIONS",
    "campaign_name": "{{campaign_name}}",
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": {{budget}}
}'
```

## Tiếp cận & Tần suất (`Reach & Frequency`)
<a id="doc-1739470723315713"></a>
<!-- doc_id: 1739470723315713 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Reach & Frequency

Tiếp cận & Tần suất (Reach & Frequency - R&F) là hình thức mua chiến dịch cho phép nhà quảng cáo TikTok For Business lên kế hoạch và đặt mua trước các chiến dịch với chi phí và tần suất hiển thị có thể dự đoán trước.

- Để tìm hiểu chi tiết về quảng cáo R&F, xem [Giới thiệu về Reach & Frequency](quan-ly-chien-dich-p1.md#doc-1744571201117186).
- Để tìm hiểu cách tạo chiến dịch R&F, xem [Tạo chiến dịch Reach & Frequency](quan-ly-chien-dich-p1.md#doc-1744571205201922).
- Để tìm hiểu cách quản lý chiến dịch R&F, xem [Quản lý chiến dịch Reach & Frequency](quan-ly-chien-dich-p1.md#doc-1744571207714818).
- Để tra cứu các API liên quan đến R&F, xem [Tham chiếu API Reach & Frequency](quan-ly-chien-dich-p1.md#doc-1744571210012673).


## Giới thiệu về Tiếp cận & Tần suất (`About Reach & Frequency`)
<a id="doc-1744571201117186"></a>
<!-- doc_id: 1744571201117186 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Reach & Frequency > About Reach & Frequency

Tiếp cận & Tần suất (Reach & Frequency - R&F) mang lại khả năng tiếp cận có thể dự đoán trước, tần suất được kiểm soát chặt chẽ và đảm bảo phân phối lượt hiển thị với trải nghiệm quảng cáo linh hoạt và minh bạch. Khác với Quảng cáo Đấu giá (Auction ads) phụ thuộc vào giá thầu và tính cạnh tranh của thị trường, R&F cho phép bạn kiểm soát chính xác quy mô đối tượng tiếp cận và số lần họ nhìn thấy thông điệp quảng cáo của bạn trước khi bắt đầu phân phối.

> [!NOTE]
> Tính năng Reach & Frequency đã phát hành rộng rãi (GA). Các nhà phát triển có thể tích hợp tính năng này, tuy nhiên chỉ áp dụng cho các tài khoản quảng cáo đã được đưa vào danh sách cho phép (allowlist). Để đăng ký allowlist, hãy liên hệ với đại diện TikTok của bạn.

Quảng cáo R&F hiện có thể phân phối tại các quốc gia và khu vực sau: Úc, Áo, Argentina, Bahrain, Belarus, Bỉ, Brazil, Campuchia, Canada, Chile, Colombia, Cộng hòa Séc, Đan Mạch, Ecuador, Ai Cập, Phần Lan, Pháp, Đức, Hy Lạp, Hungary, Indonesia, Iraq, Ireland, Israel, Ý, Nhật Bản, Jordan, Kazakhstan, Kuwait, Lebanon, Malaysia, Mexico, Morocco, Hà Lan, New Zealand, Na Uy, Oman, Pakistan, Peru, Philippines, Ba Lan, Bồ Đào Nha, Qatar, Romania, Nga, Ả Rập Xê Út, Singapore, Nam Phi, Hàn Quốc, Tây Ban Nha, Thụy Điển, Thụy Sĩ, Tỉnh Đài Loan, Thái Lan, Thổ Nhĩ Kỳ, Ukraine, Các Tiểu vương quốc Ả Rập Thống nhất, Vương quốc Anh, Hoa Kỳ, Uruguay, Việt Nam.

### Ước tính kho quảng cáo (Inventory estimate)

Bạn có thể sử dụng endpoint [/rf/inventory/estimate/](../12-api-reference/57-reach-and-frequency.md#doc-1738235487941633) để tạo các dự báo kho quảng cáo phục vụ lập kế hoạch chiến dịch. Kết quả ước tính được tính toán theo thời gian thực dựa trên mục tiêu quảng cáo, vị trí hiển thị, nhắm mục tiêu, lịch trình, tần suất hiển thị và cài đặt giữ chỗ.
- Bạn có thể dự đoán theo ngân sách cố định (`FIXED_BUDGET`), lượt hiển thị cố định (`FIXED_SHOW`) hoặc lượt tiếp cận cố định (`FIXED_REACH`).
- Dữ liệu trả về bao gồm `budget`, `cpm`, `impression`, `reach` và `average_frequency` tương ứng với các biểu đồ **Impressions & Budget** và **Reach & Budget** trên TikTok Ads Manager.

### Đơn hàng và ngân sách (Orders and budgets)
Khi nhóm quảng cáo R&F được tạo, một đơn hàng R&F sẽ tự động được khởi tạo để giữ chỗ kho quảng cáo. Đúng 5 phút trước khi quảng cáo bắt đầu phân phối, hệ thống sẽ khóa số tiền ngân sách tương ứng từ số dư tài khoản quảng cáo của bạn. Ngân sách bị khóa chỉ dùng riêng cho quảng cáo R&F đó.

## Tạo chiến dịch Tiếp cận & Tần suất (`Create a Reach & Frequency campaign`)
<a id="doc-1744571205201922"></a>
<!-- doc_id: 1744571205201922 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Reach & Frequency > Create a Reach & Frequency campaign

Quy trình từng bước để tạo một chiến dịch R&F hoàn chỉnh:

1. **Tạo chiến dịch:** Sử dụng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) với `objective_type` là `RF_REACH`.
2. **Ước tính kho quảng cáo:** Gọi [/rf/inventory/estimate/](../12-api-reference/57-reach-and-frequency.md#doc-1738235487941633) với các thông số nhắm mục tiêu và lịch phân phối. Lưu ý `schedule_start_time` phải có định dạng `YYYY-MM-DD HH:00:00` và `schedule_end_time` có định dạng `YYYY-MM-DD HH:59:59` theo múi giờ phân phối quảng cáo.
3. **Tạo biểu đồ ngân sách & lượt hiển thị/tiếp cận (Tùy chọn):** Dựa trên mảng `results` trả về để vẽ biểu đồ tương quan.
4. **Tạo nhóm quảng cáo R&F:** Gọi endpoint [/adgroup/rf/create/](../12-api-reference/57-reach-and-frequency.md#doc-1738235338194945).
   - Truyền `rf_purchased_type` (`FIXED_SHOW`, `FIXED_REACH` hoặc `FIXED_BUDGET`).
   - Cung cấp các giá trị `budget`, `purchased_impression` và `purchased_reach` lấy từ bước ước tính kho quảng cáo.
   - Cấu hình tần suất kiểm soát qua `frequency` và `frequency_schedule`.
5. **Tạo quảng cáo R&F:** Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354). Lưu ý quảng cáo R&F chỉ hỗ trợ nội dung sáng tạo video.

## Quản lý chiến dịch Tiếp cận & Tần suất (`Manage a Reach & Frequency campaign`)
<a id="doc-1744571207714818"></a>
<!-- doc_id: 1744571207714818 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Reach & Frequency > Manage a Reach & Frequency campaign

Sau khi tạo chiến dịch R&F, bạn có thể quản lý, điều chỉnh hoặc hủy đơn hàng R&F:

- **Cập nhật nhóm quảng cáo R&F:** Sử dụng endpoint **/adgroup/rf/update/** để điều chỉnh tên nhóm quảng cáo, nội dung sáng tạo hoặc trạng thái hoạt động.
- **Hủy hoặc xóa nhóm quảng cáo R&F:** Sử dụng endpoint **/adgroup/status/update/**. Nếu hủy nhóm quảng cáo trước khi thời điểm phân phối bắt đầu, ngân sách bị khóa sẽ được hoàn trả lại số dư tài khoản.

## Tham chiếu API Tiếp cận & Tần suất (`API reference`)
<a id="doc-1744571210012673"></a>
<!-- doc_id: 1744571210012673 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Reach & Frequency > API reference

Danh mục các endpoint API dành riêng cho Tiếp cận & Tần suất (Reach & Frequency):
- [/rf/inventory/estimate/](../12-api-reference/57-reach-and-frequency.md#doc-1738235487941633): Ước tính kho quảng cáo R&F.
- [/adgroup/rf/create/](../12-api-reference/57-reach-and-frequency.md#doc-1738235338194945): Tạo nhóm quảng cáo R&F.
- **/adgroup/rf/update/**: Cập nhật nhóm quảng cáo R&F.

## TopView (`TopView`)
<a id="doc-1804258360285186"></a>
<!-- doc_id: 1804258360285186 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > TopView

TopView là định dạng quảng cáo video xuất hiện ngay lập tức khi người dùng mở ứng dụng TikTok. Đây là quảng cáo toàn màn hình mạnh mẽ kèm âm thanh tự động bật, mang lại mức độ nhận diện thương hiệu cao nhất trước bất kỳ nội dung nào khác trên TikTok.

### Tính khả dụng trên API (Availability)

Bảng dưới đây nêu rõ các tính năng được hỗ trợ qua API cho quảng cáo TopView:

| Feature | Available in API | Related endpoints |
|---|---|---|
| Creating TopView campaigns, ad groups, or ads | ❌ | Không hỗ trợ tạo qua API |
| Updating TopView campaigns, ad groups, or ads | ❌ | Không hỗ trợ cập nhật qua API |
| Retrieving TopView campaigns, ad groups, or ads | ✅ | • [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986) <br> • [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922) <br> • [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) |
| Copying TopView campaigns, ad groups, or ads | ❌ | Không hỗ trợ sao chép qua API |
| Running synchronous basic reports and audience reports | ✅ | • [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) |
| Previewing TopView ads | ❌ | Không hỗ trợ xem trước qua API |

### Dữ liệu có thể truy xuất cho nhóm quảng cáo TopView (Retrievable data)
Khi truy xuất dữ liệu nhóm quảng cáo TopView qua [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922), bạn có thể truy cập các trường: `advertiser_id`, `campaign_id`, `campaign_name`, `adgroup_id`, `adgroup_name`, `placements`, `location_ids`, `gender`, `age_groups`, `languages`, `interest_category_ids`, `predict_impression`, `topview_reach_range`, `pre_discount_cpm`, `cpm`, `discount_type`, `discount_amount`, `discount_percentage`, `pre_discount_budget`, `budget`, `schedule_type`, `schedule_start_time`, `schedule_end_time`, `billing_event`, `create_time`, `modify_time`, `operation_status`, `secondary_status`.


## (Sắp ngừng hỗ trợ) Chiến dịch Smart+ cũ (`(To be deprecated) Legacy Smart+ Campaign`)
<a id="doc-1767959274087425"></a>
<!-- doc_id: 1767959274087425 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > (To be deprecated) Legacy Smart+ Campaign

Smart+ Campaign là giải pháp tự động hóa bằng AI của TikTok nhằm tối đa hóa kết quả phân phối với ít nỗ lực vận hành thủ công nhất. Hệ thống cung cấp nhiều mẫu nội dung sáng tạo và giá thầu cho phiên đấu giá nhằm nâng cao hiệu suất chiến dịch. Smart+ Campaign hỗ trợ các mục tiêu: `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`.

> [!IMPORTANT]
> - **Nâng cấp lên Upgraded Smart+ API**: Chúng tôi đã ra mắt bộ API Upgraded Smart+ mới với năng lực vượt trội. Xem thêm [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458) và [Danh sách endpoint Upgraded Smart+ API](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843301794874370).
> - **Lộ trình ngừng hỗ trợ (Deprecation)**:
>   - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo chiến dịch Smart+ cũ bằng endpoint [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362). Các chiến dịch cũ chưa di chuyển sẽ không tự động chuyển đổi.
>   - Các nhà phát triển có nhu cầu gia hạn có thể gửi đơn qua biểu mẫu gia hạn chính thức trước ngày **30 tháng 6 năm 2026**.

### Báo cáo cho Smart+ Campaign
Bạn có thể truy cập dữ liệu báo cáo ở cấp chiến dịch hoặc nhóm quảng cáo qua [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) hoặc [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602), và cấp sáng tạo qua [/campaign/spc/report/get/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1776454619412481).

## Chiến dịch Upgraded Smart+ (`Upgraded Smart+ Campaign`)
<a id="doc-1853452461203458"></a>
<!-- doc_id: 1853452461203458 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Upgraded Smart+ Campaign

Chiến dịch Upgraded Smart+ giới thiệu một quy trình làm việc hợp nhất mới (trải nghiệm Upgraded Smart+). Quy trình tinh gọn này cho phép bạn tiếp cận cả các tính năng thủ công (Manual) và tự động hóa (Smart+) ngay trong cùng một chiến dịch.

Upgraded Smart+ API kết hợp khả năng **tự động hóa dựa trên AI** với **khả năng kiểm soát chi tiết**, cho phép tinh chỉnh nhắm mục tiêu đồng thời tận dụng AI để tối ưu hóa hiệu suất phân phối.

### Lợi ích cốt lõi
- **Kiểm soát chi tiết:** Điều chỉnh giá thầu, nhắm mục tiêu, vị trí hiển thị và khả năng đưa nhiều phần tử sáng tạo vào trong một chiến dịch duy nhất.
- **Tự động hóa nâng cao:** Tùy chỉnh chiến lược ở cấp độ từng thành phần.
- **Kết hợp linh hoạt:** Cho phép nhà quảng cáo tùy biến các thiết lập tự động hóa theo từng cấu phần để tăng tính minh bạch và độ linh hoạt chiến lược.

### Hướng dẫn di chuyển (Migration guidance)
**Upgraded Smart+ API sẽ đóng vai trò là bộ endpoint thống nhất cho tất cả các quy trình tạo chiến dịch trong tương lai, thay thế cả Smart+ API cũ và Campaign Management API cho chiến dịch thủ công:**
- **Legacy Smart+ API:** Cần di chuyển ngay. Ngừng tạo mới sau ngày **31/03/2026**. Endpoint cập nhật duy trì đến **30/06/2026**.
- **Manual Campaign Management API:** Ngừng tạo mới qua [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) sau ngày **31/12/2026**. Endpoint cập nhật [/campaign/update/](../12-api-reference/24-campaign.md#doc-1739320422086657) vẫn hoạt động và sẽ có thông báo trước 3 tháng khi ngừng hỗ trợ.

## Truy xuất dữ liệu cho Upgraded Smart+, Smart+ và Chiến dịch thủ công (`Retrieve data for Upgrade Smart+, Smart+, and Manual Campaigns`)
<a id="doc-1854103649826817"></a>
<!-- doc_id: 1854103649826817 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Upgraded Smart+ Campaign > Retrieve data for Upgrade Smart+, Smart+, and Manual Campaigns

Hướng dẫn này tổng quan về các cấp độ dữ liệu và phương thức truy xuất cho 3 loại chiến dịch: Manual Campaign, Smart+ Campaign và Upgraded Smart+ Campaign.

### Các cấp độ dữ liệu tổng thể (Overall data levels)

| Cấp độ dữ liệu (Data level) | Manual Campaign | Smart+ Campaign | Upgrade Smart+ Campaign |
|---|---|---|---|
| Campaign | ✅ Hỗ trợ đầy đủ | ✅ Hỗ trợ đầy đủ | ✅ Hỗ trợ đầy đủ |
| Ad group | ✅ Hỗ trợ đầy đủ | ✅ Hỗ trợ đầy đủ | ✅ Hỗ trợ đầy đủ |
| Ad | ✅ Hỗ trợ đầy đủ | ⚠️ Trả về dữ liệu giới hạn | ✅ Hỗ trợ đầy đủ |
| Creative | ❌ Không hỗ trợ | ✅ Hỗ trợ đầy đủ | ✅ Hỗ trợ đầy đủ |

### Toàn cảnh truy xuất dữ liệu (Data retrieval landscape)

- **Chiến dịch thủ công (Manual Campaigns):**
  - Cấp Campaign: [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986)
  - Cấp Ad group: [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922)
  - Cấp Ad: [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770)
  - Báo cáo: [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353)
- **Chiến dịch Upgraded Smart+:**
  - Cấp Campaign: [/smart_plus/campaign/get/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312818332930)
  - Cấp Ad group: [/smart_plus/adgroup/get/](../12-api-reference/62-upgraded-smartplus-p2.md#doc-1843314879617026)
  - Cấp Ad (Asset Group): [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)
  - Cấp Creative: [/smart_plus/creative/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)
  - Báo cáo: Hỗ trợ đầy đủ qua Reporting API ở tất cả các cấp độ.

## Thay đổi về tính tương thích cho Chiến dịch Upgraded Smart+ (`Compatibility changes for Upgraded Smart+ Campaigns`)
<a id="doc-1854112742370306"></a>
<!-- doc_id: 1854112742370306 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Upgraded Smart+ Campaign > Compatibility changes for Upgraded Smart+ Campaigns

Bảng dưới đây nêu bật các thay đổi tương thích trên các endpoint hiện có khi áp dụng Upgraded Smart+:

| Phân hệ (Module) | Endpoints | Thay đổi tương thích chính |
|---|---|---|
| Campaign | [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986) | Mặc định trả về cả chiến dịch Upgraded Smart+. Tham số `campaign_automation_type` có sẵn trong yêu cầu và phản hồi để phân biệt Manual, Smart+ và Upgraded Smart+. |
| Campaign | [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602), [/campaign/update/](../12-api-reference/24-campaign.md#doc-1739320422086657) | Không thể dùng để tạo hoặc cập nhật Upgraded Smart+. Sử dụng các endpoint Upgraded Smart+ tương ứng. |
| Ad group | [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922) | Mặc định trả về cả nhóm quảng cáo Upgraded Smart+ kèm tham số `campaign_automation_type`. |
| Ad group | [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745) | Không dùng để tạo hoặc cập nhật nhóm quảng cáo Upgraded Smart+. |
| Ad | [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) | Hỗ trợ truy xuất quảng cáo Upgraded Smart+. Bổ sung trường `smart_plus_ad_id`, bộ lọc `ad_ids_v2`, giá trị enum `UPGRADED_SMART_PLUS` trong `campaign_automation_type`. |
| Ad Preview | [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426) | Không dùng để xem trước quảng cáo Upgraded Smart+. Sử dụng [/smart_plus/ad/preview/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317445798914) thay thế. |
| Smart Creative | [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626) | Không hỗ trợ tạo quảng cáo Smart Creative bằng nhóm quảng cáo Upgraded Smart+. |


## Chiến dịch chuyên dụng (`Dedicated Campaign`)
<a id="doc-1740029173531649"></a>
<!-- doc_id: 1740029173531649 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Dedicated Campaign

Chiến dịch chuyên dụng (Dedicated Campaign - DC) là loại chiến dịch đặc biệt nhắm mục tiêu vào các thiết bị chạy hệ điều hành iOS 14.5 trở lên. Thiết bị chạy iOS 14.5+ chiếm phần lớn lưu lượng truy cập; việc tạo chiến dịch chuyên dụng đảm bảo bạn tiếp cận được nhóm người dùng này (nếu tạo chiến dịch thông thường, quảng cáo sẽ không thể phân phối tới các thiết bị iOS 14.5+).

Tùy thuộc vào việc ứng dụng đã kích hoạt SKAdNetwork (SKAN) 4.0 hay chưa, chiến dịch có thể là iOS 14 Dedicated Campaign hoặc SKAN 4.0 Dedicated Campaign. Chiến dịch chuyên dụng chỉ có thể tạo với mục tiêu `PRODUCT_SALES` (khi `campaign_product_source` là `CATALOG`) hoặc `APP_PROMOTION` (khi `app_promotion_type` là `APP_INSTALL`).

### Cấu hình cửa sổ phân bổ SKAN 4.0 (Attribution Window)

Với SKAN 4.0, bạn có thể định cấu hình cửa sổ phân bổ cho một chiến dịch đang tắt (`operation_status` là `DISABLE`) thông qua tham số `postback_window_mode` ở cấp chiến dịch.

Bảng tác động của cửa sổ phân bổ đến việc giải phóng hạn ngạch chiến dịch:

| Attribution window | Corresponding postback | Impact on DC campaign quota release | Value for postback_window_mode |
|---|---|---|---|
| 0-2 days | First postback | Tối đa 4 ngày để giải phóng hạn ngạch | `POSTBACK_WINDOW_MODE1` |
| 3-7 days | First two postbacks | Tối đa 13 ngày để giải phóng hạn ngạch | `POSTBACK_WINDOW_MODE2` |
| 8-35 days | All three postbacks | Tối đa 41 ngày để giải phóng hạn ngạch | `POSTBACK_WINDOW_MODE3` |

### Quy trình tạo Dedicated Campaign

1. **Kiểm tra điều kiện:** Xác minh trường `skan_allowed` qua [/app/list/](../12-api-reference/43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](../12-api-reference/43-events-1-0-p1.md#doc-1740859272887297). Kiểm tra hạn ngạch còn lại qua [/campaign/quota/info/](../12-api-reference/24-campaign.md#doc-1752256376677378).
2. **Tạo chiến dịch:** Sử dụng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) với `campaign_type` là `IOS14_CAMPAIGN` và chỉ định `app_id`.
3. **Tạo nhóm quảng cáo:** Sử dụng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114). Thiết lập `ios14_targeting` là `IOS14_PLUS` hoặc không truyền giá trị.
4. **Tạo quảng cáo:** Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

### Cấu trúc chiến dịch chuyên dụng SKAN (SKAN Dedicated Campaign Structure)

| Campaign Type | iOS 14 SKAN Dedicated Campaigns using a non-SKAN 4.0 App | SKAN 4.0 Dedicated Campaigns using a SKAN 4.0 App |
|---|---|---|
| Maximum number of Dedicated Campaigns for each ad network in an iOS app | 15 hoặc 25 (mở rộng lên 25 cần duyệt allowlist) | 15 hoặc 25 (mở rộng lên 25 cần duyệt allowlist) |
| Maximum number of active ad groups within a Dedicated Campaign | 5 | 5 |
| Maximum number of undeleted ads within an ad group | 50 | • Nếu không bật Smart+, ACO hay Smart Creative: 9 <br> • Nếu có bật Smart+, ACO hoặc Smart Creative: không giới hạn |

## Giới hạn hạn ngạch Chiến dịch chuyên dụng (`Dedicated Campaign quota limits`)
<a id="doc-1752256248260610"></a>
<!-- doc_id: 1752256248260610 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Dedicated Campaign > Dedicated Campaign quota limits

Để tuân thủ chính sách của Apple về SKAdNetwork, số lượng chiến dịch chuyên dụng đang hoạt động đồng thời bị giới hạn theo từng mạng quảng cáo (ad network).

### Quy tắc hạn ngạch cho SKAN 4.0 Dedicated Campaign

Bảng độ trễ ngẫu nhiên và thời gian giải phóng hạn ngạch:

| Attribution window | Random delay in sending the postback | Impact on DC campaign quota release |
|---|---|---|
| 0-2 days | 24 - 48 giờ | Tối đa 4 ngày để giải phóng hạn ngạch |
| 3-7 days | 24 - 144 giờ | Tối đa 13 ngày để giải phóng hạn ngạch |
| 8-35 days | 24 - 144 giờ | Tối đa 41 ngày để giải phóng hạn ngạch |

### Mạng quảng cáo và vị trí hiển thị (Ad network and placements)

| Network | Supported placement | Number of campaign quota for iOS 14 SKAN Dedicated Campaigns | Number of campaign quota for SKAN 4.0 Dedicated Campaigns |
|---|---|---|---|
| TikTok | TikTok (`PLACEMENT_TIKTOK`), Global App Bundle (`PLACEMENT_GLOBAL_APP_BUNDLE`) | 15 hoặc 25 | 15 hoặc 25 |
| Pangle | Pangle (`PLACEMENT_PANGLE`) | 15 hoặc 25 | 15 hoặc 25 |

- Nếu sử dụng **Chọn vị trí thủ công (Select Placement)**, chiến dịch sẽ chiếm 1 hạn ngạch cho mạng tương ứng.
- Nếu sử dụng **Vị trí tự động (Automatic Placement)**, chiến dịch sẽ chiếm đồng thời 1 hạn ngạch trên mạng TikTok và 1 hạn ngạch trên mạng Pangle.

Sử dụng endpoint [/campaign/quota/info/](../12-api-reference/24-campaign.md#doc-1752256376677378) để kiểm tra số lượng hạn ngạch còn lại ở cấp chiến dịch và nhóm quảng cáo.

## Thử nghiệm phân tách Super Split Test (`Super Split Test`)
<a id="doc-1742668394531842"></a>
<!-- doc_id: 1742668394531842 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Super Split Test

Super Split Test (thường gọi là thử nghiệm A/B) là cơ chế do TikTok cung cấp giúp bạn kiểm tra các biến số khác nhau của nhóm quảng cáo hoặc chiến dịch nhằm xác định chiến lược tối ưu nhất. Thử nghiệm mang lại kết quả có ý nghĩa thống kê và độ chính xác cao.

### Phạm vi và quy tắc
- Hỗ trợ thử nghiệm ở cấp nhóm quảng cáo (Ad group level) và cấp chiến dịch (Campaign level - cần allowlist).
- Đối với thử nghiệm nhóm quảng cáo, có thể so sánh 2 nhóm quảng cáo từ cùng một hoặc khác chiến dịch.
- Đối với chiến dịch chuyên dụng iOS 14, hai nhóm quảng cáo so sánh phải thuộc cùng một chiến dịch và sử dụng cùng App ID.
- Không hỗ trợ Tối ưu hóa ngân sách chiến dịch (CBO) khi thử nghiệm ở cấp chiến dịch.

### Mục tiêu tối ưu hóa được hỗ trợ (Supported optimization goals)

Bảng các mục tiêu tối ưu hóa và chỉ số đánh giá chính trong thử nghiệm phân tách:

| Optimization Goal | Key metrics |
|---|---|
| Reach (REACH) | `COST_PER_REACH` |
| Impression (SHOW) | `COST_PER_SHOW` |
| Click (CLICK) | `COST_PER_CLICK`, `COST_PER_SHOW` |
| Leads (LEAD_GENERATION) | `COST_PER_CONVERT`, `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `CONVERT_RATE` |
| Install (INSTALL) | `COST_PER_CONVERT`, `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `CONVERT_RATE` |
| Conversion (CONVERT) | `COST_PER_CONVERT`, `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `CONVERT_RATE` |
| In-app event (IN_APP_EVENT) | `COST_PER_CONVERT`, `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `CONVERT_RATE` |
| Value (VALUE) | `COST_PER_CLICK`, `COST_PER_SHOW`, `COST_PER_CONVERT`, `COMPLETE_PAYMENT_ROAS` |
| Follow (FOLLOWERS) | `COST_PER_CONVERT`, `COST_PER_SHOW` |
| Profile visit (PROFILE_VIEWS) | `COST_PER_CONVERT`, `COST_PER_SHOW` |
| 6-second views (Focused view) (ENGAGED_VIEW) | `COST_PER_SHOW`, `COST_PER_FOCUSED_VIEW`, `FOCUSED_VIEW_RATE` |
| 15-second views (Focused view), allowlisted (ENGAGED_VIEW_FIFTEEN) | `COST_PER_SHOW`, `COST_PER_FOCUSED_VIEW`, `FOCUSED_VIEW_RATE` |
| Conversation (CONVERSATION) | `COST_PER_CONVERT`, `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `CONVERT_RATE` |
| Landing Page View (TRAFFIC_LANDING_PAGE_VIEW) | `COST_PER_CLICK`, `COST_PER_SHOW`, `CLICK_THROUGH_RATE`, `COST_PER_LANDING_PAGE_VIEW`, `LANDING_PAGE_VIEW_RATE` |

### Các endpoint liên quan
- [Tạo thử nghiệm phân tách (Create a split test)](../12-api-reference/65-super-split-test.md#doc-1742666471475201)
- [Lấy kết quả thử nghiệm (Get split test results)](../12-api-reference/65-super-split-test.md#doc-1742666557045761)
- [Chạy nhóm quảng cáo chiến thắng (Run the winning ad group)](../12-api-reference/65-super-split-test.md#doc-1742666543736834)
- [Cập nhật thời gian thử nghiệm (Update split test time)](../12-api-reference/65-super-split-test.md#doc-1742666501911553)
- [Kết thúc thử nghiệm (End a split test)](../12-api-reference/65-super-split-test.md#doc-1742666522399746)

## Sử dụng thử nghiệm phân tách (`Use split tests`)
<a id="doc-1742668948278274"></a>
<!-- doc_id: 1742668948278274 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Super Split Test > Use split tests

Bài viết này hướng dẫn chi tiết quy trình triển khai thử nghiệm phân tách A/B:

1. **Tạo chiến dịch:** Sử dụng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo:** Sử dụng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Khởi tạo thử nghiệm:** Sử dụng endpoint [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) và chỉ định chỉ số chính muốn theo dõi.
4. **Xem kết quả thử nghiệm:** Sử dụng [/split_test/result/get/](../12-api-reference/65-super-split-test.md#doc-1742666557045761) sau khi thử nghiệm đã kết thúc ít nhất 24 giờ. Hệ thống trả về giá trị P-value tương ứng. Nhóm hoặc chiến dịch chiến thắng được xác định khi P-value <= 0.1.
5. **Thúc đẩy nhóm chiến thắng:** Đối với thử nghiệm nhóm quảng cáo, sau khi xác định nhóm chiến thắng, gọi endpoint [/split_test/promote/](../12-api-reference/65-super-split-test.md#doc-1742666543736834) để phân phối nhóm chiến thắng và tạm dừng nhóm còn lại (ngân sách nhóm chiến thắng sẽ tự động được nhân đôi).


## Ngân sách (`Budget`)
<a id="doc-1739381246298114"></a>
<!-- doc_id: 1739381246298114 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Budget

Để cung cấp nhiều quyền kiểm soát hơn đối với chi phí quảng cáo, TikTok For Business hỗ trợ cài đặt ngân sách ở cả cấp chiến dịch (campaign) và cấp nhóm quảng cáo (ad group).

Để đảm bảo hiệu quả phân phối, TikTok for Business quy định mức ngân sách tối thiểu cho cả ngân sách trọn đời (lifetime) và ngân sách hàng ngày (daily):
* **Ngân sách tối thiểu ở cấp chiến dịch:**
  - Đối với các chiến dịch thông thường, cả ngân sách hàng ngày và ngân sách trọn đời phải đạt tối thiểu **20 USD** (ngoại trừ các chiến dịch có `objective_type` là `PRODUCT_SALES` và `campaign_product_source` là `STORE`).
  - Đối với chiến dịch có `objective_type` là `PRODUCT_SALES` và `campaign_product_source` là `STORE`, cả ngân sách ngày và trọn đời phải đạt trên **10 USD**.
* **Ngân sách tối thiểu ở cấp nhóm quảng cáo:**
  - Đối với các nhóm quảng cáo thông thường, ngân sách hàng ngày phải vượt quá **20 USD**. Ngân sách trọn đời được tính bằng: *Ngân sách ngày tối thiểu (20 USD) × số ngày theo lịch trình*.
  - Đối với nhóm quảng cáo có `product_source` là `STORE` hoặc `SHOWCASE`, ngân sách hàng ngày phải vượt quá **10 USD**. Ngân sách trọn đời tính bằng: *10 USD × số ngày theo lịch trình*.

### Các chế độ ngân sách ở các cấp độ khác nhau

| Ad Level | Campaign Budget Optimization (CBO) | Buget Mode |
|---|---|---|
| Campaign | Bật (Enabled) | Khi CBO bật, `budget_mode` ở cấp chiến dịch hỗ trợ: <br> • `BUDGET_MODE_TOTAL`: Ngân sách trọn đời. <br> • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách ngày động (chi phí tuần không vượt quá ngân sách trung bình ngày × 7, chi phí ngày không vượt quá 125% mức trung bình). <br> • `BUDGET_MODE_DAY`: Ngân sách ngày cố định. |
| Campaign | Tắt (Disabled) | Khi CBO tắt, `budget_mode` ở cấp chiến dịch hỗ trợ: <br> • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách. <br> • `BUDGET_MODE_TOTAL`: Ngân sách trọn đời. <br> • `BUDGET_MODE_DAY`: Ngân sách ngày. |
| Ad Group | Bật (Enabled) | Khi CBO bật, `budget_mode` ở cấp nhóm quảng cáo sẽ bị bỏ qua (sử dụng ngân sách chiến dịch). |
| Ad Group | Tắt (Disabled) | Khi CBO tắt, `budget_mode` ở cấp nhóm quảng cáo hỗ trợ: <br> • `BUDGET_MODE_TOTAL`: Ngân sách trọn đời. <br> • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách ngày động. <br> • `BUDGET_MODE_DAY`: Ngân sách ngày. |

### Hướng dẫn thiết lập ngân sách
Ngân sách quảng cáo được định cấu hình phụ thuộc vào đơn vị tiền tệ của tài khoản quảng cáo của bạn. Việc xác minh ngân sách dựa trên 3 yếu tố:
- Độ chính xác của tiền tệ (Precision / số chữ số thập phân tối đa cho phép).
- Phạm vi giá trị ngân sách: Tính bằng **phạm vi giá trị ngân sách cơ bản** × **Tỷ lệ xác minh ngân sách của loại tiền tệ tương ứng (Budget Verification Ratio)**.
  - Ví dụ: Với tài khoản JPY (Budget Verification Ratio là 100), phạm vi ngân sách ngày cơ bản [20, 10.000.000) USD sẽ tương ứng với [2.000, 1.000.000.000) JPY.

## Tối ưu hóa ngân sách chiến dịch (`Campaign Budget Optimization`)
<a id="doc-1739381757818881"></a>
<!-- doc_id: 1739381757818881 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Campaign Budget Optimization

Tối ưu hóa ngân sách chiến dịch (CBO) tối ưu hóa việc phân bổ ngân sách ở cấp chiến dịch thay vì ở từng nhóm quảng cáo riêng lẻ. Với CBO, bạn chỉ cần thiết lập ngân sách tổng thể ở cấp chiến dịch, hệ thống sẽ tự động liên tục phân bổ ngân sách theo thời gian thực tới các nhóm quảng cáo mang lại hiệu suất tốt nhất.

### Các mục tiêu quảng cáo hỗ trợ CBO
CBO hỗ trợ các mục tiêu quảng cáo sau (`objective_type`):
- `REACH` (Tiếp cận)
- `TRAFFIC` (Lưu lượng truy cập)
- `WEB_CONVERSIONS` (Chuyển đổi trang web)
- `APP_PROMOTION` (Quảng bá ứng dụng)
- `LEAD_GENERATION` (Tìm kiếm khách hàng tiềm năng)
- `VIDEO_VIEWS` (Lượt xem video)
- `ENGAGEMENT` (Tương tác cộng đồng)
- `PRODUCT_SALES` (Doanh số sản phẩm - áp dụng cho Video Shopping Ads với nguồn catalog)

### Mục tiêu tối ưu hóa được hỗ trợ khi bật CBO

| `objective_type` ở cấp chiến dịch | `optimization_goal` ở cấp nhóm quảng cáo |
|---|---|
| `REACH` | `REACH` |
| `VIDEO_VIEWS` | `ENGAGED_VIEW`, `ENGAGED_VIEW_FIFTEEN` |
| `TRAFFIC` | `CLICK`, `TRAFFIC_LANDING_PAGE_VIEW` |
| `WEB_CONVERSIONS` | `CONVERT`, `VALUE`, `AUTOMATIC_VALUE_OPTIMIZATION` |
| `APP_PROMOTION` | `INSTALL`, `IN_APP_EVENT`, `VALUE` |
| `LEAD_GENERATION` | `LEAD_GENERATION` |
| `ENGAGEMENT` | `FOLLOWERS`, `PAGE_VISIT` |
| `PRODUCT_SALES` | `INSTALL`, `IN_APP_EVENT`, `CONVERT` |

### Quy trình kích hoạt CBO
1. **Tạo chiến dịch:** Sử dụng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602), đặt `budget_optimize_on` là `TRUE`, chọn `budget_mode` và nhập `budget` ở cấp chiến dịch.
2. **Tạo nhóm quảng cáo:** Sử dụng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114). Bắt buộc chỉ định `optimization_goal` và `bid_type`. Không cần truyền `budget` hay `budget_mode` ở cấp nhóm quảng cáo. Tất cả các nhóm quảng cáo trong cùng chiến dịch CBO phải có cùng `optimization_goal`, `bid_type` và `optimization_event`.
3. **Tạo quảng cáo:** Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

## Tỷ lệ xác minh ngân sách và phạm vi giá trị cho từng loại tiền tệ (`Budget verification ratio and value range for each currency`)
<a id="doc-1737585839634433"></a>
<!-- doc_id: 1737585839634433 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Budget > Budget verification ratio and value range for each currency

Bảng dưới đây liệt kê tỷ lệ xác minh ngân sách (Budget verification ratio) và độ chính xác (Precision) cho từng loại tiền tệ:

| Currency | Code | Budget verification ratio | Precision |
|---|---|---|---|
| US Dollar | USD | 1 | 0.01 |
| Euro | EUR | 1 | 0.01 |
| Japanese Yen | JPY | 100 | 1 |
| Hong Kong Dollar | HKD | 10 | 0.01 |
| British Pound | GBP | 1 | 0.01 |
| Malaysian Ringgit | MYR | 1 | 0.01 |
| Russian Ruble | RUB | 100 | 0.01 |
| South African Rand | ZAR | 10 | 0.01 |
| South Korean Won | KRW | 1,000 | 1 |
| UAE Dirham | AED | 1 | 0.01 |
| Saudi Riyal | SAR | 1 | 0.01 |
| Hungarian Forint | HUF | 1 | 1 |
| Polish Zloty | PLN | 4 | 0.01 |
| Danish Krone | DKK | 10 | 0.01 |
| Swedish Krona | SEK | 10 | 0.01 |
| Norwegian Krone | NOK | 10 | 0.01 |
| Turkish Lira | TRY | 10 | 0.01 |
| Mexican Peso | MXN | 10 | 0.01 |
| Thai Baht | THB | 10 | 0.01 |
| Australian Dollar | AUD | 1 | 0.01 |
| Canadian Dollar | CAD | 1 | 0.01 |
| New Zealand Dollar | NZD | 1 | 0.01 |
| Singapore Dollar | SGD | 1 | 0.01 |
| Swiss Franc | CHF | 1 | 0.01 |
| Chinese Yuan | CNY | 10 | 0.01 |
| Algerian Dinar | DZD | 100 | 0.01 |
| Argentine Peso | ARS | 1 | 0.01 |
| Bangladeshi Taka | BDT | 100 | 0.01 |
| Bolivian Boliviano | BOB | 10 | 0.01 |
| Brazilian Real | BRL | 1 | 0.01 |
| Chilean Peso | CLP | 1,000 | 1 |
| Colombian Peso | COP | 1,000 | 0.01 |
| Costa Rican Colon | CRC | 1,000 | 0.01 |
| Czech Koruna | CZK | 10 | 0.01 |
| Egyptian Pound | EGP | 10 | 0.01 |
| Guatemalan Quetzal | GTQ | 10 | 0.01 |
| Honduran Lempira | HNL | 10 | 0.01 |
| Icelandic Krona | ISK | 100 | 1 |
| Indian Rupee | INR | 100 | 0.01 |
| Indonesian Rupiah | IDR | 10,000 | 1 |
| Israeli Shekel | ILS | 1 | 0.01 |
| Kazakhstani Tenge | KZT | 1,000 | 0.01 |
| Kenyan Shilling | KES | 100 | 0.01 |
| Kuwaiti Dinar | KWD | 1 | 0.01 |
| Moroccan Dirham | MAD | 10 | 0.01 |
| Nigerian Naira | NGN | 1,000 | 0.01 |
| Pakistani Rupee | PKR | 100 | 0.01 |
| Panamanian Balboa | PAB | 1 | 0.01 |
| Paraguayan Guarani | PYG | 10,000 | 1 |
| Peruvian Sol | PEN | 1 | 0.01 |
| Philippine Peso | PHP | 10 | 0.01 |
| Qatari Riyal | QAR | 10 | 0.01 |
| Romanian Leu | RON | 1 | 0.01 |
| Nicaraguan Cordoba | NIO | 10 | 0.01 |
| Venezuelan Bolivar | VEF | 100,000 | 0.01 |
| Macanese Pataca | MOP | 10 | 0.01 |
| Ukrainian Hryvnia | UAH | 10 | 0.01 |
| Uruguayan Peso | UYU | 10 | 0.01 |
| Vietnamese Dong | VND | 10,000 | 1 |


## Chiến dịch Promote (`Promote campaign`)
<a id="doc-1785880454546433"></a>
<!-- doc_id: 1785880454546433 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Promote campaign

Promote (Quảng bá) là công cụ quảng cáo tích hợp sẵn trong ứng dụng di động TikTok, cho phép người dùng nhanh chóng gia tăng mức độ tiếp cận cho video, thúc đẩy lưu lượng truy cập trang web và tăng lượng người theo dõi tài khoản. Khi bạn kích hoạt Promote cho một video trong ứng dụng TikTok, một chiến dịch Promote bao gồm một nhóm quảng cáo Promote và một quảng cáo Promote duy nhất sẽ tự động được khởi tạo trong hệ thống.

### Tính khả dụng trên API (Availability)

Bảng dưới đây nêu rõ các tính năng được hỗ trợ qua API đối với quảng cáo Promote:

> [!NOTE]
> Các endpoint của Business Center không hỗ trợ quảng cáo Promote.

| Feature | Available in API | Related endpoints |
|---|---|---|
| Creating Promote campaigns, Promote ad groups, or Promote ads | ❌ | Không hỗ trợ tạo qua API (/campaign/create/, /adgroup/create/, /ad/create/) |
| Updating Promote campaigns, Promote ad groups, or Promote ads | ❌ | Không hỗ trợ chỉnh sửa qua API |
| Retrieving Promote campaigns, Promote ad groups, or Promote ads | ✅ | • [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986) <br> • [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922) <br> • [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) |
| Running synchronous and asynchronous basic reports and audience reports | ✅ | • [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) <br> • [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602) <br> • [/report/task/check/](../12-api-reference/58-reporting.md#doc-1740302781443073) <br> • [/report/task/download/](../12-api-reference/58-reporting.md#doc-1740302808815618) |
| Previewing Promote ads | ❌ | Không hỗ trợ xem trước qua API |
| Creating or binding automated rules | ❌ | Không hỗ trợ gắn quy tắc tự động |
| Changelog | ❌ | Không hỗ trợ nhật ký thay đổi |
| Ad comments | ❌ | Không hỗ trợ lấy bình luận qua API |
| Negative keywords | ❌ | Không hỗ trợ từ khóa phủ định |

### Trạng thái của quảng cáo Promote (Statuses of Promote ads)
Để tìm hiểu về trạng thái của quảng cáo Promote ở các cấp chiến dịch, nhóm quảng cáo và quảng cáo, hãy xem [Trạng thái phụ được hỗ trợ cho trạng thái chính - Dành cho chiến dịch Promote](quan-ly-chien-dich-tom-tat.md#doc-1757239620352002).

### Các bộ lọc được hỗ trợ cho quảng cáo Promote
Dữ liệu của quảng cáo Promote mặc định bị lọc bỏ trong các endpoint truy vấn (`campaign_system_origins` là `["TT_ADS_PLATFORM"]`). Để lấy dữ liệu quảng cáo Promote, bạn cần đặt tham số `campaign_system_origins` thành `["PROMOTE"]` khi gọi [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986), [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922) hoặc [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770).

### Dữ liệu báo cáo cho quảng cáo Promote (Reporting data for Promote ads)

Bạn có thể chạy báo cáo cơ bản (basic report) hoặc báo cáo đối tượng (audience report) ở cấp chiến dịch, nhóm quảng cáo hoặc quảng cáo cho các chiến dịch Promote. Trong báo cáo đồng bộ, bạn cần thiết lập bộ lọc `campaign_system_origins` là `["PROMOTE"]`. Trong báo cáo bất đồng bộ, dữ liệu Promote được bao gồm mặc định.

#### Chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension | Supported in Basic reports? | Supported in Audience reports? |
|---|---|---|
| `advertiser_id` | ✅ | ✅ |
| `campaign_id` | ✅ | ✅ |
| `adgroup_id` | ✅ | ✅ |
| `ad_id` | ✅ | ✅ |
| `stat_time_day` | ✅ | ✅ |
| `gender` | ❌ | ✅ |
| `age` | ❌ | ✅ |
| `country_code` | ❌ | ✅ |
| `province_id` | ❌ | ✅ |
| `dma_id` | ❌ | ✅ |
| `ac` | ❌ | ✅ |
| `platform` | ❌ | ✅ |
| `interest_category` | ❌ | ✅ |
| `placement` | ❌ | ✅ |
| `ad_type` | ❌ | ✅ |
| `device_brand_id` | ❌ | ✅ |

#### Các chỉ số được hỗ trợ (Supported metrics)

| Field | Description | Supported in Basic reports? | Supported in Audience reports? |
|---|---|---|---|
| Attribute metrics | Nhóm chỉ số thuộc tính | | |
| ↳ `advertiser_name` | Tên tài khoản nhà quảng cáo | ✅ | ✅ |
| ↳ `advertiser_id` | ID tài khoản nhà quảng cáo | ✅ | ✅ |
| Basic metrics | Nhóm chỉ số cơ bản | | |
| ↳ `impressions` | Số lượt hiển thị | ✅ | ✅ |
| ↳ `clicks` | Số lượt nhấp (Trang đích) | ✅ | ✅ |
| ↳ `ctr` | Tỷ lệ nhấp CTR | ✅ | ✅ |
| ↳ `reach` | Lượt tiếp cận | ✅ | ❌ |
| ↳ `cost_per_1000_reached` | Chi phí trên 1.000 người tiếp cận | ✅ | ❌ |
| ↳ `conversion` | Lượt chuyển đổi | ✅ | ✅ |
| ↳ `cost_per_conversion` | Chi phí trên mỗi chuyển đổi (CPA) | ✅ | ✅ |
| ↳ `conversion_rate` | Tỷ lệ chuyển đổi CVR (Lượt nhấp) | ✅ | ✅ |
| ↳ `conversion_rate_v2` | Tỷ lệ chuyển đổi CVR (Lượt hiển thị) | ✅ | ✅ |
| ↳ `real_time_conversion` | Lượt chuyển đổi theo thời gian thực | ✅ | ✅ |
| ↳ `real_time_cost_per_conversion` | Chi phí CPA theo thời gian thực | ✅ | ✅ |
| ↳ `result` | Kết quả | ✅ | ✅ |
| ↳ `cost_per_result` | Chi phí trên mỗi kết quả | ✅ | ✅ |
| Video play metrics | Nhóm chỉ số phát video | | |
| ↳ `video_play_actions` | Lượt xem video | ✅ | ✅ |
| ↳ `video_watched_2s` | Lượt xem video 2 giây | ✅ | ✅ |
| ↳ `video_watched_continuous_2s` | Lượt xem video liên tục 2 giây | ✅ | ✅ |
| ↳ `video_watched_6s` | Lượt xem video 6 giây | ✅ | ✅ |
| ↳ `engaged_view` | Lượt xem tập trung 6 giây (Focused view) | ✅ | ❌ |
| ↳ `engaged_view_15s` | Lượt xem tập trung 15 giây (Focused view) | ✅ | ❌ |
| Engagement metrics | Nhóm chỉ số tương tác | | |
| ↳ `engagements` | Tất cả lượt nhấp (Clicks All) | ✅ | ❌ |
| ↳ `engagement_rate` | Tỷ lệ tương tác tổng thể (CTR All) | ✅ | ❌ |
| ↳ `profile_visits` | Lượt ghé thăm hồ sơ trả phí | ✅ | ✅ |
| ↳ `profile_visits_rate` | Tỷ lệ ghé thăm hồ sơ | ✅ | ✅ |
| ↳ `likes` | Lượt thích trả phí | ✅ | ✅ |
| ↳ `comments` | Lượt bình luận trả phí | ✅ | ✅ |
| ↳ `shares` | Lượt chia sẻ trả phí | ✅ | ✅ |
| ↳ `follows` | Lượt theo dõi trả phí | ✅ | ✅ |
| LIVE metrics | Nhóm chỉ số phát trực tiếp | | |
| ↳ `live_views` | Lượt xem LIVE | ✅ | ❌ |
| ↳ `live_unique_views` | Lượt xem LIVE duy nhất | ✅ | ❌ |
| ↳ `live_effective_views` | Lượt xem LIVE hiệu quả | ✅ | ❌ |
| ↳ `live_product_clicks` | Lượt nhấp vào sản phẩm trong LIVE | ✅ | ❌ |
| In-App Event metrics | Nhóm chỉ số sự kiện trong ứng dụng | | |
| ↳ `total_purchase` | Tổng số lượt mua hàng | ✅ | ❌ |
| ↳ `cost_per_total_purchase` | Chi phí trên mỗi lượt mua hàng | ✅ | ❌ |
| ↳ `value_per_total_purchase` | Giá trị trên mỗi lượt mua hàng | ✅ | ❌ |
| ↳ `total_purchase_value` | Tổng giá trị mua hàng | ✅ | ❌ |
| ↳ `total_active_pay_roas` | ROAS mua hàng | ✅ | ❌ |

### Bộ lọc báo cáo được hỗ trợ (Supported filters)
Các bộ lọc được hỗ trợ bao gồm: `campaign_ids`, `adgroup_ids`, `ad_ids`, `campaign_status`, `adgroup_status`, `ad_status`, `billing_event`, `image_mode`, `create_time`. Xem chi tiết tại [Báo cáo cơ bản - Bộ lọc hỗ trợ](bao-cao-p3.md#doc-1751443975608321) và [Báo cáo đối tượng - Bộ lọc hỗ trợ](bao-cao-p3.md#doc-1751454172429314).
