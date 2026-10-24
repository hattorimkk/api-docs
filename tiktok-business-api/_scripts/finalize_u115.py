import os

def finalize_u115():
    path = "docs/09-marketing-api/quan-ly-chien-dich-p2.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Automatic Enhancements remaining English
    text = text.replace("Mini series (MINI_SERIES)", "Phim ngắn nhiều tập (MINI_SERIES)")
    text = text.replace("The following tables detail the scenarios where `creative_auto_enhancement_strategy_list` can be used to enable Automatic Enhancements via the [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) endpoint.",
                        "Các bảng dưới đây nêu chi tiết các trường hợp có thể sử dụng `creative_auto_enhancement_strategy_list` để bật tính năng Tự động nâng cao qua endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).")
    text = text.replace("> For Manual Ads, only the following strategies are configurable via creative_auto_enhancement_strategy_list:\n> *   Video quality (`VIDEO_QUALITY`)\n> *   Music refresh (`MUSIC_REFRESH`)\n> *   Image quality (`IMAGE_QUALITY`)\n> *   Resize (`IMAGE_RESIZE`)",
                        "> Đối với quảng cáo thủ công (Manual Ads), chỉ có các chiến lược sau có thể định cấu hình qua `creative_auto_enhancement_strategy_list`:\n> *   Chất lượng video (`VIDEO_QUALITY`)\n> *   Làm mới âm nhạc (`MUSIC_REFRESH`)\n> *   Chất lượng hình ảnh (`IMAGE_QUALITY`)\n> *   Điều chỉnh kích thước (`IMAGE_RESIZE`)")
    text = text.replace("**Advertising objective** (virtual_objective_type and objective_type)",
                        "**Mục tiêu quảng cáo (Advertising objective)** (`virtual_objective_type` và `objective_type`)")
    text = text.replace("**Use catalog** (catalog_enabled and campaign_product_source)",
                        "**Sử dụng danh mục (Use catalog)** (`catalog_enabled` và `campaign_product_source`)")
    text = text.replace("Any of the following configurations: • catalog_enabled is set to true • campaign_product_source is set to CATALOG",
                        "Bất kỳ cấu hình nào sau đây: • `catalog_enabled` được đặt là `true` • `campaign_product_source` được đặt là `CATALOG`")
    text = text.replace("campaign_product_source as CATALOG", "`campaign_product_source` là `CATALOG`")
    text = text.replace("campaign_product_source as false", "`campaign_product_source` là `false`")
    text = text.replace("campaign_product_source as true", "`campaign_product_source` là `true`")
    text = text.replace("Not specified", "Không chỉ định")

    # FAQ Section
    faq_sec_old = """# FAQs
> Đường dẫn: Marketing API > Campaign Management > Guides > FAQs
This article summarizes FAQs about the Campaign Management API.

## Ad group 
Q1: **I specified `app_id` in the campaign creation endpoint (for example, /adgroup/create/), but got an error "DB record not found". Why would this happen?** 
Please check the `app_id` you are using. The `app_id` you specified in the request should be the mobile app ID rather than the API App ID that you can find on the Developer Portal. The mobile app ID is added to the ad account under the events manager, which you plan on promoting.

Q2: **How to create an ad group for Value Optimization?**
Check out [Value Optimization](quan-ly-chien-dich-p2.md#doc-1739381743067137) to find out how to enable Value Optimization.

Q3:  **How to configure interests and behavior targeting via API?**
Please use the following endpoints to configure targeting options for interests and behavior.
-  Interest targeting:
  - [/tool/interest_category/](../12-api-reference/70-tools-p1.md#doc-1737174348712961) : Get available interest categories.
  - [/tool/interest_keyword/recommend/](../12-api-reference/70-tools-p1.md#doc-1763590884474882): Get recommended interest keywords. 
  - [/tool/interest_keyword/get/](../12-api-reference/70-tools-p1.md#doc-1763590894544897) : Get available interest keywords by ID.
- Video interactions:
  - [/tool/action_category/](../12-api-reference/70-tools-p1.md#doc-1737166752522241) : Get available video interaction categories(action_scene = VIDEO_RELATED in the response). 
  - [/tool/targeting_category/recommend/](../12-api-reference/70-tools-p1.md#doc-1736275204260866) : Get recommended video interaction categories ( scene = VIDEO_RELATED in the response)
- Creator interactions: 
  - [/tool/action_category/](../12-api-reference/70-tools-p1.md#doc-1737166752522241) : Get available creator interaction categories (action_scene = CREATOR_RELATED in the response). 
  - [/tool/targeting_category/recommend/](../12-api-reference/70-tools-p1.md#doc-1736275204260866) :  Get recommended creator interaction categories (scene = CREATOR_RELATED in the response). 
- Hashtag interactions:
  - [/tool/hashtag/recommend/](../12-api-reference/70-tools-p1.md#doc-1736271339521025) : Get recommended hashtags.
  - [/tool/hashtag/get/](../12-api-reference/70-tools-p1.md#doc-1736280889167874) : Get hashtags by IDs. 
 
## Ad 
 Q1: **I received an error message "The creative type is not consistent with your ad group settings. Please change the creative type in your ad group settings." when calling the /ad/create/ endpoint.**
The reason for this error message is your ad group has enabled Automated Creative Optimization (ACO)(`creative_material_mode` = `DYNAMIC`), but you used the 'regular' ad creation endpoints /ad/create/ to create ACO ads. To resolve this, you should use [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626) instead to create ACO ads.

Q2: **I received an error message " Unsupported image size. Please upload another image"  when calling the /ad/create/ endpoint. Why would this error message occur?**
Your image did not meet our requirements. See [Image Ads Specification](https://ads.tiktok.com/help/article/image-ads-specification?lang=en) or [Video Ads Specifications](https://ads.tiktok.com/help/article/video-ads-specifications?lang=en) to find out more detailed specifications.

Q3: **I received an error message "Invalid identity type" when calling the /identity/video/get/ endpoint. Why would this error message occur?** 
It might be due to passing `CUSTOMIZED_USER` as the `identity_type`. `CUSTOMIZED_USER` is not supported in the /identity/video/get/ endpoint, and the supported identity types are `AUTH_CODE`, `TT_USER` and `BC_AUTH_TT`.
Currently there are four types of authorized identities. The three identity types of `AUTH_CODE`, `TT_USER` and `BC_AUTH_TT`  do not have a `video_id`, but have a `tiktok_item_id` associated with them. If you want to create Spark Ads, you should use the three types. The fourth identity type `CUSTOMIZED_USER` has a `video_id`, meaning that you have an ad that is using a video uploaded to the Ads Manager Creative Library. Check out [Identities](quan-ly-chien-dich-p2.md#doc-1738958351620097) to learn more.

## Other
Q1: **I noticed that some parameters were not displayed in the response or were being ignored by the request, and why would this happen?**
One of the possible causes is you were using v1.2 syntax but the v1.3 API endpoint.
In API v1.3, we've updated the parameter names and types to make them more clear and meet industry standards.  For example, `placement` was renamed to `placements` in v1.3, and if you still use `placement`  as the request parameter in the /v1.3/adgroup/create/ endpoint, the parameter would be ignored. Please refer to the "Comparing v1.2 and v1.3" table in each API endpoint article to find out the detailed changes."""

    faq_sec_new = """# Các câu hỏi thường gặp (FAQs)
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
Trong API v1.3, tên và kiểu dữ liệu tham số đã được cập nhật chuẩn hóa. Ví dụ: tham số `placement` ở v1.2 đã đổi tên thành `placements` ở v1.3. Nếu bạn vẫn truyền `placement` vào endpoint `/v1.3/adgroup/create/`, hệ thống sẽ bỏ qua tham số này. Vui lòng tham khảo bảng "So sánh giữa v1.2 và v1.3" trong bài viết chi tiết của từng endpoint để cập nhật đúng tham số."""

    # Search for FAQ section start and end
    p_faq_start = text.find("# FAQs\n> Đường dẫn: Marketing API > Campaign Management > Guides > FAQs")
    p_faq_end = text.find("<a id=\"doc-1739381823123458\"></a>", p_faq_start)
    if p_faq_start != -1 and p_faq_end != -1:
        text = text[:p_faq_start] + faq_sec_new + "\n\n---\n\n" + text[p_faq_end:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done finalize_u115")

if __name__ == "__main__":
    finalize_u115()
