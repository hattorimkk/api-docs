# Smart+ phiên bản cũ (sắp ngừng hỗ trợ)

> Phân hệ: apiref:(To be deprecated) Legacy Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. (Sắp ngừng hỗ trợ) Smart+ phiên bản cũ (#doc-1765314260115458)](#doc-1765314260115458)
- [2. (Sắp ngừng hỗ trợ) Lấy hạn ngạch động cho chiến dịch Smart+ phiên bản cũ (#doc-1831564498409473)](#doc-1831564498409473)
- [3. (Sắp ngừng hỗ trợ) Tạo chiến dịch Smart+ phiên bản cũ (#doc-1767334204047362)](#doc-1767334204047362)
- [4. (Sắp ngừng hỗ trợ) Cập nhật chiến dịch Smart+ phiên bản cũ (#doc-1767334250066945)](#doc-1767334250066945)
- [5. (Sắp ngừng hỗ trợ) Lấy danh sách chiến dịch Smart+ phiên bản cũ (#doc-1767334299811842)](#doc-1767334299811842)
- [6. (Sắp ngừng hỗ trợ) Bật hoặc tắt mẫu sáng tạo trong chiến dịch Smart+ phiên bản cũ (#doc-1837969177953361)](#doc-1837969177953361)
- [7. (Sắp ngừng hỗ trợ) Chạy báo cáo chiến dịch Smart+ phiên bản cũ (#doc-1776454619412481)](#doc-1776454619412481)
- [8. (Sắp ngừng hỗ trợ) Các chỉ số trong báo cáo chiến dịch Smart+ phiên bản cũ (#doc-1776461365424129)](#doc-1776461365424129)

---

<a id="doc-1765314260115458"></a>
<!-- doc_id: 1765314260115458 -->
<!-- doc_id: 1765314260115458 -->
# (Sắp ngừng hỗ trợ) Smart+ phiên bản cũ (Legacy Smart+)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+
Chiến dịch Smart+ là giải pháp tự động hóa dựa trên AI của TikTok giúp tối đa hóa kết quả phân phối với ít nỗ lực nhất từ phía bạn. Smart+ API hỗ trợ bạn tích hợp các Chiến dịch Smart+ vào quy trình làm việc tùy chỉnh, nâng cao tính linh hoạt và khả năng mở rộng. Xem [Tạo chiến dịch Smart+ phiên bản cũ](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1768006268820546) để biết các bước chi tiết.

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.

Nhóm này gồm các endpoint sau:
- [Lấy hạn ngạch động cho chiến dịch Smart+ phiên bản cũ đang hoạt động](61-to-be-deprecated-legacy-smartplus.md#doc-1831564498409473)
- [Tạo chiến dịch Smart+ phiên bản cũ](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362)
- [Cập nhật chiến dịch Smart+ phiên bản cũ](61-to-be-deprecated-legacy-smartplus.md#doc-1767334250066945)
- [Lấy danh sách chiến dịch Smart+ phiên bản cũ](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842)
- [Bật hoặc tắt mẫu sáng tạo trong chiến dịch Smart+ phiên bản cũ](61-to-be-deprecated-legacy-smartplus.md#doc-1837969177953361)
- [Chạy báo cáo chiến dịch Smart+ phiên bản cũ](61-to-be-deprecated-legacy-smartplus.md#doc-1776454619412481)

---

<a id="doc-1831564498409473"></a>
<!-- doc_id: 1831564498409473 -->
<!-- doc_id: 1831564498409473 -->
# (Sắp ngừng hỗ trợ) Lấy hạn ngạch động cho chiến dịch Smart+ phiên bản cũ (Get the dynamic quota on Legacy Smart+ Campaigns)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Get the dynamic quota on Legacy Smart+ Campaigns
Sử dụng endpoint này để lấy thông tin hạn ngạch động về số lượng Chiến dịch Smart+ đang hoạt động trong một tài khoản quảng cáo.

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/spc/quota/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/quota/get/?advertiser_id={{advertiser_id}}' \
--header 'Access-token: {{Access-token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data|object|Returned data.|
#|total_quota|number|The total quota of active Smart+ Campaigns for the ad account.|
#|used_quota|number|The number of active Smart+ Campaigns within the ad account.|
#|used_campaign_ids|string[]|Returned only when `used_quota` is greater than 0.<br><br>The IDs of the active Smart+ Campaigns within the ad account.<br><br>To disable active Smart+ Campaigns, use [/campaign/status/update/](24-campaign.md#doc-1739320994354178) with `operation_status` set to `DISABLE`.|

```

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "active_campaign_ids": [
            "{{active_campaign_id}}",
            "{{active_campaign_id}}"
        ],
        "total_quota": 50,
        "used_quota": 2
    }
}
```
```


---

<a id="doc-1767334204047362"></a>
<!-- doc_id: 1767334204047362 -->
<!-- doc_id: 1767334204047362 -->
# (Sắp ngừng hỗ trợ) Tạo chiến dịch Smart+ phiên bản cũ (Create a Legacy Smart+ Campaign)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Create a Legacy Smart+ Campaign
Sử dụng endpoint này để tạo a Smart+ Campaign. 

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.
## Điều kiện tiên quyết trước khi bắt đầu
Check Liệu your ad account has reached the Smart+ Campaign quota by using [/campaign/spc/quota/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1831564498409473).

Nếu bạn không thể tạo chiến dịch Smart+ mới do đã đạt giới hạn hạn mức, hãy dùng `/campaign/spc/quota/get/` để xác định các chiến dịch Smart+ đang hoạt động. Sau đó bạn có thể tạm dừng một số chiến dịch đang hoạt động để giải phóng hạn mức bằng [/campaign/status/update/](24-campaign.md#doc-1739320994354178).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/spc/create/

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
| operation_status | string | The status of the campaign when created. ⏎ Các giá trị enum hỗ trợ: • `ENABLE`: The campaign is enabled when created. • `DISABLE`: The campaign is disabled when created.Giá trị mặc định: `ENABLE`. ⏎ If you want to update the status of the campaign after creation, use the [/campaign/status/update](24-campaign.md#doc-1739320994354178) endpoint. |
| objective_type  ****(Bắt buộc)**** | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. ⏎ To learn about the detailed steps for creating Smart+ Lead Generation Campaigns, see [Create Smart+ Lead Generation Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1827645480080385). |
| spc_type | string | Chỉ hợp lệ khi `objective_type` is `WEB_CONVERSIONS`. ⏎ The web campaign type. ⏎ Các giá trị enum hỗ trợ: • `WEB_ALL_IN_ONE`: Smart+ Web Campaign, where the supported optimization goals include Conversion, Value, Click and Landing page view. • `UNSET`(to-be-deprecated): Smart Performance Web Campaign, where the supported optimization goals are limited to Conversion, Value, and Click. Giá trị mặc định: `UNSET`. ⏎ To learn about the detailed steps for creating Smart+ Web Campaigns, see [Create Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ **Note**:  • Smart Performance Web Campaigns will be deprecated in the next API version. To ensure a smooth API integration, we recommend that you upgrade to [Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186) as soon as possible. Smart+ Web Campaigns are a new AI-powered automation solution that leverages machine learning to drive business outcomes for advertisers. • Once set, this field cannot be updated. |
| web_all_in_one_catalog_status | string | Chỉ hợp lệ khi `spc_type` is `WEB_ALL_IN_ONE`. ⏎ The status of catalog in the Smart+ Web Campaign. ⏎ Các giá trị enum hỗ trợ: •  `OPEN`: enabled. Smart+ Web Campaigns with catalog enabled are Smart+ Catalog Ads. To learn about the detailed steps for creating Smart+ Catalog Ads, see [Create Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186).  • `UNSET`: disabled. Smart+ Web Campaigns with catalog disabled are regular Smart+ Web Campaigns. To learn about the detailed steps for creating regular Smart+ Web Campaigns, see [Create a regular Smart+ Web Campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). Giá trị mặc định: `UNSET`. |
| app_promotion_type **(Điều kiện)** | string | Bắt buộc khi `objective_type` is `APP_PROMOTION`. ⏎ App promotion type. ⏎ Currently, we only support  `APP_INSTALL`. |
| virtual_objective_type | string | The new objective type. ⏎ Enum value: `SALES`. ⏎ Use this field to create a campaign with the Sales objective, the combined objective for Website Lượt chuyển đổi and Product Sales objectives. Learn more about [the Sales objective](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1834189283112962). |
| sales_destination**(Điều kiện)** | string | Required and Chỉ hợp lệ khi `virtual_objective_type` is specified. ⏎ Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. • When `sales_destination` is set to `WEB_AND_APP`, you need to set `web_all_in_one_catalog_status` to `OPEN`. • To learn about how to create Smart+ Campaigns with this setting, see [Create Smart+ Catalog Ads with Website and App Optimization](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1842232769643905). ⏎ **Note**: Creating Smart+ Catalog Ads with Website and App Optimization (with `sales_destination` set to `WEB_AND_APP`) is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| campaign_type | string | Campaign type. ⏎ Các giá trị enum hỗ trợ: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`. ⏎ Giá trị mặc định: `REGULAR_CAMPAIGN`. |
| campaign_app_profile_page_state | string | Có thực hiện use app profile page to optimize delivery. ⏎ Các giá trị enum hỗ trợ: `ON`, `OFF`. ⏎ Giá trị mặc định: `OFF`. ⏎ **Note:** • You can use the field only when `objective_type` is `APP_PROMOTION`and your campaign is an iOS 14 Dedicated Campaign. Otherwise, an error will occur. • When `ON` is selected, pass in the `page_id` of App Profile Page. •   To create an App Profile Page, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881) and set  `businessType` to `4`. |
| is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị enum hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ Để tìm hiểu cách tạo các chiến dịch này, xem [Create Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). ⏎ **Note**: Once set, this field cannot be updated. |
| disable_skan_campaign | boolean | Chỉ hợp lệ khi the following conditions are all met:  • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `IOS14_CAMPAIGN`. • `app_id` is set to the ID of an iOS app that is eligible for [Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). To confirm Liệu an app is eligible for Advanced Dedicated Campaigns, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `advanced_dedicated_campaign_allowed`. ⏎ Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition).  • For a Dedicated Campaign using an app that is eligible for Advanced Dedicated Campaigns, you need to enable SKAN attribution or Advanced Dedicated Campaign or both. You cannot disable SKAN attribution and Advanced Dedicated Campaign simultaneously. • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. • If you enable Advanced Dedicated Campaign by setting `is_advanced_dedicated_campaign` to `true` simultaneously, you'll be able to retrieve both [SAN](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) and [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. ⏎ **Note**:  • Disabling SKAN attribution for Dedicated Campaigns is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • If you are allowlisted for disabling SKAN attribution for Dedicated Campaigns, you cannot set `bid_type` to `BID_TYPE_CUSTOM` when the following conditions are all met: • `is_advanced_dedicated_campaign` is `false`. • `disable_skan_campaign` is `false`. • `optimization_goal` is `INSTALL` or `IN_APP_EVENT`. • Once set, this field cannot be updated. • Getting access to Advanced Dedicated Campaign requires the app to meet certain criteria. If your app is ineligible for Advanced Dedicated Campaign, reach out to your TikTok representative. Your TikTok representative will be able to provide troubleshooting support to help your app get access to Advanced Dedicated Campaign. |
| campaign_name  ****(Bắt buộc)**** | string | Campaign name. |
| special_industries | string[] | Ad categories. Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities.**Note:** ⏎ • Once you've specified the industry type, the system will adjust your target options to help you comply with advertising policies. See [Ad targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665) for details. • This field is only supported for advertisers who are registered in the US or Canada. |
| product_source **(Điều kiện)** | string | Bắt buộc khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| catalog_id **(Điều kiện)** | string | Bắt buộc khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ The ID of the catalog to use in the Smart+ Catalog Ads. ⏎ Currently, you can only specify an E-commerce catalog. ⏎ To retrieve the catalogs within your Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610). |
| catalog_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| product_specific_type **(Điều kiện)** | string | Bắt buộc khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products.  •  `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. ⏎ • If this field is set to `ALL`, you don't need to input `product_set_id` and `product_ids`.  • If this field is set to `PRODUCT_SET`, you need to pass in `product_set_id`.  • If this field is set to `CUSTOMIZED_PRODUCTS`, `product_ids` is required. |
| product_set_id **(Điều kiện)** | string | Bắt buộc khi `product_specific_type` is `PRODUCT_SET`. ⏎ The ID of a product set. ⏎ • To retrieve the product sets within your ad account, use [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169).  • To create a product set, use [/catalog/set/create/](29-catalog-product-sets.md#doc-1740572891104257). |
| product_ids **(Điều kiện)** | string[] | Bắt buộc khi `product_specific_type` is `CUSTOMIZED_PRODUCTS`. ⏎ The product IDs of the catalog products. ⏎ Kích thước tối đa: 20. ⏎ To retrieve the product ID (`product_id`) of each catalog product, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| promotion_type  ****(Bắt buộc)**** | string | Promotion type (Optimization location). You can decide where you'd like to promote your products using this field. ⏎ Currently, we support `APP_ANDROID`, `APP_IOS`, `WEBSITE`, and `LEAD_GENERATION`. ⏎ • When `objective_type` is `APP_PROMOTION`, set this field to `APP_ANDROID` or `APP_IOS`. • When `objective_type` is `WEB_CONVERSIONS`, set this field to `WEBSITE`. • When `objective_type` is `LEAD_GENERATION`, set this field to `LEAD_GENERATION`. |
| app_id **(Điều kiện)** | string | Bắt buộc khi `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`. ⏎ The App ID of the app to promote. ⏎ You can get `app_id` by using the [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) endpoint. |
| promotion_website_type | string | Chỉ hợp lệ khi `objective_type` is `WEB_CONVERSIONS` and `spc_type` is `UNSET` or not passed. ⏎ TikTok Instant Page type. ⏎ Currently, we only support `TIKTOK_NATIVE_PAGE`(To use TikTok Instant Page). ⏎ If you want to use TikTok Instant Page  in your ads,  you need to pass `page_id` of the TikTok Instant Page and `pixel_id` is not supported. |
| promotion_target_type **(Điều kiện)** | string | Bắt buộc khi `objective_type` is `LEAD_GENERATION`. ⏎ The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| optimization_goal  ****(Bắt buộc)**** | string | The measurable results you'd like to drive with your campaigns. ⏎ Currently, we support `CLICK`, `INSTALL`, `IN_APP_EVENT`, `VALUE`, `CONVERT`, `TRAFFIC_LANDING_PAGE_VIEW`, and `LEAD_GENERATION`. ⏎ To find the detailed description for each optimization goal, see [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| pixel_id **(Điều kiện)** | string | • Bắt buộc khi `optimization_goal` is set to `CONVERT` or `VALUE`. • Not supported when `optimization_goal` is not set to `CONVERT` or `VALUE`. ⏎ ID TikTok Pixel. ⏎ To obtain the list of Pixel IDs within your ad account, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978). |
| optimization_event**(Điều kiện)** | string | Required in any of the following scenarios: • `pixel_id` is specified. • `pixel_id` is not specified and `optimization_goal` is `IN_APP_EVENT` or `VALUE`. ⏎ Conversion event. ⏎ For the supported app and pixel events, see [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). ⏎ To find out the supported events for your app, use [/app/optimization_event/](43-events-1-0-p1.md#doc-1740859338750977). |
| app_config **(Điều kiện)** | object[] | Bắt buộc khi `sales_destination` is `WEB_AND_APP`. ⏎ Details of the app or apps to promote. ⏎ Kích thước tối đa: 2. ⏎ You can specify any of the following in this field: • an Android app • an iOS app • an Android app and an iOS app |
| ↳ app_id **(Điều kiện)** | string | Bắt buộc khi `app_config` is specified. ⏎ The App ID of the app to promote. ⏎ To obtain the list of App IDs within your ad account, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `app_id`. |
| deep_funnel_optimization_status | string | Chỉ hợp lệ khi `promotion_type` is `LEAD_GENERATION`. ⏎ The status of deep funnel optimization. ⏎ Deep funnel optimization optimizes both your upper funnel events and deeper funnel events. You can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: To enable deep funnel optimization.  •  `OFF`: To disable deep funnel optimization. Giá trị mặc định: `OFF`. ⏎ To learn about how to configure deep funnel optimization for Smart+ Lead Generation Campaigns, see [Create Smart+ Lead Generation Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1827645480080385). ⏎ **Note**:  • Deep funnel optimization with CRM events is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.  • Deep funnel optimization with Pixel or Offline events is generally available. |
| deep_funnel_event_source **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel.  • `OFFLINE`: Offline Event Set. • `CRM`: CRM Event Set. |
| deep_funnel_event_source_id **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. ⏎ • When `deep_funnel_event_source` is `PIXEL`, specify a ID TikTok Pixel via this field.   •  To obtain a list of Pixels, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978). • When `deep_funnel_event_source` is `OFFLINE`, specify an Offline Event Set ID via this field.   • To obtain a list of Offline Event Set IDs, use [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313).   • When `deep_funnel_event_source` is `CRM`, specify a CRM Event Set ID via this field.   • To obtain a list of CRM Event Set IDs, use [/crm/list/](43-events-1-0-p2.md#doc-1780896521680898). |
| deep_funnel_optimization_event **(Điều kiện)** | string | Bắt buộc khi `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ • To find out the supported values for Standard Events available for Pixels, Offline Event Sets, and CRM Event Sets, see the **"Event name for ad creation"** column in [Supported Pixel events](../09-marketing-api/do-luong-quang-cao-p2.md#doc-1739585696931842).   • To find the list of optimization events for a Pixel, use [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978) and check the returned `optimization_event`. ⏎ Example: `SHOPPING`. |
| bid_type | string | Bidding strategy that determines how the system manages your cost per result, spends your budget, and how it delivers campaigns. ⏎ Các giá trị enum hỗ trợ: • `BID_TYPE_NO_BID`: Maximum Delivery. • `BID_TYPE_CUSTOM`: Cost Cap (or Target CPA). |
| bid_price **(Điều kiện)** | float | Bắt buộc khi the following conditions are met: • `spc_type` is `WEB_ALL_IN_ONE` • `optimization_goal` is `CLICK`  • `bid_type` is `BID_TYPE_CUSTOM` ⏎ The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. |
| conversion_bid_price **(Điều kiện)** | float | Bắt buộc khi the following conditions are met:  • `spc_type` is `WEB_ALL_IN_ONE` • `optimization_goal` is `CONVERT` or `TRAFFIC_LANDING_PAGE_VIEW` •  `bid_type` is `BID_TYPE_CUSTOM` ⏎ The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `conversion_bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. |
| deep_bid_type | string | Bidding strategy for in-app events. ⏎ Currently, we only support `DEFAULT`,  `AEO`, `VO_MIN_ROAS` (supported only for Smart+ Web Campaigns), and `VO_HIGHEST_VALUE` in this field. ⏎ For the descriptions of supported values, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| roas_bid **(Điều kiện)** | float | Bắt buộc khi `deep_bid_type` is `VO_MIN_ROAS`. ⏎ Target ROAS for Value-Based Optimization. ⏎ Value range: 0.01-1,000. |
| vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7).   • `ZERO_DAY`: The current day (day 0).   Giá trị mặc định: `SEVEN_DAYS`. ⏎ • When the Minimum ROAS (Target ROAS) bidding strategy is used, this field represents the window type of the target ROAS value (Day 7 ROAS or Day 0 ROAS). The system will aim to keep your average ROAS of the seventh day or of the current day around or higher than the target ROAS value, regardless of your budget.  • When the Highest Value bidding strategy is used, this field represents the Highest Value window type (Day 7 Highest Value or Day 0 Highest Value). The system will aim to spend your budget fully and maximize the value of results within the first seven days or within the current day. ⏎ To learn more about how to use VBO IAA for your ad groups, see [Enable VBO for App](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1770019181843458). ⏎ **Note**:  • VBO IAP and VBO IAA in different scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. •  Day 0 or day 7 bidding (`vbo_window` is `ZERO_DAY` or `SEVEN_DAYS`) for **VBO IAP** in Advanced Dedicated Campaign or Android campaign scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. • Day 0 or day 7 bidding (`vbo_window` is `ZERO_DAY` or `SEVEN_DAYS`) for **VBO IAA** in Advanced Dedicated Campaign or Android campaign scenarios are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. • Once set, this field cannot be updated. |
| click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Use this field to define the timeframe during which conversions can be attributed to the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off.  •  `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click.  • `FOURTEEN_DAYS`: 14-day click. •  `TWENTY_EIGHT_DAYS`: 28-day click. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note:**  • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. •  If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922). •  Once set, this field cannot be updated. |
| engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Use this field to define the timeframe during which conversions can be attributed to the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. •  If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922). •  Once set, this field cannot be updated. |
| view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Use this field to define the timeframe during which conversions can be attributed to the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  • If you want to manually configure the attribution windows, you need to pass at least `click_attribution_window` and `view_attribution_window` simultaneously, and optionally `engaged_view_attribution_window`. Note that the `engaged_view_attribution_window`, once passed, must be accompanied by `click_attribution_window` and `view_attribution_window`. •  If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922). •  Once set, this field cannot be updated. |
| attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset.  •  `EVERY`: Every. To count multiple events from someone as separate conversions.  •  `ONCE`: Once. To count multiple events from someone as 1 conversion. ⏎ To learn about the allowed values of this field for different advertising objective scenarios, refer to [Attribution window and event count](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1777694366654465). ⏎ **Note**:  •  If you don't manually pass `click_attribution_window`, `engaged_view_attribution_window`, `view_attribution_window` and `attribution_event_count`, then default settings, if any, will be used. To confirm Liệu a default setting is used when you don't manually pass this field, use [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922). •  Once set, this field cannot be updated. |
| billing_event  ****(Bắt buộc)**** | string | Events that you want to pay for. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Billing Event](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ Currently, we only support `OCPM` and `CPC`. |
| location_ids  ****(Bắt buộc)**** | string[] | IDs of the locations that you want to target. ⏎ To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) or [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. ⏎ To get the list of location IDs, see **Location IDs**. ⏎ **Note:** ⏎ If you add the US as your target location, then you can not remove the US after campaign creation. |
| languages | string[] | Codes of the languages that you want to target. ⏎ For the list of language codes supported, see [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED` ⏎ Giá trị mặc định: `GENDER_UNLIMITED`. ⏎ **Note:** The field is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| spc_audience_age | string | The age group that the campaign targets. ⏎ Enum value: • `18+`: 18+. • `25+`: 25+. • The value `25+` is only available when `objective_type` is `LEAD_GENERATION`. ⏎ Giá trị mặc định: `18+`. |
| exclude_age_under_eighteen | boolean | Exclude the group aged under eighteen. ⏎ **Note:** Starting from September 21st, 2023, you can no longer target the audience aged under eighteen. The only supported value is `true`. |
| excluded_audience_ids | string[] | List of audience ID to be excluded. ⏎ You can get audience IDs by using the [/dmp/custom_audience/list/ ](09-audience.md#doc-1739940506015746)endpoint. |
| placement_type | string | The placement strategy that decides where your campaigns will be shown. ⏎ • `PLACEMENT_TYPE_NORMAL`: Select Placement. You can choose the apps to deliver your ads on. • `PLACEMENT_TYPE_AUTOMATIC`: Automatic placement. TikTok's ad system will use smart calculations to give you the best combination of ad placements across all apps. Giá trị mặc định: `PLACEMENT_TYPE_NORMAL`. ⏎ • For Smart+ Android App Campaigns (with `promotion_type` as `APP_ANDROID`), automated placement selection is a key feature.  • The system will automatically configure placements for your Smart+ Android App Campaigns based on your other settings and select high-quality traffic from various placements to deliver better results. If provided, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]` separately.  • To retrieve the exact placement setting of a Smart+ App Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  • For Smart+ iOS App Campaigns  (with `promotion_type` as `APP_IOS`), automated placement selection is a key feature. • Starting June 30th, 2025, the system will automatically configure placements for your Smart+ iOS App Campaigns based on your other settings and select high-quality traffic from various placements to deliver better results. If provided after June 30th, 2025, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]` separately. • To retrieve the exact placement setting of a Smart+ App Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  • For Smart+ Web Campaigns, automated placement selection is a key feature. The system will automatically configure placements based on your other settings and select high-quality traffic from various placements to deliver better results. If provided, the parameters `placement_type` and `placements` will be ignored. To retrieve the exact placement setting of a Smart+ Web Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  •  If the targeted locations (`location_ids`) of the campaign are all not supported for Pangle placement, the returned `placement_type` will be `PLACEMENT_TYPE_NORMAL` and `placements` will be `["PLACEMENT_TIKTOK"]`. •  If one or more targeted locations (`location_ids`) of the campaign are supported for Pangle placement, the returned `placement_type` will be `PLACEMENT_TYPE_AUTOMATIC` and `placements` will be `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]`. • For Smart+ Lead Generation Campaigns (with `promotion_type` as `LEAD_GENERATION`), manually configure the placement as TikTok. Set `placement_type` to `PLACEMENT_TYPE_NORMAL` and `placements` to `["PLACEMENT_TIKTOK"]`. ⏎ **Note:** • `placement_type` can not be updated after the campaign creation. • If you want to opt out of the Pangle placement, contact your TikTok representative. |
| placements | string[] | The apps where you want to deliver your ads. ⏎ Currently, we support `PLACEMENT_TIKTOK`. ⏎ • For Smart+ Android App Campaigns (with `promotion_type` as `APP_ANDROID`), automated placement selection is a key feature. The system will automatically configure placements for your Smart+ Android App campaigns based on your other settings and select high-quality traffic from various placements to deliver better results. If provided, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]` separately. To retrieve the exact placement setting of a Smart+ App Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  • For Smart+ iOS App Campaigns  (with `promotion_type` as `APP_IOS`), automated placement selection is a key feature. Starting June 30th, 2025, the system will automatically configure placements for your Smart+ iOS App campaigns based on your other settings and select high-quality traffic from various placements to deliver better results. If provided after June 30th, 2025, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]` separately. To retrieve the exact placement setting of a Smart+ App Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  • For Smart+ Web Campaigns, automated placement selection is a key feature. The system will automatically configure placements based on your other settings and select high-quality traffic from various placements to deliver better results. If provided, the parameters `placement_type` and `placements` will be ignored. To retrieve the exact placement setting of a Smart+ Web Campaign, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).  •  If the targeted locations (`location_ids`) of the campaign are all not supported for Pangle placement, the returned `placement_type` will be `PLACEMENT_TYPE_NORMAL` and `placements` will be `["PLACEMENT_TIKTOK"]`. •  If one or more targeted locations (`location_ids`) of the campaign are supported for Pangle placement, the returned `placement_type` will be `PLACEMENT_TYPE_AUTOMATIC` and `placements` will be `["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"]`. • For Smart+ Lead Generation Campaigns (with `promotion_type` as `LEAD_GENERATION`), manually configure the placement as TikTok. Set `placement_type` to `PLACEMENT_TYPE_NORMAL` and `placements` to `["PLACEMENT_TIKTOK"]`. ⏎ **Note**:  • `placements` can not be updated after the campaign creation. |
| comment_disabled | boolean | Có thực hiện allow comments on your campaigns on TikTok. ⏎ Giá trị mặc định: `false`. |
| share_disabled | boolean | Có thực hiện disable sharing of the campaign to third-party platforms. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| video_download_disabled | boolean | Liệu users can download your video ads on TikTok(can not be updated once created). ⏎ Giá trị mặc định: `false`. |
| blocked_pangle_app_ids | string[] | Pangle app block ID list. ⏎ You can get an ID via the `app_package_id` field returned by [Get Pangle block list](55-pangle.md#doc-1740039957181441). ⏎ Do not specify this field when you set `placements` only as `PLACEMENT_TIKTOK`. |
| budget_mode | string | Budget mode. ⏎ Các giá trị enum hỗ trợ: ` BUDGET_MODE_DAY`, `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ Giá trị mặc định: `BUDGET_MODE_DAY`. ⏎ To learn about how to set budget modes, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). ⏎ **Note**:  • Currently, this field cannot be updated after creation. • For Smart+ Lead Generation Campaigns, the only supported value is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The daily budget strategy. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable automatic budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. ⏎ **Note**: Enabling automatic budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget  ****(Bắt buộc)**** | float | Fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. ⏎ To learn about the minimum budget and how to set budget modes, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). ⏎ To directly see the daily budget value range for a currency, see [Currency-Daily budget value range](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| schedule_type  ****(Bắt buộc)**** | string | Schedule type. ⏎ Currently, we support `SCHEDULE_START_END` and `SCHEDULE_FROM_NOW`. |
| schedule_start_time  ****(Bắt buộc)**** | string | Schedule start time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The start time can be up to 12 hours earlier than the current time, but cannot be later than `2028-01-01 00:00:00`. |
| schedule_end_time **(Điều kiện)** | string | Schedule end time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The end time cannot be later than `2038-01-01 00:00:00`. |
| dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: If not specified, all-0, or all-1 are considered as full-time delivery. |
| identity_type  **(Điều kiện)** | string | Bắt buộc khi you are not using Spark Ads (`tiktok_item_id`). ⏎ Identity type for non-Spark Ads. ⏎ Enum value: `CUSTOMIZED_USER`. ⏎ Giá trị mặc định: `CUSTOMIZED_USER`. |
| identity_id **(Điều kiện)** | string | Bắt buộc khi you are not using Spark Ads (`tiktok_item_id`). ⏎ Identity ID for non-Spark Ads. |
| media_info_list   ****(Bắt buộc)**** | object[] | List of media information. ⏎ Kích thước tối đa: 30. |
| ↳ media_info  ****(Bắt buộc)**** | object | Material information. |
| ↳↳ video_info **(Điều kiện)** | object | Required for the following types of ads: • Non-Spark Ad Single Video ads.  • Spark Ad Single Video ads through Spark Ads Push. ⏎ Video information. |
| ↳↳↳ video_id **(Điều kiện)** | string | Bắt buộc khi `video_info` is passed. ⏎ Video ID. ⏎ You can get the video ID when you upload a video using the [/file/video/ad/upload/](71-video.md#doc-1737587322856449) endpoint. ⏎ **Note:**: To ensure a smooth integration journey, we recommend that you use [/file/video/ad/upload/](71-video.md#doc-1737587322856449) (`upload_type` = `UPLOAD_BY_VIDEO_ID`) to bind video ID with your ID tài khoản quảng cáo TikTok. |
| ↳↳↳ file_name | string | Video name. |
| ↳↳ image_info **(Điều kiện)** | object[] | • Required for the following types of ads: • Non-Spark Ad Single Video ads. You need to specify a video cover. • Spark Ad Single Video ads through Spark Ads Push. You need to specify a video cover. • Non-Spark Ad Standard Carousel ads, which are only supported for Smart+ Web Campaigns. You need to specify one to 35 carousel images. • Spark Ad Standard Carousel ads through Spark Ads Push, which are only supported for Smart+ Web Campaigns. You need to specify one to 35 carousel images.  • Not supported for Catalog Carousel ads. ⏎ Image information. |
| ↳↳↳ web_uri **(Điều kiện)** | string | Bắt buộc khi `image_info` is passed. ⏎ Image ID. ⏎ • To upload an image and obtain the image ID, use [/file/image/ad/upload/](47-images.md#doc-1739067433456642). • To search for images within your ad account, use [/file/image/ad/search/](47-images.md#doc-1740052016789506). ⏎ • The image to be used in Single Video ads should meet the following requirement: The aspect ratio of the image is the same as the video. • The images to be used in Standard Carousel Ads should meet the following requirements at the same time: • Specifications: • File Type: JPG, JPEG, or PNG. • Image Resolution: a maximum of 1242 x 2340 pixels or 2340 x 1242 pixels. • Aspect Ratio: a maximum of 9:20 or 20:9. • File Size: within 50 MB. • The value of the parameter `is_carousel_usable` returned from [/file/image/ad/search/](47-images.md#doc-1740052016789506) for the image is `true`. |
| ↳↳ music_info **(Điều kiện)** | object | Required for the following scenarios: • When you create Standard Carousel Ads, including: • Non-Spark Ad Standard Carousel ads • Spark Ad Standard Carousel ads through Spark Ads Push • Spark Ad Standard Carousel ads through Spark Ads Pull • When `objective_type` is `WEB_CONVERSIONS` and `catalog_creative_toggle` is true. The system will automatically generate catalog carousel ads. To learn about how to ensure that the catalog carousel format is available, see [Customize ad format combinations in Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Music information. |
| ↳↳↳ music_id **(Điều kiện)** | string | Bắt buộc khi `music_info` is passed. ⏎ The ID of the piece of music to use in the Carousel Ads. ⏎ • To obtain a valid music ID for Standard Carousel Ads, you can do any of the following: • Filter the pieces of music for Standard Carousel Ads under an ad account by specifying `music_scene` as `CAROUSEL_ADS` in [/file/music/get/](52-music.md#doc-1740053909509122). • Upload a piece of customized music for Standard Carousel Ads to an ad account through any of the following methods: • Specifying `music_scene` as `CAROUSEL_ADS` and passing `music_file` and `music_signature` in [/file/music/upload/](52-music.md#doc-1740052650395650). • Specifying `music_scene` as `CAROUSEL_ADS`, specifying `upload_type` as `UPLOAD_BY_FILE_ID`, and passing `file_id` in [/file/music/upload/](52-music.md#doc-1740052650395650). • To obtain a valid music ID for Catalog Carousel Ads, you can do any of the following: • Filter the pieces of music for Catalog Carousel Ads under an ad account by specifying `music_scene` as `CATALOG_CAROUSEL` in [/file/music/get/](52-music.md#doc-1740053909509122). • Upload a piece of customized music for Catalog Carousel Ads to an ad account through any of the following methods: • Specifying `music_scene` as `CATALOG_CAROUSEL` and passing `music_file` and `music_signature` in [/file/music/upload/](52-music.md#doc-1740052650395650). • Specifying `music_scene` as `CATALOG_CAROUSEL`, specifying `upload_type` as `UPLOAD_BY_FILE_ID`, and passing `file_id` in [/file/music/upload/](52-music.md#doc-1740052650395650). |
| ↳↳ aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` is `CUSTOMIZED_USER`. ⏎ Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.  • `NOT_DECLARED`: To not declare that the ad contains AI-generated content.Giá trị mặc định: `NOT_DECLARED`. ⏎ To learn about the supported advertising objectives and ad formats for the toggle and the detailed steps for using the toggle, see [AIGC self-disclosure toggle](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). ⏎ **Note**:  • You can only update this field when you update the video (`video_id`). |
| ↳↳ tiktok_item_id **(Điều kiện)** | string | Bắt buộc khi you create Spark Ads through Spark Ads Pull, including: •  Spark Ad Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. • Spark Ad Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). ⏎ Pass in the `item_id` you get from the response of the [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) and [/identity/video/get/](46-identity.md#doc-1740218475032577) endpoints. ⏎ When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `title_list`. ⏎ **Note**: By using Spark Ads, you confirm that you have the rights to use the music in the videos for commercial purposes. |
| ↳↳ identity_type **(Điều kiện)** | string | Bắt buộc khi you use Spark Ads. ⏎ Identity type for Spark Ads. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). ⏎ **Note**: If this field is set to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE` and `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`, you need to specify a dynamic CTA via `call_to_action_id`. |
| ↳↳ identity_id **(Điều kiện)** | string | Bắt buộc khi you use Spark Ads. ⏎ Identity ID for Spark Ads. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| dark_post_status | string | Chỉ hợp lệ khi you create Spark Ads through Spark Ads Push. ⏎ The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. ⏎ Giá trị mặc định: `ON`. ⏎ **Note**:  • You can set this to `OFF` only if both the identity's "Show through ads only" mode is disabled and the ad account does not have mandatory "Show through ads only" mode enabled. If the ad account enforces mandatory "Ads-only mode", you can only set this field to `ON` when creating Spark Ads using Spark Ads Push. This prevents the posts from appearing on your TikTok profile and gaining organic traffic, regardless of the identity's own `ads_only_mode` setting. It's a safeguard to ensure your Spark Ads Push content remains ads-only and avoids accidental profile posts. • To confirm the "Show through ads only" mode status of an identity, use [/identity/info/](46-identity.md#doc-1740218453385217) and check the returned `ads_only_mode`.  • To confirm the mandatory "Show through ads only" mode status of an ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `ads_only_mode`. |
| catalog_creative_toggle | boolean | Chỉ hợp lệ khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ If you set this field to `true`, `music_info` is required and the system will use catalog creatives to automatically generate ads in diverse formats such as catalog video, catalog carousel, and single video. For detailed configuration options and requirements, see [Customize ad format combinations in Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). |
| title_list **(Điều kiện)** | object[] | List of ad titles (also called ad texts). ⏎ Ad titles are shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. ⏎ When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `title_list`. |
| ↳ title **(Điều kiện)** | string | Bắt buộc khi `title_list` is passed. ⏎ Ad title (ad text). |
| call_to_action_id **(Điều kiện)** | string | Required in any of the following scenarios: • Scenario 1:  • `objective_type` is `LEAD_GENERATION`. • Scenario 2:  • `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • `identity_type` within the `media_info` object is `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`. ⏎ The ID of the CTA portfolio that you want to use in your ads. A CTA portfolio is a group of auto-optimized CTAs. ⏎ For details about auto-optimized CTAs, see [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). |
| call_to_action_list | object[] | Call-to-action list. ⏎ **Note**: This field is not supported in any of the following scenarios and you need to use `call_to_action_id` instead. • Scenario 1:  • `objective_type` is `LEAD_GENERATION`. • Scenario 2:  • `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • `identity_type` within the `media_info` object is `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`. |
| ↳ call_to_action **(Điều kiện)** | string | Bắt buộc khi `call_to_action_list` is passed. ⏎ Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| product_info | object | Additional product information. This information will be used to create ad variations to help achieve advertising goals such as standing out, building trust, or boosting performance. |
| ↳ promo_info_list | object[] | Valid only in [regular Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Details of promo codes and offers. ⏎ Promo codes and offers can help boost your ad performance. Make sure your codes and offers are active, accurate, and ready to use at checkout. ⏎ Kích thước tối đa: 10. |
| ↳↳ discount_type **(Điều kiện)** | string | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳ discount_value **(Điều kiện)** | float | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount value. ⏎ • When `discount_type` is `PERCENTAGE`, specify an integer between 1-100. • When `discount_type` is `CASH`, specify a float greater than 0. |
| ↳↳ discount_currency **(Điều kiện)** | string | Bắt buộc khi `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳ promo_code | string | The promo code. ⏎ • For promo codes that require shoppers to enter a code at checkout, specify the code through this field. • For offers that apply automatically, omit this field. ⏎ Giới hạn độ dài: 30 characters long and cannot contain emoji. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. ⏎ **Note**: Promo codes exclusive to TikTok often perform best. |
| ↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳ minimum_purchase_value **(Điều kiện)** | float | Bắt buộc khi `minimum_purchase_type` is specified. ⏎ Minimum purchase value. •  When `minimum_purchase_type` is `QUANTITY`, specify an integer that is 0 or greater. •  When `minimum_purchase_type` is `SUBTOTAL`, specify a float greater than 0. |
| ↳↳ minimum_purchase_currency **(Điều kiện)** | string | Bắt buộc khi `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. ⏎ • The `valid_end_time` should be later than the current time. • If you specify `valid_end_time`, provide `valid_start_time` at the same time. |
| card_list | object[] | Creative portfolio ID list. ⏎ Size range: 0-1. |
| ↳ card_id | string | Creative portfolio ID. ⏎ Pass the ID of one of the following creative portfolio types: • call-to-action text. • Website info card.  • Display Card. • Download Card. • Countdown Sticker.  • Gift Code Sticker. • Pop-up Showcase. ⏎ To create a creative portfolio, use [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426). ⏎ • To learn about how to get the ID of a Display Card, Website info card, or Download Card portfolio, see [Cards](../09-marketing-api/creatives.md#doc-1749019652141058). • To learn about how to get the ID of a Countdown Sticker or Giftcode Sticker portfolio, see [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177). • To learn about how to get the ID of a Pop-out Showcase portfolio, see [Premium Add-ons](../09-marketing-api/creatives.md#doc-1749019676181505). |
| automatic_add_on_enabled | boolean | Chỉ hợp lệ khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ Có thực hiện enable auto-selection of interactive add-ons. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ If you set this field to `true`, the system will automatically apply the most suitable interactive add-ons to your ads. To learn more about this setting, see the instructions for this field in [Create Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). |
| page_list | object[] | Page ID list. ⏎ Size range: 0-1. |
| ↳ page_id | string | Page ID. ⏎ • To obtain pages within your ad account, use [/page/get/](54-page.md#doc-1820826387779586). • To create instant pages, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881). |
| deeplink | string | The specific location where you want your audience to go if they have your app installed. ⏎ If you pass this field, you should also provide the `deeplink_type` field. |
| deeplink_type | string | The deeplink type. ⏎ Currently, we only support `DEFERRED_DEEPLINK`. ⏎ If you pass this field, you should also provide the `deeplink` field. |
| landing_page_urls | object[] | Landing page URL list. ⏎ Before you use this field, please be aware of the following two modes. ⏎ •  Single landing page mode: ⏎ In this mode, all videos/TikTok posts have the same landing page. When you create a campaign in single landing page mode, the size range of this field is 0-1. Additionally, you don't need to specify `video_id` or `tiktok_item_id` in this object array. • Multiple landing page mode: ⏎ This mode can only be used when `objective_type` = `WEB_CONVERSIONS`, `promotion_type` is `WEBSITE` and `spc_type` is `UNSET` or not passed. In this mode, each video/TikTok post corresponds to a landing page URL. When you create a campaign in multiple landing page mode, the size range of this field is 0-30, and the size must be equal to the number of videos. For instance, if creating a campaign with three videos (three objects in `media_info_list`), you must specify three objects in `landing_page_urls`. Additionally, you need to specify: **either** `video_id` when creating a non-Spark Ad, **or** `tiktok_item_id` when creating a Spark Ad. ⏎ **Note**: Multiple landing page mode is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ landing_page_url  **(Điều kiện)** | string | Bắt buộc khi `landing_page_urls` is passed. ⏎ Landing page URL. |
| ↳ video_id **(Điều kiện)** | string | •  Bắt buộc khi creating a non-Spark Ad campaign in multiple landing page mode. • You don't need this field when creating a campaign in single landing page mode. ⏎ Video ID. ⏎ Pass the `video_id` that you specified in the `video_info` object. |
| ↳ tiktok_item_id**(Điều kiện)** | string | •  Bắt buộc khi creating a Spark Ad in multiple landing page mode. •  You don't need this field when creating a campaign in single landing page mode. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). ⏎ Pass the `tiktok_item_id` that you specified in the `media_info` object. |
| utm_params | object[] | Valid when `objective_type` is `WEB_CONVERSIONS`. ⏎ A list of URL parameters. ⏎ Kích thước tối đa: 14. ⏎ If you set `landing_page_url` to a URL that already includes URL parameters, you can optionally pass `utm_params` at the same time to store the URL parameters used in the URL. In such cases, you need to ensure that `utm_params` exactly matches the used URL parameters. The URL parameters will not be automatically appended to the `landing_page_url` upon ad delivery. |
| ↳ key | string | The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, and video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, and color. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳ value | string | The value of the URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| disclaimer_info | object | Chỉ hợp lệ khi `sales_destination` is `WEB_AND_APP`. ⏎ Details of the disclaimer. |
| ↳ disclaimer_type | string | The type of disclaimer that you want to add to the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. ⏎ See [Include disclaimers in ads](../09-marketing-api/creatives.md#doc-1739953274550273) to learn about how to configure disclaimer settings. ⏎ **Note**:  • The disclaimer feature only supports TikTok placement. • Once added to your ads, the disclaimer cannot be deleted. |
| ↳ disclaimer_text **(Điều kiện)** | object | Bắt buộc khi `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer that you want to add to the ad. |
| ↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳ disclaimer_clickable_texts **(Điều kiện)** | object[] | Bắt buộc khi `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. ⏎ Kích thước tối đa: 3. ⏎ If you use multiple clickable disclaimers, both the overall length for all the texts you pass in and the length of individual text need to be no more than 40 characters. |
| ↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳ url | string | The URL for the clickable disclaimer. When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| tracking_app_id | string | Valid when `objective_type` is `WEB_CONVERSIONS`. ⏎ The ID of the App that you want to measure. ⏎ You can use this field to measure offsite app events. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| impression_tracking_url | string | Default Impression Tracking URL. URL generated by your data partner to track impression events in your ads. Generally you can find and copy the URL from their platform. ⏎ •  If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). •  If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Default Impression Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). |
| click_tracking_url | string | Click Tracking URL. URL generated by your data partner to track click events in your ads. Generally you can find and copy the URL from their platform. ⏎ •  If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). •  If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Click Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). ⏎ **Note:** `click_tracking_url` can not be updated if your app info already contains the click monitoring URL. |
| app_tracking_info_list | object[] | Chỉ hợp lệ khi `sales_destination` is `WEB_AND_APP`. ⏎ Details of Third-party tracking settings. ⏎ Kích thước tối đa: 4. |
| ↳ app_type **(Điều kiện)** | string | Bắt buộc khi `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳ app_id **(Điều kiện)** | string | Bắt buộc khi `app_tracking_info_list` is specified. ⏎ The App ID of the App. ⏎ • When `app_type` is `APP_ANDROID`, specify the App ID for an Android App. • When `app_type` is `APP_IOS`, specify the App ID for an iOS App. |
| ↳ impression_tracking_url **(Điều kiện)** | string | When `app_type` is specified, specify either `impression_tracking_url` or `click_tracking_url` or both. ⏎ Impression tracking URL. ⏎ • When `app_type` is `APP_ANDROID`, specify an impression tracking URL for Android. • When `app_type` is `APP_IOS`, specify an impression tracking URL for iOS. |
| ↳ click_tracking_url **(Điều kiện)** | string | When `app_type` is specified, specify either `impression_tracking_url` or `click_tracking_url` or both. ⏎ Click tracking URL. ⏎ • When `app_type` is `APP_ANDROID`, specify a click tracking URL for Android. • When `app_type` is `APP_IOS`, specify a click tracking URL for iOS. |

### List of values for `discount_currency` or `minimum_purchase_currency`
Bảng sau liệt kê các giá trị enum của `discount_currency` hoặc `minimum_purchase_currency`.

| Value for discount_currency ⏎ or minimum_purchase_currency | Currency |
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
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "operation_status": "ENABLE",
    "objective_type": "APP_PROMOTION",
    "app_promotion_type": "APP_INSTALL",
    "campaign_type": "REGULAR_CAMPAIGN",
    "campaign_name": "{{campaign_name}}",
    "promotion_type": "APP_ANDROID",
    "app_id": "{{app_id}}",
    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
    "location_ids": [
        "6252001"
    ],
    "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
    "budget": {{budget}},
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "optimization_goal": "INSTALL",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "identity_type": "CUSTOMIZED_USER",
    "identity_id": "{{identity_id}}",
    "media_info_list": [
        {
            "media_info": {
                "video_info": {
                    "video_id": "{{video_id}}",
                    "file_name": "{{file_name}}"
                },
                "image_info": [
                    {
                        "web_uri": "{{web_uri}}"
                    }
                ]
            }
        }
    ],
    "title_list": [
        {
            "title": "{{title}}"
        }
    ],
    "call_to_action_id": "{{call_to_action_id}}"
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
| ↳ operation_status | string | The status of the campaign. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled. • `DISABLE` : The campaign is disabled. |
| ↳ campaign_secondary_status | string | Campaign status (Secondary status). ⏎ For the supported campaign secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/campaign/get/](24-campaign.md#doc-1739315828649986). |
| ↳ is_smart_performance_campaign | boolean | Liệu campaign is an automated campaign type. ⏎ Các giá trị được hỗ trợ: • `true`: The campaign is either a Smart+ Campaign or a Smart Performance Web Campaign.  • `false`: The campaign is a standard campaign type. ⏎ **Note**: If `is_smart_performance_campaign` is `true` and `objective_type` is `WEB_CONVERSIONS`, you can confirm Liệu web campaign is a Smart+ Web Campaign or Smart Performance Web Campaign by checking the returned `spc_type`. |
| ↳ objective_type | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`,`WEB_CONVERSIONS`, and `LEAD_GENERATION`. |
| ↳ spc_type | string | The web campaign type. ⏎ Các giá trị enum hỗ trợ: • `WEB_ALL_IN_ONE`: Smart+ Web Campaign, where the supported optimization goals include Conversion, Value, Click and Landing page view. • `UNSET`: Smart Performance Web Campaign, where the supported optimization goals are limited to Conversion, Value, and Click. |
| ↳ web_all_in_one_catalog_status | string | The status of catalog in the Smart+ Web Campaign. ⏎ Các giá trị enum hỗ trợ: • `OPEN`: enabled. • `UNSET`: disabled. |
| ↳ app_promotion_type | string | App promotion type. ⏎ Currently, we only support `APP_INSTALL`. |
| ↳ virtual_objective_type | string | The new objective type. ⏎ Enum value: `SALES`. ⏎ Use this field to create a campaign with the Sales objective, the combined objective for Website Lượt chuyển đổi and Product Sales objectives. Learn more about [the Sales objective](https://business-api.tiktok.com/portal/docs?id=). |
| ↳ sales_destination | string | Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. |
| ↳ campaign_type | string | Campaign Type. ⏎ Currently, we support `REGULAR_CAMPAIGN` and `IOS14_CAMPAIGN`. |
| ↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị enum hỗ trợ: `true`, `false`. |
| ↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition).  • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (`conversion_bid_price`) or ROAS (`roas_bid`) is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN.  • `SKAN`: SKAN. |
| ↳ campaign_name | string | Campaign name. |
| ↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳ adgroup_secondary_status | string | Ad group status (Secondary status). ⏎ For the supported adgroup secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/adgroup/get/](24-campaign.md#doc-1739315828649986). |
| ↳ product_source | string | Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| ↳ catalog_id | string | The ID of the catalog to use in the Smart+ Catalog Ads. |
| ↳ catalog_authorized_bc_id | string | The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| ↳ product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products.  • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. |
| ↳ product_set_id | string | The ID of a product set. |
| ↳ product_ids | string[] | The product IDs of the catalog products. |
| ↳ promotion_type | string | Promotion type (Optimization location) and you can decide where you'd like to promote your products using this field. For value definitions, see [Enumerations - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_id | string | The App ID of the app to promote. ⏎ You can get `app_id` by using the [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) endpoint. |
| ↳ app_type | string | The type of the promoted app. ⏎ Currently, we support `APP_ANDROID` and `APP_IOS`. |
| ↳ promotion_website_type | string | TikTok Instant Page type. ⏎ Currently, we only support `TIKTOK_NATIVE_PAGE`(To use TikTok Instant Page). |
| ↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ pixel_id | string | ID TikTok Pixel. |
| ↳ optimization_event | string | Conversion event for the ad group. ⏎ See [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) for more. |
| ↳ app_config | object[] | Returned when `sales_destination` is `WEB_AND_APP`. ⏎ Details of the app or apps to promote. |
| ↳↳ app_id | string | The App ID of the app to promote. |
| ↳ deep_funnel_optimization_status | string | The status of deep funnel optimization. ⏎ With deep funnel optimization, you can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: enabled.   •  `OFF`: disabled. |
| ↳ deep_funnel_event_source | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel.   • `OFFLINE`: Offline Event Set.  • `CRM`: CRM Event Set. |
| ↳ deep_funnel_event_source_id | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. ⏎ • When `deep_funnel_event_source` is `PIXEL` , this field represents a ID TikTok Pixel. • When `deep_funnel_event_source` is `OFFLINE`, this field represents an Offline Event Set ID.   • When `deep_funnel_event_source` is `CRM`, this field represents a CRM Event Set ID. |
| ↳ deep_funnel_optimization_event | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ Example: `SHOPPING`. |
| ↳ bid_type | string | Bidding strategy. ⏎ For enum values and their descriptions, see [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ bid_price | float | The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳ conversion_bid_price | float | The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳ deep_bid_type | string | Bidding strategy for in-app events. ⏎ For enum values and their descriptions, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | Target ROAS for Value-Based Optimization. |
| ↳ incentive_offer_type | string | The type of incentive offer applicable to the Smart+ Campaign. ⏎ If your campaign meets the eligibility criteria, but underperforms against certain CPA or Minimum ROAS thresholds you will be reimbursed with part of the gap with ad credits within the same ad account. ⏎ To learn more about the incentive offer eligibility criteria and the calculation of incentive amount, see [Smart+ Incentive Offer (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: The campaign is ineligible for any incentive offer. • `COST_CAP_AND_MIN_ROAS`: Ads groups within the campaign that use the Cost Cap or Minimum ROAS/Target ROAS bidding strategy are eligible for the incentive offer. |
| ↳ vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7).   • `ZERO_DAY`: The current day (day 0). |
| ↳ click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off.  •  `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click.  • `FOURTEEN_DAYS`: 14-day click. •  `TWENTY_EIGHT_DAYS`: 28-day click. |
| ↳ engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Các giá trị enum hỗ trợ: • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. |
| ↳ view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. |
| ↳ attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset.  •  `EVERY`: Every. To count multiple events from someone as separate conversions.  •  `ONCE`: Once. To count multiple events from someone as 1 conversion. |
| ↳ billing_event | string | Bid method. See [Enumerations - Bid method](../15-appendix/phu-luc-p1.md#doc-1737174886619138) for optional values. |
| ↳ location_ids | string[] | IDs of the locations that you want to target. ⏎ Use [Get locations](70-tools-p1.md#doc-1737189539571713) to get available locations. |
| ↳ languages | string[] | Codes of the languages that you want to target. For the list of language codes supported, see [Enumerations - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳ spc_audience_age | string | The age group that the campaign targets. ⏎ Các giá trị enum hỗ trợ: `18+`, `25+`. |
| ↳ exclude_age_under_eighteen | boolean | Có thực hiện exclude the group aged under eighteen. |
| ↳ excluded_audience_ids | string[] | List of audience IDs to be excluded. |
| ↳ placement_type | string | The placement strategy that decides where your ads will be shown. ⏎ Currently, we support `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳ placements | string[] | The apps where you want to deliver your ads. ⏎ Currently, we support `PLACEMENT_TIKTOK` and `PLACEMENT_PANGLE`. |
| ↳ comment_disabled | boolean | Có thực hiện allow comments on your ads on TikTok. |
| ↳ share_disabled | boolean | Liệu sharing to third-party platforms is disabled for ads in this ad group. |
| ↳ video_download_disabled | boolean | Liệu users can download your video ads on TikTok. |
| ↳ blocked_pangle_app_ids | string[] | Pangle app block ID list. |
| ↳ brand_safety_type | string | Inventory filter tier for the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Expanded inventory. Your ads will not appear next to explicitly inappropriate content, but they may appear next to content that features mature themes. • `STANDARD_INVENTORY`: Standard inventory. Your ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Limited inventory. Your ads will not appear next to content that contains mature themes. • `NO_BRAND_SAFETY`: Full inventory without using any brand safety solution, which means your ads may appear next to some content featuring mature themes. ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳ category_exclusion_ids | string[] | The ID list of content categories that you want to avoid showing the Smart+ Campaign next to. ⏎ To obtain the details of these content categories based on category IDs, use [/tool/content_exclusion/info/](70-tools-p2.md#doc-1769738105333826). ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳ budget_mode | string | Budget mode. ⏎ See [Enumerations-Budget Mode](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ budget_auto_adjust_strategy | string | Returned only when `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable automatic budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable automatic budget increase. |
| ↳ budget | float | Fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. |
| ↳ current_budget | float | Returned only when `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`. ⏎ Current campaign budget for a campaign with automatic budget increase enabled. |
| ↳ scheduled_budget | float | Scheduled campaign budget for the next day. ⏎ A value not equal to 0 means the scheduled budget is set and the value represents the budget; a value of 0 means the scheduled budget is not set. |
| ↳ schedule_type | string | Schedule type. ⏎ Currently, we support `SCHEDULE_START_END` and `SCHEDULE_FROM_NOW`. |
| ↳ schedule_start_time | string | Ad delivery start time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ schedule_end_time | string | Ad delivery end time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: Not specified, all-0, or all-1 are considered as full-time delivery. |
| ↳ skip_learning_phase | boolean | Có thực hiện skip the learning phase. |
| ↳ identity_id | string | Identity ID when you are not using Spark Ads. |
| ↳ identity_type | string | Identity type when you are not using Spark Ads. ⏎ Enum value: `CUSTOMIZED_USER`. |
| ↳ app_download_url | string | App download link. |
| ↳ app_name | string | The display name of the app download ad. |
| ↳ media_info_list | object[] | List of media information. |
| ↳↳ media_info | object | Material information. |
| ↳↳↳ video_info | object | Video information. |
| ↳↳↳↳ video_id | string | Video ID. |
| ↳↳↳↳ file_name | string | Video name. |
| ↳↳↳ image_info | object[] | Image information. |
| ↳↳↳↳ web_uri | string | Image ID. |
| ↳↳↳ music_info | object | Music information. |
| ↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳ aigc_disclosure_type | string | Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.  • `NOT_DECLARED`: To not declare that the ad contains AI-generated content. |
| ↳↳↳ tiktok_item_id | string | The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳↳↳ identity_id | string | Identity ID when you use Spark Ads. |
| ↳↳↳ identity_type | string | Identity type when you use Spark Ads. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ dark_post_status | string | The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. |
| ↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will use catalog creatives to automatically generate ads in diverse formats such as catalog video, catalog carousel, and single video. |
| ↳ title_list | object[] | List of ad titles (also called ad texts). Ad titles are shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. |
| ↳↳ title | string | Ad title (ad text). |
| ↳ call_to_action_id | string | The ID of the CTA portfolio that you want to use in your ads. |
| ↳ call_to_action_list | object[] | Call-to-action list. |
| ↳↳ call_to_action | string | Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ product_info | object | Additional product information. This information will be used to create ad variations to help achieve advertising goals such as standing out, building trust, or boosting performance. |
| ↳↳ promo_info_list | object[] | Valid only in [regular Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Details of promo codes and offers. ⏎ Promo codes and offers can help boost your ad performance. Make sure your codes and offers are active, accurate, and ready to use at checkout. |
| ↳↳↳ discount_type | string | Returned when `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳ discount_value | string | Returned when `promo_info_list` is specified. ⏎ Discount value. ⏎ • When `discount_type` is `PERCENTAGE`, this field will be an integer between 1-100. •  When `discount_type` is `CASH`, this field will be a float greater than 0. |
| ↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳ minimum_purchase_value | float | Returned when `minimum_purchase_type` is specified. ⏎ Minimum purchase value. ⏎ •  When `minimum_purchase_type` is `QUANTITY`, this field will be an integer that is 0 or greater. • When `minimum_purchase_type` is `SUBTOTAL`, this field will be a float greater than 0. |
| ↳↳↳ minimum_purchase_currency | string | Returned when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳ card_list | object[] | Creative portfolio ID list. |
| ↳↳ card_id | string | Creative portfolio ID. |
| ↳ automatic_add_on_enabled | boolean | Có thực hiện enable auto-selection of interactive add-ons. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will automatically apply the most suitable interactive add-ons to your ads. |
| ↳ page_list | object[] | Page ID list. |
| ↳↳ page_id | string | Page ID. |
| ↳ deeplink | string | The specific location where you want your audience to go if they have your app installed. |
| ↳ deeplink_type | string | The deeplink type. |
| ↳ landing_page_urls | object[] | Landing page URL list. |
| ↳↳ landing_page_url | string | Landing page URL. |
| ↳↳ video_id | string | Returned when the campaign is in multiple landing page mode. ⏎ Video ID. |
| ↳↳ tiktok_item_id | string | Returned when the campaign is in multiple landing page mode. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳ utm_params | object[] | A list of URL parameters. ⏎ URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳ key | string | The URL parameter. ⏎ The parameter can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, and video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, and color. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. |
| ↳↳ value | string | The value of the URL parameter. ⏎ The value can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳ disclaimer_info | object | Details of the disclaimer. |
| ↳↳ disclaimer_type | string | The type of disclaimer that you want to add to the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. |
| ↳↳ disclaimer_text | object | Returned when `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer that you want to add to the ad. |
| ↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳↳ disclaimer_clickable_texts | object[] | Returned when `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. |
| ↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳↳ url | string | The URL for the clickable disclaimer. When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ↳ tracking_app_id | string | The ID of the app that is measured. |
| ↳ impression_tracking_url | string | Default Impression Tracking URL. |
| ↳ click_tracking_url | string | Click Tracking URL. |
| ↳ app_tracking_info_list | object[] | Details of Third-party tracking settings. |
| ↳↳ app_type | string | Returned when `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳ app_id | string | Returned when `app_tracking_info_list` is specified. ⏎ The App ID of the App. ⏎ • When `app_type` is `APP_ANDROID`, this field represents the App ID for an Android App. • When `app_type` is `APP_IOS`, this field represents the App ID for an iOS App. |
| ↳↳ impression_tracking_url | string | Impression tracking URL. ⏎ When `app_type` is `APP_ANDROID`, this field represents an impression tracking URL for Android. •  • When `app_type` is `APP_IOS`, this field represents an impression tracking URL for iOS. |
| ↳↳ click_tracking_url | string | Click tracking URL. ⏎ • When `app_type` is `APP_ANDROID`, this field represents a click tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents a click tracking URL for iOS. |
| ↳ create_time | string | The time when the campaign was created, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ modify_time | string | The time when the campaign was modified, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "pixel_id": null,
        "carousel_image_index": null,
        "deeplink": "",
        "adgroup_secondary_status": "ADGROUP_STATUS_AUDIT",
        "gender": "GENDER_UNLIMITED",
        "special_industries": null,
        "location_ids": [
            "6252001"
        ],
        "schedule_end_time": "{{schedule_end_time}}",
        "excluded_audience_ids": null,
        "shopping_ads_fallback_type": null,
        "promotion_type": "APP_ANDROID",
        "product_ids": null,
        "automatic_add_on_enabled": null,
        "budget": {{budget}},
        "skip_learning_phase": true,
        "impression_tracking_url": null,
        "share_disabled": false,
        "deep_bid_type": "DEFAULT",
        "engaged_view_attribution_window": "SEVEN_DAYS",
        "conversion_bid_price": null,
        "is_advanced_dedicated_campaign": false,
        "promotion_website_type": null,
        "schedule_type": "SCHEDULE_START_END",
        "attribution_event_count": "ONCE",
        "campaign_app_profile_page_state": "UNSET",
        "product_set_id": null,
        "roas_bid": null,
        "call_to_action_id": "{{call_to_action_id}}",
        "app_promotion_type": "APP_INSTALL",
        "languages": [],
        "is_smart_performance_campaign": true,
        "call_to_action_list": [],
        "click_tracking_url": null,
        "modify_time": "{{modify_time}}",
        "bid_price": null,
        "media_info_list": [
            {
                "media_info": {
                    "video_info": {
                        "video_id": "{{video_id}}",
                        "file_name": "{{file_name}}"
                    },
                    "identity_type": null,
                    "aigc_disclosure_type": null,
                    "music_info": null,
                    "tiktok_item_id": null,
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "identity_id": null
                }
            }
        ],
        "catalog_creative_toggle": null,
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "identity_type": "CUSTOMIZED_USER",
        "card_list": null,
        "campaign_secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "page_list": null,
        "scheduled_budget": 0,
        "bid_type": "BID_TYPE_NO_BID",
        "placements": [
            "PLACEMENT_TIKTOK",
            "PLACEMENT_PANGLE"
        ],
        "app_download_url": "{{app_download_url}}",
        "view_attribution_window": "ONE_DAY",
        "create_time": "{{create_time}",
        "dayparting": 
"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "product_specific_type": null,
        "catalog_authorized_bc_id": null,
        "schedule_start_time": "{{schedule_start_time}}",
        "comment_disabled": false,
        "campaign_type": "REGULAR_CAMPAIGN",
        "deeplink_type": null,
        "campaign_id": "{{campaign_id}}",
        "product_source": null,
        "blocked_pangle_app_ids": null,
        "carousel_image_labels": null,
        "billing_event": "OCPM",
        "campaign_name": "{{campaign_name}}",
        "app_name": "{{app_name}}",
        "optimization_goal": "INSTALL",
        "video_download_disabled": false,
        "operation_status": "ENABLE",
        "click_attribution_window": "SEVEN_DAYS",
        "title_list": [
            {
                "title": "{{title}}"
            }
        ],
        "landing_page_urls": null,
        "spc_audience_age": "18+",
        "app_type": "APP_ANDROID",
        "spc_type": "UNSET",
        "web_all_in_one_catalog_status": null,
        "optimization_event": "ACTIVE",
        "objective_type": "APP_PROMOTION",
        "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
        "exclude_age_under_eighteen": true,
        "identity_id": "{{identity_id}}",
        "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
        "catalog_id": null
    }
}
```

---

<a id="doc-1767334250066945"></a>
<!-- doc_id: 1767334250066945 -->
<!-- doc_id: 1767334250066945 -->
# (Sắp ngừng hỗ trợ) Cập nhật chiến dịch Smart+ phiên bản cũ (Update a Legacy Smart+ Campaign)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Update a Legacy Smart+ Campaign
Sử dụng endpoint này để cập nhật a Smart+ Campaign. Not all information of a Smart+ Campaign can be modified (For example, **placement**). The endpoint supports incremental updates. 
> **Note:** 
> Bạn không thể cập nhật Chiến dịch Smart+ qua [/campaign/update/](24-campaign.md#doc-1739320422086657), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745), and [/ad/update/](02-ads-p2.md#doc-1739953405142018). 

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.
## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/spc/update/

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
| campaign_id  ****(Bắt buộc)**** | string | ID chiến dịch quảng cáo. |
| campaign_name | string | Campaign name. |
| special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities.**Note** ⏎ • Currently, we only support clearing this field. • This field is only supported for advertisers who are registered in America or Canada. |
| product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products.  •  `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. ⏎ • If this field is set to `ALL`, you don't need to input `product_set_id` and `product_ids`.  • If this field is set to `PRODUCT_SET`, you need to pass in `product_set_id`.  • If this field is set to `CUSTOMIZED_PRODUCTS`, `product_ids` is required. |
| product_set_id **(Điều kiện)** | string | Bắt buộc khi `product_specific_type` is `PRODUCT_SET`. ⏎ The ID of a product set. ⏎ • To retrieve the product sets within your ad account, use [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169).  • To create a product set, use [/catalog/set/create/](29-catalog-product-sets.md#doc-1740572891104257). |
| product_ids **(Điều kiện)** | string[] | Bắt buộc khi `product_specific_type` is `product_ids`. ⏎ The product IDs of the catalog products. ⏎ Kích thước tối đa: 20. ⏎ To retrieve the product ID (`product_id`) of each catalog product, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| bid_price | float | Chỉ hợp lệ khi the following conditions are met: • `spc_type` is `WEB_ALL_IN_ONE` • `optimization_goal` is `CLICK`  • `bid_type` is `BID_TYPE_CUSTOM` ⏎ The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. |
| conversion_bid_price | float | Chỉ hợp lệ khi the following conditions are met:  • `spc_type` is `WEB_ALL_IN_ONE` • `optimization_goal` is `CONVERT` or `TRAFFIC_LANDING_PAGE_VIEW` •  `bid_type` is `BID_TYPE_CUSTOM` ⏎ The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. ⏎ `conversion_bid_price` needs to be lower than budget. See [Bidding-Bidding limits](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) to learn more about the bid verification mechanism. |
| roas_bid | float | Target ROAS for Value-Based Optimization. ⏎ Value range: 0.01-1,000. |
| location_ids | string[] | IDs of the locations that you want to target. ⏎ To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) or [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. ⏎ To get the list of location IDs, see **Location IDs**. ⏎ **Note**: If you add the US as your target location, then you can not remove the US after campaign creation. |
| languages | string[] | Codes of the languages that you want to target. ⏎ For the list of language codes supported, see [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. ⏎ **Note**: The field is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| spc_audience_age | string | The age group that the campaign targets. ⏎ Enum value: • `18+`: 18+. • `25+`: 25+. • The value `25+` is only available when `objective_type` is `LEAD_GENERATION`. |
| exclude_age_under_eighteen | boolean | Exclude the group aged under eighteen. ⏎ **Note**: Starting from September 21st, 2023, you can no longer target audience aged under eighteen. ⏎ The field can only be updated from `false` to `true`. |
| excluded_audience_ids | string[] | List of audience IDs to be excluded. ⏎ You can get audience IDs by using the [/dmp/custom_audience/list/ ](09-audience.md#doc-1739940506015746)endpoint. |
| comment_disabled | boolean | Có thực hiện allow comments on your campaigns on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| share_disabled | boolean | Có thực hiện disable sharing of the campaign to third-party platforms. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| blocked_pangle_app_ids | string[] | Pangle app block ID list. ⏎ You can get an ID via the `app_package_id` field returned by [Get Pangle block list](55-pangle.md#doc-1740039957181441). |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The daily budget strategy. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable automatic budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable automatic budget increase. ⏎ **Note**: Enabling automatic budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget | float | Fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. ⏎ To learn about the minimum budget and how to set budget modes, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). ⏎ To directly see the daily budget value range for a currency, see [Currency-Daily budget value range](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| schedule_type | string | Schedule type. ⏎ Currently, we support `SCHEDULE_START_END` and `SCHEDULE_FROM_NOW`. |
| schedule_start_time | string | Schedule start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The start time can be up to 12 hours earlier than the current time. |
| schedule_end_time | string | Schedule end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: If not specified, all-0, or all-1 are considered as full-time delivery. |
| identity_id | string | Identity ID when you are not using Spark Ads. |
| media_info_list | object[] | List of media information. ⏎ Kích thước tối đa: 30. |
| ↳ media_info | object | Material information. |
| ↳↳ video_info | object | Valid for the following types of ads: • Non-Spark Ad Single Video ads.  • Spark Ad Single Video ads through Spark Ads Push. ⏎ Video information. |
| ↳↳↳ video_id**(Điều kiện)** | string | Bắt buộc khi `video_info` is passed. ⏎ Video ID. ⏎ You can get the video ID when you upload a video using the [/file/video/ad/upload/](71-video.md#doc-1737587322856449) endpoint. ⏎ **Note**: To ensure a smooth integration journey, we recommend that you use [/file/video/ad/upload/](71-video.md#doc-1737587322856449) (`upload_type` = `UPLOAD_BY_VIDEO_ID`) to bind video ID with your ID tài khoản quảng cáo TikTok. |
| ↳↳↳ file_name | string | Video name. |
| ↳↳ image_info | object[] | • Valid for the following types of ads: • Non-Spark Ad Single Video ads. You need to specify a video cover. • Spark Ad Single Video ads through Spark Ads Push. You need to specify a video cover. • Non-Spark Ad Standard Carousel ads, which are only supported for Smart+ Web Campaigns. You need to specify one to 35 carousel images. • Spark Ad Standard Carousel ads through Spark Ads Push, which are only supported for Smart+ Web Campaigns. You need to specify one to 35 carousel images.  • Not supported for Catalog Carousel ads. ⏎ Image information. |
| ↳↳↳ web_uri  **(Điều kiện)** | string | Bắt buộc khi `image_info` is passed. ⏎ Image ID. ⏎ • To upload an image and obtain the image ID, use [/file/image/ad/upload/](47-images.md#doc-1739067433456642). • To search for images within your ad account, use [/file/image/ad/search/](47-images.md#doc-1740052016789506). ⏎ • The image to be used in Single Video ads should meet the following requirement: The aspect ratio of the image is the same as the video. • The images to be used in Standard Carousel Ads should meet the following requirements at the same time: • Specifications: • File Type: JPG, JPEG, or PNG. • Image Resolution: a maximum of 1242 x 2340 pixels or 2340 x 1242 pixels. • Aspect Ratio: a maximum of 9:20 or 20:9. • File Size: within 50 MB. • The value of the parameter `is_carousel_usable` returned from [/file/image/ad/search/](47-images.md#doc-1740052016789506) for the image is `true`. |
| ↳↳ music_info | object | Valid for the following scenarios: • When you create Standard Carousel Ads, including: • Non-Spark Ad Standard Carousel ads • Spark Ad Standard Carousel ads through Spark Ads Push • Spark Ad Standard Carousel ads through Spark Ads Pull • When `objective_type` is `WEB_CONVERSIONS` and `catalog_creative_toggle` is `true`. The system will automatically generate catalog carousel ads. ⏎ Music information. |
| ↳↳↳ music_id **(Điều kiện)** | string | Bắt buộc khi `music_info` is passed. ⏎ The ID of the piece of music to use in the Carousel Ads. ⏎ • To obtain a valid music ID for Standard Carousel Ads, you can do any of the following: • Filter the pieces of music for Standard Carousel Ads under an ad account by specifying `music_scene` as `CAROUSEL_ADS` in [/file/music/get/](52-music.md#doc-1740053909509122). • Upload a piece of customized music for Standard Carousel Ads to an ad account through any of the following methods: • Specifying `music_scene` as `CAROUSEL_ADS` and passing `music_file` and `music_signature` in [/file/music/upload/](52-music.md#doc-1740052650395650). • Specifying `music_scene` as `CAROUSEL_ADS`, specifying `upload_type` as `UPLOAD_BY_FILE_ID`, and passing `file_id` in [/file/music/upload/](52-music.md#doc-1740052650395650). • To obtain a valid music ID for Catalog Carousel Ads, you can do any of the following: • Filter the pieces of music for Catalog Carousel Ads under an ad account by specifying `music_scene` as `CATALOG_CAROUSEL` in [/file/music/get/](52-music.md#doc-1740053909509122). • Upload a piece of customized music for Catalog Carousel Ads to an ad account through any of the following methods: • Specifying `music_scene` as `CATALOG_CAROUSEL` and passing `music_file` and `music_signature` in [/file/music/upload/](52-music.md#doc-1740052650395650). • Specifying `music_scene` as `CATALOG_CAROUSEL`, specifying `upload_type` as `UPLOAD_BY_FILE_ID`, and passing `file_id` in [/file/music/upload/](52-music.md#doc-1740052650395650). |
| ↳↳ aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` is `CUSTOMIZED_USER`. ⏎ Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-genlark://client/chat/6956489210853343233erated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.  • `NOT_DECLARED`: To not declare that the ad contains AI-generated content.Giá trị mặc định: `NOT_DECLARED`. ⏎ To learn about the supported advertising objectives and ad formats for the toggle and the detailed steps for using the toggle, see [AIGC self-disclosure toggle](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). ⏎ **Note**:  • You can only update this field when you update the video (`video_id`). |
| ↳↳ tiktok_item_id | string | Valid when you create Spark Ads through Spark Ads Pull, including: •  Spark Ad Single Video ads through Spark Ads Pull. You need to specify a TikTok video post. • Spark Ad Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). ⏎ Pass in the `item_id` you get from the response of the [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) and [/identity/video/get/](46-identity.md#doc-1740218475032577) endpoints. ⏎ When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `title_list`. ⏎ **Note**: By using Spark Ads, you confirm that you have the rights to use the music in the videos for commercial purposes. |
| ↳↳ identity_type | string | Identity type for Spark Ads. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). ⏎ **Note**: If this field is set to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE` and `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`, you need to specify a dynamic CTA via `call_to_action_id`. |
| ↳↳ identity_id | string | Identity ID for Spark Ads. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| dark_post_status | string | Chỉ hợp lệ khi you create Spark Ads through Spark Ads Push. ⏎ The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. ⏎ **Note**: You can only set this field to `OFF` if the "Ads-only mode" is disabled for the identity. To confirm the "Ads-only mode" status of an identity, use [/identity/info/](46-identity.md#doc-1740218453385217) and check the returned `ads_only_mode`. |
| catalog_creative_toggle | boolean | Chỉ hợp lệ khi `web_all_in_one_catalog_status` is `OPEN`. ⏎ Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ If you set this field to `true`, `music_info` is required and the system will use catalog creatives to automatically generate ads in diverse formats such as catalog video, catalog carousel, and single video. For detailed configuration options and requirements, see [Customize ad format combinations in Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). |
| title_list | object[] | List of ad titles (also called ad texts). ⏎ Ad titles are shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. |
| ↳ title  **(Điều kiện)** | string | Bắt buộc khi `title_list` is passed. ⏎ Ad title (ad text). |
| call_to_action_id **(Điều kiện)** | string | Required in any of the following scenarios: • Scenario 1:  • `objective_type` is `LEAD_GENERATION`. • Scenario 2:  • `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • `identity_type` within the `media_info` object is `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`. ⏎ The ID of the CTA portfolio that you want to use in your ads. A CTA portfolio is a group of auto-optimized CTAs. ⏎ For details about auto-optimized CTAs, see [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). |
| call_to_action_list | object[] | Call-to-action list. ⏎ **Note**: This field is not supported in any of the following scenarios and you need to use `call_to_action_id` instead. • Scenario 1:  • `objective_type` is `LEAD_GENERATION`. • Scenario 2:  • `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`. • `identity_type` within the `media_info` object is `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`. |
| ↳ call_to_action | string | Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| product_info | object | Additional product information. This information will be used to create ad variations to help achieve advertising goals such as standing out, building trust, or boosting performance. |
| ↳ promo_info_list | object[] | Valid only in [regular Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Details of promo codes and offers. ⏎ Promo codes and offers can help boost your ad performance. Make sure your codes and offers are active, accurate, and ready to use at checkout. ⏎ Kích thước tối đa: 10. ⏎ **Note**: • This field supports full replacement. If you want to update this field, specify all fields for each object within `promo_info_list`.  •  Any changes to parameters within `promo_info_list` or updates to the `promo_code` will result in a new ad review for the Smart+ Campaign. |
| ↳↳ discount_type **(Điều kiện)** | string | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳ discount_value **(Điều kiện)** | float | Bắt buộc khi `promo_info_list` is specified. ⏎ Discount value. ⏎ • When `discount_type` is `PERCENTAGE`, specify an integer between 1-100. • When `discount_type` is `CASH`, specify a float greater than 0. |
| ↳↳ discount_currency **(Điều kiện)** | string | Bắt buộc khi `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳ promo_code | string | The promo code. ⏎ • For promo codes that require shoppers to enter a code at checkout, specify the code through this field. • For offers that apply automatically, omit this field. ⏎ Giới hạn độ dài: 30 characters long and cannot contain emoji. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. ⏎ **Note**: Promo codes exclusive to TikTok often perform best. |
| ↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳ minimum_purchase_value **(Điều kiện)** | float | Bắt buộc khi `minimum_purchase_type` is specified. ⏎ Minimum purchase value. •  When `minimum_purchase_type` is `QUANTITY`, specify an integer that is 0 or greater. •  When `minimum_purchase_type` is `SUBTOTAL`, specify a float greater than 0. |
| ↳↳ minimum_purchase_currency **(Điều kiện)** | string | Bắt buộc khi `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. ⏎ • The `valid_end_time` should be later than the current time. • If you specify `valid_end_time`, provide `valid_start_time` at the same time. |
| card_list | object[] | Creative portfolio ID list. ⏎ Size range: 0-1. |
| ↳ card_id | string | Creative portfolio ID. ⏎ Pass the ID of one of the following creative portfolio types: • call-to-action text. • Website info card.  • Display Card. • Download Card. • Countdown Sticker.  • Gift Code Sticker. • Pop-up Showcase. ⏎ To create a creative portfolio, use [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426). ⏎ • To learn about how to get the ID of a Display Card, Website info card, or Download Card portfolio, see [Cards](../09-marketing-api/creatives.md#doc-1749019652141058). • To learn about how to get the ID of a Countdown Sticker or Giftcode Sticker portfolio, see [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177). • To learn about how to get the ID of a Pop-out Showcase portfolio, see [Premium Add-ons](../09-marketing-api/creatives.md#doc-1749019676181505). |
| page_list | object[] | Page ID list. ⏎ Size range: 0-1. |
| ↳ page_id | string | Page ID. ⏎ • To obtain pages within your ad account, use [/page/get/](54-page.md#doc-1820826387779586). • To create instant pages, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881). |
| deeplink_type | string | The deeplink type. ⏎ Currently, we only support `DEFERRED_DEEPLINK`. ⏎ **Note**: If you pass this field, you should also provide the `deeplink` field. |
| deeplink | string | The specific location where you want your audience to go if they have your app installed. ⏎ **Note**: If you pass this field, you should also provide the `deeplink_type` field. |
| landing_page_urls | object[] | Landing page URL list. ⏎ Before you use this field, please be aware of the following two modes. You can switch the ad between the two modes. ⏎ • Single landing page mode: ⏎ In this mode, all videos/TikTok posts have the same landing page. When you update a campaign to single landing page mode, the size range of this field is 0-1. Additionally, you don't need to specify `video_id` or `tiktok_item_id` in this object array. •  Multiple landing page mode: ⏎ This mode can only be used when `objective_type` = `WEB_CONVERSIONS`, `promotion_type` is `WEBSITE` and `spc_type` is `UNSET` or not passed. In this mode, each video/TikTok post corresponds to a landing page URL. When you create a campaign in multiple landing page mode, the size range of this field is 0-30, and the size must be equal to the number of videos. For instance, if updating a campaign with three videos (three objects in `media_info_list`), you must specify three objects in `landing_page_urls`. Additionally, you need to specify: **either** `video_id` when updating a non-Spark ad, **or** `tiktok_item_id` when updating a Spark Ad. ⏎ **Note**:  • If you update `media_info_list` in the request, you need to update `landing_page_urls` at the same time. • Multiple landing page mode is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ landing_page_url  **(Điều kiện)** | string | Bắt buộc khi `landing_page_urls` is passed. ⏎ Landing page URL. |
| ↳ video_id **(Điều kiện)** | string | •  Bắt buộc khi updating a non-Spark Ad campaign to multiple landing page mode. • You don't need this field when updating a campaign to single landing page mode. ⏎ Video ID. ⏎ Pass the `video_id` that you specified in the `video_info` object. |
| ↳ tiktok_item_id**(Điều kiện)** | string | •  Bắt buộc khi updating a Spark Ad campaign to multiple landing page mode. •  You don't need this field when updating a campaign to single landing page mode. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). ⏎ Pass the `tiktok_item_id` that you specified in the `media_info` object. |
| utm_params | object[] | Valid when `objective_type` is `WEB_CONVERSIONS`. ⏎ A list of URL parameters. ⏎ Kích thước tối đa: 14. ⏎ If you set `landing_page_url` to a URL that already includes URL parameters, you can optionally pass `utm_params` at the same time to store the URL parameters used in the URL. In such cases, you need to ensure that `utm_params` exactly matches the used URL parameters. The URL parameters will not be automatically appended to the `landing_page_url` upon ad delivery. |
| ↳ key | string | The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, and video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, and color. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. ⏎ Length limit when you specify a custom parameter: 100 characters. |
| ↳ value | string | The value of the URL parameter. ⏎ You can specify a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. ⏎ Length limit when you specify a custom value: 600 characters. |
| disclaimer_info | object | Chỉ hợp lệ khi `sales_destination` is `WEB_AND_APP`. ⏎ Details of the disclaimer. |
| ↳ disclaimer_type | string | The type of disclaimer that you want to add to the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. ⏎ See [Include disclaimers in ads](../09-marketing-api/creatives.md#doc-1739953274550273) to learn about how to configure disclaimer settings. ⏎ **Note**:  • The disclaimer feature only supports TikTok placement. • Once added to your ads, the disclaimer cannot be deleted. |
| ↳ disclaimer_text **(Điều kiện)** | object | Bắt buộc khi `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer that you want to add to the ad. |
| ↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳ disclaimer_clickable_texts **(Điều kiện)** | object[] | Bắt buộc khi `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. ⏎ Kích thước tối đa: 3. ⏎ If you use multiple clickable disclaimers, both the overall length for all the texts you pass in and the length of individual text need to be no more than 40 characters. |
| ↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳ url | string | The URL for the clickable disclaimer. When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| tracking_app_id | string | Valid when `objective_type` is `WEB_CONVERSIONS`. ⏎ The ID of the App that you want to measure. ⏎ You can use this field to measure offsite app events. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| impression_tracking_url | string | Default Impression Tracking URL. URL generated by your data partner to track impression events in your ads. Generally you can find and copy the URL from their platform.  •  If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). •  If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Default Impression Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). |
| click_tracking_url | string | Click Tracking URL. URL generated by your data partner to track click events in your ads. Generally you can find and copy the URL from their platform.  •  If the partner ID for the App (`app_id` specified at the ad group level ) that you want to track is `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field. If you do, this field will be ignored. You can obtain the partner ID of an App through `partner_id` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). •  If self-attribution has been enabled for the App (`app_id` specified at the ad group level ) that you want to track and the partner ID for the App is not `44` (TikTok Business SDK) or `49` (TikTok App API), you don't need to pass in this field because this field will default to the Click Tracking URL you have configured for the App, and updates to the URL are not supported. You can check Liệu self-attribution has been enabled for the App through `self_attribution_enabled` returned from [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) or [/app/info/](43-events-1-0-p1.md#doc-1740859272887297). |

### List of values for `discount_currency` or `minimum_purchase_currency`
Bảng sau liệt kê các giá trị enum của `discount_currency` hoặc `minimum_purchase_currency`.

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
curl -H "Access-Token:{{Access-Token}}" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "campaign_name": "{{campaign_name}}"
}' \
https://business-api.tiktok.com/open_api/v1.3/campaign/spc/update/
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
| ↳ operation_status | string | The status of the campaign. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled. • `DISABLE` : The campaign is disabled. |
| ↳ campaign_secondary_status | string | Campaign status (Secondary status). ⏎ For the supported campaign secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/campaign/get/](24-campaign.md#doc-1739315828649986). |
| ↳ is_smart_performance_campaign | boolean | Liệu campaign is an automated campaign type. ⏎ Các giá trị được hỗ trợ: • `true`: The campaign is either a Smart+ Campaign or a Smart Performance Web Campaign.  • `false`: The campaign is a standard campaign type. ⏎ **Note**: If `is_smart_performance_campaign` is `true` and `objective_type` is `WEB_CONVERSIONS`, you can confirm Liệu web campaign is a Smart+ Web Campaign or Smart Performance Web Campaign by checking the returned `spc_type`. |
| ↳ objective_type | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. |
| ↳ spc_type | string | The web campaign type. ⏎ Các giá trị enum hỗ trợ: • `WEB_ALL_IN_ONE`: Smart+ Web Campaign, where the supported optimization goals include Conversion, Value, Click and Landing page view. • `UNSET`: Smart Performance Web Campaign, where the supported optimization goals are limited to Conversion, Value, and Click. |
| ↳ web_all_in_one_catalog_status | string | The status of catalog in the Smart+ Web Campaign. ⏎ Các giá trị enum hỗ trợ: • `OPEN`: enabled. • `UNSET`: disabled. |
| ↳ app_promotion_type | string | App promotion type. ⏎ Currently, we only support `APP_INSTALL`. |
| ↳ virtual_objective_type | string | The new objective type. ⏎ Enum value: `SALES`. ⏎ Use this field to create a campaign with the Sales objective, the combined objective for Website Lượt chuyển đổi and Product Sales objectives. Learn more about [the Sales objective](https://business-api.tiktok.com/portal/docs?id=). |
| ↳ sales_destination | string | Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. |
| ↳ campaign_type | string | Campaign Type. ⏎ Currently, we support `REGULAR_CAMPAIGN` and `IOS14_CAMPAIGN`. |
| ↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị enum hỗ trợ: `true`, `false`. |
| ↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition).  • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (`conversion_bid_price`) or ROAS (`roas_bid`) is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN.  • `SKAN`: SKAN. |
| ↳ campaign_name | string | Campaign name. |
| ↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳ adgroup_secondary_status | string | Ad group status (Secondary status). ⏎ For the supported adgroup secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/adgroup/get/](24-campaign.md#doc-1739315828649986). |
| ↳ product_source | string | Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| ↳ catalog_id | string | The ID of the catalog to use in the Smart+ Catalog Ads. |
| ↳ catalog_authorized_bc_id | string | The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| ↳ product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products.  • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. |
| ↳ product_set_id | string | The ID of a product set. |
| ↳ product_ids | string[] | The product IDs of the catalog products. |
| ↳ promotion_type | string | Promotion type (Optimization location) and you can decide where you'd like to promote your products using this field. For value definitions, see [Enumerations - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_id | string | The App ID of the app to promote. ⏎ You can get `app_id` by using the [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) endpoint. |
| ↳ app_type | string | The type of the promoted app. ⏎ Currently, we support `APP_ANDROID` and `APP_IOS`. |
| ↳ promotion_website_type | string | TikTok Instant Page type. ⏎ Currently, we only support `TIKTOK_NATIVE_PAGE`(To use TikTok Instant Page). |
| ↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ pixel_id | string | ID TikTok Pixel. |
| ↳ optimization_event | string | Conversion event for the ad group. ⏎ See [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) for more. |
| ↳ app_config | object[] | Returned when `sales_destination` is `WEB_AND_APP`. ⏎ Details of the app or apps to promote. |
| ↳↳ app_id | string | The App ID of the app to promote. |
| ↳ deep_funnel_optimization_status | string | The status of deep funnel optimization. ⏎ With deep funnel optimization, you can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: enabled.   •  `OFF`: disabled. |
| ↳ deep_funnel_event_source | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel.   • `OFFLINE`: Offline Event Set.  • `CRM`: CRM Event Set. |
| ↳ deep_funnel_event_source_id | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. ⏎ • When `deep_funnel_event_source` is `PIXEL` , this field represents a ID TikTok Pixel. • When `deep_funnel_event_source` is `OFFLINE`, this field represents an Offline Event Set ID.   • When `deep_funnel_event_source` is `CRM`, this field represents a CRM Event Set ID. |
| ↳ deep_funnel_optimization_event | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ Example: `SHOPPING`. |
| ↳ bid_type | string | Bidding strategy. ⏎ For enum values and their descriptions, see [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ bid_price | float | The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳ conversion_bid_price | float | The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳ deep_bid_type | string | Bidding strategy for in-app events. ⏎ For enum values and their descriptions, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | Target ROAS for Value-Based Optimization. |
| ↳ incentive_offer_type | string | The type of incentive offer applicable to the Smart+ Campaign. ⏎ If your campaign meets the eligibility criteria, but underperforms against certain CPA or Minimum ROAS thresholds you will be reimbursed with part of the gap with ad credits within the same ad account. ⏎ To learn more about the incentive offer eligibility criteria and the calculation of incentive amount, see [Smart+ Incentive Offer (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: The campaign is ineligible for any incentive offer. • `COST_CAP_AND_MIN_ROAS`: Ads groups within the campaign that use the Cost Cap or Minimum ROAS/Target ROAS bidding strategy are eligible for the incentive offer. |
| ↳ vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7).   • `ZERO_DAY`: The current day (day 0). |
| ↳ click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off.  •  `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click.  • `FOURTEEN_DAYS`: 14-day click. •  `TWENTY_EIGHT_DAYS`: 28-day click. |
| ↳ engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Các giá trị enum hỗ trợ: • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. |
| ↳ view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. |
| ↳ attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset.  •  `EVERY`: Every. To count multiple events from someone as separate conversions.  •  `ONCE`: Once. To count multiple events from someone as 1 conversion. |
| ↳ billing_event | string | Bid method. See [Enumerations - Bid method](../15-appendix/phu-luc-p1.md#doc-1737174886619138) for optional values. |
| ↳ location_ids | string[] | IDs of the locations that you want to target. ⏎ Use [Get locations](70-tools-p1.md#doc-1737189539571713) to get available locations. |
| ↳ languages | string[] | Codes of the languages that you want to target. For the list of language codes supported, see [Enumerations - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳ spc_audience_age | string | The age group that the campaign targets. ⏎ Enum value: `18+`, `25+`. ⏎ • For campaigns with the `LEAD_GENERATION` objective (Smart+ Lead Generation Campaigns), the value of this field can be either `18+` or `25+`.  • For campaigns with the `APP_PROMOTION` objective (Smart+ App Campaigns) or `WEB_CONVERSIONS` objective (Smart+ Web Campaigns or Smart Performance Web Campaigns), the value of this field can only be `18+`. ⏎ **Note**: Currently, creating Smart+ Lead Generation Campaigns via API is not supported. To filter existing Smart+ Lead Generation Campaigns with the `LEAD_GENERATION` objective within your ad account, call [/campaign/get/](24-campaign.md#doc-1739315828649986) and set `filtering` to `{"objective_type":"LEAD_GENERATION", "is_smart_performance_campaign": true}`. |
| ↳ exclude_age_under_eighteen | boolean | Có thực hiện exclude the group aged under eighteen. |
| ↳ excluded_audience_ids | string[] | List of audience IDs to be excluded. |
| ↳ placement_type | string | The placement strategy that decides where your ads will be shown. ⏎ Currently, we support `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳ placements | string[] | The apps where you want to deliver your ads. ⏎ Currently, we support `PLACEMENT_TIKTOK` and `PLACEMENT_PANGLE`. |
| ↳ comment_disabled | boolean | Có thực hiện allow comments on your ads on TikTok. |
| ↳ share_disabled | boolean | Liệu sharing to third-party platforms is disabled for ads in this ad group. |
| ↳ video_download_disabled | boolean | Liệu users can download your video ads on TikTok. |
| ↳ blocked_pangle_app_ids | string[] | Pangle app block ID list. |
| ↳ brand_safety_type | string | Inventory filter tier for the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Expanded inventory. Your ads will not appear next to explicitly inappropriate content, but they may appear next to content that features mature themes. • `STANDARD_INVENTORY`: Standard inventory. Your ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Limited inventory. Your ads will not appear next to content that contains mature themes. • `NO_BRAND_SAFETY`: Full inventory without using any brand safety solution, which means your ads may appear next to some content featuring mature themes. ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳ category_exclusion_ids | string[] | The ID list of content categories that you want to avoid showing the Smart+ Campaign next to. ⏎ To obtain the details of these content categories based on category IDs, use [/tool/content_exclusion/info/](70-tools-p2.md#doc-1769738105333826). ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳ budget_mode | string | Budget mode. ⏎ See [Enumerations-Budget Mode](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ budget_auto_adjust_strategy | string | Returned only when `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable automatic budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable automatic budget increase. |
| ↳ budget | float | Fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. |
| ↳ current_budget | float | Returned only when `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`. ⏎ Current campaign budget for a campaign with automatic budget increase enabled. |
| ↳ scheduled_budget | float | Scheduled campaign budget for the next day. ⏎ A value not equal to 0 means the scheduled budget is set and the value represents the budget; a value of 0 means the scheduled budget is not set. |
| ↳ schedule_type | string | Schedule type. ⏎ Currently, we support `SCHEDULE_START_END` and `SCHEDULE_FROM_NOW`. |
| ↳ schedule_start_time | string | Ad delivery start time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ schedule_end_time | string | Ad delivery end time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: Not specified, all-0, or all-1 are considered as full-time delivery. |
| ↳ skip_learning_phase | boolean | Có thực hiện skip the learning phase. |
| ↳ identity_id | string | Identity ID when you are not using Spark Ads. |
| ↳ identity_type | string | Identity type when you are not using Spark Ads. ⏎ Enum value: `CUSTOMIZED_USER`. |
| ↳ app_download_url | string | App download link. |
| ↳ app_name | string | The display name of the app download ad. |
| ↳ media_info_list | object[] | List of media information. |
| ↳↳ media_info | object | Material information. |
| ↳↳↳ video_info | object | Video information. |
| ↳↳↳↳ video_id | string | Video ID. |
| ↳↳↳↳ file_name | string | Video name. |
| ↳↳↳ image_info | object[] | Image information. |
| ↳↳↳↳ web_uri | string | Image ID. |
| ↳↳↳ music_info | object | Music information. |
| ↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳ aigc_disclosure_type | string | Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.  • `NOT_DECLARED`: To not declare that the ad contains AI-generated content. |
| ↳↳↳ tiktok_item_id | string | The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳↳↳ identity_type | string | Identity type when you use Spark Ads. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ identity_id | string | Identity ID when you use Spark Ads. |
| ↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ dark_post_status | string | The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. |
| ↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will use catalog creatives to automatically generate ads in diverse formats such as catalog video, catalog carousel, and single video. |
| ↳ title_list | object[] | List of ad titles (also called ad texts). Ad titles are shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. |
| ↳↳ title | string | Ad title (ad text). |
| ↳ call_to_action_id | string | The ID of the CTA portfolio that you want to use in your ads. |
| ↳ call_to_action_list | object[] | Call-to-action list. |
| ↳↳ call_to_action | string | Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ product_info | object | Additional product information. This information will be used to create ad variations to help achieve advertising goals such as standing out, building trust, or boosting performance. |
| ↳↳ promo_info_list | object[] | Valid only in [regular Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Details of promo codes and offers. ⏎ Promo codes and offers can help boost your ad performance. Make sure your codes and offers are active, accurate, and ready to use at checkout. |
| ↳↳↳ discount_type | string | Returned when `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳ discount_value | string | Returned when `promo_info_list` is specified. ⏎ Discount value. ⏎ • When `discount_type` is `PERCENTAGE`, this field will be an integer between 1-100. •  When `discount_type` is `CASH`, this field will be a float greater than 0. |
| ↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳ minimum_purchase_value | float | Returned when `minimum_purchase_type` is specified. ⏎ Minimum purchase value. ⏎ •  When `minimum_purchase_type` is `QUANTITY`, this field will be an integer that is 0 or greater. • When `minimum_purchase_type` is `SUBTOTAL`, this field will be a float greater than 0. |
| ↳↳↳ minimum_purchase_currency | string | Returned when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳ card_list | object[] | Creative portfolio ID list. |
| ↳↳ card_id | string | Creative portfolio ID. |
| ↳ automatic_add_on_enabled | boolean | Có thực hiện enable auto-selection of interactive add-ons. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will automatically apply the most suitable interactive add-ons to your ads. |
| ↳ page_list | object[] | Page ID list. |
| ↳↳ page_id | string | Page ID. |
| ↳ deeplink | string | The specific location where you want your audience to go if they have your app installed. |
| ↳ deeplink_type | string | The deeplink type. |
| ↳ landing_page_urls | object[] | Landing page URL list. |
| ↳↳ landing_page_url | string | Landing page URL. |
| ↳↳ video_id | string | Returned when the campaign is in multiple landing page mode. ⏎ Video ID. |
| ↳↳ tiktok_item_id | string | Returned when the campaign is in multiple landing page mode. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳ utm_params | object[] | A list of URL parameters. ⏎ URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳ key | string | The URL parameter. ⏎ The parameter can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, and video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, and color. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. |
| ↳↳ value | string | The value of the URL parameter. ⏎ The value can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳ disclaimer_info | object | Details of the disclaimer. |
| ↳↳ disclaimer_type | string | The type of disclaimer that you want to add to the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. |
| ↳↳ disclaimer_text | object | Returned when `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer that you want to add to the ad. |
| ↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳↳ disclaimer_clickable_texts | object[] | Returned when `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. |
| ↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳↳ url | string | The URL for the clickable disclaimer. When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ↳ tracking_app_id | string | The ID of the app that is measured. |
| ↳ impression_tracking_url | string | Default Impression Tracking URL. |
| ↳ click_tracking_url | string | Click Tracking URL. |
| ↳ app_tracking_info_list | object[] | Details of Third-party tracking settings. |
| ↳↳ app_type | string | Returned when `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳ app_id | string | Returned when `app_tracking_info_list` is specified. ⏎ The App ID of the App. ⏎ • When `app_type` is `APP_ANDROID`, this field represents the App ID for an Android App. • When `app_type` is `APP_IOS`, this field represents the App ID for an iOS App. |
| ↳↳ impression_tracking_url | string | Impression tracking URL. ⏎ When `app_type` is `APP_ANDROID`, this field represents an impression tracking URL for Android. •  • When `app_type` is `APP_IOS`, this field represents an impression tracking URL for iOS. |
| ↳↳ click_tracking_url | string | Click tracking URL. ⏎ • When `app_type` is `APP_ANDROID`, this field represents a click tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents a click tracking URL for iOS. |
| ↳ create_time | string | The time when the campaign was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ modify_time | string | The time when the campaign was modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "campaign_id": "{{campaign_id}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "pixel_id": null,
        "app_type": "APP_ANDROID",
        "objective_type": "APP_PROMOTION",
        "campaign_name": "{{campaign_name}}",
        "is_smart_performance_campaign": true,
        "operation_status": "ENABLE",
        "campaign_secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "adgroup_secondary_status": "ADGROUP_STATUS_CREATE",
        "campaign_type": "REGULAR_CAMPAIGN",
        "app_promotion_type": "APP_INSTALL",
        "optimization_goal": "CLICK",
        "bid_type": "BID_TYPE_NO_BID",
        "deep_bid_type": null,
        "skip_learning_phase": null,
        "budget": {{budget}},
        "budget_mode": "BUDGET_MODE_DAY",
        "scheduled_budget": {{scheduled_budget}},
        "promotion_type": "APP_ANDROID",
        "optimization_event": "ACTIVE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "placement_type": "PLACEMENT_TYPE_NORMAL",
        "promotion_website_type": null,
        "comment_disabled": true,
        "share_disabled": true,
        "video_download_disabled": true,
        "location_ids": [
            "{{location_ids}}"
        ],
        "languages": [
            "{{languages}}"
        ],
        "exclude_age_under_eighteen": false,
        "excluded_audience_ids": null,
        "blocked_pangle_app_ids": null,
        "special_industries": null,
        "schedule_type": "SCHEDULE_FROM_NOW",
        "schedule_start_time": "2024-04-17 22:00:00",
        "schedule_end_time": "2034-04-15 22:00:00",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "billing_event": "CPC",
        "app_download_url": "{{app_download_url}}",
        "app_name": "{{app_name}}",
        "call_to_action_id": null,
        "call_to_action_list": [
            {
                "call_to_action": "INSTALL_NOW"
            },
            {
                "call_to_action": "DOWNLOAD_NOW"
            }
        ],
        "media_info_list": [
            {
                "media_info": {
                    "video_info": {
                        "video_id": "{{video_id}}",
                        "file_name": "{{file_name}}"
                    },
                    "identity_id": null,
                    "image_info": [
                        {
                            "web_uri": "{{web_url}}"
                        }
                    ],
                    "identity_type": null,
                    "tiktok_item_id": null
                }
            }
        ],
        "title_list": [
            {
                "title": "{{title}}"
            },
            {
                "title": "{{title}}"
            }
        ],
        "page_list": null,
        "card_list": null,
        "landing_page_urls": null,
        "deeplink": "{{deeplink}}",
        "deeplink_type": "DEFERRED_DEEPLINK",
        "identity_id": "{{identity_id}}",
        "identity_type": "CUSTOMIZED_USER",
        "impression_tracking_url": null,
        "click_tracking_url": "{{click_tracking_url}}",
        "create_time": "{{create_time}}",
        "modify_time": "{{modify_time}}"
    }
}
```

---

<a id="doc-1767334299811842"></a>
<!-- doc_id: 1767334299811842 -->
<!-- doc_id: 1767334299811842 -->
# (Sắp ngừng hỗ trợ) Lấy danh sách chiến dịch Smart+ phiên bản cũ (Get Legacy Smart+ Campaigns)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Get Legacy Smart+ Campaigns
Dùng endpoint này để lấy thông tin chi tiết của các chiến dịch Smart+ và chiến dịch Smart Performance Web.  

> **Important:** 
>
> - **Upgraded Smart+ API**:
>   - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>   - **Get started**:
>     - **Reporting**: No additional allowlist required.
>     - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>   - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>   - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.

> **Note:** 
> Smart Performance Web Campaigns will be deprecated in the next API version. To ensure a smooth API integration, we recommend that you upgrade to [Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186) as soon as possible. Smart+ Web Campaigns are a new AI-powered automation solution that leverages machine learning to drive business outcomes for advertisers.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/campaign/spc/get/`

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| campaign_ids  ****(Bắt buộc)**** | string[] | A list of campaign IDs. ⏎ Kích thước tối đa: 100. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl -H "Access-Token:{{Access-Token}}" -H "Content-Type:application/json" -X GET \
-d '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_ids": ["{{campaign_ids}}"]
}' \
https://business-api.tiktok.com/open_api/v1.3/campaign/spc/get/
(/code)
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ list | object[] | A list of Smart+ Campaigns or Smart Performance Web Campaigns. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳↳ operation_status | string | The status of the campaign. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled. • `DISABLE` : The campaign is disabled. |
| ↳↳ campaign_secondary_status | string | Campaign status (Secondary status). ⏎ For the supported campaign secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/campaign/get/](24-campaign.md#doc-1739315828649986). |
| ↳↳ is_smart_performance_campaign | boolean | Liệu campaign is an automated campaign type. ⏎ Các giá trị được hỗ trợ: • `true`: The campaign is either a Smart+ Campaign or a Smart Performance Web Campaign.  • `false`: The campaign is a standard campaign type. ⏎ **Note**: If `is_smart_performance_campaign` is `true` and `objective_type` is `WEB_CONVERSIONS`, you can confirm Liệu web campaign is a Smart+ Web Campaign or Smart Performance Web Campaign by checking the returned `spc_type`. |
| ↳↳ objective_type | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. |
| ↳↳ spc_type | string | The web campaign type. ⏎ Các giá trị enum hỗ trợ: • `WEB_ALL_IN_ONE`: Smart+ Web Campaign, where the supported optimization goals include Conversion, Value, Click and Landing page view. • `UNSET`: Smart Performance Web Campaign, where the supported optimization goals are limited to Conversion, Value, and Click. |
| ↳↳ web_all_in_one_catalog_status | string | The status of catalog in the Smart+ Web Campaign. ⏎ Các giá trị enum hỗ trợ: • `OPEN`: enabled. • `UNSET`: disabled. |
| ↳↳ app_promotion_type | string | App promotion type. ⏎ Currently, we only support `APP_INSTALL`. |
| ↳↳ virtual_objective_type | string | The new objective type. ⏎ Enum value: `SALES`. ⏎ Use this field to create a campaign with the Sales objective, the combined objective for Website Lượt chuyển đổi and Product Sales objectives. Learn more about [the Sales objective](https://business-api.tiktok.com/portal/docs?id=). |
| ↳↳ sales_destination | string | Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. |
| ↳↳ campaign_type | string | Campaign Type. ⏎ Currently, we support `REGULAR_CAMPAIGN` and `IOS14_CAMPAIGN`. |
| ↳↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị enum hỗ trợ: `true`, `false`. |
| ↳↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition).  • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (`conversion_bid_price`) or ROAS (`roas_bid`) is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN.  • `SKAN`: SKAN. |
| ↳↳ campaign_name | string | Campaign name. |
| ↳↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳↳ adgroup_secondary_status | string | Ad group status (Secondary status). ⏎ For the supported adgroup secondary statuses for a certain primary status, see [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002). ⏎ It is equal to `secondary_status` in [/adgroup/get/](24-campaign.md#doc-1739315828649986). |
| ↳↳ product_source | string | Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| ↳↳ catalog_id | string | The ID of the catalog to use in the Smart+ Catalog Ads. |
| ↳↳ catalog_authorized_bc_id | string | The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| ↳↳ product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products.  • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. |
| ↳↳ product_set_id | string | The ID of a product set. |
| ↳↳ product_ids | string[] | The product IDs of the catalog products. |
| ↳↳ promotion_type | string | Promotion type (Optimization location) and you can decide where you'd like to promote your products using this field. For value definitions, see [Enumerations - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ app_id | string | The App ID of the app to promote. ⏎ You can get `app_id` by using the [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) endpoint. |
| ↳↳ app_type | string | The type of the promoted app. ⏎ Currently, we support `APP_ANDROID` and `APP_IOS`. |
| ↳↳ promotion_website_type | string | TikTok Instant Page type. ⏎ Currently, we only support `TIKTOK_NATIVE_PAGE`(To use TikTok Instant Page). |
| ↳↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ pixel_id | string | ID TikTok Pixel. |
| ↳↳ optimization_event | string | Conversion event for the ad group. ⏎ See [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) for more. |
| ↳↳ app_config | object[] | Returned when `sales_destination` is `WEB_AND_APP`. ⏎ Details of the app or apps to promote. |
| ↳↳↳ app_id | string | The App ID of the app to promote. |
| ↳↳ deep_funnel_optimization_status | string | The status of deep funnel optimization. ⏎ With deep funnel optimization, you can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: enabled.   •  `OFF`: disabled. |
| ↳↳ deep_funnel_event_source | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel.   • `OFFLINE`: Offline Event Set.  • `CRM`: CRM Event Set. |
| ↳↳ deep_funnel_event_source_id | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. ⏎ • When `deep_funnel_event_source` is `PIXEL` , this field represents a ID TikTok Pixel. • When `deep_funnel_event_source` is `OFFLINE`, this field represents an Offline Event Set ID.   • When `deep_funnel_event_source` is `CRM`, this field represents a CRM Event Set ID. |
| ↳↳ deep_funnel_optimization_event | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ Example: `SHOPPING`. |
| ↳↳ bid_type | string | Bidding strategy. ⏎ For enum values and their descriptions, see [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ bid_price | float | The target cost per click. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳↳ conversion_bid_price | float | The target cost per conversion or cost per landing page view. The system will aim to get the most results while keeping the average cost per result around or lower than the specified amount. |
| ↳↳ deep_bid_type | string | Bidding strategy for in-app events. ⏎ For enum values and their descriptions, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ roas_bid | float | Target ROAS for Value-Based Optimization. |
| ↳↳ incentive_offer_type | string | The type of incentive offer applicable to the Smart+ Campaign. ⏎ If your campaign meets the eligibility criteria, but underperforms against certain CPA or Minimum ROAS thresholds you will be reimbursed with part of the gap with ad credits within the same ad account. ⏎ To learn more about the incentive offer eligibility criteria and the calculation of incentive amount, see [Smart+ Incentive Offer (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: The campaign is ineligible for any incentive offer. • `COST_CAP_AND_MIN_ROAS`: Ads groups within the campaign that use the Cost Cap or Minimum ROAS/Target ROAS bidding strategy are eligible for the incentive offer. |
| ↳↳ vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7).   • `ZERO_DAY`: The current day (day 0). |
| ↳↳ click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off.  •  `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click.  • `FOURTEEN_DAYS`: 14-day click. •  `TWENTY_EIGHT_DAYS`: 28-day click. |
| ↳↳ view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. |
| ↳↳ engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Các giá trị enum hỗ trợ: • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. |
| ↳↳ attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset.  •  `EVERY`: Every. To count multiple events from someone as separate conversions.  •  `ONCE`: Once. To count multiple events from someone as 1 conversion. |
| ↳↳ billing_event | string | Bid method. See [Enumerations - Bid method](../15-appendix/phu-luc-p1.md#doc-1737174886619138) for optional values. |
| ↳↳ location_ids | string[] | IDs of the locations that you want to target. ⏎ Use [Get locations](70-tools-p1.md#doc-1737189539571713) to get available locations. |
| ↳↳ languages | string[] | Codes of the languages that you want to target. For the list of language codes supported, see [Enumerations - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳↳ spc_audience_age | string | The age group that the campaign targets. ⏎ Enum value: `18+`, `25+`. ⏎ • For campaigns with the `LEAD_GENERATION` objective (Smart+ Lead Generation Campaigns), the value of this field can be either `18+` or `25+`.  • For campaigns with the `APP_PROMOTION` objective (Smart+ App Campaigns) or `WEB_CONVERSIONS` objective (Smart+ Web Campaigns or Smart Performance Web Campaigns), the value of this field can only be `18+`. ⏎ **Note**: Currently, creating Smart+ Lead Generation Campaigns via API is not supported. To filter existing Smart+ Lead Generation Campaigns with the `LEAD_GENERATION` objective within your ad account, call [/campaign/get/](24-campaign.md#doc-1739315828649986) and set `filtering` to `{"objective_type":"LEAD_GENERATION", "is_smart_performance_campaign": true}`. |
| ↳↳ exclude_age_under_eighteen | boolean | Có thực hiện exclude the group aged under eighteen. |
| ↳↳ excluded_audience_ids | string[] | List of audience IDs to be excluded. |
| ↳↳ placement_type | string | The placement strategy that decides where your ads will be shown. ⏎ Currently, we support `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TYPE_AUTOMATIC`. |
| ↳↳ placements | string[] | The apps where you want to deliver your ads. ⏎ Currently, we support `PLACEMENT_TIKTOK` and `PLACEMENT_PANGLE`. |
| ↳↳ comment_disabled | boolean | Có thực hiện allow comments on your ads on TikTok. |
| ↳↳ share_disabled | boolean | Liệu sharing to third-party platforms is disabled for ads in this ad group. |
| ↳↳ video_download_disabled | boolean | Liệu users can download your video ads on TikTok. |
| ↳↳ blocked_pangle_app_ids | string[] | Pangle app block ID list. |
| ↳↳ brand_safety_type | string | Inventory filter tier for the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Expanded inventory. Your ads will not appear next to explicitly inappropriate content, but they may appear next to content that features mature themes. • `STANDARD_INVENTORY`: Standard inventory. Your ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Limited inventory. Your ads will not appear next to content that contains mature themes. • `NO_BRAND_SAFETY`: Full inventory without using any brand safety solution, which means your ads may appear next to some content featuring mature themes. ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳↳ category_exclusion_ids | string[] | The ID list of content categories that you want to avoid showing the Smart+ Campaign next to. ⏎ To obtain the details of these content categories based on category IDs, use [/tool/content_exclusion/info/](70-tools-p2.md#doc-1769738105333826). ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳↳ budget_mode | string | Budget mode. ⏎ See [Enumerations-Budget Mode](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ budget_auto_adjust_strategy | string | Returned only when `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable automatic budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable automatic budget increase. |
| ↳↳ budget | float | Fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. |
| ↳↳ current_budget | float | Returned only when `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`. ⏎ Current campaign budget for a campaign with automatic budget increase enabled. |
| ↳↳ scheduled_budget | float | Scheduled campaign budget for the next day. ⏎ A value not equal to 0 means the scheduled budget is set and the value represents the budget; a value of 0 means the scheduled budget is not set. |
| ↳↳ schedule_type | string | Schedule type. ⏎ Currently, we support `SCHEDULE_START_END` and `SCHEDULE_FROM_NOW`. |
| ↳↳ schedule_start_time | string | Ad delivery start time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ schedule_end_time | string | Ad delivery end time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: Not specified, all-0, or all-1 are considered as full-time delivery. |
| ↳↳ skip_learning_phase | boolean | Có thực hiện skip the learning phase. |
| ↳↳ identity_id | string | Identity ID when you are not using Spark Ads. |
| ↳↳ identity_type | string | Identity type when you are not using Spark Ads. ⏎ Enum value: `CUSTOMIZED_USER`. |
| ↳↳ app_download_url | string | App download link. |
| ↳↳ app_name | string | The display name of the app download ad. |
| ↳↳ media_info_list | object[] | List of media information. |
| ↳↳↳ ad_material_id | string | The ad material ID for the creative within the campaign. ⏎ An ad material ID is an ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID that you obtain when uploading the creative to your ad account’s Creative Library. |
| ↳↳↳ material_operation_status | string | The status of the creative. ⏎ Các giá trị enum hỗ trợ: • `DISABLE`: The creative is disabled (in 'OFF' status). • `ENABLE`: The creative is enabled (in 'ON' status). |
| ↳↳↳ media_info | object | Material information. |
| ↳↳↳↳ image_info | object[] | Image information. |
| ↳↳↳↳↳ web_uri | string | Image ID. |
| ↳↳↳↳ video_info | object | Video information. |
| ↳↳↳↳↳ video_id | string | Video ID. |
| ↳↳↳↳↳ file_name | string | Video name. |
| ↳↳↳↳ music_info | object | Music information. |
| ↳↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳↳ aigc_disclosure_type | string | Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.  • `NOT_DECLARED`: To not declare that the ad contains AI-generated content. |
| ↳↳↳↳ tiktok_item_id | string | The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳↳↳↳ identity_type | string | Identity type when you use Spark Ads. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳↳ identity_id | string | Identity ID when you use Spark Ads. |
| ↳↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ dark_post_status | string | The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. |
| ↳↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will use catalog creatives to automatically generate ads in diverse formats such as catalog video, catalog carousel, and single video. |
| ↳↳ title_list | object[] | List of ad titles (also called ad texts). Ad titles are shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. |
| ↳↳↳ title | string | Ad title (ad text). |
| ↳↳ call_to_action_id | string | The ID of the CTA portfolio that you want to use in your ads. |
| ↳↳ call_to_action_list | object[] | Call-to-action list. |
| ↳↳↳ call_to_action | string | Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ product_info | object | Additional product information. This information will be used to create ad variations to help achieve advertising goals such as standing out, building trust, or boosting performance. |
| ↳↳↳ promo_info_list | object[] | Valid only in [regular Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). ⏎ Details of promo codes and offers. ⏎ Promo codes and offers can help boost your ad performance. Make sure your codes and offers are active, accurate, and ready to use at checkout. |
| ↳↳↳↳ discount_type | string | Returned when `promo_info_list` is specified. ⏎ Discount type. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳↳ discount_value | string | Returned when `promo_info_list` is specified. ⏎ Discount value. ⏎ • When `discount_type` is `PERCENTAGE`, this field will be an integer between 1-100. •  When `discount_type` is `CASH`, this field will be a float greater than 0. |
| ↳↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Discount currency. ⏎ Để xem danh sách giá trị enum, xem [List of values for `discount_currency` or `minimum_purchase_currency`](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362). |
| ↳↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳↳ minimum_purchase_value | float | Returned when `minimum_purchase_type` is specified. ⏎ Minimum purchase value. ⏎ •  When `minimum_purchase_type` is `QUANTITY`, this field will be an integer that is 0 or greater. • When `minimum_purchase_type` is `SUBTOTAL`, this field will be a float greater than 0. |
| ↳↳↳↳ minimum_purchase_currency | string | Returned when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Minimum purchase currency. ⏎ Để xem danh sách giá trị enum, xem [List of values for `discount_currency` or `minimum_purchase_currency`](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362). |
| ↳↳↳↳ valid_start_time | string | Valid start time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳↳ valid_end_time | string | Valid end time (UTC+0) for the promo code or offer, in the format of `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ card_list | object[] | Creative portfolio ID list. |
| ↳↳↳ card_id | string | Creative portfolio ID. |
| ↳↳ automatic_add_on_enabled | boolean | Có thực hiện enable auto-selection of interactive add-ons. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ If you set this field to `true`, the system will automatically apply the most suitable interactive add-ons to your ads. |
| ↳↳ page_list | object[] | Page ID list. |
| ↳↳↳ page_id | string | Page ID. |
| ↳↳ deeplink | string | The specific location where you want your audience to go if they have your app installed. |
| ↳↳ deeplink_type | string | The deeplink type. |
| ↳↳ landing_page_urls | object[] | Landing page URL list. |
| ↳↳↳ landing_page_url | string | Landing page URL. |
| ↳↳↳ video_id | string | Returned when the campaign is in multiple landing page mode. ⏎ Video ID. |
| ↳↳↳ tiktok_item_id | string | Returned when the campaign is in multiple landing page mode. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳↳ utm_params | object[] | A list of URL parameters. ⏎ URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳ key | string | The URL parameter. ⏎ The parameter can be a custom parameter or a UTM parameter. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, and video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, and color. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. ⏎ Note that UTM parameters are case-sensitive. |
| ↳↳↳ value | string | The value of the URL parameter. ⏎ The value can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳ disclaimer_info | object | Details of the disclaimer. |
| ↳↳↳ disclaimer_type | string | The type of disclaimer that you want to add to the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. |
| ↳↳↳ disclaimer_text | object | Returned when `disclaimer_type` is `TEXT_ONLY`. ⏎ The text-only disclaimer that you want to add to the ad. |
| ↳↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 90 characters. |
| ↳↳↳ disclaimer_clickable_texts | object[] | Returned when `disclaimer_type` is `TEXT_LINK`. ⏎ The clickable disclaimer or clickable disclaimers that you want to add to the ad. |
| ↳↳↳↳ text | string | The disclaimer text. ⏎ Giới hạn độ dài: 40 characters. |
| ↳↳↳↳ url | string | The URL for the clickable disclaimer. When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ↳↳ tracking_app_id | string | The ID of the app that is measured. |
| ↳↳ impression_tracking_url | string | Default Impression Tracking URL. |
| ↳↳ click_tracking_url | string | Click Tracking URL. |
| ↳↳ app_tracking_info_list | object[] | Details of Third-party tracking settings. |
| ↳↳↳ app_type | string | Returned when `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳↳ app_id | string | Returned when `app_tracking_info_list` is specified. ⏎ The App ID of the App. ⏎ • When `app_type` is `APP_ANDROID`, this field represents the App ID for an Android App. • When `app_type` is `APP_IOS`, this field represents the App ID for an iOS App. |
| ↳↳↳ impression_tracking_url | string | Impression tracking URL. ⏎ When `app_type` is `APP_ANDROID`, this field represents an impression tracking URL for Android. •  • When `app_type` is `APP_IOS`, this field represents an impression tracking URL for iOS. |
| ↳↳↳ click_tracking_url | string | Click tracking URL. ⏎ • When `app_type` is `APP_ANDROID`, this field represents a click tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents a click tracking URL for iOS. |
| ↳↳ create_time | string | The time when the campaign was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ modify_time | string | The time when the campaign was modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [        
       { "campaign_id": "{{campaign_id}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "pixel_id": null,
        "app_type": "APP_ANDROID",
        "objective_type": "APP_PROMOTION",
        "campaign_name": "{{campaign_name}}",
        "is_smart_performance_campaign": true,
        "operation_status": "ENABLE",
        "campaign_secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "adgroup_secondary_status": "ADGROUP_STATUS_CREATE",
        "campaign_type": "REGULAR_CAMPAIGN",
        "app_promotion_type": "APP_INSTALL",
        "optimization_goal": "CLICK",
        "bid_type": "BID_TYPE_NO_BID",
        "deep_bid_type": null,
        "skip_learning_phase": null,
        "budget": {{budget}},
        "budget_mode": "BUDGET_MODE_DAY",
        "scheduled_budget": {{scheduled_budget}},
        "promotion_type": "APP_ANDROID",
        "optimization_event": "ACTIVE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "placement_type": "PLACEMENT_TYPE_NORMAL",
        "promotion_website_type": null,
        "comment_disabled": true,
        "share_disabled": true,
        "video_download_disabled": true,
        "location_ids": [
            "{{location_ids}}"
        ],
        "languages": [
            "{{languages}}"
        ],
        "exclude_age_under_eighteen": false,
        "excluded_audience_ids": null,
        "blocked_pangle_app_ids": null,
        "special_industries": null,
        "schedule_type": "SCHEDULE_FROM_NOW",
        "schedule_start_time": "2024-04-17 22:00:00",
        "schedule_end_time": "2034-04-15 22:00:00",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "billing_event": "CPC",
        "app_download_url": "{{app_download_url}}",
        "app_name": "{{app_name}}",
        "call_to_action_id": null,
        "call_to_action_list": [
            {
                "call_to_action": "INSTALL_NOW"
            },
            {
                "call_to_action": "DOWNLOAD_NOW"
            }
        ],
        "media_info_list": [
            {
                "media_info": {
                    "video_info": {
                        "video_id": "{{video_id}}",
                        "file_name": "{{file_name}}"
                    },
                    "identity_id": null,
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "identity_type": null,
                    "tiktok_item_id": null
                }
            }
        ],
        "title_list": [
            {
                "title": "{{title}}"
            },
            {
                "title": "{{title}}"
            }
        ],
        "page_list": null,
        "card_list": null,
        "landing_page_urls": null,
        "deeplink": "{{deeplink}}",
        "deeplink_type": "DEFERRED_DEEPLINK",
        "identity_id": "{{identity_id}}",
        "identity_type": "CUSTOMIZED_USER",
        "impression_tracking_url": null,
        "click_tracking_url": "{{click_tracking_url}}",
        "create_time": "{{create_time}}",
        "modify_time": "{{modify_time}}"
        }
	  ]    
    }
}
(/code)
```

---

<a id="doc-1837969177953361"></a>
<!-- doc_id: 1837969177953361 -->
<!-- doc_id: 1837969177953361 -->
# (Sắp ngừng hỗ trợ) Bật hoặc tắt mẫu sáng tạo trong chiến dịch Smart+ phiên bản cũ (Disable or enable creatives in a Legacy Smart+ Campaign)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Disable or enable creatives in a Legacy Smart+ Campaign
Dùng endpoint này để tắt hoặc bật một hoặc nhiều creative trong chiến dịch Smart+. 

Creative có thể là video, carousel hoặc bài đăng TikTok. 

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/spc/material_status/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|campaign_id***(Bắt buộc)***|string|The ID of a Smart+ Campaign.<br><br>To retrieve existing Smart+ Campaigns within your ad account, use [/campaign/get/](24-campaign.md#doc-1739315828649986) and set `filtering` to `&#123;"is_smart_performance_campaign" : true&#125;`.|
|ad_material_ids***(Bắt buộc)***|string[]|A list of ad material IDs for creatives to operate on.<br>An ad material ID is an ad-specific material ID generated when a particular creative is used in a Smart+ ad. This ID differs from the creative ID you obtain when uploading the creative to your ad account’s Creative Library.<br><br>To obtain ad material IDs associated with a Smart+ ad, use [/campaign/spc/get/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842).<br><br>Kích thước tối đa: 20.<br><br>The number of creatives you can operate on varies based on the type of creatives you want to operate on:<ul><li>If you want to operate on the following types of creatives, you can only specify one ID in `ad_material_ids`:<ul><li>a carousel in Spark Ad Standard Carousel created through Sparks Ads Push</li><li>a carousel in non-Spark Ad Standard Carousel</li></ul></li><li>If you want to operate on the following types of creatives, you can specify up to 20 IDs in `ad_material_ids`:<ul><li>non-Spark Ad Video</li><li>Spark Ad Video created through Sparks Ads Push</li><li>TikTok video posts in Spark Ad Video created through Sparks Ads Pull</li><li>TikTok photo posts in Spark Ad Standard Carousel created through Sparks Ads Pull</li></ul></li></ul>|
|material_status***(Bắt buộc)***|string|The operation to perform on the creatives.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DISABLE`: disable.</li><li>`ENABLE`: enable.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/material_status/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "ad_material_ids": ["{{ad_material_id}}"],
    "material_status": "DISABLE"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#|campaign_id|string|The ID of a Smart+ Campaign.|
#|ad_material_ids|string[]|A list of ad material IDs for creatives operated on.<br>An ad material ID is an ad-specific material ID generated when a particular creative is used in a Smart+ ad.<br> This ID differs from the creative ID you obtain when uploading the creative to your ad account’s Creative Library.|
#|material_status|string|The statuses of the creatives.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DISABLE`: The creatives are disabled (in 'OFF' status).</li><li>`ENABLE`: The creatives are enabled (in 'ON' status).</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "material_status": "DISABLE",
        "campaign_id": "{{campaign_id}}",
        "ad_material_ids": [
            "{{ad_material_id}}"
        ]
    }
}
```

---

<a id="doc-1776454619412481"></a>
<!-- doc_id: 1776454619412481 -->
<!-- doc_id: 1776454619412481 -->
# (Sắp ngừng hỗ trợ) Chạy báo cáo chiến dịch Smart+ phiên bản cũ (Run a Legacy Smart+ Campaign report)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Run a Legacy Smart+ Campaign report
Dùng endpoint này để chạy báo cáo cho các chiến dịch Smart+ và Smart Performance Web ở cấp creative (video, nội dung quảng cáo, bài đăng Spark Ad, video catalog hoặc carousel catalog). 

> **Important:** 
> - **Upgraded Smart+ API**:
>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại hiệu suất và năng lực nâng cao. Upgraded Smart+ API mới đã được ra mắt. Tìm hiểu thêm về [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458) và [các endpoint Upgraded Smart+ API khả dụng](62-upgraded-smartplus-p1.md#doc-1843301794874370).
>     - **Get started**:
>         - **Reporting**: No additional allowlist required.
>         - **Campaign Management**: Để truy cập trải nghiệm Smart+ nâng cấp, hãy liên hệ với đại diện kinh doanh TikTok để đưa tài khoản quảng cáo của bạn vào danh sách cho phép (allowlist). Nếu tài khoản quảng cáo của bạn đã nằm trong danh sách cho phép, bạn có thể trực tiếp sử dụng các endpoint tạo và chỉnh sửa của Upgraded Smart+ API.  
> - **Legacy API Deprecation**: 
>     - Sau ngày **31 tháng 3 năm 2026**, bạn sẽ không thể tạo các Chiến dịch Smart+ phiên bản cũ bằng endpoint [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362).
>     - Lưu ý rằng các Chiến dịch Smart+ cũ chưa được chuyển đổi sẽ không tự động chuyển sang API mới. Việc cố gắng gọi endpoint Legacy Smart+ API sau này sẽ bị trả về lỗi, khiến việc tạo chiến dịch mới qua endpoint này không khả dụng.
> - **Legacy API deprecation extension request process for existing legacy Smart+ creation developers**:
>     - 1. **Submit a request**: Nếu bạn yêu cầu gia hạn, vui lòng gửi đơn đăng ký qua [Biểu mẫu yêu cầu gia hạn bên ngoài cho Legacy Smart+ Creation API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgsm2yMsQaSoAsMy77tcAzng).
>     - 2. **Allowlist processing**: Sau khi nhận được yêu cầu, chúng tôi sẽ xử lý đưa ID ứng dụng nhà phát triển liên kết vào danh sách cho phép. Sau khi hoàn tất, nhà phát triển có thể tiếp tục gọi endpoint `/campaign/spc/create/` cho đến ngày **30 tháng 6 năm 2026**.
>     - 3. **Extended timeline for strong business needs**: Nếu bạn có nhu cầu kinh doanh quan trọng yêu cầu gia hạn sau ngày 30 tháng 6 năm 2026, vui lòng nêu rõ tình huống sử dụng trong biểu mẫu ứng dụng hoặc liên hệ trực tiếp với đại diện bán hàng.

>  **Note:** 
>    • Dữ liệu trả về qua endpoint này có thể có độ trễ khoảng 30 phút.  • Smart Performance Web Campaigns will be deprecated in the next API version. To ensure a smooth API integration, we recommend that you upgrade to [Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186) as soon as possible. Smart+ Web Campaigns are a new AI-powered automation solution that leverages machine learning to drive business outcomes for advertisers.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| campaign_ids  ****(Bắt buộc)**** | string[] | List of campaign IDs. ⏎ Kích thước tối đa: 1. |
| material_type  ****(Bắt buộc)**** | string | Creative material type. ⏎ Các giá trị enum hỗ trợ: `SPC_VIDEO`, `SPC_AD_TEXT`, `SPC_SPARK`, `SPC_CATALOG_VIDEO`, `SPC_CATALOG_CAROUSEL`.  • If `material_type` is `SPC_VIDEO`, you can retrieve data on videos. You can specify basic data, video play, interaction, in-app event, in-app event (SKAN), page event, date, and video material details metric in the `metrics` field.  • If `material_type` is `SPC_AD_TEXT`, you can retrieve data on ad texts. You can only specify basic data, interaction, in-app event, in-app event (SKAN), page event, and date metrics in the `metrics` field.  • If `material_type` is `SPC_SPARK`, you can retrieve data on Spark Ad posts. You can only specify basic data, interaction, in-app event, in-app event (SKAN), and page event metrics in the `metrics` field. • If `material_type` is `SPC_CATALOG_VIDEO`, you can retrieve data on catalog videos. You can only specify basic data, interaction, in-app event, in-app event (SKAN), page event and date metrics in the `metrics` field. • If `material_type` is `SPC_CATALOG_CAROUSEL`, you can retrieve data on catalog carousel. You can only specify basic data, interaction, in-app event, in-app event (SKAN), page event and date metrics in the `metrics` field. ⏎ To learn about the specific metrics within each metric type, see [Metrics in Smart+ Campaign reports](61-to-be-deprecated-legacy-smartplus.md#doc-1776461365424129). ⏎ **Note**:   • When`material_type` is set to `SPC_SPARK`, ensure the `campaign_ids` field only includes a campaign that contains Spark Ads exclusively. If any campaign specified within `campaign_ids` contains both Spark Ads and non-Spark Ads, an empty list will be returned. • Smart+ Campaign reports of the `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL` type are only supported for [Smart+ Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1814122471133186). |
| is_include_removed_material | boolean | Chỉ hợp lệ khi `material_type` is `SPC_VIDEO`, `SPC_AD_TEXT`, or `SPC_SPARK`. ⏎ Có thực hiện query data of deleted videos, texts, or posts. ⏎ Các giá trị được hỗ trợ: • `true`: Include data of deleted videos, texts, or posts in the response.  • `false` : Not include data of deleted videos, texts, or posts in the response.Giá trị mặc định: `true`. |
| metrics | string[] | Metrics to query. ⏎ Giá trị mặc định: `["spend", "impressions"]` . ⏎ Refer to [Metrics in Smart+ Campaign reports](61-to-be-deprecated-legacy-smartplus.md#doc-1776461365424129) for all supported metrics for a report. |
| query_lifetime | boolean | Có thực hiện request the lifetime metrics. ⏎ Giá trị mặc định: `false`. ⏎ If `query_lifetime` = `true`, the `start_date` and `end_date` parameters will be ignored. |
| start_date  **(Điều kiện)** | string | Bắt buộc khi `query_lifetime` is `false` or not specified. ⏎ Query start date (closed interval) in the format of `YYYY-MM-DD`. ⏎ The date is based on the ad account time zone. |
| end_date  **(Điều kiện)** | string | Bắt buộc khi `query_lifetime` is `false` or not specified. ⏎ Query end date (closed interval) in the format of `YYYY-MM-DD`. ⏎ The date is based on the ad account time zone. ⏎ **Note**: The time difference between `start_date` and `end_date` must be less than 365 days. |
| page | number | Current Số trang cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. |
| page_size | number | Page size. ⏎ Value range: 1-100. ⏎ Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
#### Run a report on videos
```http
// curl
curl --location -request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/?advertiser_id={{advertiser_id}}&material_type=SPC_VIDEO&campaign_ids=[["{{campaign_id}}"]]&query_lifetime=true&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
#### Run a report on ad texts
```http
// curl
curl --location -request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/?advertiser_id={{advertiser_id}}&material_type=SPC_AD_TEXT&campaign_ids=[["{{campaign_id}}"]]&query_lifetime=true&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
#### Run a report on Spark Ad posts
```http
// curl
curl --location -request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/?advertiser_id={{advertiser_id}}&material_type=SPC_SPARK&campaign_ids=["{{campaign_id}}"]&query_lifetime=true&is_include_removed_material=true&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
#### Run a report on catalog videos
```http
// curl
curl --location -request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/?advertiser_id={{advertiser_id}}&material_type=SPC_CATALOG_VIDEO&campaign_ids=["{{campaign_id}}"]&query_lifetime=true&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
#### Run a report on catalog carousel
```http
// curl
curl --location -request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/spc/report/get/?advertiser_id={{advertiser_id}}&material_type=SPC_CATALOG_CAROUSEL&campaign_ids=["{{campaign_id}}"]&query_lifetime=true&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. ⏎ For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. ⏎ Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The unique ID of the request. |
| data | object | Returned data. |
| ↳ list | object[] | Data list. |
| ↳↳ dimensions | object | Dimension data. |
| ↳↳↳ material_id | string | Material ID. |
| ↳↳↳ campaign_id | string | Returned only when `material_type` is `SPC_VIDEO`, `SPC_AD_TEXT`, or `SPC_SPARK`. ⏎ ID chiến dịch quảng cáo. |
| ↳↳↳ catalog_id | string | Returned only when `material_type` is `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL`. ⏎ ID danh mục sản phẩm. |
| ↳↳ metrics | object | Metric data. ⏎ The following metrics will be returned alongside the metrics you specify via `metrics` in the request based on `material_type`: • When `material_type` is `SPC_VIDEO`: `is_removed_from_spc`, `video_id` and `file_name`.  • When `material_type` is `SPC_AD_TEXT`: `is_removed_from_spc`, and `ad_text`. • When `material_type` is `SPC_SPARK`:`is_removed_from_spc`, `tiktok_item_id`, `identity_id` and `tiktok_name`. • When `material_type` is `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL`: `catalog_name`, `catalog_create_time`, and `catalog_modify_time`. |
| ↳↳↳ {metric_name} | string | Returned metrics, which are determined by the `metrics` field specified in your request. ⏎ **Note**: If your metrics include `video_resolution`, its data type is object. |
| ↳↳↳ is_removed_from_spc | string | Returned only when `material_type` is `SPC_VIDEO`, `SPC_AD_TEXT`, or `SPC_SPARK`. ⏎ Liệu material is removed from the Smart+ ads. ⏎ Các giá trị enum hỗ trợ: ⏎ • `"1"`: true. • `"0"`: false. |
| ↳↳↳ video_id | string | Returned only when `material_type` is `SPC_VIDEO`. ⏎ Video ID. |
| ↳↳↳ file_name | string | Returned only when `material_type` is`SPC_VIDEO`. ⏎ Video name. |
| ↳↳↳ ad_text | string | Returned only when `material_type` is `SPC_AD_TEXT`. ⏎ Ad text. |
| ↳↳↳ identity_id | string | Returned only when `material_type` is `SPC_SPARK`. ⏎ Identity ID. |
| ↳↳↳ tiktok_item_id | string | Returned only when `material_type` is `SPC_SPARK`. ⏎ The ID of the TikTok post to be used as an ad (Spark Ad). |
| ↳↳↳ tiktok_name | string | Returned only when `material_type` is `SPC_SPARK`. ⏎ The username of the TikTok account. ⏎ **Note**: Currently,  Smart+ Campaigns support TikTok posts with `identity_type` as `AUTH_CODE` or `TT_USER`. For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ catalog_name | string | Returned only when `material_type` is `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL`. ⏎ The name of the catalog. |
| ↳↳↳ catalog_create_time | string | Returned only when `material_type` is `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL`. ⏎ The time when the catalog was created, in the format of `YYYY-MM-DD HH:MM:SS`(UTC+0). ⏎ Example: `2024-00-01 00:00:00`. |
| ↳↳↳ catalog_modify_time | string | Returned only when `material_type` is `SPC_CATALOG_VIDEO` or `SPC_CATALOG_CAROUSEL`. ⏎ The time when the catalog was last modified, in the format of `YYYY-MM-DD HH:MM:SS`(UTC+0). ⏎ Example: `2024-00-01 00:00:00`. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
#### Run a report on videos
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
                "metrics": {
                    "video_id": "{{video_id}}",
                    "is_removed_from_spc": "0",
                    "file_name": "{{file_name}}",
                    "impressions": "0",
                    "spend": "0.0"
                },
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "material_id": "{{material_id}}"
                }
            }
        ],
        "page_info": {
            "page_size": 100,
            "total_page": 1,
            "page": 1,
            "total_number": 1
        }
    }
}
```

#### Run a report on ad texts
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
                "metrics": {
                    "ad_text": "{{ad_text}}",
                    "is_removed_from_spc": "0",
                    "spend": "0.0",
                    "impressions": "0"
                },
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "ad_text": "{{ad_text}}",
                    "is_removed_from_spc": "0",
                    "spend": "0.0",
                    "impressions": "0"
                },
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "material_id": "{{material_id}}"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "total_page": 1,
            "page_size": 100,
            "total_number": 2
        }
    }
}
```
#### Run a report on Spark Ad posts
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "page": 1,
            "total_page": 1,
            "total_number": 4,
            "page_size": 100
        },
        "list": [
            {
                "metrics": {
                    "spend": "0.0",
                    "is_removed_from_spc": "0",
                    "identity_id": "{{identity_id}}",
                    "tiktok_name": "{{tiktok_name}}",
                    "tiktok_item_id": "{{tiktok_item_id}}",
                    "impressions": "0"
                },
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            ...,
            {
                "metrics": {
                    "spend": "0.0",
                    "is_removed_from_spc": "0",
                    "identity_id": "{{identity_id}}",
                    "tiktok_name": "{{tiktok_name}}",
                    "tiktok_item_id": "{{tiktok_item_id}}",
                    "impressions": "0"
                },
                "dimensions": {
                    "campaign_id": "{{campaign_id}}",
                    "material_id": "{{material_id}}"
                }
            }
        ]
    }
}
```
#### Run a report on catalog videos
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "page_size": 100,
            "total_number": 1,
            "page": 1,
            "total_page": 1
        },
        "list": [
            {
                "dimensions": {
                    "catalog_id": "{{catalog_id}}",
                    "campaign_id": "{{campaign_id}}"
                },
                "metrics": {
                    "catalog_name": "{{catalog_name}}",
                    "catalog_create_time": "{{catalog_create_time}}",
                    "impressions": "0",
                    "spend": "0.000",
                    "catalog_modify_time": "{{catalog_modify_time}}"
                }
            }
        ]
    }
}
```
#### Run a report on catalog carousel
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
                    "catalog_id": "{{catalog_id}}",
                    "campaign_id": "{{campaign_id}}"
                },
                "metrics": {
                    "spend": "0.000",
                    "impressions": "0",
                    "catalog_modify_time": "{{catalog_modify_time}}",
                    "catalog_create_time": "{{catalog_create_time}}",
                    "catalog_name": "{{catalog_name}}"
                }
            }
        ],
        "page_info": {
            "total_number": 1,
            "total_page": 1,
            "page_size": 100,
            "page": 1
        }
    }
}
```

---

<a id="doc-1776461365424129"></a>
<!-- doc_id: 1776461365424129 -->
<!-- doc_id: 1776461365424129 -->
# (Sắp ngừng hỗ trợ) Các chỉ số trong báo cáo chiến dịch Smart+ phiên bản cũ (Metrics in Legacy Smart+ Campaign reports)
> Đường dẫn: API Reference > (To be deprecated) Legacy Smart+ > (To be deprecated) Run a Legacy Smart+ Campaign report > (To be deprecated) Metrics in Legacy Smart+ Campaign reports
Dưới đây là các chỉ số được hỗ trợ cho báo cáo chiến dịch Smart+.

## Basic data

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| spend | string | Tổng chi phí | Ước tính tổng số tiền bạn đã chi tiêu cho chiến dịch, nhóm quảng cáo hoặc mẫu quảng cáo trong lịch trình phân phối. |
| cpc | string | CPC (Đích đến) | Số tiền trung bình bạn phải trả cho một lượt nhấp đến một đích đến được chỉ định. |
| cpm | string | CPM | Số tiền trung bình bạn đã chi tiêu cho mỗi 1.000 lượt hiển thị. |
| impressions | string | Lượt hiển thị | Số lần quảng cáo của bạn xuất hiện trên màn hình. |
| clicks | string | Lượt nhấp (Đích đến) | Số lượt nhấp từ quảng cáo của bạn dẫn đến các đích đến được chỉ định. |
| ctr | string | CTR (Đích đến) | Tỷ lệ phần trăm số lần người dùng nhấp đến đích đến được chỉ định sau khi xem quảng cáo của bạn. |
| conversion | string | Lượt chuyển đổi | Số lần quảng cáo đạt được kết quả, dựa trên mục tiêu và cài đặt bạn đã chọn. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_conversion | string | CPA | Số tiền trung bình bạn đã chi tiêu cho một lượt chuyển đổi. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| conversion_rate | string | CVR (Lượt nhấp) | Tỷ lệ phần trăm lượt chuyển đổi từ tất cả các lượt nhấp vào quảng cáo của bạn. Chỉ số này sẽ sớm bị loại bỏ. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| conversion_rate_v2 | string | CVR (Lượt hiển thị) | Tỷ lệ phần trăm lượt chuyển đổi từ tất cả các lượt hiển thị quảng cáo của bạn. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| real_time_conversion | string | Real-time Lượt chuyển đổi | Số lần quảng cáo đạt được kết quả dựa trên mục tiêu và cài đặt bạn đã chọn. ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| real_time_cost_per_conversion | string | Real-time CPA | Số tiền trung bình bạn đã chi tiêu cho một lượt chuyển đổi. ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| real_time_conversion_rate | string | Real-time CVR (Lượt nhấp) | The percentage of conversions from all clicks on your ads. This metric will be removed soon . ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| real_time_conversion_rate_v2 | string | Real-time CVR (Lượt hiển thị) | Tỷ lệ phần trăm lượt chuyển đổi từ tất cả các lượt hiển thị quảng cáo của bạn. ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| secondary_goal_result | string | Secondary goal result | The number of times your ad achieved an outcome, based on the secondary goal you selected. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_secondary_goal_result | string | Cost per secondary goal result | The average cost for each secondary goal result from your adverts. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| secondary_goal_result_rate | string | Secondary goal result rate | The percentage of secondary goal results you achieved out of all of the installs of your adverts. As one campaign may have a number of different secondary goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| skan_conversion | string | Lượt chuyển đổi (SKAN) | Số lần quảng cáo đạt được kết quả dựa trên mục tiêu và cài đặt bạn đã chọn. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_conversion | string | CPA (SKAN) | Số tiền trung bình bạn đã chi tiêu cho một lượt chuyển đổi. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_conversion_rate | string | CVR (SKAN, clicks) | The percentage of conversions from all clicks of your ads. Data may be incomplete due to SKAdNetwork (SKAN) limitations. This metric will be removed soon. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. ⏎ **Note**: ⏎ Starting late October, 2023, the calculation logic for this metric will be updated to be impression-based (the same as `skan_conversion_rate_v2`). To ensure a smooth API integration and avoid disruptions caused by the change in calculation logic, we recommend you switch to using the impression-based metric `skan_conversion_rate_v2` as soon as possible. |
| skan_conversion_rate_v2 | string | CVR (SKAN, impressions) | Tỷ lệ phần trăm lượt chuyển đổi từ tất cả các lượt hiển thị quảng cáo của bạn. Data may be incomplete due to SKAdNetwork (SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |

## Video play

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| video_play_actions | string | Video Views | The number of times someone started playing your video. Replays will not be counted. |
| video_watched_2s | string | 2-second video Views | The number of times your video played for at least 2 seconds. Replays will not be counted. |
| video_watched_6s | string | 6-second video Views | The number of times your video played for at least 6 seconds, or played in full. Replays will not be counted. |
| video_views_p100 | string | Video Views at 100% | The number of times your video was played at 100% of its length. Replays will not be counted. |
| video_views_p75 | string | Video Views at 75% | The number of times your video was played at 75% of its duration. Replays will not be counted. |
| video_views_p50 | string | Video Views at 50% | The number of times your video was played at 50% of its duration. Replays will not be counted. Data from Pangle is currently not supported. |
| video_views_p25 | string | Video Views at 25% | The number of times your video was played at 25% of its duration. Replays will not be counted. Data from Pangle is currently not supported. |
| average_video_play | string | Average Watch Time per Video View | The average time your video was played per single video view, including any time spent replaying the video. |

## Interaction

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| follows | string | Paid followers | The number of new followers that were gained within 1 day of a user seeing a paid ad. ⏎ This metric is only for Spark Ads. |
| likes | string | Paid likes | The number of likes your video creative received within 1 day of a user seeing a paid ad. |
| comments | string | Paid comments | The number of comments your video creative received within 1 day of a user seeing a paid ad. |
| shares | string | Paid shares | The number of times your video creative was shared within 1 day of a user seeing a paid ad. |
| profile_visits | string | Paid profile visits | The number of profile visits the paid ad drove during the campaign. ⏎ This metric is only for Spark Ads. |
| profile_visits_rate | string | Paid profile visit rate | The rate of profile visits per impression the paid ad drove during the campaign. ⏎ This metric is only for Spark Ads. |

## In-app event - Statistic Type: Every

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| total_registration | string | Total registration | The number of registration events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_registration | string | Cost per registration | The average cost of each registration event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_purchase | string | Total purchase | The number of purchase events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_purchase | string | Cost per purchase | The average cost for each purchase event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_total_purchase | string | Value per purchase | The avarage value returned from each purchase event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_purchase_value | string | Total purchase value | The total value returned from all purchase events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_active_pay_roas | string | Purchase ROAS | The total return on ad spend (ROAS) from purchase events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_app_event_add_to_cart | string | Total add-to-cart | The number of add to cart events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_app_event_add_to_cart | string | Cost per add-to-cart | The average cost for each ad to cart event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_total_app_event_add_to_cart | string | Value per add-to-cart | The average value returned from each add-to-cart event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_app_event_add_to_cart_value | string | Total add-to-cart value | The total value returned from all add to cart events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_checkout | string | Total checkout | The number of checkout events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_checkout | string | Cost per checkout | The average cost for each checkout event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_checkout | string | Value per checkout | The average value returned from each checkout event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_checkout_value | string | Total checkout value | The total value returned from all checkout events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_view_content | string | Total view content | The number of view content events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_view_content | string | Cost per view content | The average cost for each view content. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_total_view_content | string | Value per view content | The average value returned from each view content. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_view_content_value | string | Total view view content | The total value returned from all view content events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_next_day_open | string | Total day 1 retention | The number of day 2 retention events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_next_day_open | string | Cost per day 1 retention | The average cost for each day 2 retention events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_launch_app | string | Total launch app | The total of launch app events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_launch_app | string | Cost per launch app | The average cost for each launch app event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_complete_tutorial | string | Total complete tutorial | The number of complete tutorial events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_complete_tutorial | string | Cost per complete tutorial | The average cost for each complete tutorial event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_total_complete_tutorial | string | Value per complete tutorial | The average value returned from each complete tutorial event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_complete_tutorial_value | string | Total complete tutorial value | The total value returned from all complete tutorial events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_achieve_level | string | Total achieve level | The number of achieve level events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_total_achieve_level | string | Cost per achieve level | The average cost for each achieve level event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| value_per_total_achieve_level | string | Value per achieve level | The average value returned from each achieve level event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| total_achieve_level_value | string | Total achieve level value | The total value returned from all achieve level events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |

## In-app event - Statistic Type: Once

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| real_time_app_install | string | Real-time app installs | The number of app install events that are attributed to your ads. ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| real_time_app_install_cost | string | Cost per real-time app install | The average cost for each app install event. ⏎ Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| app_install | string | App install | The number of app install events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_app_install | string | Cost per app install | The average cost for each app install event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| registration | string | Unique registration | The number of unique registration events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_registration | string | Cost per unique registration | The average cost for each registration that is attributed to your ad. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| registration_rate | string | Unique registration rate (%) | The percentage of registration events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| purchase | string | Unique purchase | The number of unique purchase events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_purchase | string | Cost per unique purchase | The average cost for each unique purchase that is attributed to your ad. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| purchase_rate | string | Unique purchase rate (%) | The percentage of purchase events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| app_event_add_to_cart | string | Unique add-to-cart | The number of unique add to cart events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_app_event_add_to_cart | string | Cost per unique add-to-cart | The average cost of each unique add to cart event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| app_event_add_to_cart_rate | string | Unique add-to-cart rate (%) | The percentage of unique add to cart events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| checkout | string | Unique checkout | The number of unique checkout events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_checkout | string | Cost per unique checkout | The average cost of each unique checkout event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| checkout_rate | string | Unique checkout rate (%) | The percentage of unique checkout events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| view_content | string | Unique view content | The number of unique view content events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_view_content | string | Cost per unique view content | The average cost of each unique view content event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| view_content_rate | string | Unique view content rate (%) | The percentage of unique checkout events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| next_day_open | string | Day 1 retention | The number of unique day 2 retention events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_next_day_open | string | Cost per unique day 1 retention | The average cost of each unique day 2 retention event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| next_day_open_rate | string | Unique day 1 retention rate (%) | The percentage of unique day 2 retention events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| launch_app | string | Unique launch app | The number of unique launch app events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_launch_app | string | Cost per unique launch app | The average cost of each unique launch app event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| launch_app_rate | string | Unique launch app rate (%) | The percentage of unique launch app events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| complete_tutorial | string | Unique complete tutorial | The number of unique complete tutorial events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_complete_tutorial | string | Cost per unique complete tutorial | The average cost of each unique complete tutorial event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| complete_tutorial_rate | string | Unique complete tutorial rate (%) | The percentage of unique complete tutorial events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| achieve_level | string | Unique achieve level | The number of unique achieve level events that are attributed to your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_achieve_level | string | Cost per unique achieve level | The average cost of each unique achieve level event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| achieve_level_rate | string | Unique achieve level rate (%) | The percentage of unique achieve level events out of all app install events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |

## In-app event (SKAN)

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| skan_app_install | string | App Install (SKAN) | The number of unique app install events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_app_install | string | Cost per App Install (SKAN) | The average cost of each unique app install event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_app_install_withheld | string | App installs (SKAN Privacy Withheld) | The number of unique app install events that are attributed to your ads, with withheld values due to Apple's privacy threshold. Data may be incomplete due to SKAdNetwork (SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_registration | string | Unique registration (SKAN) | The number of unique registration events that are attributed to your ads. Data may be incomplete due to SKAdNetwork (SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_registration | string | Cost per unique registration (SKAN) | The average cost of each unique registration event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_registration_rate | string | Unique registration rate (SKAN) | The percentage of unique registration events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_registration | string | Total registration (SKAN) | The number of registration events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_registration | string | Cost per registration (SKAN) | The average cost for each registration event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_purchase | string | Unique Purchase (SKAN) | The number of unique purchase events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_purchase | string | Cost per unique purchase (SKAN) | The average cost of each unique purchase event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_purchase_rate | string | Unique purchase rate (SKAN) | The percentage of unique purchase events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_purchase | string | Total purchase (SKAN) | The number of purchase events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_purchase | string | Cost per purchase (SKAN) | The average cost for each purchase event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_purchase_value | string | Total Purchase Value (SKAN) | The total value returned from all purchase events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_repetitive_active_pay_roas | string | Purchase ROAS (SKAN) | The total return on ad spend (ROAS) from purchase events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_add_to_cart | string | Unique add-to-cart (SKAN) | The number of unique add to cart events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_add_to_cart | string | Cost per unique add-to-cart (SKAN) | The average cost of each unique add to cart event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_add_to_cart_rate | string | Unique add-to-cart rate (SKAN) | The percentage of unique checkout events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_add_to_cart | string | Total add-to-cart (SKAN) | The number of add to cart events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_add_to_cart | string | Cost per add-to-cart (SKAN) | The average cost for each add to cart event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_add_to_cart_value | string | Total add-to-cart value (SKAN) | The total value returned from all add to cart events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_checkout | string | Unique checkout (SKAN) | The number of unique checkout events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_checkout | string | Cost per unique checkout (SKAN) | The average cost of each unique checkout event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_checkout_rate | string | Unique checkout rate (SKAN) | The percentage of unique checkout events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_checkout | string | Total checkout (SKAN) | The number of checkout events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_checkout | string | Cost per checkout (SKAN) | The average cost for each checkout event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_checkout_value | string | Total checkout value (SKAN) | The total value returned from all checkout events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_view_content | string | Unique view content (SKAN) | The number of unique view content events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_view_content | string | Cost per unique view content (SKAN) | The average cost of each unique view content event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_view_content_rate | string | Unique view content rate (SKAN) | The percentage of unique view content events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_view_content | string | Total view content (SKAN) | The number of view content events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_view_content | string | Cost per view content (SKAN) | The average cost for each view content event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_launch_app | string | Unique launch app (SKAN) | The number of unique launch app events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_launch_app | string | Cost per unique launch app (SKAN) | The average cost of each unique launch app event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_launch_app_rate | string | Unique launch app rate (SKAN) | The percentage of unique launch app events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_launch_app | string | Total launch app (SKAN) | The number of launch app events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_launch_app | string | Cost per launch app (SKAN) | The average cost for each launch app event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_complete_tutorial | string | Unique complete tutorial (SKAN) | The number of unique complete tutorial events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_complete_tutorial | string | Cost per unique complete tutorial (SKAN) | The average cost of each unique complete tutorial event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_complete_tutorial_rate | string | Unique complete tutorial rate (SKAN) | The percentage of unique complete tutorial events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_complete_tutorial | string | Total complete tutorial (SKAN) | The number of complete tutorial events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_complete_tutorial | string | Cost per complete tutorial (SKAN) | The average cost for each complete tutorial event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_complete_tutorial_value | string | Total complete tutorial value (SKAN) | The total value returned from all complete tutorial events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_achieve_level | string | Unique achieve level (SKAN) | The number of unique achieve level events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_achieve_level | string | Cost per unique achieve level (SKAN) | The average cost of each unique achieve level event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_achieve_level_rate | string | Unique achieve level rate (SKAN) | The percentage of unique achieve level events out of all app install events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_achieve_level | string | Total achieve level (SKAN) | The number of achieve level events that are attributed to your ads. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_cost_per_total_achieve_level | string | Cost per achieve level (SKAN) | The average cost for each achieve level event. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |
| skan_total_achieve_level_value | string | Total achieve level value (SKAN) | The total value returned from all achieve level events. Data may be incomplete due to SKAdNetwork(SKAN) limitations. ⏎ The total count is based on when the events are returned through the SKAdNetwork API. There may be a delay between the actual conversion time and when the conversion is reported. |

## Page event

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| total_landing_page_view | string | Total landing page view | The number of landing page view events from your ads. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| cost_per_landing_page_view | string | Cost per landing page view | The average cost of each landing page view event. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |
| landing_page_view_rate | string | Landing page view rate | The percentage of click events that are landing page view events. ⏎ Tổng số được tính toán dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra. |

## Date

| Metric (Chỉ số) | Type (Kiểu dữ liệu) | Mô tả chi tiết | Chi tiết bổ sung |
|---|---|---|---|
| create_time | string | Created on | Time at which the ad was created. Example: `2022-09-06T01:05:12Z` |
| modify_time | string | Modified on | Time at which the ad was modified. Example: `2022-09-06T01:05:12Z` |

## Video Material Details

| Metric | Type | Description |
|---|---|---|
| video_duration | string | Video Duration |
| video_resolution | object | Video Resolution |
| ↳ height | integer | Height |
| ↳ width | integer | Width |
| video_format | string | Video Format |
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ phiên bản cũ (sắp ngừng hỗ trợ)**:

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

