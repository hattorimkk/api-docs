# Smart+ nâng cấp (Upgraded Smart+) — phần 2/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Lấy danh sách nhóm quảng cáo Smart+ nâng cấp (#doc-1843314879617026)](#doc-1843314879617026)

---

<a id="doc-1843314879617026"></a>
<!-- doc_id: 1843314879617026 -->
<!-- doc_id: 1843314879617026 -->
# Lấy danh sách nhóm quảng cáo Smart+ nâng cấp (Get Upgraded Smart+ Ad Groups)
> Đường dẫn: API Reference > Upgraded Smart+ > Nhóm quảng cáo > Lấy danh sách nhóm quảng cáo Smart+ nâng cấp
Sử dụng endpoint này để truy xuất danh sách các nhóm quảng cáo Smart+ nâng cấp trong tài khoản quảng cáo.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| fields | string[] | Danh sách các trường bạn muốn lấy. ⏎ Khi không chỉ định trường này, tất cả các trường sẽ được trả về theo mặc định. ⏎ Để biết các trường được phép, xem các trường dưới mục `list` trong phần Dữ liệu phản hồi (Response). |
| include_effective_status | boolean | Có bao gồm tham số `effective_status` trong phản hồi hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| filtering | object | Điều kiện lọc dữ liệu. ⏎ Example: `filtering={"objective_type":"APP_PROMOTION"}` |
| ↳ campaign_ids | string[] | Lọc theo ID chiến dịch. ⏎ Kích thước tối đa: 100. ⏎ Để lấy ID chiến dịch, sử dụng [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). |
| ↳ adgroup_ids | string[] | Lọc theo ID nhóm quảng cáo. ⏎ Kích thước tối đa: 100. |
| ↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳ effective_statuses | string[] | Lọc theo danh sách trạng thái nhóm quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Đang xét duyệt (Under review). • `NOT_DELIVERED`: Chưa phân phối (Not delivered). • `SCHEDULED`: Đã lên lịch (Scheduled). • `PARTIAL_DELIVERY`: Phân phối một phần (Partial delivery). • `ACTIVE`: Đang hoạt động (Active). • `ENDED`: Đã kết thúc (Ended). • `PAUSED`: Đã tạm dừng (Paused). • `DELETED`: Đã xóa (Deleted). |
| ↳ primary_status | string | Trạng thái chính (Primary status). ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ Giá trị mặc định là `STATUS_NOT_DELETE`, trả về nhóm quảng cáo ở mọi trạng thái ngoại trừ `STATUS_DELETE`. ⏎ Nếu bạn muốn lấy nhóm quảng cáo ở tất cả các trạng thái bao gồm cả `STATUS_DELETE`, hãy sử dụng `STATUS_ALL`. |
| ↳ secondary_status | string | Trạng thái phụ của nhóm quảng cáo (Secondary status). ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Ad Group Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ objective_type | string | Mục tiêu quảng cáo. ⏎ Hiện tại, chúng tôi hỗ trợ `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`. ⏎ Để xem giải thích chi tiết về các giá trị enum, xem [Enumeration-Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ sales_destination | string | Đích đến bán hàng (Sales destination), nơi bạn muốn thúc đẩy doanh số. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Trang web. Thúc đẩy doanh số trên trang web của bạn. • `APP`: Ứng dụng. Thúc đẩy doanh số trên ứng dụng của bạn (yêu cầu danh mục sản phẩm). • `WEB_AND_APP`: Trang web và ứng dụng. Thúc đẩy doanh số trên cả trang web và ứng dụng của bạn. |
| ↳ promotion_type | string | Loại quảng bá (vị trí tối ưu hóa) mà bạn muốn lọc. ⏎ Các giá trị enum hỗ trợ: • `APP`: Ứng dụng. • `WEBSITE`: Trang đích. • `INSTANT_FORM`: Biểu mẫu tức thì (Instant Form). • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`: Tin nhắn trực tiếp trên TikTok. • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`: Ứng dụng mạng xã hội. • `LEAD_GEN_CLICK_TO_CALL`: Cuộc gọi điện thoại. ⏎ **Lưu ý**: • Trường bộ lọc này khác với trường `promotion_type` dùng khi tạo nhóm quảng cáo (cũng được trả về trong phản hồi của endpoint này). • Để tìm hiểu cách thiết lập trường này nhằm lọc các loại quảng bá nhất định được dùng khi tạo nhóm quảng cáo, xem [Phụ lục - Ánh xạ giữa các loại quảng bá khác nhau](../15-appendix/phu-luc-p1.md#doc-1758485431181314). |
| ↳ optimization_goal | string | Kết quả có thể đo lường bạn muốn thúc đẩy với chiến dịch của mình. ⏎ Hiện tại, chúng tôi hỗ trợ `CLICK`, `INSTALL`, `IN_APP_EVENT`, `VALUE`, `CONVERT`, `TRAFFIC_LANDING_PAGE_VIEW` và `LEAD_GENERATION`. ⏎ Để xem mô tả chi tiết cho từng mục tiêu tối ưu hóa, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| page | number | Số trang hiện tại cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. ⏎ Khoảng giá trị: ≥ 1. |
| page_size | number | Kích thước trang. ⏎ Giá trị mặc định: 10. ⏎ Khoảng giá trị: 1-1.000. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/get/?advertiser_id={{advertiser_id}}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các nhóm quảng cáo Smart+ nâng cấp trong tài khoản quảng cáo. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳↳ campaign_name | string | Tên của chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad group is enabled (in 'ON' status). • `DISABLE`: The ad group is disabled (in 'OFF' status). |
| ↳↳ effective_status | string | Returned only when `effective_status` is `true` in the request. ⏎ The status of the ad group. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Under review. • `NOT_DELIVERED`: Not delivered. • `SCHEDULED`: Scheduled. • `PARTIAL_DELIVERY`: Partial delivery. • `ACTIVE`: Active. • `ENDED`: Ended. • `PAUSED`: Paused. • `DELETED`: Deleted. |
| ↳↳ secondary_status | string | Ad group secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Ad group Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ catalog_id | string | Được trả về khi `catalog_enabled` là `true` ở cấp chiến dịch. ⏎ ID danh mục sản phẩm (catalog) được sử dụng trong nhóm quảng cáo. |
| ↳↳ catalog_authorized_bc_id | string | Được trả về khi `catalog_enabled` là `true` ở cấp chiến dịch. ⏎ ID của Trung tâm doanh nghiệp (Business Center) sở hữu danh mục sản phẩm (`catalog_id`). |
| ↳↳ product_source | string | Nguồn sản phẩm bạn muốn lấy để quảng bá. ⏎ Giá trị enum: `CATALOG` (danh mục). |
| ↳↳ promotion_type | string | Loại quảng bá (Vị trí tối ưu hóa). Bạn có thể quyết định nơi muốn quảng bá sản phẩm bằng trường này. ⏎ Hiện tại hỗ trợ: `APP_ANDROID`, `APP_IOS`, `WEBSITE`, `MINI_GAME`, `NATIVE_SERIES`, `LEAD_GENERATION` và `LEAD_GENERATION_MULTI_DESTINATION`. • Khi `objective_type` là `APP_PROMOTION` và `app_promotion_type` là `APP_INSTAL`, trường này sẽ là `APP_ANDROID` hoặc `APP_IOS`. • Khi `objective_type` là `APP_PROMOTION` và `app_promotion_type` là `MINIS`, trường này sẽ là `MINI_APP`, `MINI_GAME` hoặc `NATIVE_SERIES`. • Khi `objective_type` là `WEB_CONVERSIONS`: • Nếu `sales_destination` là `WEBSITE`, trường này sẽ là `WEBSITE`. • Nếu `sales_destination` là `APP`, trường này sẽ là `APP_ANDROID` hoặc `APP_IOS`. • Khi `objective_type` là `LEAD_GENERATION`, trường này sẽ là một trong các giá trị: • `LEAD_GENERATION` • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` • `LEAD_GEN_CLICK_TO_CALL` • `LEAD_GENERATION_MULTI_DESTINATION`. |
| ↳↳ optimization_locations | object[] | Được trả về khi `promotion_type` là `LEAD_GENERATION_MULTI_DESTINATION`. ⏎ Danh sách các vị trí tối ưu hóa cho nhóm quảng cáo Tìm kiếm khách hàng tiềm năng. ⏎ Để tìm hiểu loại quảng cáo có thể sử dụng trường này, xem [Tạo chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng nâng cấp với nhiều vị trí đích](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1876685025962241). |
| ↳↳↳ promotion_type | string | Promotion type (Optimization location). ⏎ You can decide where you want audiences to convert or complete an action. ⏎ Các giá trị enum hỗ trợ: `LEAD_GENRATION`, `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`. |
| ↳↳↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳↳↳ optimization_event | string | Optimization event. ⏎ Các giá trị enum hỗ trợ: • `ON_WEB_REGISTER`: Complete registration. • `CONSULT`: Contact. • `FORM`: Submit form. • `ON_WEB_SUBSCRIBE`: Subscribe. |
| ↳↳ promotion_website_type | string | Loại trang tức thì TikTok (TikTok Instant Page type). ⏎ Hiện tại chỉ hỗ trợ `TIKTOK_NATIVE_PAGE` (Sử dụng Trang tức thì TikTok). |
| ↳↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ gaming_ad_compliance_agreement | string | Returned only in any of the following scenarios: • Scenario 1: When the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • Scenario 2: When the following conditions are all met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `REGULAR_CAMPAIGN`. ⏎ Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳↳ pixel_id | string | ID TikTok Pixel. |
| ↳↳ app_config | object[] | Được trả về khi `sales_destination` là `WEB_AND_APP`. ⏎ Chi tiết về ứng dụng hoặc các ứng dụng cần quảng bá. |
| ↳↳↳ app_id | string | App ID của ứng dụng cần quảng bá. |
| ↳↳ minis_id | string | Được trả về khi `promotion_type` là `MINI_APP` hoặc `MINI_GAME`. ⏎ ID của TikTok Mini. |
| ↳↳ optimization_event | string | Sự kiện chuyển đổi cho nhóm quảng cáo. ⏎ Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) để biết thêm. ⏎ **Lưu ý**: Nếu bạn bật Tối ưu hóa theo giá trị khi tạo nhóm quảng cáo bằng cách đặt `optimization_event` thành `IMPRESSION_LEVEL_AD_REVENUE` hoặc `AD_REVENUE_VALUE` (hai giá trị enum này tương đương và có cùng hiệu lực), bạn sẽ luôn nhận được `IMPRESSION_LEVEL_AD_REVENUE` dưới dạng `optimization_event` trong phản hồi. |
| ↳↳ custom_conversion_id | string | ID của Chuyển đổi tùy chỉnh (Custom Conversion) được sử dụng trong nhóm quảng cáo. |
| ↳↳ deep_funnel_optimization_status | string | Với tính năng tối ưu hóa phễu sâu (deep funnel optimization), bạn có thể chọn một sự kiện phụ song song với sự kiện tối ưu hóa chính, giúp cải thiện hiệu quả chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `ON`: Bật. • `OFF`: Tắt. |
| ↳↳ deep_funnel_event_source | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ Loại nguồn sự kiện. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel. • `OFFLINE`: Bộ sự kiện ngoại tuyến (Offline Event Set). • `CRM`: Bộ sự kiện CRM (CRM Event Set). |
| ↳↳ deep_funnel_event_source_id | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ ID nguồn sự kiện. • Khi `deep_funnel_event_source` là `PIXEL`, trường này đại diện cho ID TikTok Pixel. • Khi `deep_funnel_event_source` là `OFFLINE`, trường này đại diện cho ID bộ sự kiện ngoại tuyến. • Khi `deep_funnel_event_source` là `CRM`, trường này đại diện cho ID bộ sự kiện CRM. |
| ↳↳ deep_funnel_optimization_event | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ Sự kiện tối ưu hóa phễu sâu. ⏎ Ví dụ: `SHOPPING`. |
| ↳↳ app_attribution_source | string | Nguồn phân bổ cho ứng dụng của bạn. ⏎ Nguồn phân bổ bạn chọn sẽ được sử dụng để tối ưu hóa, đấu thầu và báo cáo. ⏎ Các giá trị enum hỗ trợ: • `MMP`: Phân bổ qua MMP (đối tác đo lường di động). Tín hiệu từ MMP đã chọn sẽ được dùng để phân bổ. • `SAN`: Phân bổ qua SAN (mạng tự phân bổ). Tín hiệu từ TikTok SAN sẽ được dùng để phân bổ. |
| ↳↳ app_data_source | string | Nguồn dữ liệu cho ứng dụng của bạn. ⏎ Tín hiệu phân bổ bạn chọn sẽ được sử dụng cho báo cáo. ⏎ Các giá trị enum hỗ trợ: • `MMP`: Tín hiệu MMP. Dữ liệu từ MMP của bạn sẽ được dùng cho báo cáo. • `EVENT_SDK`: Tín hiệu App Events SDK. Dữ liệu từ TikTok App Events SDK sẽ được dùng cho báo cáo. • `EVENT_API`: Tín hiệu Events API. Dữ liệu từ TikTok Events API sẽ được dùng cho báo cáo. |
| ↳↳ identity_id | string | Chỉ được trả về trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ ID danh tính (Identity ID). |
| ↳↳ identity_type | string | Chỉ được trả về trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ Loại danh tính. ⏎ Các giá trị enum hỗ trợ: • `TT_USER`: Người dùng Tài khoản Doanh nghiệp TikTok. • `BC_AUTH_TT`: Tài khoản TikTok mà Business Center được ủy quyền truy cập. ⏎ Xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) để biết chi tiết. |
| ↳↳ identity_authorized_bc_id | string | Được trả về khi `identity_type` là `BC_AUTH_TT`. ⏎ ID của Trung tâm doanh nghiệp (Business Center) liên kết với danh tính người dùng tài khoản TikTok trong Business Center. |
| ↳↳ native_series_id | string | ID của TikTok Series. ⏎ Series cung cấp các gói video độc quyền và cao cấp do các nhà sáng tạo nội dung sản xuất. Quyền truy cập Series có thể được mua qua hồ sơ của nhà sáng tạo và các liên kết gắn kèm trên video TikTok. |
| ↳↳ messaging_app_type | string | Loại ứng dụng nhắn tin tức thì hoặc URL tùy chỉnh dùng trong Nhóm quảng cáo Tin nhắn tức thì. ⏎ Các giá trị enum hỗ trợ: • `MESSENGER`: Messenger. • `WHATSAPP`: WhatsApp. • `ZALO`: Zalo. • `LINE`: Line. • `IM_URL`: URL tin nhắn tức thì. ⏎ Để tìm hiểu thêm về cách tạo Quảng cáo Tin nhắn tức thì TikTok với Smart+ nâng cấp, xem [Tạo chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng nâng cấp với vị trí tối ưu hóa là ứng dụng nhắn tin tức thì](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302988449921). |
| ↳↳ zalo_id_type | string | Định dạng thông tin liên hệ Zalo. ⏎ Các giá trị enum hỗ trợ: • `ZALO_OFFICIAL_ACCOUNT`: ID Zalo Official Account. • `ZALO_PHONE_ACCOUNT`: Số điện thoại Zalo. |
| ↳↳ messaging_app_account_id | string | ID tài khoản ứng dụng nhắn tin tức thì. • Khi `messaging_app_type` là `MESSENGER`, trường này đại diện cho Facebook Page ID. • Khi `messaging_app_type` là `LINE`, trường này đại diện cho LINE Business ID. • Khi `zalo_id_type` là `ZALO_OFFICIAL_ACCOUNT`, trường này đại diện cho ID Zalo Official Account. • Khi `messaging_app_type` là `WHATSAPP` hoặc khi `zalo_id_type` là `ZALO_PHONE_ACCOUNT`, trường này đại diện cho số điện thoại WhatsApp hoặc Zalo được tự động điền dựa trên `phone_info` đã chỉ định. |
| ↳↳ message_event_set_id | string | ID của bộ sự kiện tin nhắn dùng trong Nhóm quảng cáo Tin nhắn tức thì. ⏎ Nếu tài khoản ứng dụng tin nhắn (tài khoản Messenger hoặc Zalo Official Account chỉ định qua `messaging_app_account_id`, hoặc số điện thoại WhatsApp/Zalo từ `phone_info`) khớp với bộ sự kiện hiện có, trường này sẽ được **tự động điền** bộ sự kiện tin nhắn duy nhất tương ứng. |
| ↳↳ phone_info | object | Chi tiết số điện thoại WhatsApp hoặc Zalo. |
| ↳↳↳ phone_region_code | string | Mã vùng quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `US`. |
| ↳↳↳ phone_region_calling_code | string | Mã quay số quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `+1`. |
| ↳↳↳ phone_number | string | Số điện thoại WhatsApp hoặc Zalo. |
| ↳↳ bid_type | string | Chiến lược giá thầu. ⏎ Để xem các giá trị enum và mô tả, xem [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ bid_price | float | Chi phí mục tiêu trên mỗi lượt nhấp. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |
| ↳↳ conversion_bid_price | float | Chi phí mục tiêu trên mỗi chuyển đổi hoặc chi phí trên mỗi lượt xem trang đích. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |
| ↳↳ deep_bid_type | string | Chiến lược đặt giá thầu cho sự kiện trong ứng dụng. ⏎ Để xem các giá trị enum và mô tả, xem [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ roas_bid | float | ROAS mục tiêu cho Tối ưu hóa theo giá trị (Value-Based Optimization). |
| ↳↳ value_rule_set_id | string | ID của bộ quy tắc giá trị liên kết với nhóm quảng cáo. |
| ↳↳ incentive_offer_type | string | Loại ưu đãi khuyến khích áp dụng cho Nhóm quảng cáo Smart+ nâng cấp. ⏎ Nếu nhóm quảng cáo của bạn đáp ứng tiêu chí hợp lệ và vượt qua các ngưỡng CPA hoặc ROAS tối thiểu/ROAS mục tiêu nhất định, bạn sẽ được thưởng tín dụng quảng cáo để sử dụng trong cùng tài khoản quảng cáo. ⏎ Để tìm hiểu thêm về tiêu chí hợp lệ và cách tính mức ưu đãi, xem [Ưu đãi khuyến khích trên nền tảng Smart+ (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: Nhóm quảng cáo không đủ điều kiện nhận ưu đãi. • `COST_CAP_AND_MIN_ROAS`: Nhóm quảng cáo sử dụng chiến lược giá thầu Cost Cap hoặc ROAS tối thiểu/ROAS mục tiêu và đủ điều kiện nhận ưu đãi. ⏎ • Để kiểm tra tính hợp lệ bảo vệ giá thầu (ưu đãi khuyến khích) cho danh sách Chiến dịch hoặc Nhóm quảng cáo Smart+ nâng cấp, sử dụng [/report/bid_protection/status/get/](70-tools-p2.md#doc-1874392512912449). • Để xem lịch sử bảo vệ giá thầu và tín dụng quảng cáo trong 60 ngày qua, sử dụng [/report/bid_protection/detail/get/](70-tools-p3.md#doc-1874392516418561). |
| ↳↳ vbo_window | string | Khung thời gian của chiến lược giá thầu đã chọn cho [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Tối ưu hóa theo giá trị cho quảng cáo trong ứng dụng) hoặc [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Tối ưu hóa theo giá trị cho mua hàng trong ứng dụng). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: 7 ngày đầu tiên (ngày thứ 7). • `ZERO_DAY`: Ngày hiện tại (ngày 0). |
| ↳↳ click_attribution_window | string | Khoảng thời gian phân bổ lượt nhấp (Click-through window). Đây là khoảng thời gian từ khi người dùng nhấp vào quảng cáo của bạn đến khi thực hiện hành động. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Tắt. • `ONE_DAY`: Lượt nhấp 1 ngày. • `SEVEN_DAYS`: Lượt nhấp 7 ngày. • `FOURTEEN_DAYS`: Lượt nhấp 14 ngày. • `TWENTY_EIGHT_DAYS`: Lượt nhấp 28 ngày. • `THIRTY_DAYS`: Lượt nhấp 30 ngày. • `THIRTY_TWO_DAYS`: Lượt nhấp 32 ngày. • `ONE_HUNDRED_EIGHTY_DAYS`: Lượt nhấp 180 ngày. |
| ↳↳ engaged_view_attribution_window | string | Khoảng thời gian phân bổ lượt xem tương tác (Engaged view-through window). Đây là khoảng thời gian sau khi người dùng xem ít nhất 6 giây quảng cáo video mà lượt chuyển đổi được tính. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Tắt. • `ONE_DAY`: Lượt xem tương tác 1 ngày. • `SEVEN_DAYS`: Lượt xem tương tác 7 ngày. • `FOURTEEN_DAYS`: Lượt xem tương tác 14 ngày. • `TWENTY_EIGHT_DAYS`: Lượt xem tương tác 28 ngày. |
| ↳↳ view_attribution_window | string | Khoảng thời gian phân bổ lượt xem (View-through window). Đây là khoảng thời gian từ khi người dùng xem quảng cáo của bạn đến khi thực hiện hành động. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Tắt. • `ONE_DAY`: Lượt xem 1 ngày. • `SEVEN_DAYS`: Lượt xem 7 ngày. |
| ↳↳ attribution_event_count | string | Cách tính số lượng sự kiện (Loại thống kê). ⏎ Cách tính các hành động của người dùng sau khi chỉ xem hoặc nhấp vào quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Chưa thiết lập. • `EVERY`: Tất cả. Tính nhiều sự kiện từ cùng một người dùng thành các lượt chuyển đổi riêng biệt. • `ONCE`: Một lần. Tính nhiều sự kiện từ cùng một người dùng thành 1 lượt chuyển đổi duy nhất. |
| ↳↳ billing_event | string | Sự kiện tính phí. ⏎ Để xem danh sách giá trị enum, xem [Enumerations - Billing event](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ pacing | string | Loại phân phối. Lựa chọn loại phân phối quyết định tốc độ sử dụng ngân sách hàng ngày của bạn. ⏎ Các giá trị enum hỗ trợ: • `PACING_MODE_SMOOTH`: Tiêu chuẩn. Ngân sách sẽ được sử dụng đều nhất có thể tùy thuộc vào nhu cầu thị trường và khung giờ cao điểm. Phù hợp cho các nhà quảng cáo muốn chi tiêu ổn định. |
| ↳↳ automated_keywords_enabled | boolean | Có bật tính năng từ khóa tự động để hệ thống tự tìm các từ khóa liên quan nhằm mở rộng phạm vi tiếp cận và cải thiện kết quả hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ search_keywords | object[] | Chỉ trả về cho Chiến dịch Quảng cáo Tìm kiếm. ⏎ Danh sách các từ khóa tìm kiếm, tức là các từ hoặc cụm từ dùng để so khớp quảng cáo với các cụm từ người dùng tìm kiếm. |
| ↳↳↳ keyword | string | Từ khóa tìm kiếm. |
| ↳↳↳ match_type | string | Loại đối sánh cho từ khóa tìm kiếm. ⏎ Các giá trị enum hỗ trợ: • `PRECISE_WORD`: Đối sánh chính xác. Quảng cáo chỉ hiển thị khi tìm kiếm chứa chính xác cụm từ hoặc biến thể gần, cho phép thêm từ phía trước hoặc phía sau. • `PHRASE_WORD`: Đối sánh cụm từ. Quảng cáo chỉ hiển thị khi tìm kiếm khớp chính xác với từ khóa của bạn hoặc biến thể rất gần. • `BROAD_WORD`: Đối sánh rộng. Quảng cáo hiển thị cho nhiều tìm kiếm liên quan nhằm mang lại phạm vi tiếp cận rộng nhất. |
| ↳↳↳ audit_status | string | Trạng thái xét duyệt của từ khóa tìm kiếm. ⏎ Các giá trị enum hỗ trợ: • `AUDITING`: Từ khóa đang được xét duyệt. • `PASS`: Từ khóa đã vượt qua xét duyệt và có thể phân phối. • `REJECTED`: Từ khóa không vượt qua xét duyệt và không thể phân phối. |
| ↳↳↳ reject_info | object[] | Chỉ được trả về khi `audit_status` là `REJECTED`. ⏎ Chi tiết về lý do từ chối. |
| ↳↳↳↳ forbidden_location | string | Khu vực nhắm mục tiêu không vượt qua xét duyệt. ⏎ Để xem danh sách giá trị enum, xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳↳ reject_reasons | object[] | Danh sách các lý do từ chối. |
| ↳↳↳↳↳ reason | string | Lý do từ chối. |
| ↳↳ budget_mode | string | Chế độ ngân sách nhóm quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `BUDGET_MODE_TOTAL`: Ngân sách trọn đời. • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách hàng ngày động. Đây là ngân sách hàng ngày trung bình trong một tuần. Chi phí hàng ngày sẽ không vượt quá 125% ngân sách hàng ngày trung bình, và chi phí hàng tuần không vượt quá 7 lần ngân sách hàng ngày trung bình. |
| ↳↳ budget_auto_adjust_strategy | string | Chỉ trả về khi thỏa mãn cả 2 điều kiện: • Ở cấp chiến dịch: `budget_optimize_on` là `false`. • Ở cấp nhóm quảng cáo: `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ Chiến lược ngân sách nhóm quảng cáo cho ngân sách tùy chỉnh. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: Bật tự động tăng ngân sách theo mục tiêu. Cho phép ngân sách tự động tăng khi quảng cáo đạt hiệu quả tốt và thỏa mãn CPA mục tiêu, ROAS mục tiêu Ngày 0 cùng các yêu cầu ngân sách. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, giá trị `budget` được chỉ định sẽ là ngân sách hàng ngày ban đầu. Ngân sách hàng ngày sẽ được phép tự động tăng 20%, tối đa 10 lần mỗi ngày khi tỷ lệ sử dụng ngân sách đạt từ 90% trở lên. Ngân sách hàng ngày sẽ được đặt lại về ngân sách ban đầu mỗi ngày. • `UNSET`: Tắt tự động tăng ngân sách theo mục tiêu. |
| ↳↳ budget | float | Ngân sách cố định hoặc ngân sách ban đầu của nhóm quảng cáo. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách hàng ngày ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. |
| ↳↳ current_budget | float | Chỉ được trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách hiện tại của nhóm quảng cáo đã bật tự động tăng ngân sách theo mục tiêu. |
| ↳↳ min_budget | float | Ngân sách tối thiểu của nhóm quảng cáo. ⏎ Hệ thống sẽ cố gắng chi tiêu ít nhất số tiền này nhưng không đảm bảo tuyệt đối. |
| ↳↳ schedule_type | string | Loại lịch chạy. ⏎ Các giá trị enum hỗ trợ: • `SCHEDULE_FROM_NOW`: Chạy nhóm quảng cáo liên tục sau thời gian bắt đầu đã lên lịch. • `SCHEDULE_START_END`: Chạy nhóm quảng cáo trong khoảng thời gian từ thời điểm bắt đầu đến thời điểm kết thúc đã lên lịch. |
| ↳↳ schedule_start_time | string | Thời gian bắt đầu phân phối nhóm quảng cáo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ schedule_end_time | string | Thời gian kết thúc phân phối nhóm quảng cáo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ movie_premiere_date | string | Ngày công chiếu tại rạp, theo định dạng `YYYY-MM-DD` (UTC+0). ⏎ Cung cấp ngày công chiếu giúp hệ thống tích hợp mốc thời gian này để tối ưu hóa hiệu suất. |
| ↳↳ dayparting | string | Phân bổ thời gian phân phối quảng cáo theo khung giờ, định dạng chuỗi gồm 48 x 7 ký tự. ⏎ Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật. Mỗi ký tự có thể nhận giá trị 0 hoặc 1. Giá trị 1 đại diện cho phân phối trong khung 30 phút, và 0 đại diện cho không phân phối. Ký tự đầu tiên tương ứng 0:01-0:30 Thứ Hai; ký tự thứ hai tương ứng 0:31-1:00 Thứ Hai, và ký tự cuối cùng tương ứng 23:31-0:00 Chủ Nhật. ⏎ **Lưu ý**: Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian. |
| ↳↳ targeting_optimization_mode | string | Chế độ tối ưu hóa nhắm mục tiêu đối tượng. ⏎ Các giá trị enum hỗ trợ: • `MANUAL`: Nhắm mục tiêu tùy chỉnh. Bạn có thể sử dụng cài đặt tùy chỉnh để kiểm soát chính xác ai nhìn thấy quảng cáo. Điều này có thể hạn chế phân phối và ảnh hưởng hiệu suất. • `AUTOMATIC`: Nhắm mục tiêu tự động. Sử dụng dữ liệu thời gian thực và máy học để tiếp cận đối tượng có khả năng tương tác cao nhất. |
| ↳↳ suggestion_audience_enabled | boolean | Có bật gợi ý đối tượng (audience suggestions) hay không. ⏎ Gợi ý đối tượng giúp định hướng nhắm mục tiêu tự động thông qua việc chọn các cài đặt đối tượng bổ sung. Các cài đặt này chỉ đóng vai trò gợi ý và không đảm bảo sẽ phân phối đến đúng đối tượng đó. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ targeting_spec | object | Thiết lập nhắm mục tiêu (Targeting settings). |
| ↳↳↳ app_targeting_type | string | Chỉ trả về khi thỏa mãn tất cả điều kiện: • Ở cấp chiến dịch: `objective_type` là `WEB_CONVERSIONS`, `sales_destination` là `APP`, `optimization_goal` là `CLICK`, `IN_APP_EVENT` hoặc `VALUE`. ⏎ Loại nhắm mục tiêu ứng dụng. ⏎ Các giá trị enum hỗ trợ: • `PROSPECT`: Tìm kiếm khách hàng tiềm năng mới, bao gồm những người chưa từng tương tác với sản phẩm. • `RETARGETING`: Nhắm mục tiêu lại (Retargeting). Hiển thị quảng cáo cho những người đã từng tương tác với doanh nghiệp trên và ngoài TikTok. |
| ↳↳↳ location_ids | string[] | Danh sách ID vị trí địa lý bạn muốn nhắm mục tiêu. |
| ↳↳↳ zipcode_ids | string[] | ID mã bưu chính (zip code / postal code) của các vị trí được nhắm mục tiêu. |
| ↳↳↳ spc_audience_age | string | Nhóm tuổi mà nhóm quảng cáo nhắm tới. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Mọi nhóm tuổi. • `OVER_EIGHTEEN`: 18+. • `OVER_TWENTY_FIVE`: 25+. |
| ↳↳↳ languages | string[] | Mã ngôn ngữ mà bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách mã ngôn ngữ được hỗ trợ, xem [Enumerations - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ operating_systems | string[] | Hệ điều hành thiết bị bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. |
| ↳↳↳ excluded_audience_ids | string[] | Danh sách ID đối tượng cần loại trừ. |
| ↳↳↳ age_groups | string[] | Các nhóm tuổi bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ gender | string | Giới tính bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳↳↳ audience_ids | string[] | Danh sách ID đối tượng tùy chỉnh. |
| ↳↳↳ shopping_ads_retargeting_type | string | Loại nhắm mục tiêu lại (Retargeting type). ⏎ Các giá trị enum hỗ trợ: • `LAB1`: Nhắm mục tiêu lại đối tượng đã xem sản phẩm hoặc thêm vào giỏ hàng nhưng chưa mua. • `LAB2`: Nhắm mục tiêu lại đối tượng đã thêm sản phẩm vào giỏ hàng nhưng chưa mua. • `LAB3`: Nhắm mục tiêu lại đối tượng bằng cách kết hợp tùy chỉnh. • `OFF`: Không nhắm mục tiêu lại. |
| ↳↳↳ shopping_ads_retargeting_actions_days | number | Được trả về khi `shopping_ads_retargeting_type` là `LAB1` hoặc `LAB2`. ⏎ Khoảng thời gian hợp lệ cho hành động đối tượng đã chỉ định. Đối tượng hoàn thành hành động trong khoảng thời gian này sẽ được nhắm mục tiêu lại. |
| ↳↳↳ included_custom_actions | object[] | Chi tiết về đối tượng danh mục (catalog audience) cần bao gồm. ⏎ Đối tượng danh mục dựa trên tương tác của người dùng với sản phẩm cụ thể và thường mang lại hiệu suất tốt hơn đối tượng tùy chỉnh. |
| ↳↳↳↳ code | string | Hành động tùy chỉnh dùng để lọc đối tượng cần nhắm mục tiêu lại. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: Đối tượng đã xem sản phẩm. • `ADD_TO_CART`: Đối tượng đã thêm sản phẩm vào giỏ hàng. • `PURCHASE`: Đối tượng đã mua sản phẩm. |
| ↳↳↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc các đối tượng đã hoàn thành hành động được chỉ định. |
| ↳↳↳ excluded_custom_actions | object[] | Chi tiết về đối tượng danh mục cần loại trừ. ⏎ Cải thiện hiệu suất quảng cáo bằng cách loại trừ các sản phẩm mà người dùng đã tương tác, đảm bảo họ chỉ thấy các quảng cáo phù hợp nhất từ thương hiệu của bạn. |
| ↳↳↳↳ code | string | Hành động tùy chỉnh dùng để lọc loại trừ đối tượng. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: Đối tượng đã xem sản phẩm. • `ADD_TO_CART`: Đối tượng đã thêm sản phẩm vào giỏ hàng. • `PURCHASE`: Đối tượng đã mua sản phẩm. |
| ↳↳↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc loại trừ các đối tượng đã hoàn thành hành động được chỉ định. |
| ↳↳↳ shopping_ads_retargeting_custom_audience_relation | string | Mối quan hệ logic giữa đối tượng nhắm mục tiêu lại (xác định bởi `shopping_ads_retargeting_type`) và đối tượng tùy chỉnh (xác định bởi `audience_ids`). ⏎ Các giá trị enum hỗ trợ: • `OR`: Kết hợp đối tượng nhắm mục tiêu lại và đối tượng tùy chỉnh để tạo tệp đối tượng mục tiêu chung. Nhóm quảng cáo sẽ nhắm tới bất kỳ ai thuộc đối tượng danh mục hoặc đối tượng tùy chỉnh. • `AND`: Lấy giao điểm giữa đối tượng nhắm mục tiêu lại và đối tượng tùy chỉnh. Nhóm quảng cáo sẽ chỉ nhắm tới những người thuộc cả hai tệp đối tượng. |
| ↳↳↳ included_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle mà bạn muốn bao gồm. |
| ↳↳↳ excluded_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle mà bạn muốn loại trừ. |
| ↳↳↳ interest_category_ids | string[] | Danh sách ID từ khóa sở thích chung bạn muốn dùng để nhắm mục tiêu đối tượng. |
| ↳↳↳ interest_keyword_ids | string[] | Danh sách ID danh mục sở thích bổ sung bạn muốn dùng để nhắm mục tiêu đối tượng. ⏎ Để tìm kiếm các danh mục sở thích bổ sung, sử dụng [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (khuyến nghị) hoặc [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| ↳↳↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm bạn muốn dùng để nhắm mục tiêu đối tượng quan tâm đến việc mua hàng liên quan đến một danh mục nội dung. |
| ↳↳↳ actions | object[] | Danh sách các đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳↳↳↳ action_scene | string | Loại hành vi người dùng bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_RELATED`: Tương tác với video. • `CREATOR_RELATED`: Tương tác với nhà sáng tạo. • `HASHTAG_RELATED`: Tương tác với hashtag. |
| ↳↳↳↳ action_period | number | Khoảng thời gian thu thập hành vi. |
| ↳↳↳↳ video_user_actions | string[] | Tương tác cụ thể của người dùng bạn muốn nhắm mục tiêu cho loại hành vi người dùng tương ứng. • Nếu `action_scene` là `VIDEO_RELATED`, các giá trị được phép là: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`. • Nếu `action_scene` là `CREATOR_RELATED`, các giá trị được phép là: `FOLLOWING`, `VIEW_HOMEPAGE`. • Nếu `action_scene` là `HASHTAG_RELATED`, giá trị được phép là: `VIEW_HASHTAG`. |
| ↳↳↳↳ action_category_ids | string[] | Danh sách ID danh mục tương tác video, danh mục tương tác nhà sáng tạo, hashtag hoặc nhóm hashtag bạn muốn dùng để nhắm mục tiêu đối tượng. |
| ↳↳↳ smart_interest_behavior_enabled | boolean | Có bật tính năng Sở thích & Hành vi thông minh (Smart interests & behaviors) hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Để tìm hiểu thêm về Sở thích & Hành vi thông minh và cách bật tính năng này, xem [Nhắm mục tiêu thông minh (Smart Targeting)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳↳ smart_audience_enabled | boolean | Có bật tính năng Đối tượng thông minh (Smart audience) hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Để tìm hiểu thêm về Đối tượng thông minh và cách bật tính năng này, xem [Nhắm mục tiêu thông minh (Smart Targeting)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳↳ spending_power | string | Sức chi tiêu bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `ALL`, `HIGH`. ⏎ Nếu đặt thành `HIGH`, bạn có thể nhắm mục tiêu người dùng có sức chi tiêu cao, những người thường chi tiêu nhiều hơn cho mua sắm trên quảng cáo TikTok so với người dùng trung bình. |
| ↳↳↳ household_income | string[] | Thu nhập hộ gia đình bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `TOP5` (Top 5% mã ZIP), `TOP10` (Top 10% mã ZIP), `TOP10_25` (Top 10% - 25% mã ZIP), `TOP25_50` (Top 25% - 50% mã ZIP). |
| ↳↳↳ min_android_version | string | Phiên bản Android tối thiểu. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ min_ios_version | string | Phiên bản iOS tối thiểu của đối tượng. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị. |
| ↳↳↳ network_types | string[] | Loại mạng bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ carrier_ids | string[] | Danh sách nhà mạng bạn muốn nhắm mục tiêu. |
| ↳↳↳ isp_ids | string[] | Danh sách ID nhà cung cấp dịch vụ Internet (ISP) được nhắm mục tiêu. |
| ↳↳↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu. 10000 nghĩa là 1000+. Các số phải là bội số của 50. ⏎ **Quan trọng**: Giới hạn trên bạn đặt sẽ được cộng thêm 50 và số mới thu được sẽ được sử dụng làm giới hạn trên thực tế cho nhắm mục tiêu thiết bị. Giới hạn trên thực tế được hiển thị trong cài đặt nhóm quảng cáo trên Trình quản lý quảng cáo TikTok. Nếu bạn đặt và nhận khoảng giá [0, 250], điều đó thực tế có nghĩa là [0, 300]. |
| ↳↳↳ saved_audience_id | string | Được trả về khi bạn đã chỉ định `saved_audience_id` khi tạo nhóm quảng cáo. ⏎ ID Đối tượng đã lưu (Saved Audience ID). |
| ↳↳↳ blocked_pangle_app_ids | string[] | Danh sách ID ứng dụng Pangle bị chặn. |
| ↳↳↳ brand_safety_type | string | Cấp bộ lọc khoảng không quảng cáo (Inventory filter tier) cho Chiến dịch Smart+. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Khoảng không quảng cáo mở rộng. Quảng cáo của bạn sẽ không xuất hiện cạnh nội dung không phù hợp rõ ràng, nhưng có thể xuất hiện cạnh nội dung có chủ đề trưởng thành. • `STANDARD_INVENTORY`: Khoảng không quảng cáo tiêu chuẩn. Quảng cáo của bạn sẽ xuất hiện cạnh nội dung phù hợp với hầu hết các thương hiệu. • `LIMITED_INVENTORY`: Khoảng không quảng cáo giới hạn. Quảng cáo của bạn sẽ không xuất hiện cạnh nội dung có chủ đề trưởng thành. • `NO_BRAND_SAFETY`: Toàn bộ khoảng không quảng cáo mà không sử dụng giải pháp an toàn thương hiệu nào, đồng nghĩa quảng cáo có thể xuất hiện cạnh một số nội dung có chủ đề trưởng thành. ⏎ **Lưu ý**: Cài đặt này được áp dụng tự động dựa trên cấu hình [Trung tâm an toàn thương hiệu (Brand Safety Hub)](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) của bạn. Để truy xuất chi tiết các cài đặt này cho tài khoản quảng cáo, sử dụng [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳↳↳ category_exclusion_ids | string[] | Danh sách ID danh mục nội dung cần loại trừ. |
| ↳↳ is_hfss | boolean | Nội dung quảng bá có phải là sản phẩm/thương hiệu HFSS (Nhiều chất béo, muối, đường) hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ is_lhf_compliance | boolean | Nội dung quảng bá có tuân thủ quy định LHF (Thực phẩm kém lành mạnh) hay không. ⏎ Khi `is_lhf_compliance` là `true`, bạn xác nhận rằng bất kỳ sản phẩm thực phẩm hoặc đồ uống nào bạn quảng cáo trên TikTok tại Vương quốc Anh đều tuân thủ [Quy định về thực phẩm kém lành mạnh năm 2024 (2024 Less Healthy Foods Regulations)](https://www.legislation.gov.uk/uksi/2024/1266/made) và tất cả các luật hiện hành khác. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ placement_type | string[] | Chiến lược vị trí vị trí hiển thị (placement) quyết định nơi quảng cáo xuất hiện. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TYPE_AUTOMATIC`: Vị trí tự động (Automatic placement). • `PLACEMENT_TYPE_NORMAL`: Chọn vị trí thủ công (Select placement). |
| ↳↳ placements | string[] | Các ứng dụng bạn muốn phân phối quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TIKTOK`: TikTok. • `PLACEMENT_PANGLE`: Pangle. • `PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle. |
| ↳↳ tiktok_subplacements | string[] | Các vị trí phụ bên trong TikTok cho quảng cáo, cho phép bạn chọn nơi quảng cáo xuất hiện. ⏎ Các giá trị enum hỗ trợ: • `LEMON8`: Lemon8, ứng dụng cộng đồng cho nội dung đời sống, tập trung vào trải nghiệm thực tế, mẹo, hướng dẫn và đánh giá sản phẩm. Khi bao gồm Lemon8 làm vị trí phụ, quảng cáo sẽ xuất hiện trên bảng tin Dành cho bạn (For You feed), bảng tin Tìm kiếm và bảng tin Video chân thực. [Tìm hiểu thêm về Lemon8 cho Đấu thầu hiệu suất](https://ads.tiktok.com/help/article/about-lemon8-in-tiktok-ads-manager). • `PINE_DRAMA`: PineDrama, ứng dụng xem phim truyền hình ngắn tập. Quảng cáo sẽ được đặt trên các trang đề xuất, trong luồng tập phim và hơn thế nữa. [Tìm hiểu thêm về PineDrama cho Đấu thầu hiệu suất](https://ads.tiktok.com/help/article/about-pinedrama-for-performance-auction-in-tiktok-ads-manager). |
| ↳↳ search_result_enabled | boolean | Có bao gồm quảng cáo của bạn trong Quảng cáo Tìm kiếm (Search Ads) hay không, cụ thể là hiển thị quảng cáo khi người dùng tìm kiếm doanh nghiệp của bạn trên TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ comment_disabled | boolean | Có tắt tính năng bình luận trên quảng cáo TikTok hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ share_disabled | boolean | Có tắt tính năng chia sẻ chiến dịch sang các nền tảng bên thứ ba hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ video_download_disabled | boolean | Người dùng có thể tải xuống quảng cáo video của bạn trên TikTok hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ skip_learning_phase | boolean | Có bỏ qua giai đoạn máy học (learning phase) hay không. ⏎ Giá trị hỗ trợ: `true`. |
| ↳↳ create_time | string | Thời điểm nhóm quảng cáo được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Ví dụ: `2025-01-01 00:00:01`. |
| ↳↳ modify_time | string | Thời điểm nhóm quảng cáo được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Ví dụ: `2025-01-01 00:00:01`. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "bid_type": "BID_TYPE_NO_BID",
                "billing_event": "CPC",
                "budget": 0,
                "budget_mode": "BUDGET_MODE_INFINITE",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "catalog_authorized_bc_id": "{{catalog_authorized_bc_id}}",
                "catalog_id": "{{catalog_id}}",
                "comment_disabled": false,
                "conversion_bid_price": 0,
                "create_time": "{{create_time}}",
                "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "optimization_goal": "CLICK",
                "pacing": "PACING_MODE_SMOOTH",
                "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                "placements": [
                    "PLACEMENT_TIKTOK"
                ],
                "product_source": "CATALOG",
                "promotion_type": "WEBSITE",
                "promotion_website_type": "UNSET",
                "schedule_end_time": "{{schedule_end_time}}",
                "schedule_start_time": "{{schedule_start_time}}",
                "schedule_type": "SCHEDULE_START_END",
                "search_result_enabled": true,
                "secondary_status": "ADGROUP_STATUS_TIME_DONE",
                "share_disabled": false,
                "targeting_optimization_mode": "AUTOMATIC",
                "targeting_spec": {
                    "age_groups": [
                        "AGE_18_24",
                        "AGE_25_34",
                        "AGE_35_44",
                        "AGE_45_54",
                        "AGE_55_100"
                    ],
                    "brand_safety_type": "EXPANDED_INVENTORY",
                    "gender": "GENDER_UNLIMITED",
                    "location_ids": [
                        "3686110"
                    ],
                    "spc_audience_age": "OVER_EIGHTEEN",
                    "spending_power": "ALL"
                },
                "video_download_disabled": false
            },
            {
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "attribution_event_count": "EVERY",
                "bid_type": "BID_TYPE_NO_BID",
                "billing_event": "OCPM",
                "budget": 0,
                "budget_mode": "BUDGET_MODE_INFINITE",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "catalog_authorized_bc_id": "{{catalog_authorized_bc_id}}",
                "catalog_id": "{{catalog_id}}",
                "click_attribution_window": "SEVEN_DAYS",
                "comment_disabled": false,
                "conversion_bid_price": 0,
                "create_time": "{{create_time}}",
                "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "optimization_event": "ADD_BILLING",
                "optimization_goal": "CONVERT",
                "pacing": "PACING_MODE_SMOOTH",
                "pixel_id": "{{pixel_id}}",
                "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                "placements": [
                    "PLACEMENT_TIKTOK"
                ],
                "product_source": "CATALOG",
                "promotion_type": "WEBSITE",
                "promotion_website_type": "UNSET",
                "schedule_end_time": "{{schedule_end_time}}",
                "schedule_start_time": "{{schedule_start_time}}",
                "schedule_type": "SCHEDULE_START_END",
                "search_result_enabled": true,
                "secondary_status": "ADGROUP_STATUS_TIME_DONE",
                "share_disabled": false,
                "skip_learning_phase": true,
                "targeting_optimization_mode": "AUTOMATIC",
                "targeting_spec": {
                    "age_groups": [
                        "AGE_18_24",
                        "AGE_25_34",
                        "AGE_35_44",
                        "AGE_45_54",
                        "AGE_55_100"
                    ],
                    "brand_safety_type": "EXPANDED_INVENTORY",
                    "gender": "GENDER_UNLIMITED",
                    "location_ids": [
                        "6252001"
                    ],
                    "spc_audience_age": "OVER_EIGHTEEN",
                    "spending_power": "ALL"
                },
                "video_download_disabled": false,
                "view_attribution_window": "ONE_DAY"
            },
            {
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "app_id": "{{app_id}}",
                "attribution_event_count": "EVERY",
                "bid_type": "BID_TYPE_NO_BID",
                "billing_event": "OCPM",
                "budget": 0,
                "budget_mode": "BUDGET_MODE_INFINITE",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "click_attribution_window": "SEVEN_DAYS",
                "comment_disabled": false,
                "conversion_bid_price": 0,
                "create_time": "{{create_time}}",
                "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                "deep_bid_type": "AEO",
                "engaged_view_attribution_window": "SEVEN_DAYS",
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "optimization_event": "ACTIVE_PAY",
                "optimization_goal": "IN_APP_EVENT",
                "pacing": "PACING_MODE_SMOOTH",
                "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
                "placements": [
                    "PLACEMENT_TIKTOK",
                    "PLACEMENT_GLOBAL_APP_BUNDLE",
                    "PLACEMENT_PANGLE"
                ],
                "promotion_type": "APP_ANDROID",
                "schedule_end_time": "{{schedule_end_time}}",
                "schedule_start_time": "{{schedule_start_time}}",
                "schedule_type": "SCHEDULE_START_END",
                "search_result_enabled": true,
                "secondary_status": "ADGROUP_STATUS_TIME_DONE",
                "share_disabled": false,
                "skip_learning_phase": true,
                "targeting_optimization_mode": "AUTOMATIC",
                "targeting_spec": {
                    "age_groups": [
                        "AGE_18_24",
                        "AGE_25_34",
                        "AGE_35_44",
                        "AGE_45_54",
                        "AGE_55_100"
                    ],
                    "brand_safety_type": "EXPANDED_INVENTORY",
                    "gender": "GENDER_UNLIMITED",
                    "location_ids": [
                        "1562822"
                    ],
                    "operating_systems": [
                        "ANDROID"
                    ],
                    "spc_audience_age": "OVER_EIGHTEEN",
                    "spending_power": "ALL"
                },
                "video_download_disabled": false,
                "view_attribution_window": "ONE_DAY"
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

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 2/7**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def execute_request():
    url = f"{BASE_URL}/example/get/"
    params = {"advertiser_id": ADVERTISER_ID}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    execute_request()
```

