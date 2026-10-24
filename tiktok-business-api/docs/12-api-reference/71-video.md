# Video

> Phân hệ: apiref:Video.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Video (#doc-1737587293087810)](#doc-1737587293087810)
- [2. Tải lên video (Upload a video) (#doc-1737587322856449)](#doc-1737587322856449)
- [3. Cập nhật tên video (Update the name of a video) (#doc-1740049987749890)](#doc-1740049987749890)
- [4. Lấy thông tin video (Get info about videos) (#doc-1740050161973250)](#doc-1740050161973250)
- [5. Tìm kiếm video (Search for videos) (#doc-1740050472224769)](#doc-1740050472224769)
- [6. Lấy ảnh bìa video đề xuất (Get suggested thumbnails for a video) (#doc-1740051189071873)](#doc-1740051189071873)

---

<a id="doc-1737587293087810"></a>
<!-- doc_id: 1737587293087810 -->
<!-- doc_id: 1737587293087810 -->
# Video
> Đường dẫn: API Reference > Video
Video là một loại tài sản nội dung sáng tạo bạn có thể sử dụng để tạo quảng cáo. Bạn cũng có thể sử dụng ID video trong các công cụ sáng tạo như [Video thông minh (Smart Video)](38-creative-tools.md#doc-1739352294717441), [Nhạc nền video thông minh (Smart Video Soundtrack)](38-creative-tools.md#doc-1739089635852289), [Tối ưu hóa nhanh (Quick Optimization)](38-creative-tools.md#doc-1739355078757377) và [Tự động sửa lỗi (Smart Fix)](38-creative-tools.md#doc-1741468875279361). Ngoài ra, video có thể được đưa vào gói video thông qua [/catalog/video_package/create/](31-catalog-video-templates.md#doc-1740665273039873), nơi bạn cần chỉ định video thông qua `video_id`.

Nhóm API này bao gồm các endpoint sau:
* [Tải lên video](71-video.md#doc-1737587322856449)
* [Cập nhật tên video](71-video.md#doc-1740049987749890)
* [Lấy thông tin video](71-video.md#doc-1740050161973250)
* [Tìm kiếm video](71-video.md#doc-1740050472224769)
* [Lấy ảnh bìa video đề xuất](71-video.md#doc-1740051189071873)

---

<a id="doc-1737587322856449"></a>
<!-- doc_id: 1737587322856449 -->
<!-- doc_id: 1737587322856449 -->
# Tải lên video (Upload a video)
> Đường dẫn: API Reference > Video > Upload a video
Sử dụng endpoint này để tải video lên Thư viện tài sản (Asset Library) và sử dụng ID video nhận được để tạo quảng cáo.

Thời gian chờ (timeout) cho giao diện này là 10 giây, và tốc độ truyền tải phụ thuộc vào băng thông mạng. Vui lòng bảo đảm dung lượng tệp tin ở mức hợp lý.

Nếu bạn tải lên video đã tồn tại sẵn trong tài khoản quảng cáo, hệ thống sẽ trả về thông tin của video hiện có đó.

> **Lưu ý:** 
> - Chúng tôi khuyến nghị bạn nên bật tính năng Smart Fix khi tải video lên. API này sẽ tự động phát hiện và sửa các lỗi kỹ thuật trong video, bảo đảm video đáp ứng đầy đủ tiêu chuẩn phân phối quảng cáo. Để tìm hiểu cách bật Smart Fix, vui lòng tham khảo [Smart Fix](../09-marketing-api/creatives.md#doc-1741472523309058).
> - Kể từ ngày 24 tháng 4 năm 2025, Smart Fix sẽ giới hạn các bản sửa tự động chỉ cho các loại lỗi `LOW_RESOLUTION` và `ILLEGAL_VIDEO_SIZE` và hoạt động như sau: 
> 	- Điều chỉnh độ phân giải:
> 		- `LOW_RESOLUTION`: Nếu phát hiện lỗi này, video sẽ tự động được nâng cấp lên độ phân giải tiêu chuẩn 1280x720 pixel (còn gọi là 720p).
>   	- `ILLEGAL_VIDEO_SIZE`: Nếu phát hiện lỗi này, video sẽ tự động được điều chỉnh về một trong các tỷ lệ khung hình chuẩn: 1:1 (vuông), 9:16 (dọc), hoặc 16:9 (ngang).
>  	- Giới hạn kết quả: Chỉ một phiên bản video đã sửa lỗi duy nhất được trả về.
>  	- Quy ước đặt tên: Video đã sửa sẽ được đặt tên theo tên tùy chỉnh chỉ định qua tham số `file_name` hoặc tuân theo quy ước đặt tên mặc định nếu không truyền tên tùy chỉnh (xem mô tả của `file_name` để biết chi tiết).

## Điều kiện tiên quyết trước khi bắt đầu
Bạn cần xác nhận video đáp ứng [Yêu cầu về nội dung sáng tạo để phân phối](https://ads.tiktok.com/help/article?aid=6669199281502552069) trước khi video có thể được sử dụng trong quảng cáo.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Nếu `upload_type` là `UPLOAD_BY_FILE`, sử dụng `multipart/form-data`. ⏎ Nếu `upload_type` là `UPLOAD_BY_URL` hoặc `UPLOAD_BY_FILE_ID`, sử dụng `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| file_name | string | Tên video. ⏎ Giới hạn độ dài: 1 - 100 ký tự. ⏎ Giá trị mặc định: • Khi không bật Smart Fix (`flaw_detect` và `auto_fix_enabled` đặt thành `false`): • Nếu bạn tải lên tệp cục bộ, tên mặc định là tên tệp gốc. • Nếu bạn cung cấp URL, tên mặc định là phần tên tệp trong đường dẫn URL. Nếu tên tệp gốc hoặc phần tên tệp vượt quá 100 ký tự, hệ thống sẽ cắt ngắn chỉ giữ lại 100 ký tự đầu tiên. • Khi bật Smart Fix (`flaw_detect` và `auto_fix_enabled` đặt thành `true`): • Tên mặc định sẽ là tên tệp gốc (đối với tệp cục bộ) hoặc phần tên tệp của URL (đối với URL). Nếu bạn chỉ định tên video tùy chỉnh qua `file_name`, giá trị `file_name` sẽ là tên của video đã sửa lỗi. ⏎ **Lưu ý**: Các video trong cùng một `advertiser_id` không được phép trùng tên tệp. Bạn có thể gọi [/file/name/check/](44-files.md#doc-1759130033155073) để kiểm tra xem tên tệp đã được sử dụng hay chưa. ⏎ Nếu gặp lỗi trùng tên tệp, vui lòng đổi tên tệp hoặc thêm dấu thời gian vào tên tệp gốc và tải lại video. |
| upload_type | string | Phương thức tải video lên. ⏎ Giá trị mặc định: `UPLOAD_BY_FILE` ⏎ Các giá trị enum hỗ trợ: `UPLOAD_BY_FILE`, `UPLOAD_BY_URL`, `UPLOAD_BY_FILE_ID`, `UPLOAD_BY_VIDEO_ID`. ⏎ **Lưu ý**: Nếu bạn đặt trường này là `UPLOAD_BY_FILE`, `UPLOAD_BY_URL` hoặc `UPLOAD_BY_FILE_ID`, một ID video mới (`video_id`) sẽ được trả về. Nếu bạn tải lên cùng một video nhiều lần bằng bất kỳ phương thức nào trong ba phương thức này, bạn sẽ nhận được một ID video mới cho mỗi lần tải. |
| video_file **(Điều kiện)** | file | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE`. ⏎ Tệp video. ⏎ Thông số khuyến nghị: ⏎ (1) Dung lượng tệp: Giới hạn tối đa 500 MB ⏎ (2) Tỷ lệ khung hình: 9:16, 16:9, và 1:1. ⏎ (3) Định dạng: .mp4, .mov, .mpeg, .avi. ⏎ Ví dụ: `'video_file=@"/Users/admin/Downloads/sample-mov-file.mov"'` ⏎ **Lưu ý**: Trước khi tải lên, hãy bảo đảm tệp tin có thể phát được bình thường và đúng định dạng hỗ trợ. |
| video_signature **(Điều kiện)** | string | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE`. ⏎ Mã băm MD5 của video (dùng để xác thực phía máy chủ). |
| video_url **(Điều kiện)** | string | Bắt buộc khi `upload_type` là `UPLOAD_BY_URL`. ⏎ Địa chỉ URL của video, ví dụ http://xxx.xxx. ⏎ (1) Dung lượng tệp: Khuyến nghị dưới 10 MB. ⏎ (2) Xác thực: Hệ thống sẽ xác thực `Content-Type` trong header phản hồi. Loại phương tiện không hợp lệ phổ biến là dạng văn bản (`Content-Type` = text/*, chẳng hạn text/html, text/plain). Ngoài ra, hệ thống sẽ xác thực dữ liệu nếu bạn cài đặt `Content-MD5` trong header phản hồi. ⏎ (3) Mã hóa: URL cần là URL hợp lệ trong trình duyệt. Ví dụ, khoảng trắng trong URL phải được mã hóa thành `%20`. Bạn có thể sao chép và dán URL vào thanh địa chỉ trình duyệt để URL tự động mã hóa. ⏎ (4) Khác: Giới hạn về tỷ lệ khung hình, định dạng, độ phân giải và tốc độ bit tương tự như `video_file`. ⏎ **Lưu ý**: Trước khi tải lên, hãy chắc chắn URL video **có thể phát được** và ở **định dạng được hỗ trợ**. Nếu URL không hợp lệ hoặc sai định dạng (ví dụ .txt), bạn có thể nhận thông báo lỗi hoặc ID video không hợp lệ và không thể dùng tạo quảng cáo. |
| file_id **(Điều kiện)** | string | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE_ID`. ⏎ `file_id` của tệp bạn muốn tải lên. Trường này áp dụng cho các tệp đã tải lên kho lưu trữ tệp. Bạn có thể lấy `file_id` qua các endpoint [Upload Files](44-files.md#doc-1737719988918274). |
| video_id **(Điều kiện)** | string | Bắt buộc khi `upload_type` là `UPLOAD_BY_VIDEO_ID`. ⏎ ID video. ⏎ **Lưu ý**: Bạn cần truyền vào `video_id` của video được tạo trên **TikTok Ads Manager** hoặc qua **API**. Nếu truyền giá trị từ các nguồn khác, bạn có thể nhận thông báo lỗi hoặc không thể sử dụng video để tạo quảng cáo. ⏎ Bạn có thể lấy `video_id` trong phản hồi của endpoint [/file/video/ad/upload/](71-video.md#doc-1737587322856449) hoặc qua endpoint [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| is_third_party | boolean | Video có phải từ bên thứ ba hay không. |
| flaw_detect | boolean | Có tự động phát hiện sự cố kỹ thuật trong video của bạn hay không. ⏎ Giá trị mặc định: `false`. |
| auto_fix_enabled | boolean | Có tự động sửa sự cố đã phát hiện hay không. ⏎ Giá trị mặc định: `false`. ⏎ Nếu phát hiện sự cố trong video của bạn: • Khi `auto_fix_enabled` đặt thành `false`, hệ thống sẽ trả về thông báo lỗi kèm danh sách loại lỗi. • Khi `auto_fix_enabled` đặt thành `true`, hệ thống sẽ tự động sửa các lỗi `LOW_RESOLUTION` và `ILLEGAL_VIDEO_SIZE` đồng thời trả về `fix_task_id` và `flaw_types`. ⏎ **Lưu ý**: • Khi phát hiện lỗi `LOW_RESOLUTION`, video sẽ tự động được nâng cấp lên độ phân giải chuẩn 1280x720 pixel (720p). • Khi phát hiện lỗi `ILLEGAL_VIDEO_SIZE`, video sẽ tự động được điều chỉnh về một trong các tỷ lệ khung hình chuẩn: 1:1 (vuông), 9:16 (dọc), hoặc 16:9 (ngang). |
| auto_bind_enabled | boolean | Chỉ hợp lệ khi `flaw_detect` = `true` và `auto_fix_enabled` = `true`. ⏎ Có tự động tải video đã sửa lỗi lên thư viện nội dung sáng tạo của bạn hay không. ⏎ Giá trị mặc định: `false`. |
| pre_review_enabled | boolean | Có tạo tác vụ tiền kiểm duyệt cho video và các tài liệu liên quan (gồm văn bản quảng cáo và URL trang đích) hay không. ⏎ Tác vụ tiền kiểm duyệt là quy trình đánh giá tính tuân thủ và chất lượng của tài nguyên sáng tạo trước khi tạo quảng cáo, bảo đảm đáp ứng quy chuẩn quảng cáo của TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ Khi đặt trường này là `true`, bạn cần đồng thời chỉ định `pre_review_info`, và phản hồi sẽ bao gồm `pre_review_task_id`. |
| pre_review_info **(Điều kiện)** | object | Bắt buộc khi `pre_review_enabled` đặt thành `true`. ⏎ Thông tin chi tiết bổ sung cho quá trình tiền kiểm duyệt. |
| ↳ landing_page_url | string | Đường dẫn URL của trang đích sử dụng trong quảng cáo. |
| ↳ ad_text | string | Nội dung văn bản hiển thị trong quảng cáo. ⏎ Văn bản quảng cáo hiển thị cho khán giả như một phần của mẫu quảng cáo để truyền tải thông điệp. ⏎ Văn bản quảng cáo phải dài từ 1-100 ký tự và không chứa biểu tượng cảm xúc (emoji). ⏎ Mỗi chữ tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi chữ cái tiếng Anh tính là 1 ký tự. |
| ↳ location_codes **(Điều kiện)** | string[] | Bắt buộc khi chỉ định `pre_review_info`. ⏎ Danh sách mã quốc gia/khu vực bạn muốn nhắm mục tiêu. ⏎ Kích thước tối đa: 1. ⏎ Để xem danh sách giá trị enum, xem [Danh sách giá trị cho `location_codes` hoặc `location_code`](#anchor-location-codes). ⏎ Ví dụ: `US`. |
| ↳ is_ecommerce | boolean | Liệu tài nguyên sáng tạo có dành cho quảng cáo thương mại điện tử (E-commerce), bao gồm [Chiến dịch GMV Max](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009058467842) và Quảng cáo Catalog hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |

<a id="anchor-location-codes"></a>
## Danh sách giá trị cho `location_codes` hoặc `location_code` (List of values for `location_codes` or `location_code`)

Bảng dưới đây liệt kê các giá trị enum cho tham số yêu cầu `location_codes` trong [/creative/pre_review/task/create/](35-creative-pre-review.md#doc-1874110632584577), [/file/video/ad/upload/](71-video.md#doc-1737587322856449), và [/file/image/ad/upload/](47-images.md#doc-1739067433456642), cùng tham số phản hồi `location_code` trong [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082).

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

## Ví dụ lệnh cURL (Example)
### Tải lên qua tệp có bật Smart Fix (Upload by file with Smart Fix enabled)
```bash
# cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--form 'advertiser_id="{{advertiser_id}}"' \
--form 'file_name="{{file_name}}"' \
--form 'upload_type="UPLOAD_BY_FILE"' \
--form 'video_file=@"/Desktop/Example.mp4"' \
--form 'video_signature="{{video_signature}}"' \
--form 'flaw_detect="true"' \
--form 'auto_fix_enabled="true"' \
--form 'auto_bind_enabled="true"'
```

### Tải lên qua tệp không bật Smart Fix (Upload by file with Smart Fix disabled)
```bash
# cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--form 'advertiser_id="{{advertiser_id}}"' \
--form 'file_name="{{file_name}}"' \
--form 'upload_type="UPLOAD_BY_FILE"' \
--form 'video_file=@"/Desktop/Example.mp4"' \
--form 'video_signature="{{video_signature}}"'
```

### Tải lên qua URL có bật Smart Fix (Upload by URL with Smart Fix enabled)
```bash
# cURL
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--data '{
    "advertiser_id":"{{advertiser_id}}",
    "file_name":"{{file_name}}",
    "upload_type":"UPLOAD_BY_URL",
    "video_url":"{{video_url}}",
    "flaw_detect":true,
    "auto_fix_enabled":true,
    "auto_bind_enabled":true
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object[] | Dữ liệu trả về. Vì lý do tương thích ngược, dữ liệu trả về dưới dạng mảng chỉ chứa một đối tượng duy nhất. ⏎ **Lưu ý**: Do độ trễ mạng giữa client và server, có thể ban đầu chỉ có `video_id` được trả về. Trường hợp này bạn có thể chờ từ 30 giây đến 5 phút rồi gọi endpoint [/file/video/ad/search/](71-video.md#doc-1740050472224769) để truy xuất toàn bộ thông tin. |
| ↳ video_cover_url | string | URL tạm thời của ảnh bìa video, có giá trị trong 6 giờ và cần lấy lại khi hết hạn. ⏎ Thời điểm hết hạn nằm sau tham số `x-expires` theo định dạng Epoch/Unix timestamp (giây). ⏎ Ví dụ: `http://p16-sign-sg.tiktokcdn.com/v0201/b99a388e3709470be5c~tplv-noop.image?x-expires=**1671742348**&x-signature=FziJhvED9NDTDmPofv3I%3D`. |
| ↳ format | string | Định dạng video. |
| ↳ preview_url | string | Liên kết xem trước video, có giá trị trong 6 giờ và cần lấy lại khi hết hạn. ⏎ Để tra cứu thời gian hết hạn, xem `preview_url_expire_time`. |
| ↳ preview_url_expire_time | string | Thời gian hết hạn của liên kết xem trước video, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ file_name | string | Tên tệp video. |
| ↳ displayable | boolean | Liệu video có thể hiển thị được trên nền tảng hay không. |
| ↳ height | number | Chiều cao video (pixels). |
| ↳ width | number | Chiều rộng video (pixels). |
| ↳ bit_rate | number | Tốc độ bit tính theo bps. |
| ↳ create_time | string | Thời gian tạo theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| ↳ modify_time | string | Thời gian chỉnh sửa theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| ↳ signature | string | Mã băm MD5 của tệp video. |
| ↳ duration | float | Thời lượng video, tính bằng giây. |
| ↳ video_id | string | ID video, sử dụng để tạo quảng cáo. ⏎ **Lưu ý**: • Nếu tải lên bằng ID video (`upload_type` là `UPLOAD_BY_VIDEO_ID`), cùng ID video đó sẽ được trả về. • Nếu tải lên bằng tệp, URL hoặc ID tệp (`upload_type` là `UPLOAD_BY_FILE`, `UPLOAD_BY_URL` hoặc `UPLOAD_BY_FILE_ID`), một ID video mới (`video_id`) sẽ được sinh ra cho mỗi lần tải lên. |
| ↳ size | number | Dung lượng tệp video, tính theo bytes. |
| ↳ material_id | string | ID tài nguyên (Material ID). |
| ↳ allowed_placements | string[] | Các vị trí phân phối được phép. Do bản quyền âm nhạc, một số tài nguyên do công cụ sáng tạo sinh ra chỉ được phép phân phối trên TikTok. Xem danh sách enum tại [Phụ lục - Vị trí phân phối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Các giá trị `PLACEMENT_TOPBUZZ` và `PLACEMENT_HELO` không còn khả dụng để tạo quảng cáo và sẽ bị ngừng hỗ trợ trong phiên bản tới. |
| ↳ allow_download | boolean | Liệu video có được phép tải xuống hay không. Do bản quyền âm nhạc, một số tài nguyên chỉ được xem trước, nghiêm cấm tải xuống hoặc phát tán. |
| ↳ fix_task_id | string | Chỉ trả về khi bạn đặt cả `flaw_detect` và `auto_fix_enabled` là `true` trong yêu cầu, và có lỗi video được phát hiện. ⏎ ID tác vụ sửa lỗi (Fix task ID). ⏎ Để lấy video đã sửa lỗi, bạn có thể: • Truyền giá trị trường này vào trường `task_id` trong [/video/fix/task/get/](38-creative-tools.md#doc-1741469487859714). • Hoặc truy xuất từ [/file/video/ad/search/](71-video.md#doc-1740050472224769) nếu bạn đã đặt `auto_bind_enabled` là `true`. |
| ↳ flaw_types | string[] | Chỉ trả về khi bạn đặt cả `flaw_detect` và `auto_fix_enabled` là `true` và có lỗi video. ⏎ Danh sách loại lỗi phát hiện trong video. ⏎ Các giá trị enum: • `LOW_RESOLUTION`: Độ phân giải thấp hơn 540x960 px, không đạt yêu cầu. • `ILLEGAL_VIDEO_SIZE`: Kích thước khung hình không hợp lệ. Hãy dùng kích thước chuẩn: Vuông (1:1), Dọc (9:16), Ngang (16:9). • `NO_BGM` (sắp ngừng hỗ trợ): Video không có âm thanh nền hoặc âm thanh không rõ ràng. • `BLACK_EDGE` (sắp ngừng hỗ trợ): Video có viền đen ảnh hưởng trải nghiệm. • `ILLEGAL_DURATION` (sắp ngừng hỗ trợ): Thời lượng dài hơn 60s hoặc ngắn hơn 5s. |
| ↳ pre_review_task_id | string | Chỉ trả về khi `pre_review_enabled` trong yêu cầu đặt là `true`. ⏎ ID của tác vụ tiền kiểm duyệt. ⏎ Để lấy kết quả tiền kiểm duyệt, truyền giá trị này vào trường `task_id` trong [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082). |

## Ví dụ lệnh cURL (Example)
### Phản hồi tải lên qua tệp có bật Smart Fix khi phát hiện lỗi (Upload by file with Smart Fix enabled and issue detected)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": [
        {
            "fix_task_id": "{{fix_task_id}}",
            "flaw_types": [
                "LOW_RESOLUTION"
            ]
        }
    ]
}
```

### Phản hồi tải lên qua tệp không bật Smart Fix (Upload by file with Smart Fix disabled)
> **Lưu ý:** 
>Do độ trễ mạng giữa client và server, có thể chỉ `video_id` được trả về ngay. Trong trường hợp đó, bạn có thể chờ từ 30 giây đến 5 phút rồi gọi endpoint [/file/video/ad/search/](71-video.md#doc-1740050472224769) để lấy đầy đủ dữ liệu.

```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": [
        {
            "video_id": "{{video_id}}"
        }
    ]
}
```

### Phản hồi tải lên qua URL có bật Smart Fix khi phát hiện lỗi (Upload by URL with Smart Fix enabled and issue detected)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": [
        {
            "fix_task_id": "{{fix_task_id}}",
            "flaw_types": [
                "ILLEGAL_VIDEO_SIZE"
            ]
        }
    ]
}
```

---

<a id="doc-1740049987749890"></a>
<!-- doc_id: 1740049987749890 -->
<!-- doc_id: 1740049987749890 -->
# Cập nhật tên video (Update the name of a video)
> Đường dẫn: API Reference > Video > Update the name of a video
Sử dụng endpoint này để cập nhật tên của một video trong thư viện.

### Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/file/video/ad/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. Sử dụng `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| file_name  ****(Bắt buộc)**** | string | Tên video mới. Giới hạn độ dài: 1 - 100 ký tự. Nếu một video khác đã dùng cùng tên tệp trong cùng `advertiser_id`, hệ thống sẽ tự động thêm dấu thời gian mili-giây vào cuối. Nếu tên chứa hơn 100 ký tự, chỉ 100 ký tự đầu tiên được sử dụng. |
| video_id  ****(Bắt buộc)**** | string | ID video cần cập nhật tên. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID",
    "file_name": "FILE_NAME",
    "video_id": "VIDEO_ID"
}' \
https://business-api.tiktok.com/open_api/v1.3/file/video/ad/update/
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). Xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| request_id | string | Mã định danh duy nhất của yêu cầu (Log ID). |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
  "message": "OK",
  "code": 0,
  "data": {},
  "request_id": "2020063011514801023125104012818"
}
```

---

<a id="doc-1740050161973250"></a>
<!-- doc_id: 1740050161973250 -->
<!-- doc_id: 1740050161973250 -->
# Lấy thông tin chi tiết video (Get info about videos)
> Đường dẫn: API Reference > Video > Get info about videos
Sử dụng endpoint này để lấy thông tin chi tiết về danh sách các video có thể dùng trong quảng cáo từ Thư viện tài sản (Asset Library).

### Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/file/video/ad/info/

**Method**  GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| video_ids  ****(Bắt buộc)**** | string[] | Danh sách ID video cần tra cứu. ⏎ Kích thước tối đa: 60. ⏎ **Lưu ý**: Nếu video không thể dùng trong quảng cáo, ID video đó sẽ bị bỏ qua. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \\
--data-urlencode "advertiser_id=ADVERTISER_ID" \\
--data-urlencode "video_ids=VIDEO_IDS" \\
https://business-api.tiktok.com/open_api/v1.3/file/video/ad/info/
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ máy chủ. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ list | list | Danh sách dữ liệu video. |
| ↳↳ displayable | boolean | Liệu video có thể hiển thị được trên nền tảng hay không. |
| ↳↳ width | number | Chiều rộng video (pixels). |
| ↳↳ video_cover_url | string | URL tạm thời của ảnh bìa video, có giá trị trong 6 giờ và cần lấy lại sau khi hết hạn. ⏎ Thời điểm hết hạn nằm sau tham số `x-expires` theo định dạng Epoch/Unix timestamp (giây). ⏎ Ví dụ: `http://p16-sign-sg.tiktokcdn.com/v0201/b99a388e3709470be5c~tplv-noop.image?x-expires=**1671742348**&x-signature=FziJhvED9NDTDmPofv3I%3D`. |
| ↳↳ bit_rate | number | Tốc độ bit tính theo bps. |
| ↳↳ format | string | Định dạng tệp video. |
| ↳↳ preview_url | string | Liên kết xem trước video, có hiệu lực trong 6 giờ và cần lấy lại sau khi hết hạn. ⏎ Xem thời gian hết hạn tại `preview_url_expire_time`. |
| ↳↳ preview_url_expire_time | string | Thời gian hết hạn của liên kết xem trước video, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ duration | float | Thời lượng video tính bằng giây. |
| ↳↳ height | number | Chiều cao video (pixels). |
| ↳↳ signature | string | Mã băm MD5 của tệp video. |
| ↳↳ video_id | string | ID video, dùng để tạo quảng cáo phân phối. |
| ↳↳ size | number | Dung lượng video tính bằng bytes. |
| ↳↳ material_id | string | ID tài nguyên (Material ID). |
| ↳↳ allowed_placements | string[] | Vị trí phân phối khả dụng. Do bản quyền âm nhạc, một số tài nguyên tạo bởi công cụ sáng tạo chỉ được phép phân phối trên TikTok. Xem danh sách enum tại [Phụ lục - Vị trí phân phối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ allow_download | boolean | Liệu video có được phép tải xuống hay không. Do bản quyền âm nhạc, một số tài nguyên chỉ được xem trước, nghiêm cấm tải xuống hoặc phát tán. |
| ↳↳ file_name | string | Tên tệp video. |
| ↳↳ create_time | string | Thời gian tạo theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| ↳↳ modify_time | string | Thời gian cập nhật theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "list": [
            {
                "format": "mp4",
                "preview_url": "http://v16-tiktokcdn-com.akamaized.net/2a19f67683ed9aa54b3df2e5c842f15d/5fccd703/video/tos/alisg/tos-alisg-v-0000/9a0033884eab42248ad6b46f7b11e44c/?a=0&br=3114&bt=1557&cd=0%7C0%7C0&cr=0&cs=0&dr=0&ds=3&er=&l=2020120607050201011517615618A693BE&lr=ad&mime_type=video_mp4&qs=0&rc=anNlbnRuOWU2eDMzZjYzM0Apdjh3ZHJuOWZzZTMzNDY6eWdwMnFebGgzYG1fLS0uMDRzc2RtX2huaDNfMHItLWAwLS06Yw%3D%3D&vl=&vr=",
                "file_name": "wanfadong_tagging_test.mp4",
                "video_cover_url": "http://p16-sign-sg.tiktokcdn.com/v0201/94ebe1a3e6734559a16f3e81c43787ec~tplv-noop.image?x-expires=1607259907&x-signature=Oy4%2FyYvkw%2FLTWz97pFCDx0Y6o4g%3D",
                "height": 720,
                "width": 1280,
                "bit_rate": 1594584,
                "create_time": "2020-11-16T08:19:57Z",
                "modify_time": "2020-11-16T08:19:57Z",
                "signature": "b24f08f569b73a33eec93edb8f4423e2",
                "duration": 5.312,
                "video_id": "v070331c0000bup3cb66kkoqaktb5psg",
				"material_id": "6895633277416374000",
            	"allowed_placements": [
                    "PLACEMENT_TOPBUZZ",
                    "PLACEMENT_TIKTOK",
                    "PLACEMENT_HELO",
                    "PLACEMENT_PANGLE"
            	],
            	"allow_download": true,
                "size": 1058804
            }
        ]
    },
    "request_id": "2020120607050201011517615618A693BE"
}
```

---

<a id="doc-1740050472224769"></a>
<!-- doc_id: 1740050472224769 -->
<!-- doc_id: 1740050472224769 -->
# Tìm kiếm video (Search for videos)
> Đường dẫn: API Reference > Video > Search for videos
Sử dụng endpoint này để tìm kiếm các nội dung video sáng tạo có thể sử dụng trong quảng cáo từ Thư viện tài sản của tài khoản quảng cáo.

Phản hồi sẽ chỉ bao gồm tối đa 10.000 video được sửa đổi gần đây nhất.

## So sánh giữa v1.2 và v1.3 (Comparing v1.2 and v1.3)
Bảng dưới đây nêu rõ các điểm khác biệt giữa endpoint v1.2 và v1.3.

| Changes | v1.2 | v1.3 |
|---|---|---|
| Đường dẫn endpoint | `/v1.2/file/video/ad/search/` | `/v1.3/file/video/ad/search/` |
| Kiểu dữ liệu tham số yêu cầu | `advertiser_id`: number | `advertiser_id`: string |
| Tham số yêu cầu ngừng hỗ trợ ở v1.3 | / | `height` ⏎ `ratio` ⏎ `width` ⏎ `displayable` |
| Tên tham số phản hồi | `poster_url` ⏎ `url` | `video_cover_url` ⏎ `preview_url` |
| Tham số phản hồi ngừng hỗ trợ ở v1.3 | / | `id` |
| Tham số yêu cầu mới bổ sung | / | `video_name` ⏎ `video_material_sources` ⏎ `sort_field` |
| Tham số phản hồi mới bổ sung | / | `preview_url_expire_time` |

### Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/file/video/ad/search/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| filtering | object | Điều kiện lọc dữ liệu. |
| ↳ video_ids | string[] | Danh sách ID video. ⏎ Kích thước tối đa: 100. ⏎ **Lưu ý**: • Nếu video không dùng được trong quảng cáo, ID video sẽ bị bỏ qua. • Nếu không truyền trường lọc này và có nhiều ID video được sinh ra cho cùng một video do tải lên nhiều lần, chỉ một ID video hợp lệ duy nhất được trả về cho video đó. |
| ↳ material_ids | string[] | Danh sách ID tài nguyên (Material ID). ⏎ Kích thước tối đa: 20. |
| ↳ video_name | string | Tên video. Bạn có thể tìm kiếm gần đúng (fuzzy search) bằng cách nhập tên video. |
| ↳ video_material_sources | string[] | Danh sách nguồn tài nguyên video. Bạn có thể tìm kiếm video theo nguồn gốc tạo ra. ⏎ Các giá trị enum hỗ trợ: • `UPLOADED_TO_TIKTOK_ADS_MANAGER`: Tải lên từ TikTok Ads Manager. • `UPLOADED_TO_CATALOG`: Tải lên từ Catalog. • `CREATIVE_TOOL_SMART_VIDEO`: Công cụ Creative - Smart Video. • `CREATIVE_TOOL_QUICK_OPTIMIZATION`: Công cụ Creative - Tối ưu nhanh. • `CREATIVE_TOOL_VIDEO_TEMPLATE`: Công cụ Creative - Mẫu video. • `CREATIVE_TOOL_SMART_VIDEO_SOUNDTRACK`: Công cụ Creative - Nhạc nền Smart Video. • `CREATIVE_TOOL_TIKTOK_VIDEO_EDITOR`: Công cụ Creative - Trình biên tập video TikTok. • `TIKTOK_CREATIVE_EXCHANGE`: Sàn giao dịch TikTok Creative Exchange. • `CATALOG_VIDEO_TEMPLATE`: Mẫu video Catalog. • `DYNAMIC_VIDEO_EDITOR`: Trình biên tập video động. • `CREATIVE_CHALLENGE`: Creative challenge. • `AUTOMATED_CREATIVE_OPTIMIZATION`: Tối ưu hóa sáng tạo tự động (ACO). • `OTHER`: Khác. • `QUICK_GENERATION`: Tạo nhanh. • `CREATIVE_CENTER_VIDEO_UPLOAD`: Creative Center - Tải lên video. • `CREATIVE_CENTER_TIKTOK_VIDEO_EDITOR`: Creative Center - Trình biên tập video. • `CREATIVE_CENTER_VIDEO_TEMPLATE`: Creative Center - Mẫu video. • `DYNAMIC_SCENE`: Phân cảnh động. • `SMART_OPTIMIZATION_TOOL`: Công cụ tối ưu hóa thông minh. |
| sort_field | string | Tiêu chí sắp xếp danh sách video. ⏎ Các giá trị enum hỗ trợ: • `CREATE_TIME`: Sắp xếp theo thời gian tạo giảm dần (DESC), đưa các video tạo gần nhất lên đầu. • `MODIFY_TIME`: Sắp xếp theo thời gian cập nhật gần nhất giảm dần (DESC), đưa các video vừa chỉnh sửa lên đầu. Giá trị mặc định: `CREATE_TIME`. |
| page | number | Số trang hiện tại cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. Phạm vi: ≥ 1. |
| page_size | number | Số lượng kết quả trên mỗi trang. ⏎ Giá trị mặc định: 20. Phạm vi: 1-100. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id={advertiser_id}" \
--data-urlencode "filtering={\"width\": \"{width}\", \"video_ids\": [\"{video_ids}\"], \"ratio\": [\"{ratio}\"], \"height\": \"{height}\"}" \
--data-urlencode "page={page}" \
--data-urlencode "page_size={page_size}" \
https://business-api.tiktok.com/open_api/v1.3/file/video/ad/search/
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách thông tin video. |
| ↳↳ video_id | string | ID video, sử dụng để tạo quảng cáo. ⏎ **Lưu ý**: Nếu không truyền `video_ids` và có nhiều ID cho cùng một video do tải lên nhiều lần, chỉ một ID video hợp lệ duy nhất được trả về. |
| ↳↳ video_cover_url | string | URL tạm thời của ảnh bìa video, có giá trị trong 6 giờ và cần lấy lại sau khi hết hạn. ⏎ Thời điểm hết hạn nằm sau tham số `x-expires` theo Unix timestamp. ⏎ Ví dụ: `http://p16-sign-sg.tiktokcdn.com/v0201/b99a388e3709470be5c~tplv-noop.image?x-expires=**1671742348**&x-signature=FziJhvED9NDTDmPofv3I%3D`. |
| ↳↳ format | string | Định dạng video. |
| ↳↳ preview_url | string | Liên kết xem trước video, có hiệu lực trong 6 giờ và cần lấy lại khi hết hạn. ⏎ Xem thời gian hết hạn tại `preview_url_expire_time`. |
| ↳↳ preview_url_expire_time | string | Thời gian hết hạn của liên kết xem trước video, định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳↳ duration | float | Thời lượng video, tính bằng giây. |
| ↳↳ height | number | Chiều cao video (pixels). |
| ↳↳ width | number | Chiều rộng video (pixels). |
| ↳↳ bit_rate | float | Tốc độ bit, tính theo bps. |
| ↳↳ signature | string | Mã băm MD5 của tệp video. |
| ↳↳ size | number | Dung lượng video tính bằng bytes. |
| ↳↳ material_id | string | ID tài nguyên (Material ID). |
| ↳↳ allowed_placements | string[] | Vị trí phân phối khả dụng. Xem chi tiết tại [Phụ lục - Vị trí phân phối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ allow_download | boolean | Liệu video có được phép tải xuống hay không. Do bản quyền âm nhạc, một số tài nguyên chỉ được xem trước, nghiêm cấm tải xuống hoặc phát tán. |
| ↳↳ file_name | string | Tên tệp video. |
| ↳↳ create_time | string | Thời gian tạo theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| ↳↳ modify_time | string | Thời gian cập nhật theo giờ UTC. Định dạng: `2020-06-10T07:39:14Z`. |
| ↳↳ displayable | boolean | Liệu video có thể hiển thị trên nền tảng hay không. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu. |
| ↳↳ page_size | number | Số kết quả trên mỗi trang. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |
| request_id | string | Mã định danh duy nhất của yêu cầu (Log ID). |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "page_info": {
            "total_number": 1,
            "page": 1,
            "page_size": 20,
            "total_page": 1
        },
        "list": [
            {
                "video_cover_url": "http://p16-sign-sg.tiktokcdn.com/v0201/94ebe1a3e6734559a16f3e81c43787ec~tplv-noop.image?x-expires=1607260002&x-signature=falvnSNOT94w4gjeB8PGGFyAdys%3D",
                "format": "mp4",
                "preview_url": "http://v16m-default.akamaized.net/64d28cac783ab57b70c2d91c30fb1b5d/5fccd762/video/tos/alisg/tos-alisg-v-0000/9a0033884eab42248ad6b46f7b11e44c/?a=0&br=3114&bt=1557&cd=0%7C0%7C0&cr=0&cs=0&dr=0&ds=3&er=&l=2020120607063701011517615517A19974&lr=ad&mime_type=video_mp4&qs=0&rc=anNlbnRuOWU2eDMzZjYzM0Apdjh3ZHJuOWZzZTMzNDY6eWdwMnFebGgzYG1fLS0uMDRzc2RtX2huaDNfMHItLWAwLS06Yw%3D%3D&vl=&vr=",
                "file_name": "wanfadong_test.mp4",
                "displayable": true,
                "height": 720,
                "width": 1280,
                "bit_rate": 1594584,
                "create_time": "2020-11-16T08:19:57Z",
                "modify_time": "2020-11-16T08:19:57Z",
                "signature": "b24f08f569b73a33eec93edb8f4423e2",
                "duration": 5.312,
                "video_id": "v070331c0000bup3cb66kkoqaktb5psg",
				"material_id": "6895633277416374000",
            	"allowed_placements": [
                    "PLACEMENT_TOPBUZZ",
                    "PLACEMENT_TIKTOK",
                    "PLACEMENT_HELO",
                    "PLACEMENT_PANGLE"
            	],
            	"allow_download": true,
                "size": 1058804
            }
        ]
    },
    "request_id": "2020120607063701011517615517A19974"
}
```

---

<a id="doc-1740051189071873"></a>
<!-- doc_id: 1740051189071873 -->
<!-- doc_id: 1740051189071873 -->
# Lấy ảnh bìa video đề xuất (Get suggested thumbnails for a video)
> Đường dẫn: API Reference > Video > Get suggested thumbnails for a video
Sử dụng endpoint này để lấy danh sách ảnh bìa video đề xuất dựa trên nội dung video sáng tạo. Bạn có thể xem trước các ảnh bìa bằng URL trong phản hồi, sau đó chọn một hình ảnh làm ảnh bìa cho quảng cáo video của mình.

> **Lưu ý:** 
> Nếu bạn muốn lấy ảnh bìa đề xuất cho một video vừa tải lên gần đây, chúng tôi khuyến nghị bạn chờ từ 30 giây đến 5 phút trước khi gọi endpoint này để video được chuyển mã (transcode) và xử lý hoàn tất. Gọi endpoint trước khi chuyển mã xong có thể gây lỗi `Insufficient permissions for some videos`.

## So sánh giữa v1.2 và v1.3 (Comparing v1.2 and v1.3)
Bảng dưới đây nêu rõ các điểm khác biệt giữa endpoint v1.2 và v1.3.

| Changes | v1.2 | v1.3 |
|---|---|---|
| Đường dẫn endpoint | `/v1.2/file/video/suggestcover/` | `/v1.3/file/video/suggestcover/` |
| Kiểu dữ liệu tham số yêu cầu | `advertiser_id`: number | `advertiser_id`: string |

### Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/file/video/suggestcover/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| video_id  ****(Bắt buộc)**** | string | Video ID. |
| poster_number | number | Số lượng ảnh bìa ứng viên bạn muốn lấy. Phạm vi: `1-10`. Giá trị mặc định: `10`. **Nếu tổng số ảnh bìa ứng viên ít hơn số lượng yêu cầu, toàn bộ ứng viên sẽ được trả về. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id={advertiser_id}" \
--data-urlencode "video_id={video_id}" \
https://business-api.tiktok.com/open_api/v1.3/file/video/suggestcover/
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách thông tin hình ảnh. |
| ↳↳ width | number | Chiều rộng hình ảnh (pixels). |
| ↳↳ height | number | Chiều cao hình ảnh (pixels). |
| ↳↳ id | string | ID hình ảnh. |
| ↳↳ url | string | Địa chỉ URL xem trước hình ảnh, có giá trị trong 1 giờ và cần lấy lại khi hết hạn. |
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "list": [
          {
            "url": "http://p1.ipstatp.com/large/tos-useast2a-p-0000/8cc546a4b96a4933a27b0c7fefdd66a9_1584964597",
            "width": 560,
            "id": "tos-useast2a-p-0000/8cc546a4b96a4938a27b0c7fefdd66a9_1584964597",
            "height": 320
          },
          {
            "url": "http://p1.ipstatp.com/large/tos-useast2a-p-0000/36973f6fd2344c9fa5889db57d743ac6_1584964597",
            "width": 560,
            "id": "tos-useast2a-p-0000/36973f6fd2344c90a5889db57d743ac6_1584964597",
            "height": 320
          }
        ]
    },
    "request_id": "2020032312235001018904922349195A66"
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Video**:

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

