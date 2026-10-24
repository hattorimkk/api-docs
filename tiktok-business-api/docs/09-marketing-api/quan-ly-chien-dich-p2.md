# Hướng dẫn quản lý chiến dịch — phần 2/2

Tài liệu này là phần tiếp theo (phần 2/2) trong bộ hướng dẫn quản lý chiến dịch quảng cáo TikTok Marketing API. Nội dung bao gồm việc tích hợp Realtime API (RTA) cho nhắm mục tiêu thời gian thực, thiết lập nhóm quảng cáo (Ad group), vị trí hiển thị (Placements) và Tìm kiếm tự động (Automatic Search Placement), các tùy chọn nhắm mục tiêu đối tượng và danh mục quảng cáo đặc biệt (Special Ad Category), tối ưu hóa đấu thầu và giá trị (Value Optimization), ước tính kết quả phân phối (Estimated Delivery Results), cùng toàn bộ quy trình thiết lập quảng cáo (Ad), Smart Creative, ACO, danh tính (Identities), tự công bố AIGC và tự động nâng cao chất lượng quảng cáo.

## API Thời gian thực - Realtime API (`Realtime API`)
<a id="doc-1805437148769281"></a>
<!-- doc_id: 1805437148769281 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Campaign > Realtime API

Bài viết này hướng dẫn cách kích hoạt Realtime API (RTA) cho quảng cáo của bạn. RTA cho phép bạn tích hợp dữ liệu đối tượng theo thời gian thực trực tiếp vào quy trình đấu giá và nhắm mục tiêu để nâng cao hiệu suất phân phối.

### Điều kiện tiên quyết (Prerequisites)
- Đã được cấp quyền truy cập TikTok API for Business.
- Tính năng RTA và đấu thầu RTA (`rta_bid_enabled`) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Bạn cần hoàn tất quy trình onboarding để hệ thống của bạn có thể nhận và phản hồi các yêu cầu RTA từ TikTok.

### Các bước thực hiện (Steps)

#### Kích hoạt RTA cho chiến dịch App Promotion

1. **Tạo chiến dịch:** Sử dụng endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo | Quảng bá ứng dụng (App Promotion) | `objective_type` | `APP_PROMOTION` |
| App promotion type | App install hoặc App retargeting | `app_promotion_type` | `APP_INSTALL` hoặc `APP_RETARGETING` |
| Smart+ Campaign | Tắt (Disabled) | / | Không hỗ trợ tạo Smart+ Campaign có bật RTA |
| Realtime API (RTA) | Bật (Enabled) | `rta_id` | Truyền một trong các RTA ID liên kết với tài khoản quảng cáo |
| Use RTA bid (Optional) | Bật hoặc tắt | `rta_bid_enabled` | `true` hoặc `false` |

2. **Tạo nhóm quảng cáo:** Sử dụng endpoint [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Vị trí hiển thị | **Chọn vị trí hiển thị (Select Placement)** với vị trí TikTok | `placement_type`, `placements` | `placement_type` là `PLACEMENT_TYPE_NORMAL`, `placements` là `["PLACEMENT_TIKTOK"]` |
| Bao gồm kết quả tìm kiếm (Tùy chọn) | Bật (khuyến nghị) hoặc tắt | `search_result_enabled` | `true` hoặc `false` |
| Nhắm mục tiêu đối tượng • Đối tượng ◦ Bao gồm ◦ Loại trừ | Tắt | `audience_ids`, `excluded_audience_ids` | Không truyền |

3. **Tạo quảng cáo:** Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

#### Kích hoạt RTA cho chiến dịch Web Conversions
1. **Tạo chiến dịch:** Gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) với `objective_type` là `WEB_CONVERSIONS`, truyền `rta_id` và tùy chọn `rta_bid_enabled`.
2. **Tạo nhóm quảng cáo:** Gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) chọn vị trí TikTok, không truyền `audience_ids`.
3. **Tạo quảng cáo:** Gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

#### Kích hoạt RTA cho chiến dịch Product Sales
1. **Tạo chiến dịch:** Gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602) với `objective_type` là `PRODUCT_SALES`, truyền `rta_id`.
2. **Tạo nhóm quảng cáo:** Gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Tạo quảng cáo:** Gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) với `product_specific_type`:

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Products | Tất cả sản phẩm hoặc Bộ sản phẩm | `product_specific_type` | `ALL`, `PRODUCT_SET` hoặc `CUSTOMIZED_PRODUCTS` |

## Nhóm quảng cáo (`Ad group`)
<a id="doc-1745292233615362"></a>
<!-- doc_id: 1745292233615362 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group

Sau khi tạo chiến dịch, bạn sẽ tiến hành thiết lập nhóm quảng cáo (Ad group). Ở cấp nhóm quảng cáo, bạn cần cấu hình vị trí hiển thị, tệp đối tượng mục tiêu, ngân sách và lịch trình, chiến lược đấu thầu và nhiều tùy chọn khác.

