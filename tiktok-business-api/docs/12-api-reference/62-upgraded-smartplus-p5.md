# Smart+ nâng cấp (Upgraded Smart+) — phần 5/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Create an Upgraded Smart+ Ad (#doc-1843317390059522)](#doc-1843317390059522)

---

<a id="doc-1843317390059522"></a>
<!-- doc_id: 1843317390059522 -->
<!-- doc_id: 1843317390059522 -->
# Create an Upgraded Smart+ Ad
> Đường dẫn: API Reference > Upgraded Smart+ > Ads > Create an Upgraded Smart+ Ad
Sử dụng endpoint này để tạo an Upgraded Smart+ Ad.

Currently, you can only create a maximum of 30 ads within an Upgraded Smart+ Ad Group.

> **Important:** 
> Creating non-Spark Ads using Custom Identities in ad groups that deliver to Automatic Placement or Select Placement when TikTok is included is no longer supported for existing ad accounts. All new ad accounts created on or after January 15, 2026 cannot create non-Spark Ads using Custom Identities for these placements. Existing ads remain unaffected and editable. Ad campaigns that deliver only to Pangle or Global App Bundle placements are not be affected by Custom Identity deprecation. Learn more [about changes coming to Custom Identity](https://ads.tiktok.com/help/article/about-changes-coming-to-custom-identity) and [migrate to Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1848048566169730).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/create/

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
| adgroup_id  ****(Bắt buộc)**** | string | ID nhóm quảng cáo. ⏎ To obtain ad group IDs, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). |
| ad_name | string | Ad name. ⏎ To make the ad name automatically generated, set this field to `""`(empty string). The format of the auto-generated ad name is ID mẫu quảng cáo (`ad_id`). ⏎ Giới hạn độ dài: 512 and cannot contain emojis. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. |
| operation_status | string | The status of the ad when created. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad is enabled when created. • `DISABLE` : The ad is disabled when created.Giá trị mặc định: `ENABLE`. |
| creative_list **(Điều kiện)** | object[] | • Required for Single Video, Standard Carousel, and Catalog Carousel formats. • Not needed for the Multi-Show format. ⏎ A list of creatives. ⏎ Size range: 1-50. |
| ↳ creative_info  **(Điều kiện)** | object | Bắt buộc khi `creative_list` is specified. ⏎ Creative information. |
| ↳↳ ad_format  **(Điều kiện)** | string | Bắt buộc khi `creative_info` is specified. ⏎ The ad format. ⏎ Các giá trị enum hỗ trợ: • `SINGLE_VIDEO`: Single Video. • To use this format, specify any of the following: • a video through `video_id` and a video cover through `web_uri` • a TikTok video post through `tiktok_item_id`. • `CAROUSEL_ADS`: Standard Carousel. • To use this format, specify any of the following: • carousel images through `web_uri` and a piece of music through `music_id`. • TikTok photo posts images through `tiktok_item_id`. • `CATALOG_CAROUSEL`: Catalog Carousel. • To use this format in Upgraded Smart+ Web Catalog Carousel Ads, specify a piece of music through `music_id`. • To use this format in Upgraded Smart+ Automotive Catalog Carousel Ads, specify a piece of music through `music_id` and an end card through `web_uri`. |
| ↳↳ material_name | string | Chỉ hợp lệ khi `ad_format` is `CAROUSEL_ADS`. ⏎ A custom name for the carousel. ⏎ Giới hạn độ dài: 255 characters. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. ⏎ To make the carousel name automatically generated, set this field to `""`(empty string) or leave this field unspecified. |
| ↳↳ video_info **(Điều kiện)** | object | Required for the following types of ads: ⏎ • Non-Spark Ads Single Video ads.  • Spark Ads Single Video ads through Spark Ads Push. ⏎ Video information. |
| ↳↳↳ video_id **(Điều kiện)** | string | Bắt buộc khi `video_info` is specified. ⏎ Video ID. ⏎ To upload a video and obtain the video ID, use [/file/video/ad/upload/](71-video.md#doc-1737587322856449). ⏎ To search for videos within your ad account, use [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| ↳↳↳ file_name | string | Video name. |
| ↳↳ thumbnail_mode | string | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level, `is_search_campaign` is `true`. • At the ad level, `video_info` is specified. ⏎ The mode of the video thumbnail. ⏎ The thumbnail will be shown as the first image on a search results page. Thumbnails are critical for catching your audience's attention and driving clicks. ⏎ Các giá trị enum hỗ trợ: • `AUTOMATIC`: Smart thumbnail. The system will show a different frame from your video customized for different audiences to closely match what they're searching for and what they're most likely to tap. You need to manually specify a video cover through `image_info`, which will be used as the fallback video thumbnail if no matching thumbnails are found. • `MANUAL`: Manual thumbnail. You need to manually specify a video cover through `image_info`, which will be used as the video thumbnail. ⏎ By default, the video thumbnail mode is manual thumbnail. |
| ↳↳ image_info **(Điều kiện)** | object[] | • Required for the following types of ads: • Non-Spark Ads Single Video ads. You need to specify a video cover. • Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. • Non-Spark Ads Standard Carousel ads. You need to specify one to 35 carousel images. • Spark Ads Standard Carousel ads through Spark Ads Push. You need to specify one to 35 carousel images. • Catalog Carousel ads in [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314). You need to specify one image as the end card image. • Not supported for Catalog Carousel ads in Upgraded Smart+ Web Ads. ⏎ Image information. |
| ↳↳↳ web_uri **(Điều kiện)** | string | Bắt buộc khi `image_info` is specified. ⏎ Image ID. ⏎ To upload an image and obtain the image ID, use [/file/image/ad/upload/](47-images.md#doc-1739067433456642). ⏎ To search for images within your ad account, use [/file/image/ad/search/](47-images.md#doc-1740052016789506). |
| ↳↳ music_info **(Điều kiện)** | object | Required for the following scenarios: ⏎ • When you create Standard Carousel Ads, including: • Non-Spark Ads Standard Carousel ads • Spark Ads Standard Carousel ads through Spark Ads Push • Spark Ads Standard Carousel ads through Spark Ads Pull • When `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION` and `catalog_creative_toggle` is `true`. The system will automatically generate catalog carousel ads. ⏎ Music information. |
| ↳↳↳ music_id **(Điều kiện)** | string | Bắt buộc khi `music_info` is specified. ⏎ The ID of the piece of music to use in the carousel ads. |
| ↳↳ aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` within `ad_configuration` is `CUSTOMIZED_USER`. ⏎ Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content. • `NOT_DECLARED`: To not declare that the ad contains AI-generated content.Giá trị mặc định: `NOT_DECLARED`. ⏎ To learn about the supported advertising objectives and ad formats for the toggle and the detailed steps for using the toggle, see [AIGC self-disclosure toggle](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). |
| ↳↳ tiktok_item_id **(Điều kiện)** | string | • Bắt buộc khi you create Spark Ads through Spark Ads Pull, including: • Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. • Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post. • Not supported when `catalog_creative_toggle` is `true`. ⏎ The ID of the TikTok post to be used as an ad (Spark Ads). ⏎ Pass in the `item_id` you get from the response of the [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) and [/identity/video/get/](46-identity.md#doc-1740218475032577) endpoints. ⏎ When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `title_list`. ⏎ **Note**: By using Spark Ads, you confirm that you have the rights to use the music in the videos for commercial purposes. |
| ↳↳ identity_type **(Điều kiện)** | string | Bắt buộc khi you create Spark Ads without using catalog creatives. ⏎ Identity type. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). ⏎ **Note**:  • If you want to create Spark Ads using catalog creatives, specify the `identity_type` and `identity_id` within `ad_configuration`. • If this field is set to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE` and the following conditions are both met, you need to specify a dynamic CTA via `call_to_action_id`. • At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳↳ identity_id **(Điều kiện)** | string | Bắt buộc khi you create Spark Ads without using catalog creatives. ⏎ Identity ID. ⏎ **Note**: If you want to create Spark Ads using catalog creatives, specify the `identity_type` and `identity_id` within `ad_configuration`. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| playable_list | object[] | Valid only in any of the following scenarios: • Scenario 1: • At the campaign level, `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`. • At the ad group level, the placement is not Global Apple Bundle-only (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_GLOBAL_APP_BUNDLE"]`) . • At the ad level, `ad_format` is `SINGLE_VIDEO` and a video or video post is specified. • Scenario 2: • At the campaign level, `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `MINIS`. • At the ad group level: • `promotion_type` is `MINI_GAME`. • The placement is not Global Apple Bundle-only (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_GLOBAL_APP_BUNDLE"]`) . • At the ad level, `ad_format` is `SINGLE_VIDEO` and a video or video post is specified. ⏎ The list of playables. ⏎ Kích thước tối đa: 5. ⏎ **Note**: The Playable Ad is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ playable_url | string | The URL of the playable. • To upload playables to the Creative Library of your ad account and obtain the playable URLs, see [Upload playables](../09-marketing-api/creatives.md#doc-1868153086739601). • To obtain the URLs of existing playables within your ad account, use [/playable/get/](56-playable-ads.md#doc-1737732758495234). ⏎ **Note**: If you want to create Playable Ads using TikTok-only placement (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_TIKTOK"]`), ensure the playables are not horizontal. To verify the orientation of your playable, use [/playable/get/](56-playable-ads.md#doc-1737732758495234) and confirm that the `playable_orientation` is either `BOTH` or `PORTRAIT`. |
| ad_text_list **(Điều kiện)** | object[] | Bắt buộc khi `tiktok_item_id` is not specified. ⏎ List of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. ⏎ Kích thước tối đa: 5. |
| ↳ ad_text **(Điều kiện)** | string | Bắt buộc khi `ad_text_list` is specified. ⏎ Ad text. |
| auto_message_list **(Điều kiện)** | object[] | Bắt buộc khi `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` at the ad group level. ⏎ Details of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Kích thước tối đa: 1. |
| ↳ auto_message_id **(Điều kiện)** | string | Bắt buộc khi `auto_message_list` is specified. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is welcome message. • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ To learn more about how to create TikTok Direct Messaging Ads with welcome messages, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as TikTok direct messages](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302969710913). |
| call_to_action_list**(Điều kiện)** | object[] | Call-to-action list. ⏎ Kích thước tối đa: 3. ⏎ Liệu this field is required varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact scenarios where this field is required. |
| ↳ call_to_action **(Điều kiện)** | string | Bắt buộc khi `call_to_action_list` is specified. ⏎ Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| interactive_add_on_list | object[] | A list of interactive add-on (creative portfolio) IDs. ⏎ Size range: 0-1. |
| ↳ card_id | string | The ID of an interactive add-on. ⏎ Pass the ID of one of the following creative portfolio types: • Display Card. • Hotel Card. • Flight Card. • Destination Card. • Countdown Sticker. • Gift Code Sticker. • Inventory Card (for [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314)). ⏎ To create a creative portfolio, use [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426). • To learn about how to get the ID of a Display Card, Inventory Card, Hotel Card, Flight Card, or Destination Card portfolio, see [Cards](../09-marketing-api/creatives.md#doc-1749019652141058). • To learn about how to get the ID of a Countdown Sticker or Giftcode Sticker portfolio, see [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177). |
| page_list | object[] | A list of pages. ⏎ Size range: 0-3. |
| ↳ page_id | string | Page ID. ⏎ • To obtain pages within your ad account, use [/page/get/](54-page.md#doc-1820826387779586). • To create instant pages, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881). |
| landing_page_url_list | object[] | Landing page URL list. ⏎ Size range: 0-1. |
| ↳ landing_page_url **(Điều kiện)** | string | Bắt buộc khi `landing_page_url_list` is specified. ⏎ Landing page URL. |
| custom_product_page_list | object[] | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • `is_search_campaign` is `false`. • At the ad group level: • An iOS app is specified via `app_id`. ⏎ Details of the custom product page to use in the ad. ⏎ Size range: 0-1. |
| ↳ custom_product_page_url | string | The Custom Product Page (CPP) URL. ⏎ CPPs are product pages with customized screenshots, promotional text, and app previews that can be used to highlight specific content or features of the promoted app, or reach specific audiences. Only users with iOS 15+ will be able to open a custom product page. ⏎ The CPP URL must be consistent with the promoted app (`app_id`) at the ad group level. ⏎ Format: `https://apps.apple.com/{region}/app/{app_name}/id{app_id}?ppid={ppid}`. ⏎ Giới hạn độ dài: 512 characters. ⏎ Example: `https://apps.apple.com/us/app/tiktok/id835599320?ppid=12345a6b-c789-12d3-e4f5-g6h78i91jk2l`. ⏎ To learn about how to create Custom Product Pages in the Apple App Store and obtain the corresponding CPP URLs, see [Custom product pages on the App Store](https://developer.apple.com/app-store/custom-product-pages/). |
| deeplink_list | object[] | A list of deeplinks. ⏎ Size range: 0-1. |
| ↳ deeplink | string | Deeplink, the specific location where you want your audience to go if they have your app installed. |
| ↳ deeplink_type **(Điều kiện)** | string | Bắt buộc khi `deeplink` is specified. ⏎ The deeplink type. ⏎ Enum value: `DEFERRED_DEEPLINK`, `NORMAL`. ⏎ If you pass this field, you should also provide the `deeplink` field. |
| multi_dest_list **(Điều kiện)** | object[] | Required and Chỉ hợp lệ khi `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION` is specified at the ad group level. ⏎ A list of destinations for the Lead Generation ad. ⏎ To learn about the ad type where this field can be used, see [Create an Upgraded Smart+ Lead Generation Campaign with multiple location selection](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1876685025962241). |
| ↳ dest_type **(Điều kiện)** | string | Bắt buộc khi `multi_dest_list` is specified. ⏎ Destination type. ⏎ Các giá trị enum hỗ trợ: • `EXTERNAL_WEBSITE`: Website URL. You need to specify `landing_page_url` simultaneously. • `INSTANT_PAGE`: Instant Form. You need to specify `page_id` simultaneously. • `TT_DIRECT_MESSAGAE`: Message template. You need to specify `auto_message_id` simultaneously. ⏎ **Note**: Once set, this field cannot be updated. |
| ↳ landing_page_url **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `EXTERNAL_WEBSITE`. ⏎ Landing page URL. |
| ↳ page_id **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `INSTANT_PAGE`. ⏎ The ID of an Instant Form. • To obtain the page IDs of Instant Forms within your ad account, use [/page/get/](54-page.md#doc-1820826387779586) and set `business_type` to `LEAD_GEN`. • To create an Instant Form, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881) and set `businessType` to `1`. |
| ↳ auto_message_id **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `TT_DIRECT_MESSAGAE`. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is message template (welcome message). • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ **Note**: Once set, this field cannot be updated. |
| disclaimer | object | Chỉ hợp lệ khi the following conditions are both met: • At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`, or `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `false` or not specified. • At the ad group level, the TikTok placement is included. You can use any of the following configurations: • **Automatic Placement**: Leave `placement_type` and `placements` unspecified. • **Select specific placements** with TikTok included: Set `placement_type` to `PLACEMENT_TYPE_NORMAL` and include `PLACEMENT_TIKTOK` in the value for `placements`.Disclaimer information. ⏎ **Note**: Once added to your ads, the disclaimer cannot be deleted. |
| ↳ disclaimer_type **(Điều kiện)** | string | Bắt buộc khi `disclaimer` is specified. ⏎ The type of disclaimer that you want to add to the ad. ⏎ You can add a disclaimer to ensure your ad remains compliant with local and regional policies. ⏎ Các giá trị enum hỗ trợ: • `TEXT_ONLY`: text-only disclaimer.  • `TEXT_LINK`: clickable disclaimer. ⏎ See [Include disclaimers in ads](../09-marketing-api/creatives.md#doc-1739953274550273) to learn about how to configure disclaimer settings. ⏎ **Note**: Once set, this field cannot be updated. |
| ↳ disclaimer_text **(Điều kiện)** | object | Bắt buộc khi `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer in the ad. |
| ↳↳ text **(Điều kiện)** | string | Bắt buộc khi `disclaimer_text` is specified. ⏎ The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳ disclaimer_clickable_texts **(Điều kiện)** | object[] | Bắt buộc khi `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. ⏎ Kích thước tối đa: 3. ⏎ If you use multiple clickable disclaimers, both the overall length for all the texts you specify and the length of individual text need to be no more than 40 characters. |
| ↳↳ text **(Điều kiện)** | string | Bắt buộc khi `disclaimer_clickable_texts` is specified. ⏎ The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳ url **(Điều kiện)** | string | Bắt buộc khi `disclaimer_clickable_texts` is specified. ⏎ The URL for the clickable disclaimer. ⏎ When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ad_configuration | object | Additional configurations. |
| ↳ identity_type **(Điều kiện)** | string | Required in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives. • You are creating Spark Ads with the Multi-Show format using an entertainment catalog. Learn more about how you can create such ads in [Create Upgraded Smart+ Streaming Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302920924306). ⏎ Identity type. • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. • Enum values for Upgraded Smart+ Streaming Spark Ads with the Multi-Show format (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ identity_id **(Điều kiện)** | string | Required in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives. • You are creating Spark Ads with the Multi-Show format using an entertainment catalog. Learn more about how you can create such ads in [Create Upgraded Smart+ Streaming Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302920924306). ⏎ Identity ID. |
| ↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ dark_post_status | string | Chỉ hợp lệ khi you create Spark Ads through Spark Ads Push. ⏎ The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. ⏎ Giá trị mặc định: `ON`. ⏎ **Note**:  • You can set this to `OFF` only if both the identity's "Show through ads only" mode is disabled and the ad account does not have mandatory "Show through ads only" mode enabled. If the ad account enforces mandatory "Ads-only mode", you can only set this field to `ON` when creating Spark Ads using Spark Ads Push. This prevents the posts from appearing on your TikTok profile and gaining organic traffic, regardless of the identity's own `ads_only_mode` setting. It's a safeguard to ensure your Spark Ads Push content remains ads-only and avoids accidental profile posts. • To confirm the "Show through ads only" mode status of an identity, use [/identity/info/](46-identity.md#doc-1740218453385217) and check the returned `ads_only_mode`.  • To confirm the mandatory "Show through ads only" mode status of an ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `ads_only_mode`. |
| ↳ product_specific_type **(Điều kiện)** | string | • When `catalog_enabled` is `true` at the campaign level, this field is required and can be set to `ALL`, `PRODUCT_SET`, or `CUSTOMIZED_PRODUCTS`. • When `catalog_enabled` is `false` or not set at the campaign level, this field is optional and can only be set to `UNSET`. ⏎ Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products. • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. • `UNSET`: Unset. ⏎ • If this field is set to `ALL`, you don't need to input `product_set_id` and `product_ids`. • If this field is set to `PRODUCT_SET`, you need to pass in `product_set_id`. • If this field is set to `CUSTOMIZED_PRODUCTS`, `product_ids` is required. |
| ↳ product_set_id **(Điều kiện)** | string | Bắt buộc khi `product_specific_type` is `PRODUCT_SET`. ⏎ The ID of a product set. ⏎ • To retrieve the product sets within your ad account, use [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169). • To create a product set, use [/catalog/set/create/](29-catalog-product-sets.md#doc-1740572891104257). |
| ↳ product_ids **(Điều kiện)** | string[] | Bắt buộc khi `product_specific_type` is `CUSTOMIZED_PRODUCTS`. ⏎ The product IDs of the catalog products. ⏎ Kích thước tối đa: 20. ⏎ To retrieve the product ID (`product_id`) of each catalog product, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳ catalog_creative_toggle | boolean | Chỉ hợp lệ khi `catalog_enabled` is `true` at the campaign level. ⏎ Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ • If you set this field to `true` in Upgraded Smart+ Web Ads using the catalog carousel format, you need to provide a `creative_info` with only `music_info` in it to specify the music to be used in catalog carousel. • If you set this field to `true` in [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314) using the catalog carousel format, you need to provide a `creative_info` with one image in `image_info` and `music_info` in it to specify the end card image and music to be used in catalog carousel. |
| ↳ catalog_creative_info | object | Chỉ hợp lệ khi`catalog_creative_toggle` is `true` and this field is supported for your specific use case.  • The availability of this field varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. ⏎ Additional settings for catalog creatives to use in your ads. |
| ↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce, entertainment, generic, or online-to-offline catalog to use in the ad. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates. • `MULTI_SHOW`: Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. • When you use this format, specify the identity details through the parameters `identity_type`, `identity_id`, and `identity_authorized_bc_id` within the object `ad_configuration`. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. ⏎ **Note**: If you specify `catalog_media_settings`, you cannot subsequently update `catalog_creative_toggle` to `false` or update `catalog_media_settings` to an empty list (`[]`). |
| ↳↳ catalog_template_video_id | string | The ID of a video template in your catalog to use in the ad. • To obtain the IDs of video templates (video packages) in your catalog, use [/catalog/video_package/get/](31-catalog-video-templates.md#doc-1740574099715073). • To learn about how to create video packages on TikTok Ads Manager, see [How to create video packages in a Catalog](https://ads.tiktok.com/help/article/how-to-create-video-packages-in-a-catalog). ⏎ The availability of this field varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. |
| ↳ creative_auto_add_toggle | boolean | Valid only in any of the following scenarios: ⏎ • Scenario 1: • At the campaign level, `objective_type` is `WEB_CONVERSIONS` and `sales_destination` is `WEBSITE`. • Scenario 2: • At the campaign level, `objective_type` is `LEAD_GENERATION`. • At the ad group level, `promotion_type` is `LEAD_GENERATION` and `promotion_target_type` is `INSTANT_PAGE` or `EXTERNAL_WEBSITE`. • Scenario 3: • At the campaign level, `objective_type` is `LEAD_GENERATION`. • At the ad group level, `promotion_type` is `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` and `messaging_app_type` is `MESSENGER` or `WHATAPP`. ⏎ Có thực hiện auto-add newly generated assets during delivery. ⏎ During your campaign, the system will generate new creative assets from your existing campaign assets and creative library. By using TikTok's latest trending elements (hooks, music, text, and more), you'll get high-quality, ready-to-use content that delivers alongside your other selected assets. ⏎ New assets will be added to your campaign automatically and won't appear on your TikTok profile. You can turn off this feature anytime. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ The Giá trị mặc định for this field is determined by your allowlist status for the "auto-adding newly generated assets during delivery by default" feature: • If you are allowlisted, this field will default to `true`. • If you are not allowlisted, this field will default to `false`. ⏎ **Note**: Auto-adding newly generated assets during delivery is available to all advertisers. However, having it turned on by default is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ creative_auto_enhancement_strategy_list | string[] | The list of automatic enhancement strategies to apply to your ads. ⏎ Automatic enhancements are real-time edits applied to your ads during your campaign. They can improve performance by creating more engaging and impactful visuals, sound, and more. ⏎ For best results, turn on all automatic enhancements to improve the overall quality of your ads without any extra work. ⏎ Các giá trị enum hỗ trợ: • `TRANSLATE_AND_DUB`: Translate and dub. Connect with global audiences by delivering your ad in 50+ languages. • `MUSIC_REFRESH`: Music refresh. Stay on-trend by swapping in music currently popular on TikTok. • `VIDEO_QUALITY`: Video quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_QUALITY`: Image quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_RESIZE`: Resize. Resize your image to take advantage of full-screen capabilities. ⏎ The Giá trị mặc định for this field is determined by your allowlist status for the "automatic enhancements enabled by default" feature: • If you are allowlisted for certain strategies to be enabled by default, this field will default to a list of those strategies. • For example, if you are allowlisted for all these strategies to be enabled by default, this field will default to `["TRANSLATE_AND_DUB","MUSIC_REFRESH","VIDEO_QUALITY","IMAGE_QUALITY","IMAGE_RESIZE"]`.  • If you are not allowlisted for any strategies to be enabled by default, this field will default to an empty list (`[]`). ⏎ To learn about the scenarios where you can enable this setting, see [Availability of Automatic Enhancements for Upgraded Smart+ Ads](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1855450880142402). ⏎ **Note**:  • Automatic enhancements are available to all advertisers. However, having them turned on by default is currently a separate allowlist-only feature for each enhancement. If you would like to access it, please contact your TikTok representative. . • In Upgraded Smart+ Generic Catalog Ads using the `WEB_CONVERSIONS` objective (where `objective_type` is `WEB_CONVERSIONS`, `catalog_enabled` is `true`, and `catalog_type` is `GENERIC`), you need to set `creative_auto_enhancement_strategy_list` to `[]` at the same time when you set any of the following parameters: • `catalog_media_settings` • `catalog_tag_list` |
| ↳ deeplink_utm_params | object[] | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level: • `objective_type` is `WEB_CONVERSIONS` • `sales_destination` is `APP`. • At the ad level: • `deeplink` is specified. • `deeplink_type` is `DEFERRED_DEEPLINK`. ⏎ A list of deeplink URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. ⏎ Kích thước tối đa: 14. ⏎ **Note**: Deeplink URL parameters are currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳↳ key | string | The deeplink URL parameter. ⏎ You can specify a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳↳ value | string | The value of the deeplink URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| ↳ end_card_cta **(Điều kiện)** | string | Bắt buộc khi the following conditions are met: • At the campaign level: • `objective_type` is `LEAD_GENERATION`. • `catalog_enabled` is `true`. • At the ad group level: • An Auto-Inventory or Auto-Model catalog is specified through `catalog_id`. • At the ad level: • `catalog_creative_toggle` is `true`. ⏎ Call-to-action for the end card (`image_info`) of an Upgraded Smart+ [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873), or [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). ⏎ Các giá trị enum hỗ trợ: • `SEARCH_INVENTORY` (Recommended): Search inventory. • `LEARN_MORE`: Learn more. • `SHOP_NOW`: Shop now. • `SIGN_UP`: Sign up. • `CONTACT_US`: Contact us. • `BOOK_NOW`: Book now. • `READ_MORE`: Read more. • `VIEW_MORE`: View now. • `ORDER_NOW`: Order now. • `SEND_MESSAGE`: Send message. • This value is only available for [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). |
| ↳ product_display_field_list | string[] | A list of product details to display in your [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161). ⏎ Các giá trị enum hỗ trợ: • `DEALER_NAME`: the `dealer_name` field of vehicles. • `MAKE`: the `make` field of vehicles. • `MODEL`: the `model` field of vehicles. • `YEAR`: the `year` field of vehicles. • `MILEAGE`: the `mileage` field of vehicles. • `PRICE`: the `price` field of vehicles. • `SALE_PRICE`: the `sale_price` field of vehicles. • `EXTERIOR_COLOR`: the `exterior_color` field of vehicles. • `TRIM`: the `trim` field of vehicles. • `ADDRESS_CITY`: the `city` field of vehicles. • `VEHICLE_STATE`: the `state_of_vehicle` field of vehicles.Max size for Automotive Carousel Ad for Inventory: 2. ⏎ Enum values for Upgraded Smart+ Lead Generic Catalog Ads: • `RATING`: the `rating` field of generic products or services. • `SALE_PRICE`: the `sale_price` field of generic products or services. • `PRICE`: the `price` field of generic products or services. • `DESCRIPTION`: the `description` field of generic products or services. • `ADDRESS_CITY`: the `address.city` field of generic products or services. • `ADDRESS_REGION`: the `address.region` field of generic products or services. • `ADDRESS_STREET`: the `address.street` field of generic products or services. • `CUSTOM_LABEL_0`: the `custom_label_0` field of generic products or services. • `CUSTOM_LABEL_1`: the `custom_label_1` field of generic products or services. • `CUSTOM_LABEL_2`: the `custom_label_2` field of generic products or services.Max size for Upgraded Smart+ Lead Generic Catalog Ads: 2. ⏎ The title of each vehicle, product, or service is displayed automatically. For instance, if you set this field to `["MILEAGE","YEAR"]`, the ad will display the `mileage`, `price` and `title` fields of each vehicle. ⏎ To retrieve the product detail fields of your vehicles in an Auto-Inventory catalog or that of your products or services in a generic catalog and check Liệu you need to update the details, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). ⏎ **Note**: Once set, this field cannot be updated. |
| ↳ auto_disclaimer_types | string[] | Chỉ hợp lệ khi the following conditions are met: ⏎ • At the campaign level: • `objective_type` is `LEAD_GENERATION`. • `catalog_enabled` is `true`. • At the ad group level: • An Auto-Model catalog is specified through `catalog_id`. • At the ad level: • `catalog_creative_toggle` is `true.` ⏎ The type of disclaimer to show in the Automotive Carousel Ad for Models. ⏎ Các giá trị enum hỗ trợ: • `EMISSION`: Emission disclaimer. • `DISCOUNT`: Discount or offer disclaimer. ⏎ Kích thước tối đa: 1. ⏎ **Note**: Before using any type of disclaimer, ensure that you have specified the necessary disclaimer details for each vehicle in the Auto-Model catalog. ⏎ • To use the emission disclaimer, ensure that you have provided the following details for each vehicle: • `emission_disclaimer` • `emission_disclaimer_url` • `emission_overlay_disclaimer` • `emission_image_link` • To use the discount or offer disclaimer, ensure that you have provided the following details for each vehicle: • `offer_disclaimer` • `offer_disclaimer_url`To get the attributes of vehicles in an Auto-Model catalog, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). ⏎ To update the attributes of vehicles in an Auto-Model catalog, use [/catalog/product/update/](28-catalog-products-p2.md#doc-1740562287852546). |
| ↳ utm_params | object[] | Valid when `objective_type` is `WEB_CONVERSIONS` at the campaign level. ⏎ A list of URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. ⏎ Max size : 14. ⏎ If you set `landing_page_url` to a URL that already includes URL parameters, you can optionally pass `utm_params` at the same time to store the URL parameters used in the URL. In such cases, you need to ensure that `utm_params` exactly matches the used URL parameters. The URL parameters will not be automatically appended to the `landing_page_url` upon ad delivery. |
| ↳↳ key | string | The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm.Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳↳ value | string | The value of the URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| ↳ fallback_type**(Điều kiện)** | string | Fallback type. ⏎ The destination when the user is unable to access the deeplink because the app has not been installed. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: The promoted web page as fallback URL. You need to simultaneously specify the fallback URL through `landing_page_url_list`. • `APP_INSTALL`: The App Store or Google Play page for the promoted App. ⏎ Liệu this field is required varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact scenarios where this field is required. |
| ↳ product_info | object | Product information. ⏎ This information will be used in different ad variations to create personalized ad delivery with the goal of improving ad performance. Based on past data, ads with complete information often have more clicks and conversions. Results may vary. ⏎ All fields within the `product_info` object are optional. The more detailed information you provide through the parameters, the better the generated ad variations will be. ⏎ To learn about the scenarios where you can use the parameters within this field, see [Available product information settings in Upgraded Smart+ Campaigns](../15-appendix/phu-luc-p2.md#doc-1860735968798721). |
| ↳↳ product_titles | string[] | A list of product names. ⏎ Size range: 0-1. ⏎ Length limit for each product name: 40 characters and cannot contain emoji. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. ⏎ If you don't provide a product name, a default name will be used so that the name won't appear blank. |
| ↳↳ product_image_list | object[] | A list of product images. ⏎ Size range: 0-10. ⏎ If you don't provide a product image, a generic image will be used so that the image won't appear blank. |
| ↳↳↳ web_uri | string | The image ID of a product image. ⏎ Specifications requirements: • Image format: .jpg, .png, .jpeg, or .webp. • File size: no more than 5 MB • Image size: no limit.Recommend image resolution: 800 x 800 pixels. ⏎ To obtain the image ID, use the [/file/image/ad/search/](47-images.md#doc-1740052016789506) or [/file/image/ad/upload/](47-images.md#doc-1739067433456642) endpoint. |
| ↳↳ selling_points | string[] | A list of selling points. ⏎ Kích thước tối đa: 15. ⏎ Each selling point must be 1-25 characters long and cannot contain emoji. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. |
| ↳↳ catalog_tag_list | string[] | Valid in any of the following scenarios: • Scenario 1: At the campaign level `objective_type` is `WEB_CONVERSIONS` and `catalog_type` is `ECOMMERCE`. • Scenario 2:  • At the campaign level `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `true`. • At the ad group level an Auto-Inventory catalog is specified through `catalog_id`. • Scenario 3: • At the campaign level, `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION`, `catalog_enabled` is `true`, and `catalog_type` is `GENERIC`.Details of the product information for catalog ads. • For scenario 1, the specified product information will be automatically displayed from your catalog to drive results. The enum values are: • `PRICE`: Price. • `STRIKETHROUGH_PRICE`: Strikethrough price. • `DISCOUNT`: Discount. • `FREE_SHIPPING`: Free shipping.Giá trị mặc định: `["PRICE", "STRIKETHROUGH_PRICE", "DISCOUNT", "FREE_SHIPPING"]`. ⏎ Kích thước tối đa: 4. • For scenario 2, the corresponding text for the specified product information will be displayed on the inventory card. The enum values are: • `DEALER_NAME`: Dealer name. • `CURRENT_MILEAGE`: Current mileage. • `LEAD_PRICE`: Price. • `LEAD_SALE_PRICE`: Sale price. • `EXTERIOR_COLOR`: Exterior color. • `TRIM`: Trim. • `ADDRESS_CITY`: City. • `VEHICLE_STATE`: Vehicle state.Kích thước tối đa: 2 for primary catalog tags (`DEALER_NAME`,`CURRENT_MILEAGE`,`EXTERIOR_COLOR`,`TRIM`,`ADDRESS_CITY`,`VEHICLE_STATE`) and 2 for secondary catalog tags (`LEAD_PRICE`,`LEAD_SALE_PRICE`). • For scenario 3, the enum values are: • `GENERIC_RATING`: Rating. • `GENERIC_SALE_PRICE`: Sale price. • `GENERIC_PRICE`: Price. • `GENERIC_DESCRIPTION`: Product description. • `GENERIC_ADDRESS_CITY`: City. • `GENERIC_ADDRESS_REGION`: Locations or regions. • `GENERIC_ADDRESS_STREET`: Street address. • `GENERIC_CUSTOM_LABEL_0`: Custom label 0. • `GENERIC_CUSTOM_LABEL_1`: Custom label 1. • `GENERIC_CUSTOM_LABEL_2`: Custom label 2. ⏎ **Note**: For scenario 3: • In [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161) (where `objective_type` is `LEAD_GENERATION`, `catalog_enabled` is `true`, and `catalog_type` is `GENERIC`) , the maximum number of attributes you can specify depends on your selection: • Max size 3: Allowed only if your selection includes both `GENERIC_PRICE` and `GENERIC_SALE_PRICE` (for example, the two price attributes plus one other attribute). • Max size 2: Allowed for all other combinations. |
| ↳↳ product_card_type | string[] | The product card display type. ⏎ Các giá trị enum hỗ trợ: • `PRODUCT_CARD`: Product Card. • `PRODUCT_TILE`: Product Tiles. • `PRODUCT_INFO_CARD`: Info Card. • `PRODUCT_SHOWCASE_TILE`: Showcase Tiles. • `ANCHOR`: Anchor. • `CAROUSEL_LABEL`: Carousel label. ⏎ No Giá trị mặc định. ⏎ **Note**: When you provide this field, you need to include at least one value. |
| ↳↳ promo_info_list | object[] | Valid only for [regular Upgraded Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302878676994). ⏎ Details of promo codes and offers. ⏎ Your offer details for promo codes, offers, or events will be highlighted to boost engagement and ad performance. Promo codes require shoppers to enter a code at checkout. Offers apply automatically and no code is needed. ⏎ Kích thước tối đa: 10. |
| ↳↳↳ discount_type**(Điều kiện)** | string | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳ discount_value**(Điều kiện)** | float | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount value. • When `discount_type` is `PERCENTAGE`, specify an integer between 1-100. • When `discount_type` is `CASH`, specify a float greater than 0. |
| ↳↳↳ discount_currency**(Điều kiện)** | string | Bắt buộc khi `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ promo_code | string | The promo code. • For promo codes that require shoppers to enter a code at checkout, specify the code through this field. • For offers that apply automatically, omit this field. ⏎ Giới hạn độ dài: 30 characters long and cannot contain emoji. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. ⏎ **Note**: Promo codes exclusive to TikTok often perform best. |
| ↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳ minimum_purchase_value**(Điều kiện)** | float | Bắt buộc khi `minimum_purchase_type` is specified. ⏎ Minimum purchase value. • When `minimum_purchase_type` is `QUANTITY`, specify an integer that is 0 or greater. • When `minimum_purchase_type` is `SUBTOTAL`, specify a float greater than 0. |
| ↳↳↳ minimum_purchase_currency**(Điều kiện)** | string | Bắt buộc khi `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. • The `valid_end_time` should be later than the current time. • If you specify `valid_end_time`, provide `valid_start_time` at the same time. |
| ↳ product_info_enabled **(Điều kiện)** | string | The product information mode. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: To disable product information mode. • `NON_CATALOG`: To enable the non-catalog version of product information. • `CATALOG`: To enable the catalog version of product information. ⏎ Giá trị mặc định: `UNSET`. ⏎ To learn about the scenarios where you need to set this parameter, see [Available product information settings in Upgraded Smart+ Campaigns](../15-appendix/phu-luc-p2.md#doc-1860735968798721). ⏎ **Note**:  • This field will automatically be set to `CATALOG` when the following conditions are both met at the campaign level: • `app_promotion_type` is `MINIS`. • `catalog_enabled` is `true`. • This field can only be set to `UNSET` when an Inventory Card portfolio is specified through `card_id` in [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314). |
| ↳ call_to_action_id**(Điều kiện)** | string | The ID of the call-to-action (CTA) portfolio (also known as dynamic CTA) that you want to use in your ads. A CTA portfolio is a group of auto-optimized CTAs. ⏎ For details about auto-optimized CTAs, see [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). ⏎ Liệu this field is required varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact scenarios where this field is required. |
| ↳ phone_info **(Điều kiện)** | object | Bắt buộc khi `promotion_type` is set to `LEAD_GEN_CLICK_TO_CALL` at the ad group level. ⏎ Details of the phone number that the ad audience can directly reach out to you (the advertiser) through when they click the call-to-action button within the ad. ⏎ Learn about how to [create an Upgraded Smart+ Lead Generation Campaign with optimization location as phone call](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302998941697). |
| ↳↳ phone_region_code **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The region code for the phone number that the audience can click on the ad to call. ⏎ Example: `US`. ⏎ To obtain the region code (`phone_region_code`) and region calling code (`phone_region_calling_code`) for the region that is associated with a specific phone number, use [/tool/phone_region_code/](70-tools-p2.md#doc-1774488637039618). |
| ↳↳ phone_region_calling_code **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The region calling code for the phone number that the audience can click on the ad to call. ⏎ Example: `+1`. ⏎ To obtain the region code (`phone_region_code`) and region calling code (`phone_region_calling_code`) for the region that is associated with a specific phone number, use [/tool/phone_region_code/](70-tools-p2.md#doc-1774488637039618). |
| ↳↳ phone_number **(Điều kiện)** | string | Bắt buộc khi `phone_info` is specified. ⏎ The phone number that the audience can click on the ad to call. ⏎ Example: `12638282`. |
| ↳ tracking_info | object | Tracking information. |
| ↳↳ viewability_postbid_partner | string | Post-bid third-party viewability measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. ⏎ **Note**: • Post-bid third-party viewability measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • See [Brand safety](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) to learn about the supported advertising objectives, supported markets, and the general introduction of post-bid measurement. • When you pass in both `brand_safety_postbid_partner` and `viewability_postbid_partner`: • If you set either of these two fields as `IAS`, you need to specify both as `IAS`, and assign the same value (the wrapped VAST URL that you obtain from the measurement partner IAS) to `brand_safety_vast_url` and `viewability_vast_url`. • If you set either of these two fields as `ZEFR`, you need to specify both as `ZEFR`. • If you set two different post-bid measurement partners, only the post-bid brand safety measurement setting will become valid. |
| ↳↳ viewability_vast_url **(Điều kiện)** | string | Bắt buộc khi `viewability_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure viewability. You need to get the URL from the measurement partner IAS. ⏎ **Note**: • Post-bid third-party viewability measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When you set both `brand_safety_postbid_partner` and `viewability_postbid_partner` as IAS, `brand_safety_vast_url` should be the same as `viewability_vast_url`. |
| ↳↳ brand_safety_postbid_partner | string | Post-bid third-party brand safety measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. ⏎ **Note**: • Post-bid third-party brand safety measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • See [Brand safety](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) to learn about the supported advertising objectives, supported markets, and the general introduction of post-bid measurement. • When you pass in both `brand_safety_postbid_partner` and `viewability_postbid_partner`: • If you set either of these two fields as `IAS`, you need to specify both as `IAS`, and assign the same value (the wrapped VAST URL that you obtain from the measurement partner IAS) to `brand_safety_vast_url` and `viewability_vast_url`. • If you set two different post-bid measurement partners, only the post-bid brand safety measurement setting will become valid. |
| ↳↳ brand_safety_vast_url **(Điều kiện)** | string | Bắt buộc khi `brand_safety_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure brand safety. You need to get the URL from the measurement partner IAS. ⏎ **Note**: • Post-bid third-party brand safety measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When you set both `brand_safety_postbid_partner` and `viewability_postbid_partner` as IAS, `brand_safety_vast_url` should be the same as `viewability_vast_url`. |
| ↳↳ impression_tracking_url | string | Default Impression Tracking URL. ⏎ URL generated by your data partner to track impression events in your ads. Generally you can find and copy the URL from their platform. ⏎ • If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). • If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Default Impression Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). |
| ↳↳ click_tracking_url | string | Click Tracking URL. ⏎ URL generated by your data partner to track click events in your ads. Generally you can find and copy the URL from their platform. ⏎ • If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). • If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Click Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).Currently, Pangle does not support DCM, Sizmek or Flashtalking. |
| ↳↳ tracking_app_id | string | Valid when `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION`. ⏎ The ID of the App that you want to track. ⏎ You can use this field to track offsite app events. ⏎ If `app_id` is specified at the ad group level and you want to track offsite app events, then the application ID you pass via this field must be the same ID that you specified at the ad group level. Otherwise, you can pass in any application ID that you'd like to track via this field. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ tracking_pixel_id | string | Valid only in any of the following scenarios: • Scenario 1: At the campaign level, `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. • Scenario 2:  • At the campaign level, `objective_type` is `LEAD_GENERATION`. • At the ad group level, `promotion_target_type` is not set to `EXTERNAL_WEBSITE`. ⏎ The ID of the pixel for tracking the actions people take on your website, such as page views, add to cart, purchases, and more. ⏎ • If `pixel_id` is already set at the ad group level, this `tracking_pixel_id` must match it for tracking website events. • If `pixel_id` is not set at the ad group level, you may specify any ID TikTok Pixel for tracking website events. |
| ↳↳ tracking_offline_event_set_ids | string[] | Chỉ hợp lệ khi the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. ⏎ A list of Offline Event set IDs for tracking customer actions that happen in-person, such as in-store purchases or live event attendance. ⏎ Kích thước tối đa: 50. ⏎ See [here](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193) to learn more about how to create and manage Offline Event sets. ⏎ **Note**: • For a new ad, existing auto-tracking Offline Event sets have to be tracked. You can choose to omit or provide this field. • If you omit this field, it automatically includes all **existing** auto-tracking Offline Event set IDs within your ad account. • If you provide this field, you need to specify all **existing** auto-tracking Offline Event set IDs. Adding non-auto-tracking Offline Event set IDs is optional. To find existing auto-tracking Offline Event sets within an ad account, call [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313) and select sets where `auto_tracking` is `true`. |
| ↳↳ tracking_message_event_set_id | string | Valid when the following conditions are met: • At the ad group level: • `promotion_type` is `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`. • `optimization_goal` is `CLICK`. • `messaging_app_type` is `MESSENGER` or `WHATSAPP`. • At the ad level: • `page_list` is not specified. ⏎ The ID of the message event set that you want to measure in the Instant Messaging Ad. You can use this field to measure when users have started conversation in your instant messaging app. ⏎ To obtain the list of available message event sets, use [/ctm/message_event_set/get/](43-events-1-0-p2.md#doc-1816979158055937). ⏎ To learn more about how to create TikTok Instant Messaging Ads, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302988449921). ⏎ **Note**: Once set, this field cannot be updated. |
| ↳↳ app_tracking_info_list | object[] | Chỉ hợp lệ khi `sales_destination` is `WEB_AND_APP` at the campaign level. ⏎ Details of Third-party tracking settings. ⏎ Kích thước tối đa: 4. |
| ↳↳↳ app_type **(Điều kiện)** | string | Bắt buộc khi `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳↳ app_id **(Điều kiện)** | string | Bắt buộc khi `app_tracking_info_list` is specified. ⏎ The App ID of the App. • When `app_type` is `APP_ANDROID`, specify the App ID for an Android App. • When `app_type` is `APP_IOS`, specify the App ID for an iOS App. |
| ↳↳↳ impression_tracking_url **(Điều kiện)** | string | When `app_type` is specified, specify either `impression_tracking_url` or `click_tracking_url` or both. ⏎ Impression tracking URL. • When `app_type` is `APP_ANDROID`, specify an impression tracking URL for Android. • When `app_type` is `APP_IOS`, specify an impression tracking URL for iOS. |
| ↳↳↳ click_tracking_url **(Điều kiện)** | string | When `app_type` is specified, specify either `impression_tracking_url` or `click_tracking_url` or both. ⏎ Click tracking URL. • When `app_type` is `APP_ANDROID`, specify a click tracking URL for Android. • When `app_type` is `APP_IOS`, specify a click tracking URL for iOS. |

### List of values for `discount_currency` or `minimum_purchase_currency`
The following table lists the enum values for `discount_currency` or `minimum_purchase_currency`.

| Value for discount_currency or minimum_purchase_currency | Currency |
|---|---|
| `AED` | UAE Dirham |
| `ARS` | Argentine Peso |
| `AUD` | Australian Dollar |
| `BDT` | Bangladesh Taka |
| `BHD` | Bahraini Dinar |
| `BOB` | Bolivian Boliviano |
| `BRL` | Brazilian Real |
| `BYN` | Belarusian Ruble |
| `CAD` | Canadian Dollar |
| `CHF` | Swiss Franc |
| `CLP` | Chilean Peso |
| `CNY` | Chinese Yuan |
| `COP` | Colombian Peso |
| `CRC` | Costa Rican Colón |
| `CZK` | Czech Republic Koruna |
| `DKK` | Danish Krone |
| `DZD` | Algerian Dinar |
| `EGP` | Egyptian Pound |
| `EUR` | Euro |
| `GBP` | British Pound |
| `GTQ` | Guatemalan Quetzal |
| `HKD` | Hong Kong Dollar |
| `HNL` | Honduran Lempira |
| `HUF` | Hungarian Forint |
| `IDR` | Indonesian Rupiah |
| `ILS` | New Israeli Shekel |
| `INR` | Indian Rupee |
| `IQD` | Iraqi Dinar |
| `ISK` | Icelandic Króna |
| `JOD` | Jordanian Dinar |
| `JPY` | Japanese Yen |
| `KES` | Kenyan Shilling |
| `KHR` | Cambodian Riel |
| `KRW` | South Korean Won |
| `KWD` | Kuwaiti Dinar |
| `KZT` | Tenge |
| `LBP` | Lebanese Pound |
| `LKR` | Sri Lanka Rupee |
| `MAD` | Moroccan Dirham |
| `MOP` | Pataca |
| `MXN` | Mexican Peso |
| `MYR` | Malaysian Ringgit |
| `NGN` | Nigerian Naira |
| `NIO` | Nicaraguan Cordoba |
| `NOK` | Norwegian Krone |
| `NZD` | New Zealand Dollar |
| `OMR` | Rial Omani |
| `PEN` | Peruvian Sol |
| `PHP` | Philippine Piso |
| `PKR` | Pakistan Rupee |
| `PLN` | Polish ZŁOty |
| `PYG` | Paraguayan Guarani |
| `QAR` | Qatari Rial |
| `RON` | Romanian Leu |
| `RSD` | Serbian Dinar |
| `RUB` | Russian Ruble |
| `SAR` | Saudi Riyal |
| `SEK` | Krona |
| `SGD` | Singapore Dollar |
| `THB` | Thai Baht |
| `TRY` | Turkish Lira |
| `TWD` | New Taiwan Dollar |
| `UAH` | Hryvnia |
| `USD` | US Dollar |
| `UYU` | Peso Uruguayo |
| `VEF` | Venezuelan Bolívar |
| `VND` | Vietnamese Dong |
| `ZAR` | South African Rand |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_id": "{{adgroup_id}}",
    "ad_name": "{{ad_name}}",
    "landing_page_url_list": [
        {
            "landing_page_url": "{{landing_page_url}}"
        }
    ],
    "creative_list": [
        {
            "creative_info": {
                "ad_format":"CAROUSEL_ADS",
                "image_info": [
                    {
                        "web_uri": "{{web_uri}}"
                    }
                ],
                "music_info": {
                    "music_id": "{{music_id}}"
                },
                "identity_type": "TT_USER",
                "identity_id": "{{identity_id}}"
            }
        },
        {
            "creative_info": {
                "ad_format":"SINGLE_VIDEO",
                "video_info": {
                    "video_id": "{{video_id}}"
                },
                "image_info": [
                    {
                        "web_uri": "{{web_uri}}"
                    }
                ],
                "identity_type": "TT_USER",
                "identity_id": "{{identity_id}}"
            }
        },
        {
            "creative_info": {
                "ad_format":"SINGLE_VIDEO",
                "tiktok_item_id": "{{tiktok_item_id}}",
                "identity_type": "TT_USER",
                "identity_id": "{{identity_id}}"
            }
        },
        {
            "creative_info": {
                "ad_format":"SINGLE_VIDEO",
                "tiktok_item_id": "{{tiktok_item_id}}",
                "identity_type": "BC_AUTH_TT",
                "identity_id": "{{identity_id}}",
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}"
            }
        },
        {
            "creative_info": {
                "ad_format":"SINGLE_VIDEO",
                "tiktok_item_id": "{{tiktok_item_id}}",
                "identity_type": "AUTH_CODE",
                "identity_id": "{{identity_id}}"
            }
        }
    ],
    "ad_text_list": [
        {
            "ad_text": "{{ad_text}}"
        },
        {
            "ad_text": "{{ad_text}}"
        },
        {
            "ad_text": "{{ad_text}}"
        },
        {
            "ad_text": "{{ad_text}}"
        },
        {
            "ad_text": "{{ad_text}}"
        }
    ],
    "ad_configuration": {
        "utm_params": [
            {
                "key": "{{key}}",
                "value": "{{value}}"
            }
        ],
        "call_to_action_id": "{{call_to_action_id}}"
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳ campaign_name | string | Campaign name. |
| ↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳ adgroup_name | string | Ad group name. |
| ↳ smart_plus_ad_id | string | ID mẫu quảng cáo. |
| ↳ ad_name | string | Ad name. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad is enabled (in 'ON' status). • `DISABLE`: The ad is disabled (in 'OFF' status). • `FROZEN`: The ad is terminated and cannot be enabled. |
| ↳ secondary_status | string | Ad secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ The following secondary statuses are newly added for Upgraded Smart+ Ads: • `AD_STATUS_DELIVERY_AND_REAUDIT`: Review of modifications in progress. • `AD_STATUS_DELIVERY_AND_TRANSCODING_FAIL`: Transcoding of the video or videos in the ad failed. • `AD_STATUS_REVIEW_PARTIALLY_APPROVED`: Ad in partial review and in delivery. • `AD_STATUS_COLLECTION_TOGGLED_OFF`: Lead collection has ended. • `AD_STATUS_PRIVACY_POLICY_REJECTED`: Ad rejected due to privacy policy violations. • `AD_STATUS_PRIVACY_POLICY_AUDIT`: Ad in review for privacy policy compliance. |
| ↳ create_time | string | The time when the ad was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ modify_time | string | The time when the ad was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ creative_list | object[] | A list of creatives. |
| ↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳↳ smart_plus_creative_id | string | The ID of the creative in the Upgraded Smart+ Ad. ⏎ This ID is the same as the creative ID you retrieve in the following scenarios: • The `ad_id` you receive from [/ad/get/](02-ads-p1.md#doc-1735735588640770) when you do not specify the `ad_ids_v2` filter. • The `ad_id` metric you retrieve from [/report/integrated/get/](58-reporting.md#doc-1740302848100353) when you set `data_level` to `AUCTION_AD` and include `ad_id` in `dimensions`. |
| ↳↳ material_operation_status | string | The status of the creative. ⏎ Các giá trị enum hỗ trợ: • `ENABLE`: The creative is enabled (in 'ON' status). • `DISABLE`: The creative is disabled (in 'OFF' status). |
| ↳↳ creative_info | object | Creative information. |
| ↳↳↳ ad_format | string | The ad format. ⏎ Các giá trị enum hỗ trợ: • `SINGLE_VIDEO`: Single Video. • `CAROUSEL_ADS`: Standard Carousel. • `CATALOG_CAROUSEL`: Catalog Carousel. |
| ↳↳↳ material_name | string | Material name. ⏎ **Note**: If `ad_format` is `CAROUSEL_ADS` and you have set a non-empty custom name for the carousel via `material_name` in the request, this field will return your custom carousel name. |
| ↳↳↳ video_info | object | Video information. |
| ↳↳↳↳ video_id | string | Video ID. |
| ↳↳↳↳ file_name | string | Video name. |
| ↳↳↳ thumbnail_mode | string | The mode of the video thumbnail. ⏎ The thumbnail will be shown as the first image on a search results page. Thumbnails are critical for catching your audience's attention and driving clicks. ⏎ Các giá trị enum hỗ trợ: • `AUTOMATIC`: Smart thumbnail. The system will show a different frame from your video customized for different audiences to closely match what they're searching for and what they're most likely to tap. The video cover specified through `image_info` will be used as the fallback video thumbnail if no matching thumbnails are found. • `MANUAL`: Manual thumbnail. The video cover specified through `image_info` will be used as the video thumbnail. |
| ↳↳↳ image_info | object[] | Image information. |
| ↳↳↳↳ web_uri | string | Image ID. |
| ↳↳↳ music_info | object | Music information. |
| ↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳ aigc_disclosure_type | string | Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content. • `NOT_DECLARED`: To not declare that the ad contains AI-generated content. |
| ↳↳↳ tiktok_item_id | string | The ID of the TikTok post to be used as an ad (Spark Ads). |
| ↳↳↳ identity_type | string | Returned for Spark Ads created without using catalog creatives. ⏎ Identity type. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ identity_id | string | Returned for Spark Ads created without using catalog creatives. ⏎ Identity ID. |
| ↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ playable_list | object[] | A list of playables. |
| ↳↳ playable_url | string | The URL of the playable. |
| ↳ ad_text_list | object[] | A list of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. |
| ↳↳ ad_text | string | Ad text. |
| ↳ auto_message_list | object[] | Returned only when `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` at the ad group level. ⏎ Details of the automatic message to use in a TikTok Direct Messaging Ad. |
| ↳↳↳ auto_message_id | string | Bắt buộc khi `auto_message_list` is specified. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is welcome message. • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ To learn more about how to create TikTok Direct Messaging Ads with welcome messages, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as TikTok direct messages](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302969710913). |
| ↳ call_to_action_list | object[] | Call-to-action list. |
| ↳↳ call_to_action | string | Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ interactive_add_on_list | object[] | A list of interactive add-on (creative portfolio) IDs. |
| ↳↳ card_id | string | The ID of an interactive add-on. |
| ↳ page_list | object[] | A list of pages. |
| ↳↳ page_id | string | Page ID. |
| ↳ landing_page_url_list | object[] | A list of landing page URLs. |
| ↳↳ landing_page_url | string | Landing page URL. |
| ↳ custom_product_page_list | object[] | Details of the custom product page to use in the ad. |
| ↳↳ custom_product_page_url | string | The Custom Product Page (CPP) URL. ⏎ CPPs are product pages with customized screenshots, promotional text, and app previews that can be used to highlight specific content or features of the promoted app, or reach specific audiences. ⏎ Example: `https://apps.apple.com/us/app/tiktok/id835599320?ppid=12345a6b-c789-12d3-e4f5-g6h78i91jk2l`. |
| ↳ deeplink_list | object[] | A list of deeplinks. |
| ↳↳ deeplink | string | Deeplink, the specific location where you want your audience to go if they have your app installed. |
| ↳↳ deeplink_type | string | The deeplink type. ⏎ Các giá trị enum hỗ trợ: • `NORMAL`: non-deferred deeplink. • `DEFERRED_DEEPLINK`: deferred deeplink. |
| ↳ multi_dest_list | object[] | Returned only when `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION` is specified at the ad group level. ⏎ A list of destinations for the Lead Generation ad. |
| ↳↳ dest_type | string | Destination type. ⏎ Các giá trị enum hỗ trợ: • `EXTERNAL_WEBSITE`: Website URL. You need to specify `landing_page_url` simultaneously. • `INSTANT_PAGE`: Instant Form. You need to specify `page_id` simultaneously. • `TT_DIRECT_MESSAGAE`: Message template. You need to specify `auto_message_id` simultaneously. |
| ↳↳ landing_page_url | string | Returned when `dest_type` is `EXTERNAL_WEBSITE`. ⏎ Landing page URL. |
| ↳↳ page_id | string | Returned when `dest_type` is `INSTANT_PAGE`. ⏎ The ID of an Instant Form. |
| ↳↳ auto_message_id | string | Returned when `dest_type` is `TT_DIRECT_MESSAGAE`. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. |
| ↳ disclaimer | object | Disclaimer information. |
| ↳↳ disclaimer_type | string | The type of disclaimer in the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_ONLY`: text-only disclaimer. • `TEXT_LINK`: clickable disclaimer. |
| ↳↳ disclaimer_text | object | The text-only disclaimer in the ad. |
| ↳↳↳ text | string | The disclaimer text. |
| ↳↳ disclaimer_clickable_texts | object[] | The clickable disclaimer or clickable disclaimers in the ad. |
| ↳↳↳ text | string | The disclaimer text. |
| ↳↳↳ url | string | The URL for the clickable disclaimer. ⏎ When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ↳ ad_configuration | object | Additional configurations. |
| ↳↳ identity_type | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ Identity type. • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ identity_id | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ Identity ID. |
| ↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ dark_post_status | string | The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. |
| ↳↳ product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products. • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. • `UNSET`: Unset. |
| ↳↳ product_set_id | string | The ID of a product set. |
| ↳↳ product_ids | string[] | The product IDs of catalog products. |
| ↳↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ catalog_creative_info | object | Additional settings for catalog creatives to use in your ads. |
| ↳↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce, entertainment, generic, or online-to-offline catalog to use in the ad. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates. • `MULTI_SHOW`: Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact supported values for your scenario. |
| ↳↳↳ catalog_template_video_id | string | The ID of a video template in your catalog to use in the ad. |
| ↳↳ creative_auto_add_toggle | boolean | Có thực hiện auto-add newly generated assets during delivery. ⏎ During your campaign, the system will generate new creative assets from your existing campaign assets and creative library. By using TikTok's latest trending elements (hooks, music, text, and more), you'll get high-quality, ready-to-use content that delivers alongside your other selected assets. ⏎ New assets will be added to your campaign automatically and won't appear on your TikTok profile. You can turn off this feature anytime. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ creative_auto_enhancement_strategy_list | string[] | The list of automatic enhancement strategies to apply to your ads. ⏎ Automatic enhancements are real-time edits applied to your ads during your campaign. They can improve performance by creating more engaging and impactful visuals, sound, and more. ⏎ Các giá trị enum hỗ trợ: • `TRANSLATE_AND_DUB`: Translate and dub. Connect with global audiences by delivering your ad in 50+ languages. • `MUSIC_REFRESH`: Music refresh. Stay on-trend by swapping in music currently popular on TikTok. • `VIDEO_QUALITY`: Video quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_QUALITY`: Image quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_RESIZE`: Resize. Resize your image to take advantage of full-screen capabilities. |
| ↳↳ deeplink_utm_params | object[] | A list of deeplink URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳ key | string | The deeplink URL parameter. ⏎ It can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. |
| ↳↳↳ value | string | The value of the deeplink URL parameter. ⏎ It can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳ end_card_cta | string | Call-to-action for the end card (`image_ids`) of an Upgraded Smart+ [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873), or [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). ⏎ Các giá trị enum hỗ trợ: • `SEARCH_INVENTORY` (Recommended): Search inventory. • `LEARN_MORE`: Learn more. • `SHOP_NOW`: Shop now. • `SIGN_UP`: Sign up. • `CONTACT_US`: Contact us. • `BOOK_NOW`: Book now. • `READ_MORE`: Read more. • `VIEW_MORE`: View now. • `ORDER_NOW`: Order now. • `SEND_MESSAGE`: Send message. • This value is only available for [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). |
| ↳↳ product_display_field_list | string[] | A list of product details to display in your [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161). ⏎ Enum values for Automotive Carousel Ad for Inventory: • `DEALER_NAME`: the `dealer_name` field of vehicles. • `MAKE`: the `make` field of vehicles. • `MODEL`: the `model` field of vehicles. • `YEAR`: the `year` field of vehicles. • `MILEAGE`: the `mileage` field of vehicles. • `PRICE`: the `price` field of vehicles. • `SALE_PRICE`: the `sale_price` field of vehicles. • `EXTERIOR_COLOR`: the `exterior_color` field of vehicles. • `TRIM`: the `trim` field of vehicles. • `ADDRESS_CITY`: the `city` field of vehicles. • `VEHICLE_STATE`: the `state_of_vehicle` field of vehicles. ⏎ Enum values for Upgraded Smart+ Lead Generic Catalog Ads: • `RATING`: the `rating` field of generic products or services. • `SALE_PRICE`: the `sale_price` field of generic products or services. • `PRICE`: the `price` field of generic products or services. • `DESCRIPTION`: the `description` field of generic products or services. • `ADDRESS_CITY`: the `address.city` field of generic products or services. • `ADDRESS_REGION`: the `address.region` field of generic products or services. • `ADDRESS_STREET`: the `address.street` field of generic products or services. • `CUSTOM_LABEL_0`: the `custom_label_0` field of generic products or services. • `CUSTOM_LABEL_1`: the `custom_label_1` field of generic products or services. • `CUSTOM_LABEL_2`: the `custom_label_2` field of generic products or services. ⏎ The title of each vehicle, product, or service is displayed automatically. For instance, if you set this field to `["MILEAGE","YEAR"]`, the ad will display the `mileage`, `price` and `title` fields of each vehicle. ⏎ To retrieve the product detail fields of your vehicles  in an Auto-Inventory catalog or that of your products or services in a generic catalog and check Liệu you need to update the details, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳↳ auto_disclaimer_types | string[] | The type of disclaimer to show in the [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873). ⏎ Các giá trị enum hỗ trợ: • `EMISSION`: Emission disclaimer. • `DISCOUNT`: Discount or offer disclaimer. |
| ↳↳ utm_params | object[] | A list of URL parameters. ⏎ URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳ key | string | The URL parameter. ⏎ The parameter can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm.Note that UTM parameters are case-sensitive. |
| ↳↳↳ value | string | The value of the URL parameter. ⏎ The value can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳ fallback_type | string | Fallback type. ⏎ The destination when the user is unable to access the deeplink because the app has not been installed. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: The promoted web page as fallback URL. You need to simultaneously specify the fallback URL through `landing_page_url_list`. • `APP_INSTALL`: The App Store or Google Play page for the promoted App. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact supported values for your scenario. |
| ↳↳ product_info | object | Product information. ⏎ This information will be used in different ad variations to create personalized ad delivery with the goal of improving ad performance. Based on past data, ads with complete information often have more clicks and conversions. Results may vary. |
| ↳↳↳ product_titles | string[] | A list of product names. |
| ↳↳↳ product_image_list | object[] | A list of product images. |
| ↳↳↳↳ web_uri | string | The image ID of a product image. |
| ↳↳↳ selling_points | string[] | A list of selling points. |
| ↳↳↳ catalog_tag_list | string[] | Returned in any of the following scenarios: • Scenario 1: At the campaign level `objective_type` is `WEB_CONVERSIONS` and `catalog_type` is `ECOMMERCE`. • Scenario 2:  • At the campaign level, `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `true`. • At the ad group level, an Auto-Inventory catalog is specified through `catalog_id`. • Scenario 3: • At the campaign level, `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION`, `catalog_enabled` is `true`, and `catalog_type` is `GENERIC`.Details of the product information for catalog ads. • For scenario 1, the specified product information will be automatically displayed from your catalog to drive results. The enum values are: • `PRICE`: Price. • `STRIKETHROUGH_PRICE`: Strikethrough price. • `DISCOUNT`: Discount. • `FREE_SHIPPING`: Free shipping. • For scenario 2, the corresponding text for the specified product information will be displayed on the inventory card. The enum values are: • `DEALER_NAME`: Dealer name. • `CURRENT_MILEAGE`: Current mileage. • `LEAD_PRICE`: Price. • `LEAD_SALE_PRICE`: Sale price. • `EXTERIOR_COLOR`: Exterior color. • `TRIM`: Trim. • `ADDRESS_CITY`: City. • `VEHICLE_STATE`: Vehicle state. • For scenario 3, the enum values are: • `GENERIC_RATING`: Rating. • `GENERIC_SALE_PRICE`: Sale price. • `GENERIC_PRICE`: Price. • `GENERIC_DESCRIPTION`: Product description. • `GENERIC_ADDRESS_CITY`: City. • `GENERIC_ADDRESS_REGION`: Locations or regions. • `GENERIC_ADDRESS_STREET`: Street address. • `GENERIC_CUSTOM_LABEL_0`: Custom label 0. • `GENERIC_CUSTOM_LABEL_1`: Custom label 1. • `GENERIC_CUSTOM_LABEL_2`: Custom label 2. |
| ↳↳↳ product_card_type | string[] | The product card display type. ⏎ Các giá trị enum hỗ trợ: • `PRODUCT_CARD`: Product Card. • `PRODUCT_TILE`: Product Tiles. • `PRODUCT_INFO_CARD`: Info Card. • `PRODUCT_SHOWCASE_TILE`: Showcase Tiles. • `ANCHOR`: Anchor. • `CAROUSEL_LABEL`: Carousel label. |
| ↳↳↳ promo_info_list | object[] | Returned only for [regular Upgraded Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302878676994). ⏎ Details of promo codes and offers. ⏎ Your offer details for promo codes, offers, or events will be highlighted to boost engagement and ad performance. Promo codes require shoppers to enter a code at checkout. Offers apply automatically and no code is needed. |
| ↳↳↳↳ discount_type | string | Returned only when `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳↳ discount_value | float | Returned when `promo_info_list` is specified. ⏎ Discount value. |
| ↳↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳ promo_code | string | The promo code. |
| ↳↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳↳ minimum_purchase_value | float | Returned only when `minimum_purchase_type` is specified. ⏎ Minimum purchase value. |
| ↳↳↳↳ minimum_purchase_currency | string | Returned only when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ product_info_enabled | string | The product information mode. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: To disable product information mode. • `NON_CATALOG`: To enable the non-catalog version of product information. • `CATALOG`: To enable the catalog version of product information. |
| ↳↳ call_to_action_id | string | The ID of the call-to-action portfolio to use in your ad. |
| ↳↳ phone_info | object | Returned only when `promotion_type` is set to `LEAD_GEN_CLICK_TO_CALL` at the ad group level. ⏎ Details of the phone number that the ad audience can directly reach out to you (the advertiser) through when they click the call-to-action button within the ad. ⏎ Learn about how to [create an Upgraded Smart+ Lead Generation Campaign with optimization location as phone call](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302998941697). |
| ↳↳↳ phone_region_code | string | The region code for the phone number that the audience can click on the ad to call. ⏎ Example: `US`. |
| ↳↳↳ phone_region_calling_code | string | The region calling code for the phone number that the audience can click on the ad to call. ⏎ Example: `+1`. |
| ↳↳↳ phone_number | string | The phone number that the audience can click on the ad to call. ⏎ Example: `12638282`. |
| ↳↳ tracking_info | object | Tracking information. |
| ↳↳↳ viewability_postbid_partner | string | Post-bid third-party viewability measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳↳ viewability_vast_url | string | Returned when `viewability_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure viewability. You need to get the URL from the measurement partner IAS. |
| ↳↳↳ brand_safety_postbid_partner | string | Post-bid third-party brand safety measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳↳ brand_safety_vast_url | string | Returned when `brand_safety_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure brand safety. You need to get the URL from the measurement partner IAS. |
| ↳↳↳ impression_tracking_url | string | Default Impression Tracking URL. |
| ↳↳↳ click_tracking_url | string | Click Tracking URL. |
| ↳↳↳ tracking_app_id | string | The ID of the app that is measured. |
| ↳↳↳ tracking_pixel_id | string | The ID of the pixel for tracking the actions people take on your website, such as page views, add to cart, purchases, and more. |
| ↳↳↳ tracking_offline_event_set_ids | string[] | A list of Offline Event set IDs for tracking customer actions that happen in-person, such as in-store purchases or live event attendance. |
| ↳↳↳ tracking_message_event_set_id | string | The ID of the message event set that you want to measure in the Instant Messaging Ad. |
| ↳↳↳ app_tracking_info_list | object[] | Details of Third-party tracking settings. |
| ↳↳↳↳ app_type | string | Returned when `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳↳↳ app_id | string | Returned when `app_tracking_info_list` is specified. ⏎ The App ID of the App. • When `app_type` is `APP_ANDROID`, this field represents the App ID for an Android App. • When `app_type` is `APP_IOS`, this field represents the App ID for an iOS App. |
| ↳↳↳↳ impression_tracking_url | string | Impression tracking URL. • When `app_type` is `APP_ANDROID`, this field represents an impression tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents an impression tracking URL for iOS. |
| ↳↳↳↳ click_tracking_url | string | Click tracking URL. • When `app_type` is `APP_ANDROID`, this field represents a click tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents a click tracking URL for iOS. |
| page_info | object | Pagination information. |
| ↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳ page_size | number | Page size. |
| ↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳ total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "ad_configuration": {
            "call_to_action_id": "{{call_to_action_id}}",
            "tracking_info": {},
            "utm_params": [
                {
                    "key": "{{key}}",
                    "value": "{{value}}"
                }
            ]
        },
        "ad_name": "{{ad_name}}",
        "ad_text_list": [
            {
                "ad_text": "{{ad_text}}"
            },
            {
                "ad_text": "{{ad_text}}"
            },
            {
                "ad_text": "{{ad_text}}"
            },
            {
                "ad_text": "{{ad_text}}"
            },
            {
                "ad_text": "{{ad_text}}"
            }
        ],
        "adgroup_id": "{{adgroup_id}}",
        "adgroup_name": "{{adgroup_name}}",
        "advertiser_id": "{{advertiser_id}}",
        "call_to_action_list": [],
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "create_time": "{{create_time}}",
        "creative_list": [
            {
                "ad_material_id": "{{ad_material_id}}",
                "creative_info": {
                    "ad_format":"SINGLE_VIDEO",
                    "identity_authorized_bc_id": "0",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER",
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "material_name": "",
                    "video_info": {
                        "file_name": "",
                        "video_id": "{{video_id}}"
                    }
                },
                "material_operation_status": "ENABLE"
            },
            {
                "ad_material_id": "{{ad_material_id}}",
                "creative_info": {
                    "ad_format":"SINGLE_VIDEO",
                    "identity_authorized_bc_id": "0",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER",
                    "tiktok_item_id": "{{tiktok_item_id}}"
                },
                "material_operation_status": "ENABLE"
            },
            {
                "ad_material_id": "{{ad_material_id}}",
                "creative_info": {
                    "ad_format":"SINGLE_VIDEO",
                    "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "BC_AUTH_TT",
                    "tiktok_item_id": "{{tiktok_item_id}}"
                },
                "material_operation_status": "ENABLE"
            },
            {
                "ad_material_id": "{{ad_material_id}}",
                "creative_info": {
                    "ad_format":"CAROUSEL_ADS",
                    "identity_authorized_bc_id": "0",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER",
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "material_name": "{{material_name}}",
                    "music_info": {
                        "music_id": "{{music_id}}"
                    }
                },
                "material_operation_status": "ENABLE"
            },
            {
                "ad_material_id": "{{ad_material_id}}",
                "creative_info": {
                    "ad_format":"SINGLE_VIDEO",
                    "identity_authorized_bc_id": "0",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "AUTH_CODE",
                    "tiktok_item_id": "{{tiktok_item_id}}"
                },
                "material_operation_status": "ENABLE"
            }
        ],
        "deeplink_list": [],
        "interactive_add_on_list": [],
        "landing_page_url_list": [
            {
                "landing_page_url": "{{landing_page_url}}"
            }
        ],
        "modify_time": "{{modify_time}}",
        "operation_status": "ENABLE",
        "page_list": [],
        "secondary_status": "AD_STATUS_AUDIT",
        "smart_plus_ad_id": "{{smart_plus_ad_id}}"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 5/7**:

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

