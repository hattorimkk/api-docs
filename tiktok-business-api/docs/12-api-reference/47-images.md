# Hình ảnh (Images)

> Phân hệ: apiref:Images.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Images (#doc-1739067422728193)](#doc-1739067422728193)
- [2. Upload an image (#doc-1739067433456642)](#doc-1739067433456642)
- [3. Update the name of an image (#doc-1740039806891010)](#doc-1740039806891010)
- [4. Get info about images (#doc-1740051721711618)](#doc-1740051721711618)
- [5. Search for images (#doc-1740052016789506)](#doc-1740052016789506)

---

<a id="doc-1739067422728193"></a>
<!-- doc_id: 1739067422728193 -->
<!-- doc_id: 1739067422728193 -->
# Images
> Đường dẫn: API Reference > Images
Images can be divided into three categories: images to be used as ads, images as video covers, and profile images. See [Upload videos, images and music-Upload images](../09-marketing-api/creatives.md#doc-1738963828459521) to learn about how to upload images for these three purposes.

Images are also a type of creative assets you can include in a creative portfolio via [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426), where you would need to specify the image via `image_id`.

This group consists of the following endpoints:
* [Upload an image](47-images.md#doc-1739067433456642)
* [Update the name of an image](47-images.md#doc-1740039806891010)
* [Get info about images](47-images.md#doc-1740051721711618)
* [Search for images](47-images.md#doc-1740052016789506)

---

<a id="doc-1739067433456642"></a>
<!-- doc_id: 1739067433456642 -->
<!-- doc_id: 1739067433456642 -->
# Upload an image
> Đường dẫn: API Reference > Images > Upload an image
Sử dụng endpoint này để tải lên pictures to the Asset Library and use the obtained image ID for creating ads. 

Request timeout for this endpoint is 10s, và tốc độ truyền tải phụ thuộc vào băng thông mạng. Vui lòng bảo đảm dung lượng tệp tin ở mức hợp lý.

To learn about the steps of creating single image ads, refer to [Create single image ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1777633230937090).

To learn about the steps of creating Carousel Ads, refer to [Create Carousel Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713).

# Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/file/image/ad/upload/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Use `multipart/form-data` when upload_type is `UPLOAD_BY_FILE`. ⏎ Use `application/json` when upload_type is `UPLOAD_BY_URL` or `UPLOAD_BY_FILE_ID`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| file_name | string | Image name. ⏎ Giới hạn độ dài: 1-100 characters. ⏎ The Giá trị mặc định is the file name. If the final filename has more than 100 chars, it will be cut off. ⏎ **Important**: Images under the same `advertiser_id` cannot have duplicated file names. You can call [/file/name/check/](44-files.md#doc-1759130033155073) to check Liệu file name has been used. ⏎ If you get an error about duplicated file names, please rename the files or append timestamps to the original file names ( for example, in the format of `_`) , and upload the images again. |
| upload_type ****(Bắt buộc)**** | string | Image upload method. ⏎ Giá trị mặc định: `UPLOAD_BY_FILE`. ⏎ Các giá trị enum hỗ trợ: `UPLOAD_BY_FILE`, `UPLOAD_BY_URL`, `UPLOAD_BY_FILE_ID`. |
| image_file **(Điều kiện)** | file | Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE`. ⏎ Image file. ⏎ Thông số khuyến nghị:  • File size: within 50 MB. • Resolution: The total pixel count of the image, which is obtained by multiplying the width and height, should not exceed 3,686,400 pixels (1440 x 2560). For example, a resolution of 2400 x 1256 pixels is within the supported range, while a resolution of 3600 x 1256 pixels will result in an error. ⏎ To learn about the recommended image resolution for a certain use case, refer to the section "Image resolution guidelines and use cases". • File type: JPG, JPEG, or PNG |
| image_signature **(Điều kiện)** | string | Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE`. ⏎ MD5 of the image (used for server verification). |
| image_url **(Điều kiện)** | url | Bắt buộc khi `upload_type` is `UPLOAD_BY_URL`. ⏎ Image url address. Example: http://xxx.xxx. |
| file_id**(Điều kiện)** | string | Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE_ID`. ⏎ The `file_id` of the image that you want to upload. ⏎ This field is for files that are uploaded to the file repository. ⏎ You can get `file_id` via the [Upload Files](44-files.md#doc-1737719988918274) endpoints. |
| pre_review_enabled | boolean | Có thực hiện create a pre-review task for the image and any associated materials, which may include ad text and the landing page URL. ⏎ A pre-review task is a process initiated to evaluate and assess the compliance and quality of your creatives before they are used to create ads, ensuring that they meet TikTok advertising guidelines and standards. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ When you set this field to `true`, you need to specify `pre_review_info` simultaneously, and the response will include the `pre_review_task_id`. |
| pre_review_info **(Điều kiện)** | object | Bắt buộc khi `pre_review_enabled` is set to `true`. ⏎ Additional details for the pre-review. |
| ↳ landing_page_url | string | Đường dẫn URL của trang đích sử dụng trong quảng cáo. |
| ↳ ad_text | string | Nội dung văn bản hiển thị trong quảng cáo. ⏎ An ad text is shown to your audience as part of your ad creative, to deliver the message you intend to communicate to them. ⏎ Ad text must be 1-100 characters long and cannot contain emoji. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. |
| ↳ location_codes **(Điều kiện)** | string[] | Bắt buộc khi `pre_review_info` is specified. ⏎ Danh sách mã quốc gia/khu vực bạn muốn nhắm mục tiêu. ⏎ Kích thước tối đa: 1. ⏎ Để xem danh sách giá trị enum, xem [List of values for `location_codes` or `location_code`](https://business-api.tiktok.com/portal/docs/upload-an-image-reference/v1.3#anchor-2-1). ⏎ Example: `US`. |
| ↳ is_ecommerce | boolean | Liệu creatives are intended for use in E-commerce ads, including [GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009058467842) and Catalog Ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |

## List of values for `location_codes` or `location_code`

The following table lists the enum values for the request parameter `location_codes` in [/creative/pre_review/task/create/](35-creative-pre-review.md#doc-1874110632584577), [/file/video/ad/upload/](71-video.md#doc-1737587322856449), and [/file/image/ad/upload/](47-images.md#doc-1739067433456642), and the response parameter `location_code` in [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082).

| Mã quốc gia (Location Code) | Tên quốc gia/vùng lãnh thổ |
|---|---|
| `AD` | Andorra |
| `AE` | United Arab Emirates |
| `AG` | Antigua and Barbuda |
| `AI` | Anguilla |
| `AL` | Albania |
| `AO` | Angola |
| `AR` | Argentina |
| `AT` | Austria |
| `AU` | Australia |
| `AW` | Aruba |
| `AZ` | Azerbaijan |
| `BA` | Bosnia and Herzegovina |
| `BB` | Barbados |
| `BD` | Bangladesh |
| `BE` | Belgium |
| `BG` | Bulgaria |
| `BH` | Bahrain |
| `BL` | Saint Barthélemy |
| `BM` | Bermuda |
| `BO` | Bolivia |
| `BQ` | Caribbean Netherlands |
| `BR` | Brazil |
| `BS` | The Bahamas |
| `BY` | Belarus |
| `BZ` | Belize |
| `CA` | Canada |
| `CD` | Democratic Republic of the Congo |
| `CH` | Switzerland |
| `CL` | Chile |
| `CO` | Colombia |
| `CR` | Costa Rica |
| `CU` | Cuba |
| `CV` | Cabo Verde |
| `CW` | Curaçao |
| `CY` | Cyprus |
| `CZ` | Czech Republic |
| `DE` | Germany |
| `DJ` | Djibouti |
| `DK` | Denmark |
| `DM` | Dominica |
| `DO` | Dominican Republic |
| `DZ` | Algeria |
| `EC` | Ecuador |
| `EE` | Estonia |
| `EG` | Egypt |
| `ER` | Eritrea |
| `ES` | Spain |
| `FI` | Finland |
| `FO` | Faroe Islands |
| `FR` | France |
| `GB` | United Kingdom |
| `GD` | Grenada |
| `GE` | Georgia |
| `GF` | French Guiana |
| `GG` | Bailiwick of Guernsey |
| `GI` | Gibraltar |
| `GL` | Greenland |
| `GN` | Guinea |
| `GP` | Guadeloupe |
| `GQ` | Equatorial Guinea |
| `GR` | Greece |
| `GT` | Guatemala |
| `GW` | Guinea-Bissau |
| `HK` | Hong Kong |
| `HN` | Honduras |
| `HR` | Croatia |
| `HT` | Haiti |
| `HU` | Hungary |
| `ID` | Indonesia |
| `IE` | Ireland |
| `IL` | Israel |
| `IM` | Isle of Man |
| `IN` | India |
| `IQ` | Iraq |
| `IS` | Iceland |
| `IT` | Italy |
| `JE` | Jersey |
| `JM` | Jamaica |
| `JO` | Jordan |
| `JP` | Japan |
| `KE` | Kenya |
| `KH` | Cambodia |
| `KM` | Comoros |
| `KN` | Saint Kitts and Nevis |
| `KR` | South Korea |
| `KW` | Kuwait |
| `KY` | Cayman Islands |
| `KZ` | Kazakhstan |
| `LB` | Lebanon |
| `LC` | Saint Lucia |
| `LI` | Liechtenstein |
| `LK` | Sri Lanka |
| `LT` | Lithuania |
| `LU` | Luxembourg |
| `LV` | Latvia |
| `LY` | Libya |
| `MA` | Morocco |
| `MC` | Monaco |
| `MD` | Moldova |
| `ME` | Montenegro |
| `MF` | Saint Martin |
| `MK` | North Macedonia |
| `MM` | Myanmar |
| `MO` | Macao |
| `MQ` | Martinique |
| `MR` | Mauritania |
| `MS` | Montserrat |
| `MT` | Malta |
| `MX` | Mexico |
| `MY` | Malaysia |
| `MZ` | Mozambique |
| `NG` | Nigeria |
| `NI` | Nicaragua |
| `NL` | Netherlands |
| `NO` | Norway |
| `NP` | Nepal |
| `NZ` | New Zealand |
| `OM` | Oman |
| `PA` | Panama |
| `PE` | Peru |
| `PF` | French Polynesia |
| `PH` | Philippines |
| `PK` | Pakistan |
| `PL` | Poland |
| `PM` | Saint Pierre and Miquelon |
| `PR` | Puerto Rico |
| `PS` | Palestine |
| `PT` | Portugal |
| `PY` | Paraguay |
| `QA` | Qatar |
| `RO` | Romania |
| `RS` | Serbia |
| `RU` | Russia |
| `SA` | Saudi Arabia |
| `SD` | Sudan |
| `SE` | Sweden |
| `SG` | Singapore |
| `SI` | Slovenia |
| `SJ` | Svalbard and Jan Mayen |
| `SK` | Slovakia |
| `SM` | San Marino |
| `SO` | Somalia |
| `SS` | South Sudan |
| `ST` | Sao Tome and Principe |
| `SV` | El Salvador |
| `SX` | Sint Maarten |
| `SY` | Syria |
| `TC` | Turks and Caicos Islands |
| `TD` | Chad |
| `TF` | French Southern and Antarctic Lands |
| `TH` | Thailand |
| `TN` | Tunisia |
| `TR` | Turkey |
| `TT` | Trinidad and Tobago |
| `TW` | Taiwan (Province of China) |
| `UA` | Ukraine |
| `US` | United States |
| `UY` | Uruguay |
| `UZ` | Uzbekistan |
| `VC` | Saint Vincent and the Grenadines |
| `VE` | Venezuela |
| `VG` | British Virgin Islands |
| `VI` | Virgin Islands of the United States |
| `VN` | Vietnam |
| `YE` | Yemen |
| `ZA` | South Africa |

## Image resolution guidelines and use cases
The following table outlines the recommended resolutions for a certain use case. Ensure that the image file you upload has the recommended resolution for the specific use case to avoid any issues with image condensation or expansion (with potential loss of clarity) when delivered in ads.

| Use case | Recommended resolution |
|---|---|
| Pangle single image ads | • 720 pixels (width) x 1280 pixels (height)  • 1200 pixels (width) x 628 pixels (height) • 640 pixels (width) x 640 pixels (height) • 640 pixels (width) x 100 pixels (height) •  600 pixels (width) x 500 pixels (height)  • 640 pixels (width) x 200 pixels (height) |
| Global App Bundle single image ads | • 720 pixels (width) x 1280 pixels (height)  • 1200 pixels (width) x 628 pixels (height) • 640 pixels (width) x 640 pixels (height) |
| Video cover (thumbnail) in TikTok single video ads | • 720 pixels (width) x 1280 pixels (height) • 1280 pixels (width) x 720 pixels (height) • 640 pixels (width) x 640 pixels (height) ⏎ **Note**: The video cover resolution must match the video resolution and meet these requirements: • Supported aspect ratios: 9:16, 16:9, or 1:1  • Resolution ranges per aspect ratio: • 9:16 aspect ratio: 960-3840 pixels (width) × 540-2160 pixels (height) • 16:9 aspect ratio: 960-3840 pixels (width) × 540-2160 pixels (height)  • 1:1 aspect ratio: 640-1280 pixels (width) × 640-1280 pixels (height) |

## Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/file/image/ad/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'advertiser_id="{{advertiser_id}}"' \
--form 'file_name="{{file_name}}"' \
--form 'image_file=@"{{image_file}}"' \
--form 'image_signature="{{image_signature}}"'
```

# Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ image_id | string | Image ID that is used to create ads. |
| ↳ material_id | string | Material ID. |
| ↳ is_carousel_usable | boolean | Liệu source of the image is valid for Carousel Ads. ⏎ **Note**:  • Due to the latency in writing the image data, this field might not be returned. In such situations, we recommend waiting for 10 seconds and then using the `image_id` returned from this endpoint with either [/file/image/ad/info/](47-images.md#doc-1740051721711618) or [/file/image/ad/search/](47-images.md#doc-1740052016789506) to retrieve the data. • To use an image in Carousel Ads, you need to ensure the value of this field is `true`, and the image meets the specifications requirements listed in [Create Carousel Ads-Steps-Create an ad](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713). |
| ↳ displayable | bool | Liệu it can be displayed on the platform. |
| ↳ height | number | Image height. |
| ↳ width | number | Image width. |
| ↳ format | string | Image Format. |
| ↳ image_url | string | Image URL, valid for an hour and needs to be re-acquired after expiration. |
| ↳ signature | string | MD5 of picture. |
| ↳ size | number | Image size in bytes. |
| ↳ file_name | string | Image name. |
| ↳ create_time | string | Thời gian tạo. UTC time. Format: 2020-06-10T07:39:14Z. ⏎ **Note**: Due to the latency in writing the image data, this field might not be returned. In such situations, we recommend waiting for 10 seconds and then using the `image_id` returned from this endpoint with either [/file/image/ad/info/](47-images.md#doc-1740051721711618) or [/file/image/ad/search/](47-images.md#doc-1740052016789506) to retrieve the data. |
| ↳ modify_time | string | Modification time. UTC time. Format: 2020-06-10T07:39:14Z. ⏎ **Note**: Due to the latency in writing the image data, this field might not be returned. In such situations, we recommend waiting for 10 seconds and then using the `image_id` returned from this endpoint with either [/file/image/ad/info/](47-images.md#doc-1740051721711618) or [/file/image/ad/search/](47-images.md#doc-1740052016789506) to retrieve the data. |
| ↳ pre_review_task_id | string | Returned only when `pre_review_enabled` in the request is set to `true`. ⏎ The ID of the pre-review task. ⏎ To obtain the result of the pre-review task, pass the value of this field to the `task_id` field in [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082). |

## Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "displayable": false,
        "width": 320,
        "signature": "{{signature}},
        "height": 640,
        "create_time": "{{create_time}}",
        "file_name": "{{file_name}}",
        "image_id": "{{image_id}}",
        "format": "jpeg",
        "modify_time": "{{modify_time}}",
        "image_url": "{{image_url}}",
        "is_carousel_usable": true,
        "material_id": "{{material_id}}",
        "size": 73398
    }
}
```

---

<a id="doc-1740039806891010"></a>
<!-- doc_id: 1740039806891010 -->
<!-- doc_id: 1740039806891010 -->
# Update the name of an image
> Đường dẫn: API Reference > Images > Update the name of an image
Sử dụng endpoint này để cập nhật name of an image.

 ## Comparing v1.2 and v1.3
 The following table outlines the differences between v1.2 and v1.3 endpoints. 
 
| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | /v1.2/file/image/ad/update/ | /v1.3/file/image/ad/update/ |
| Request parameter data type | `advertiser_id`: number | `advertiser_id`: string |

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/file/image/ad/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `multipart/form-data`,`application/json`. ⏎ Use `multipart/form-data` when the `upload_type` is `UPLOAD_BY_FILE`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| file_name  ****(Bắt buộc)**** | string | Image name. Giới hạn độ dài: 1 - 100 characters. If another image uses the same file name under the same `advertiser_id`, there will a millisecond timestamp added at the end. If the file name contains more than 100 characters, only the first 100 characters will be used. |
| image_id  ****(Bắt buộc)**** | string | Image ID. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID",
    "file_name": "FILE_NAME",
    "image_id": "IMAGE_ID"
}' \
https://business-api.tiktok.com/open_api/v1.3/file/image/ad/update/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return Information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned Data. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
  "message": "OK",
  "code": 0,
  "data": {},
  "request_id": "2020063011512801023125104012348"
}
```

---

<a id="doc-1740051721711618"></a>
<!-- doc_id: 1740051721711618 -->
<!-- doc_id: 1740051721711618 -->
# Get info about images
> Đường dẫn: API Reference > Images > Get info about images
Use this endpoint to obtain the information of  images from the Asset Library.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/file/image/ad/info/

**Method**  GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| image_ids  ****(Bắt buộc)**** | string[] | Image ID list. Up to 100 IDs per request. ⏎ **Note**:  If you obtain the image IDs of thumbnails for ads created on TikTok Ads Manager using the [/ad/get/](02-ads-p1.md#doc-1735735588640770) endpoint, they are not supported. This is because these thumbnails have not been uploaded to the Asset Library and linked to your ad account. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/file/image/ad/info/?advertiser_id={{advertiser_id}}&image_ids=["{{image_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return Information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned Data. |
| ↳ list | object[] | Information about the images. |
| ↳↳ image_id | string | Image ID, used to create ads. |
| ↳↳ material_id | string | Material ID. |
| ↳↳ is_carousel_usable | boolean | Liệu source of the image is valid for Carousel Ads. ⏎ **Note**: To use an image in Carousel Ads, you need to ensure:   •  The value of this field is `true`, **and ** •  The image meets the specifications requirements listed in [Create Carousel Ads-Steps-Create an ad](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713). |
| ↳↳ width | number | Image width. |
| ↳↳ format | string | Image format. |
| ↳↳ image_url | string | Image URL, valid for an hour and needs to be re-acquired after expiration. |
| ↳↳ height | number | Image height. |
| ↳↳ signature | string | MD5 of picture. |
| ↳↳ size | number | Image size in bytes. |
| ↳↳ file_name | string | Image name. |
| ↳↳ create_time | string | Thời gian tạo. UTC time. Format: 2020-06-10T07:39:14Z. |
| ↳↳ modify_time | string | Modification time. UTC time. Format: 2020-06-10T07:39:14Z. |
| ↳↳ displayable | boolean | Liệu it can be displayed on the platform. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "is_carousel_usable": true,
                "size": 39779,
                "format": "jpeg",
                "modify_time": "{{modify_time}}",
                "create_time": "{{create_time}}",
                "displayable": false,
                "width": 750,
                "material_id": "{{material_id}}",
                "image_url": "{{image_url}}",
                "file_name": "{{file_name}}",
                "image_id": "{{image_id}}",
                "signature": "{{signature}}",
                "height": 422
            }
        ]
    }
}
```

---

<a id="doc-1740052016789506"></a>
<!-- doc_id: 1740052016789506 -->
<!-- doc_id: 1740052016789506 -->
# Search for images
> Đường dẫn: API Reference > Images > Search for images
Sử dụng endpoint này để tìm kiếm image creatives in an advertising account's Asset Library.

Only the first 10000 images (ordered by `modify_time`) will be returned.

 ## Comparing v1.2 and v1.3
 The following table outlines the differences between v1.2 and v1.3 endpoints. 
 
| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | /v1.2/file/image/ad/search/ | /v1.3/file/image/ad/search/ |
| Request parameter data type | `advertiser_id`: number | `advertiser_id`: string |
| Response parameter deprecated in v1.3 | / | `id`: string |
| New response parameters | / | `is_carousel_usable` |

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/file/image/ad/search/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| filtering | object | Filters on the data. This parameter is an array of filter objects. |
| ↳ height | number | Image height. |
| ↳ image_ids | string[] | Image IDs. At most 100 IDs can be included in the list. |
| ↳ material_ids | string[] | A list of material IDs. At most 100 IDs can be included in the list. |
| ↳ ratio | float[] | Image aspect ratio, e.g.: [1.7, 2.5]. Use 1.7 to search for Images with aspect ratio between 1.65-1.75, i.e. the precision floating point is 0.05. |
| ↳ width | number | Image width. |
| ↳ displayable | boolean | Các giá trị enum hỗ trợ: • `False`(Giá trị mặc định): Search in all materials. • `True`: Search in the materials displayed on the platform. |
| page | number | Current Số trang cần lấy dữ liệu. Giá trị mặc định: 1. Value range: ≥ 1. |
| page_size | number | Page size. Giá trị mặc định: 20. Value range: 1-100. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/file/image/ad/search/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return Information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ list | object[] | A list of image information. |
| ↳↳ image_id | string | Image ID. It can be used to create ads. |
| ↳↳ material_id | string | Material ID. |
| ↳↳ is_carousel_usable | boolean | Liệu source of the image is valid for Carousel Ads. ⏎ **Note**: To use an image in Carousel Ads, you need to ensure:   •  The value of this field is `true`, **and ** •  The image meets the specifications requirements listed in [Create Carousel Ads-Steps-Create an ad](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713). |
| ↳↳ width | number | Image width. |
| ↳↳ format | string | Image format. |
| ↳↳ image_url | string | Picture preview link, valid for an hour and needs to be re-acquired after expiration. |
| ↳↳ height | number | Image height. |
| ↳↳ signature | string | MD5 of the image. |
| ↳↳ size | number | Image size. |
| ↳↳ file_name | string | Image name. |
| ↳↳ create_time | string | Thời gian tạo. UTC time. Format: 2020-06-10T07:39:14Z. |
| ↳↳ modify_time | string | Modification time. UTC time. Format: 2020-06-10T07:39:14Z. |
| ↳↳ displayable | boolean | Liệu it can be displayed on the platform. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Total pages of results. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "page_size": 20,
            "total_page": 1,
            "total_number": 2,
            "page": 1
        },
        "list": [
            {
                "height": 720,
                "size": 118834,
                "image_url": "{{image_url}}",
                "modify_time": "{{modify_time}}",
                "create_time": "{{create_time}}",
                "image_id": "{{image_id}}",
                "file_name": "{{file_name}}",
                "width": 1280,
                "signature": "{{signature}}",
                "displayable": false,
                "material_id": "{{material_id}}",
                "format": "jpeg",
                "is_carousel_usable": false
            },
            {
                "height": 720,
                "size": 159992,
                "image_url": "{{image_url}}",
                "modify_time": "{{modify_time}}",
                "create_time": "{{create_time}}",
                "image_id": "{{image_id}}",
                "file_name": "{{file_name}}",
                "width": 1280,
                "signature": "{{signature}}",
                "displayable": false,
                "material_id": "{{material_id}}",
                "format": "jpeg",
                "is_carousel_usable": false
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Hình ảnh (Images)**:

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