Khám phá các tài nguyên sau để tìm hiểu chi tiết về nhóm quảng cáo:
- [Tạo nhóm quảng cáo](quan-ly-chien-dich-p2.md#doc-1738857874837506)
- [Vị trí hiển thị (Placements)](quan-ly-chien-dich-p2.md#doc-1745292441739265)
- [Nhắm mục tiêu (Targeting)](quan-ly-chien-dich-p2.md#doc-1745292439329793) bao gồm [Nhắm mục tiêu đối tượng](quan-ly-chien-dich-p2.md#doc-1739381236849665) và [Nhắm mục tiêu theo ngữ cảnh](quan-ly-chien-dich-p2.md#doc-1745292519923713)
- [An toàn thương hiệu (Brand safety)](quan-ly-chien-dich-tom-tat.md#doc-1739381752981505)
- [Sự kiện chuyển đổi (Conversion events)](quan-ly-chien-dich-p2.md#doc-1739361474981889)
- [Đấu thầu (Bidding)](quan-ly-chien-dich-p2.md#doc-1745292444424193) và Tối ưu hóa giá trị (Value optimization)
- [Cửa sổ phân bổ và cách tính sự kiện](quan-ly-chien-dich-tom-tat.md#doc-1777694366654465)
- [Trạng thái phụ được hỗ trợ](quan-ly-chien-dich-tom-tat.md#doc-1757239620352002)
- [Ước tính kết quả phân phối (EDR)](quan-ly-chien-dich-p1.md#doc-1742668394531842)

## Tạo nhóm quảng cáo (`Create an ad group`)
<a id="doc-1738857874837506"></a>
<!-- doc_id: 1738857874837506 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Create an ad group

Sử dụng endpoint [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) để tạo nhóm quảng cáo. Bạn có thể định cấu hình các tham số sau:
- **Thông tin chung:** `advertiser_id`, `campaign_id`, `adgroup_name`.
- **Địa điểm tối ưu hóa:** `promotion_type`.
- **Vị trí hiển thị:** `placement_type` và `placements`.
- **Nhắm mục tiêu:** Đối tượng, nhân khẩu học, sở thích hành vi. Bạn có thể gọi [/ad/audience_size/estimate/](../12-api-reference/07-ad-groups-p1.md#doc-1740302379236353) để ước tính quy mô đối tượng trước khi tạo.
- **Ngân sách:** `budget_mode`, `budget` (nếu không bật CBO ở chiến dịch).
- **Lịch trình:** `schedule_type`, `schedule_start_time`, `schedule_end_time`, `dayparting`.
- **Đấu thầu & Tối ưu hóa:** `bid_type`, `billing_event`, `deep_bid_type`, `optimization_goal`.

### Bước tiếp theo
[Tạo quảng cáo](quan-ly-chien-dich-p2.md#doc-1745292553358338).

## Vị trí hiển thị (`Placements`)
<a id="doc-1745292441739265"></a>
<!-- doc_id: 1745292441739265 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Placements

Vị trí hiển thị cho phép bạn chọn nơi quảng cáo sẽ xuất hiện trước người dùng.

### Loại vị trí hiển thị (`placement_type`)
- **Vị trí tự động (`PLACEMENT_TYPE_AUTOMATIC`):** Tận dụng tất cả các vị trí khả dụng để tối ưu hóa kết quả quảng cáo.
- **Chọn vị trí thủ công (`PLACEMENT_TYPE_NORMAL`):** Cho phép chọn thủ công các ứng dụng muốn phân phối quảng cáo qua tham số `placements`.

### Các vị trí hiển thị hỗ trợ (`placements`)
- **TikTok (`PLACEMENT_TIKTOK`):** Quảng cáo In-feed xuất hiện trên trang "Dành cho bạn" (For You) của TikTok.
- **Pangle (`PLACEMENT_PANGLE`):** Mạng lưới quảng cáo đối tác Pangle.
- **Global App Bundle (`PLACEMENT_GLOBAL_APP_BUNDLE`):** Chuỗi ứng dụng tiêu dùng đa dạng bao gồm CapCut và Fizzo. (Không hỗ trợ mục tiêu Landing Page View).

## Quản lý vị trí hiển thị trong nhóm quảng cáo (`Manage placements in ad groups`)
<a id="doc-1771747626094593"></a>
<!-- doc_id: 1771747626094593 -->

> Đường dẫn: Marketing API > Quản lý chiến dịch > Hướng dẫn > Nhóm quảng cáo > Vị trí hiển thị > Quản lý vị trí hiển thịs in ad groups

Vị trí Tìm kiếm tự động (Automatic Search Placement) cho phép tiếp cận những người dùng đang chủ động tìm kiếm các từ khóa liên quan đến sản phẩm hoặc dịch vụ của bạn trên TikTok. Quảng cáo tìm kiếm sẽ hiển thị dưới dạng nội dung "Được tài trợ" (Sponsored) tại các vị trí khác nhau trên trang kết quả tìm kiếm của TikTok.

### Mục tiêu quảng cáo hỗ trợ
- `APP_PROMOTION` (Quảng bá ứng dụng)
- `WEB_CONVERSIONS` (Chuyển đổi trang web)
- `TRAFFIC` (Lưu lượng truy cập)
- `LEAD_GENERATION` (Tìm kiếm khách hàng tiềm năng)

Tính năng này được kích hoạt thông qua tham số `search_result_enabled` tại cấp nhóm quảng cáo. Xem thêm tại [Tạo quảng cáo Tìm kiếm](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1780164603696130).

## Nhắm mục tiêu (`Targeting`)
<a id="doc-1745292439329793"></a>
<!-- doc_id: 1745292439329793 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Targeting

TikTok cung cấp các tùy chọn nhắm mục tiêu đa dạng ở cấp nhóm quảng cáo để tiếp cận chính xác đối tượng mong muốn:
- [Nhắm mục tiêu đối tượng (Audience targeting)](quan-ly-chien-dich-p2.md#doc-1739381236849665)
- [Nhắm mục tiêu theo ngữ cảnh (Contextual targeting)](quan-ly-chien-dich-p2.md#doc-1745292519923713)


## Nhắm mục tiêu đối tượng (`Audience targeting`)
<a id="doc-1739381236849665"></a>
<!-- doc_id: 1739381236849665 -->

> Đường dẫn: Marketing API > Quản lý chiến dịch > Hướng dẫn > Nhóm quảng cáo > Nhắm mục tiêu > Nhắm mục tiêu đối tượng

Bạn có thể sử dụng các tùy chọn sau để nhắm mục tiêu chính xác tới tệp đối tượng mong muốn ở cấp nhóm quảng cáo.

### Các tùy chọn nhắm mục tiêu thủ công (Manual targeting options)

| Tùy chọn | Trường dữ liệu sử dụng | Mô tả chi tiết |
|---|---|---|
| Demographics | Nhóm nhân khẩu học | |
| ↳ Gender | `gender` | Giới tính mục tiêu: `GENDER_FEMALE`, `GENDER_MALE` hoặc `GENDER_UNLIMITED`. |
| ↳ Age | `age_groups` | Danh sách nhóm tuổi mục tiêu. Xem [Enum - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ Location | `location_ids` hoặc `zipcode_ids` | Danh sách ID địa điểm hoặc mã bưu chính mục tiêu. Sử dụng [/tool/region/](../12-api-reference/70-tools-p1.md#doc-1737189539571713) để tra cứu ID địa điểm. |
| ↳ Language | `languages` | Danh sách ngôn ngữ mục tiêu. Sử dụng [/tool/language/](../12-api-reference/70-tools-p1.md#doc-1737188554152962). |
| ↳ Household income | `household_income` | Thu nhập hộ gia đình (áp dụng tại Hoa Kỳ): `TOP5`, `TOP10`, `TOP10_25`, `TOP25_50`. |
| ↳ Spending power | `spending_power` | Sức mua của người dùng: `ALL` hoặc `HIGH` (người có chi tiêu cao). |
| Interests & Behaviors | Sở thích & Hành vi | |
| ↳ Interests | `interest_category_ids`, `interest_keyword_ids` | Danh mục sở thích chung và từ khóa sở thích. Sử dụng [/targeting/search/](../12-api-reference/70-tools-p1.md#doc-1796638342793218) để tra cứu. |
| ↳ Purchase intention | `purchase_intention_keyword_ids` | Danh mục ý định mua sắm của người dùng. |
| ↳ Video interactions & Creator interactions & Hashtag interactions | `actions` | Danh sách đối tượng hành vi (`action_scene`, `action_category_ids`, `action_period`, `video_user_actions`). |
| ↳ Smart interests & behaviors | `smart_interest_behavior_enabled` | Bật/tắt tính năng Sở thích & Hành vi thông minh. |
| Devices | Thiết bị | |
| ↳ Connection Type | `network_types` | Loại kết nối: `wifi`, `2G`, `3G`, `4G`. |
| ↳ Operation System | `operating_systems` | Hệ điều hành: `android`, `iOS`, `PC`. |
| ↳ Operation System Version | `min_android_version`, `min_ios_version`, `ios14_targeting` | Phiên bản hệ điều hành tối thiểu. |
| ↳ Device Model | `device_model_ids` | Mẫu thiết bị mục tiêu. Tra cứu qua [/tool/device_model/](../12-api-reference/70-tools-p1.md#doc-1737172880570369). |
| ↳ Device Price | `device_price_ranges` | Khoảng giá thiết bị. Ví dụ: `[50, 250]`. |
| ↳ Carrier | `carrier_ids` | Danh sách ID nhà mạng. Tra cứu qua [/tool/carrier/](../12-api-reference/70-tools-p1.md#doc-1737168013095938). |
| ↳ Internet Service Provider (ISP) | `isp_ids` | Nhà cung cấp dịch vụ Internet. Tra cứu qua [/tool/targeting/list/](../12-api-reference/70-tools-p2.md#doc-1762962378261506). |
| Audience | Tệp đối tượng | Tệp đối tượng tùy chỉnh (Custom Audience) hoặc Tệp đối tượng tương tự (Lookalike Audience). |
| ↳ Include Audience | `audience_ids` | Danh sách ID đối tượng cần bao gồm. |
| ↳ Smart audience | `smart_audience_enabled` | Bật/tắt tính năng Đối tượng thông minh (Smart audience). |
| ↳ Exclude Audience | `excluded_audience_ids` | Danh sách ID đối tượng cần loại trừ. |

### Yêu cầu nhắm mục tiêu cho chiến dịch có Danh mục quảng cáo đặc biệt (Special ad categories)
Nếu bạn chỉ định `special_industries` (danh mục ngành hàng đặc biệt như nhà ở, việc làm, tín dụng) cho chiến dịch, các nhóm quảng cáo phải tuân thủ các quy định nghiêm ngặt:

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Automatic targeting | Tắt (Disabled) | `auto_targeting_enabled` | Không truyền |
| Demographics - Location | Tắt nhắm mục tiêu theo Zipcode | `zipcode_ids` | Không truyền |
| Demographics - Gender | Không giới hạn giới tính | `gender` | `GENDER_UNLIMITED` |
| Demographics - Age | Trên 18 tuổi | `age_groups` | Không truyền (khuyến nghị) hoặc nhóm tuổi từ 18+ |
| Demographics - Household income | Tắt | `household_income` | Không truyền |
| Audience - Include | Không sử dụng đối tượng tương tự (Lookalike) | `audience_ids` | Chỉ truyền ID đối tượng non-lookalike |
| Audience - Exclude | Không sử dụng Lookalike, Challenge hoặc Premium | `excluded_audience_ids` | Chỉ truyền đối tượng hợp lệ |
| Interests & Behaviours - Interests | Tắt từ khóa sở thích | `interest_keyword_ids` | Không truyền |

## Danh mục quảng cáo đặc biệt (`Special Ad Category`)
<a id="doc-1783164662979586"></a>
<!-- doc_id: 1783164662979586 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Targeting > Special Ad Category

Danh mục quảng cáo đặc biệt (Special Ad Category) áp dụng cho các nhà quảng cáo phát hành quảng cáo liên quan đến Nhà ở (Housing), Việc làm (Employment) hoặc Tín dụng (Credit) tại một số quốc gia cụ thể (chẳng hạn như Hoa Kỳ hoặc Canada). Để ngăn chặn sự phân biệt đối xử, các tùy chọn nhắm mục tiêu theo độ tuổi, giới tính, mã bưu chính và một số tệp đối tượng tương tự sẽ bị hạn chế hoặc không khả dụng.

Bạn khai báo danh mục đặc biệt qua tham số `special_industries` ở cấp chiến dịch khi gọi endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).

## Bật Nhắm mục tiêu thông minh cho nhóm quảng cáo (`Enable Smart Targeting for your ad groups`)
<a id="doc-1783164826830849"></a>
<!-- doc_id: 1783164826830849 -->

> Đường dẫn: Marketing API > Quản lý chiến dịch > Hướng dẫn > Nhóm quảng cáo > Nhắm mục tiêu > Nhắm mục tiêu đối tượng > Smart Targeting > Enable Smart Targeting for your ad groups

Bài viết này hướng dẫn các bước bật tính năng Nhắm mục tiêu thông minh (Smart Targeting) cho nhóm quảng cáo của bạn để mở rộng tệp đối tượng tiếp cận tiềm năng bằng máy học.

### 1. Tạo chiến dịch
Sử dụng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo (Advertising objective) | Lưu lượng truy cập (Traffic), Quảng bá ứng dụng (App promotion), Tìm kiếm khách hàng tiềm năng (Lead generation), Chuyển đổi trang web (Website conversions) | `objective_type` | `TRAFFIC`, `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS` |
| App promotion type for App promotion objective | App install hoặc App pre-registration | `app_promotion_type` | `APP_INSTALL` hoặc `APP_PREREGISTRATION` |
| Special ad categories | Tắt | `special_industries` | Không truyền |

### 2. Tạo nhóm quảng cáo
Sử dụng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).

| Cài đặt (Setting) | Yêu cầu | Tham số | Cách cấu hình tham số |
|---|---|---|---|
| Placements | **Select Placement** chỉ với vị trí TikTok | `placement_type`, `placements` | `placement_type` là `PLACEMENT_TYPE_NORMAL`, `placements` là `["PLACEMENT_TIKTOK"]` |
| Audience targeting • Saved audience | Tắt | `saved_audience_id` | Không truyền |
| Audience targeting • Automatic targeting | Tắt | `auto_targeting_enabled` | Không truyền |
| Audience targeting • Targeting expansion | Tắt | `targeting_expansion` | Không truyền |
| Audience targeting • Audience • Include | Chỉ định ít nhất 1 đối tượng | `audience_ids` | Truyền giá trị hợp lệ |
| Audience targeting • Audience • Smart audience | Bật | `smart_audience_enabled` | `true` |
| Audience targeting • Interests & Behaviors • Smart interests & behaviors | Bật | `smart_interest_behavior_enabled` | `true` |

## Nhắm mục tiêu theo ngữ cảnh (`Contextual targeting`)
<a id="doc-1745292519923713"></a>
<!-- doc_id: 1745292519923713 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Targeting > Contextual targeting

Nhắm mục tiêu theo ngữ cảnh (Contextual targeting) cho phép bạn tiếp cận người dùng dựa trên nội dung video mà họ đang xem hoặc các chủ đề họ quan tâm trên TikTok:
- **Sở thích (Interests):** Nhắm mục tiêu những người dùng thể hiện sự quan tâm lâu dài đến các ngành hàng cụ thể qua `interest_category_ids`.
- **Hành vi video (Video interactions):** Nhắm mục tiêu người dùng đã xem hết, thích, bình luận hoặc chia sẻ video thuộc các chủ đề nhất định trong 7 hoặc 15 ngày qua (`action_scene`: `VIDEO_RELATED`).
- **Hành vi nhà sáng tạo (Creator interactions):** Nhắm mục tiêu người dùng theo dõi hoặc xem trang hồ sơ của nhà sáng tạo nội dung (`action_scene`: `CREATOR_RELATED`).
- **Tương tác hashtag (Hashtag interactions):** Nhắm mục tiêu người dùng xem video có gắn hashtag cụ thể (`action_scene`: `HASHTAG_RELATED`).

---

<a id="doc-1739361474981889"></a>
<!-- doc_id: 1739361474981889 -->
# Sự kiện chuyển đổi (Conversion events)
> Đường dẫn: Marketing API > Quản lý chiến dịch > Hướng dẫn > Nhóm quảng cáo > Sự kiện chuyển đổi (Conversion events)
# Sự kiện ứng dụng (App events)
Bảng dưới đây liệt kê các giá trị enum cho sự kiện chuyển đổi (`optimization_event`) trong các sự kiện ứng dụng phục vụ quản lý chiến dịch.

| Giá trị enum cho optimization_event | Loại sự kiện (Event type) | Ghi chú chi tiết |
|---|---|---|
| `ACTIVE` | Cài đặt ứng dụng (Install) | Người dùng cài đặt và mở ứng dụng lần đầu. |
| `ACTIVE_PAY` | Mua hàng (Purchase) | Người dùng hoàn tất giao dịch thanh toán trong ứng dụng. |
| `ACTIVE_REGISTER` | Đăng ký tài khoản (Registration) | Người dùng hoàn tất đăng ký tài khoản. |
| `ADD_TO_WISHLIST` | Thêm vào danh sách yêu thích (Add to Wishlist) | Người dùng thêm sản phẩm vào danh sách mong muốn. |
| `COMPLETE_TUTORIAL` | Hoàn thành hướng dẫn (Complete Tutorial) | Người dùng hoàn tất phần hướng dẫn chơi hoặc sử dụng. |
| `CREATE_GAMEROLE` | Tạo nhân vật (Create Role) | Người dùng tạo nhân vật trong trò chơi. |
| `CREATE_GROUP` | Tạo nhóm (Create Group) | Người dùng khởi tạo một hội nhóm hoặc bang phái. |
| `IN_APP_AD_CLICK` | Nhấp quảng cáo trong app (In-App Ad Click) | Người dùng nhấp vào quảng cáo hiển thị trong ứng dụng. |
| `IN_APP_AD_IMPR` | Lượt hiển thị quảng cáo trong app (In-App Ad Impression) | Quảng cáo được hiển thị bên trong ứng dụng. |
| `IN_APP_CART` | Thêm vào giỏ hàng (Add to Cart) | Người dùng thêm mặt hàng vào giỏ hàng trong ứng dụng. |
| `IN_APP_DETAIL_UV` | Xem nội dung (View Content) | Người dùng truy cập và xem chi tiết trang sản phẩm/nội dung. |
| `JOIN_GROUP` | Tham gia nhóm (Join Group) | Người dùng tham gia vào hội nhóm hoặc bang phái. |
| `LAUNCH_APP` | Mở ứng dụng (Launch App) | Người dùng khởi chạy ứng dụng. |
| `LIVE_CLICK_PRODUCT_ACTION` | / | Số lượt nhấp vào liên kết sản phẩm trong các phiên mua sắm phát trực tiếp (Live Shopping). Có hiệu lực khi `promotion_type` là `LIVE_SHOPPING` và `optimization_goal` là `PRODUCT_CLICK_IN_LIVE`. ⏎ **Lưu ý**: `LIVE_CLICK_PRODUCT_ACTION` hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt. |
| `LIVE_STAY_TIME` | / | Thời gian xem và lưu lại trong phòng mua sắm phát trực tiếp (Live Shopping). Có hiệu lực khi `promotion_type` là `LIVE_SHOPPING` và `optimization_goal` là `MT_LIVE_ROOM`. ⏎ **Lưu ý**: `LIVE_STAY_TIME` hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt. |
| `LOAN_COMPLETION` | Giải ngân khoản vay (Loan Disbursement) | Hoàn tất quy trình giải ngân tài chính. |
| `LOGIN` | Đăng nhập (Login) | Người dùng đăng nhập vào hệ thống ứng dụng. |
| `NEXT_DAY_OPEN` | Duy trì ngày đầu (Day 1 Retention) | Người dùng mở lại ứng dụng vào ngày hôm sau. |
| `RATE` | Đánh giá xếp hạng (Rate) | Người dùng gửi xếp hạng hoặc đánh giá chất lượng. |
| `SALES_LEAD` | Tạo khách hàng tiềm năng (Generate Lead) | Thu thập thành công thông tin khách hàng tiềm năng. |
| `SEARCH` | Tìm kiếm (Search) | Người dùng thực hiện thao tác tìm kiếm trong ứng dụng. |
| `SPEND_CREDITS` | Sử dụng điểm/tiền tệ (Spend Credit) | Người dùng tiêu xài tiền tệ, xu hoặc điểm trong ứng dụng. |
| `UNLOCK_ACHIEVEMENT` | Mở khóa thành tích (Unlock Achievement) | Người dùng mở khóa danh hiệu hoặc thành tích mới. |
| `UPDATE_LEVEL` | Đạt cấp độ (Achieve Level) | Người dùng thăng hạng hoặc đạt cấp bậc mới trong ứng dụng. |
| `ENGAGED_VIEW` | / | Chỉ hợp lệ khi `optimization_goal` là `ENGAGED_VIEW`. ⏎ Lượt xem tập trung 6 giây (Focused view). ⏎ Số lần video được phát ít nhất 6 giây hoặc nhận được tối thiểu 1 lượt tương tác trong vòng 1 ngày kể từ khi người dùng xem quảng cáo trả phí. Các tương tác được đo lường bao gồm: Thích, chia sẻ, theo dõi, truy cập trang hồ sơ, nhấp liên kết, nhấp hashtag, nhấp âm thanh, nhấp liên kết ghim (anchor) và nhấp tiện ích tương tác. |
| `ENGAGED_VIEW_FIFTEEN` | / | Chỉ hợp lệ khi `optimization_goal` là `ENGAGED_VIEW_FIFTEEN`. ⏎ Lượt xem tập trung 15 giây (Focused view). ⏎ Số lần video được phát ít nhất 15 giây hoặc nhận được tối thiểu 1 lượt tương tác trong vòng 1 ngày kể từ khi người dùng xem quảng cáo trả phí. Các tương tác đo lường tương tự như trên. |
| `LANDING_PAGE_VIEW` | / | Lượt xem trang đích (Landing Page View). Người dùng nhấp vào quảng cáo và tải thành công nội dung trang đích. ⏎ Sự kiện chuyển đổi `LANDING_PAGE_VIEW` được hỗ trợ cho cả hai mục tiêu Lưu lượng truy cập (Traffic) và Doanh số sản phẩm (Product Sales). • Để sử dụng cho mục tiêu Traffic, xem [Danh mục giá trị enum - Mục tiêu tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). • Để sử dụng cho mục tiêu Product Sales, xem [Tối ưu hóa lượt xem trang đích cho Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1775099621140482). ⏎ **Lưu ý**: Nếu `optimization_event` của nhóm quảng cáo được đặt là `LANDING_PAGE_VIEW` và `objective_type` là `TRAFFIC`, nhóm quảng cáo đó không thể gắn vào thử nghiệm phân tách (split test). |
| `PAGE_VISIT` | / | Lượt truy cập Trang hồ sơ TikTok và các trang TikTok khác (bao gồm danh sách phát, hashtag, âm nhạc, hiệu ứng...). ⏎ **Lưu ý**: Khi `optimization_goal` là `PAGE_VISIT`, `optimization_event` sẽ được hệ thống tự động thiết lập là `PAGE_VISIT`. |
| `MESSAGE` | / | Chỉ hợp lệ khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` hoặc `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` và `optimization_goal` là `CONVERSATION`. ⏎ Thu thập khách hàng tiềm năng qua tin nhắn trực tiếp TikTok hoặc ứng dụng nhắn tin tức thì. ⏎ **Lưu ý**: Nếu `promotion_type` được đặt là một trong hai giá trị trên và `optimization_goal` là `CONVERSATION`, trường `optimization_event` có thể bỏ qua và mặc định là `MESSAGE`. |
| `DESTINATION_VISIT` | / | Chỉ hợp lệ khi `optimization_goal` là `DESTINATION_VISIT`. ⏎ Lượt truy cập trang đích. Quảng cáo với mục tiêu tối ưu này sẽ điều hướng người dùng đến trang trong ứng dụng hoặc chuyển tiếp dự phòng sang trang web. ⏎ **Lưu ý**: • Mục tiêu tối ưu hóa Destination Visit (`DESTINATION_VISIT`) hiện là tính năng danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok để kích hoạt. • Khi đã chọn `optimization_goal` là `DESTINATION_VISIT`, trường `optimization_event` có thể bỏ qua và mặc định là `DESTINATION_VISIT`. Nếu truyền giá trị khác, hệ thống sẽ bỏ qua. |
| `AD_REVENUE_VALUE` | Doanh thu quảng cáo (Ad revenue) | Chỉ áp dụng cho kịch bản VBO IAA (Tối ưu hóa theo giá trị doanh thu quảng cáo trong ứng dụng). ⏎ Tối ưu hóa doanh thu nhận được từ quảng cáo hiển thị trong ứng dụng. ⏎ Để tìm hiểu thêm về VBO IAA, xem [Tối ưu hóa theo giá trị - Các loại giá trị](quan-ly-chien-dich-p2.md#doc-1739381743067137). ⏎ **Lưu ý**: Nếu bạn bật VBO khi tạo nhóm quảng cáo bằng cách đặt `optimization_event` thành `IMPRESSION_LEVEL_AD_REVENUE` hoặc `AD_REVENUE_VALUE` (hai enum này hoàn toàn tương đương và có cùng tác dụng), hệ thống sẽ luôn trả về `IMPRESSION_LEVEL_AD_REVENUE` trong phản hồi. |

## Mục tiêu tối ưu hóa phụ (Secondary optimization goal)

Bảng dưới đây liệt kê các giá trị enum cho sự kiện chuyển đổi sâu (`secondary_optimization_event`) trong các sự kiện ứng dụng. Trường này xác định mục tiêu tối ưu hóa phụ khi `optimization_goal` là `INSTALL` hoặc `VALUE`.

| Giá trị enum cho secondary_optimization_event | Mô tả chi tiết |
|---|---|
| `ACTIVE_PAY` | Mua hàng (Purchase). Người dùng hoàn tất quá trình thanh toán trong ứng dụng. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `ACTIVE_REGISTER` | Đăng ký tài khoản (Registration). Người dùng đăng ký thành công tài khoản trong ứng dụng. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `ADD_PAYMENT_INFO` | Thêm thông tin thanh toán (Add Payment Info). |
| `IN_APP_CART` | Thêm vào giỏ hàng (Add To Cart). Người dùng thêm một mặt hàng vào giỏ mua sắm trong ứng dụng. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `IN_APP_ORDER` | Thanh toán đơn hàng (Checkout). |
| `LOAN_APPLY`{-Deprecated} | Nộp hồ sơ vay vốn (Loan Apply). |
| `LOAN_CREDIT`{-Deprecated} | Phê duyệt hạn mức vay (Loan Approval). |
| `NEXT_DAY_OPEN` | Duy trì ngày đầu (Day 1 Retention). Người dùng mở lại ứng dụng ngày hôm sau. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `PURCHASE_ROI` | Lợi tức đầu tư mua hàng (ROI of the purchase). ⏎ Có hiệu lực khi `optimization_goal` là `VALUE`. |
| `START_TRIAL`{-Deprecated} | Bắt đầu dùng thử (Start Trial). |
| `SUBSCRIBE` | Đăng ký thuê bao (Subscribe). Người dùng đăng ký kênh hoặc gói dịch vụ trong ứng dụng. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `UPDATE_LEVEL` | Đạt cấp độ (Achieve Level). Người dùng đạt đến một cấp bậc nhất định trong trò chơi. ⏎ Có hiệu lực khi `optimization_goal` là `INSTALL`. |
| `DAY7_RETENTION` | Duy trì ngày thứ 7 (Day 7 retention). ⏎ Có hiệu lực khi đáp ứng đồng thời các điều kiện: • Cấp chiến dịch: `objective_type` = `APP_PROMOTION` hoặc `APP_INSTALL`. • Cấp nhóm quảng cáo: `placements` = `PLACEMENT_PANGLE`, `optimization_goal` = `INSTALL`, `optimization_event` = `ACTIVE`. ⏎ **Lưu ý**: Duy trì ngày thứ 7 hiện là tính năng allowlist. Vui lòng liên hệ đại diện TikTok để kích hoạt. |
| `PREFERRED_LEAD` | Khách hàng tiềm năng ưu tiên (Preferred Leads). Phân phối quảng cáo đến những người có khả năng cao nhất đáp ứng tiêu chuẩn khách hàng tiềm năng mong muốn của bạn. |

# Sự kiện Pixel (Pixel events)
Bảng dưới đây liệt kê các giá trị enum cho sự kiện chuyển đổi (`optimization_event`) trong các sự kiện web phục vụ quản lý chiến dịch.

| Giá trị enum cho optimization_event | Mô tả chi tiết |
|---|---|
| `ADD_BILLING` | Thêm thông tin thanh toán (Add Payment Info) |
| `BUTTON`{-Deprecated} | Nhấp vào nút (Click Button) |
| `CONSULT` | Tư vấn / Liên hệ (Consult) |
| `DOWNLOAD_START` | Tải xuống tệp / ứng dụng (Download) |
| `FORM` | Gửi biểu mẫu khách hàng tiềm năng (Lead) |
| `INITIATE_ORDER` | Bắt đầu thanh toán (Initiate Checkout). Đối với kịch bản mua sắm trực tiếp (`promotion_type`=`LIVE_SHOPPING`), sự kiện này quản lý theo allowlist và chỉ hợp lệ khi `optimization_goal` là `CONVERT`. |
| `ON_WEB_ADD_TO_WISHLIST` | Thêm vào danh sách yêu thích trên web (Add to Wishlist) |
| `ON_WEB_CART` | Thêm vào giỏ hàng trên web (Add to Cart) |
| `ON_WEB_DETAIL` | Xem chi tiết nội dung trên web (View Content) |
| `ON_WEB_ORDER`{-Deprecated} | Đặt hàng trên web (Place an Order) |
| `ON_WEB_REGISTER` | Hoàn tất đăng ký trên web (Complete Registration) |
| `ON_WEB_SEARCH` | Tìm kiếm trên web (Search) |
| `ON_WEB_SUBSCRIBE` | Đăng ký theo dõi / thuê bao trên web (Subscribe) |
| `SHOPPING` | Hoàn tất mua hàng (Purchase) |


---

<a id="doc-1745292444424193"></a>
<!-- doc_id: 1745292444424193 -->
# Đấu thầu (Bidding)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding
Đấu thầu là yếu tố then chốt trong toàn bộ quy trình thiết lập quảng cáo. Bạn có thể sử dụng các tính năng đấu thầu dưới đây để tối ưu hóa việc phân phối quảng cáo của mình.

# Chiến lược giá thầu (Bid strategy)
Chiến lược giá thầu (`bid_type`) xác định cách hệ thống quản lý chi phí trên mỗi kết quả, phân bổ chi tiêu ngân sách và phân phối mẫu quảng cáo. Xem [tại đây](https://ads.tiktok.com/help/article?aid=6731899932019523590) để biết thêm thông tin chi tiết.

Hệ thống cung cấp hai chiến lược giá thầu chính:
- `BID_TYPE_CUSTOM`: Đấu thầu thủ công. Chiến lược này được gọi là **Giới hạn chi phí (Cost Cap)** trên giao diện TikTok Ads Manager.
- `BID_TYPE_NO_BID`: Không kiểm soát giá thầu, chi tiêu toàn bộ ngân sách để thu về lượng kết quả tối đa có thể. Chiến lược này được gọi là **Phân phối tối đa (Maximum Delivery)** trên TikTok Ads Manager.

# Sự kiện tính phí (Billing event)
Sự kiện tính phí (`billing_event`) xác định thời điểm bạn phải trả phí cho quảng cáo. Xem [tại đây](https://ads.tiktok.com/help/article?aid=9686) để tìm hiểu chi tiết.

Chúng tôi hỗ trợ các loại sự kiện tính phí sau:
- `CPC`: Giá thầu là chi phí bạn sẵn sàng trả cho mỗi lượt nhấp (Cost per click).
- `CPM`: Giá thầu là mức giá bạn sẵn sàng trả cho mỗi 1.000 lượt hiển thị (Cost per mille).
- `CPV`: Giá thầu là mức giá bạn sẵn sàng trả cho mỗi lượt xem video (Cost per view).
- `OCPC`: Giá thầu tối ưu hóa cho mỗi lượt nhấp (Optimized cost per click).
- `GD`: Phân phối đảm bảo (Guaranteed delivery).
- `OCPM`: Giá thầu tối ưu hóa cho mỗi 1.000 lượt hiển thị (Optimized cost per mille).

# Giới hạn giá thầu (Bidding limits)
Giới hạn giá thầu phụ thuộc vào loại tiền tệ của tài khoản quảng cáo, sự kiện tính phí được chọn, cùng mức ngân sách ở cấp nhóm quảng cáo và cấp chiến dịch. Để thiết lập giá thầu, bạn cần đặt `bid_type` là `BID_TYPE_CUSTOM` ở cấp nhóm quảng cáo và truyền vào trường `bid_price` hoặc `conversion_bid_price`. Cơ chế xác thực giá thầu bao gồm ba bước kiểm tra:
1. Độ chính xác thập phân của tiền tệ: Các loại tiền tệ khác nhau quy định số chữ số thập phân tối đa khác nhau. Ví dụ: Đô la Mỹ (USD) cho phép tối đa hai chữ số thập phân, trong khi Yên Nhật (JPY) chỉ cho phép số nguyên.
2. Giới hạn giá thầu tối đa: Mức giá thầu trần được tính bằng **Mức giá định danh cơ sở của sự kiện tính phí (`billing_event`) * Tỷ lệ xác thực giá thầu theo tiền tệ (Bid Verification Ratio)**. Ví dụ: Nếu sự kiện tính phí là CPC (giới hạn cơ sở = 30) và tiền tệ là JPY (tỷ lệ xác thực = 100), mức giá thầu tối đa có thể đặt là 3.000 JPY.
> **Lưu ý:** Tỷ lệ xác thực giá thầu giống hệt Tỷ lệ xác thực ngân sách. Xem tỷ lệ cho từng loại tiền tệ tại mục [Tiền tệ](quan-ly-chien-dich-p1.md#doc-1737585839634433), **HOẶC** tra cứu mức giá thầu tối đa trực tiếp tại [Giới hạn giá thầu](quan-ly-chien-dich-p2.md#doc-1750444779586561).
3. Giới hạn ngân sách: Giá thầu bắt buộc phải thấp hơn ngân sách thiết lập cho nhóm quảng cáo và chiến dịch.

# Giá thầu đề xuất (Suggested bid)
Ứng dụng công nghệ máy học phân tích thiết lập quảng cáo và dữ liệu phân phối lịch sử, tính năng giá thầu đề xuất mang lại gợi ý tối ưu và khoa học nhất cho quảng cáo của bạn. Xem [tại đây](https://ads.tiktok.com/help/article?aid=9683) để tìm hiểu chi tiết.

Bạn có thể lấy giá thầu gợi ý bằng cách gọi endpoint [/tool/bid/recommend/](../12-api-reference/70-tools-p2.md#doc-1737107845597186). Lưu ý rằng giá thầu gợi ý chỉ áp dụng được với chiến lược giá thầu **Giới hạn chi phí (Cost Cap)** (`bid_type` = `BID_TYPE_CUSTOM`).


---

<a id="doc-1739381743067137"></a>
<!-- doc_id: 1739381743067137 -->
# Tối ưu hóa theo giá trị (Value-Based Optimization)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding > Value-Based Optimization
Tối ưu hóa theo giá trị (Value-Based Optimization - VBO) là phương pháp phân phối quảng cáo hướng tới những đối tượng người dùng có tiềm năng trở thành khách hàng mang lại giá trị cao. VBO bao gồm một mục tiêu tối ưu hóa mang tên `VALUE` với hai loại giá trị riêng biệt và hai chiến lược đấu thầu. Hai chiến lược đấu thầu này được định cấu hình qua trường `deep_bid_type`.

## Các loại giá trị (dành cho Ứng dụng)
Khi bạn đã thiết lập mục tiêu tối ưu hóa là Giá trị (`VALUE`), bạn có thể lựa chọn một trong hai loại giá trị sau:
- **Giá trị mua hàng (Purchase Value)**: Còn gọi là VBO IAP (Tối ưu hóa giá trị từ mua hàng trong ứng dụng), giúp tối đa hóa doanh thu từ các giao dịch thanh toán trong ứng dụng. Loại giá trị này nhắm mục tiêu tới những người dùng có xu hướng chi tiêu nhiều tiền trong app.
- **Giá trị doanh thu quảng cáo (Ad Revenue Value)**: Còn gọi là VBO IAA (Tối ưu hóa giá trị từ doanh thu quảng cáo trong ứng dụng). Loại giá trị này ưu tiên phân phối tới những người dùng có khả năng xem nhiều quảng cáo và tạo ra doanh thu quảng cáo lớn nhất cho bạn.

Lưu ý rằng mục tiêu tối ưu hóa Giá trị (`VALUE`) cũng được hỗ trợ cho các trang web, giúp tối ưu hóa giá trị đơn hàng trên website. Tuy nhiên, hai loại giá trị phân tách ở trên áp dụng riêng cho ứng dụng di động.

Lựa chọn đúng loại giá trị VBO giúp chiến lược quảng cáo bám sát mục tiêu doanh thu của doanh nghiệp.

> **Lưu ý:** Tính năng VBO IAP và VBO IAA trong các trường hợp khác nhau hiện là tính năng danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt. Một số tính năng VBO sẽ tự động mở khóa khi tài khoản của bạn đạt đủ điều kiện. Để biết tiêu chuẩn mở khóa, tham khảo [Kích hoạt Tối ưu hóa theo giá trị - Tiêu chuẩn mở khóa VBO](quan-ly-chien-dich-tom-tat.md#doc-1770019181843458).

## Các chiến lược đấu thầu (Bidding strategies)

* **`VO_HIGHEST_VALUE`**: Giá trị cao nhất (Highest Value). Đấu thầu tự động không kèm mục tiêu ROAS hay mức trần chi phí.
* **`VO_MIN_ROAS`**: ROAS tối thiểu (Minimum ROAS). Đặt giá thầu gắn liền với mục tiêu tỷ suất hoàn vốn ROAS cụ thể.
* **`VO_MIN`** (không còn hỗ trợ): Giới hạn chi phí (Cost Cap). Đặt giá thầu kèm mức trần chi phí. Lưu ý rằng chiến lược này chỉ từng hỗ trợ mục tiêu `PRODUCT_SALES` và đã dừng hoạt động từ cuối tháng 6/2023.

## Giới hạn và điều kiện (Limits)

* Hỗ trợ 3 mục tiêu quảng cáo: `APP_PROMOTION`, `WEB_CONVERSIONS`, `PRODUCT_SALES`.
* Có thể quảng bá cho website, ứng dụng Android hoặc iOS.
* Chỉ hỗ trợ sự kiện tính phí oCPM (`billing_event` = `OCPM`).

## Hướng dẫn bật VBO (Enable VBO)
Để tìm hiểu cách kích hoạt VBO, vui lòng tham khảo [Kích hoạt Tối ưu hóa theo giá trị trong Smart+ Campaign](quan-ly-chien-dich-tom-tat.md#doc-1840137502583809) và [Kích hoạt Tối ưu hóa theo giá trị trong Chiến dịch thủ công](quan-ly-chien-dich-tom-tat.md#doc-1770019181843458).


---

<a id="doc-1750444779586561"></a>
<!-- doc_id: 1750444779586561 -->
# Giới hạn giá thầu (Bidding limits)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding > Bidding limits
Vui lòng tham khảo bảng dưới đây để tra cứu độ chính xác thập phân cho phép của từng loại tiền tệ và mức giá thầu tối đa tương ứng với từng sự kiện tính phí.

| Tiền tệ (Currency) | Mã (Code) | Độ chính xác (Precision) | Giá thầu tối đa CPC | Giá thầu tối đa CPM | Giá thầu tối đa CPV | Giá thầu tối đa OCPC | Giá thầu tối đa GD | Giá thầu tối đa OCPM |
|---|---|---|---|---|---|---|---|---|
| Bảng Anh (British Pound) | `GBP` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Nhân dân tệ (Chinese Yuan) | `CNY` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Euro | `EUR` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Đô la Hồng Kông (Hong Kong Dollar) | `HKD` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Yên Nhật (Japanese Yen) | `JPY` | 1 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Đô la Mỹ (US Dollar) | `USD` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Dinar Algeria (Algerian Dinar) | `DZD` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Peso Argentina (Argentine Peso) | `ARS` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Đô la Úc (Australian Dollar) | `AUD` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Taka Bangladesh (Bangladeshi Taka) | `BDT` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Boliviano Bolivia (Bolivian Boliviano) | `BOB` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Real Brazil (Brazilian Real) | `BRL` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Đô la Canada (Canadian Dollar) | `CAD` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Peso Chile (Chilean Peso) | `CLP` | 1 | 30000 | 120000 | 120000 | 1500000 | 30000 | 1500000 |
| Peso Colombia (Colombian Peso) | `COP` | 0.01 | 30000 | 120000 | 120000 | 1500000 | 30000 | 1500000 |
| Colon Costa Rica (Costa Rican Colon) | `CRC` | 0.01 | 30000 | 120000 | 120000 | 1500000 | 30000 | 1500000 |
| Koruna Séc (Czech Koruna) | `CZK` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Krone Đan Mạch (Danish Krone) | `DKK` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Bảng Ai Cập (Egyptian Pound) | `EGP` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Quetzal Guatemala (Guatemalan Quetzal) | `GTQ` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Lempira Honduras (Honduran Lempira) | `HNL` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Forint Hungary (Hungarian Forint) | `HUF` | 1 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Krona Iceland (Icelandic Krona) | `ISK` | 1 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Rupee Ấn Độ (Indian Rupee) | `INR` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Rupiah Indonesia (Indonesian Rupiah) | `IDR` | 1 | 300000 | 1200000 | 1200000 | 15000000 | 300000 | 15000000 |
| Shekel mới Israel (Israeli New Shekel) | `ILS` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Shilling Kenya (Kenyan Shilling) | `KES` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Pataca Ma Cao (Macanese Pataca) | `MOP` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Ringgit Malaysia (Malaysian Ringgit) | `MYR` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Peso Mexico (Mexican Peso) | `MXN` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Tân Đài tệ (New Taiwan Dollar) | `TWD` | 1 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Đô la New Zealand (New Zealand Dollar) | `NZD` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Cordoba Nicaragua (Nicaraguan Cordoba) | `NIO` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Naira Nigeria (Nigerian Naira) | `NGN` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Krone Na Uy (Norwegian Krone) | `NOK` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Rupee Pakistan (Pakistani Rupee) | `PKR` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Guarani Paraguay (Paraguayan Guarani) | `PYG` | 1 | 300000 | 1200000 | 1200000 | 15000000 | 300000 | 15000000 |
| Sol Peru (Peruvian Nuevo Sol) | `PEN` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Peso Philippines (Philippine Peso) | `PHP` | 0.01 | 1500 | 6000 | 6000 | 75000 | 1500 | 75000 |
| Zloty Ba Lan (Polish Zloty) | `PLN` | 0.01 | 120 | 480 | 480 | 6000 | 120 | 6000 |
| Riyal Qatar (Qatari Riyal) | `QAR` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Leu Romania (Romanian Leu) | `RON` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Rúp Nga (Russian Ruble) | `RUB` | 0.01 | 3000 | 12000 | 12000 | 150000 | 3000 | 150000 |
| Riyal Ả Rập Xê Út (Saudi Riyal) | `SAR` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Đô la Singapore (Singapore Dollar) | `SGD` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Rand Nam Phi (South African Rand) | `ZAR` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Won Hàn Quốc (South Korean Won) | `KRW` | 1 | 30000 | 120000 | 120000 | 1500000 | 30000 | 1500000 |
| Krona Thụy Điển (Swedish Krona) | `SEK` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Franc Thụy Sĩ (Swiss Franc) | `CHF` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Baht Thái (Thai Baht) | `THB` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Lira Thổ Nhĩ Kỳ (Turkish Lira) | `TRY` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Dirham UAE (UAE Dirham) | `AED` | 0.01 | 30 | 120 | 120 | 1500 | 30 | 1500 |
| Hryvnia Ukraina (Ukrainian Hryvnia) | `UAH` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Peso Uruguay (Uruguayan Peso) | `UYU` | 0.01 | 300 | 1200 | 1200 | 15000 | 300 | 15000 |
| Bolivar Venezuela (Venezuelan Bolivar) | `VEF` | 0.01 | 3000000 | 12000000 | 12000000 | 150000000 | 3000000 | 150000000 |
| Đồng Việt Nam (Vietnamese Dong) | `VND` | 1 | 300000 | 1200000 | 1200000 | 15000000 | 300000 | 15000000 |

---

<a id="doc-1746463274713089"></a>
<!-- doc_id: 1746463274713089 -->
# Ước tính kết quả phân phối (Estimated Delivery Results)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results
Ước tính kết quả phân phối (Estimated Delivery Results - EDR) là tính năng hỗ trợ nâng cao hiệu suất nhóm quảng cáo bằng cách cung cấp các đề xuất giá thầu và ngân sách dựa trên thuật toán máy học. Các đề xuất này được phân tích từ dữ liệu lịch sử phân phối, cho phép bạn dự báo hiệu suất nhóm quảng cáo đang chạy trong nhiều kịch bản ngân sách và giá thầu khác nhau, giúp tối ưu hóa chi tiêu và tối đa hóa kết quả kinh doanh.
 
> **Lưu ý:** **Các đề xuất chỉ có hiệu lực trong ngày nhận đề xuất (theo múi giờ của tài khoản nhà quảng cáo) và kết quả ước tính chỉ áp dụng cho ngày hôm đó.**
 
- Xem [Nhận ngân sách đề xuất (Get recommended budgets)](quan-ly-chien-dich-p2.md#doc-1746463333984258) để tìm hiểu cách sử dụng EDR cho ngân sách.
- Xem [Nhận giá thầu đề xuất (Get recommended bids)](quan-ly-chien-dich-p2.md#doc-1746463347473410) để tìm hiểu cách sử dụng EDR cho giá thầu.


---

<a id="doc-1746463333984258"></a>
<!-- doc_id: 1746463333984258 -->
# Nhận ngân sách đề xuất (Get recommended budgets)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended budgets
Tính năng EDR ngân sách (Budget EDR) cho phép bạn áp dụng mức ngân sách tối ưu từ kết quả ước tính để mở rộng quy mô nhóm quảng cáo và thúc đẩy thêm nhiều chuyển đổi hơn. Kết quả ước tính (dành cho hiệu suất nhóm quảng cáo trong cùng ngày) bao gồm 15 bộ dữ liệu tương ứng với các tỷ lệ tăng ngân sách từ -20% đến 50% (bước nhảy 5%), cùng dữ liệu tăng trưởng chuyển đổi ước tính tương ứng.

## Điều kiện tiên quyết (Prerequisites)
Vui lòng bảo đảm các điều kiện sau được thỏa mãn trước khi gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378) để nhận đề xuất ước tính ngân sách:

### Ở cấp chiến dịch (At the campaign level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo (Advertising objective) | Một trong các mục tiêu: <ul><li>Quảng bá ứng dụng (App promotion)</li><li>Chuyển đổi web (Web conversions)</li><li>Tìm kiếm khách hàng tiềm năng (Lead generation)</li></ul> | `objective_type` | Giá trị hợp lệ: <ul><li>`APP_PROMOTION`</li><li>`WEB_CONVERSIONS`</li><li>`LEAD_GENERATION`</li></ul> |
| Tối ưu hóa ngân sách chiến dịch (Campaign Budget Optimization - CBO) | Tắt (Disabled) | `budget_optimize_on` | `false` |

### Ở cấp nhóm quảng cáo (At the ad group level)
> **Lưu ý:**
> Kết quả ước tính phân phối ngân sách được đưa ra theo cấu hình nhóm quảng cáo cụ thể. Nếu bạn đánh giá nhiều nhóm quảng cáo có cùng cấu hình qua `/tool/diagnosis/get/`, hệ thống chỉ trả về kết quả cho nhóm quảng cáo được tạo sớm nhất.

| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Vị trí hiển thị (Placement) | <ul><li><strong>Vị trí tự động (Automatic Placement)</strong> hoặc </li><li><strong>Chọn vị trí hiển thị (Select Placement)</strong> có bao gồm vị trí TikTok</li></ul> | `placement_type` & `placements` | <ul><li> Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc </li><li> Đặt `placement_type` là `PLACEMENT_TYPE_NORMAL` và bao gồm `PLACEMENT_TIKTOK` trong `placements`</li></ul> |
| Quảng cáo phát trực tiếp (Live ads) | Tắt (Disabled) | `promotion_type` | <strong>Khác</strong> `LIVE_SHOPPING` |
| Loại ngân sách (Budget type) | Ngân sách hàng ngày (Daily budget) | `budget_mode` | `BUDGET_MODE_DAY` |
| Mục tiêu tối ưu hóa (Optimization goal) | Một trong các mục tiêu: <ul><li> Lượt nhấp (Click) </li><li> Cài đặt (Install) </li><li>Khách hàng tiềm năng (Leads)</li><li>Chuyển đổi (Conversions)</li><li>Cuộc trò chuyện (Conversations)</li></ul> | `optimization_goal` | Giá trị hợp lệ: <ul><li>`CLICK`</li><li>`INSTALL`</li><li>`LEAD_GENERATION`</li><li>`CONVERT`</li><li>`CONVERSATION`</li></ul> |
| Chiến lược giá thầu (Bidding strategy) | Phân phối tối đa (Maximum Delivery) | `bid_type` | `BID_TYPE_NO_BID` |
| Sự kiện tính phí (Billing Event) | Loại `OCPX` | `billing_event` | `OCPC` hoặc `OCPM` |
| Tối ưu hóa sự kiện ứng dụng & VBO (App Event Optimization & Value-based Optimization) | Cả hai đều tắt (Both disabled) | `deep_bid_type` | `DEFAULT` |
| Ngân sách theo lịch (Scheduled budget) | Tắt (Disabled) | `scheduled_budget` | Không thiết lập qua [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817) |
| Yêu cầu khác (Other) | <ul><li> Không điều chỉnh ngân sách nhóm quảng cáo trong ngày muốn lấy đề xuất từ [/delivery/budget/recommend/](../12-api-reference/70-tools-p2.md#doc-1746463695763458).</li><li> Có ít nhất <strong>5</strong> lượt chuyển đổi trong ngày gần nhất.</li><li> Không phải nhóm quảng cáo đặt trước (reservation).</li></ul> | / | / |

## Các bước thực hiện (Steps)
Thực hiện các bước sau để sử dụng tính năng EDR Ngân sách:
1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Tạo quảng cáo** bằng cách gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
4. **Lọc ra các nhóm quảng cáo đạt điều kiện chuyển đổi** bằng cách xuất báo cáo. Nhóm quảng cáo cần có ít nhất **5** lượt chuyển đổi trong ngày gần nhất. Khuyến nghị chạy [Báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737), [Báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201), [Báo cáo mẫu tương tác](bao-cao-p3.md#doc-1738864940608513) hoặc [Báo cáo DSA](bao-cao-p3.md#doc-1738864960144385).
5. **Lấy đề xuất ngân sách** thông qua endpoint [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378). Truyền danh sách ID nhóm quảng cáo đạt chuẩn vào trường `adgroup_ids`. Kết quả ước tính phân phối ngân sách nằm trong đối tượng `budget_edr_info`.
6. **Cập nhật ngân sách trong cùng ngày** (theo múi giờ tài khoản nhà quảng cáo) bằng endpoint [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817).

---

<a id="doc-1746463347473410"></a>
<!-- doc_id: 1746463347473410 -->
# Nhận giá thầu đề xuất (Get recommended bids)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended bids
Tính năng EDR giá thầu (Bid EDR) cho phép bạn áp dụng mức giá thầu phù hợp từ kết quả ước tính để mở rộng quy mô nhóm quảng cáo và gia tăng tốc độ cắn tiền ngân sách. Kết quả ước tính (áp dụng trong cùng ngày) bao gồm 9 bộ dữ liệu tương ứng với các tỷ lệ tăng giá thầu từ -10% đến 30% (bước nhảy 5%) cùng dữ liệu chi phí gia tăng ước tính tương ứng.

## Điều kiện tiên quyết (Prerequisites)
Vui lòng bảo đảm các điều kiện sau được thỏa mãn trước khi gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378) để nhận đề xuất giá thầu:

### Ở cấp chiến dịch (At the campaign level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo (Advertising objective) | Một trong các mục tiêu: <ul><li>Quảng bá ứng dụng (App promotion)</li><li>Chuyển đổi web (Web conversions)</li><li>Tìm kiếm khách hàng tiềm năng (Lead generation)</li></ul> | `objective_type` | Giá trị hợp lệ: <ul><li>`APP_PROMOTION`</li><li>`WEB_CONVERSIONS`</li><li>`LEAD_GENERATION`</li></ul> |
| Tối ưu hóa ngân sách chiến dịch (Campaign Budget Optimization - CBO) | Tắt (Disabled) | `budget_optimize_on` | `false` |

### Ở cấp nhóm quảng cáo (At the ad group level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Vị trí hiển thị (Placement) | <ul><li><strong>Vị trí tự động (Automatic Placement)</strong> hoặc </li><li><strong>Chọn vị trí hiển thị (Select Placement)</strong> có bao gồm TikTok</li></ul> | `placement_type` & `placements` | <ul><li> Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc </li><li> Đặt `placement_type` là `PLACEMENT_TYPE_NORMAL` và thêm `PLACEMENT_TIKTOK` vào `placements`</li></ul> |
| Quảng cáo phát trực tiếp (Live ads) | Tắt (Disabled) | `promotion_type` | <strong>Khác</strong> `LIVE_SHOPPING` |
| Loại ngân sách (Budget type) | Ngân sách hàng ngày (Daily budget) | `budget_mode` | `BUDGET_MODE_DAY` |
| Mục tiêu tối ưu hóa (Optimization goal) | Một trong các mục tiêu: <ul><li>Lượt nhấp (Click)</li><li>Cài đặt (Install)</li><li>Khách hàng tiềm năng (Leads)</li><li>Chuyển đổi (Conversions)</li><li>Cuộc trò chuyện (Conversations)</li></ul> | `optimization_goal` | Giá trị hợp lệ: <ul><li>`CLICK`</li><li>`INSTALL`</li><li>`LEAD_GENERATION`</li><li>`CONVERT`</li><li>`CONVERSATION`</li></ul> |
| Chiến lược giá thầu (Bidding strategy) | Giới hạn chi phí (Cost Cap) | `bid_type` | `BID_TYPE_CUSTOM` |
| Sự kiện tính phí (Billing Event) | Loại `OCPX` | `billing_event` | `OCPC` hoặc `OCPM` |
| Tối ưu sự kiện app & VBO (App Event Optimization & Value-based Optimization) | Cả hai đều tắt (Both disabled) | `deep_bid_type` | `DEFAULT` |
| Ngân sách theo lịch (Scheduled budget) | Tắt (Disabled) | `scheduled_budget` | Không thiết lập qua [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817) |
| Yêu cầu khác (Other) | <ul><li>Không điều chỉnh giá thầu nhóm quảng cáo trong ngày muốn lấy đề xuất từ [/delivery/bid/recommend/](../12-api-reference/70-tools-p2.md#doc-1746463732779009).</li><li>Có ít nhất <strong>5</strong> lượt chuyển đổi trong ngày gần nhất.</li><li>Không phải nhóm quảng cáo đặt trước (reservation).</li></ul> | / | / |

## Các bước thực hiện (Steps)
Thực hiện theo các bước sau để áp dụng tính năng EDR Giá thầu:
1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Tạo mẫu quảng cáo** bằng cách gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
4. **Lọc các nhóm quảng cáo thỏa mãn điều kiện chuyển đổi** bằng cách xuất báo cáo (cần có tối thiểu **5** chuyển đổi trong ngày gần nhất). Bạn có thể chạy [Báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737), [Báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201), [Báo cáo mẫu tương tác](bao-cao-p3.md#doc-1738864940608513) hoặc [Báo cáo DSA](bao-cao-p3.md#doc-1738864960144385).
5. **Lấy đề xuất giá thầu** bằng cách gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378). Truyền ID nhóm quảng cáo đạt chuẩn vào trường `adgroup_ids`. Kết quả ước tính nằm trong đối tượng phản hồi `bid_edr_info`.
6. **Cập nhật giá thầu trong cùng ngày** (theo múi giờ tài khoản quảng cáo) bằng endpoint [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745) và gán giá thầu đã chọn vào trường `conversion_bid_price` hoặc `bid_price`.

---

<a id="doc-1745292235571201"></a>
<!-- doc_id: 1745292235571201 -->
# Quảng cáo (Ad)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad
Quảng cáo là đơn vị nhỏ nhất trong cấu trúc chiến dịch và là nội dung hiển thị trực tiếp đến đối tượng khán giả mục tiêu. Nội dung quảng cáo có thể bao gồm video, hình ảnh, văn bản mô tả và các nút kêu gọi hành động (CTA).

**Xem [tại đây](quan-ly-chien-dich-p1.md#doc-1740673047618561) để tìm hiểu chi tiết về bảng đối chiếu giữa các tính năng trên TikTok Ads Manager và cấu hình tham số API.**

Khám phá các tài nguyên sau để tìm hiểu toàn diện về quảng cáo trên TikTok for Business:
- [Tạo quảng cáo (Create an ad)](quan-ly-chien-dich-p2.md#doc-1745292553358338): Hướng dẫn quy trình tạo mẫu quảng cáo.
- [Sáng tạo thông minh (Smart Creative)](quan-ly-chien-dich-p2.md#doc-1767322784934914): Hướng dẫn sử dụng công cụ sáng tạo tự động Smart Creative.
- [Danh tính (Identities)](quan-ly-chien-dich-p2.md#doc-1738958351620097): Giới thiệu các loại danh tính được ủy quyền và các endpoint liên quan để triển khai Spark Ads.
- [Liên kết sâu (Deeplink)](quan-ly-chien-dich-tom-tat.md#doc-1779541971843073): Giới thiệu các loại deeplink, cơ chế chuyển tiếp dự phòng (fallback) và thiết lập phù hợp cho từng trường hợp.
- [Trang sản phẩm tùy chỉnh (Custom Product Pages)](quan-ly-chien-dich-tom-tat.md#doc-1798658439859202): Hướng dẫn cấu hình Custom Product Pages (CPP) của App Store trong quảng cáo.
- [Công tắc tự công bố nội dung AIGC](quan-ly-chien-dich-p2.md#doc-1799186631031809): Giới thiệu các mục tiêu và định dạng hỗ trợ tự công bố nội dung do AI tạo ra (AIGC).
- [Tự động nâng cao chất lượng (Automatic Enhancements)](quan-ly-chien-dich-p2.md#doc-1855450880142402): Hướng dẫn kích hoạt tính năng tự động nâng cao chất lượng nội dung quảng cáo.


---

<a id="doc-1745292553358338"></a>
<!-- doc_id: 1745292553358338 -->
# Tạo quảng cáo (Create an ad)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Create an ad
Bài viết này hướng dẫn chi tiết quy trình tạo mới một mẫu quảng cáo trên TikTok for Business.

# Các bước thực hiện (Steps)

Sử dụng endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) để tạo quảng cáo. Bạn có thể định cấu hình các tham số sau ở cấp quảng cáo:

Để nắm rõ các tính năng ở cấp quảng cáo trên TikTok Ads Manager tương ứng với những tham số API nào, xem [Ánh xạ giữa tính năng chiến dịch trên TikTok Ads Manager và cấu hình API](quan-ly-chien-dich-p1.md#doc-1740673047618561).

- **Thông tin chung (General info):**
  - `advertiser_id`: ID tài khoản nhà quảng cáo.
  - `adgroup_id`: ID nhóm quảng cáo. Để lấy `adgroup_id`, tạo nhóm quảng cáo bằng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) và nhận mã ID trả về từ phản hồi.
  - `ad_name`: Tên mô tả của mẫu quảng cáo.

- **Danh tính phát hành (Identity):**
  - Sử dụng `identity_id` và `identity_type` để chỉ định danh tính hiển thị. Xem [Danh tính (Identities)](quan-ly-chien-dich-p2.md#doc-1738958351620097) để tra cứu các loại danh tính và trường hợp ứng dụng.

- **Tài nguyên sáng tạo (Creative):**
  - Chỉ định các tài nguyên bao gồm nút kêu gọi hành động `call_to_action`/`call_to_action_id`, danh sách ảnh `image_ids`, nội dung văn bản `ad_text`/`ad_texts`, video `video_id` và bài đăng TikTok `tiktok_item_id`. Để tìm hiểu thêm, xem chương [Creatives](creatives.md#doc-1736271785207810).

- **Định dạng quảng cáo (Ad format):**
  - Sử dụng `ad_format` để xác định định dạng hiển thị. Các giá trị enum được hỗ trợ bao gồm `SINGLE_IMAGE`, `SINGLE_VIDEO`, `CAROUSEL_ADS`, `CATALOG_CAROUSEL`, `LIVE_CONTENT`.

- **Theo dõi sự kiện (Tracking):**
  - Sử dụng `tracking_pixel_id`, `tracking_app_id` và `tracking_offline_event_set_ids` để theo dõi và ghi nhận sự kiện chuyển đổi.

Để tra cứu chi tiết toàn bộ các tham số bổ sung khác, vui lòng xem tài liệu endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

## Ví dụ cURL (Example)


---

<a id="doc-1767322784934914"></a>
<!-- doc_id: 1767322784934914 -->
# Sáng tạo thông minh (Smart Creative)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Smart Creative
Smart Creative là công cụ toàn diện ứng dụng trí tuệ nhân tạo (AI), tích hợp liền mạch chẩn đoán nội dung sáng tạo, báo cáo tài nguyên, tự động sản xuất biến thể và tối ưu hóa phân phối trong một quy trình duy nhất. Công cụ giúp nhà quảng cáo tạo ra nhiều nội dung sẵn sàng phân phối từ số lượng nguyên liệu giới hạn và tối đa hóa hiệu quả sinh lời của các tài nguyên đó.

> [!WARNING]
> Bạn không thể tạo quảng cáo Smart Creative trong các nhóm quảng cáo đã có sẵn các mẫu quảng cáo khác bên trong.

## Tạo quảng cáo Smart Creative (Create Smart Creative ads)
1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
- Hiện tại, Smart Creative chỉ hỗ trợ các mục tiêu quảng cáo (`objective_type`) là `APP_PROMOTION`, `WEB_CONVERSIONS`, `TRAFFIC` hoặc `LEAD_GENERATION` ở cấp chiến dịch.
2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
- Thiết lập `creative_material_mode` thành `CUSTOM`.
3. **Tải lên các tài nguyên sáng tạo** thông qua các endpoint:
- Tải lên video bằng [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) và lấy mã `video_id` trả về trong phản hồi.
- Tải lên hình ảnh bằng [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642) và lấy mã `image_id` trả về trong phản hồi.
- Nhận các nút kêu gọi hành động CTA tiêu chuẩn hoặc động qua [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785). Xem chi tiết tại [Gợi ý CTA](creatives.md#doc-1740307296329730).
4. **Tạo quảng cáo Smart Creative** bằng cách gọi [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626).
- Thiết lập `is_smart_creative` thành `true`.
> **Lưu ý:** Khi `is_smart_creative` được đặt là `true`, hệ thống sẽ tự động gán `creative_material_mode` thành `SMART_CREATIVE` ở cấp nhóm quảng cáo.
- Điền mã ID ảnh và ID video thu được từ Bước 3 lần lượt vào các trường `web_uri` và `video_id` (bên trong đối tượng `media_info`).
> **Lưu ý:** Bạn có thể nhập tối đa 30 tài nguyên trong đối tượng `media_info`. Các tài nguyên không được trùng lặp nhau.
- Điền các văn bản CTA nhận được từ Bước 3 vào trường `call_to_action_list` hoặc `call_to_action_id`.
> **Lưu ý:** Bạn có thể nhập tối đa 3 nút kêu gọi hành động (không trùng lặp).
- Điền các tiêu đề văn bản quảng cáo vào trường `title_list`.
> **Lưu ý:** Bạn có thể nhập tối đa 5 đoạn văn bản quảng cáo (không trùng lặp).
- Điền mã ID trang tức thì vào trường `page_id`. • Để lấy danh sách trang tức thì trong tài khoản, gọi [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586). • Để tạo trang tức thì, sử dụng [Instant Page Editor SDK](creatives.md#doc-1740307202170881).


---

<a id="doc-1739470718398465"></a>
<!-- doc_id: 1739470718398465 -->
# (Không còn hỗ trợ) Tối ưu hóa sáng tạo tự động - ACO
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > (Deprecated) Automated Creative Optimization
Tính năng Tối ưu hóa sáng tạo tự động (Automated Creative Optimization - ACO) tự động kết hợp và phân phối các nguyên liệu sáng tạo chất lượng cao.

> [!NOTE]
> Quảng cáo ACO không còn được hỗ trợ trong API hiện tại. Để đảm bảo tích hợp mượt mà, chúng tôi khuyến nghị bạn chuyển đổi sang [Quảng cáo sáng tạo thông minh (Smart Creative)](quan-ly-chien-dich-p2.md#doc-1767322784934914).

Với ACO, bạn có thể tải lên hình ảnh hoặc video, soạn thảo các đoạn văn bản quảng cáo và chọn nút kêu gọi hành động (CTA). Hệ thống sẽ tự động ghép nối các tài nguyên sáng tạo thành nhiều biến thể quảng cáo khác nhau cho chiến dịch. Các quảng cáo này được liên tục thử nghiệm, đánh giá và tối ưu hóa để tìm ra tổ hợp biến số hiệu quả nhất, từ đó phân phối biến thể tốt nhất đến đối tượng mục tiêu. Xem [tại đây](https://ads.tiktok.com/help/article?aid=9529) để tìm hiểu ưu điểm và các thực tiễn tốt nhất của ACO.

# Các mục tiêu quảng cáo được hỗ trợ (Supported objectives)
ACO chỉ được hỗ trợ khi bạn chọn một trong các mục tiêu quảng cáo (`objective_type`) sau cho chiến dịch:
- Quảng bá ứng dụng (`APP_PROMOTION`)
- Chuyển đổi trang web (`WEB_CONVERSIONS`)
- Lưu lượng truy cập (`TRAFFIC`)
- Tìm kiếm khách hàng tiềm năng (`LEAD_GENERATION`)

# Quy tắc tạo tên quảng cáo (Ad name generation rules)
- Nếu truyền một chuỗi hợp lệ vào trường `name` và có truyền `file_name` trong `image_info` hoặc `video_info`, tên quảng cáo sẽ được tạo theo định dạng "adName_" kèm theo số thứ tự, ví dụ: "adName_001".
- Nếu truyền chuỗi rỗng vào trường `name` nhưng có truyền `file_name`, tên quảng cáo sẽ được tạo theo định dạng "file_name" kèm số thứ tự, ví dụ: "image001" hoặc "video_002".
- Nếu truyền chuỗi rỗng vào trường `name` và không truyền `file_name`, tên quảng cáo sẽ tạo theo định dạng "_" kèm số thứ tự, ví dụ: "001". Nên tránh trường hợp này để tên quảng cáo mang ý nghĩa rõ ràng hơn.


---

<a id="doc-1745292500427777"></a>
<!-- doc_id: 1745292500427777 -->
# (Không còn hỗ trợ) Tạo quảng cáo ACO (Create ACO ads)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > (Deprecated) Automated Creative Optimization > (Deprecated) Create ACO ads
> [!NOTE]
> Quảng cáo ACO không còn được hỗ trợ trong API. Để đảm bảo tính tương thích và hiệu suất cao nhất, chúng tôi khuyến nghị bạn chuyển đổi sang [Quảng cáo sáng tạo thông minh (Smart Creative)](quan-ly-chien-dich-p2.md#doc-1767322784934914).

Tài liệu này trình bày quy trình kỹ thuật từng bước tạo quảng cáo Tối ưu hóa sáng tạo tự động (ACO):

1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
  - Chỉ hỗ trợ các mục tiêu quảng cáo (`objective_type`) là `APP_PROMOTION`, `WEB_CONVERSIONS`, `TRAFFIC` và `LEAD_GENERATION`.

2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
  - Đặt `creative_material_mode` thành `DYNAMIC` để kích hoạt ACO.
> **Lưu ý:** Quảng cáo ACO (`creative_material_mode` = `DYNAMIC`) sẽ bị ngừng hỗ trợ trong các phiên bản tương lai. Bạn nên sử dụng [Smart Creative](quan-ly-chien-dich-p2.md#doc-1767322784934914).

3. **Tải lên tài nguyên sáng tạo** qua các endpoint tương ứng:
  - Tải lên video bằng [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) và nhận mã `video_id`.
  - Tải lên hình ảnh bằng [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642) và nhận mã `image_id`.
  - Lấy các văn bản kêu gọi hành động CTA tiêu chuẩn hoặc động qua [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785). Xem [Gợi ý CTA](creatives.md#doc-1740307296329730).
4. **Tạo mẫu quảng cáo ACO** bằng cách gọi endpoint [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626).
  - Truyền mã ID ảnh và video từ Bước 3 vào các trường `web_uri` và `video_id` (bên trong đối tượng `media_info`).
> **Lưu ý:** Bạn có thể nhập tối đa 30 tài nguyên không trùng lặp trong đối tượng `media_info`.
  - Nhập danh sách nút CTA vào `call_to_action_list` hoặc `call_to_action_id` (tối đa 3 nút không trùng lặp).
  - Nhập các tiêu đề quảng cáo vào mảng `title_list` (tối đa 5 tiêu đề không trùng lặp).
  - Điền ID trang tức thì vào trường `page_id`. Bạn có thể lấy mã ID trang bằng [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586).

**Các bước tiếp theo (Next steps)**
Tùy theo nhu cầu vận hành, bạn có thể thực hiện các tác vụ sau:
- Sử dụng [/ad/aco/update/](../12-api-reference/60-smart-creative.md#doc-1739473077112833) để chỉnh sửa tài nguyên của quảng cáo tự động.
- Sử dụng [/ad/aco/material_status/update/](../12-api-reference/60-smart-creative.md#doc-1739506701165570) để cập nhật trạng thái bật/tắt của từng nguyên liệu (văn bản, hình ảnh, video).


---

<a id="doc-1738958351620097"></a>
<!-- doc_id: 1738958351620097 -->
# Danh tính (Identities)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Identities
Với tính năng Danh tính (Identity), bạn có thể tạo Spark Ads bằng cách đẩy các bài đăng từ tài khoản TikTok for Business sang tài khoản TikTok Doanh nghiệp liên kết, hoặc bằng cách kéo các bài đăng từ tài khoản Doanh nghiệp liên kết, từ các bài đăng được ủy quyền hoặc từ các tài khoản TikTok được cấp quyền.

Hệ thống hỗ trợ 5 loại danh tính được ủy quyền:
* **Người dùng tùy chỉnh (Custom User - `CUSTOMIZED_USER`)**: Đại diện cho tài khoản TikTok ảo chỉ dùng cho việc hiển thị quảng cáo in-feed. Loại danh tính này được khởi tạo qua endpoint **/identity/create/**. Ngay cả khi không chạy Spark Ads, chúng tôi vẫn khuyến nghị bạn truyền `identity_id` và `identity_type` (`CUSTOMIZED_USER`) để quản lý thông tin quảng cáo tốt hơn.
* **Người dùng ủy quyền (Authorized User - `AUTH_CODE`)**: Tạo ra khi bạn sử dụng mã cấp quyền (authorization code) để truy cập tài khoản TikTok hoặc bài đăng TikTok.
* **Người dùng TikTok (TikTok User - `TT_USER`)**: Tạo ra khi bạn liên kết tài khoản TikTok for Business với tài khoản TikTok Business, hoặc khi liên kết với tài khoản TikTok thông thường rồi nâng cấp lên Business.
* **Tài khoản TikTok trong Business Center (`BC_AUTH_TT`)**: Tạo ra khi bạn thêm tài khoản TikTok vào Business Center và chủ tài khoản TikTok phê duyệt yêu cầu. Sau đó, thành viên trong Business Center có thể truy cập thông tin hồ sơ và video LIVE của tài khoản đó.
* **Tài khoản TikTok cho TikTok Shop (`TTS_TT`)**: Tạo ra khi bạn thiết lập một tài khoản TikTok chính thức liên kết với TikTok Shop.

Có 3 loại danh tính dùng để tạo Spark Ads: Người dùng ủy quyền (`AUTH_CODE`), Người dùng TikTok (`TT_USER`) và Tài khoản TikTok trong Business Center (`BC_AUTH_TT`). Xem chi tiết tại [Spark Ads - Hướng dẫn tạo Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).

## Các endpoint liên quan (Related endpoints)
* [Tạo danh tính](../12-api-reference/46-identity.md#doc-1740654203526146)
* [Xóa danh tính](../12-api-reference/46-identity.md#doc-1759155939236865)
* [Lấy danh sách danh tính](../12-api-reference/46-identity.md#doc-1740218420781057)
* [Lấy thông tin chi tiết danh tính](../12-api-reference/46-identity.md#doc-1740218453385217)
* [Lấy danh sách video theo danh tính](../12-api-reference/46-identity.md#doc-1740218475032577)
* [Lấy thông tin ủy quyền âm nhạc](../12-api-reference/46-identity.md#doc-1740218495869954)
* [Lấy thông tin video TikTok](../12-api-reference/46-identity.md#doc-1740218522178562)


---

<a id="doc-1799186631031809"></a>
<!-- doc_id: 1799186631031809 -->
# Công tắc tự công bố nội dung AIGC (AIGC self-disclosure toggle)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > AIGC self-disclosure toggle
Công tắc tự công bố nội dung AIGC (Nội dung do trí tuệ nhân tạo tạo ra), hay còn gọi là cài đặt "Quảng cáo này chứa nội dung do AI tạo ra", cho phép bạn chủ động minh bạch thông tin trong mẫu quảng cáo. Khi bật công tắc này, quảng cáo sẽ hiển thị nhãn "Nhà quảng cáo gắn nhãn do AI tạo" khi người dùng nhấp vào ảnh thu nhỏ trong trang kết quả tìm kiếm của TikTok và xem quảng cáo toàn màn hình. Khi bật tính năng này, bạn xác nhận rằng nội dung tuân thủ đúng [nguyên tắc về nội dung do AI tạo ra của TikTok](https://ads.tiktok.com/help/article/tiktok-ads-policy-misleading-and-false-content?lang=en).

Bạn có thể bật công tắc này cho các mẫu quảng cáo không phải Spark Ads (non-Spark Ads). Đối với Spark Ads, hệ thống sẽ sử dụng nhãn "Do AI tạo" riêng và TikTok có thể tự động gắn nhãn này nếu phát hiện nội dung hoàn toàn do AI tạo ra hoặc được chỉnh sửa đáng kể bằng AI.

## Các mục tiêu quảng cáo và định dạng hỗ trợ
Bảng dưới đây mô tả các mục tiêu quảng cáo và định dạng mẫu quảng cáo hỗ trợ công tắc tự công bố AIGC:

| Mục tiêu quảng cáo ⏎ (objective_type) | Định dạng hỗ trợ (Supported ad formats) | Cấu hình ở cấp quảng cáo (Ad-level configurations) |
|---|---|---|
| • `REACH` • `TRAFFIC` • `VIDEO_VIEWS` • `APP_PROMOTION` • `WEB_CONVERSIONS` | • Video đơn (Single Video) • Thẻ xoay vòng tiêu chuẩn (Standard Carousel) | Đặt `ad_format` thành một trong các giá trị: • `SINGLE_VIDEO` • `CAROUSEL_ADS` |
| `RF_REACH` | Video đơn (Single Video) | Đặt `ad_format` là `SINGLE_VIDEO` |
| `LEAD_GENERATION` | Video đơn (Single Video) | Đặt `ad_format` là `SINGLE_VIDEO` |
| `PRODUCT_SALES` | Cho Video Shopping Ads với Catalog: • Định dạng động • Video đơn • Video danh mục • Thẻ xoay vòng danh mục | Nếu `campaign_product_source` là `CATALOG` ở cấp chiến dịch và `shopping_ads_type` là `VIDEO` ở cấp nhóm quảng cáo, áp dụng một trong các cấu hình: • Đặt `dynamic_format` là `DYNAMIC_CREATIVE` • Đặt `ad_format` là `SINGLE_VIDEO` và `vertical_video_strategy` là `SINGLE_VIDEO` • Đặt `ad_format` là `SINGLE_VIDEO` và `vertical_video_strategy` là `CATALOG_VIDEOS` • Đặt `ad_format` là `CATALOG_CAROUSEL` |

## Các bước thực hiện (Steps)
Tùy theo loại quảng cáo bạn muốn kích hoạt tính năng tự công bố AIGC, bạn có thể triển khai trên quảng cáo tiêu chuẩn, Chiến dịch Smart+ hoặc quảng cáo Smart Creative:

### Dành cho quảng cáo tiêu chuẩn (For standard ads)
Để bật công tắc cho quảng cáo tiêu chuẩn, thực hiện các bước sau:
1. **Tạo chiến dịch** bằng endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
- Thiết lập `objective_type` thành một trong các mục tiêu được hỗ trợ.
2. **Tạo nhóm quảng cáo** bằng endpoint [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
- Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `PLACEMENT_TYPE_NORMAL` và có chứa `PLACEMENT_TIKTOK` trong `placements`.
3. **Tạo mẫu quảng cáo** bằng endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
- Chỉ định danh tính non-Spark Ads bằng cách đặt `identity_type` thành `CUSTOMIZED_USER`.
- Đặt `ad_format` thành định dạng được hỗ trợ.
- Thiết lập `aigc_disclosure_type` thành `SELF_DISCLOSURE`.

### Dành cho Chiến dịch Smart+ (For Smart+ Campaigns)
Khi tạo chiến dịch Smart+ qua endpoint legacy [/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362):
- Đặt `objective_type` là `APP_PROMOTION` hoặc `WEB_CONVERSIONS`.
- Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `PLACEMENT_TYPE_NORMAL` kèm vị trí TikTok.
- Thiết lập `identity_type` thành `CUSTOMIZED_USER`.
- Cung cấp video và ảnh bìa qua `video_info` và `image_info`.
- Đặt `aigc_disclosure_type` bên trong đối tượng `media_info` thành `SELF_DISCLOSURE`.

### Dành cho quảng cáo Smart Creative (For Smart Creative ads)
Khi tạo quảng cáo Smart Creative theo hướng dẫn tại mục [Smart Creative](quan-ly-chien-dich-p2.md#doc-1767322784934914):
- Ở bước tạo nhóm quảng cáo [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114), chọn vị trí tự động hoặc vị trí TikTok.
- Ở bước tạo quảng cáo [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626):
  - Đặt `identity_type` bên trong `common_material` thành `CUSTOMIZED_USER`.
  - Cung cấp video và ảnh bìa qua `video_info` và `image_info`.
  - Đặt `aigc_disclosure_type` bên trong đối tượng `media_info` thành `SELF_DISCLOSURE`.


---

<a id="doc-1855450880142402"></a>
<!-- doc_id: 1855450880142402 -->
# Tự động nâng cao chất lượng (Automatic Enhancements)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Automatic Enhancements
Tự động nâng cao chất lượng (Automatic Enhancements) là giải pháp tối ưu hóa quảng cáo ứng dụng công nghệ Symphony AIGC tiên tiến nhất của TikTok để tự động nâng cấp video và hình ảnh tải lên khi tạo chiến dịch.

Các tùy chọn Tự động nâng cao chất lượng bao gồm:
- **Dịch thuật và lồng tiếng (Translate and dub)**: Tiếp cận khách hàng toàn cầu bằng cách tự động dịch và lồng tiếng quảng cáo sang hơn 50 ngôn ngữ.
- **Làm mới âm nhạc (Music refresh)**: Luôn bắt kịp xu hướng bằng cách hoán đổi sang các bài nhạc thịnh hành trên TikTok.
- **Nâng cao chất lượng video (Video quality)**: Tăng cường độ phân giải và độ sắc nét tổng thể của video.
- **Nâng cao chất lượng hình ảnh (Image quality)**: Tăng cường độ phân giải và độ rõ nét của hình ảnh.
- **Điều chỉnh kích thước (Resize)**: Tự động điều chỉnh kích thước ảnh để tận dụng tối đa không gian hiển thị toàn màn hình.

## Khả năng hỗ trợ (Availability)
Khả năng sử dụng tính năng Tự động nâng cao chất lượng được thiết lập qua tham số `creative_auto_enhancement_strategy_list`, tùy thuộc vào loại quảng cáo (Smart+ nâng cấp hoặc Thủ công) và các cấu hình chiến dịch cụ thể.

### Dành cho quảng cáo Upgraded Smart+
Các bảng dưới đây tổng hợp các kịch bản có thể sử dụng `creative_auto_enhancement_strategy_list` để bật tính năng Tự động nâng cao qua endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522).

> **Lưu ý:**
> Tất cả các chiến lược Tự động nâng cao đều khả dụng cho Upgraded Smart+ Ads tại các trường hợp được hỗ trợ.

#### Dành cho quảng cáo Quảng bá ứng dụng (App Promotion ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Loại quảng bá ứng dụng (App promotion type)** (`app_promotion_type`)
**Sử dụng danh mục (Use catalog)** (`catalog_enabled`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Quảng bá ứng dụng (APP_PROMOTION)
Cài đặt ứng dụng (APP_INSTALL)
false
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

Nhắm mục tiêu lại ứng dụng (APP_RETARGETING)
false
❌

TikTok Minis (MINIS)
true
**Chọn vị trí cụ thể** chỉ bao gồm vị trí TikTok: • Đặt placement_type là PLACEMENT_TYPE_NORMAL và placements là ["PLACEMENT_TIKTOK"].
❌

false
❌

#### Dành cho quảng cáo Thu thập khách hàng tiềm năng (Lead Generation ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Sử dụng danh mục (Use catalog)** (`catalog_enabled`)
**Vị trí tối ưu hóa (Optimization Location)** (`promotion_type` và `promotion_target_type`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Tìm kiếm khách hàng tiềm năng (LEAD_GENERATION)
false
Biểu mẫu tức thì (promotion_type là LEAD_GENERATION và promotion_target_type là INSTANT_PAGE)
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

false
Trang web (promotion_type là LEAD_GENERATION và promotion_target_type là EXTERNAL_WEBSITE)
✅

true
**Chọn vị trí cụ thể** chỉ bao gồm vị trí TikTok: • Đặt placement_type là PLACEMENT_TYPE_NORMAL và placements là ["PLACEMENT_TIKTOK"].
❌

false
Tin nhắn trực tiếp TikTok (promotion_type là LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE và không truyền promotion_target_type)
❌

true
❌

false
Ứng dụng tin nhắn tức thì (promotion_type là LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE và không truyền promotion_target_type)
✅

false
Cuộc gọi điện thoại (promotion_type là LEAD_GEN_CLICK_TO_CALL và không truyền promotion_target_type)
❌

#### Dành cho quảng cáo Doanh số bán hàng (Sales ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Đích đến bán hàng (Sales destination)** (`sales_destination`)
**Sử dụng danh mục (Use catalog)** (`catalog_enabled`)
**Loại danh mục (Catalog type)** (`catalog_type`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Sales (WEB_CONVERSIONS)
Trang web (WEBSITE)
false
Không chỉ định
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

true
E-commerce (ECOMMERCE)
✅

true
Du lịch và giải trí (TRAVEL_ENTERTAINTAINMENT)
❌

true
Phim ngắn nhiều tập (MINI_SERIES)
✅

Ứng dụng (APP)
true
E-commerce (ECOMMERCE)
✅

Trang web và ứng dụng (WEB_AND_APP)
false
Không chỉ định
✅

true
E-commerce (ECOMMERCE)
✅

true
Du lịch và giải trí (TRAVEL_ENTERTAINTAINMENT)
❌

### Dành cho quảng cáo thủ công (Manual Ads)
Các bảng dưới đây nêu chi tiết các trường hợp có thể sử dụng `creative_auto_enhancement_strategy_list` để bật tính năng Tự động nâng cao qua endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

> **Note:** 
> Đối với quảng cáo thủ công (Manual Ads), chỉ có các chiến lược sau có thể định cấu hình qua `creative_auto_enhancement_strategy_list`:
> *   Chất lượng video (`VIDEO_QUALITY`)
> *   Làm mới âm nhạc (`MUSIC_REFRESH`)
> *   Chất lượng hình ảnh (`IMAGE_QUALITY`)
> *   Điều chỉnh kích thước (`IMAGE_RESIZE`)

#### Dành cho quảng cáo Quảng bá ứng dụng (App Promotion ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Loại quảng bá ứng dụng (App promotion type)** (`app_promotion_type`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Quảng bá ứng dụng (APP_PROMOTION)
Cài đặt ứng dụng (APP_INSTALL)
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

Nhắm mục tiêu lại ứng dụng (APP_RETARGETING)
✅

Đăng ký trước ứng dụng (APP_PREREGISTRATION)
✅

  
#### Dành cho quảng cáo Thu thập khách hàng tiềm năng (Lead Generation ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Sử dụng danh mục (Use catalog)** (`catalog_enabled`)
**Vị trí tối ưu hóa (Optimization Location)** (`promotion_type` và `promotion_target_type`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Tìm kiếm khách hàng tiềm năng (LEAD_GENERATION)
false
Biểu mẫu tức thì (promotion_type là LEAD_GENERATION và promotion_target_type là INSTANT_PAGE)
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

false
Trang web (promotion_type là LEAD_GENERATION và promotion_target_type là EXTERNAL_WEBSITE)
✅

true
**Chọn vị trí cụ thể** chỉ bao gồm vị trí TikTok: • Đặt placement_type là PLACEMENT_TYPE_NORMAL và placements là ["PLACEMENT_TIKTOK"].
❌

false
Tin nhắn trực tiếp TikTok (promotion_type là LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE và không truyền promotion_target_type)
✅

false
Ứng dụng tin nhắn tức thì (promotion_type là LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE và không truyền promotion_target_type)
✅

false
Cuộc gọi điện thoại (promotion_type là LEAD_GEN_CLICK_TO_CALL và không truyền promotion_target_type)
✅

#### Dành cho quảng cáo Doanh số bán hàng (Sales ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`virtual_objective_type` và `objective_type`)
**Đích đến bán hàng (Sales destination)** (`sales_destination`)
**Sử dụng danh mục (Use catalog)** (`catalog_enabled` và `campaign_product_source`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Doanh số (virtual_objective_type là SALES và objective_type là WEB_CONVERSIONS)
Trang web (WEBSITE)
Không chỉ định
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

Bất kỳ cấu hình nào sau đây: • `catalog_enabled` được đặt là `true` • `campaign_product_source` được đặt là `CATALOG`
❌

Doanh số (virtual_objective_type là SALES và objective_type là PRODUCT_SALES)
Ứng dụng (APP)
`campaign_product_source` là `CATALOG`
❌

Doanh số (virtual_objective_type là SALES và objective_type là PRODUCT_SALES)
Trang web và ứng dụng (WEB_AND_APP)
`campaign_product_source` là `false`
✅

`campaign_product_source` là `true`
❌

#### Dành cho các loại quảng cáo khác (Other ads)

**Campaign level**
**Ad group level**
**Ad level**

**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)
**Loại chiến dịch (Campaign type)** (`rf_campaign_type`)
**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)
**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**

Lưu lượng truy cập (TRAFFIC)
N/A
Một trong các loại sau: • **Vị trí tự động (Automatic Placement)**: Không truyền placement_type và placements. • **Chọn vị trí cụ thể** có bao gồm TikTok: Đặt placement_type là PLACEMENT_TYPE_NORMAL và thêm PLACEMENT_TIKTOK vào placements.
✅

Tiếp cận đấu thầu (REACH)
N/A
✅

Tiếp cận & Tần suất (RF_REACH)
Tiếp cận & Tần suất tiêu chuẩn (STANDARD)
❌

Tiếp cận & Tần suất (RF_REACH)
TikTok Pulse (PULSE)
❌

Lượt xem video (VIDEO_VIEWS)
N/A
✅

Tương tác cộng đồng (ENGAGEMENT)
N/A
✅


---

<a id="doc-1767309272869890"></a>
<!-- doc_id: 1767309272869890 -->
# Các câu hỏi thường gặp (FAQs)
> Đường dẫn: Marketing API > Campaign Management > Guides > FAQs
Bài viết này tổng hợp và giải đáp các câu hỏi thường gặp liên quan đến Campaign Management API.

## Nhóm quảng cáo (Ad group)
**Q1: Tôi đã chỉ định `app_id` trong endpoint tạo chiến dịch/nhóm quảng cáo (ví dụ /adgroup/create/), nhưng nhận được lỗi "DB record not found". Tại sao lại xảy ra lỗi này?**
Vui lòng kiểm tra lại mã `app_id` bạn đang sử dụng. Tham số `app_id` cần truyền trong yêu cầu gọi API là ID ứng dụng di động được thêm vào Trình quản lý sự kiện (Events Manager) của tài khoản quảng cáo mà bạn muốn quảng bá, chứ không phải App ID của ứng dụng nhà phát triển trên Cổng thông tin nhà phát triển (Developer Portal).

**Q2: Làm thế nào để tạo nhóm quảng cáo cho tính năng Tối ưu hóa theo giá trị (Value Optimization)?**
Tham khảo mục [Tối ưu hóa theo giá trị](quan-ly-chien-dich-p2.md#doc-1739381743067137) để nắm rõ cách kích hoạt VBO.

**Q3: Cách định cấu hình nhắm mục tiêu sở thích và hành vi qua API?**
Vui lòng sử dụng các endpoint sau để thiết lập các tùy chọn nhắm mục tiêu sở thích và hành vi:
- Nhắm mục tiêu sở thích (Interest targeting):
  - [/tool/interest_category/](../12-api-reference/70-tools-p1.md#doc-1737174348712961): Lấy danh mục sở thích khả dụng.
  - [/tool/interest_keyword/recommend/](../12-api-reference/70-tools-p1.md#doc-1763590884474882): Nhận từ khóa sở thích đề xuất.
  - [/tool/interest_keyword/get/](../12-api-reference/70-tools-p1.md#doc-1763590894544897): Lấy thông tin từ khóa sở thích theo ID.
- Tương tác với video (Video interactions):
  - [/tool/action_category/](../12-api-reference/70-tools-p1.md#doc-1737166752522241): Lấy danh mục tương tác video khả dụng (`action_scene` = `VIDEO_RELATED` trong phản hồi).
  - [/tool/targeting_category/recommend/](../12-api-reference/70-tools-p1.md#doc-1736275204260866): Lấy danh mục tương tác video đề xuất (`scene` = `VIDEO_RELATED` trong phản hồi).
- Tương tác với nhà sáng tạo (Creator interactions):
  - [/tool/action_category/](../12-api-reference/70-tools-p1.md#doc-1737166752522241): Lấy danh mục tương tác nhà sáng tạo (`action_scene` = `CREATOR_RELATED` trong phản hồi).
  - [/tool/targeting_category/recommend/](../12-api-reference/70-tools-p1.md#doc-1736275204260866): Lấy danh mục tương tác nhà sáng tạo đề xuất (`scene` = `CREATOR_RELATED` trong phản hồi).
- Tương tác với Hashtag (Hashtag interactions):
  - [/tool/hashtag/recommend/](../12-api-reference/70-tools-p1.md#doc-1736271339521025): Lấy danh sách hashtag đề xuất.
  - [/tool/hashtag/get/](../12-api-reference/70-tools-p1.md#doc-1736280889167874): Lấy thông tin hashtag theo ID.

## Mẫu quảng cáo (Ad)
**Q1: Tôi nhận được thông báo lỗi "The creative type is not consistent with your ad group settings. Please change the creative type in your ad group settings." khi gọi endpoint /ad/create/.**
Nguyên nhân là do nhóm quảng cáo của bạn đang bật tính năng Tối ưu hóa sáng tạo tự động ACO (`creative_material_mode` = `DYNAMIC`), nhưng bạn lại gọi endpoint thông thường `/ad/create/`. Để khắc phục, bạn cần chuyển sang sử dụng endpoint [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626) để tạo quảng cáo ACO.

**Q2: Tôi gặp lỗi "Unsupported image size. Please upload another image" khi gọi /ad/create/. Nguyên nhân do đâu?**
Hình ảnh tải lên không đáp ứng các thông số kỹ thuật tiêu chuẩn của TikTok. Vui lòng tham khảo [Quy chuẩn kỹ thuật quảng cáo hình ảnh](https://ads.tiktok.com/help/article/image-ads-specification?lang=en) hoặc [Quy chuẩn kỹ thuật quảng cáo video](https://ads.tiktok.com/help/article/video-ads-specifications?lang=en) để biết thêm chi tiết.

**Q3: Tôi nhận được thông báo lỗi "Invalid identity type" khi gọi endpoint /identity/video/get/.**
Nguyên nhân có thể do bạn đã truyền `CUSTOMIZED_USER` vào trường `identity_type`. Endpoint `/identity/video/get/` không hỗ trợ `CUSTOMIZED_USER`, mà chỉ hỗ trợ các loại danh tính `AUTH_CODE`, `TT_USER` và `BC_AUTH_TT`.
Các loại danh tính `AUTH_CODE`, `TT_USER` và `BC_AUTH_TT` liên kết với bài đăng qua `tiktok_item_id` (dùng để tạo Spark Ads). Trong khi đó, `CUSTOMIZED_USER` sử dụng `video_id` từ thư viện sáng tạo. Xem thêm tại mục [Danh tính (Identities)](quan-ly-chien-dich-p2.md#doc-1738958351620097).

## Các vấn đề khác (Other)
**Q1: Tôi nhận thấy một số tham số không hiển thị trong phản hồi hoặc bị hệ thống bỏ qua khi gọi request. Tại sao lại như vậy?**
Nguyên nhân phổ biến nhất là bạn đang sử dụng cú pháp của phiên bản cũ v1.2 trên endpoint API v1.3.
Trong API v1.3, tên và kiểu dữ liệu tham số đã được cập nhật chuẩn hóa. Ví dụ: tham số `placement` ở v1.2 đã đổi tên thành `placements` ở v1.3. Nếu bạn vẫn truyền `placement` vào endpoint `/v1.3/adgroup/create/`, hệ thống sẽ bỏ qua tham số này. Vui lòng tham khảo bảng "So sánh giữa v1.2 và v1.3" trong bài viết chi tiết của từng endpoint để cập nhật đúng tham số.

---

<a id="doc-1739381823123458"></a>
<!-- doc_id: 1739381823123458 -->
# Danh mục API (API reference)
> Đường dẫn: Marketing API > Campaign Management > API reference
Các endpoint sau đây khả dụng cho việc quản lý chiến dịch quảng cáo:

# Smart+ nâng cấp (Upgraded Smart+)

**Chiến dịch (Campaigns)**
* [Lấy danh sách chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312818332930)
* [Tạo chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706)
* [Cập nhật chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312876001282)
* [Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312888885314)
* [Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866528879472641)
* [Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866529943741441)

**Nhóm quảng cáo (Ad groups)**
* [Lấy danh sách nhóm quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p2.md#doc-1843314879617026)
* [Tạo nhóm quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p3.md#doc-1843314887930946)
* [Cập nhật nhóm quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843314894279682)
* [Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843314908153858)
* [Cập nhật ngân sách nhóm quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843314914438466)

**Mẫu quảng cáo (Ads)**
* [Lấy danh sách quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)
* [Tạo quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522)
* [Cập nhật quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921)
* [Cập nhật trạng thái hoạt động của quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317423164482)
* [Bật hoặc tắt tài nguyên trong quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317433577601)
* [Xem trước quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317445798914)

**Xét duyệt quảng cáo (Ad review)**
* [Lấy thông tin xét duyệt của quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317465695233)
* [Lấy thông tin xét duyệt tài nguyên của quảng cáo Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317474334722)
* [Khiếu nại quảng cáo Smart+ nâng cấp bị từ chối](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317522553106)

**Báo cáo (Reporting)**
* [Chạy báo cáo tổng quan tài nguyên Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317489576961)
* [Chạy báo cáo phân tích chi tiết tài nguyên Smart+ nâng cấp](../12-api-reference/62-upgraded-smartplus-p7.md#doc-1843317510389761)

# Chiến dịch thủ công (Manual)

**Chiến dịch (Campaigns)**
* [Lấy danh sách chiến dịch](../12-api-reference/24-campaign.md#doc-1739315828649986)
* [Tạo chiến dịch](../12-api-reference/24-campaign.md#doc-1739318962329602)
* [Cập nhật chiến dịch](../12-api-reference/24-campaign.md#doc-1739320422086657)
* [Cập nhật trạng thái chiến dịch](../12-api-reference/24-campaign.md#doc-1739320994354178)
* [Lấy hạn ngạch chiến dịch chuyên biệt theo mạng quảng cáo](../12-api-reference/24-campaign.md#doc-1752256376677378)
* [Tạo tác vụ sao chép bất đồng bộ cho chiến dịch thủ công](../12-api-reference/24-campaign.md#doc-1788434394151938)
* [Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch thủ công](../12-api-reference/24-campaign.md#doc-1788434463507458)

**Nhóm quảng cáo (Ad groups)**
* [Lấy danh sách nhóm quảng cáo](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922)
* [Lấy hạn ngạch động của nhóm quảng cáo đang hoạt động](../12-api-reference/07-ad-groups-p1.md#doc-1768463039162369)
* [Tạo nhóm quảng cáo](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114)
* [Cập nhật nhóm quảng cáo](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745)
* [Cập nhật trạng thái nhóm quảng cáo](../12-api-reference/07-ad-groups-p3.md#doc-1739591716326402)
* [Cập nhật ngân sách nhóm quảng cáo](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817)
* [Ước tính quy mô đối tượng](../12-api-reference/07-ad-groups-p1.md#doc-1740302379236353)

**Mẫu quảng cáo (Ads)**
* [Lấy danh sách quảng cáo](../12-api-reference/02-ads-p1.md#doc-1735735588640770)
* [Tạo quảng cáo](../12-api-reference/02-ads-p1.md#doc-1739953377508354)
* [Cập nhật quảng cáo](../12-api-reference/02-ads-p2.md#doc-1739953405142018)
* [Cập nhật trạng thái quảng cáo](../12-api-reference/02-ads-p2.md#doc-1739953422970882)

# Smart+ (Phiên bản cũ)
- [Lấy hạn ngạch động cho chiến dịch Smart+ đang hoạt động](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1831564498409473)
* **Tạo chiến dịch Smart+**
* **Cập nhật chiến dịch Smart+**
* **Lấy danh sách chiến dịch Smart+**
- [Bật hoặc tắt tài nguyên trong chiến dịch Smart+](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1837969177953361)
* [Chạy báo cáo chiến dịch Smart+](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1776454619412481)

# Quy tắc tự động (Automated rules)

* [Tạo quy tắc tự động](../12-api-reference/11-automated-rules.md#doc-1738767670852610)
* [Lấy thông tin quy tắc theo ID](../12-api-reference/11-automated-rules.md#doc-1738768750822466)
* [Lấy danh sách quy tắc theo bộ lọc](../12-api-reference/11-automated-rules.md#doc-1738768861976578)
* [Lấy kết quả thực thi quy tắc](../12-api-reference/11-automated-rules.md#doc-1738769076676609)
* [Lấy chi tiết kết quả thực thi](../12-api-reference/11-automated-rules.md#doc-1738769098314754)
* [Cập nhật quy tắc tự động](../12-api-reference/11-automated-rules.md#doc-1738769123170306)
* [Cập nhật trạng thái quy tắc](../12-api-reference/11-automated-rules.md#doc-1738769144119298)
* [Liên kết / Hủy liên kết quy tắc](../12-api-reference/11-automated-rules.md#doc-1738769164954626)

# Tiếp cận & Tần suất (Reach & Frequency)
[Các API Tiếp cận & Tần suất (Reach & Frequency)](quan-ly-chien-dich-p1.md#doc-1744571210012673)

# Sáng tạo thông minh (Smart Creative)
* [Tạo quảng cáo Smart Creative](../12-api-reference/60-smart-creative.md#doc-1739473063234626)
* [Lấy danh sách nguyên liệu Smart Creative](../12-api-reference/60-smart-creative.md#doc-1739473020978177)
* [Cập nhật nguyên liệu Smart Creative](../12-api-reference/60-smart-creative.md#doc-1739473077112833)
* [Cập nhật trạng thái nguyên liệu Smart Creative](../12-api-reference/60-smart-creative.md#doc-1739506701165570)

# Thử nghiệm phân tách (Split tests)
* [Tạo thử nghiệm phân tách](../12-api-reference/65-super-split-test.md#doc-1742666471475201)
* [Lấy kết quả thử nghiệm phân tách](../12-api-reference/65-super-split-test.md#doc-1742666557045761)
* [Chạy nhóm quảng cáo chiến thắng](../12-api-reference/65-super-split-test.md#doc-1742666543736834) 
* [Cập nhật thời gian thử nghiệm phân tách](../12-api-reference/65-super-split-test.md#doc-1742666501911553)
* [Tạm dừng thử nghiệm phân tách](../12-api-reference/65-super-split-test.md#doc-1742666522399746)

# GMV Max

**Chiến dịch (Campaign)**
- [Lấy danh sách chiến dịch GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1826463372290177)
- [Lấy thông tin chi tiết chiến dịch GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000968821762)
- [Tạo chiến dịch GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000988713089)
- [Cập nhật chiến dịch GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822001009002497)
- [Lấy mục tiêu ROI và ngân sách đề xuất cho GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822001024720897)
- [Tạo phiên phân phối tối đa hoặc tăng cường sáng tạo](../12-api-reference/45-gmv-max-p1.md#doc-1835246967275522)
- [Cập nhật phiên phân phối tối đa hoặc tăng cường sáng tạo](../12-api-reference/45-gmv-max-p1.md#doc-1835247009119233)
- [Lấy các phiên phân phối tối đa trong chiến dịch](../12-api-reference/45-gmv-max-p1.md#doc-1835246996436162)
- [Lấy chi tiết phiên phân phối tối đa](../12-api-reference/45-gmv-max-p1.md#doc-1835247031331842)
- [Xóa phiên phân phối tối đa hoặc tăng cường sáng tạo](../12-api-reference/45-gmv-max-p1.md#doc-1835246983475217)
- [Xóa hoặc thêm lại tài nguyên trong chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1861260625563202)

**TikTok Shop và sản phẩm**
- [Lấy danh sách TikTok Shop cho chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1822001044479041)
- [Lấy danh sách sản phẩm trong TikTok Shop](../12-api-reference/69-tiktok-store.md#doc-1793482248880130)
- [Kiểm tra tính khả dụng của TikTok Shop cho chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1822001084174338)

**Danh tính và bài đăng**
- [Lấy danh tính cho chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1822001101474882)
- [Kiểm tra tính khả dụng của danh tính/sản phẩm trong Shopping Ads](../12-api-reference/45-gmv-max-p2.md#doc-1822001136924674)
- [Lấy danh sách bài đăng cho chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1822001168512129)
- [Lấy chi tiết video trong bài đăng tùy chỉnh](../12-api-reference/45-gmv-max-p2.md#doc-1830215925061633)
- [Tạo bài đăng TikTok tùy chỉnh ở cấp cửa hàng](../12-api-reference/45-gmv-max-p2.md#doc-1866513154013585)
- [Lấy danh sách bài đăng TikTok tùy chỉnh](../12-api-reference/45-gmv-max-p2.md#doc-1866513156712449)
- [Xóa bài đăng TikTok tùy chỉnh](../12-api-reference/45-gmv-max-p2.md#doc-1866513159202306)
- [Lấy chi tiết liên kết sản phẩm của video trong bài đăng](../12-api-reference/45-gmv-max-p2.md#doc-1866513161692161)

**Ủy quyền độc quyền tài khoản quảng cáo**
- [Lấy trạng thái ủy quyền độc quyền TikTok Shop của tài khoản](../12-api-reference/45-gmv-max-p2.md#doc-1822001184635905)
- [Cấp quyền ủy quyền độc quyền TikTok Shop cho tài khoản quảng cáo](../12-api-reference/45-gmv-max-p2.md#doc-1822001200356354)

**Báo cáo (Reporting)**
- [Chạy báo cáo chiến dịch GMV Max](../12-api-reference/45-gmv-max-p2.md#doc-1824721673497601)
	- [Các chỉ số trong báo cáo chiến dịch GMV Max](../12-api-reference/45-gmv-max-p3.md#doc-1824722485971009)

# Từ khóa phủ định (Negative Keywords)
- [Lấy danh sách từ khóa phủ định](../12-api-reference/53-negative-keywords.md#doc-1775104887052289)
- [Tạo từ khóa phủ định](../12-api-reference/53-negative-keywords.md#doc-1775104895291393)
- [Cập nhật từ khóa phủ định](../12-api-reference/53-negative-keywords.md#doc-1775104902283266)
- [Xóa từ khóa phủ định](../12-api-reference/53-negative-keywords.md#doc-1775104910010369)
- [Tải xuống danh sách từ khóa phủ định](../12-api-reference/53-negative-keywords.md#doc-1775104916876290)

