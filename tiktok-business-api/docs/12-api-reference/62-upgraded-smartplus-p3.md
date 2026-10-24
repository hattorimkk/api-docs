# Smart+ nâng cấp (Upgraded Smart+) — phần 3/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Tạo nhóm quảng cáo Smart+ nâng cấp (#doc-1843314887930946)](#doc-1843314887930946)

---

<a id="doc-1843314887930946"></a>
<!-- doc_id: 1843314887930946 -->
<!-- doc_id: 1843314887930946 -->
# Tạo nhóm quảng cáo Smart+ nâng cấp (Create an Upgraded Smart+ Ad Group)
> Đường dẫn: API Reference > Smart+ nâng cấp > Nhóm quảng cáo > Tạo nhóm quảng cáo Smart+ nâng cấp
Sử dụng endpoint này để tạo một nhóm quảng cáo Smart+ nâng cấp.

Bạn có thể tạo tối đa 30 nhóm quảng cáo trong một Chiến dịch Smart+ nâng cấp.
- Nếu Tối ưu hóa ngân sách chiến dịch (CBO) được bật (`budget_optimize_on` là `true`) ở cấp chiến dịch, bạn cần đảm bảo các cài đặt sau (nếu được chỉ định) phải giống nhau đối với tất cả các nhóm quảng cáo trong cùng chiến dịch:
	- `promotion_type`
	- `promotion_target_type`
	- `optimization_goal`
	- `optimization_event`
	- `app_attribution_source`
	- `app_data_source`
	- `billing_event`
	- `bid_type`
	- `bid_price`
	- `conversion_bid_price`
	- `deep_bid_type`
	- `vbo_window`
	- `roas_bid`
	- `identity_id`, `identity_type`, `identity_authorized_bc_id` và `native_series_id` (khi `promotion_type` là `NATIVE_SERIES`)
