# Smart+ nâng cấp (Upgraded Smart+) — phần 6/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Cập nhật quảng cáo Smart+ nâng cấp (#doc-1843317411665921)](#doc-1843317411665921)
- [2. Cập nhật trạng thái hoạt động của quảng cáo Smart+ nâng cấp (#doc-1843317423164482)](#doc-1843317423164482)
- [3. Bật hoặc tắt mẫu sáng tạo trong quảng cáo Smart+ nâng cấp (#doc-1843317433577601)](#doc-1843317433577601)
- [4. Xem trước quảng cáo Smart+ nâng cấp (#doc-1843317445798914)](#doc-1843317445798914)
- [5. Xét duyệt quảng cáo (#doc-1843310536069122)](#doc-1843310536069122)
- [6. Lấy thông tin xét duyệt của quảng cáo Smart+ nâng cấp (#doc-1843317465695233)](#doc-1843317465695233)
- [7. Lấy thông tin xét duyệt mẫu sáng tạo của quảng cáo Smart+ nâng cấp (#doc-1843317474334722)](#doc-1843317474334722)
- [8. Kháng nghị từ chối duyệt quảng cáo Smart+ nâng cấp (#doc-1843317522553106)](#doc-1843317522553106)
- [9. Báo cáo (#doc-1843310542601218)](#doc-1843310542601218)
- [10. Chạy báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp (#doc-1843317489576961)](#doc-1843317489576961)
- [11. Các chiều dữ liệu hỗ trợ cho báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp (#doc-1843337892165889)](#doc-1843337892165889)

---

<a id="doc-1843317411665921"></a>
<!-- doc_id: 1843317411665921 -->
<!-- doc_id: 1843317411665921 -->
# Cập nhật quảng cáo Smart+ nâng cấp (Update an Upgraded Smart+ Ad)
> Đường dẫn: API Reference > Upgraded Smart+ > Ads > Update an Upgraded Smart+ Ad
Sử dụng endpoint này để cập nhật quảng cáo Smart+ nâng cấp (Upgraded Smart+ Ad).

Endpoint này hỗ trợ cập nhật tăng dần (incremental updates).

> **Quan trọng:** 
> Việc tạo Non-Spark Ads sử dụng Danh tính tùy chỉnh (Custom Identity) trong các nhóm quảng cáo phân phối đến Vị trí tự động (Automatic Placement) hoặc Vị trí chọn lọc (Select Placement) có bao gồm TikTok hiện không còn được hỗ trợ cho các tài khoản quảng cáo hiện có. Tất cả các tài khoản quảng cáo mới được tạo vào hoặc sau ngày 15 tháng 1 năm 2026 không thể tạo Non-Spark Ads bằng Danh tính tùy chỉnh cho các vị trí này. Các quảng cáo hiện có vẫn không bị ảnh hưởng và có thể chỉnh sửa. Các chiến dịch quảng cáo chỉ phân phối đến vị trí Pangle hoặc Global App Bundle không bị ảnh hưởng bởi việc ngừng hỗ trợ Danh tính tùy chỉnh. Tìm hiểu thêm [về những thay đổi sắp tới đối với Danh tính tùy chỉnh](https://ads.tiktok.com/help/article/about-changes-coming-to-custom-identity) và [chuyển sang Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1848048566169730).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Giá trị được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| smart_plus_ad_id  ****(Bắt buộc)**** | string | ID mẫu quảng cáo. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |
| ad_name | string | Tên mẫu quảng cáo. ⏎ Giới hạn độ dài: 512 ký tự và không được chứa emoji. ⏎ Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi ký tự tiếng Anh tính là 1 ký tự. |
| creative_list | object[] | Danh sách các mẫu sáng tạo. ⏎ Số lượng trong khoảng: 1-50. ⏎ **Lưu ý**: Chế độ cập nhật của tham số `creative_list` là thay thế toàn bộ (full replacement). Ngay cả khi bạn chỉ muốn cập nhật một trường bên trong, bạn vẫn cần chỉ định tất cả các trường trong `creative_list`. |
| ↳ ad_material_id | string | ID tài nguyên cụ thể của mẫu sáng tạo hiện có trong quảng cáo. ⏎ The ID is generated when a particular creative is used in an ad and differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. ⏎ When you provide this field, the API preserves your existing creative throughout the update and prevents the creation of a new one. Using `ad_material_id` to update your Upgraded Smart+ Ads helps you streamline non-creative ad modifications and saves you the effort of re-entering all the `creative_info` parameters. ⏎ **Note**:  • Using `ad_material_id` to update Upgraded Smart+ Ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When both `creative_info` and `ad_material_id` are specified, `creative_info` will be ignored. |
| ↳ creative_info | object | Thông tin mẫu sáng tạo. ⏎ **Lưu ý**: Khi cả `creative_info` và `ad_material_id` đều được chỉ định, `creative_info` sẽ bị bỏ qua. |
| ↳↳ ad_format | string | Định dạng quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `SINGLE_VIDEO`: Video đơn (Single Video). • To use this format, specify any of the following: • a video through `video_id` and a video cover through `web_uri` • a TikTok video post through `tiktok_item_id`. • `CAROUSEL_ADS`: Nhóm hình ảnh xoay vòng tiêu chuẩn (Standard Carousel). • To use this format, specify any of the following: • carousel images through `web_uri` and a piece of music through `music_id`. • TikTok photo posts images through `tiktok_item_id`. • `CATALOG_CAROUSEL`: Nhóm hình ảnh xoay vòng danh mục (Catalog Carousel). • To use this format in Upgraded Smart+ Web Catalog Carousel Ads, specify a piece of music through `music_id`. • To use this format in Upgraded Smart+ Automotive Catalog Carousel Ads, specify a piece of music through `music_id` and an end card through `web_uri`. |
| ↳↳ material_name | string | Chỉ hợp lệ khi `ad_format` là `CAROUSEL_ADS`. ⏎ Tên tùy chỉnh cho nhóm quảng cáo xoay vòng (carousel). ⏎ Giới hạn độ dài: 255 characters. ⏎ Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi ký tự tiếng Anh tính là 1 ký tự. ⏎ **Note**:  • If you have set a custom carousel name during ad creation and want to retain it during an update, specify `ad_material_id` (recommended) or manually pass the same name via this field. • Otherwise, the system overwrites your custom name with an auto-generated one (formatted as `Image carousel X`, where `X` is an incremental integer) if: • You omit `ad_material_id` and do not pass the same custom carousel name in this field. • You omit `ad_material_id` and set this field to null or an empty string (`""`). |
| ↳↳ video_info | object | Thông tin video. |
| ↳↳↳ video_id **(Điều kiện)** | string | Bắt buộc khi `video_info` được chỉ định. ⏎ ID video. ⏎ Để tải lên video và lấy ID video, sử dụng [/file/video/ad/upload/](71-video.md#doc-1737587322856449). ⏎ Để tìm kiếm video trong tài khoản quảng cáo, sử dụng [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| ↳↳↳ file_name | string | Tên video. |
| ↳↳ thumbnail_mode | string | Chỉ hợp lệ khi tất cả các điều kiện sau đều được thỏa mãn: • At the campaign level, `is_search_campaign` is `true`. • At the ad level, `video_info` is specified. ⏎ The mode of the video thumbnail. ⏎ Hình thu nhỏ sẽ hiển thị dưới dạng hình ảnh đầu tiên trên trang kết quả tìm kiếm. Hình thu nhỏ đóng vai trò quan trọng trong việc thu hút sự chú ý của đối tượng và thúc đẩy lượt nhấp. ⏎ Các giá trị enum hỗ trợ: • `AUTOMATIC`: Hình thu nhỏ thông minh (Smart thumbnail). The system will show a different frame from your video customized for different audiences to closely match what they're searching for and what they're most likely to tap. You need to manually specify a video cover through `image_info`, which will be used as the fallback video thumbnail if no matching thumbnails are found. • `MANUAL`: Hình thu nhỏ thủ công (Manual thumbnail). You need to manually specify a video cover through `image_info`, which will be used as the video thumbnail. ⏎ Theo mặc định, chế độ hình thu nhỏ video là hình thu nhỏ thủ công (manual thumbnail). |
| ↳↳ image_info | object[] | Thông tin hình ảnh. |
| ↳↳↳ web_uri **(Điều kiện)** | string | Bắt buộc khi `image_info` được chỉ định. ⏎ ID hình ảnh. ⏎ Để tải lên hình ảnh và lấy ID hình ảnh, sử dụng [/file/image/ad/upload/](47-images.md#doc-1739067433456642). ⏎ Để tìm kiếm hình ảnh trong tài khoản quảng cáo, sử dụng [/file/image/ad/search/](47-images.md#doc-1740052016789506). |
| ↳↳ music_info **(Điều kiện)** | object | Bắt buộc khi `catalog_creative_toggle` is `true`. ⏎ Thông tin âm nhạc. |
| ↳↳↳ music_id **(Điều kiện)** | string | Bắt buộc khi `music_info` được chỉ định. ⏎ ID của đoạn nhạc sử dụng trong quảng cáo xoay vòng (carousel). |
| ↳↳ aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` trong `ad_configuration` là `CUSTOMIZED_USER`. ⏎ Có bật nút tự khai báo nội dung do AI tạo (AIGC - Artificial Intelligence Generated Content) để biểu thị quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo của bạn sẽ gắn nhãn "Nhà quảng cáo gắn nhãn do AI tạo" khi xem toàn màn hình. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: Bật nút khai báo quảng cáo có chứa nội dung do AI tạo. • `NOT_DECLARED`: Không khai báo quảng cáo có chứa nội dung do AI tạo. ⏎ To learn about the supported advertising objectives and ad formats for the toggle and the detailed steps for using the toggle, see [AIGC self-disclosure toggle](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). |
| ↳↳ tiktok_item_id | string | ID của bài đăng TikTok dùng làm quảng cáo (Spark Ads). ⏎ Truyền vào `item_id` nhận được từ phản hồi của endpoint [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) và [/identity/video/get/](46-identity.md#doc-1740218475032577). ⏎ Khi bạn truyền `tiktok_item_id`, bạn không cần truyền các đối tượng `image_info`, `video_info` và `title_list`. ⏎ **Lưu ý**: Khi sử dụng Spark Ads, bạn xác nhận rằng mình có quyền sử dụng âm nhạc trong video cho mục đích thương mại. |
| ↳↳ identity_type | string | Hợp lệ khi bạn tạo Spark Ads mà không dùng mẫu sáng tạo danh mục. ⏎ Loại danh tính (identity type). ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). ⏎ **Note**:  • If you want to create Spark Ads using catalog creatives, specify the `identity_type` and `identity_id` within `ad_configuration`. • If this field is set to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE` and the following conditions are both met, you need to specify a dynamic CTA via `call_to_action_id`. • At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳↳ identity_id | string | Hợp lệ khi bạn tạo Spark Ads mà không dùng mẫu sáng tạo danh mục. ⏎ ID danh tính. ⏎ **Note**: If you want to create Spark Ads using catalog creatives, specify the `identity_type` and `identity_id` within `ad_configuration`. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| playable_list | object[] | Chỉ hợp lệ trong bất kỳ trường hợp nào sau đây: • Scenario 1: • At the campaign level, `objective_type` is `APP_PROMOTION`. • At the ad group level, the placement is not Global Apple Bundle-only (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_GLOBAL_APP_BUNDLE"]`) . • At the ad level, `ad_format` is `SINGLE_VIDEO` and a video or video post is specified. • Scenario 2: • At the campaign level, `objective_type` is `APP_INSTALL`. • At the ad group level: • `promotion_type` is `MINI_GAME`. • The placement is not Global Apple Bundle-only (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_GLOBAL_APP_BUNDLE"]`) . • At the ad level, `ad_format` is `SINGLE_VIDEO` and a video or video post is specified. ⏎ The list of playables. ⏎ Kích thước tối đa: 5. ⏎ **Note**: The Playable Ad is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ playable_url | string | URL của mẫu quảng cáo tương tác (playable). • To upload playables to the Creative Library of your ad account and obtain the playable URLs, see [Upload playables](../09-marketing-api/creatives.md#doc-1868153086739601). • To obtain the URLs of existing playables within your ad account, use [/playable/get/](56-playable-ads.md#doc-1737732758495234). ⏎ **Note**: If you want to create Playable Ads using TikTok-only placement (with `placement_type` as `PLACEMENT_TYPE_NORMAL` and `placements` as `["PLACEMENT_TIKTOK"]`), ensure the playables are not horizontal. To verify the orientation of your playable, use [/playable/get/](56-playable-ads.md#doc-1737732758495234) and confirm that the `playable_orientation` is either `BOTH` or `PORTRAIT`. |
| ad_text_list | object[] | List of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. ⏎ Kích thước tối đa: 5. |
| ↳ ad_text **(Điều kiện)** | string | Bắt buộc khi `ad_text_list` is specified. ⏎ Ad text. |
| call_to_action_list | object[] | Danh sách lời kêu gọi hành động (CTA). ⏎ Kích thước tối đa: 3. ⏎ Liệu this field is supported varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact scenarios where this field is supported. |
| ↳ call_to_action **(Điều kiện)** | string | Bắt buộc khi `call_to_action_list` is specified. ⏎ Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| interactive_add_on_list | object[] | Danh sách các tiện ích bổ sung tương tác (interactive add-on) (creative portfolio) IDs. ⏎ Size range: 0-1. |
| ↳ card_id | string | ID của một tiện ích bổ sung tương tác. ⏎ Pass the ID of one of the following creative portfolio types: • Display Card. • Countdown Sticker. • Gift Code Sticker. • Inventory Card (for [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314)). ⏎ To create a creative portfolio, use [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426). ⏎ • To learn about how to get the ID of a Display Card or Inventory Card portfolio, see [Cards](../09-marketing-api/creatives.md#doc-1749019652141058). • To learn about how to get the ID of a Countdown Sticker or Giftcode Sticker portfolio, see [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177). |
| page_list | object[] | Danh sách các trang. ⏎ Size range: 0-3. |
| ↳ page_id | string | Page ID. ⏎ • To obtain pages within your ad account, use [/page/get/](54-page.md#doc-1820826387779586). • To create instant pages, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881). |
| landing_page_url_list | object[] | Danh sách URL trang đích. ⏎ Size range: 0-1. |
| ↳ landing_page_url **(Điều kiện)** | string | Bắt buộc khi `landing_page_url_list` is specified. ⏎ Landing page URL. |
| custom_product_page_list | object[] | Chỉ hợp lệ khi tất cả các điều kiện sau đều được thỏa mãn: • At the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • `is_search_campaign` is `false`. • At the ad group level: • An iOS app is specified via `app_id`. ⏎ Details of the custom product page to use in the ad. ⏎ Size range: 0-1. |
| ↳ custom_product_page_url | string | URL Trang sản phẩm tùy chỉnh (Custom Product Page - CPP). ⏎ CPPs are product pages with customized screenshots, promotional text, and app previews that can be used to highlight specific content or features of the promoted app, or reach specific audiences. Only users with iOS 15+ will be able to open a custom product page. ⏎ The CPP URL must be consistent with the promoted app (`app_id`) at the ad group level. ⏎ Format: `https://apps.apple.com/{region}/app/{app_name}/id{app_id}?ppid={ppid}`. ⏎ Giới hạn độ dài: 512 characters. ⏎ Example: `https://apps.apple.com/us/app/tiktok/id835599320?ppid=12345a6b-c789-12d3-e4f5-g6h78i91jk2l`. ⏎ To learn about how to create Custom Product Pages in the Apple App Store and obtain the corresponding CPP URLs, see [Custom product pages on the App Store](https://developer.apple.com/app-store/custom-product-pages/). |
| deeplink_list | object[] | Danh sách liên kết sâu (deeplink). ⏎ Size range: 0-1. |
| ↳ deeplink | string | Deeplink, the specific location where you want your audience to go if they have your app installed. |
| ↳ deeplink_type | string | Loại liên kết sâu (deeplink). ⏎ Enum value: `DEFERRED_DEEPLINK`. ⏎ If you pass this field, you should also provide the `deeplink` field. |
| multi_dest_list | object[] | Chỉ hợp lệ khi `promotion_type` là `LEAD_GENERATION_MULTI_DESTINATION` is specified at the ad group level. ⏎ A list of destinations for the Lead Generation ad. ⏎ To learn about the ad type where this field can be used, see [Create an Upgraded Smart+ Lead Generation Campaign with multiple location selection](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1876685025962241). |
| ↳ dest_type **(Điều kiện)** | string | Bắt buộc khi `multi_dest_list` is specified. ⏎ Loại đích đến. ⏎ Các giá trị enum hỗ trợ: • `EXTERNAL_WEBSITE`: Website URL. You need to specify `landing_page_url` simultaneously. • `INSTANT_PAGE`: Instant Form. You need to specify `page_id` simultaneously. • `TT_DIRECT_MESSAGAE`: Message template. You need to specify `auto_message_id` simultaneously. ⏎ **Note**: This field cannot be updated. If specified, this field must match the value you set during ad group creation. |
| ↳ landing_page_url **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `EXTERNAL_WEBSITE`. ⏎ Landing page URL. |
| ↳ page_id **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `INSTANT_PAGE`. ⏎ The ID of an Instant Form. • To obtain the page IDs of Instant Forms within your ad account, use [/page/get/](54-page.md#doc-1820826387779586) and set `business_type` to `LEAD_GEN`. • To create an Instant Form, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881) and set `businessType` to `1`. |
| ↳ auto_message_id **(Điều kiện)** | string | Bắt buộc khi `dest_type` is `TT_DIRECT_MESSAGAE`. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is message template (welcome message). • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ **Note**: This field cannot be updated. If specified, this field must match the value you set during ad group creation. |
| disclaimer | object | Chỉ hợp lệ khi cả hai điều kiện sau đều được thỏa mãn: • At the campaign level, `objective_type` is `APP_PROMOTION`, `WEB_CONVERSIONS`, or `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `false` or not specified. • At the ad group level, the TikTok placement is included. You can use any of the following configurations: • **Automatic Placement**: Leave `placement_type` and `placements` unspecified. • **Select specific placements** with TikTok included: Set `placement_type` to `PLACEMENT_TYPE_NORMAL` and include `PLACEMENT_TIKTOK` in the value for `placements`.Disclaimer information. ⏎ **Note**:  • You cannot remove a disclaimer that was previously added during ad creation, nor can you change its `disclaimer_type` between `TEXT_ONLY` and `TEXT_LINK`. • You can only add a new disclaimer to an ad that does not already have one, or update the `text` (and `url`, if applicable) of an existing disclaimer. |
| ↳ disclaimer_type **(Điều kiện)** | string | Bắt buộc khi `disclaimer` is specified. ⏎ The type of disclaimer that you want to add to the ad. ⏎ You can add a disclaimer to ensure your ad remains compliant with local and regional policies. ⏎ Các giá trị enum hỗ trợ: • `TEXT_ONLY`: text-only disclaimer.  • `TEXT_LINK`: clickable disclaimer. ⏎ See [Include disclaimers in ads](../09-marketing-api/creatives.md#doc-1739953274550273) to learn about how to configure disclaimer settings. |
| ↳ disclaimer_text **(Điều kiện)** | object | Bắt buộc khi `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer in the ad. |
| ↳↳ text **(Điều kiện)** | string | Bắt buộc khi `disclaimer_text` is specified. ⏎ The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳ disclaimer_clickable_texts **(Điều kiện)** | object[] | Bắt buộc khi `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. ⏎ Kích thước tối đa: 3. ⏎ If you use multiple clickable disclaimers, both the overall length for all the texts you specify and the length of individual text need to be no more than 40 characters. |
| ↳↳ text **(Điều kiện)** | string | Bắt buộc khi `disclaimer_clickable_texts` is specified. ⏎ The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳ url **(Điều kiện)** | string | Bắt buộc khi `disclaimer_clickable_texts` is specified. ⏎ The URL for the clickable disclaimer. ⏎ When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ad_configuration | object | Các cấu hình bổ sung. |
| ↳ identity_type | string | Valid in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives. ⏎ Loại danh tính (identity type). • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ identity_id | string | Valid in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives. ⏎ ID danh tính. |
| ↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ dark_post_status | string | Chỉ hợp lệ khi bạn tạo Spark Ads qua Spark Ads Push. ⏎ Trạng thái của "Chế độ chỉ hiển thị qua quảng cáo" (Ads-only mode) cho mẫu sáng tạo của bạn. ⏎ Các giá trị enum hỗ trợ: • `ON`: Bật chế độ chỉ hiển thị qua quảng cáo để giới hạn bài đăng chỉ nhận lưu lượng truy cập trả phí. • `OFF`: Tắt chế độ chỉ hiển thị qua quảng cáo. Bài đăng sẽ xuất hiện trên hồ sơ TikTok của bạn và đủ điều kiện nhận lưu lượng truy cập tự nhiên. ⏎ **Note**:  • You can set this to `OFF` only if both the identity's "Show through ads only" mode is disabled and the ad account does not have mandatory "Show through ads only" mode enabled. If the ad account enforces mandatory "Ads-only mode", you can only set this field to `ON` when creating Spark Ads using Spark Ads Push. This prevents the posts from appearing on your TikTok profile and gaining organic traffic, regardless of the identity's own `ads_only_mode` setting. It's a safeguard to ensure your Spark Ads Push content remains ads-only and avoids accidental profile posts. • To confirm the "Show through ads only" mode status of an identity, use [/identity/info/](46-identity.md#doc-1740218453385217) and check the returned `ads_only_mode`.  • To confirm the mandatory "Show through ads only" mode status of an ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `ads_only_mode`. |
| ↳ product_specific_type | string | • When `catalog_enabled` is `true` at the campaign level, this field can be set to `ALL`, `PRODUCT_SET`, or `CUSTOMIZED_PRODUCTS`. • When `catalog_enabled` is `false` or not set at the campaign level, this field can only be set to `UNSET`. ⏎ Các chiều khác nhau để lựa chọn sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Cho phép TikTok chọn động từ tất cả sản phẩm. • `PRODUCT_SET`: Chỉ định một nhóm sản phẩm. TikTok sẽ chọn sản phẩm động từ nhóm này. • `CUSTOMIZED_PRODUCTS`: Chỉ định một số lượng sản phẩm tùy chỉnh. • `UNSET`: Chưa thiết lập (Unset). ⏎ • If this field is set to `ALL`, you don't need to input `product_set_id` and `product_ids`. • If this field is set to `PRODUCT_SET`, you need to pass in `product_set_id`. • If this field is set to `CUSTOMIZED_PRODUCTS`, `product_ids` is required. |
| ↳ product_set_id **(Điều kiện)** | string | Bắt buộc khi `product_specific_type` is `PRODUCT_SET`. ⏎ ID của nhóm sản phẩm. ⏎ • Để lấy các nhóm sản phẩm trong tài khoản quảng cáo của bạn, sử dụng [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169). • Để tạo một nhóm sản phẩm, sử dụng [/catalog/set/create/](29-catalog-product-sets.md#doc-1740572891104257). |
| ↳ product_ids **(Điều kiện)** | string[] | Bắt buộc khi `product_specific_type` is `CUSTOMIZED_PRODUCTS`. ⏎ Danh sách ID sản phẩm trong danh mục. ⏎ Kích thước tối đa: 20. ⏎ To retrieve the product ID (`product_id`) of each catalog product, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳ catalog_creative_toggle | boolean | Chỉ hợp lệ khi `catalog_enabled` là `true` ở cấp chiến dịch. ⏎ Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ • If you set this field to `true` in Upgraded Smart+ Web Ads using the catalog carousel format, you need to provide a `creative_info` with only `music_info` in it to specify the music to be used in catalog carousel. • If you set this field to `true` in [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314) using the catalog carousel format, you need to provide a `creative_info` with one image in `image_info` and `music_info` in it to specify the end card image and music to be used in catalog carousel. |
| ↳ catalog_creative_info | object | Chỉ hợp lệ khi `catalog_creative_toggle` is `true` and this field is supported for your specific use case.  • The availability of this field varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. ⏎ Additional settings for catalog creatives to use in your ads. |
| ↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce, entertainment, generic, or online-to-offline catalog to use in the ad. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates.  • `MULTI_SHOW`: Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. ⏎ **Note**: If `catalog_media_settings` is specified during ad creation, you cannot update `catalog_creative_toggle` to `false` or update `catalog_media_settings` to an empty list (`[]`). |
| ↳↳ catalog_template_video_id | string | ID mẫu video trong danh mục của bạn dùng trong quảng cáo. • To obtain the IDs of video templates (video packages) in your catalog, use [/catalog/video_package/get/](31-catalog-video-templates.md#doc-1740574099715073). • To learn about how to create video packages on TikTok Ads Manager, see [How to create video packages in a Catalog](https://ads.tiktok.com/help/article/how-to-create-video-packages-in-a-catalog). ⏎ The availability of this field varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact requirements for your scenario. |
| ↳ creative_auto_add_toggle | boolean | Chỉ hợp lệ trong bất kỳ trường hợp nào sau đây: ⏎ • Scenario 1: • At the campaign level, `objective_type` is `WEB_CONVERSIONS` and `sales_destination` is `WEBSITE`. • Scenario 2: • At the campaign level, `objective_type` is `LEAD_GENERATION`. • At the ad group level, `promotion_type` is `LEAD_GENERATION` and `promotion_target_type` is `INSTANT_PAGE` or `EXTERNAL_WEBSITE`. ⏎ Có thực hiện auto-add newly generated assets during delivery. ⏎ During your campaign, the system will generate new creative assets from your existing campaign assets and creative library. By using TikTok's latest trending elements (hooks, music, text, and more), you'll get high-quality, ready-to-use content that delivers alongside your other selected assets. ⏎ New assets will be added to your campaign automatically and won't appear on your TikTok profile. You can turn off this feature anytime. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ creative_auto_enhancement_strategy_list | string[] | The list of automatic enhancement strategies to apply to your ads. ⏎ Automatic enhancements are real-time edits applied to your ads during your campaign. They can improve performance by creating more engaging and impactful visuals, sound, and more. ⏎ For best results, turn on all automatic enhancements to improve the overall quality of your ads without any extra work. ⏎ Các giá trị enum hỗ trợ: • `TRANSLATE_AND_DUB`: Translate and dub. Connect with global audiences by delivering your ad in 50+ languages. • `MUSIC_REFRESH`: Music refresh. Stay on-trend by swapping in music currently popular on TikTok. • `VIDEO_QUALITY`: Video quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_QUALITY`: Image quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_RESIZE`: Resize. Resize your image to take advantage of full-screen capabilities. ⏎ To learn about the scenarios where you can enable this setting, see [Availability of Automatic Enhancements for Upgraded Smart+ Ads](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1855450880142402). ⏎ **Note**:  • Once an ad group is created, the `TRANSLATE_AND_DUB` option within `creative_auto_enhancement_strategy_list` cannot be updated. You cannot add it if it was initially excluded, nor remove it if it was included. • The automatic enhancements for images (`IMAGE_QUALITY` and `IMAGE_RESIZE`) will only take effect if your ad contains image creatives. |
| ↳ deeplink_utm_params | object[] | Chỉ hợp lệ khi tất cả các điều kiện sau đều được thỏa mãn: • At the campaign level: • `objective_type` is `WEB_CONVERSIONS` • `sales_destination` is `APP`. • At the ad level: • `deeplink` is specified. • `deeplink_type` is `DEFERRED_DEEPLINK`. ⏎ A list of deeplink URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. ⏎ Kích thước tối đa: 14. ⏎ **Note**: Deeplink URL parameters are currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳↳ key | string | The deeplink URL parameter. ⏎ You can specify a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳↳ value | string | The value of the deeplink URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| ↳ end_card_cta | string | Valid when the following conditions are met: ⏎ • At the campaign level: • `objective_type` is `LEAD_GENERATION`. • `catalog_enabled` is `true`. • At the ad group level: • An Auto-Inventory or Auto-Model catalog is specified through `catalog_id`. • At the ad level: • `catalog_creative_toggle` is `true`. ⏎ Call-to-action for the end card (`image_info`) of an Upgraded Smart+ [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873), or [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). ⏎ Các giá trị enum hỗ trợ: • `SEARCH_INVENTORY` (Recommended): Search inventory. • `LEARN_MORE`: Learn more. • `SHOP_NOW`: Shop now. • `SIGN_UP`: Sign up. • `CONTACT_US`: Contact us. • `BOOK_NOW`: Book now. • `READ_MORE`: Read more. • `VIEW_MORE`: View now. • `ORDER_NOW`: Order now. • `SEND_MESSAGE`: Send message. • This value is only available for [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). |
| ↳ auto_disclaimer_types | string[] | Chỉ hợp lệ khi the following conditions are met: ⏎ • At the campaign level: • `objective_type` is `LEAD_GENERATION`. • `catalog_enabled` is `true`. • At the ad group level: • An Auto-Model catalog is specified through `catalog_id`. • At the ad level: • `catalog_creative_toggle` is `true.` ⏎ The type of disclaimer to show in the [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873). ⏎ Các giá trị enum hỗ trợ: • `EMISSION`: Emission disclaimer. • `DISCOUNT`: Discount or offer disclaimer. ⏎ Kích thước tối đa: 1. ⏎ **Note**: Before using any type of disclaimer, ensure that you have specified the necessary disclaimer details for each vehicle in the Auto-Model catalog. ⏎ • To use the emission disclaimer, ensure that you have provided the following details for each vehicle: • `emission_disclaimer` • `emission_disclaimer_url` • `emission_overlay_disclaimer` • `emission_image_link` • To use the discount or offer disclaimer, ensure that you have provided the following details for each vehicle: • `offer_disclaimer` • `offer_disclaimer_url`To get the attributes of vehicles in an Auto-Model catalog, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). ⏎ To update the attributes of vehicles in an Auto-Model catalog, use [/catalog/product/update/](28-catalog-products-p2.md#doc-1740562287852546). |
| ↳ utm_params | object[] | Valid when `objective_type` is `WEB_CONVERSIONS` at the campaign level. ⏎ A list of URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. ⏎ Max size : 14. ⏎ If you set `landing_page_url` to a URL that already includes URL parameters, you can optionally pass `utm_params` at the same time to store the URL parameters used in the URL. In such cases, you need to ensure that `utm_params` exactly matches the used URL parameters. The URL parameters will not be automatically appended to the `landing_page_url` upon ad delivery. |
| ↳↳ key | string | The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm.Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳↳ value | string | The value of the URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| ↳ product_info**(Điều kiện)** | object | Product information. ⏎ This information will be used in different ad variations to create personalized ad delivery with the goal of improving ad performance. Based on past data, ads with complete information often have more clicks and conversions. Results may vary. ⏎ All fields within the `product_info` object are optional. The more detailed information you provide through the parameters, the better the generated ad variations will be. ⏎ To learn about the scenarios where you can use the parameters within this field, see [Available product information settings in Upgraded Smart+ Campaigns](../15-appendix/phu-luc-p2.md#doc-1860735968798721). ⏎ **Note**: The update mode of the `product_info` parameter is full replacement. Even if you want to update one field within it, you need to specify all fields within `product_info`. When `product_info` is updated, the ad will be reviewed again. |
| ↳↳ product_titles | string[] | A list of product names. ⏎ Size range: 0-1. ⏎ Length limit for each product name: 40 characters and cannot contain emoji. Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi ký tự tiếng Anh tính là 1 ký tự. ⏎ If you don't provide a product name, a default name will be used so that the name won't appear blank. |
| ↳↳ product_image_list | object[] | A list of product images. ⏎ Size range: 0-10. ⏎ If you don't provide a product image, a generic image will be used so that the image won't appear blank. |
| ↳↳↳ web_uri | string | The image ID of a product image. ⏎ Specifications requirements: • Image format: .jpg, .png, .jpeg, or .webp. • File size: no more than 5 MB • Image size: no limit.Recommend image resolution: 800 x 800 pixels. ⏎ To obtain the image ID, use the [/file/image/ad/search/](47-images.md#doc-1740052016789506) or [/file/image/ad/upload/](47-images.md#doc-1739067433456642) endpoint. |
| ↳↳ selling_points | string[] | A list of selling points. ⏎ Kích thước tối đa: 15. ⏎ Each selling point must be 1-25 characters long and cannot contain emoji. ⏎ Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi ký tự tiếng Anh tính là 1 ký tự. |
| ↳↳ catalog_tag_list | string[] | Valid in any of the following scenarios: • Scenario 1: At the campaign level `objective_type` is `WEB_CONVERSIONS` and `catalog_type` is `ECOMMERCE`. • Scenario 2:  • At the campaign level `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `true`. • At the ad group level an Auto-Inventory catalog is specified through `catalog_id`.Details of the product information for catalog ads. • For scenario 1, the specified product information will be automatically displayed from your catalog to drive results. The enum values are: • `PRICE`: Price. • `STRIKETHROUGH_PRICE`: Strikethrough price. • `DISCOUNT`: Discount. • `FREE_SHIPPING`: Free shipping.Giá trị mặc định: `["PRICE", "STRIKETHROUGH_PRICE", "DISCOUNT", "FREE_SHIPPING"]`. ⏎ Kích thước tối đa: 4. • For scenario 2, the corresponding text for the specified product information will be displayed on the inventory card. The enum values are: • `DEALER_NAME`: Dealer name. • `CURRENT_MILEAGE`: Current mileage. • `LEAD_PRICE`: Price. • `LEAD_SALE_PRICE`: Sale price. • `EXTERIOR_COLOR`: Exterior color. • `TRIM`: Trim. • `ADDRESS_CITY`: City. • `VEHICLE_STATE`: Vehicle state.Kích thước tối đa: 2 for primary catalog tags (`DEALER_NAME`,`CURRENT_MILEAGE`,`EXTERIOR_COLOR`,`TRIM`,`ADDRESS_CITY`,`VEHICLE_STATE`) and 2 for secondary catalog tags (`LEAD_PRICE`,`LEAD_SALE_PRICE`). |
| ↳↳ product_card_type | string[] | The product card display type. ⏎ Các giá trị enum hỗ trợ: • `PRODUCT_CARD`: Product Card. • `PRODUCT_TILE`: Product Tiles. • `PRODUCT_INFO_CARD`: Info Card. • `PRODUCT_SHOWCASE_TILE`: Showcase Tiles. • `ANCHOR`: Anchor. • `CAROUSEL_LABEL`: Carousel label. ⏎ **Note**: If you want to disable the product card, set this field to `[]`. |
| ↳↳ promo_info_list | object[] | Chỉ hợp lệ cho [Chiến dịch Web Smart+ nâng cấp thông thường](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302878676994). ⏎ Chi tiết về mã ưu đãi và khuyến mại. ⏎ Your offer details for promo codes, offers, or events will be highlighted to boost engagement and ad performance. Promo codes require shoppers to enter a code at checkout. Offers apply automatically and no code is needed. ⏎ Kích thước tối đa: 10. ⏎ **Note**: The update mode of the `promo_info_list` parameter is full replacement. Even if you want to update one field within it, you need to specify all fields within `promo_info_list`. When `promo_info_list` is updated, the ad will be reviewed again. |
| ↳↳↳ discount_type**(Điều kiện)** | string | Bắt buộc khi `promo_info_list` is specified. ⏎ Loại giảm giá. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Giảm giá theo phần trăm. • `CASH`: Giảm giá bằng tiền mặt. |
| ↳↳↳ discount_value**(Điều kiện)** | float | Bắt buộc khi `promo_info_list` is specified. ⏎ Giá trị giảm giá. • When `discount_type` is `PERCENTAGE`, specify an integer between 1-100. • When `discount_type` is `CASH`, specify a float greater than 0. |
| ↳↳↳ discount_currency**(Điều kiện)** | string | Bắt buộc khi `discount_type` is `CASH`. ⏎ Loại tiền tệ giảm giá. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ promo_code | string | Mã ưu đãi / mã khuyến mại. • For promo codes that require shoppers to enter a code at checkout, specify the code through this field. • For offers that apply automatically, omit this field. ⏎ Giới hạn độ dài: 30 characters long and cannot contain emoji. Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi ký tự tiếng Anh tính là 1 ký tự. ⏎ **Note**: Promo codes exclusive to TikTok often perform best. |
| ↳↳↳ minimum_purchase_type | string | Loại giá trị mua hàng tối thiểu. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Số lượng tối thiểu. • `SUBTOTAL`: Tổng phụ tối thiểu. |
| ↳↳↳ minimum_purchase_value**(Điều kiện)** | float | Bắt buộc khi `minimum_purchase_type` is specified. ⏎ Giá trị mua hàng tối thiểu. • When `minimum_purchase_type` is `QUANTITY`, specify an integer that is 0 or greater. • When `minimum_purchase_type` is `SUBTOTAL`, specify a float greater than 0. |
| ↳↳↳ minimum_purchase_currency**(Điều kiện)** | string | Bắt buộc khi `minimum_purchase_type` is `SUBTOTAL`. ⏎ Loại tiền tệ mua hàng tối thiểu. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ valid_start_time | string | Thời gian bắt đầu có hiệu lực (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ valid_end_time | string | Thời gian kết thúc có hiệu lực (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. • The `valid_end_time` should be later than the current time. • If you specify `valid_end_time`, provide `valid_start_time` at the same time. |
| ↳ product_info_enabled | string | Chế độ thông tin sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Để tắt chế độ thông tin sản phẩm. • `NON_CATALOG`: Để bật phiên bản không theo danh mục của thông tin sản phẩm. • `CATALOG`: Để bật phiên bản danh mục của thông tin sản phẩm. ⏎ To learn about the scenarios where you need to set this parameter, see [Available product information settings in Upgraded Smart+ Campaigns](../15-appendix/phu-luc-p2.md#doc-1860735968798721). ⏎ **Note**:  • This field will automatically be set to `CATALOG` when the following conditions are both met at the campaign level: • `app_promotion_type` is `MINIS`. • `catalog_enabled` is `true`. • This field can only be set to `UNSET` when an Inventory Card portfolio is specified through `card_id` in [Upgraded Smart+ Automotive Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324618421314). |
| ↳ call_to_action_id | string | The ID of the call-to-action (CTA) portfolio (also known as dynamic CTA) that you want to use in your ads. A CTA portfolio is a group of auto-optimized CTAs. ⏎ For details about auto-optimized CTAs, see [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). ⏎ Liệu this field is supported varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact scenarios where this field is supported. |
| ↳ tracking_info | object | Tracking information. ⏎ To learn about the scenarios where this field is supported, see [the specific use case](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3). |
| ↳↳ viewability_postbid_partner | string | Post-bid third-party viewability measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. ⏎ You can only update this field for the created ad before the ad passes the review and becomes active. ⏎ **Note**: • Post-bid third-party viewability measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • See [Brand safety](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) to learn about the supported advertising objectives, supported markets, and the general introduction of post-bid measurement. • When you pass in both `brand_safety_postbid_partner` and `viewability_postbid_partner`: • If you set either of these two fields as `IAS`, you need to specify both as `IAS`, and assign the same value (the wrapped VAST URL that you obtain from the measurement partner IAS) to `brand_safety_vast_url` and `viewability_vast_url`. • If you set either of these two fields as `ZEFR`, you need to specify both as `ZEFR`. • If you set two different post-bid measurement partners, only the post-bid brand safety measurement setting will become valid. |
| ↳↳ viewability_vast_url **(Điều kiện)** | string | Bắt buộc khi `viewability_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure viewability. You need to get the URL from the measurement partner IAS. ⏎ You can only update this field for the created ad before the ad passes the review and becomes active. ⏎ **Note**: • Post-bid third-party viewability measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When you set both `brand_safety_postbid_partner` and `viewability_postbid_partner` as IAS, `brand_safety_vast_url` should be the same as `viewability_vast_url`. |
| ↳↳ brand_safety_postbid_partner | string | Post-bid third-party brand safety measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. ⏎ You can only update this field for the created ad before the ad passes the review and becomes active. ⏎ **Note**: • Post-bid third-party brand safety measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • See [Brand safety](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) to learn about the supported advertising objectives, supported markets, and the general introduction of post-bid measurement. • When you pass in both `brand_safety_postbid_partner` and `viewability_postbid_partner`: • If you set either of these two fields as `IAS`, you need to specify both as `IAS`, and assign the same value (the wrapped VAST URL that you obtain from the measurement partner IAS) to `brand_safety_vast_url` and `viewability_vast_url`. • If you set two different post-bid measurement partners, only the post-bid brand safety measurement setting will become valid. |
| ↳↳ brand_safety_vast_url **(Điều kiện)** | string | Bắt buộc khi `brand_safety_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure brand safety. You need to get the URL from the measurement partner IAS. ⏎ You can only update this field for the created ad before the ad passes the review and becomes active. ⏎ **Note**: • Post-bid third-party brand safety measurement is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When you set both `brand_safety_postbid_partner` and `viewability_postbid_partner` as IAS, `brand_safety_vast_url` should be the same as `viewability_vast_url`. |
| ↳↳ impression_tracking_url | string | Default Impression Tracking URL. ⏎ URL generated by your data partner to track impression events in your ads. Generally you can find and copy the URL from their platform. ⏎ • If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). • If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Default Impression Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). |
| ↳↳ click_tracking_url | string | Click Tracking URL. ⏎ URL generated by your data partner to track click events in your ads. Generally you can find and copy the URL from their platform. ⏎ • If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). • If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Click Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).Currently, Pangle does not support DCM, Sizmek or Flashtalking. |
| ↳↳ tracking_app_id | string | Valid when `objective_type` is `WEB_CONVERSIONS`. ⏎ The ID of the App that you want to track. ⏎ You can use this field to track offsite app events. ⏎ If `app_id` is specified at the ad group level and you want to track offsite app events, then the application ID you pass via this field must be the same ID that you specified at the ad group level. Otherwise, you can pass in any application ID that you'd like to track via this field. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ tracking_pixel_id | string | Chỉ hợp lệ trong bất kỳ trường hợp nào sau đây: • Scenario 1: At the campaign level, `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. • Scenario 2:  • At the campaign level, `objective_type` is `LEAD_GENERATION`. • At the ad group level, `promotion_target_type` is not set to `EXTERNAL_WEBSITE`. ⏎ The ID of the pixel for tracking the actions people take on your website, such as page views, add to cart, purchases, and more. ⏎ • If `pixel_id` is already set at the ad group level, this `tracking_pixel_id` must match it for tracking website events. • If `pixel_id` is not set at the ad group level, you may specify any ID TikTok Pixel for tracking website events. |
| ↳↳ tracking_offline_event_set_ids | string[] | Chỉ hợp lệ khi the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. ⏎ A list of Offline Event set IDs for tracking customer actions that happen in-person, such as in-store purchases or live event attendance. ⏎ Kích thước tối đa: 50. ⏎ See [here](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193) to learn more about how to create and manage Offline Event sets. ⏎ **Note**: ⏎ • For a new ad, existing auto-tracking Offline Event sets have to be tracked. You can choose to omit or provide this field. • If you omit this field, it automatically includes all **existing** auto-tracking Offline Event set IDs within your ad account. • If you provide this field, you need to specify all **existing** auto-tracking Offline Event set IDs. Adding non-auto-tracking Offline Event set IDs is optional. To find existing auto-tracking Offline Event sets within an ad account, call [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313) and select sets where `auto_tracking` is `true`. |

### Danh sách giá trị cho `discount_currency` hoặc `minimum_purchase_currency`
Bảng sau đây liệt kê các giá trị enum cho `discount_currency` hoặc `minimum_purchase_currency`.

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
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "smart_plus_ad_id": "{{smart_plus_ad_id}}",
    "ad_name": "{{ad_name}}"
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
| ↳ ad_name | string | Tên mẫu quảng cáo. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad is enabled (in 'ON' status). • `DISABLE`: The ad is disabled (in 'OFF' status). • `FROZEN`: The ad is terminated and cannot be enabled. |
| ↳ secondary_status | string | Ad secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ The following secondary statuses are newly added for Upgraded Smart+ Ads: • `AD_STATUS_DELIVERY_AND_REAUDIT`: Review of modifications in progress. • `AD_STATUS_DELIVERY_AND_TRANSCODING_FAIL`: Transcoding of the video or videos in the ad failed. • `AD_STATUS_REVIEW_PARTIALLY_APPROVED`: Ad in partial review and in delivery. • `AD_STATUS_COLLECTION_TOGGLED_OFF`: Lead collection has ended. • `AD_STATUS_PRIVACY_POLICY_REJECTED`: Ad rejected due to privacy policy violations. • `AD_STATUS_PRIVACY_POLICY_AUDIT`: Ad in review for privacy policy compliance. |
| ↳ create_time | string | The time when the ad was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ modify_time | string | The time when the ad was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ creative_list | object[] | Danh sách các mẫu sáng tạo. |
| ↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳↳ smart_plus_creative_id | string | The ID of the creative in the Upgraded Smart+ Ad. ⏎ This ID is the same as the creative ID you retrieve in the following scenarios: • The `ad_id` you receive from [/ad/get/](02-ads-p1.md#doc-1735735588640770) when you do not specify the `ad_ids_v2` filter. • The `ad_id` metric you retrieve from [/report/integrated/get/](58-reporting.md#doc-1740302848100353) when you set `data_level` to `AUCTION_AD` and include `ad_id` in `dimensions`. |
| ↳↳ material_operation_status | string | Trạng thái của mẫu sáng tạo. ⏎ Các giá trị enum hỗ trợ: • `ENABLE`: The creative is enabled (in 'ON' status). • `DISABLE`: The creative is disabled (in 'OFF' status). |
| ↳↳ creative_info | object | Thông tin mẫu sáng tạo. |
| ↳↳↳ ad_format | string | Định dạng quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `SINGLE_VIDEO`: Video đơn (Single Video). • `CAROUSEL_ADS`: Nhóm hình ảnh xoay vòng tiêu chuẩn (Standard Carousel). • `CATALOG_CAROUSEL`: Nhóm hình ảnh xoay vòng danh mục (Catalog Carousel). |
| ↳↳↳ material_name | string | Material name. ⏎ **Note**: If `ad_format` is `CAROUSEL_ADS` and you have set a non-empty custom name for the carousel via `material_name` in the request, this field will return your custom carousel name. |
| ↳↳↳ video_info | object | Thông tin video. |
| ↳↳↳↳ video_id | string | ID video. |
| ↳↳↳↳ file_name | string | Tên video. |
| ↳↳↳ thumbnail_mode | string | The mode of the video thumbnail. ⏎ Hình thu nhỏ sẽ hiển thị dưới dạng hình ảnh đầu tiên trên trang kết quả tìm kiếm. Hình thu nhỏ đóng vai trò quan trọng trong việc thu hút sự chú ý của đối tượng và thúc đẩy lượt nhấp. ⏎ Các giá trị enum hỗ trợ: • `AUTOMATIC`: Hình thu nhỏ thông minh (Smart thumbnail). The system will show a different frame from your video customized for different audiences to closely match what they're searching for and what they're most likely to tap. The video cover specified through `image_info` will be used as the fallback video thumbnail if no matching thumbnails are found. • `MANUAL`: Hình thu nhỏ thủ công (Manual thumbnail). The video cover specified through `image_info` will be used as the video thumbnail. |
| ↳↳↳ image_info | object[] | Thông tin hình ảnh. |
| ↳↳↳↳ web_uri | string | ID hình ảnh. |
| ↳↳↳ music_info | object | Thông tin âm nhạc. |
| ↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳ aigc_disclosure_type | string | Có bật nút tự khai báo nội dung do AI tạo (AIGC - Artificial Intelligence Generated Content) để biểu thị quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo của bạn sẽ gắn nhãn "Nhà quảng cáo gắn nhãn do AI tạo" khi xem toàn màn hình. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: Bật nút khai báo quảng cáo có chứa nội dung do AI tạo. • `NOT_DECLARED`: Không khai báo quảng cáo có chứa nội dung do AI tạo. |
| ↳↳↳ tiktok_item_id | string | ID của bài đăng TikTok dùng làm quảng cáo (Spark Ads). |
| ↳↳↳ identity_type | string | Returned for Spark Ads created without using catalog creatives. ⏎ Loại danh tính (identity type). ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ identity_id | string | Returned for Spark Ads created without using catalog creatives. ⏎ ID danh tính. |
| ↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ playable_list | object[] | A list of playables. |
| ↳↳ playable_url | string | URL của mẫu quảng cáo tương tác (playable). |
| ↳ ad_text_list | object[] | A list of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. |
| ↳↳ ad_text | string | Ad text. |
| ↳ auto_message_list | object[] | Returned only when `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` at the ad group level. ⏎ Details of the automatic message to use in a TikTok Direct Messaging Ad. |
| ↳↳↳ auto_message_id | string | Bắt buộc khi `auto_message_list` is specified. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is welcome message. • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ To learn more about how to create TikTok Direct Messaging Ads with welcome messages, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as TikTok direct messages](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302969710913). |
| ↳ call_to_action_list | object[] | Danh sách lời kêu gọi hành động (CTA). |
| ↳↳ call_to_action | string | Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ interactive_add_on_list | object[] | Danh sách các tiện ích bổ sung tương tác (interactive add-on) (creative portfolio) IDs. |
| ↳↳ card_id | string | ID của một tiện ích bổ sung tương tác. |
| ↳ page_list | object[] | Danh sách các trang. |
| ↳↳ page_id | string | Page ID. |
| ↳ landing_page_url_list | object[] | A list of landing page URLs. |
| ↳↳ landing_page_url | string | Landing page URL. |
| ↳ custom_product_page_list | object[] | Details of the custom product page to use in the ad. |
| ↳↳ custom_product_page_url | string | URL Trang sản phẩm tùy chỉnh (Custom Product Page - CPP). ⏎ CPPs are product pages with customized screenshots, promotional text, and app previews that can be used to highlight specific content or features of the promoted app, or reach specific audiences. ⏎ Example: `https://apps.apple.com/us/app/tiktok/id835599320?ppid=12345a6b-c789-12d3-e4f5-g6h78i91jk2l`. |
| ↳ deeplink_list | object[] | Danh sách liên kết sâu (deeplink). |
| ↳↳ deeplink | string | Deeplink, the specific location where you want your audience to go if they have your app installed. |
| ↳↳ deeplink_type | string | Loại liên kết sâu (deeplink). ⏎ Các giá trị enum hỗ trợ: • `NORMAL`: non-deferred deeplink. • `DEFERRED_DEEPLINK`: deferred deeplink. |
| ↳ multi_dest_list | object[] | Returned only when `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION` is specified at the ad group level. ⏎ A list of destinations for the Lead Generation ad. |
| ↳↳ dest_type | string | Loại đích đến. ⏎ Các giá trị enum hỗ trợ: • `EXTERNAL_WEBSITE`: Website URL. You need to specify `landing_page_url` simultaneously. • `INSTANT_PAGE`: Instant Form. You need to specify `page_id` simultaneously. • `TT_DIRECT_MESSAGAE`: Message template. You need to specify `auto_message_id` simultaneously. |
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
| ↳ ad_configuration | object | Các cấu hình bổ sung. |
| ↳↳ identity_type | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ Loại danh tính (identity type). • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ identity_id | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ ID danh tính. |
| ↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ dark_post_status | string | Trạng thái của "Chế độ chỉ hiển thị qua quảng cáo" (Ads-only mode) cho mẫu sáng tạo của bạn. ⏎ Các giá trị enum hỗ trợ: • `ON`: Bật chế độ chỉ hiển thị qua quảng cáo để giới hạn bài đăng chỉ nhận lưu lượng truy cập trả phí. • `OFF`: Tắt chế độ chỉ hiển thị qua quảng cáo. Bài đăng sẽ xuất hiện trên hồ sơ TikTok của bạn và đủ điều kiện nhận lưu lượng truy cập tự nhiên. |
| ↳↳ product_specific_type | string | Các chiều khác nhau để lựa chọn sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Cho phép TikTok chọn động từ tất cả sản phẩm. • `PRODUCT_SET`: Chỉ định một nhóm sản phẩm. TikTok sẽ chọn sản phẩm động từ nhóm này. • `CUSTOMIZED_PRODUCTS`: Chỉ định một số lượng sản phẩm tùy chỉnh. • `UNSET`: Chưa thiết lập (Unset). |
| ↳↳ product_set_id | string | ID của nhóm sản phẩm. |
| ↳↳ product_ids | string[] | The product IDs of catalog products. |
| ↳↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ catalog_creative_info | object | Additional settings for catalog creatives to use in your ads. |
| ↳↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce, entertainment, generic, or online-to-offline catalog to use in the ad. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates. • `MULTI_SHOW`: Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact supported values for your scenario. |
| ↳↳↳ catalog_template_video_id | string | ID mẫu video trong danh mục của bạn dùng trong quảng cáo. |
| ↳↳ creative_auto_add_toggle | boolean | Có thực hiện auto-add newly generated assets during delivery. ⏎ During your campaign, the system will generate new creative assets from your existing campaign assets and creative library. By using TikTok's latest trending elements (hooks, music, text, and more), you'll get high-quality, ready-to-use content that delivers alongside your other selected assets. ⏎ New assets will be added to your campaign automatically and won't appear on your TikTok profile. You can turn off this feature anytime. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ creative_auto_enhancement_strategy_list | string[] | The list of automatic enhancement strategies to apply to your ads. ⏎ Automatic enhancements are real-time edits applied to your ads during your campaign. They can improve performance by creating more engaging and impactful visuals, sound, and more. ⏎ Các giá trị enum hỗ trợ: • `TRANSLATE_AND_DUB`: Translate and dub. Connect with global audiences by delivering your ad in 50+ languages. • `MUSIC_REFRESH`: Music refresh. Stay on-trend by swapping in music currently popular on TikTok. • `VIDEO_QUALITY`: Video quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_QUALITY`: Image quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_RESIZE`: Resize. Resize your image to take advantage of full-screen capabilities. • `CALL_TO_ACTION_ENHANCEMENT`: CTA enhancement. Tailor and optimize your call to action based on specific use cases to enhance performance. • `AIGC_CARD`: Generate ad card. Increase engagement by showcasing key messages and visuals designed to drive clicks and conversions. ⏎ **Note**: Currently, you cannot enable the strategies `CALL_TO_ACTION_ENHANCEMENT` and `AIGC_CARD` through `creative_auto_enhancement_strategy_list` via API. |
| ↳↳ deeplink_utm_params | object[] | A list of deeplink URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳ key | string | The deeplink URL parameter. ⏎ It can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. |
| ↳↳↳ value | string | The value of the deeplink URL parameter. ⏎ It can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳ end_card_cta | string | Call-to-action for the end card (`image_ids`) of an Upgraded Smart+ [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873), or [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). ⏎ Các giá trị enum hỗ trợ: • `SEARCH_INVENTORY` (Recommended): Search inventory. • `LEARN_MORE`: Learn more. • `SHOP_NOW`: Shop now. • `SIGN_UP`: Sign up. • `CONTACT_US`: Contact us. • `BOOK_NOW`: Book now. • `READ_MORE`: Read more. • `VIEW_MORE`: View now. • `ORDER_NOW`: Order now. • `SEND_MESSAGE`: Send message. • This value is only available for [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). |
| ↳↳ product_display_field_list | string[] | A list of product details to display in your [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161). ⏎ Enum values for Automotive Carousel Ad for Inventory: • `DEALER_NAME`: the `dealer_name` field of vehicles. • `MAKE`: the `make` field of vehicles. • `MODEL`: the `model` field of vehicles. • `YEAR`: the `year` field of vehicles. • `MILEAGE`: the `mileage` field of vehicles. • `PRICE`: the `price` field of vehicles. • `SALE_PRICE`: the `sale_price` field of vehicles. • `EXTERIOR_COLOR`: the `exterior_color` field of vehicles. • `TRIM`: the `trim` field of vehicles. • `ADDRESS_CITY`: the `city` field of vehicles. • `VEHICLE_STATE`: the `state_of_vehicle` field of vehicles. ⏎ Enum values for Upgraded Smart+ Lead Generic Catalog Ads : • `RATING`: the `rating` field of generic products or services. • `SALE_PRICE`: the `sale_price` field of generic products or services. • `PRICE`: the `price` field of generic products or services. • `DESCRIPTION`: the `description` field of generic products or services. • `ADDRESS_CITY`: the `address.city` field of generic products or services. • `ADDRESS_REGION`: the `address.region` field of generic products or services. • `ADDRESS_STREET`: the `address.street` field of generic products or services. • `CUSTOM_LABEL_0`: the `custom_label_0` field of generic products or services. • `CUSTOM_LABEL_1`: the `custom_label_1` field of generic products or services. • `CUSTOM_LABEL_2`: the `custom_label_2` field of generic products or services. ⏎ The title of each vehicle, product, or service is displayed automatically. For instance, if you set this field to `["MILEAGE","YEAR"]`, the ad will display the `mileage`, `price` and `title` fields of each vehicle. ⏎ To retrieve the product detail fields of your vehicles in an Auto-Inventory catalog or that of your products or services in a generic catalog and check Liệu you need to update the details, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
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
| ↳↳↳ promo_info_list | object[] | Returned only for [regular Upgraded Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302878676994). ⏎ Chi tiết về mã ưu đãi và khuyến mại. ⏎ Your offer details for promo codes, offers, or events will be highlighted to boost engagement and ad performance. Promo codes require shoppers to enter a code at checkout. Offers apply automatically and no code is needed. |
| ↳↳↳↳ discount_type | string | Returned only when `promo_info_list` is specified. ⏎ Loại giảm giá. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Giảm giá theo phần trăm. • `CASH`: Giảm giá bằng tiền mặt. |
| ↳↳↳↳ discount_value | float | Returned when `promo_info_list` is specified. ⏎ Giá trị giảm giá. |
| ↳↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Loại tiền tệ giảm giá. ⏎ Để xem danh sách giá trị enum, xem  List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳ promo_code | string | Mã ưu đãi / mã khuyến mại. |
| ↳↳↳↳ minimum_purchase_type | string | Loại giá trị mua hàng tối thiểu. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Số lượng tối thiểu. • `SUBTOTAL`: Tổng phụ tối thiểu. |
| ↳↳↳↳ minimum_purchase_value | float | Returned only when `minimum_purchase_type` is specified. ⏎ Giá trị mua hàng tối thiểu. |
| ↳↳↳↳ minimum_purchase_currency | string | Returned only when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Loại tiền tệ mua hàng tối thiểu. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳ valid_start_time | string | Thời gian bắt đầu có hiệu lực (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳↳ valid_end_time | string | Thời gian kết thúc có hiệu lực (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ product_info_enabled | string | Chế độ thông tin sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Để tắt chế độ thông tin sản phẩm. • `NON_CATALOG`: Để bật phiên bản không theo danh mục của thông tin sản phẩm. • `CATALOG`: Để bật phiên bản danh mục của thông tin sản phẩm. |
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
            "catalog_creative_toggle": false,
            "product_ids": [
                "{{product_id}}",
                "{{product_id}}",
                "{{product_id}}",
                "{{product_id}}"
            ],
            "product_specific_type": "CUSTOMIZED_PRODUCTS",
            "tracking_info": {},
            "utm_params": []
        },
        "ad_name": "{{ad_name}}",
        "ad_text_list": [],
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
        "secondary_status": "AD_STATUS_DONE",
        "smart_plus_ad_id": "{{smart_plus_ad_id}}"
    }
}
```

---

<a id="doc-1843317423164482"></a>
<!-- doc_id: 1843317423164482 -->
<!-- doc_id: 1843317423164482 -->
# Cập nhật trạng thái hoạt động của quảng cáo Smart+ nâng cấp (Update the operation statuses of Upgraded Smart+ Ads)
> Đường dẫn: API Reference > Upgraded Smart+ > Ads > Update the operation statuses of Upgraded Smart+ Ads
Sử dụng endpoint này để bật, tạm dừng hoặc xóa các quảng cáo Smart+ nâng cấp (Upgraded Smart+ Ads).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/status/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Giá trị được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| smart_plus_ad_ids  ****(Bắt buộc)**** | string[] | A list of ad IDs. ⏎ Kích thước tối đa: 20. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |
| operation_status  ****(Bắt buộc)**** | string | The operation to perform on the ads. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (pause), `ENABLE` (enable), `DELETE` (delete). ⏎ **Note**: The status of deleted ads or ads in deleted campaigns or ad groups cannot be modified. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/status/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "smart_plus_ad_ids":["{{smart_plus_ad_ids}}"],
    "operation_status": "DISABLE"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ smart_plus_ad_ids | string[] | The ID list of updated ads. |
| ↳ status | string | The current statuses of the ads. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (paused), `ENABLE` (enabled), `DELETE` (deleted). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "smart_plus_ad_ids": [
            "{{smart_plus_ad_id}}"
        ],
        "status": "DISABLE"
    }
}
```

---

<a id="doc-1843317433577601"></a>
<!-- doc_id: 1843317433577601 -->
<!-- doc_id: 1843317433577601 -->
# Bật hoặc tắt mẫu sáng tạo trong quảng cáo Smart+ nâng cấp (Disable or enable creatives in an Upgraded Smart+ Ad)
> Đường dẫn: API Reference > Upgraded Smart+ > Ads > Disable or enable creatives in an Upgraded Smart+ Ad
Sử dụng endpoint này để tắt hoặc bật một hoặc nhiều mẫu sáng tạo trong quảng cáo Smart+ nâng cấp.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/material_status/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Giá trị được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| smart_plus_ad_id  ****(Bắt buộc)**** | string | ID mẫu quảng cáo. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |
| ad_material_ids  ****(Bắt buộc)**** | string[] | A list of ad material IDs for creatives to operate on. ⏎ An ad material ID is an ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. ⏎ To obtain ad material IDs associated with an ad, use [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). ⏎ Kích thước tối đa: 20. ⏎ You can operate on the following creative types: • Carousels from Standard Carousel Spark Ads (via Spark Ads Push). • Carousels from non-Spark Ad Standard Carousels. • Videos from non-Spark Ads. • Videos from Spark Ads (via Spark Ads Push). • TikTok video posts used as Spark Ad Videos (via Spark Ads Pull). • TikTok photo posts used as Standard Carousel Spark Ads (via Spark Ads Pull). ⏎ **Note**: You cannot mix carousel and non-carousel creative types in the same request. |
| operation_status  ****(Bắt buộc)**** | string | The operation to perform on the creatives. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (pause), `ENABLE` (enable). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/material_status/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "smart_plus_ad_id":"{{smart_plus_ad_id}}",
    "ad_material_ids": ["{{ad_material_ids}}"],
    "operation_status": "DISABLE"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ smart_plus_ad_id | string[] | ID mẫu quảng cáo. |
| ↳ ad_material_ids | string[] | A list of ad material IDs for creatives operated on. ⏎ An ad material ID is an ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳ material_status | string | The statuses of the creatives. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (paused), `ENABLE` (enabled). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "ad_material_ids": [
            "{{ad_material_id}}"
        ],
        "operation_status": "DISABLE",
        "smart_plus_ad_id": "{{smart_plus_ad_id}}"
    }
}
```

---

<a id="doc-1843317445798914"></a>
<!-- doc_id: 1843317445798914 -->
<!-- doc_id: 1843317445798914 -->
# Xem trước quảng cáo Smart+ nâng cấp (Preview Upgraded Smart+ Ads)
> Đường dẫn: API Reference > Upgraded Smart+ > Ads > Preview Upgraded Smart+ Ads
Sử dụng endpoint này để xem trước một quảng cáo Smart+ nâng cấp dự định tạo hoặc một quảng cáo Smart+ nâng cấp hiện có.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/preview/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Giá trị được phép: `application/json`. |

**Parameters**

### Xem trước các quảng cáo dự định tạo (Preview ads that you plan to create)
This allows you to preview your ad before creating it.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| preview_type  ****(Bắt buộc)**** | string | Preview type. ⏎ Enum value:  • `ADS_CREATION`: Preview an ad by ad creation parameters. |
| catalog_enabled | boolean | Có thực hiện use catalog in the campaign. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| catalog_id **(Điều kiện)** | string | Bắt buộc khi `catalog_enabled` is `true`. ⏎ The ID of the catalog to use in the ad group. ⏎ To retrieve the catalogs within your Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610). |
| catalog_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `catalog_enabled` is `true`. ⏎ The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| creative_list  ****(Bắt buộc)**** | object[] | Danh sách các mẫu sáng tạo. ⏎ Size range: 1- 31. |
| ↳ creative_info  ****(Bắt buộc)**** | object | Thông tin mẫu sáng tạo. |
| ↳↳ video_info **(Điều kiện)** | object | Required for the following types of ads: • Non-Spark Ads Single Video ads.  • Spark Ads Single Video ads through Spark Ads Push. ⏎ Thông tin video. |
| ↳↳↳ video_id **(Điều kiện)** | string | Bắt buộc khi `video_info` được chỉ định. ⏎ ID video. ⏎ Để tải lên video và lấy ID video, sử dụng [/file/video/ad/upload/](71-video.md#doc-1737587322856449). ⏎ Để tìm kiếm video trong tài khoản quảng cáo, sử dụng [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| ↳↳ image_info **(Điều kiện)** | object[] | • Required for the following types of ads: • Non-Spark Ads Single Video ads. You need to specify a video cover. • Spark Ads Single Video ads through Spark Ads Push. You need to specify a video cover. • Non-Spark Ads Standard Carousel ads. You need to specify one to 35 carousel images. • Spark Ads Standard Carousel ads through Spark Ads Push. You need to specify one to 35 carousel images. • Not supported for Catalog Carousel ads. ⏎ Thông tin hình ảnh. |
| ↳↳↳ web_uri **(Điều kiện)** | string | Bắt buộc khi `image_info` được chỉ định. ⏎ ID hình ảnh. ⏎ Để tải lên hình ảnh và lấy ID hình ảnh, sử dụng [/file/image/ad/upload/](47-images.md#doc-1739067433456642). ⏎ Để tìm kiếm hình ảnh trong tài khoản quảng cáo, sử dụng [/file/image/ad/search/](47-images.md#doc-1740052016789506). |
| ↳↳ music_info **(Điều kiện)** | object | • Required for the following scenarios: • When you create Standard Carousel Ads, including: • Non-Spark Ads Standard Carousel ads • Spark Ads Standard Carousel ads through Spark Ads Push • Spark Ads Standard Carousel ads through Spark Ads Pull • When `objective_type` is `WEB_CONVERSIONS` and `catalog_creative_toggle` is `true`. The system will automatically generate Catalog Carousel ads.Thông tin âm nhạc. |
| ↳↳↳ music_id **(Điều kiện)** | string | Bắt buộc khi `music_info` được chỉ định. ⏎ ID của đoạn nhạc sử dụng trong quảng cáo xoay vòng (carousel). |
| ↳↳ tiktok_item_id **(Điều kiện)** | string | • Bắt buộc khi you create Spark Ads through Spark Ads Pull, including: • Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. • Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post. • Not supported when `catalog_creative_toggle` is `true`. ⏎ ID của bài đăng TikTok dùng làm quảng cáo (Spark Ads). ⏎ Truyền vào `item_id` nhận được từ phản hồi của endpoint [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) và [/identity/video/get/](46-identity.md#doc-1740218475032577). ⏎ Khi bạn truyền `tiktok_item_id`, bạn không cần truyền các đối tượng `image_info`, `video_info` và `title_list`. ⏎ **Lưu ý**: Khi sử dụng Spark Ads, bạn xác nhận rằng mình có quyền sử dụng âm nhạc trong video cho mục đích thương mại. |
| ↳↳ identity_type **(Điều kiện)** | string | Bắt buộc khi you create Spark Ads without using catalog creatives. ⏎ Loại danh tính (identity type). ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). ⏎ **Note**:  • If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the `identity_type` and `identity_id` within `ad_configuration`. • If this field is set to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE` and the following conditions are both met, you need to specify a dynamic CTA via `call_to_action_id`. • At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳↳ identity_id **(Điều kiện)** | string | Bắt buộc khi you create Spark Ads without using catalog creatives. ⏎ ID danh tính. ⏎ **Note**: If you want to create Spark Ads using catalog creatives from an E-commerce catalog, specify the `identity_type` and `identity_id` within `ad_configuration`. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ad_text_list **(Điều kiện)** | object[] | Bắt buộc khi `tiktok_item_id` is not specified. ⏎ List of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. ⏎ Kích thước tối đa: 5. |
| ↳ ad_text **(Điều kiện)** | string | Bắt buộc khi `ad_text_list` is specified. ⏎ Ad text. |
| call_to_action_list | object[] | Danh sách lời kêu gọi hành động (CTA). ⏎ Kích thước tối đa: 3. ⏎ **Note**: • This field is not supported for Upgraded Smart+ Lead Generation Campaigns. • The preview link will only display the first call-to-action in this list. • `call_to_action_list` and `call_to_action_id` cannot be set at the same time. |
| ↳ call_to_action **(Điều kiện)** | string | Bắt buộc khi `call_to_action_list` is specified. ⏎ Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ad_configuration | object | Các cấu hình bổ sung. |
| ↳ identity_type **(Điều kiện)** | string | Required in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more about how you can create such ads in [Create Upgraded Smart+ E-commerce Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302895272962). ⏎ Loại danh tính (identity type). • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ E-commerce Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ Để biết chi tiết về danh tính, xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ identity_id **(Điều kiện)** | string | Required in any of the following scenarios: • You are creating non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • You are creating Spark Ads using catalog creatives from an E-commerce catalog. Learn more about how you can create such ads in [Create Upgraded Smart+ E-commerce Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302895272962). ⏎ ID danh tính. |
| ↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ product_specific_type **(Điều kiện)** | string | Bắt buộc khi `catalog_enabled` is `true` at the campaign level. ⏎ Các chiều khác nhau để lựa chọn sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Cho phép TikTok chọn động từ tất cả sản phẩm. • `PRODUCT_SET`: Chỉ định một nhóm sản phẩm. TikTok sẽ chọn sản phẩm động từ nhóm này. • `CUSTOMIZED_PRODUCTS`: Chỉ định một số lượng sản phẩm tùy chỉnh. ⏎ •  If this field is set to `ALL`, you don't need to input `product_set_id` and `product_ids`. •  If this field is set to `PRODUCT_SET`, you need to pass in `product_set_id`. •  If this field is set to `CUSTOMIZED_PRODUCTS`, `product_ids` is required. |
| ↳ product_set_id **(Điều kiện)** | string | Bắt buộc khi `product_specific_type` is `PRODUCT_SET`. ⏎ ID của nhóm sản phẩm. ⏎ • Để lấy các nhóm sản phẩm trong tài khoản quảng cáo của bạn, sử dụng [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169). •  Để tạo một nhóm sản phẩm, sử dụng [/catalog/set/create/](29-catalog-product-sets.md#doc-1740572891104257). |
| ↳ product_ids **(Điều kiện)** | string[] | Bắt buộc khi `product_specific_type` is `CUSTOMIZED_PRODUCTS`. ⏎ Danh sách ID sản phẩm trong danh mục. ⏎ Kích thước tối đa: 20. ⏎ To retrieve the product ID (`product_id`) of each catalog product, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳ catalog_creative_toggle | boolean | Chỉ hợp lệ khi `catalog_enabled` is `true`. ⏎ Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ If you set this field to `true`, you need to provide a `creative_info` with only `music_info` in it to specify the music to be used in Nhóm hình ảnh xoay vòng danh mục (Catalog Carousel). |
| ↳ catalog_creative_info | object | Chỉ hợp lệ khi the following conditions are met: • The ad is an [Upgraded Smart+ E-commerce Catalog Ad](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302895272962) or [Upgraded Smart+ Streaming Ad](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302920924306). • `catalog_creative_toggle` is `true`. ⏎ Additional settings for catalog creatives to use in your ads. |
| ↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce or entertainment catalog to use in the ad. ⏎ Enum values for an [Upgraded Smart+ E-commerce Catalog Ad](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302895272962): • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates. If you include this value in `catalog_media_settings`, you can optionally specify `catalog_template_video_id` at the same time. • If `catalog_template_video_id` is not specified, all video templates and video URLs from your catalog will be used to generate the ad. • If `catalog_template_video_id` is specified, the selected video template will be used to generate the ad. ⏎ Enum values for an [Upgraded Smart+ Streaming Ad](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302920924306): • `VIDEO`: Video. • `TEMPLATE_VIDEO`: Video templates. If you include this value in `catalog_media_settings`, you cannot specify `catalog_template_video_id` at the same time. • All video templates and video URLs from your catalog will be used to generate the ad. • `MULTI_SHOW`: Multi-show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. |
| ↳↳ catalog_template_video_id | string | Chỉ hợp lệ khi the following conditions are met: • The ad is an [Upgraded Smart+ Streaming Ad](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302920924306). • `TEMPLATE_VIDEO` is included in `catalog_media_settings`. ⏎ ID mẫu video trong danh mục của bạn dùng trong quảng cáo. ⏎ To obtain the IDs of video templates (video packages) in your catalog, use [/catalog/video_package/get/](31-catalog-video-templates.md#doc-1740574099715073). ⏎ To learn about how to create video packages on TikTok Ads Manager, see [How to create video packages in a Catalog](https://ads.tiktok.com/help/article/how-to-create-video-packages-in-a-catalog). |
| ↳ call_to_action_id | string | The ID of the call-to-action (CTA) portfolio (also known as dynamic CTA) that you want to use in your ads. A CTA portfolio is a group of auto-optimized CTAs. ⏎ For details about auto-optimized CTAs, see [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). ⏎ **Note**: `call_to_action_list` and `call_to_action_id` cannot be set at the same time. |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/preview/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "preview_type": "ADS_CREATION",
    "catalog_enabled": true,
    "catalog_id": "{{catalog_id}}",
    "catalog_authorized_bc_id": "{{catalog_authorized_bc_id}}",
    "creative_list": [
        {
            "creative_info": {
                "video_info": {
                    "video_id": "{{video_id}}"
                }
            },
            "image_info": [
                {
                    "web_uri": "{{web_uri}}"
                }
            ]
        },
        {
            "creative_info": {
                "tiktok_item_id": "{{tiktok_item_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT",
                "identity_bc_id": "{{identity_bc_id}}"
            }
        },
        {
            "creative_info": {
                "image_info": [
                    {
                        "web_uri": "{{web_uri}}"
                    },
                    {
                        "web_uri": "{{web_uri}}"
                    }
                ],
                "music_info": {
                    "music_id": "{{music_id}}"
                }
            }
        },
        {
            "creative_info": {
                "music_info": {
                    "music_id": "{{music_id}}"
                }
            }
        }
    ],
    "ad_text_list": [
        {
            "ad_text": "{{ad_text}}"
        },
        {
            "ad_text": "{{ad_text}}"
        }
    ],
    "call_to_action_list": [
        {
            "call_to_action": "APPLY_NOW"
        },
        {
            "call_to_action": "DOWNLOAD_NOW"
        }
    ],
    "ad_configuration": {
        "product_specific_type": "ALL",
        "catalog_creative_toggle": true
    }
}'
```

### Xem trước các quảng cáo hiện có (Preview existing ads)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| preview_type  ****(Bắt buộc)**** | string | Preview type. ⏎ Enum value: • `AD`: preview an existing ad. |
| smart_plus_ad_id  ****(Bắt buộc)**** | string | ID of the Upgraded Smart+ Ad that you want to preview. ⏎ To obtain a list of Upgraded Smart+ Ad IDs, use [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/preview/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "preview_type": "AD",
    "smart_plus_ad_id": "{{smart_plus_ad_id}}"
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
| ↳ preview_link | string | Preview link. ⏎ Validity period: 30 days. |
| ↳ iframe | string | The iframe code snippet with the preview link. You can embed the iframe code into your HTML file. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "iframe": "<iframe src=\"https://ads.tiktok.com/ad_preview_tool?ad_preview_id={{ad_preview_id}}\"></iframe>",
        "preview_link": "{{preview_link}}"
    }
}
```

---

<a id="doc-1843310536069122"></a>
<!-- doc_id: 1843310536069122 -->
<!-- doc_id: 1843310536069122 -->
# Xét duyệt quảng cáo (Ad Review)
> Đường dẫn: API Reference > Upgraded Smart+ > Ad Review
Ad Review API cho phép bạn lấy thông tin xét duyệt cho các nhóm quảng cáo và mẫu quảng cáo, bao gồm trạng thái xét duyệt, lý do từ chối và đề xuất xử lý, hoặc yêu cầu đánh giá lại sau khi bị từ chối.

Nhóm này bao gồm các endpoint sau:
* [Get the review info of Upgraded Smart+ Ads](62-upgraded-smartplus-p6.md#doc-1843317465695233)
* [Get the review info of Upgraded Smart+ Ad creatives](62-upgraded-smartplus-p6.md#doc-1843317474334722)
* [Appeal rejection of an Upgraded Smart+ Ad](62-upgraded-smartplus-p6.md#doc-1843317522553106)

---

<a id="doc-1843317465695233"></a>
<!-- doc_id: 1843317465695233 -->
<!-- doc_id: 1843317465695233 -->
# Lấy thông tin xét duyệt của quảng cáo Smart+ nâng cấp (Get the review info of Upgraded Smart+ Ads)
> Đường dẫn: API Reference > Upgraded Smart+ > Ad Review > Get the review info of Upgraded Smart+ Ads
Sử dụng endpoint này để truy xuất kết quả xét duyệt của các quảng cáo Smart+ nâng cấp, bao gồm các mẫu sáng tạo bên trong quảng cáo.

Một mẫu quảng cáo cần phải được phê duyệt trước khi có thể phân phối, và có thể bị từ chối do nhiều nguyên nhân khác nhau, chẳng hạn như vị trí hiển thị hoặc nhắm mục tiêu không hợp lệ. Dựa trên lý do từ chối và đề xuất nhận được, bạn có thể chỉnh sửa mẫu quảng cáo tương ứng bằng cách sử dụng [/smart_plus/ad/update/](62-upgraded-smartplus-p6.md#doc-1843317411665921).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/review_info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| smart_plus_ad_ids  ****(Bắt buộc)**** | string[] | A list of Ad IDs. ⏎ Kích thước tối đa: 100. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |
| lang | string | The code of the language for the returned `reasons`,`suggestion`, and `specification` within the `reject_info` object array. ⏎ Để xem danh sách giá trị enum, xem List of values for `lang`. ⏎ Giá trị mặc định: `en`. |
| extra_info_setting | object | Additional settings. |
| ↳ include_reject_info | boolean | Có thực hiện include the reason for rejection. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| ↳ include_violation_frame | boolean | Có thực hiện include the video frames @that have been flagged for violations. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ **Note**: You can only set this field to `true` when `include_reject_info` is `true`. |

### Danh sách giá trị cho `lang`
Bảng sau đây liệt kê các giá trị enum cho `lang`.

| Language code (lang) | Language (Ngôn ngữ) |
|---|---|
| `ar` | Arabic |
| `cs-CZ` | Czech |
| `de` | German |
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `id` | Indonesian |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `ms` | Malay |
| `pl-PL` | Polish |
| `pt-BR` | Portuguese (Brazil) |
| `ru` | Russian |
| `sv-SE` | Swedish |
| `th` | Thai |
| `tr` | Turkish |
| `vi` | Vietnamese |
| `zh` | Simplified Chinese |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/review_info/?advertiser_id={{advertiser_id}}&smart_plus_ad_ids=["{{smart_plus_ad_ids}}"]&extra_info_setting={"include_reject_info": true, "include_violation_frame": true}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ smart_plus_ad_review_infos | object[] | Information about the review result for the ads. |
| ↳↳ smart_plus_ad_id | string | ID mẫu quảng cáo. |
| ↳↳ review_status | string | Trạng thái xét duyệt của mẫu quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `ALL_AVAILABLE`: The ad has been reviewed and can be delivered to all specified targeting countries. • `PART_AVAILABLE`: The ad has been reviewed and can only be delivered to some of the specified targeting countries. • `UNAVAILABLE`: The ad has been reviewed and cannot be delivered. |
| ↳↳ passed_locations | string[] | The targeted regions that passed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳ appeal_status | string | The appeal status of the ad. ⏎ Các giá trị enum hỗ trợ: • `NOT_APPEALED`: The appeal is not submitted. • `APPEALING`: The appeal is being processed. • `APPEAL_SUCCESSFUL`: The appeal has succeeded. • `APPEAL_FAILED`: The appeal failed. • `APPEAL_DONE`: The appeal went through an additional review. To confirm Liệu appeal succeeded or failed, check the `review_status` value. |
| ↳↳ appeal_reject_reasons | string[] | The reasons for rejecting the appeal. |
| ↳↳ reject_info | object[] | Details of the rejection. |
| ↳↳↳ reasons | string[] | The reasons for failing the ad review. |
| ↳↳↳ suggestion | string | The review suggestion. |
| ↳↳↳ forbidden_ages | string[] | The age groups that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ forbidden_locations | string[] | The codes of the targeted regions that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ forbidden_placements | string[] | The placements that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ content_info | object | Details of the content that was rejected. |
| ↳↳↳↳ content_type | string | Content type. ⏎ Các giá trị enum hỗ trợ: • `ModeString`: string. • `ModeImage`: image. • `ModeVideo`: video. • `ModeMusic`: music to be used in a carousel. • `LandingPage`: landing page. • `ModeCollection`: series collection. • `ModePhotoPost:` TikTok photo post. |
| ↳↳↳↳ text_content | string | The text that was rejected. |
| ↳↳↳↳ image_content | object | The image content that was rejected. |
| ↳↳↳↳↳ image_id | string | The ID of the image. |
| ↳↳↳↳ video_content | object | The video content that was rejected. |
| ↳↳↳↳↳ video_id | string | The ID of the video. |
| ↳↳↳↳ carousel_music_info | object | The music content in a carousel that was rejected. |
| ↳↳↳↳↳ music_id | string | The ID of the music. |
| ↳↳↳ violation_frames | object[] | Returned only when `include_violation_frame` is set to `true` in the request. ⏎ Details of the video frames that have been flagged for violations. |
| ↳↳↳↳ type | string | The type of frame. |
| ↳↳↳↳ video_id | string | ID video. |
| ↳↳↳↳ web_url_list | string[] | A list of image URLs or landing page URLs flagged for violations. |
| ↳↳↳↳ violation_frame_material_type | string | The type of creative that was considered a violative item in the frame. ⏎ Các giá trị enum hỗ trợ: • `DOWNLOAD URL`: Download URL. • `EXTERNAL_URL`: Landing page URL. • `INSTANT_PAGE`: TikTok Instant Page. • `LEAD_GENERATION`: Instant Form. • `OPEN_URL`: Deeplink. • `VIDEO`: Video. • `UNSET`: Other. |
| ↳↳↳ specification | string | An auto-generated summary for the rejection reason. |
| ↳↳↳ video_violation_frames | object[] | Details of images flagged for violations. |
| ↳↳↳↳ web_url | string | The URL of the image of a specific frame where a violation has occurred. |
| ↳↳↳↳ hover_periods | string[] | A list of time periods when violations occur in hover images. |
| ↳↳↳↳ thumbnail_periods | string[] | A list of time periods when violations occur in thumbnail images. |
| ↳ material_review_infos | object[] | Information about the review result for the creatives. |
| ↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. ⏎ **Note**: For carousel creatives, this ID identifies an image inside the carousel, while the `ad_material_id` from [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914) identifies the entire carousel itself. |
| ↳↳ smart_plus_ad_id | string | ID mẫu quảng cáo. |
| ↳↳ review_status | string | Trạng thái xét duyệt của mẫu sáng tạo. ⏎ Các giá trị enum hỗ trợ: • `ALL_AVAILABLE`: The creative has been reviewed and can be delivered to all specified targeting countries. • `PART_AVAILABLE`: The creative has been reviewed and can only be delivered to some of the specified targeting countries. • `UNAVAILABLE`: The creative has been reviewed and cannot be delivered. |
| ↳↳ passed_locations | string[] | The targeted regions that passed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳ reject_info | object[] | Details of the rejection. |
| ↳↳↳ reasons | string[] | The reasons for failing the ad review. |
| ↳↳↳ suggestion | string | The review suggestion. |
| ↳↳↳ forbidden_ages | string[] | The age groups that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ forbidden_locations | string[] | The codes of the targeted regions that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ forbidden_placements | string[] | The placements that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ content_info | object | Details of the content that was rejected. |
| ↳↳↳↳ content_type | string | Content type. ⏎ Các giá trị enum hỗ trợ: • `ModeString`: string. • `ModeImage`: image. • `ModeVideo`: video. • `ModeMusic`: music to be used in a carousel. • `LandingPage`: landing page. • `ModeCollection`: series collection. • `ModePhotoPost:` TikTok photo post. |
| ↳↳↳↳ text_content | string | The text that was rejected. |
| ↳↳↳↳ image_content | object | The image content that was rejected. |
| ↳↳↳↳↳ image_id | string | The ID of the image. |
| ↳↳↳↳ video_content | object | The video content that was rejected. |
| ↳↳↳↳↳ video_id | string | The ID of the video. |
| ↳↳↳↳ carousel_music_info | object | The music content in a carousel that was rejected. |
| ↳↳↳↳↳ music_id | string | The ID of the music. |
| ↳↳↳ violation_frames | object[] | Returned only when `include_violation_frame` is set to `true` in the request. ⏎ Details of the video frames that have been flagged for violations. |
| ↳↳↳↳ type | string | The type of frame. |
| ↳↳↳↳ video_id | string | ID video. |
| ↳↳↳↳ web_url_list | string[] | A list of image URLs or landing page URLs flagged for violations. |
| ↳↳↳↳ violation_frame_material_type | string | The type of creative that was considered a violative item in the frame. ⏎ Các giá trị enum hỗ trợ: • `DOWNLOAD URL`: Download URL. • `EXTERNAL_URL`: Landing page URL. • `INSTANT_PAGE`: TikTok Instant Page. • `LEAD_GENERATION`: Instant Form. • `OPEN_URL`: Deeplink. • `VIDEO`: Video. • `UNSET`: Other. |
| ↳↳↳ specification | string | An auto-generated summary for the rejection reason. |
| ↳↳↳ video_violation_frames | object[] | Details of images flagged for violations. |
| ↳↳↳↳ web_url | string | The URL of the image of a specific frame where a violation has occurred. |
| ↳↳↳↳ hover_periods | string[] | A list of time periods when violations occur in hover images. |
| ↳↳↳↳ thumbnail_periods | string[] | A list of time periods when violations occur in thumbnail images. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "material_review_infos": [
            {
                "ad_material_id": "{{ad_material_id}}",
                "passed_locations": null,
                "reject_info": null,
                "review_status": "ALL_AVAILABLE",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            },
            {
                "ad_material_id": "{{ad_material_id}}",
                "passed_locations": null,
                "reject_info": null,
                "review_status": "ALL_AVAILABLE",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            }
        ],
        "smart_plus_ad_review_infos": [
            {
                "appeal_reject_reasons": null,
                "appeal_status": "NOT_APPEALED",
                "passed_locations": null,
                "reject_info": [],
                "review_status": "ALL_AVAILABLE",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1843317474334722"></a>
<!-- doc_id: 1843317474334722 -->
<!-- doc_id: 1843317474334722 -->
# Lấy thông tin xét duyệt mẫu sáng tạo của quảng cáo Smart+ nâng cấp (Get the review info of Upgraded Smart+ Ad creatives)
> Đường dẫn: API Reference > Upgraded Smart+ > Ad Review > Get the review info of Upgraded Smart+ Ad creatives
Sử dụng endpoint này để truy xuất kết quả xét duyệt của các mẫu sáng tạo bên trong quảng cáo Smart+ nâng cấp.

Một mẫu sáng tạo cần phải được phê duyệt trước khi có thể phân phối, và có thể bị từ chối do nhiều lý do khác nhau, chẳng hạn như cấu hình vị trí hiển thị hoặc nhắm mục tiêu không phù hợp. Dựa trên các lý do từ chối và gợi ý nhận được, bạn có thể chỉnh sửa mẫu sáng tạo tương ứng bằng cách sử dụng [/smart_plus/ad/update/](62-upgraded-smartplus-p6.md#doc-1843317411665921).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/material/review_info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| ad_material_ids  ****(Bắt buộc)**** | string[] | A list of ad material IDs for creatives to operate on. ⏎ An ad material ID is an ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. ⏎ Kích thước tối đa: 100. ⏎ To obtain ad material IDs associated with an ad, use [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). ⏎ **Note**: For images within a carousel, you need to provide the `ad_material_id` from [/smart_plus/ad/review_info/](62-upgraded-smartplus-p6.md#doc-1843317465695233), not the one from [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914) which identifies the entire carousel. |
| lang | string | The code of the language for the returned `reasons`,`suggestion`, and `specification` within the `reject_info` object array. ⏎ Để xem danh sách giá trị enum, xem List of values for `lang`. ⏎ Giá trị mặc định: `en`. |
| extra_info_setting | object | Additional settings. |
| ↳ include_reject_info | boolean | Có thực hiện include the reason for rejection. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| ↳ include_violation_frame | boolean | Có thực hiện include the video frames that have been flagged for violations. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ **Note**: You can only set this field to `true` when `include_reject_info` is `true`. |

### Danh sách giá trị cho `lang`
Bảng sau đây liệt kê các giá trị enum cho `lang`.

| Languag ecode (lang) | Language (Ngôn ngữ) |
|---|---|
| `ar` | Arabic |
| `cs-CZ` | Czech |
| `de` | German |
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `id` | Indonesian |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `ms` | Malay |
| `pl-PL` | Polish |
| `pt-BR` | Portuguese (Brazil) |
| `ru` | Russian |
| `sv-SE` | Swedish |
| `th` | Thai |
| `tr` | Turkish |
| `vi` | Vietnamese |
| `zh` | Simplified Chinese |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/material/review_info/?advertiser_id={{advertiser_id}}&ad_material_ids=["{{ad_material_ids}}"]&extra_info_setting={"include_reject_info": true, "include_violation_frame": true}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ material_review_infos | object[] | Information about the review result for the creatives. |
| ↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳↳ smart_plus_ad_id | string | ID mẫu quảng cáo. |
| ↳↳ passed_locations | string[] | The targeted regions that passed the review. |
| ↳↳ review_status | string | Trạng thái xét duyệt của mẫu sáng tạo. ⏎ Các giá trị enum hỗ trợ: • `ALL_AVAILABLE`: The creative has been reviewed and can be delivered to all specified targeting countries. • `PART_AVAILABLE`: The creative has been reviewed and can only be delivered to some of the specified targeting countries. • `UNAVAILABLE`: The creative has been reviewed and cannot be delivered. |
| ↳↳ reject_info | object[] | Details of the rejection. |
| ↳↳↳ reasons | string[] | The reasons for failing the ad review. |
| ↳↳↳ suggestion | string | The review suggestion. |
| ↳↳↳ forbidden_ages | string[] | The age groups that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ forbidden_locations | string[] | The codes of the targeted regions that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ forbidden_placements | string[] | The placements that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ content_info | object | Details of the content that was rejected. |
| ↳↳↳↳ content_type | string | Content type. ⏎ Các giá trị enum hỗ trợ: • `ModeString`: string. • `ModeImage`: image. • `ModeVideo`: video. • `ModeMusic`: music to be used in a carousel. • `LandingPage`: landing page. • `ModeCollection`: series collection. • `ModePhotoPost:` TikTok photo post. |
| ↳↳↳↳ text_content | string | The text that was rejected. |
| ↳↳↳↳ image_content | object | The image content that was rejected. |
| ↳↳↳↳↳ image_id | string | The ID of the image. |
| ↳↳↳↳ video_content | object | The video content that was rejected. |
| ↳↳↳↳↳ video_id | string | The ID of the video. |
| ↳↳↳↳ carousel_music_info | object | The music content in a carousel that was rejected. |
| ↳↳↳↳↳ music_id | string | The ID of the music. |
| ↳↳↳ violation_frames | object[] | Returned only when `include_violation_frame` is set to `true` in the request. ⏎ Details of the video frames that have been flagged for violations. |
| ↳↳↳↳ type | string | The type of frame. |
| ↳↳↳↳ video_id | string | ID video. |
| ↳↳↳↳ web_url_list | string[] | A list of image URLs or landing page URLs flagged for violations. |
| ↳↳↳↳ violation_frame_material_type | string | The type of creative that was considered a violative item in the frame. ⏎ Các giá trị enum hỗ trợ: • `DOWNLOAD URL`: Download URL. • `EXTERNAL_URL`: Landing page URL. • `INSTANT_PAGE`: TikTok Instant Page. • `LEAD_GENERATION`: Instant Form. • `OPEN_URL`: Deeplink. • `VIDEO`: Video. • `UNSET`: Other. |
| ↳↳↳ specification | string | An auto-generated summary for the rejection reason. |
| ↳↳↳ video_violation_frames | object[] | Details of images flagged for violations. |
| ↳↳↳↳ web_url | string | The URL of the image of a specific frame where a violation has occurred. |
| ↳↳↳↳ hover_periods | string[] | A list of time periods when violations occur in hover images. |
| ↳↳↳↳ thumbnail_periods | string[] | A list of time periods when violations occur in thumbnail images. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "material_review_infos": [
            {
                "ad_material_id": "{{ad_material_id}}",
                "passed_locations": null,
                "reject_info": [],
                "review_status": "ALL_AVAILABLE",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1843317522553106"></a>
<!-- doc_id: 1843317522553106 -->
<!-- doc_id: 1843317522553106 -->
# Kháng nghị từ chối duyệt quảng cáo Smart+ nâng cấp (Appeal rejection of an Upgraded Smart+ Ad)
> Đường dẫn: API Reference > Upgraded Smart+ > Ad Review > Appeal rejection of an Upgraded Smart+ Ad
Sử dụng endpoint này để kháng nghị việc từ chối duyệt một quảng cáo Smart+ nâng cấp, cho phép bạn yêu cầu đánh giá lại quảng cáo khi quảng cáo đó bị từ chối trong quá trình xét duyệt.

Sau khi gửi kháng nghị, bạn cần chờ một khoảng thời gian rồi gọi endpoint [/smart_plus/ad/review_info/](62-upgraded-smartplus-p6.md#doc-1843317465695233) để kiểm tra trạng thái kháng nghị và xem trạng thái xét duyệt đã được cập nhật hay chưa.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/appeal/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Giá trị được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| smart_plus_ad_id  ****(Bắt buộc)**** | string | ID mẫu quảng cáo. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). |
| appeal_reason | string | The reason for the appeal. |
| attachment_list | string[] | List of attachment links. ⏎ Kích thước tối đa: 100. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/appeal/' \
--header 'Access-Token: &#123;&#123;Access-Token&#125;&#125;' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "&#123;&#123;advertiser_id&#125;&#125;",
    "smart_plus_ad_id": "&#123;&#123;smart_plus_ad_id&#125;&#125;"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. ⏎ For a successful request, this field will be an empty object (`{}`). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1843310542601218"></a>
<!-- doc_id: 1843310542601218 -->
<!-- doc_id: 1843310542601218 -->
# Báo cáo (Reporting)
> Đường dẫn: API Reference > Upgraded Smart+ > Reporting
Bạn có thể sử dụng Reporting API để chạy báo cáo về dữ liệu quảng cáo của mình.

Nhóm này bao gồm các endpoint sau:
* [Run an Upgraded Smart+ Creative Overview Report](62-upgraded-smartplus-p6.md#doc-1843317489576961)
* [Run an Upgraded Smart+ Creative Breakdown Report](62-upgraded-smartplus-p7.md#doc-1843317510389761)

---

<a id="doc-1843317489576961"></a>
<!-- doc_id: 1843317489576961 -->
<!-- doc_id: 1843317489576961 -->
# Chạy báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp (Run an Upgraded Smart+ Creative Overview Report)
> Đường dẫn: API Reference > Upgraded Smart+ > Reporting > Run an Upgraded Smart+ Creative Overview Report
Sử dụng endpoint này để truy xuất Báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp (Upgraded Smart+ Creative Overview Report), tổng quan về dữ liệu báo cáo hiệu suất của các mẫu sáng tạo trong quảng cáo Smart+ nâng cấp.

Báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp không hỗ trợ phân tích chi tiết (breakdown) theo phạm vi thời gian (giờ, ngày, tuần hoặc tháng).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/material_report/overview/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| dimensions  ****(Bắt buộc)**** | string[] | Dimension grouping conditions. ⏎ For example, `["campaign_id", "main_material_id"]` indicates that both `campaign_id` and `main_material_id` are grouped. ⏎ To learn about available dimensions and supported dimension groupings, see [Supported dimensions](62-upgraded-smartplus-p6.md#doc-1843337892165889). |
| metrics | string[] | Metrics to query. ⏎ Giá trị mặc định: `["spend", "impressions"]`. ⏎ Note that the amount of currency metrics is based on the currency of the ad account (`advertiser_id`). ⏎ To learn about the supported metrics at the ad level, see [Supported ad-level metrics for Upgraded Smart+ Creative Reports](62-upgraded-smartplus-p7.md#doc-1843337909199938). |
| filtering | object | Điều kiện lọc dữ liệu. |
| ↳ campaign_ids | string[] | A list of campaign IDs. ⏎ Kích thước tối đa: 200. ⏎ To obtain campaign IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). ⏎ • Filter combination rule: You cannot combine the filter `campaign_ids` with the filter `adgroup_ids` or `smart_plus_ad_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` |
| ↳ adgroup_ids | string[] | A list of ad group IDs. ⏎ Kích thước tối đa: 200. ⏎ To obtain ad group IDs, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). ⏎ •  Filter combination rule: You cannot combine the filter `adgroup_ids` with the filter `campaign_ids` or `smart_plus_ad_ids`. • Filter and dimension combination limitation: You can combine the filter with any of the following dimensions: • `advertiser_id` • `adgroup_id` • `smart_plus_ad_id` |
| ↳ smart_plus_ad_ids | string[] | A list of ad IDs. ⏎ Kích thước tối đa: 200. ⏎ Để lấy ID quảng cáo, sử dụng [/smart_plus/ad/get/](62-upgraded-smartplus-p4.md#doc-1843317378982914). ⏎ • Filter combination rule: You cannot combine the filter `smart_plus_ad_ids` with the filter `campaign_ids` or `adgroup_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `smart_plus_ad_id` |
| ↳ main_material_types | string[] | A list of main creative types. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_NON_SPARK_ADS`: Video (non-Spark Ads). • `VIDEO_SPARK_ADS`: Video (Spark Ads). • `CAROUSEL_NON_SPARK_ADS`: Carousel (non-Spark Ads). • `CAROUSEL_SPARK_ADS`: Carousel (Spark Ads). • `SINGLE_IMAGE_NON_SPARK_ADS`: Single image (non-Spark Ads). • `CATALOG_VIDEO`: Catalog video. • `CATALOG_VIDEO_TEMPLATE`: Catalog video template. • `CATALOG_CAROUSEL`: Catalog carousel. • `CATALOG_MULTI_SHOW`: Catalog Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. ⏎ • Filter combination rule: The filter `main_material_types` can be used alone. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` |
| ↳ main_material_ids | string[] | A list of of main creative IDs. ⏎ • Filter combination rule: When you use this filter, you can specify up to 400 IDs in total for the filters `main_material_ids`, `ad_text_entity_ids`, `call_to_action_entity_ids`, and `interactive_add_on_entity_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` ⏎ **Note**: When you use the filter `main_material_id`, you need to specify the filter `main_material_types` simultaneously and filter only one type. |
| ↳ ad_text_entity_ids | string[] | A list of ad text entity IDs. ⏎ The ID is a system-generated unique identifier for an ad text. ⏎ • Filter combination rule: When you use this filter, you can specify up to 400 IDs in total for the filters `main_material_ids`, `ad_text_entity_ids`, `call_to_action_entity_ids`, and `interactive_add_on_entity_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` |
| ↳ call_to_action_entity_ids | string[] | A list of call-to-action entity IDs. ⏎ The ID is a system-generated unique identifier for a call-to-action. ⏎ • Filter combination rule: When you use this filter, you can specify up to 400 IDs in total for the filters `main_material_ids`, `ad_text_entity_ids`, `call_to_action_entity_ids`, and `interactive_add_on_entity_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` |
| ↳ interactive_add_on_entity_ids | string[] | Danh sách các tiện ích bổ sung tương tác (interactive add-on) entity IDs. ⏎ The ID is a system-generated unique identifier for an interactive add-on. ⏎ • Filter combination rule: When you use this filter, you can specify up to 400 IDs in total for the filters `main_material_ids`, `ad_text_entity_ids`, `call_to_action_entity_ids`, and `interactive_add_on_entity_ids`. • Filter and dimension combination rule: You can combine the filter with any of the following dimensions: • `advertiser_id` • `campaign_id` • `adgroup_id` • `smart_plus_ad_id` |
| query_lifetime | boolean | Có thực hiện request lifetime metrics. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ If you set `query_lifetime` to `true`, the parameters `start_date` and `end_date` will be ignored. |
| start_date **(Điều kiện)** | string | Bắt buộc khi `query_lifetime` is `false` or not specified. ⏎ Query start date (closed interval) in the format of `YYYY-MM-DD`. ⏎ The date is based on the ad account time zone. |
| end_date **(Điều kiện)** | string | Bắt buộc khi `query_lifetime` is `false` or not specified. ⏎ Query end date (closed interval) in the format of `YYYY-MM-DD`. ⏎ The date is based on the ad account time zone. ⏎ **Note**: The time difference between `start_date` and `end_date` must be equal to or less than 365 days. |
| sort_field | string | Sorting field. ⏎ Default sorting field: `spend`. ⏎ All supported metrics (excluding attribute metrics) support sorting. |
| sort_type | string | Thứ tự sắp xếp kết quả. ⏎ Các giá trị enum hỗ trợ: `ASC` (ascending), `DESC`(descending). ⏎ Giá trị mặc định: `DESC`. |
| page | number | Current Số trang cần lấy dữ liệu. ⏎ Value range: ≥1. ⏎ Giá trị mặc định: 1. |
| page_size | number | Page size. ⏎ Value range: 1-100. ⏎ Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/material_report/overview/?advertiser_id={{advertiser_id}}&dimensions=["smart_plus_ad_id","main_material_id"]&metrics=["spend"]&filtering={"smart_plus_ad_ids": ["{{smart_plus_ad_id}}"]}&start_date={{start_date}}&end_date={{end_date}}&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ list | object[] | Data list. |
| ↳↳ dimensions | object | Dimension data. |
| ↳↳↳ advertiser_id | string | Returned when the parameter `dimensions` contains `advertiser_id` in the request. ⏎ ID tài khoản quảng cáo TikTok. |
| ↳↳↳ campaign_id | string | Returned when the parameter `dimensions` contains `campaign_id` in the request. ⏎ ID chiến dịch quảng cáo. |
| ↳↳↳ adgroup_id | string | Returned when the parameter `dimensions` contains `adgroup_id` in the request. ⏎ ID nhóm quảng cáo. |
| ↳↳↳ smart_plus_ad_id | string | Returned when the parameter `dimensions` contains `smart_plus_ad_id`in the request. ⏎ ID mẫu quảng cáo. |
| ↳↳↳ main_material_id | string | Returned when the parameter `dimensions` contains `main_material_id` in the request. ⏎ Material ID. ⏎ • When `main_material_type` is `VIDEO_NON_SPARK_ADS`, `CATALOG_VIDEO`, or `SINGLE_IMAGE_NON_SPARK_ADS`, this field represents the ID of a main creative. • When `main_material_type` is `VIDEO_SPARK_ADS` or `CAROUSEL_SPARK_ADS`, this field represents the ID of TikTok post. • When `main_material_type` is `CATALOG_VIDEO_TEMPLATE`, `CATALOG_CAROUSEL`, or `CATALOG_MULTI_SHOW`, this field represents the ID of a catalog. • When `main_material_type` is `CAROUSEL_NON_SPARK_ADS`, this field represents the ID of a carousel. |
| ↳↳↳ main_material_type | string | Returned when the parameter `dimensions` contains `main_material_id` in the request. ⏎ Main creative type. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_NON_SPARK_ADS`: Video (non-Spark Ads). • `VIDEO_SPARK_ADS`: Video (Spark Ads). • `CAROUSEL_NON_SPARK_ADS`: Carousel (non-Spark Ads). • `CAROUSEL_SPARK_ADS`: Carousel (Spark Ads). • `SINGLE_IMAGE_NON_SPARK_ADS`: Single image (non-Spark Ads). • `CATALOG_VIDEO`: Catalog video. • `CATALOG_VIDEO_TEMPLATE`: Catalog video template. • `CATALOG_CAROUSEL`: Catalog carousel. • `CATALOG_MULTI_SHOW`: Catalog Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. |
| ↳↳↳ ad_text_entity_id | string | Ad text entity ID. ⏎ The ID is a system-generated unique identifier for an ad text. |
| ↳↳↳ ad_text_entity_type | string | Ad text entity type. ⏎ Enum value: • `text`: ad text. |
| ↳↳↳ call_to_action_entity_id | string | Call-to-action entity ID. ⏎ The ID is a system-generated unique identifier for a call-to-action. |
| ↳↳↳ call_to_action_entity_type | string | Call-to-action entity type. ⏎ Các giá trị enum hỗ trợ: • `manual_call_to_action`: standard call to action. • `dynamic_call_to_action`: dynamic call to action. |
| ↳↳↳ interactive_add_on_entity_id | string | Interactive add-on entity ID. ⏎ The ID is a system-generated unique identifier for an interactive add-on. |
| ↳↳↳ interactive_add_on_entity_type | string | Interactive add-on entity type. ⏎ Enum value: • `add_on`: interactive add-on. |
| ↳↳ metrics | object | Metric data. ⏎ If the parameter `dimensions` does not contain `smart_plus_ad_id` in the request, the following metrics will return an empty string (`""`) : • `ad_material_id` • `material_primary_status` • `material_second_status` • `operation_status` |
| ↳↳↳ {metric_name} | string | Returned metrics, which are determined by the `metrics` field specified in the request. |
| ↳↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳↳↳ main_material_name | string | Main creative name. |
| ↳↳↳ ad_text | string | Ad text. |
| ↳↳↳ call_to_action | string | Call-to-action. |
| ↳↳↳ interactive_add_on_name | string | Interactive add-on name. |
| ↳↳↳ interactive_add_on_id | string | Interactive add-on ID. ⏎ This ID is generated when you create the interactive add-on in the Creative Library and is different from `interactive_add_on_entity_id`. |
| ↳↳↳ material_primary_status | string | Returned when the parameter `dimensions` contains `smart_plus_ad_id` in the request. ⏎ The primary status of the creative. ⏎ Để xem danh sách giá trị enum, xem [List of values for `material_primary_status`](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ material_second_status_list | string[] | The list of secondary statuses of the creative. ⏎ Để xem danh sách giá trị enum, xem [List of values for `material_second_status_list`](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: When the parameter `dimensions` doesn't contain `smart_plus_ad_id` in the request, this field will not be returned. |
| ↳↳↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : enabled (in 'ON' status). • `DISABLE`: disabled (in 'OFF' status). • `FROZEN`: terminated and cannot be enabled. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "main_material_id": "{{main_material_id}}",
                    "main_material_type": "VIDEO_SPARK_ADS",
                    "smart_plus_ad_id": "{{smart_plus_ad_id}}"
                },
                "metrics": {
                    "main_material_name": "{{main_material_name}}",
                    "spend": "0.00"
                }
            },
            {
                "dimensions": {
                    "main_material_id": "{{main_material_id}}",
                    "main_material_type": "CAROUSEL_SPARK_ADS",
                    "smart_plus_ad_id": "{{smart_plus_ad_id}}"
                },
                "metrics": {
                    "main_material_name": "{{main_material_name}}",
                    "spend": "0.00"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 100,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1843337892165889"></a>
<!-- doc_id: 1843337892165889 -->
<!-- doc_id: 1843337892165889 -->
# Các chiều dữ liệu hỗ trợ cho báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp (Supported dimensions for Upgraded Smart+ Creative Overview Reports)
> Đường dẫn: API Reference > Upgraded Smart+ > Reporting > Run an Upgraded Smart+ Creative Overview Report > Supported dimensions for Upgraded Smart+ Creative Overview Reports
Dimension (Chiều dữ liệu) là thuộc tính dùng để nhóm dữ liệu của bạn.

Bảng sau đây trình bày chi tiết các chiều dữ liệu khả dụng và các nhóm chiều dữ liệu được hỗ trợ trong Báo cáo tổng quan mẫu sáng tạo Smart+ nâng cấp.

| Dimension name (Tên chiều dữ liệu) | Dimension type (Loại chiều dữ liệu) | Mô tả chi tiết | Các nhóm chiều dữ liệu được hỗ trợ |
|---|---|---|---|
| `advertiser_id` | Chiều dữ liệu quảng cáo | Nhóm theo ID tài khoản quảng cáo TikTok. | • `advertiser_id` x `main_material_id` • `advertiser_id` x `ad_text_entity_id` • `advertiser_id` x `call_to_action_entity_id` • `advertiser_id` x `interactive_add_on_entity_id` |
| `campaign_id` | Chiều dữ liệu quảng cáo | Group by ID chiến dịch quảng cáo. | • `campaign_id` x `main_material_id` • `campaign_id` x `ad_text_entity_id` • `campaign_id` x `call_to_action_entity_id` • `campaign_id` x `interactive_add_on_entity_id` |
| `adgroup_id` | Chiều dữ liệu quảng cáo | Group by ID nhóm quảng cáo. | • `adgroup_id` x `main_material_id` • `adgroup_id` x `ad_text_entity_id` • `adgroup_id` x `call_to_action_entity_id` • `adgroup_id` x `interactive_add_on_entity_id` |
| `smart_plus_ad_id` | Chiều dữ liệu quảng cáo | Group by ID mẫu quảng cáo. | • `smart_plus_ad_id` x `main_material_id` • `smart_plus_ad_id` x `ad_text_entity_id` • `smart_plus_ad_id` x `call_to_action_entity_id` • `smart_plus_ad_id` x `interactive_add_on_entity_id` |
| `main_material_id` | Chiều dữ liệu sáng tạo | Nhóm theo ID mẫu sáng tạo chính. | • `advertiser_id` x `main_material_id` • `campaign_id` x `main_material_id` • `adgroup_id` x `main_material_id` • `smart_plus_ad_id` x `main_material_id` |
| `ad_text_entity_id` | Chiều dữ liệu thiết lập | Nhóm theo ID thực thể văn bản quảng cáo. ⏎ The ID is a system-generated unique identifier for an ad text. | • `advertiser_id` x `ad_text_entity_id` • `campaign_id` x `ad_text_entity_id` • `adgroup_id` x `ad_text_entity_id` • `smart_plus_ad_id` x `ad_text_entity_id` |
| `call_to_action_entity_id` | Chiều dữ liệu thiết lập | Nhóm theo ID thực thể lời kêu gọi hành động (CTA). ⏎ The ID is a system-generated unique identifier for a call-to-action. | • `advertiser_id` x `call_to_action_entity_id` • `campaign_id` x `call_to_action_entity_id` • `adgroup_id` x `call_to_action_entity_id` • `smart_plus_ad_id` x `call_to_action_entity_id` |
| `interactive_add_on_entity_id` | Chiều dữ liệu thiết lập | Nhóm theo ID thực thể tiện ích bổ sung tương tác. ⏎ The ID is a system-generated unique identifier for an interactive add-on. | • `advertiser_id` x `interactive_add_on_entity_id` • `campaign_id` x `interactive_add_on_entity_id` • `adgroup_id` x `interactive_add_on_entity_id` • `smart_plus_ad_id` x `interactive_add_on_entity_id` |
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 6/7**:

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

