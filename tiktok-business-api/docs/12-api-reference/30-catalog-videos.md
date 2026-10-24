# Video Catalog

> Phân hệ: apiref:Catalog Videos.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Catalog Videos (#doc-1803654722508866)](#doc-1803654722508866)
- [2. Upload catalog videos via a file URL (#doc-1803655037415489)](#doc-1803655037415489)
- [3. Get the catalog video handling log (#doc-1803655061642242)](#doc-1803655061642242)
- [4. Get the uploaded catalog videos within a catalog (#doc-1803655082498050)](#doc-1803655082498050)
- [5. Delete uploaded catalog videos (#doc-1803655103069185)](#doc-1803655103069185)

---

<a id="doc-1803654722508866"></a>
<!-- doc_id: 1803654722508866 -->
<!-- doc_id: 1803654722508866 -->
# Catalog Videos
> Đường dẫn: API Reference > Catalog Videos
> **Important:** 
> By using Catalog API endpoints, you agree to the [Product Catalog Terms](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) and certify that you are abiding by the [TikTok Advertising Policies](https://ads.tiktok.com/help/article?aid=6685586866860720134). Please review these policies and ensure that the items you upload to your catalog don't breach them.

A catalog is an asset that allows you to store information about the products you want to promote on TikTok. Using a catalog is a great solution for anyone who is looking for an efficient way to create and manage ads that feature a variety of products, like an online retailer. Catalog Videos API enables you to upload, retrieve and delete catalog videos within your catalog.

To learn more about how to manage uploaded catalog videos to be used in VSA for Catalog, see [Upload catalog videos to associate with catalog products](../09-marketing-api/catalog.md#doc-1803654904260674).

This group consists of the following endpoints:
* [Upload catalog videos via a file URL](30-catalog-videos.md#doc-1803655037415489)
* [Get the catalog video handling log](30-catalog-videos.md#doc-1803655061642242)
* [Get the uploaded catalog videos within a catalog](30-catalog-videos.md#doc-1803655082498050)
* [Delete uploaded catalog videos](30-catalog-videos.md#doc-1803655103069185)

---

<a id="doc-1803655037415489"></a>
<!-- doc_id: 1803655037415489 -->
<!-- doc_id: 1803655037415489 -->
# Upload catalog videos via a file URL
> Đường dẫn: API Reference > Catalog Videos > Upload catalog videos via a file URL
Sử dụng endpoint này để tải lên catalog videos via a file URL. Videos will be added to the E-commerce catalog through an asynchronous task. The response will include a `feed_log_id` representing the task processing ID. You can use this ID to check the processing status and final results via the [/catalog/video/log/](30-catalog-videos.md#doc-1803655061642242) endpoint.

**Currently, the API only accepts CSV files containing video URLs.** The CSV template for catalog videos is available at [catalog_video_template](https://bytedance.sg.larkoffice.com/sheets/PcBjsyYxahFGMqteR3jl3lv8gKh).

>  **Note:** 
>  The endpoint can only handle one file task at the same time, and new tasks will fail if the current file task is not complete. Wait for the current task to complete before sending the next task. 

## Điều kiện tiên quyết trước khi bắt đầu
You need to have an existing E-commerce catalog with products available for ad creation.

If you don't have such an E-commerce catalog yet, follow the instructions in [Upload products to different catalog types via JSON schema](../09-marketing-api/catalog.md#doc-1766862002851842) to create one.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/video/file/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br><br>You need to have Catalog Management permission for the catalog. To obtain the catalogs for which you have Catalog Management permission, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). Set `asset_type` to `CATALOG` to retrieve `asset_id` values with `catalog_role` as `ADMIN`. |
| file_url ***(Bắt buộc)*** | string | The download URL of the CSV file. <br><br>The CSV catalog video template is accessible via [catalog_video_template](https://bytedance.sg.larkoffice.com/sheets/PcBjsyYxahFGMqteR3jl3lv8gKh). <br><br>To find a detailed description of each catalog video parameter, see <a href="#item-link-Catalog video parameters">Catalog video parameters</a>. |
| advertiser_ids | string[] | The IDs of the ad accounts that you want to sync the videos to. <br>Once synced, the videos will be available in the creative library of those ad accounts. If you don't want to sync the catalog videos to any ad accounts, do not pass this field. <br><br>Kích thước tối đa: 100. <br><br>The ad account and the catalog (`catalog_id`) must be within the same Business Center (`bc_id`) and you need to have Admin or Toán tử điều kiện permission for the ad account. Ineligible ad accounts will be ignored. To obtain the ad accounts for which you have Admin or Toán tử điều kiện permission, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). Set `asset_type` to `ADVERTISER` to retrieve `asset_id` values with `advertiser_role` as `ADMIN` or `Toán tử điều kiện`. |

### Catalog video parameters
The following table provides the detailed description of each parameter that you can specify for your catalog video in the CSV template via `file_url`.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| video_name ***(Bắt buộc)*** | string | The name of the video.<br><br>Giới hạn độ dài: 500 characters. |
| video_link ***(Bắt buộc)*** | string | The URL of the video file. <br><br>File size limit: 100 MB.<ul><li>For TikTok placement:<ul><li>Aspect ratio requirements: Horizontal(16:9) / Square(1:1) / Vertical(9: 16)</li><li>Resolution: Horizontal (minimum 960*540) / Square (minimum 640*640) / Vertical (minimum 540*960) </li><li>Bitrate: > 516.00 kbps</li><li>Duration: 5-60s</li><li>Safe zone: From left: 44 px, From right: 140px, From top: 130px, From bottom:483-484px </li></ul></li><li>For Global App Bundle and Pangle placements:<ul><li>Recommended duration: 5-60s</li></ul></li></ul><br>Example: https://www.tiktok.com/tiktok_t_shirt.mp4 |
| sku_id_list ***(Bắt buộc)*** | string[] | The SKU ID list of E-commerce catalog products to associate the video (`video_link`) with. <br><br>Kích thước tối đa: 20.<br><br>To specify multiple SKU IDs, separate them with commas. <br><br>Example: `SKU_ID_1,SKU_ID_2,SKU_ID_3,SKU_ID_4`. <br><br>To obtain E-commerce catalog products that can be used in ads, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). If the returned `ad_creation_eligible` for the product is `AVAILABLE`, you can use the product in ads. |
| category | string | The product category for the video.<br><br>Giới hạn độ dài: 500 characters. If the value exceeds the limit, the value will be overwritten with null. <br><br>Example: `Apparel & Accessories> Clothing> Shirts`. |
| brand | string | The brand name for the video.<br><br>Giới hạn độ dài: 500 characters. If the value exceeds the limit, the value will be overwritten with null. <br><br>Example: TikTok. |
| creator | string | The creator of the video. <br><br>Giới hạn độ dài: 500 characters. If the value exceeds the limit, the value will be overwritten with null.<br><br> Example: TikTok Creator. |
| video_type | string | The type of the video. <br><br> Giới hạn độ dài: 500 characters. If the value exceeds the limit, the value will be overwritten with null. <br><br> Example: Promotional video. |
| description | string | A short description of the video.<br><br> Giới hạn độ dài: 500 characters. If the value exceeds the limit, the value will be overwritten with null. |
| landing_page_url | string | URL of the landing page where you can view and purchase the products that are associated with the video.<br><br> Example: https://www.landingpage.com |
| custom_label_0 | string | Additional information about the video.<br><br>No length limit. |
| custom_label_1 | string | Additional information about the video.<br><br> No length limit. |
| custom_label_2 | string | Additional information about the video. <br><br>No length limit. |
| custom_label_3 | string | Additional information about the video.<br><br>No length limit. |
| custom_label_4 | string | Additional information about the video. <br><br> No length limit. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/video/file/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "advertiser_ids": ["{{advertiser_id}}"],
    "file_url": "{{file_url}}"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| feed_log_id| string | Catalog video handling log ID. <br><br>To check the processing status and final results of the upload, use [/catalog/video/log/](30-catalog-videos.md#doc-1803655061642242). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "feed_log_id": "{{feed_log_id}}"
    }
}
```

---

<a id="doc-1803655061642242"></a>
<!-- doc_id: 1803655061642242 -->
<!-- doc_id: 1803655061642242 -->
# Get the catalog video handling log
> Đường dẫn: API Reference > Catalog Videos > Get the catalog video handling log
Sử dụng endpoint này để kiểm tra if the catalog videos are uploaded successfully, and what to do if the upload fails.

## Điều kiện tiên quyết trước khi bắt đầu
You need to have the log ID of the catalog video handling task for which you want to check the results. To upload catalog videos and obtain the log ID, use [/catalog/video/file/](30-catalog-videos.md#doc-1803655037415489). 

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/video/log/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br><br>You need to have Catalog Management or Ad Promotion permission for the catalog. To obtain the catalogs for which you have Catalog Management or Ad Promotion permission, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). Set `asset_type` to `CATALOG` to retrieve `asset_id` values with `catalog_role` as `ADMIN` or `AD_PROMOTE`. |
| feed_log_id ***(Bắt buộc)*** | string | Catalog video handling log ID.  <br><br> To upload catalog videos and obtain the log ID, use [/catalog/video/file/](30-catalog-videos.md#doc-1803655037415489). |
| language | string | Supported languages. <br><br>Các giá trị enum hỗ trợ: <ul><li>`en`: English</li><li>`zh-CN`: Chinese</li><li>`ja-JP`: Japanese</li><li>`de`: German</li><li>`es`: Spanish</li><li>`fr`: French</li><li>`hi-IN`: Hindi (India)</li><li>`id`: Indonesian</li><li>`it`: Italian</li><li>`ko`: Korean</li><li>`ms`: Malay</li><li> `ru`: Russian</li><li>`th`: Thai</li><li>`tr`: Turkish</li><li>`vi`: Vietnamese</li></ul><br>Giá trị mặc định: `en`.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/video/log/' \
--header 'Access-Token: {{Access-Token}}' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "feed_log_id": "{{feed_log_id}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| video_feed_log | object | Video handling results. |
##| catalog_id | string | ID danh mục sản phẩm. |
##| feed_id | string | Feed ID. |
##| add_count | number | Total number of new videos. |
##| update_count | number | Total number of videos modified.<br><br><p><span style="color:darkred"><b>Note</b></span>: The value of this field will always be 0. |
##| delete_count | number | Total number of videos deleted. |
##| error_count | number | Number of errors. |
##| warn_count| number | Number of warnings. |
##| process_status | string | Processing status. <br><br>Các giá trị enum hỗ trợ: `PROCESSING`, `SUCCESS`,`FAILED`, `WAITING`. |
##| start_time | string | Start time of the video handling task, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br> Example: 2024-01-01 00:00:00. |
##| end_time | string | End time of the video handling task, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br>Example: 2024-01-01 00:00:00. |
#| feed_log_data | object | Detailed processing information. |
##| download_path | object | File download address with all error and warning messages. The key is language, and the value is file address.|
##| error_affected_videos | object[] | Error message. |
###| affected_video_count | number | Number of videos affected.  |
###| affected_video_item_list | object[] | List of affected videos, showing only the first five items. |
####| index | number | Index that identifies the position of the video among the videos you uploaded. <br><br>For example, an index of `2` represents the first video you uploaded through [/catalog/video/file/](30-catalog-videos.md#doc-1803655037415489), listed in the second row of the CSV file after the header row. |
####| video_name | string | The name of the video. |
####| video_link | string | The URL of the video file. <br><br>Example: https://www.tiktok.com/tiktok_t_shirt.mp4 |
####| sku_id_list | string | The SKU ID list of E-commerce catalog products to associate the video (`video_link`) with. <br><br>Example: `"SKU_ID_1, SKU_ID_2"`. |
####| description | string | A short description of the video. |
####| category | string | The product category for the video. <br><br>Example: Apparel & Accessories> Clothing> Shirts. |
###| field | string | The field with issue. |
###| issue | string | Issue details. |
###| suggestion | string | Suggestions for solving the issue. |
##| warn_affected_videos | object[] | Warning message. |
###| affected_video_count | number | Number of products affected. |
###| affected_video_item_list | object[] | List of affected items, showing only the first five items. |
####| index | number | Index that identifies the position of the video among the videos you uploaded. <br><br>For example, an index of `2` represents the first video you uploaded through [/catalog/video/file/](30-catalog-videos.md#doc-1803655037415489), listed in the second row of the CSV file after the header row. |
####| video_name | string | The name of the video. |
####| video_link | string | The URL of the video file. <br><br>Example: https://www.tiktok.com/tiktok_t_shirt.mp4 |
####| sku_id_list | string | The SKU ID list of E-commerce catalog products to associate the video (`video_link`) with. <br><br>Example: `"SKU_ID_1, SKU_ID_2"`. |
####| description | string | A short description of the video. |
####| category | string | The product category for the video. <br><br>Example: Apparel & Accessories> Clothing> Shirts. |
###| field | string | The field with issue. |
###| issue | string | Issue details. |
###| suggestion | string | Suggestions for solving the issue. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_feed_log": {
            "update_mode": null,
            "process_status": "SUCCESS",
            "catalog_id": "{{catalog_id}}",
            "delete_count": 0,
            "feed_id": "{{feed_id}}",
            "start_time": "{{start_time}}",
            "error_count": 0,
            "feed_log_data": {
                "error_affected_videos": null,
                "download_path": {},
                "warn_affected_videos": null
            },
            "end_time": "{{end_time}}",
            "warn_count": 0,
            "add_count": 1,
            "update_count": 0
        }
    }
}
```

---

<a id="doc-1803655082498050"></a>
<!-- doc_id: 1803655082498050 -->
<!-- doc_id: 1803655082498050 -->
# Get the uploaded catalog videos within a catalog
> Đường dẫn: API Reference > Catalog Videos > Get the uploaded catalog videos within a catalog
Sử dụng endpoint này để truy xuất the list of uploaded catalog videos within an E-commerce catalog.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/video/get/ 

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br><br>You need to have Catalog Management or Ad Promotion permission for the catalog. To obtain the catalogs for which you have Catalog Management or Ad Promotion permission, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). Set `asset_type` to `CATALOG` to retrieve `asset_id` values with `catalog_role` as `ADMIN` or `AD_PROMOTE`. |
| catalog_video_ids | string[] | The ID list of catalog videos that you want to filter.<br><br>Kích thước tối đa: 50.<br><br><p><span style="color:darkred"><b>Note</b></span>: If you specify a value for `catalog_video_ids`, the pagination parameters `page` and `page_size` will be ignored. |
| page | integer | Current Số trang cần lấy dữ liệu. <br><br>Value range: ≥1. Giá trị mặc định: 1. <br><br><p><span style="color:darkred"><b>Note</b></span>: If you specify a value for `catalog_video_ids`, the pagination parameters `page` and `page_size` will be ignored. |
| page_size | integer | Page size. <br><br>Value range: 1-50. Giá trị mặc định: 10. <br><br><p><span style="color:darkred"><b>Note</b></span>: If you specify a value for `catalog_video_ids`, the pagination parameters `page` and `page_size` will be ignored. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/video/get/?bc_id={{bc_id}}&catalog_id={{catalog_id}}&page=1&page_size=50' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| videos | object[] | Danh sách video trong danh mục sản phẩm. |
##|catalog_video_id | string | The ID of the catalog video.<br><br>Example:  `1234567891234567891_1234567891234567891_12345678912345_12345678-a12b-34cd-ef56-7gh89i1j2k3l `. |
##| video_name| string | The name of the video. |
##| video_link | string | The URL of the video file. |
##| sku_id_list | string[] | The list of SKU IDs associated with the video. |
##| category | string | The product category for the video. |
##| brand | string | The brand name for the video. |
##| creator | string | The creator of the video. |
##| video_type | string | The type of the video. |
##| description | string | A short description of the video. |
##| landing_page_url | string | URL of the landing page where you can view and purchase the products that are associated with the video. |
##| custom_label_0 | string | Additional information about the video. |
##| custom_label_1 | string | Additional information about the video. |
##| custom_label_2 | string | Additional information about the video. |
##| custom_label_3 | string | Additional information about the video. |
##| custom_label_4 | string | Additional information about the video. |
##| video_id | string | The video ID generated after the video extraction is complete. |
##| video_signature | string | The MD5 hash of the video. <br><br>Example: `123abcdefg4a56e789012c3cefa4d567`. |
##| status | string | Video extraction status.<br><br> Các giá trị enum hỗ trợ: <ul><li>`PENDING`: Video extraction is in progress.</li><li>`SUCCESS`: Video extraction succeeded.</li><li> `FAILED`: Video extraction failed.</li></ul>|
##| create_time | string | The time when the video upload was completed, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br>Example: `2024-01-01 00:00:00`. <br><br><p><span style="color:darkred"><b>Note</b></span>: When `status` is `PENDING` or `FAILED`, the value of this field will be an empty string (`""`). |
##| active_status | string | The user-controlled activation status of the video.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ACTIVATED`: The video is activated and can be used for ad delivery.</li><li>`DEACTIVATED`: The video is deactivated and cannot be used for ad delivery. Deactivated videos may affect the delivery of associated ads in active campaigns.</li></ul>|
##| preview_url | string | Returned only when `status` is `SUCCESS`. <br><br>The video preview link, which is valid for six hours and needs to be re-acquired after expiration. |
#| page_info | object | Pagination information. |
##| page | integer | Current Số trang cần lấy dữ liệu. |
##| page_size | integer | Page size. |
##| total_number | integer | Tổng số kết quả tìm thấy. |
##| total_page | integer | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "videos": [
            {
                "video_id": "{{video_id}}",
                "preview_url": "{{preview_url}}",
                "video_type": "{{video_type}}",
                "landing_page_url": "",
                "create_time": "{{create_time}}",
                "active_status": "DEACTIVATED",
                "catalog_video_id": "{{catalog_video_id}}",
                "video_link": "{{video_link}}",
                "creator": "{{creator}}",
                "description": "",
                "status": "SUCCESS",
                "video_name": "{{video_name}}",
                "brand": "br10",
                "category": "{{category}}",
                "video_signature": "{{video_signature}}",
                "sku_id_list": [
                    "{{sku_id_1}}",
                    "{{sku_id_2}}",
                    "{{sku_id_3}}"
                ]
            },     
            {
                "video_id": "{{video_id}}",
                "preview_url": "{{preview_url}}",
                "video_type": "{{video_type}}",
                "landing_page_url": "",
                "create_time": "{{create_time}}",
                "active_status": "ACTIVATED",
                "catalog_video_id": "{{catalog_video_id}}",
                "video_link": "{{video_link}}",
                "creator": "{{creator}}",
                "description": "",
                "status": "SUCCESS",
                "video_name": "{{video_name}}",
                "brand": "{{brand}}",
                "category": "{{category}}",
                "video_signature": "{{video_signature}}",
                "sku_id_list": [
                    "{{sku_id_1}}",
                    "{{sku_id_2}}",
                    "{{sku_id_3}}",
                    "{{sku_id_4}}",
                    "{{sku_id_5}}"
                ]
            }
        ],
        "page_info": {
            "total_number": 2,
            "total_page": 1,
            "page": 1,
            "page_size": 50
        }
    }
}
```

---

<a id="doc-1803655103069185"></a>
<!-- doc_id: 1803655103069185 -->
<!-- doc_id: 1803655103069185 -->
# Delete uploaded catalog videos
> Đường dẫn: API Reference > Catalog Videos > Delete uploaded catalog videos
Sử dụng endpoint này để xóa uploaded catalog videos from an E-commerce catalog.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/video/delete/ 

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br><br>You need to have Catalog Management permission for the catalog. To obtain the catalogs for which you have Catalog Management permission, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). Set `asset_type` to `CATALOG` to retrieve `asset_id` values with `catalog_role` as `ADMIN`. |
| catalog_video_ids ***(Bắt buộc)*** | string[] | The ID list of catalog videos that you want to delete. <br><br> Kích thước tối đa: 1. <br><br> To obtain the catalog videos within a catalog, use [/catalog/video/get/](30-catalog-videos.md#doc-1803655082498050).<br><br><p><span style="color:darkred"><b>Note</b></span>: If catalog videos have already been synced to the creative libraries of ad accounts, deleting those videos from the associated catalog will not remove them from the creative libraries. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/video/delete/ ' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "catalog_video_ids": ["{{catalog_video_id}}"]
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Video Catalog**:

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