- Nếu CBO bị tắt (`budget_optimize_on` là `false`) ở cấp chiến dịch, bạn cần đảm bảo các cài đặt sau (nếu được chỉ định) phải giống nhau đối với tất cả các nhóm quảng cáo trong cùng chiến dịch:
	- `bid_type`
	- `deep_bid_type`
	- `vbo_window`
	- `budget_mode`

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| request_id  ****(Bắt buộc)**** | string | Request ID with which you can create ad groups with duplicate names. It also supports idempotency to prevent you from sending the same request twice. If you retry requests with the same request ID multiple times, then only one will succeed. ⏎ It is different from the `request_id` returned in the response parameters, which is used to uniquely identify an HTTP request. ⏎ The value should be a string representation of a 64-bit integer number. ⏎ Example: `123456789`. |
| campaign_id  ****(Bắt buộc)**** | string | The ID of the campaign that the ad group belongs to. |
| operation_status | string | The status of the ad group when created. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad group is enabled when created. • `DISABLE` : The ad group is disabled when created. ⏎ Giá trị mặc định: `ENABLE`. |
| adgroup_name  ****(Bắt buộc)**** | string | Ad group name. ⏎ Giới hạn độ dài: 512 characters. Emoji is not supported. |
| catalog_id **(Điều kiện)** | string | Bắt buộc khi `catalog_enabled` is `true` at the campaign level. ⏎ The ID of the catalog to use in the ad group. ⏎ To retrieve the catalogs within your Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610). |
| catalog_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `catalog_enabled` is `true`. ⏎ The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| product_source **(Điều kiện)** | string | Bắt buộc khi the following conditions are met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `catalog_enabled` is `true`. • `catalog_type` is `ONLINE_TO_OFFLINE` or `TRAVEL_ENTERTAINMENT`. Learn more about how to create such ads in [Create Upgraded Smart+ App Online-to-Offline Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1875231879602658) and [Create Upgraded Smart+ App Travel Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1879220213492353). ⏎ Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| promotion_type  ****(Bắt buộc)**** | string | Promotion type (Optimization location). ⏎ You can decide where you'd like to promote your products using this field. ⏎ Currently, we support `APP_ANDROID`, `APP_IOS`, `WEBSITE`, `MINI_APP`, `MINI_GAME`, `NATIVE_SERIES`,  `LEAD_GENERATION`, `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`, `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`, `LEAD_GEN_CLICK_TO_CALL`, and `LEAD_GENERATION_MULTI_DESTINATION`. • When `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTAL` or `APP_RETARGETING`, set this field to `APP_ANDROID` or `APP_IOS`. • When `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `MINIS`, set this field to `MINI_APP`, `MINI_GAME`, or `NATIVE_SERIES`. • When `objective_type` is `WEB_CONVERSIONS`: • If `sales_destination` is `WEBSITE`, set this field to `WEBSITE`. • If `sales_destination` is `APP`, set this field to `APP_ANDROID` or `APP_IOS`. • When `objective_type` is `LEAD_GENERATION`, set this field to any of the following values: • `LEAD_GENERATION` • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` • `LEAD_GEN_CLICK_TO_CALL` • `LEAD_GENERATION_MULTI_DESTINATION` ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true` ) at the campaign level, this setting must be the same across all ad groups within the same campaign. |
| promotion_target_type | string | Valid when `objective_type` is `LEAD_GENERATION`. ⏎ The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| optimization_goal  ****(Bắt buộc)**** | string | The measurable results you'd like to drive with your campaigns. ⏎ Currently, we support `CLICK`, `INSTALL`, `IN_APP_EVENT`, `VALUE`, `CONVERT`, `TRAFFIC_LANDING_PAGE_VIEW`, `CONVERSATION`, `LEAD_GENERATION`, `LEADS`, and `WEBSITE_ENGAGEMENT`. ⏎ To find the detailed description for each optimization goal, see [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**:  • When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. • When `promotion_type` is `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` and `optimization_goal` is `CONVERSATION`, you can only set `messaging_app_type` to any of the following values: • `MESSENGER` • `WHATSAPP` • `ZALO` |
| optimization_locations **(Điều kiện)** | object[] | Bắt buộc khi `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION`. ⏎ A list of optimization locations for the Lead Generation ad group. ⏎ You need to specify at least two optimization locations in this field. ⏎ To learn about the ad type where this field can be used, see [Create an Upgraded Smart+ Lead Generation Campaign with multiple location selection](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1876685025962241). ⏎ **Note**: • Creating an Upgraded Smart+ Lead Generation Campaign with multiple location selection is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Once set, this field cannot be updated. |
| ↳ promotion_type | string | Promotion type (Optimization location). ⏎ You can decide where you want audiences to convert or complete an action. ⏎ Các giá trị enum hỗ trợ: `LEAD_GENRATION`, `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`. |
| ↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳ optimization_event | string | Optimization event. ⏎ Các giá trị enum hỗ trợ: • `ON_WEB_REGISTER`: Complete registration. • `CONSULT`: Contact. • `FORM`: Submit form. • `ON_WEB_SUBSCRIBE`: Subscribe. |
| app_id **(Điều kiện)** | string | Bắt buộc khi the following conditions are both met: ⏎ At the campaign level: • `objective_type` is`APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`, or `objective_type` is`WEB_CONVERSIONS` and `sales_destination` is `APP`. • `camapign_type` is `REGULAR_CAMPAIGN`. ⏎ The App ID of the app to promote. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). ⏎ **Note**: You cannot specify an App that has not activated the SAN module on your MMP through this field to create ad groups. To ensure that TikTok SAN integration is enabled for your App, see [How to migrate your app to SAN integration](https://ads.tiktok.com/help/article/transition-to-san-for-existing-apps). |
| gaming_ad_compliance_agreement | string | Valid in any of the following scenarios: • Scenario 1: When the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • Scenario 2: When the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `REGULAR_CAMPAIGN`. ⏎ Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: You confirm and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. ⏎ Giá trị mặc định: `OFF`. ⏎ **Note**: Agreeing to the Compliance Assurance Policy for Gaming Advertisers on TikTok is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| pixel_id **(Điều kiện)** | string | • Bắt buộc khi the following conditions are met: • At the campaign level: `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION`. • At the ad group level: `optimization_goal` is set to `CONVERT` or `VALUE`. • Not supported when `optimization_goal` is set to `CLICK`, `INSTALL`, `IN_APP_EVENT`, or `TRAFFIC_LANDING_PAGE_VIEW`. ⏎ ID TikTok Pixel. ⏎ To get all Pixel IDs, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978). |
| app_config **(Điều kiện)** | object[] | Bắt buộc khi `sales_destination` is `WEB_AND_APP` at the campaign level. ⏎ Details of the app or apps to promote. ⏎ Kích thước tối đa: 2. ⏎ You can specify any of the following in this field: • an Android app • an iOS app • an Android app and an iOS app |
| ↳ app_id **(Điều kiện)** | string | Bắt buộc khi `app_config` is specified. ⏎ The App ID of the app to promote. ⏎ To obtain the list of App IDs within your ad account, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `app_id`. |
| minis_id **(Điều kiện)** | string | Bắt buộc khi `promotion_type` is `MINI_APP` or `MINI_GAME`. ⏎ The ID of a TikTok Mini. • When `promotion_type` is `MINI_APP`, specify a TikTok Mini ID of the mini series type. • When `promotion_type` is `MINI_GAME`, specify a TikTok Mini ID of the mini game type. ⏎ To obtain the list of TikTok Minis within an ad account, use [/minis/get/](70-tools-p2.md#doc-1853450329535490) and select a TikTok Mini with `minis_status` as `ACTIVE`. ⏎ To learn more about the campaign type where this setting is supported, see [Create an Upgraded Smart+ TikTok Growth Max: Mini Dramas campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1853377811982657) and [Create an Upgraded Smart+ TikTok Growth Max: Mini Games campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1868121865281538). |
| optimization_event **(Điều kiện)** | string | Required in any of the following scenarios: • `pixel_id` is specified. • `pixel_id` is not specified and `optimization_goal` is `IN_APP_EVENT` or `VALUE`. • `pixel_id` is not specified and `minis_id` is specified. ⏎ Conversion event. ⏎ For the supported app and pixel events, see [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). ⏎ To find out the supported events for your app, use [/app/optimization_event/](43-events-1-0-p1.md#doc-1740859338750977). ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| custom_conversion_id | string | The ID of the Custom Conversion to use in the ad group. ⏎ Chỉ hợp lệ khi the following conditions are all met: • Either `pixel_id` or `app_id` is specified. • A Custom Conversion has been configured for the `pixel_id` or `app_id`. • The `optimization_goal` is set to `CONVERT` or `IN_APP_EVENT`. • The parameter `optimization_event` is specified and matches the Standard Event associated with the Custom Conversion. • The status of the Custom Conversion is Active or No recent activity. ⏎ • To obtain the list of Custom Conversions associated with a Pixel or an App, use [/custom_conversion/list/](39-custom-conversions.md#doc-1842225174460673).  • To confirm the eligibility of the Custom Conversion for ad group creation: • Ensure the returned `optimization_event` matches the `optimization_event` specified during ad group creation.  • Ensure the `activity_status` is `NO_RECENT_ACTIVITY` or `ACTIVE`. |
| deep_funnel_optimization_status | string | Chỉ hợp lệ khi `promotion_type` is `LEAD_GENERATION`. ⏎ The status of deep funnel optimization. ⏎ Deep funnel optimization optimizes both your upper funnel events and deeper funnel events. You can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: To enable deep funnel optimization. • `OFF`: To disable deep funnel optimization. ⏎ Giá trị mặc định: `OFF`. ⏎ **Note**:  • Deep funnel optimization with CRM events is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Deep funnel optimization with Pixel or Offline events is generally available. |
| deep_funnel_event_source **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel. • `OFFLINE`: Offline Event Set. • `CRM`: CRM Event Set. |
| deep_funnel_event_source_id **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. • When `deep_funnel_event_source` is `PIXEL`, specify a ID TikTok Pixel via this field. • To obtain a list of Pixels, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978). • When `deep_funnel_event_source` is `OFFLINE`, specify an Offline Event Set ID via this field. • To obtain a list of Offline Event Set IDs, use [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313). • When `deep_funnel_event_source` is `CRM`, specify a CRM Event Set ID via this field. • To obtain a list of CRM Event Set IDs, use [/crm/list/](43-events-1-0-p2.md#doc-1780896521680898). |
| deep_funnel_optimization_event **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ • To find out the supported values for Standard Events available for Pixels, Offline Event Sets, and CRM Event Sets, see the **"Event name for ad creation"** column in [Supported Pixel events](../09-marketing-api/do-luong-quang-cao-p2.md#doc-1739585696931842). •  To find the list of optimization events for a Pixel, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978) and check the returned `optimization_event`. ⏎ Example: `SHOPPING`. |
| app_attribution_source | string | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level, `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. • The mobile app is eligible for attribution source and data source configuration. • To confirm this, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297) and select an `app_id` where `is_attribution_flex_enable` returns `true`. ⏎ Attribution source for your mobile app. ⏎ The attribution source you choose will be used for optimization, bidding, and reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP (mobile measurement partner) attribution. Signals from your selected MMP will be used for attribution. • `SAN`: SAN (self-attribution network) attribution. Signals from TikTok SAN will be used for attribution. The exact value you can specify depends on your app (`app_id`) setup. To retrieve the available attribution and data source settings for your app, use [/tool/available/attribution_source/](70-tools-p2.md#doc-1870952425111618). ⏎ **Note**:  • Once set, this field cannot be updated. • When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. • Attribution source and data source configuration for an app during Upgraded Smart+ Ad Group creation is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| app_data_source | string | Data source for your app. ⏎ The attribution signals you select will be used for reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP signals. Signals from your MMP will be used for reporting. • `EVENT_SDK`: App Events SDK signals. Signals from TikTok App Events SDK will be used for reporting. • `EVENT_API`: Events API signals. Signals from TikTok Events API will be used for reporting. ⏎ The exact value you can specify depends on your app (`app_id`) setup. To retrieve the available attribution and data source settings for your app, use [/tool/available/attribution_source/](70-tools-p2.md#doc-1870952425111618). ⏎ **Note**:  • Once set, this field cannot be updated. • When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. • Attribution source and data source configuration for an app during Upgraded Smart+ Ad Group creation is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| identity_id | string | Chỉ hợp lệ trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ ID danh tính (Identity ID). |
| identity_type | string | Valid only in any of the following scenarios:  • Scenario 1: When `promotion_type` is `NATIVE_SERIES`. • Scenario 2: When `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` and your ad account is allowlisted for selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads. ⏎ Identity type of the TikTok account where your Series is hosted and managed in TikTok Growth Max: Drama Series ads or the TikTok account to use in TikTok Direct Messaging Ads. ⏎ Các giá trị enum hỗ trợ: ⏎ • `TT_USER`: TikTok Business Account User. • `BC_AUTH_TT`: The TikTok account that a Business Center is authorized to access. ⏎ See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. ⏎ **Note**: • Selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Once set, this field cannot be updated. |
| identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. ⏎ **Note**: Once set, this field cannot be updated. |
| native_series_id **(Điều kiện)** | string | Bắt buộc khi `promotion_type` is `NATIVE_SERIES`. ⏎ The ID of a TikTok Series. ⏎ Series offers exclusive and premium video packages produced by creators. Access to Series is available to purchase through the creator's profile and links attached to TikTok videos. ⏎ To obtain the list of TikTok Series available from a TikTok account that your ad account can access, use [/identity/native_series/get/](70-tools-p2.md#doc-1863332009162754) . |
| messaging_app_type **(Điều kiện)** | string | Chỉ hợp lệ khi `promotion_type` is `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`. • When `optimization_goal` is `CONVERSATION`, this field is required. • When `optimization_goal` is `CLICK`, the Giá trị mặc định for this field is `IM_URL`. ⏎ The type of instant messaging app or customized URL to use in the Instant Messaging App Ad Group. ⏎ Các giá trị enum hỗ trợ: • `MESSENGER`: Messenger. You need to simultaneously specify a Facebook Page ID via `messaging_app_account_id`. • `WHATSAPP`: WhatsApp. You need to simultaneously specify `phone_info`, which will be used to automatically populate the corresponding WhatsApp phone number. • `ZALO`: Zalo. You need to simultaneously specify Zalo contact format via `zalo_id_type`.  • `LINE`: Line. You need to simultaneously specify a LINE Business ID via `messaging_app_account_id`. • `IM_URL`: Instant Messaging URL. ⏎ To learn more about how to create Upgraded Smart+ TikTok Instant Messaging Ads, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302988449921). ⏎ **Note**:  • When `optimization_goal` is `CONVERSATION`, you cannot set this field to `LINE` or `IM_URL`. • Once set, this field cannot be updated. |
| zalo_id_type **(Điều kiện)** | string | Bắt buộc khi `messaging_app_type` is `ZALO`. ⏎ The type of Zalo contact format. ⏎ Các giá trị enum hỗ trợ: • `ZALO_OFFICIAL_ACCOUNT`: Zalo Official Account ID. You need to simultaneously specify a Zalo Official Account ID via `messaging_app_account_id`. • `ZALO_PHONE_ACCOUNT`: Zalo phone number. You need to simultaneously specify `phone_info` to automatically populate the corresponding Zalo phone number. • You can only set `zalo_id_type` to `ZALO_PHONE_ACCOUNT` when `optimization_goal` is `CLICK`. ⏎ **Note**: Once set, this field cannot be updated. |
| messaging_app_account_id **(Điều kiện)** | string | Required and valid in any of the following scenarios: • When `messaging_app_type` is `MESSENGER` or `LINE`. • When `messaging_app_type` is `ZALO` and `zalo_id_type` is `ZALO_OFFICIAL_ACCOUNT`. ⏎ The ID of the instant messaging app account. • When `messaging_app_type` is `MESSENGER`, specify the Facebook Page ID via this field. • To find your Facebook Page ID, go to your Facebook Page and click About below your cover photo, then click Page transparency. • When  `zalo_id_type` is `ZALO_OFFICIAL_ACCOUNT`, specify the Zalo Official Account ID via this field. • When `messaging_app_type` is `LINE`, specify the LINE Business ID via this field. • To find your LINE Business ID, go to your LINE official account page. • When `messaging_app_type` is `WHATSAPP` or when `zalo_id_type` is `ZALO_PHONE_ACCOUNT`, this field will be ignored and be set as the corresponding WhatsApp or Zalo phone number automatically populated based on the specified `phone_info`. ⏎ **Note**: Once set, this field cannot be updated. |
| message_event_set_id **(Điều kiện)** | string | Bắt buộc khi the following conditions are met: • `promotion_type` is `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`. • `optimization_goal` is `CONVERSATION`. • The instant messaging app account in your ad group settings doesn't match any existing message event set. ⏎ The ID of the message event set to be used in the Instant Messaging Ad Group. • If the instant messaging app account, either the Messenger account or Zalo Official Account specified via `messaging_app_account_id` or the WhatsApp or Zalo phone account populated from the specified `phone_info`, in your ad group settings matches an existing event set, this field will be **ignored and automatically populated** with the unique message event set associated with the instant messaging app account you choose. • To confirm Liệu a unique message event set is associated with the instant messaging app account you choose, use [/ctm/message_event_set/get/](43-events-1-0-p2.md#doc-1816979158055937) and check the returned `matched_event_set`. • If the instant messaging app account in your ad group settings doesn't match any existing message event set (`matched_event_set` returned from `/ctm/message_event_set/get/` is empty), use [/ctm/message_event_set/get/](43-events-1-0-p2.md#doc-1816979158055937) to obtain the message event sets available for ad creation via the response parameter `message_event_set_list`. ⏎ **Note**: Once set, this field cannot be updated. |
| phone_info **(Điều kiện)** | object | Required in any of the following scenarios: • When `messaging_app_type` is `WHATSAPP` • When `messaging_app_type` is `ZALO` and `zalo_id_type` is `ZALO_PHONE_ACCOUNT`. ⏎ Details of WhatsApp or Zalo phone number. ⏎ **Note**: Once set, this field cannot be updated. |
| ↳ phone_region_code **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The region code for WhatsApp or Zalo phone number. ⏎ Example: `US`. ⏎ To obtain the region code (`phone_region_code`) and region calling code (`phone_region_calling_code`) for the region that is associated with a specific phone number, use [/tool/phone_region_code/](70-tools-p2.md#doc-1774488637039618). |
| ↳ phone_region_calling_code **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The region calling code for the WhatsApp or Zalo phone number. ⏎ Example: `+1`. ⏎ To obtain the region code (`phone_region_code`) and region calling code (`phone_region_calling_code`) for the region that is associated with a specific phone number, use [/tool/phone_region_code/](70-tools-p2.md#doc-1774488637039618). |
| ↳ phone_number **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The WhatsApp or Zalo phone number. ⏎ For WhatsApp, use the same WhatsApp phone number connected to the Messagement Management Tool (MMT). |
| bid_type  ****(Bắt buộc)**** | string | Bidding strategy that determines how the system manages your cost per result, spends your budget, and how it delivers campaigns. ⏎ Các giá trị enum hỗ trợ: • `BID_TYPE_NO_BID`: Maximum Delivery. • `BID_TYPE_CUSTOM`: Cost Cap (or Target CPA). ⏎ **Note**: This setting, if specified, must be the same across all ad groups within the same campaign. |
| bid_price **(Điều kiện)** | float | Bắt buộc khi the following conditions are met: • `optimization_goal` is `CLICK`. • `bid_type` is `BID_TYPE_CUSTOM`. ⏎ The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| conversion_bid_price **(Điều kiện)** | float | Bắt buộc khi the following conditions are met: • `optimization_goal` is `CONVERT`,`TRAFFIC_LANDING_PAGE_VIEW` , `INSTALL`, or `IN_APP_EVENT`. • `bid_type` is `BID_TYPE_CUSTOM`. ⏎ The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `conversion_bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| deep_bid_type **(Điều kiện)** | string | Bắt buộc khi `optimization_goal` is `VALUE`. ⏎ Bidding strategy for in-app events. ⏎ Các giá trị enum hỗ trợ: `DEFAULT`, `AEO`, `VO_MIN_ROAS`, and `VO_HIGHEST_VALUE`. ⏎ For the descriptions of supported values, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ You can only set `deep_bid_type` to `VO_MIN_ROAS` in any of the following scenarios: • At the campaign level, `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`  • At the ad group level, `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` ⏎ **Note**: This setting, if specified, must be the same across all ad groups within the same campaign. |
| roas_bid **(Điều kiện)** | float | Bắt buộc khi `deep_bid_type` is `VO_MIN_ROAS`. ⏎ Target ROAS for Value-Based Optimization. ⏎ Value range: 0.01-1,000. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| value_rule_set_id | string | ID của bộ quy tắc giá trị liên kết với nhóm quảng cáo. ⏎ Quy tắc giá trị cho phép bạn ưu tiên và đặt giá thầu cao hơn cho một số loại khách hàng hoặc đối tượng dựa trên các điều kiện bạn xác định. |
| vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7). • `ZERO_DAY`: The current day (day 0). ⏎ Giá trị mặc định: `SEVEN_DAYS`. ⏎ • When the Minimum ROAS (Target ROAS) bidding strategy is used, this field represents the window type of the target ROAS value (Day 7 ROAS or Day 0 ROAS). The system will aim to keep your average ROAS of the seventh day or of the current day around or higher than the target ROAS value, regardless of your budget. • When the Highest Value bidding strategy is used, this field represents the Highest Value window type (Day 7 Highest Value or Day 0 Highest Value). The system will aim to spend your budget fully and maximize the value of results within the first seven days or within the current day. ⏎ **Note**:  • This setting, if specified, must be the same across all ad groups within the same campaign. • VBO IAP and VBO IAA in different scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. • Day 0 or day 7 bidding (`vbo_window` is `ZERO_DAY` or `SEVEN_DAYS`) for **VBO IAP** in Advanced Dedicated Campaign or Android campaign scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. • Day 0 or day 7 bidding (`vbo_window` is `ZERO_DAY` or `SEVEN_DAYS`) for **VBO IAA** in Advanced Dedicated Campaign or Android campaign scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. • Once set, this field cannot be updated. |
| click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Use this field to define the timeframe during which conversions can be attributed to the ad group. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click. • `FOURTEEN_DAYS`: 14-day click. • `TWENTY_EIGHT_DAYS`: 28-day click. • `THIRTY_DAYS`: 30-day click. • This value is only valid when `promotion_type` is `MINI_GAME`. • `THIRTY_TWO_DAYS`: 32-day click. •  This value is only valid when `promotion_type` is `MINI_APP` and `optimization_event` is `ACTIVE_PAY`. • `ONE_HUNDRED_EIGHTY_DAYS`: 180-day click. • This value is only valid when `promotion_type` is `MINI_APP` and `optimization_event` is `ACTIVE_PAY`. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**: • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. • If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). • Once set, this field cannot be updated. |
| engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Use this field to define the timeframe during which conversions can be attributed to the ad group. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • This value is only valid in [Upgraded Smart+ Ads with Website and App Optimization](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1854746404386113). • `TWENTY_EIGHT_DAYS`: 28-day engaged view. • This value is only valid in [Upgraded Smart+ Ads with Website and App Optimization](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1854746404386113). ⏎ Giá trị mặc định: `OFF`. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. • If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use the [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026) interface. • Once set, this field cannot be updated. |
| view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Use this field to define the timeframe during which conversions can be attributed to the ad group. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. • If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use[/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). • Once set, this field cannot be updated. |
| attribution_event_count | string | Event count (Statistic type). ⏎ The way that people\'s actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset. • `EVERY`: Every. To count multiple events from someone as separate conversions. • `ONCE`: Once. To count multiple events from someone as 1 conversion. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  • If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). • Once set, this field cannot be updated. |
| billing_event  ****(Bắt buộc)**** | string | Events that you want to pay for. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Billing Event](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ Currently, we only support `OCPM` and `CPC`: • When `optimization_goal` is `CLICK`, set this field to `CPC`. • When `optimization_goal` is not `CLICK`, set this field to `OCPM`. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting must be the same across all ad groups within the same campaign. |
| automated_keywords_enabled | boolean | Chỉ hợp lệ khi at the campaign level `is_search_campaign` is `true`. ⏎ Có thực hiện enable automated keywords and let the system find relevant keywords to expand reach and improve results. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ Enabling automated keywords is recommended as it complements your manually specified keywords by discovering new opportunities and targeting high-intent search queries that you might have missed. |
| search_keywords | object[] | • Required for Search Ads Campaigns (`is_search_campaign` is `true` at the campaign level). • Not supported for non-Search Ads Campaigns (`is_search_campaign` is `false` at the campaign level). ⏎ A list of search keywords, that is, words or phrases that are used to match your ads with the terms people are searching for. ⏎ Kích thước tối đa: 1,000. ⏎ To confirm Liệu an Upgraded Smart+ Campaign is a Search Ads Campaign, call [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930) and check the `is_search_campaign` returned for the campaign. ⏎ To learn more about how to create Search Ads Campaigns, see [Create Upgraded Smart+ Search Ads Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1873144295333889). |
| ↳ keyword | string | When `search_keywords` is specified, you need to provide at least one `keyword` and the corresponding `match_type`. ⏎ The search keyword. ⏎ Giới hạn độ dài: 80 characters. ⏎ The name needs to exclude emojis and the following special characters: `!` `#` `$` `%` `&` `(` `)` `*` `-` `/` `:` `;` `` `?` `@` `\` `^` `_` `¥` `……`. Otherwise, an error will occur. ⏎ To obtain the review result for search keywords, call [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026) and check the `audit_status` within the `search_keywords` object array. ⏎ **Important**: Search keywords must comply with TikTok's [Advertising Terms](https://ads.tiktok.com/help/article/advertising-on-tiktok-first-things-to-note) and Community Guidelines. • If all of your keywords are found to be non-compliant, your campaign will not be delivered. • If part of your search keywords are rejected, you need to remove the violative keywords or replace them with a suitable alternative by using [/smart_plus/adgroup/update/](62-upgraded-smartplus-p4.md#doc-1843314894279682). Your campaign will continue with the approved keywords. |
| ↳ match_type | string | When `search_keywords` is specified, you need to provide at least one `keyword` and the corresponding `match_type`. ⏎ The match type for the search keyword. ⏎ Các giá trị enum hỗ trợ: • `PRECISE_WORD`: exact match. Ads only show when a search includes the exact phrase or close variations, with additional words allowed before or after. • `PHRASE_WORD`: phrase match. Ads only show when a search exactly matches your keyword or a very close variation. • `BROAD_WORD`: broad match. Ads are shown for a wide range of relevant searches to offer the widest reach. |
| targeting_optimization_mode | string | Audience targeting optimization mode. ⏎ • `AUTOMATIC`: Automatic targeting. You can use automatic targeting to leverage real-time data and machine learning to target audiences most likely to engage with your ads.  • For an ad group that is not an Upgraded Smart+ Catalog Ad Group for App, when `targeting_optimization_mode` is `AUTOMATIC`, you can set `suggestion_audience_enabled` to `false` or `true`.  • When `targeting_optimization_mode` is `AUTOMATIC` and `suggestion_audience_enabled` is `false`, you can specify the following optional audience control settings:  • `location_ids` • `zipcode_ids` • `spc_audience_age` • `languages` • `operating_systems` • `excluded_audience_ids`  • When `targeting_optimization_mode` is `AUTOMATIC` and `suggestion_audience_enabled` is `true`, you can specify additional audience targeting settings as suggestions that guide automatic targeting. To learn more about the available settings, see the description of the parameter `suggestion_audience_enabled`.   • For an Upgraded Smart+ Catalog Ad Group for App (at the campaign level `sales_destination` is `APP`), when `targeting_optimization_mode` is `AUTOMATIC`, you can only set `suggestion_audience_enabled` to `false`.  • When `targeting_optimization_mode` is `AUTOMATIC` and `suggestion_audience_enabled` is `false` , you can specify the following optional audience control settings:  • `location_ids` • `zipcode_ids` • `spc_audience_age` • `languages` • `audience_ids` • `excluded_audience_ids` • `gender`   • `MANUAL`: Custom targeting. You can use custom targeting settings to precisely control who sees your ads. This may limit delivery and impact campaign performance.  • When `targeting_optimization_mode` is `MANUAL`, you can specify the following audience settings:  • `location_ids` • `zipcode_ids` • `age_groups` • `gender` • `languages` • `audience_ids` • `excluded_audience_ids` • `included_pangle_audience_package_ids` • `excluded_pangle_audience_package_ids` • `interest_category_ids` • `interest_keyword_ids` • `purchase_intention_keyword_ids` • `actions` • `smart_interest_behavior_enabled` • `smart_audience_enabled` • `spending_power` • `household_income` • `operating_systems` • `min_android_version` • `min_ios_version` • `device_model_ids` • `network_types` • `carrier_ids` • `isp_ids` • `device_price_ranges` • `saved_audience_id` ⏎ Giá trị mặc định: `AUTOMATIC`. ⏎ **Note**: If you specify targeting settings that don’t align with your targeting optimization mode settings (`targeting_optimization_mode` and `suggestion_audience_enabled`), those settings will be ignored, and no errors will occur. |
| suggestion_audience_enabled | boolean | Chỉ hợp lệ khi `targeting_optimization_mode` is `AUTOMATIC`. ⏎ Có thực hiện enable audience suggestions. ⏎ Audience suggestions guide automatic targeting by specifying additional audience settings. These serve as suggestions only, and delivery to those audiences is not guaranteed. ⏎ Các giá trị được hỗ trợ: `true` (recommended), `false`. ⏎ Giá trị mặc định: `false`. ⏎ When `suggestion_audience_enabled` is `true`, you can specify the following additional audience targeting settings: • `age_groups` • `gender` • `audience_ids` • `interest_category_ids` • `interest_keyword_ids` • `purchase_intention_keyword_ids` • `actions` ⏎ **Note**:  • If you specify targeting settings that don’t align with your targeting optimization mode settings (`targeting_optimization_mode` and `suggestion_audience_enabled`), those settings will be ignored, and no errors will occur. • You cannot set this field to `true` if Realtime API (RTA) is enabled at the campaign level. |
| targeting_spec  ****(Bắt buộc)**** | object | Targeting settings. ⏎ The targeting settings that you can specify vary based on the values for `targeting_optimization_mode` and `suggestion_audience_enabled`. To learn more about the available settings, see the descriptions of the two parameters. |
| ↳ app_targeting_type **(Điều kiện)** | string | Required and Chỉ hợp lệ khi the following conditions are all met: ⏎ • At the campaign level: • `objective_type` is `WEB_CONVERSIONS` • `sales_destination` is `APP`. • `optimization_goal` is `CLICK`, `IN_APP_EVENT`, or `VALUE`. ⏎ App targeting type. ⏎ Các giá trị enum hỗ trợ: • `PROSPECT`: Prospect. Find prospective customers, including those who have not interacted with your products. • `RETARGETING`: Retarget. Show ads to people who have already interacted with your business on and off TikTok. ⏎ **Note**: ⏎ • When `campaign_type` is `IOS14_CAMPAIGN` at the campaign level, you can only set this field to `PROSPECT`. • Once set, this field cannot be updated. |
| ↳ location_ids **(Điều kiện)** | string[] | • When `catalog_type` is `TRAVEL_ENTERTAINMENT` at the campaign level, you need to set `location_ids` or `zipcode_ids` or both. • When you create other types of Upgraded Smart+ Campaigns, `location_ids` is required. ⏎ IDs of the locations that you want to target. ⏎ To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) or [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. ⏎ To get the list of location IDs, see **Location IDs**. ⏎ **Note**: If you add the US as your target location, then you can not remove the US after campaign creation. |
| ↳ zipcode_ids **(Điều kiện)** | string[] | •  When `catalog_type` is `TRAVEL_ENTERTAINMENT` at the campaign level, you need to set `location_ids` or `zipcode_ids` or both. • When you create other types of Upgraded Smart+ Campaigns, `zipcode_ids` is not supported. ⏎ Zip code IDs or postal code IDs that you want to use to target locations. ⏎ Kích thước tối đa: 3,000. If you provide both `location_ids` and `zipcode_ids`, the combined total of location IDs, zip code IDs, and postal code IDs cannot exceed 3,000 per ad group. ⏎ You can get the available zip code IDs or postal code IDs based on your placement, objective and keyword via `geo_id` (when `geo_type` = `ZIP_CODE`) returned from the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) endpoint. ⏎ **Note**:  • Zip code targeting is currently only supported for the US and postal code targeting is currently only supported for Canada, Brazil, Indonesia, Thailand, and Vietnam. • Targeting postal code areas in Brazil, Indonesia, Thailand, and Vietnam is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • You cannot use zip code targeting or postal code targeting in campaigns that have enabled special ad categories (`special_industries`). • You cannot use zip code targeting or postal code targeting in campaigns with the `objective_type` as `RF_REACH`. • Overlapping targeted locations are not supported. For instance, you cannot target the US and the state of California at the same time. • If you target locations in the US via `location_ids` or `zipcode_ids` during ad group creation, you can subsequently update those IDs to other US locations but you cannot remove all US locations to target only non-US countries. • To get information about the zip code IDs or postal code IDs, you can only use [/tool/targeting/info/](70-tools-p1.md#doc-1761237001980929). |
| ↳ languages | string[] | Mã của các ngôn ngữ mà bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách mã ngôn ngữ được hỗ trợ, xem [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ operating_systems | string[] | Device operating systems that you want to target. ⏎ Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. ⏎ Only one value is allowed. ⏎ • When `promotion_type` is `APP_ANDROID`, this field will be ignored and default to `["ANDROID"]`. • When `promotion_type` is `APP_IOS`, this field will be ignored and default to `["IOS"]`. |
| ↳ spc_audience_age | string | The age group that the ad group targets. ⏎ Enum value: • `ALL`: all age groups. • `OVER_EIGHTEEN`: 18+. • `OVER_TWENTY_FIVE`: 25+. ⏎ Giá trị mặc định: `OVER_EIGHTEEN`. ⏎ **Note**:  • Targeting all age groups (`ALL`) is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • You can only use the value `ALL` when at the campaign level `smart_plus_adgroup_mode` is `MULTIPLE`. To check the `smart_plus_adgroup_mode` of a campaign, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). |
| ↳ excluded_audience_ids | string[] | Danh sách ID đối tượng cần loại trừ. ⏎ Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| ↳ age_groups | string[] | Age groups you want to target. ⏎ Các giá trị enum hỗ trợ: • `AGE_13_17`: 13-17. • `AGE_18_24`: 18-24. • `AGE_25_34`: 25-34. • `AGE_35_44`: 35-44. • `AGE_45_54`: 45-54. • `AGE_55_100`: 55+ ⏎ **Note**: You can only use the value `AGE_13_17` in the following scenario: • At the campaign level `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. |
| ↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`,`GENDER_MALE`,`GENDER_UNLIMITED`. |
| ↳ audience_ids | string[] | Danh sách ID đối tượng. ⏎ Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| ↳ shopping_ads_retargeting_type | string | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level: • `objective_type` is `WEB_CONVERSION` • `sales_destination` is `WEB_AND_APP`, `WEBSITE`, or `APP` • `catalog_type` is `ECOMMERCE` • At the ad group level: `targeting_optimization_mode` is `MANUAL`. ⏎ The retargeting type. ⏎ Các giá trị enum hỗ trợ: • `LAB1`: Retargeting audiences who viewed products or added products to cart but didn't purchase products. • `LAB2`: Retargeting audiences who added products to cart but didn't purchase products. • `LAB3`: Retargeting audiences using custom combination. • `OFF`: No retargeting. ⏎ Giá trị mặc định: `OFF`. |
| ↳ shopping_ads_retargeting_actions_days **(Điều kiện)** | number | Bắt buộc khi `shopping_ads_retargeting_type` is `LAB1` or `LAB2`. ⏎ The valid time range for the specified audience action. Audiences who have completed the specified action within the time range will be retargeted. ⏎ Value range: 1, 2, 3, 7, 14, 30, 60, 90, 180. |
| ↳ included_custom_actions**(Điều kiện)** | object[] | When `shopping_ads_retargeting_type` is `LAB3`, you need to specify either `included_custom_actions` or `excluded_custom_actions`. ⏎ Details of the catalog audience to include. ⏎ Catalog audience is based on people's interactions with specific products and often drives better performance than custom audience. |
| ↳↳ code | string | The custom action used to filter the audiences to be retargeted. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc các đối tượng đã hoàn thành hành động được chỉ định. ⏎ Khoảng giá trị: 1-180. |
| ↳ excluded_custom_actions**(Điều kiện)** | object[] | When `shopping_ads_retargeting_type` is `LAB3`, you need to specify either `included_custom_actions` or `excluded_custom_actions`. ⏎ Details of the catalog audience to exclude. ⏎ Improve ad performance by excluding products that people have already interacted with, ensuring they only see relevant ads from your brand. |
| ↳↳ code | string | The custom action used to filter out the audiences. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc loại trừ các đối tượng đã hoàn thành hành động được chỉ định. ⏎ Khoảng giá trị: 1-180. |
| ↳ shopping_ads_retargeting_custom_audience_relation | string | Chỉ hợp lệ khi the following conditions are both met: • `shopping_ads_retargeting_type` is set to `LAB1`, `LAB2`, or `LAB3`. • `audience_ids` is specified. ⏎ The logical relation between the retargeting audience specified by `shopping_ads_retargeting_type` and the custom audience specified by `audience_ids`. ⏎ Các giá trị enum hỗ trợ: • `OR`: To combine the retargeting audience and the custom audience to create the targeted audience. The ad group will target anyone in catalog or custom audiences. • `AND`: To intersect between the retargeting audience and the custom audience to create the targeted audience. The ad group will target individuals who belong to both the retargeting audience and the custom audience. ⏎ If this field is not set, the targeted audience will consist of individuals who belong to both the retargeting audience and the custom audience. ⏎ **Note**: Once set, this field cannot be updated to a null value. |
| ↳ included_pangle_audience_package_ids | string[] | Chỉ hợp lệ cho vị trí hiển thị Pangle. Không chỉ định trường này cho các vị trí khác. ⏎ Danh sách ID gói đối tượng Pangle bạn muốn bao gồm. |
| ↳ excluded_pangle_audience_package_ids | string[] | Chỉ hợp lệ cho vị trí hiển thị Pangle. Không chỉ định trường này cho các vị trí khác. ⏎ Danh sách ID gói đối tượng Pangle bạn muốn loại trừ. |
| ↳ interest_category_ids | string[] | Danh sách ID từ khóa sở thích chung bạn muốn dùng để nhắm mục tiêu đối tượng. |
| ↳ interest_keyword_ids | string[] | Danh sách ID danh mục sở thích bổ sung bạn muốn dùng để nhắm mục tiêu đối tượng. ⏎ Để tìm kiếm danh mục sở thích bổ sung, sử dụng [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (khuyến nghị) hoặc [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| ↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm bạn muốn dùng để nhắm mục tiêu đối tượng quan tâm đến việc mua hàng liên quan đến một danh mục nội dung. |
| ↳ actions | object[] | Danh sách các đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳↳ action_scene | string | The type of user behavior that you want to target. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_RELATED`: Video interactions. • `CREATOR_RELATED`: Creator interactions. • `HASHTAG_RELATED`: Hashtag interactions. |
| ↳↳ action_period | number | The time period to include behaviors from. ⏎ Các giá trị enum hỗ trợ: `0`, `7`, `15`. ⏎ If `action_scene` is `CREATOR_RELATED` or `HASHTAG_RELATED`, `0` will be used regardless of the value you specify. `0` means that there is no definite timeframe to select actions from. ⏎ **Note**: Currently, when creating an ad group with video interactions targeting (`action_scene`= `VIDEO_RELATED`) via **TikTok Ads Manager**, you cannot select the time period (`action_period`), and 15 days (`15`) will be used by default. However, when creating ad groups via **API**, `0`, `7`, or `15` can still be passed. |
| ↳↳ video_user_actions | string[] | Các tương tác cụ thể của người dùng bạn muốn nhắm mục tiêu cho loại hành vi tương ứng. • Nếu `action_scene` là `VIDEO_RELATED`, các giá trị được phép là: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`. • Nếu `action_scene` là `CREATOR_RELATED`, các giá trị được phép là: `FOLLOWING`, `VIEW_HOMEPAGE`. • Nếu `action_scene` là `HASHTAG_RELATED`, giá trị được phép là: `VIEW_HASHTAG`. |
| ↳↳ action_category_ids | string[] | Chỉ hợp lệ khi TikTok placement is the only placement selected. ⏎ IDs of the video interactions categories, creator interactions categories, hashtags, or hashtag bundles that you want to use to target audiences. ⏎ • To search for or list video interactions category IDs or creator interactions category IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/action_category/](70-tools-p1.md#doc-1737166752522241). • To get hashtag IDs or hashtag bundle IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/hashtag/recommend/](70-tools-p1.md#doc-1736271339521025). • To get recommended video interactions category IDs, creator interactions category IDs, hashtag IDs, or hashtag bundle IDs based on your industry, use [/tool/targeting_category/recommend/](70-tools-p1.md#doc-1736275204260866). |
| ↳ smart_interest_behavior_enabled | boolean | Có thực hiện turn on Smart interests & behaviors. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart interests & behaviors and how to turn on Smart interests & behaviors, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586) and [Enable Smart Targeting for your ad groups](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164826830849). |
| ↳ smart_audience_enabled | boolean | Có thực hiện turn on Smart audience. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart audience and how to turn on Smart audience, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586) and [Enable Smart Targeting for your ad groups](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164826830849). |
| ↳ spending_power | string | Spending power that you want to target. ⏎ Các giá trị enum hỗ trợ: `ALL`, `HIGH`. ⏎ If it is set to `HIGH`, you can target high spending users who typically spend more on purchases on TikTok ads than average users. |
| ↳ household_income | string[] | Household income that you want to target. ⏎ Các giá trị enum hỗ trợ: `TOP5`(Top 5% of ZIP codes), `TOP10`(Top 10% of ZIP codes), `TOP10_25`(Top 10% -25% of ZIP codes), `TOP25_50`(Top 25% - 50% of ZIP codes). |
| ↳ min_android_version | string | Minimum Android version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ min_ios_version | string | Audience minimum ios version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị. ⏎ Để lấy danh sách đầy đủ ID mẫu thiết bị và thương hiệu thiết bị, sử dụng endpoint [/tool/device_model/](70-tools-p1.md#doc-1736271001971713). |
| ↳ network_types | string[] | Network types that you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ carrier_ids | string[] | Carriers that you want to target. ⏎ The carriers must be consistent with the location(s) that you want to target. ⏎ To get the enum values, use [/tool/carrier/](70-tools-p1.md#doc-1737168013095938). A carrier is Chỉ hợp lệ khi the `in_use` field for the carrier is `true`. |
| ↳ isp_ids | string[] | Chỉ hợp lệ khi you specify a valid location ID at the country or region level via `location_ids` at the same time. ⏎ IDs of the Internet service providers (ISP) that you want to target. ⏎ You can use [/tool/targeting/list/](70-tools-p2.md#doc-1762962378261506) to get the ISP IDs that you can target for a location ID. ⏎ **Note**: When you pass in `isp_ids`, you cannot set the placement as Global App Bundle only (`placements` =`PLACEMENT_GLOBAL_APP_BUNDLE`). |
| ↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu. ⏎ Giá trị 10000 đại diện cho 1000+. Các số phải là bội số của 50. ⏎ **Quan trọng**: Giới hạn trên bạn đặt sẽ được cộng thêm 50 và số mới thu được sẽ được sử dụng làm giới hạn trên thực tế cho nhắm mục tiêu thiết bị. Giới hạn thực tế được hiển thị trong cài đặt nhóm quảng cáo trên Trình quản lý quảng cáo TikTok. Nếu bạn đặt và nhận khoảng giá [0, 250], điều đó thực tế có nghĩa là [0, 300]. |
| ↳ saved_audience_id | string | Valid when the following conditions are both met: • The category of Housing, Employment, or Credit (`specical_industries`) is NOT specified in your campaign. • TikTok placement is selected in your ad group (i.e., `placement_type` is set as `PLACEMENT_TYPE_AUTOMATIC` **or** `placement_type` is set as `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TIKTOK` is included in `placements`). ⏎ Saved Audience ID. ⏎ To obtain the list of Saved Audiences within your ad account, use [/dmp/saved_audience/list/](09-audience.md#doc-1780154619404290). ⏎ Before using this field, call [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754) to create a Saved Audience and get the Saved Audience ID in response. The ID tài khoản quảng cáo TikTok associated with your Saved Audience should be the same as the ID tài khoản quảng cáo TikTok in your ad group. Otherwise, an error will occur. ⏎ If you use `saved_audience_id` to create an ad group, we will return both the Saved Audience ID and the targeting options that are included within your Saved Audience in response. ⏎ See [Create a Saved Audience](../09-marketing-api/audience.md#doc-1780156510696449) to find out the detailed workflow and code examples. ⏎ **Note**:  • When creating a Saved Audience via [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754), you can specify various targeting options, including `gender`. However, be aware that if you are creating an ad group based on a Saved Audience, it’s essential to avoid setting both the `saved_audience_id` and targeting options (such as `gender`) defined within your Saved Audience at the same time. • In cases where the targeting settings in your Saved Audience conflict with those in your ad group, the settings from your Saved Audience will take precedence. As a result, the conflicting targeting options in your ad group will be ignored. • For example, if you create a Saved Audience where `gender` is set to `GENDER_FEMALE` and then use that Saved Audience to create an ad group while specifying `gender` as `GENDER_MALE`, the resulting ad group will adopt `GENDER_FEMALE` as the gender targeting configuration, reflecting what is set in the Saved Audience. • If the `saved_audience_id` was created with `age_groups` specified, the age restriction rules outlined in [New age restrictions for ads on TikTok](../15-appendix/phu-luc-p1.md#doc-1788755983247362) for different advertising objectives also apply. Make sure that the age targeting setting is allowed before you use the Saved Audience (`saved_audience_id` ) in the ad group. |
| ↳ blocked_pangle_app_ids | string[] | Danh sách ID ứng dụng Pangle bị chặn. ⏎ Bạn có thể lấy ID qua trường `app_package_id` trả về từ [/tool/pangle_app/block/get/](55-pangle.md#doc-1740039957181441). |
| budget_mode | string | •  Bắt buộc khi Campaign Budget Optimization (CBO) is disabled  (`budget_optimize_on` is `false`) at the campaign level. • Ignored when CBO is enabled  (`budget_optimize_on` is `true`) at the campaign level. ⏎ Ad group budget mode. ⏎ Các giá trị enum hỗ trợ: • `BUDGET_MODE_TOTAL`: Lifetime budget. • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily budget. It is the average daily budget over a week. Daily costs will not exceed 125% of the average daily budget. Weekly costs will not exceed the average daily budget * 7. ⏎ **Note**:  • This setting, if specified, must be the same across all ad groups within the same campaign. • If this field is set to `BUDGET_MODE_TOTAL`, then `schedule_type` must be `SCHEDULE_START_END`, which requires an end date (`schedule_end_time`). • When at the campaign level `budget_optimize_on` is `false` and `budget_mode` is `BUDGET_MODE_DAY`, you can only set this field to `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi the following conditions are all met:  • At the campaign level: `budget_optimize_on` is `false`.  • At the ad group level:  • When `objective_type` is `APP_PROMOTION`:  • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `optimization_goal` is `VALUE`. • `deep_bid_type` is `VO_MIN_ROAS`. • `vbo_window` is `ZERO_DAY`.  • When `objective_type` is `LEAD_GENERATION`: • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `bid_type` is`BID_TYPE_CUSTOM`. ⏎ The ad group budget strategy for custom ad group budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.   • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based  budget increase. ⏎ **Note**: Enabling Goal-based budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget | float | • Bắt buộc khi Campaign Budget Optimization (CBO) is disabled  (`budget_optimize_on` is `false`) at the campaign level. • Ignored when CBO is enabled  (`budget_optimize_on` is `true`) at the campaign level. ⏎ Fixed ad group budget or initial ad group budget. • When `budget_auto_adjust_strategy`  is `UNSET`, this field represents your fixed ad group budget. • When `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`, this field represents your initial ad group budget. To retrieve the current ad group budget, check the returned `current_budget`. ⏎ For how to configure budget settings, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). To directly see the daily budget value range for a currency, see [Currency-Daily budget value range](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| min_budget | float | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level: • `budget_optimize_on` is `true` • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • At the ad group level: • `bid_type` is `BID_TYPE_NO_BID` ⏎ Ad group minimum budget. ⏎ The system will aim to spend at least this amount, but it is not guaranteed. |
| schedule_type  ****(Bắt buộc)**** | string | Schedule type. ⏎ Các giá trị enum hỗ trợ: • `SCHEDULE_FROM_NOW`: To run the ad group continuously after the scheduled start time. • You can only set `schedule_type` to `SCHEDULE_FROM_NOW` in any of the following scenarios: • At the campaign level, `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`  • At the ad group level, `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • `SCHEDULE_START_END`: To run the ad group between the scheduled start time and end time. |
| schedule_start_time  ****(Bắt buộc)**** | string | Schedule start time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The start time can be up to 12 hours earlier than the current time, but cannot be later than `2028-01-01 00:00:00`. |
| schedule_end_time **(Điều kiện)** | string | Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`. ⏎ Schedule end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The end time cannot be later than `2038-01-01 00:00:00`. |
| movie_premiere_date | string | Hợp lệ khi thỏa mãn tất cả các điều kiện: • Ở cấp chiến dịch: `objective_type` là `WEB_CONVERSIONS`, `sales_destination` là `WEBSITE`. • Ở cấp nhóm quảng cáo: `optimization_goal` là `CONVERT`, `CLICK` hoặc `TRAFFIC_LANDING_PAGE_VIEW`. ⏎ Ngày công chiếu tại rạp, theo định dạng `YYYY-MM-DD` (UTC+0). ⏎ Cung cấp ngày công chiếu cho phép hệ thống tích hợp mốc thời gian này để tối ưu hóa hiệu suất. |
| dayparting | string | Phân bổ thời gian phân phối quảng cáo theo khung giờ, định dạng chuỗi gồm 48 x 7 ký tự. ⏎ Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Ký tự đầu tiên tương ứng 0:01-0:30 Thứ Hai; ký tự cuối cùng tương ứng 23:31-0:00 Chủ Nhật. ⏎ **Lưu ý**: Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian. |
| is_hfss | boolean | Chỉ hợp lệ khi `targeting_optimization_mode` is `MANUAL`. ⏎ Liệu promoted content is HFSS (High Fat, Salt, Sugar) Product/Brand. ⏎ If your ad is promoting or prominently featuring a product/brand classed as high in fat, salt or sugar, set this field to `true`. ⏎ In regulated regions, HFSS ads must only be targeted to users aged 18 or over. ⏎ You can set this field to `true`when your targeting locations include locations in the UK, Australia, New Zealand, and the European Union. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| is_lhf_compliance **(Điều kiện)** | boolean | When the targeting locations include locations in the UK and `is_hfss` is `true`, this field is required and must be set to `true`. ⏎ Liệu promoted content complies with LHF (Less Healthy Foods) regulations. ⏎ By setting `is_lhf_compliance` to `true`, you confirm that any food or drink products you advertise on TikTok in the UK comply with the [2024 Less Healthy Foods Regulations](https://www.legislation.gov.uk/uksi/2024/1266/made) and all other applicable laws. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| placement_type | string | The placement strategy that decides where your ads will be shown. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TYPE_AUTOMATIC`: Automatic Placement. TikTok's ad system will use smart calculations to give you the best combination of ad placements across all apps. • `PLACEMENT_TYPE_NORMAL`: Select Placement. By selecting your placement manually, you\'ll be able to choose the apps to deliver your ads on. ⏎ By default, the system will automatically configure placements for your Upgraded Smart+ Campaigns based on your other settings and select high-quality traffic from various placements to deliver better results. ⏎ However, in cases where only Select Placement is supported, omitting the placement parameters (`placement_type` and `placements`) might trigger a placement error. In such cases, you need to manually set `placement_type` to `PLACEMENT_TYPE_NORMAL` and specify `placements`. ⏎ **Note**: • `placement_type` cannot be updated after the ad group has been created. • If you set this field to `PLACEMENT_TYPE_AUTOMATIC`, the actual supported placements will be shown in the returned `placements`. For instance, if the actual supported placement is TikTok only, the returned `placements` value will be `PLACEMENT_TIKTOK`. |
| placements **(Điều kiện)** | string[] | •  When `placement_type` is `PLACEMENT_TYPE_NORMAL`, this field is required. • When `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`, this field is ignored and overwritten to the combination of ad placements that the TikTok ad system selects for your ad. ⏎ The apps where you want to deliver your ads. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TIKTOK`: TikTok. • `PLACEMENT_PANGLE`: Pangle. • `PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle. ⏎ **Note**: • `placements` cannot be updated after the ad group has been created. • The available locations you can target with the Global App Bundle placement (`PLACEMENT_GLOBAL_APP_BUNDLE`) are: Brazil, Indonesia, Vietnam, the Philippines, Thailand, Malaysia, Mexico, Saudi Arabia, and Japan. • The Global App Bundle placement (`PLACEMENT_GLOBAL_APP_BUNDLE`) does not support the optimization goal Landing Page View (`optimization_goal`=`TRAFFIC_LANDING_PAGE_VIEW`). To learn about the optimization goal, refer to the section [Enumerations-Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| tiktok_subplacements | string[] | Chỉ hợp lệ khi the following conditions are met: • At the campaign level: `objective_type` is `APP_PROMOTION`, `LEAD_GENERATION`, or `WEB_CONVERSIONS`. • At the ad group level: `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`. ⏎ The subplacements within TikTok for your ads, allowing you to choose where your ads will appear. ⏎ Các giá trị enum hỗ trợ: • `LEMON8`: Lemon8, a community app for lifestyle content, focusing on real-life experiences, tips, guides, and product reviews. By including Lemon8 as a subplacement, your ads will appear in its For You feed, Search feed, and Immersive Video feed. [Learn more about Lemon8 for Performance Auction](https://ads.tiktok.com/help/article/about-lemon8-in-tiktok-ads-manager). • `PINE_DRAMA`: PineDrama, an app for watching short-form dramas. Ads will be placed on recommendation pages, within episode streams, and more. [Learn more about PineDrama for Performance Auction](https://ads.tiktok.com/help/article/about-pinedrama-for-performance-auction-in-tiktok-ads-manager). ⏎ **Note**:  • Using the Lemon8 subplacement (`LEMON8`) in your ad group is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • The Lemon8 subplacement (`LEMON8`) is not supported when `rta_id` is specified at the campaign level. • If you want to use the Lemon8 subplacement (`LEMON8`) in Lead Generation campaigns (with `objective_type` as `LEAD_GENERATION` at the campaign level), ensure that at the ad group level `promotion_type` is `LEAD_GENERATION`. • Using the PineDrama subplacement (`PINE_DRAMA`) in your ad group is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When you use the PineDrama subplacement, the regions you can target include Brazil, Indonesia, Mexico, Thailand, the United States, and Vietnam. • Once set, this field cannot be updated. |
| comment_disabled | boolean | Có thực hiện allow comments on your campaigns on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| share_disabled | boolean | Có thực hiện disable sharing of the campaign to third-party platforms. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| video_download_disabled | boolean | Liệu users can download your video ads on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |

### Ví dụ lệnh cURL (Example)
#### Nhắm mục tiêu tự động không kèm gợi ý đối tượng
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/create/' \
--header 'Access-Token: "{{Access-Token}}" ' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "request_id": "{{request_id}}",
    "adgroup_name": "{{adgroup_name}}",
    "app_id": "{{app_id}}",
    "promotion_type": "APP_ANDROID",
    "optimization_goal": "INSTALL",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "targeting_optimization_mode": "AUTOMATIC",
    "targeting_spec": {
        "location_ids": [
            "1562822"
        ],
        "spc_audience_age": "OVER_EIGHTEEN",
        "operating_systems": [
            "ANDROID"
        ]
    }
}'
```

#### Nhắm mục tiêu tự động kèm gợi ý đối tượng
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/create/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "request_id": "{{request_id}}",
    "adgroup_name": "{{adgroup_name}}",
    "app_id": "{{app_id}}",
    "promotion_type": "APP_ANDROID",
    "optimization_goal": "INSTALL",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "targeting_optimization_mode": "AUTOMATIC",
    "suggestion_audience_enabled": true,
    "targeting_spec": {
        "location_ids": [
            "1562822"
        ],
        "spc_audience_age": "OVER_EIGHTEEN",
        "operating_systems": [
            "ANDROID"
        ],
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "gender": "GENDER_UNLIMITED",
        "audience_ids": [
            "{{audience_id}}",
            "{{audience_id}}",
            "{{audience_id}}",
            "{{audience_id}}"
        ],
        "interest_category_ids": [
            "17",
            "10"
        ],
        "purchase_intention_keyword_ids": [
            "14",
            "17"
        ],
        "actions": [
            {
                "action_scene": "VIDEO_RELATED",
                "action_period": 15,
                "video_user_actions": [
                    "WATCHED_TO_END",
                    "LIKED",
                    "COMMENTED",
                    "SHARED"
                ],
                "action_category_ids": [
                    "13",
                    "15"
                ]
            },
            {
                "action_scene": "CREATOR_RELATED",
                "action_period": 0,
                "video_user_actions": [
                    "FOLLOWING",
                    "VIEW_HOMEPAGE"
                ],
                "action_category_ids": [
                    "8",
                    "10"
                ]
            },
            {
                "action_scene": "HASHTAG_RELATED",
                "action_period": 0,
                "video_user_actions": [
                    "VIEW_HASHTAG"
                ],
                "action_category_ids": [
                    "8",
                    "5"
                ]
            }
        ]
    }
}'
```

#### Custom targeting
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/create/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "request_id": "{{request_id}}",
    "adgroup_name": "{{adgroup_name}}",
    "app_id": "{{app_id}}",
    "promotion_type": "APP_ANDROID",
    "optimization_goal": "INSTALL",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "targeting_optimization_mode": "MANUAL",
    "targeting_spec": {
        "location_ids": [
            "1562822"
        ],
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "gender": "GENDER_UNLIMITED",
        "audience_ids": [
            "{{audience_id}}",
            "{{audience_id}}",
            "{{audience_id}}",
            "{{audience_id}}"
        ],
        "interest_category_ids": [
            "17",
            "10"
        ],
        "purchase_intention_keyword_ids": [
            "14",
            "17"
        ],
        "actions": [
            {
                "action_scene": "VIDEO_RELATED",
                "action_period": 15,
                "video_user_actions": [
                    "WATCHED_TO_END",
                    "LIKED",
                    "COMMENTED",
                    "SHARED"
                ],
                "action_category_ids": [
                    "13",
                    "15"
                ]
            },
            {
                "action_scene": "CREATOR_RELATED",
                "action_period": 0,
                "video_user_actions": [
                    "FOLLOWING",
                    "VIEW_HOMEPAGE"
                ],
                "action_category_ids": [
                    "8",
                    "10"
                ]
            },
            {
                "action_scene": "HASHTAG_RELATED",
                "action_period": 0,
                "video_user_actions": [
                    "VIEW_HASHTAG"
                ],
                "action_category_ids": [
                    "8",
                    "5"
                ]
            }
        ],
        "smart_interest_behavior_enabled": false,
        "smart_audience_enabled": true,
        "spending_power": "HIGH",
        "operating_systems": [
            "ANDROID"
        ]
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳ campaign_name | string | Tên của chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad group is enabled (in 'ON' status). • `DISABLE`: The ad group is disabled (in 'OFF' status). |
| ↳ secondary_status | string | Ad group secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Ad group Status - Secondary Status](https://business-api.tiktok.com/portal/docs/enumerations-appendix/v1.3#anchor-2-2). |
| ↳ catalog_id | string | Được trả về khi `catalog_enabled` là `true` ở cấp chiến dịch. ⏎ ID danh mục sản phẩm được sử dụng trong nhóm quảng cáo. |
| ↳ catalog_authorized_bc_id | string | Được trả về khi `catalog_enabled` là `true` ở cấp chiến dịch. ⏎ ID của Trung tâm doanh nghiệp (Business Center) sở hữu danh mục sản phẩm (`catalog_id`). |
| ↳ product_source | string | Nguồn sản phẩm bạn muốn lấy để quảng bá. ⏎ Giá trị enum: `CATALOG` (danh mục). |
| ↳ promotion_type | string | Loại quảng bá (Vị trí tối ưu hóa). Bạn có thể quyết định nơi muốn quảng bá sản phẩm bằng trường này. ⏎ Hiện tại hỗ trợ: `APP_ANDROID`, `APP_IOS`, `WEBSITE`, `MINI_GAME`, `NATIVE_SERIES`, `LEAD_GENERATION` và `LEAD_GENERATION_MULTI_DESTINATION`. • Khi `objective_type` là `APP_PROMOTION` và `app_promotion_type` là `APP_INSTAL`, trường này sẽ là `APP_ANDROID` hoặc `APP_IOS`. • Khi `objective_type` là `APP_PROMOTION` và `app_promotion_type` là `MINIS`, trường này sẽ là `MINI_APP`, `MINI_GAME` hoặc `NATIVE_SERIES`. • Khi `objective_type` là `WEB_CONVERSIONS`: • Nếu `sales_destination` là `WEBSITE`, trường này sẽ là `WEBSITE`. • Nếu `sales_destination` là `APP`, trường này sẽ là `APP_ANDROID` hoặc `APP_IOS`. • Khi `objective_type` là `LEAD_GENERATION`, trường này sẽ là một trong các giá trị: • `LEAD_GENERATION` • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` • `LEAD_GEN_CLICK_TO_CALL` • `LEAD_GENERATION_MULTI_DESTINATION`. |
| ↳ optimization_locations | object[] | Được trả về khi `promotion_type` là `LEAD_GENERATION_MULTI_DESTINATION`. ⏎ Danh sách các vị trí tối ưu hóa cho nhóm quảng cáo Tìm kiếm khách hàng tiềm năng. ⏎ Để tìm hiểu loại quảng cáo có thể sử dụng trường này, xem [Tạo chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng nâng cấp với nhiều vị trí đích](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳↳ promotion_type | string | Promotion type (Optimization location). ⏎ You can decide where you want audiences to convert or complete an action. ⏎ Các giá trị enum hỗ trợ: `LEAD_GENRATION`, `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`. |
| ↳↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳↳ optimization_event | string | Optimization event. ⏎ Các giá trị enum hỗ trợ: • `ON_WEB_REGISTER`: Complete registration. • `CONSULT`: Contact. • `FORM`: Submit form. • `ON_WEB_SUBSCRIBE`: Subscribe. |
| ↳ promotion_website_type | string | Loại trang tức thì TikTok. ⏎ Hiện tại chỉ hỗ trợ `TIKTOK_NATIVE_PAGE` (Sử dụng Trang tức thì TikTok). |
| ↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳ gaming_ad_compliance_agreement | string | Returned only in any of the following scenarios: • Scenario 1: When the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • Scenario 2: When the following conditions are all met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `REGULAR_CAMPAIGN`. ⏎ Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳ pixel_id | string | ID TikTok Pixel. |
| ↳ app_config | object[] | Được trả về khi `sales_destination` là `WEB_AND_APP`. ⏎ Chi tiết về ứng dụng hoặc các ứng dụng cần quảng bá. |
| ↳↳ app_id | string | App ID của ứng dụng cần quảng bá. |
| ↳ minis_id | string | Được trả về khi `promotion_type` là `MINI_APP` hoặc `MINI_GAME`. ⏎ ID của TikTok Mini. |
| ↳ optimization_event | string | Sự kiện chuyển đổi cho nhóm quảng cáo. ⏎ Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) để biết thêm. ⏎ **Note**: If you enable Value-Based Optimization during ad group creation by setting your `optimization_event` to either `IMPRESSION_LEVEL_AD_REVENUE` or `AD_REVENUE_VALUE`(note that both enums are equivalent and have the exact same effect), you will always receive `IMPRESSION_LEVEL_AD_REVENUE` as the `optimization_event` in the response. |
| ↳ custom_conversion_id | string | ID của Chuyển đổi tùy chỉnh (Custom Conversion) được sử dụng trong nhóm quảng cáo. |
| ↳ deep_funnel_optimization_status | string | With deep funnel optimization, you can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: enabled. • `OFF`: disabled. |
| ↳ deep_funnel_event_source | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel. • `OFFLINE`: Offline Event Set. • `CRM`: CRM Event Set. |
| ↳ deep_funnel_event_source_id | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ ID nguồn sự kiện. • Khi `deep_funnel_event_source` là `PIXEL`, trường này đại diện cho ID TikTok Pixel. • Khi `deep_funnel_event_source` là `OFFLINE`, trường này đại diện cho ID bộ sự kiện ngoại tuyến. • Khi `deep_funnel_event_source` là `CRM`, trường này đại diện cho ID bộ sự kiện CRM. |
| ↳ deep_funnel_optimization_event | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ Sự kiện tối ưu hóa phễu sâu. ⏎ Ví dụ: `SHOPPING`. |
| ↳ app_attribution_source | string | Attribution source for your app. ⏎ The attribution source you choose will be used for optimization, bidding, and reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP (mobile measurement partner) attribution. Signals from your selected MMP will be used for attribution. • `SAN`: SAN (self-attribution network) attribution. Signals from TikTok SAN will be used for attribution. |
| ↳ app_data_source | string | Data source for your app. ⏎ The attribution signals you select will be used for reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP signals. Signals from your MMP will be used for reporting. • `EVENT_SDK`: App Events SDK signals. Signals from TikTok App Events SDK will be used for reporting. • `EVENT_API`: Events API signals. Signals from TikTok Events API will be used for reporting. |
| ↳ identity_id | string | Chỉ được trả về trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ ID danh tính (Identity ID). |
| ↳ identity_type | string | Returned only  in any of the following scenarios:  • Scenario 1: When `promotion_type` is `NATIVE_SERIES`. • Scenario 2: When `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` and your ad account is allowlisted for selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads. ⏎ Identity type. ⏎ Các giá trị enum hỗ trợ: • `TT_USER` : TikTok Business Account User. • `BC_AUTH_TT`: The TikTok account that a Business Center is authorized to access. ⏎ See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| ↳ identity_authorized_bc_id | string | Được trả về khi `identity_type` là `BC_AUTH_TT`. ⏎ ID của Trung tâm doanh nghiệp (Business Center) liên kết với danh tính người dùng tài khoản TikTok trong Business Center. |
| ↳ native_series_id | string | ID của TikTok Series. ⏎ Series cung cấp các gói video độc quyền và cao cấp do các nhà sáng tạo nội dung sản xuất. Quyền truy cập Series có thể được mua qua hồ sơ của nhà sáng tạo và các liên kết gắn kèm trên video TikTok. |
| ↳ messaging_app_type | string | The type of instant messaging app or customized URL to use in the Instant Messaging Ad Group. ⏎ Các giá trị enum hỗ trợ: • `MESSENGER`: Messenger.  • `WHATSAPP`: WhatsApp.  • `ZALO`: Zalo.  • `LINE`: Line.  • `IM_URL`: Instant Messaging URL. ⏎ To learn more about how to create Upgraded Smart+ TikTok Instant Messaging Ads, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302988449921). |
| ↳ zalo_id_type | string | The type of Zalo contact format. ⏎ Các giá trị enum hỗ trợ: • `ZALO_OFFICIAL_ACCOUNT`: Zalo Official Account ID.  • `ZALO_PHONE_ACCOUNT`: Zalo phone number. |
| ↳ messaging_app_account_id | string | ID tài khoản ứng dụng nhắn tin tức thì. • Khi `messaging_app_type` là `MESSENGER`, trường này đại diện cho Facebook Page ID. • Khi `messaging_app_type` là `LINE`, trường này đại diện cho LINE Business ID. • Khi `zalo_id_type` là `ZALO_OFFICIAL_ACCOUNT`, trường này đại diện cho ID Zalo Official Account. • Khi `messaging_app_type` là `WHATSAPP` hoặc khi `zalo_id_type` là `ZALO_PHONE_ACCOUNT`, trường này đại diện cho số điện thoại WhatsApp hoặc Zalo được tự động điền dựa trên `phone_info` đã chỉ định. |
| ↳ message_event_set_id | string | ID của bộ sự kiện tin nhắn dùng trong Nhóm quảng cáo Tin nhắn tức thì. ⏎ Nếu tài khoản ứng dụng tin nhắn (tài khoản Messenger hoặc Zalo Official Account chỉ định qua `messaging_app_account_id`, hoặc số điện thoại WhatsApp/Zalo từ `phone_info`) khớp với bộ sự kiện hiện có, trường này sẽ được **tự động điền** bộ sự kiện tin nhắn duy nhất tương ứng. |
| ↳ phone_info | object | Chi tiết số điện thoại WhatsApp hoặc Zalo. |
| ↳↳ phone_region_code | string | Mã vùng quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `US`. |
| ↳↳ phone_region_calling_code | string | Mã quay số quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `+1`. |
| ↳↳ phone_number | string | Số điện thoại WhatsApp hoặc Zalo. |
| ↳ bid_type | string | Chiến lược giá thầu. ⏎ Để xem các giá trị enum và mô tả, xem [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ bid_price | float | Chi phí mục tiêu trên mỗi lượt nhấp. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |
| ↳ conversion_bid_price | float | Chi phí mục tiêu trên mỗi chuyển đổi hoặc chi phí trên mỗi lượt xem trang đích. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |
| ↳ deep_bid_type | string | Chiến lược đặt giá thầu cho sự kiện trong ứng dụng. ⏎ Để xem các giá trị enum và mô tả, xem [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | ROAS mục tiêu cho Tối ưu hóa theo giá trị (Value-Based Optimization). |
| ↳ value_rule_set_id | string | ID của bộ quy tắc giá trị liên kết với nhóm quảng cáo. |
| ↳ incentive_offer_type | string | The type of incentive offer applicable to the Upgraded Smart+ Ad Group. ⏎ If your ad group meets the eligibility criteria and exceeds certain CPA or Minimum ROAS/Target ROAS thresholds, you will be incentivized with ad credits to use within the same ad account. ⏎ To learn more about the incentive offer eligibility criteria and the calculation of incentive amount, see [Smart+ Platform Incentive Offer (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: The ad group is ineligible for any incentive offer. • `COST_CAP_AND_MIN_ROAS`: The ad group uses the Cost Cap or Minimum ROAS/Target ROAS bidding strategy and is eligible for the incentive offer. ⏎ • To check the bid protection (incentive offer) eligibility for a list of Upgraded Smart+ Campaigns or Upgraded Smart+ Ad Groups, use [/report/bid_protection/status/get/](70-tools-p2.md#doc-1874392512912449). • To retrieve the bid protection history and ad credit from the past 60 days for a list of Upgraded Smart+ Campaigns or Upgraded Smart+ Ad Groups, use [/report/bid_protection/detail/get/](70-tools-p3.md#doc-1874392516418561). |
| ↳ vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7). • `ZERO_DAY`: The current day (day 0). |
| ↳ click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click. • `FOURTEEN_DAYS`: 14-day click. • `TWENTY_EIGHT_DAYS`: 28-day click. • `THIRTY_DAYS`: 30-day click. • `THIRTY_TWO_DAYS`: 32-day click. • `ONE_HUNDRED_EIGHTY_DAYS`: 180-day click. |
| ↳ engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Các giá trị enum hỗ trợ: • `OFF`: off. • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. |
| ↳ view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. |
| ↳ attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset. • `EVERY`: Every. To count multiple events from someone as separate conversions. • `ONCE`: Once. To count multiple events from someone as 1 conversion. |
| ↳ billing_event | string | Billing event. ⏎ Để xem danh sách giá trị enum, xem [Enumerations - Billing event](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ pacing | string | Delivery type. Your choice of ad delivery type determines the speed at which your daily budget is used. ⏎ Các giá trị enum hỗ trợ: • `PACING_MODE_SMOOTH`: Standard. Your budget will be used as evenly as possible depending on market demand and peaktime rates. This delivery type is suitable for advertisers who prefer steady spending. |
| ↳ automated_keywords_enabled | boolean | Có thực hiện enable automated keywords and let the system find relevant keywords to expand reach and improve results. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ search_keywords | object[] | Chỉ trả về cho Chiến dịch Quảng cáo Tìm kiếm. ⏎ Danh sách các từ khóa tìm kiếm dùng để so khớp quảng cáo với các cụm từ người dùng đang tìm kiếm. |
| ↳↳ keyword | string | Từ khóa tìm kiếm. |
| ↳↳ match_type | string | The match type for the search keyword. ⏎ Các giá trị enum hỗ trợ: • `PRECISE_WORD`: exact match. Ads only show when a search includes the exact phrase or close variations, with additional words allowed before or after. • `PHRASE_WORD`: phrase match. Ads only show when a search exactly matches your keyword or a very close variation. • `BROAD_WORD`: broad match. Ads are shown for a wide range of relevant searches to offer the widest reach. |
| ↳↳ audit_status | string | The review status of the search keyword. ⏎ Các giá trị enum hỗ trợ: • `AUDITING`: The keyword is under review. • `PASS`: The keyword has passed review and can be delivered. • `REJECTED`: The keyword failed to pass the review and cannot be delivered. |
| ↳↳ reject_info | object[] | Chỉ trả về khi `audit_status` là `REJECTED`. ⏎ Chi tiết về lý do từ chối. |
| ↳↳↳ forbidden_location | string | The targeted region that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ reject_reasons | object[] | Danh sách các lý do từ chối. |
| ↳↳↳↳ reason | string | Lý do từ chối. |
| ↳ budget_mode | string | Ad group budget mode. ⏎ Các giá trị enum hỗ trợ: • `BUDGET_MODE_TOTAL`: Lifetime budget. • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily budget. It is the average daily budget over a week. Daily costs will not exceed 125% of the average daily budget. Weekly costs will not exceed the average daily budget * 7. |
| ↳ budget_auto_adjust_strategy | string | Returned only when the following conditions are both met: • At the campaign level: `budget_optimize_on` is `false`. • At the ad group level: `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The ad group budget strategy for custom ad group budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. |
| ↳ budget | float | Ngân sách cố định hoặc ngân sách ban đầu của nhóm quảng cáo. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. |
| ↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách hiện tại của nhóm quảng cáo đã bật tự động tăng ngân sách theo mục tiêu. |
| ↳ min_budget | float | Ngân sách tối thiểu của nhóm quảng cáo. ⏎ Hệ thống sẽ cố gắng chi tiêu ít nhất số tiền này nhưng không đảm bảo tuyệt đối. |
| ↳ schedule_type | string | Schedule type. ⏎ Các giá trị enum hỗ trợ: • `SCHEDULE_FROM_NOW`: To run the ad group continuously after the scheduled start time. • `SCHEDULE_START_END`: To run the ad group between the scheduled start time and end time. |
| ↳ schedule_start_time | string | Thời gian bắt đầu phân phối nhóm quảng cáo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ schedule_end_time | string | Thời gian kết thúc phân phối nhóm quảng cáo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ movie_premiere_date | string | Ngày công chiếu tại rạp, theo định dạng `YYYY-MM-DD` (UTC+0). ⏎ Cung cấp ngày công chiếu giúp hệ thống tích hợp mốc thời gian này để tối ưu hóa hiệu suất. |
| ↳ dayparting | string | Phân bổ thời gian phân phối quảng cáo theo khung giờ, định dạng chuỗi gồm 48 x 7 ký tự. ⏎ Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Ký tự đầu tiên tương ứng 0:01-0:30 Thứ Hai; ký tự cuối cùng tương ứng 23:31-0:00 Chủ Nhật. ⏎ **Lưu ý**: Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian. |
| ↳ targeting_optimization_mode | string | Chế độ tối ưu hóa nhắm mục tiêu đối tượng. • `MANUAL`: Nhắm mục tiêu tùy chỉnh. Bạn có thể sử dụng cài đặt tùy chỉnh để kiểm soát chính xác ai nhìn thấy quảng cáo. Điều này có thể hạn chế phân phối và ảnh hưởng hiệu suất. • `AUTOMATIC`: Nhắm mục tiêu tự động. Sử dụng dữ liệu thời gian thực và máy học để tiếp cận đối tượng có khả năng tương tác cao nhất. |
| ↳ suggestion_audience_enabled | boolean | Có thực hiện enable audience suggestions. ⏎ Audience suggestions guide automatic targeting by choosing additional audience settings. These serve as suggestions only, and delivery to those audiences is not guaranteed. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ targeting_spec | object | Thiết lập nhắm mục tiêu. |
| ↳↳ app_targeting_type | string | Returned only when the following conditions are all met: • At the campaign level: • `objective_type` is `WEB_CONVERSIONS` • `sales_destination` is `APP`. • `optimization_goal` is `CLICK`, `IN_APP_EVENT`, or `VALUE`. ⏎ App targeting type. ⏎ Các giá trị enum hỗ trợ: • `PROSPECT`: Prospecting. Find prospective customers, including those who have not interacted with your products. • `RETARGETING`: Retargeting. Show ads to people who have already interacted with your business on and off TikTok. |
| ↳↳ location_ids | string[] | Danh sách ID vị trí bạn muốn nhắm mục tiêu. |
| ↳↳ zipcode_ids | string[] | ID mã bưu chính (zip code / postal code) của các vị trí được nhắm mục tiêu. |
| ↳↳ spc_audience_age | string | The age group that the ad group targets. ⏎ Các giá trị enum hỗ trợ: • `ALL`: all age groups. • `OVER_EIGHTEEN`: 18+. • `OVER_TWENTY_FIVE`: 25+. |
| ↳↳ languages | string[] | Mã ngôn ngữ bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách mã ngôn ngữ được hỗ trợ, xem [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ operating_systems | string[] | Device operating systems that you want to target. ⏎ Các giá trị enum hỗ trợ: `ANDROID`, `IOS` |
| ↳↳ excluded_audience_ids | string[] | Danh sách ID đối tượng cần loại trừ. |
| ↳↳ age_groups | string[] | Age groups you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳↳ audience_ids | string[] | Danh sách ID đối tượng. |
| ↳↳ shopping_ads_retargeting_type | string | The retargeting type. ⏎ Các giá trị enum hỗ trợ: • `LAB1`: Retargeting audiences who viewed products or added products to cart but didn't purchase products. • `LAB2`: Retargeting audiences who added products to cart but didn't purchase products. • `LAB3`: Retargeting audiences using custom combination. • `OFF`: No retargeting. |
| ↳↳ shopping_ads_retargeting_actions_days | number | Được trả về khi `shopping_ads_retargeting_type` là `LAB1` hoặc `LAB2`. ⏎ Khoảng thời gian hợp lệ cho hành động đối tượng đã chỉ định. Đối tượng hoàn thành hành động trong khoảng thời gian này sẽ được nhắm mục tiêu lại. |
| ↳↳ included_custom_actions | object[] | Chi tiết về đối tượng danh mục (catalog audience) cần bao gồm. ⏎ Đối tượng danh mục dựa trên tương tác của người dùng với sản phẩm cụ thể và thường mang lại hiệu suất tốt hơn đối tượng tùy chỉnh. |
| ↳↳↳ code | string | The custom action used to filter the audiences to be retargeted. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc các đối tượng đã hoàn thành hành động được chỉ định. |
| ↳↳ excluded_custom_actions | object[] | Chi tiết về đối tượng danh mục cần loại trừ. ⏎ Cải thiện hiệu suất quảng cáo bằng cách loại trừ các sản phẩm mà người dùng đã tương tác, đảm bảo họ chỉ thấy các quảng cáo phù hợp nhất từ thương hiệu của bạn. |
| ↳↳↳ code | string | The custom action used to filter out the audiences. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc loại trừ các đối tượng đã hoàn thành hành động được chỉ định. |
| ↳↳ shopping_ads_retargeting_custom_audience_relation | string | The logical relation between the retargeting audience specified by `shopping_ads_retargeting_type` and the custom audience specified by `audience_ids`. ⏎ Các giá trị enum hỗ trợ: • `OR`: To combine the retargeting audience and the custom audience to create the targeted audience. The ad group will target anyone in catalog or custom audiences. • `AND`: To intersect between the retargeting audience and the custom audience to create the targeted audience. The ad group will target individuals who belong to both the retargeting audience and the custom audience. |
| ↳↳ included_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle mà bạn muốn bao gồm. |
| ↳↳ excluded_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle mà bạn muốn loại trừ. |
| ↳↳ interest_category_ids | string[] | Danh sách ID từ khóa sở thích chung bạn muốn dùng để nhắm mục tiêu đối tượng. |
| ↳↳ interest_keyword_ids | string[] | Danh sách ID danh mục sở thích bổ sung bạn muốn dùng để nhắm mục tiêu đối tượng. ⏎ Để tìm kiếm danh mục sở thích bổ sung, sử dụng [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (khuyến nghị) hoặc [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| ↳↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm bạn muốn dùng để nhắm mục tiêu đối tượng quan tâm đến việc mua hàng liên quan đến một danh mục nội dung. |
| ↳↳ actions | object[] | Danh sách các đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳↳↳ action_scene | string | The type of user behavior that you want to target. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_RELATED`: Video interactions. • `CREATOR_RELATED`: Creator interactions. • `HASHTAG_RELATED`: Hashtag interactions. |
| ↳↳↳ action_period | number | Khoảng thời gian thu thập hành vi. |
| ↳↳↳ video_user_actions | string[] | Các tương tác cụ thể của người dùng bạn muốn nhắm mục tiêu cho loại hành vi tương ứng. • Nếu `action_scene` là `VIDEO_RELATED`, các giá trị được phép là: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`. • Nếu `action_scene` là `CREATOR_RELATED`, các giá trị được phép là: `FOLLOWING`, `VIEW_HOMEPAGE`. • Nếu `action_scene` là `HASHTAG_RELATED`, giá trị được phép là: `VIEW_HASHTAG`. |
| ↳↳↳ action_category_ids | string[] | Danh sách ID danh mục tương tác video, danh mục tương tác nhà sáng tạo, hashtag hoặc nhóm hashtag bạn muốn dùng để nhắm mục tiêu đối tượng. |
| ↳↳ smart_interest_behavior_enabled | boolean | Liệu Smart interests & behaviors is turned on. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart interests & behaviors and how to turn on Smart interests & behaviors, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ smart_audience_enabled | boolean | Có thực hiện turn on Smart audience. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart audience and how to turn on Smart audience, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ spending_power | string | Spending power that you want to target. ⏎ Các giá trị enum hỗ trợ: `ALL`, `HIGH`. ⏎ If it is set to `HIGH`, you can target high spending users who typically spend more on purchases on TikTok ads than average users. |
| ↳↳ household_income | string[] | Household income that you want to target. ⏎ Các giá trị enum hỗ trợ: `TOP5`(Top 5% of ZIP codes), `TOP10`(Top 10% of ZIP codes), `TOP10_25`(Top 10% -25% of ZIP codes), `TOP25_50`(Top 25% - 50% of ZIP codes). |
| ↳↳ min_android_version | string | Minimum Android version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ min_ios_version | string | Audience minimum ios version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị. |
| ↳↳ network_types | string[] | Network types that you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ carrier_ids | string[] | Danh sách nhà mạng bạn muốn nhắm mục tiêu. |
| ↳↳ isp_ids | string[] | Danh sách ID nhà cung cấp dịch vụ Internet (ISP) được nhắm mục tiêu. |
| ↳↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu. 10000 nghĩa là 1000+. Các số phải là bội số của 50. ⏎ **Quan trọng**: Giới hạn trên bạn đặt sẽ được cộng thêm 50 và số mới thu được sẽ được sử dụng làm giới hạn trên thực tế cho nhắm mục tiêu thiết bị. Giới hạn trên thực tế được hiển thị trong cài đặt nhóm quảng cáo trên Trình quản lý quảng cáo TikTok. Nếu bạn đặt và nhận khoảng giá [0, 250], điều đó thực tế có nghĩa là [0, 300]. |
| ↳↳ saved_audience_id | string | Được trả về khi bạn đã chỉ định `saved_audience_id` khi tạo nhóm quảng cáo. ⏎ ID Đối tượng đã lưu (Saved Audience ID). |
| ↳↳ blocked_pangle_app_ids | string[] | Danh sách ID ứng dụng Pangle bị chặn. |
| ↳↳ brand_safety_type | string | Inventory filter tier for the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Expanded inventory. Your ads will not appear next to explicitly inappropriate content, but they may appear next to content that features mature themes. • `STANDARD_INVENTORY`: Standard inventory. Your ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Limited inventory. Your ads will not appear next to content that contains mature themes. • `NO_BRAND_SAFETY`: Full inventory without using any brand safety solution, which means your ads may appear next to some content featuring mature themes. ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳↳ category_exclusion_ids | string[] | Danh sách ID danh mục nội dung cần loại trừ. |
| ↳ is_hfss | boolean | Liệu promoted content is HFSS (High Fat, Salt, Sugar) Product/Brand. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ is_lhf_compliance | boolean | Liệu promoted content complies with LHF (Less Healthy Foods) regulations. ⏎ When `is_lhf_compliance` is `true`, you confirm that any food or drink products you advertise on TikTok in the UK comply with the [2024 Less Healthy Foods Regulations](https://www.legislation.gov.uk/uksi/2024/1266/made) and all other applicable laws. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ placement_type | string[] | The placement strategy that decides where your ads will be shown. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TYPE_AUTOMATIC`: Automatic placement. • `PLACEMENT_TYPE_NORMAL` : Select placement. |
| ↳ placements | string[] | The apps where you want to deliver your ads. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TIKTOK`: TikTok. • `PLACEMENT_PANGLE`: Pangle. • `PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle. |
| ↳ tiktok_subplacements | string[] | The subplacements within TikTok for your ads, allowing you to choose where your ads will appear. ⏎ Các giá trị enum hỗ trợ: • `LEMON8`: Lemon8, a community app for lifestyle content, focusing on real-life experiences, tips, guides, and product reviews. By including Lemon8 as a subplacement, your ads will appear in its For You feed, Search feed, and Immersive Video feed. [Learn more about Lemon8 for Performance Auction](https://ads.tiktok.com/help/article/about-lemon8-in-tiktok-ads-manager). • `PINE_DRAMA`: PineDrama, an app for watching short-form dramas. Ads will be placed on recommendation pages, within episode streams, and more. [Learn more about PineDrama for Performance Auction](https://ads.tiktok.com/help/article/about-pinedrama-for-performance-auction-in-tiktok-ads-manager). |
| ↳ search_result_enabled | boolean | Có thực hiện include your ads in Search Ads, namely to show your ads to users when they search for your business on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ comment_disabled | boolean | Có thực hiện allow comments on your ads on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ share_disabled | boolean | Có thực hiện disable sharing of the campaign to third-party platforms. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ video_download_disabled | boolean | Liệu users can download your video ads on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ skip_learning_phase | boolean | Có thực hiện skip the learning stage. ⏎ Supported value: `true`. |
| ↳ create_time | string | Thời điểm nhóm quảng cáo được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Ví dụ: `2025-01-01 00:00:01`. |
| ↳ modify_time | string | Thời điểm nhóm quảng cáo được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Ví dụ: `2025-01-01 00:00:01`. |

### Ví dụ lệnh cURL (Example)
#### Nhắm mục tiêu tự động không kèm gợi ý đối tượng
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_id": "{{adgroup_id}}",
        "adgroup_name": "{{adgroup_name}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "attribution_event_count": "ONCE",
        "bid_type": "BID_TYPE_NO_BID",
        "billing_event": "OCPM",
        "budget": 0,
        "budget_mode": "BUDGET_MODE_INFINITE",
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "click_attribution_window": "SEVEN_DAYS",
        "comment_disabled": false,
        "create_time": "{{create_time}}",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "deep_bid_type": "DEFAULT",
        "engaged_view_attribution_window": "SEVEN_DAYS",
        "min_budget": 0,
        "modify_time": "{{modify_time}}",
        "operation_status": "ENABLE",
        "optimization_event": "ACTIVE",
        "optimization_goal": "INSTALL",
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
        "secondary_status": "ADGROUP_STATUS_CREATE",
        "share_disabled": false,
        "skip_learning_phase": true,
        "targeting_optimization_mode": "AUTOMATIC",
        "targeting_spec": {
            "actions": [],
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
}
```

#### Nhắm mục tiêu tự động kèm gợi ý đối tượng
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_id": "{{adgroup_id}}",
        "adgroup_name": "{{adgroup_name}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "attribution_event_count": "ONCE",
        "bid_type": "BID_TYPE_NO_BID",
        "billing_event": "OCPM",
        "budget": 0,
        "budget_mode": "BUDGET_MODE_INFINITE",
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "click_attribution_window": "SEVEN_DAYS",
        "comment_disabled": false,
        "create_time": "{{create_time}}",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "deep_bid_type": "DEFAULT",
        "engaged_view_attribution_window": "SEVEN_DAYS",
        "min_budget": 0,
        "modify_time": "{{modify_time}}",
        "operation_status": "ENABLE",
        "optimization_event": "ACTIVE",
        "optimization_goal": "INSTALL",
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
        "secondary_status": "ADGROUP_STATUS_CREATE",
        "share_disabled": false,
        "skip_learning_phase": true,
        "suggestion_audience_enabled": true,
        "targeting_optimization_mode": "AUTOMATIC",
        "targeting_spec": {
            "actions": [
                {
                    "action_category_ids": [
                        "13",
                        "15"
                    ],
                    "action_period": 15,
                    "action_scene": "VIDEO_RELATED",
                    "video_user_actions": [
                        "WATCHED_TO_END",
                        "LIKED",
                        "COMMENTED",
                        "SHARED"
                    ]
                },
                {
                    "action_category_ids": [
                        "8",
                        "10"
                    ],
                    "action_period": 0,
                    "action_scene": "CREATOR_RELATED",
                    "video_user_actions": [
                        "FOLLOWING",
                        "VIEW_HOMEPAGE"
                    ]
                },
                {
                    "action_category_ids": [
                        "8",
                        "5"
                    ],
                    "action_period": 0,
                    "action_scene": "HASHTAG_RELATED",
                    "video_user_actions": [
                        "VIEW_HASHTAG"
                    ]
                }
            ],
            "age_groups": [
                "AGE_18_24",
                "AGE_25_34",
                "AGE_35_44",
                "AGE_45_54",
                "AGE_55_100"
            ],
            "audience_ids": [
                "{{audience_id}}",
                "{{audience_id}}",
                "{{audience_id}}",
                "{{audience_id}}"
            ],
            "brand_safety_type": "STANDARD_INVENTORY",
            "category_exclusion_ids": [
                "200",
                "201",
                "202",
                "203"
            ],
            "gender": "GENDER_UNLIMITED",
            "interest_category_ids": [
                "17",
                "10"
            ],
            "location_ids": [
                "1562822"
            ],
            "operating_systems": [
                "ANDROID"
            ],
            "purchase_intention_keyword_ids": [
                "14",
                "17"
            ],
            "spc_audience_age": "OVER_EIGHTEEN",
            "spending_power": "ALL"
        },
        "video_download_disabled": false,
        "view_attribution_window": "ONE_DAY"
    }
}
```

#### Custom targeting
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_id": "{{adgroup_id}}",
        "adgroup_name": "{{adgroup_name}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "attribution_event_count": "ONCE",
        "bid_type": "BID_TYPE_NO_BID",
        "billing_event": "OCPM",
        "budget": 0,
        "budget_mode": "BUDGET_MODE_INFINITE",
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "click_attribution_window": "SEVEN_DAYS",
        "comment_disabled": false,
        "create_time": "{{create_time}}",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "deep_bid_type": "DEFAULT",
        "engaged_view_attribution_window": "SEVEN_DAYS",
        "min_budget": 0,
        "modify_time": "{{modify_time}}",
        "operation_status": "ENABLE",
        "optimization_event": "ACTIVE",
        "optimization_goal": "INSTALL",
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
        "secondary_status": "ADGROUP_STATUS_CREATE",
        "share_disabled": false,
        "skip_learning_phase": true,
        "suggestion_audience_enabled": false,
        "targeting_optimization_mode": "MANUAL",
        "targeting_spec": {
            "actions": [
                {
                    "action_category_ids": [
                        "13",
                        "15"
                    ],
                    "action_period": 15,
                    "action_scene": "VIDEO_RELATED",
                    "video_user_actions": [
                        "WATCHED_TO_END",
                        "LIKED",
                        "COMMENTED",
                        "SHARED"
                    ]
                },
                {
                    "action_category_ids": [
                        "8",
                        "10"
                    ],
                    "action_period": 0,
                    "action_scene": "CREATOR_RELATED",
                    "video_user_actions": [
                        "FOLLOWING",
                        "VIEW_HOMEPAGE"
                    ]
                },
                {
                    "action_category_ids": [
                        "8",
                        "5"
                    ],
                    "action_period": 0,
                    "action_scene": "HASHTAG_RELATED",
                    "video_user_actions": [
                        "VIEW_HASHTAG"
                    ]
                }
            ],
            "age_groups": [
                "AGE_18_24",
                "AGE_25_34",
                "AGE_35_44",
                "AGE_45_54",
                "AGE_55_100"
            ],
            "audience_ids": [
                "{{audience_id}}",
                "{{audience_id}}",
                "{{audience_id}}",
                "{{audience_id}}"
            ],
            "brand_safety_type": "STANDARD_INVENTORY",
            "category_exclusion_ids": [
                "200",
                "201",
                "202",
                "203"
            ],
            "gender": "GENDER_UNLIMITED",
            "interest_category_ids": [
                "17",
                "10"
            ],
            "location_ids": [
                "1562822"
            ],
            "operating_systems": [
                "ANDROID"
            ],
            "purchase_intention_keyword_ids": [
                "14",
                "17"
            ],
            "smart_audience_enabled": true,
            "smart_interest_behavior_enabled": false,
            "spending_power": "HIGH"
        },
        "video_download_disabled": false,
        "view_attribution_window": "ONE_DAY"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 3/7**:

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

