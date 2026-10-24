# Smart Creative

> Phân hệ: apiref:Smart Creative.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Nội dung sáng tạo thông minh (Smart Creative) (#doc-1739472835319809)](#doc-1739472835319809)
- [2. Lấy danh sách tài nguyên Smart Creative (Get Smart Creative materials) (#doc-1739473020978177)](#doc-1739473020978177)
- [3. Tạo quảng cáo Smart Creative (Create Smart Creative ads) (#doc-1739473063234626)](#doc-1739473063234626)
- [4. Cập nhật tài nguyên Smart Creative (Update Smart Creative materials) (#doc-1739473077112833)](#doc-1739473077112833)
- [5. Cập nhật trạng thái tài nguyên Smart Creative (Update the statuses of Smart Creative materials) (#doc-1739506701165570)](#doc-1739506701165570)

---

<a id="doc-1739472835319809"></a>
<!-- doc_id: 1739472835319809 -->
<!-- doc_id: 1739472835319809 -->
# Smart Creative
> Đường dẫn: API Reference > Smart Creative
Smart Creative là giải pháp sáng tạo tự động hóa của TikTok, giúp tối ưu hóa việc phối hợp các tổ hợp tài nguyên quảng cáo thông qua tính năng phát hiện tình trạng bão hòa nhóm quảng cáo (ad group fatigue) và chiến lược tự động làm mới tài nguyên. Tính năng này giúp giảm mỏi mệt nội dung quảng cáo, kéo dài tuổi thọ nhóm quảng cáo và cải thiện hiệu quả chi phí lâu dài.

Để tìm hiểu cách bật Smart Creative cho nhóm quảng cáo, xem [Smart Creative](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1767322784934914).

Nhóm API này bao gồm các endpoint sau: 
* [Tạo quảng cáo Smart Creative](60-smart-creative.md#doc-1739473063234626)
* [Lấy danh sách tài nguyên Smart Creative](60-smart-creative.md#doc-1739473020978177)
* [Cập nhật tài nguyên Smart Creative](60-smart-creative.md#doc-1739473077112833)
* [Cập nhật trạng thái tài nguyên Smart Creative](60-smart-creative.md#doc-1739506701165570)

---

<a id="doc-1739473020978177"></a>
<!-- doc_id: 1739473020978177 -->
<!-- doc_id: 1739473020978177 -->
# Lấy danh sách tài nguyên Smart Creative (Get Smart Creative materials)
> Đường dẫn: API Reference > Smart Creative > Get Smart Creative materials
Sử dụng endpoint này để lấy thông tin các tài nguyên sáng tạo của quảng cáo Smart Creative, bao gồm nút kêu gọi hành động (CTA), văn bản, tên quảng cáo, hình ảnh hoặc tài nguyên video. Đây là endpoint hoàn toàn mới trong phiên bản v1.3.

Phản hồi từ các endpoint [/ad/aco/create/](60-smart-creative.md#doc-1739473063234626) và [/ad/aco/update/](60-smart-creative.md#doc-1739473077112833) là kết quả mô phỏng (mock result) trả về các tham số yêu cầu bạn đã truyền vào, do quá trình xử lý dữ liệu không diễn ra tức thì. Để nhận kết quả thực tế chính xác, vui lòng đợi từ 2 đến 3 giây sau khi gọi endpoint `/ad/aco/create/` hoặc `/ad/aco/update/`, sau đó gọi endpoint `/ad/aco/get/`.
  
## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/ad/aco/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|adgroup_ids ***(Bắt buộc)***|string[]| Danh sách ID nhóm quảng cáo. Số lượng: 1-100.|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok. |
| exclude_field_types_in_response| string[]|Loại trường bạn muốn loại bỏ khỏi phản hồi.<br>Các giá trị enum hỗ trợ: <ul><li>`NULL_FIELD`: Các trường có giá trị null.</li></ul>|

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "adgroup_ids=[\"ADGROUP_IDS\"]" \
https://business-api.tiktok.com/open_api/v1.3/ad/aco/get/
(/code)
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
#|list|object[]|Data list. |
##|advertiser_id|string| ID tài khoản quảng cáo TikTok.|
##|adgroup_id |string| ID nhóm quảng cáo.|
##|media_info_list |object[]| Danh sách thông tin phương tiện truyền thông. |
###|material_id|string|Material ID.|
###|material_operation_status|string|Trạng thái của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (tài nguyên bị vô hiệu hóa).|
###|media_info|object|Media Information.|
####|image_info |object[]| Image information. <ul><li>If the material is a video, the `image_info` will provide details about the video cover image.</li><li>If the material is an image, the `image_info` will provide details about the image material.</li></ul>|
#####|web_uri |string| Image ID. |
#####|file_name |string| Tên hình ảnh bạn đã chỉ định để tạo tên quảng cáo khi tạo quảng cáo Smart Creative qua [/ad/aco/create/](60-smart-creative.md#doc-1739473063234626).<br><br>Nếu không truyền `file_name` trong mảng đối tượng `image_info`, trường này sẽ là chuỗi rỗng.|
####|video_info |object| Chỉ trả về khi tài nguyên là video.<br><br>Thông tin video. |
#####|video_id|string| Video ID. |
#####|file_name |string| Tên video bạn đã chỉ định để tạo tên quảng cáo khi tạo quảng cáo Smart Creative qua [/ad/aco/create/](60-smart-creative.md#doc-1739473063234626).<br><br>Nếu không truyền `file_name` trong đối tượng `video_info`, trường này sẽ là chuỗi rỗng.|
####|aigc_disclosure_type | string | Có bật nút tự khai báo nội dung do AI tạo (AIGC) để chỉ ra quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo sẽ mang nhãn "Nhà quảng cáo đã gắn nhãn là do AI tạo" khi xem toàn màn hình.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: Bật nút để khai báo quảng cáo chứa nội dung do AI tạo.</li><li>`NOT_DECLARED`: Không khai báo nội dung do AI tạo.</li></ul>|
####| tiktok_item_id |string| ID của bài đăng TikTok được sử dụng làm mẫu quảng cáo (Spark Ads). |
####| material_name | string | Tên của tài nguyên (hình ảnh hoặc video). <br><br>`material_name` được dùng để xác định tên hiển thị tài nguyên trong TikTok Ads Manager: <ul><li>Nếu là hình ảnh, tên trong TikTok Ads Manager trùng với giá trị `material_name`.</li><li>Nếu là video, tên trong TikTok Ads Manager là giá trị của `file_name` (khi `file_name` không rỗng) hoặc `material_name` (khi `file_name` rỗng).</li></ul>|
####| identity_id |string| Identity ID.|
####| identity_type |string|Loại danh tính. Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`. Chi tiết xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
##|title_list |object[]|Danh sách tiêu đề quảng cáo (văn bản quảng cáo). Hiển thị cho người xem như một phần của mẫu quảng cáo để truyền tải thông điệp.|
###|title|string|Tiêu đề quảng cáo (văn bản quảng cáo).|
###|material_id|string|Material ID.|
###|material_operation_status|string|Trạng thái của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (tài nguyên bị vô hiệu hóa).|
##|call_to_action_list |object[]|Call-to-action list.|
###|call_to_action|string|Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
##|deeplink_list|object[]| Danh sách liên kết sâu (deeplink).|
###|deeplink|string|Vị trí cụ thể trong ứng dụng mà bạn muốn người dùng chuyển đến nếu đã cài đặt app.|
###|deeplink_type|string|Loại liên kết sâu. Giá trị cho phép phụ thuộc mục tiêu chiến dịch: `NORMAL` (hỗ trợ trong Traffic, Conversion), `DEFERRED_DEEPLINK` (hỗ trợ trong App Install). Mặc định là `NORMAL`. Chiến dịch iOS 14 không thể đặt thành `DEFERRED_DEEPLINK`.|
##|display_name_list|object[]|Display names.|
###|app_name|string|Tên ứng dụng.|
###|landing_page_name|string|Tên trang đích.|
##|avatar_icon_list|object[]|Avatar image information list.|
###|avatar_icon|object|Thông tin ảnh đại diện.|
####|web_uri|string| ID ảnh đại diện.|
##|page_list|object[]|Danh sách ID trang đích.|
###|page_id|string|Page ID.|
##|card_list|object[]|Danh sách ID thẻ tương tác. Giới hạn độ dài: [0,1].|
###|card_id|string|ID Thẻ hiển thị, ID Nhãn dán mã quà tặng, ID Nhãn dán đếm ngược hoặc ID Thẻ tải xuống.|
##|landing_page_urls|string[]|Danh sách URL trang đích.|
###|landing_page_url|string|Đường dẫn URL trang đích.|
##|common_material|object|Tài nguyên dùng chung (Common material).|
###|ad_name|string|Tên quảng cáo.|
###|call_to_action_id|string|ID của danh mục lời kêu gọi hành động (CTA portfolio) mà bạn muốn sử dụng trong quảng cáo. |
###|creative_authorized|boolean|Liệu bạn có cho phép hiển thị một số quảng cáo trong TikTok for Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, giá trị mặc định là `false`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: `creative_authorized` chỉ áp dụng cho quảng cáo video. |
###|playable_url|string|URL tài nguyên chơi thử (Playable).|
###|fallback_type|string|Loại dự phòng. Nếu người xem chưa cài đặt app, bạn có thể chuyển hướng họ đến cài đặt app hoặc mở trang web cụ thể. Các giá trị cho phép: `APP_INSTALL `, `WEBSITE`, `UNSET`. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Không áp dụng cho Deferred Deeplink. |
###|tracking_info|object|Thông tin theo dõi sự kiện (Tracking information).|
####|impression_tracking_urls|string[]|URL theo dõi lượt hiển thị mặc định.|
####| click_tracking_urls|string[]|URL theo dõi lượt nhấp.|
####|tracking_pixel_id|string|ID của TikTok Pixel bạn muốn theo dõi. Bạn có thể sử dụng trường này để đo lường các sự kiện ngoài trang web.|
####|tracking_app_id | string| ID của ứng dụng đang được theo dõi. <br><p><span style="color:darkred"><b>Note</b></span>: Trường này hiện là tính năng danh sách trắng (allowlist) cho các mục tiêu quảng cáo `APP_PROMOTION`, `PRODUCT_SALES` và `ENGAGEMENT`. Nếu bạn muốn truy cập cho ba mục tiêu này, vui lòng liên hệ đại diện TikTok. |
####| tracking_offline_event_set_ids |string[]|Danh sách ID bộ sự kiện ngoại tuyến được theo dõi. <br>See [here](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193) to learn more about how to create and manage Offline Event sets.<br><p><span style="color:darkred"><b>Note</b></span>: Offline Events Tracking is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
###| identity_id|string|ID danh tính khi không sử dụng Spark Ads (`tiktok_item_id`).|
###| identity_type|string|Loại danh tính khi không sử dụng Spark Ads (`tiktok_item_id`). Giá trị duy nhất hỗ trợ là `CUSTOMIZED_USER`. |
###|is_smart_creative|boolean|Liệu tính năng Smart Creative có được bật cho nhóm quảng cáo hay không. |
|request_id |string|Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "list": [
            {
                "open_url": null,
                "title_list": [
                    {
                        "title": "Testing"
                    }
                ],
                "open_url_list": [
                    {
                        "open_url": ""
                    }
                ],
                "app_name": null,
                "avatar_icon_list": null,
                "click_tracking_url": "",
                "landing_page_urls": null,
                "profile_image": null,
                "pixel_id": null,
                "landing_page_url": null,
                "impression_tracking_url": "",
                "page_list": null,
                "external_action": null,
                "call_to_action_list": [],
                "display_name": null,
                "display_name_list": [
                    {
                        "source": "20210531132544123456",
                        "app_name": ""
                    }
                ],
                "ad_id": 1234573413994497,
                "page_id": null,
                "media_info_list": [
                    {
                        "media_info": {
                            "image_info": [
                                {
                                    "file_name": null,
                                    "web_uri": "v0201/aa4785144d3894fcce25033c86123456"
                                }
                            ],
                            "video_info": {
                                "file_name": "12345096e244f1dab24a7e40870cc.MP4",
                                "video_id": "v12345270000bvgsmvthr46s2t1dgm20"
                            },
                            "image_mode": "IMAGE_MODE_VIDEO"
                        }
                    }
                ]
            }
        ]
    },
    "request_id": "xxx"
}
(/code);
```

---

<a id="doc-1739473063234626"></a>
<!-- doc_id: 1739473063234626 -->
<!-- doc_id: 1739473063234626 -->
# Tạo quảng cáo Smart Creative (Create Smart Creative ads)
> Đường dẫn: API Reference > Smart Creative > Create Smart Creative ads
Sử dụng endpoint này để tạo quảng cáo Smart Creative bằng cách tải các tài nguyên sáng tạo cần thiết lên thư viện. Với endpoint này, bạn có thể tải lên nhiều văn bản quảng cáo, tiêu đề, tài nguyên và lời kêu gọi hành động (CTA). Hệ thống sẽ tự động kết hợp các tài nguyên và chuẩn bị phân phối. `ad_id` không được trả về trong phản hồi. Đây là endpoint hoàn toàn mới trong v1.3.

> **Lưu ý:** 
> Quảng cáo ACO không còn được hỗ trợ trong API. Để đảm bảo tích hợp API ổn định, khuyến nghị chuyển sang [Quảng cáo Smart Creative](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1767322784934914).  

## Notes
Bảng dưới đây nêu rõ các lưu ý về dữ liệu trả về, số lượng quảng cáo tối đa, số lượng tài nguyên tối đa, yêu cầu sáng tạo và cài đặt nhóm quảng cáo bắt buộc cho endpoint này, cũng như các mục tiêu quảng cáo được hỗ trợ:
 
| Type  | Details  |
|---|---|---|
| Returned data | Phản hồi của endpoint `/ad/aco/create/` là kết quả mô phỏng (mock result) trả về các tham số yêu cầu bạn đã truyền vào, do việc xử lý dữ liệu không diễn ra tức thì. Để nhận kết quả chính xác thực tế, vui lòng chờ 2 đến 3 giây sau khi gọi `/ad/aco/create/`, rồi sử dụng endpoint [/ad/aco/get/](60-smart-creative.md#doc-1739473020978177). |
| Maximum number of ads | Bạn có thể tạo tối đa 450 quảng cáo Smart Creative cho mỗi lần gọi `/ad/aco/create/`, và tối đa 5.000 quảng cáo cho mỗi tài khoản nhà quảng cáo mỗi ngày. |
| Maximum number of materials | <ul><li>Tiêu đề: 1-5.</li><li>Văn bản kêu gọi hành động (CTA): 1-3.</li><li>Thông tin phương tiện (media info): 1-30.</li><li>ID trang đích (Page ID): 1-3.</li></ul> |
| Creative requirements | Không sử dụng trùng lặp tiêu đề quảng cáo, tài nguyên hoặc văn bản kêu gọi hành động trong cùng một quảng cáo Smart Creative. |
| Supported advertising objectives | Các endpoint Smart Creative chỉ được hỗ trợ khi bạn chọn một trong các Mục tiêu quảng cáo (`objective_type`) sau cho chiến dịch: <ul><li>Quảng bá ứng dụng (<code>APP_PROMOTION</code>)</li><li>Chuyển đổi trên web (<code>WEB_CONVERSIONS</code>)</li><li>Lưu lượng truy cập (<code>TRAFFIC</code>)</li><li>Tìm kiếm khách hàng tiềm năng (<code>LEAD_GENERATION</code>)</li></ul> |

## Quy tắc tạo tên quảng cáo (Ad name generation rules)

* Nếu truyền chuỗi hợp lệ vào trường `ad_name`, và `file_name` trong `image_info` hoặc `video_info` cũng được truyền vào, tên quảng cáo sẽ sinh theo định dạng "adName_" kèm số thứ tự (ví dụ: "adName_001").
* Nếu truyền chuỗi rỗng vào trường `ad_name`, và `file_name` trong `image_info` hoặc `video_info` có truyền vào, tên quảng cáo sẽ sinh theo định dạng "{file_name}_" kèm số thứ tự (ví dụ: "image_001" hoặc "video_002").
* Nếu truyền chuỗi rỗng vào trường `ad_name`, và `file_name` trong `image_info` hoặc `video_info` cũng không truyền vào, tên quảng cáo sẽ sinh theo định dạng "_" kèm số thứ tự (ví dụ: "_001"). Nên tránh trường hợp này để tên quảng cáo có ý nghĩa hơn.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/ad/aco/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
|Content-Type ***(Bắt buộc)***|string|Định dạng dữ liệu yêu cầu<br data-tomark-pass>Allowed format:`"application/json"`  |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok. |
|adgroup_id ***(Bắt buộc)***|string| ID nhóm quảng cáo. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Đây phải là ID của nhóm quảng cáo bạn sẽ bật Smart Creative, và `creative_material_mode` của nhóm quảng cáo phải là `SMART_CREATIVE`.|
|media_info_list***(Bắt buộc)***|object[]|Danh sách thông tin phương tiện truyền thông. <br><br>Kích thước tối đa: 30.|
#|media_info {Required}|object | Material information. |
##|video_info{+Conditional}  |object| Bắt buộc khi loại tài nguyên là video và không truyền `tiktok_item_id`.<br><br>Thông tin video. |
###|video_id {+Conditional} |string| Bắt buộc khi truyền `video_info`.<br><br>ID video. <br><br>Bạn có thể lấy ID video khi tải video lên qua endpoint [/file/video/ad/upload/](71-video.md#doc-1737587322856449). <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Để tích hợp mượt mà, khuyến nghị sử dụng [/file/video/ad/upload/](71-video.md#doc-1737587322856449) (với `upload_type` là `UPLOAD_BY_VIDEO_ID`) để liên kết ID video với ID tài khoản quảng cáo TikTok. |
###|file_name |string| Video name. |
##|image_info{+Conditional} |object[]| Bắt buộc khi loại tài nguyên là hình ảnh hoặc video và không truyền `tiktok_item_id`.<br><br>Thông tin hình ảnh. <ul><li>Khi tải tài nguyên hình ảnh (yêu cầu KHÔNG chứa `video_info`), trường này dùng làm tài nguyên ảnh.</li><li>Khi tải tài nguyên video (yêu cầu có chứa `video_info`), trường này dùng làm ảnh bìa video. Chỉ được gửi 1 ảnh trong mỗi đối tượng `image_info`.</li></ul> |
###|web_uri {+Conditional}|string|Bắt buộc khi truyền `image_info`.<br><br>ID hình ảnh.<br><br>Bạn có thể tìm thấy ID hình ảnh trong phản hồi sau khi tải ảnh lên qua endpoint [/file/image/ad/upload/](47-images.md#doc-1739067433456642). |
###|file_name |string| Tên hình ảnh. Nếu sử dụng tài nguyên hình ảnh, trường này dùng để cấu thành tên quảng cáo.|
##| aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` within `common_material` is `CUSTOMIZED_USER`. <br><br>Có bật nút tự khai báo nội dung do AI tạo (AIGC) để chỉ ra quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo sẽ mang nhãn "Nhà quảng cáo đã gắn nhãn là do AI tạo" khi xem toàn màn hình.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: Bật nút để khai báo quảng cáo chứa nội dung do AI tạo.</li><li>`NOT_DECLARED`: Không khai báo nội dung do AI tạo.</li></ul>Giá trị mặc định: `NOT_DECLARED`.<br><br>Để tìm hiểu các mục tiêu quảng cáo và định dạng quảng cáo hỗ trợ cho nút gạt cùng các bước sử dụng chi tiết, xem [Nút tự khai báo AIGC](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Bạn chỉ có thể cập nhật trường này khi cập nhật video (`video_id`).</li></ul>|
##| tiktok_item_id{+Conditional}|string|Bắt buộc khi không truyền `image_info` và `video_info`.<br><br>ID của bài đăng TikTok được sử dụng làm mẫu quảng cáo (Spark Ads).<br><br> Truyền `tiktok_item_id` nhận được từ phản hồi của các endpoint [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) và [/identity/video/get/](46-identity.md#doc-1740218475032577). <br><br>Khi đã truyền `tiktok_item_id`, bạn không cần truyền các đối tượng `image_info`, `video_info`, và `title_list`. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Khi sử dụng Spark Ads, bạn xác nhận rằng mình có quyền sử dụng âm nhạc trong video cho mục đích thương mại.|
##| identity_id{+Conditional}|string|Bắt buộc khi you use Spark Ads (`tiktok_item_id`).<br><br>Identity ID.|
##| identity_type{+Conditional}|string|Bắt buộc khi sử dụng Spark Ads (`tiktok_item_id`). <br><br>Loại danh tính. <br><br>Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`. <br><br>Chi tiết xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097).|
|title_list|object[]|Danh sách tiêu đề quảng cáo (văn bản quảng cáo). Hiển thị cho người xem như một phần của mẫu quảng cáo để truyền tải thông điệp. <br><br>When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `title_list`.|
#|title {+Conditional}|string|Bắt buộc khi truyền `title_list`.<br><br>Tiêu đề quảng cáo (văn bản quảng cáo). If you don't know how to create effective ad texts, you can try the [Smart Text](38-creative-tools.md#doc-1739084248002626) feature, which generates ad text recommendations based on the industry and language. <ul><li> An ad text must be 12-40 characters long and cannot contain emoji.</li><li>Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. </li></ul>|
|call_to_action_list **(Điều kiện)** |object[]|Danh sách nút kêu gọi hành động (CTA). <br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Đối với quảng cáo TikTok, phải chỉ định trường này hoặc `call_to_action_id`. Nếu chỉ định cả hai, trường này sẽ bị bỏ qua. </li><li>Bạn có thể đưa tối đa ba văn bản kêu gọi hành động (`call_to_action`) trong mỗi đối tượng `call_to_action_list`.</li></ul>|
#|call_to_action {+Conditional} |string|Bắt buộc khi truyền `call_to_action_list`.<br><br>Văn bản kêu gọi hành động. Xem danh sách giá trị enum tại [Phụ lục - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
|deeplink_list|object[]|Danh sách liên kết sâu (deeplink). Length range: [0,1].<br><p><span style="color:darkred"><b>Note</b></span>: Only one `deeplink` and corresponding `deeplink_type`  can be submitted in each `deeplink_list` object.|
#|deeplink|string|Vị trí cụ thể trong ứng dụng mà bạn muốn người dùng chuyển đến nếu đã cài đặt app.|
#|deeplink_type|string|Loại liên kết sâu. Giá trị cho phép phụ thuộc mục tiêu chiến dịch: `NORMAL` (hỗ trợ trong Traffic, Conversion), `DEFERRED_DEEPLINK` (hỗ trợ trong App Install). Mặc định là `NORMAL`. Chiến dịch iOS 14 không thể đặt là `DEFERRED_DEEPLINK`.|
|display_name_list **(Điều kiện)**|object[]|Tên hiển thị. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Bạn chỉ có thể truyền một `app_name` hoặc `landing_page_name` trong mỗi đối tượng `display_name_list`.|
#|app_name {+Conditional}|string| Tên ứng dụng hiển thị trong quảng cáo. Nếu không chỉ định, tên trên app store sẽ được sử dụng. Giới hạn: 1-40 ký tự. Nếu tên trên app store vượt quá 40 ký tự, bạn phải truyền tên ứng dụng mới qua trường này.|
#|landing_page_name {+Conditional}|string|Tên hiển thị của trang đích, bắt buộc khi mục tiêu quảng cáo là trang đích. Giới hạn độ dài: 1-40 ký tự. |
|page_list **(Điều kiện)**|object[]|Danh sách ID trang đích.|
#|page_id  {+Conditional}|string|Bắt buộc khi truyền `page_list`.<br><br>ID trang đích.<br><br><ul><li>Để lấy danh sách trang trong tài khoản quảng cáo, sử dụng [/page/get/](54-page.md#doc-1820826387779586).</li><li>Để tạo trang tức thì, sử dụng [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881).</li></ul>|
|card_list|object[]|Danh sách ID thẻ tương tác. Giới hạn độ dài: [0,1].|
#|card_id|string|ID Thẻ hiển thị, ID Nhãn dán mã quà tặng, ID Nhãn dán đếm ngược hoặc ID Thẻ tải xuống.<ul><li>Để tìm hiểu cách lấy ID Thẻ hiển thị hoặc ID Thẻ tải xuống, xem [Cards](../09-marketing-api/creatives.md#doc-1749019652141058).</li><li>Để tìm hiểu cách lấy ID Nhãn dán đếm ngược, xem [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177).</li></ul>|
|landing_page_urls **(Điều kiện)**|object[]|Nhiều URL trang đích. <br><br>Bạn chỉ có thể truyền một `landing_page_url` vào mỗi đối tượng `landing_page_urls`.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Một khi đã thiết lập, trường này không thể cập nhật.|
#|landing_page_url{+Conditional}|string|Bắt buộc khi `landing_page_urls` is passed.<br><br>Đường dẫn URL trang đích.|
|common_material|object|Tài nguyên dùng chung (Common material).|
#|ad_name|string|Tên quảng cáo. Đặt là " " (chuỗi rỗng) để hệ thống tự động sinh tên. Định dạng tên tự động: tên creative + Thời gian tạo (ví dụ adcreative20210111190739). Giới hạn 512 ký tự và không chứa emoji. Xem mục <strong>"Quy tắc tạo tên quảng cáo"</strong> ở trên. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Mỗi chữ tiếng Trung hoặc tiếng Nhật tính 2 ký tự, mỗi chữ cái tiếng Anh tính 1 ký tự. <br>Nếu không chỉ định tên quảng cáo tại đây, bạn sẽ không thể đổi tên qua endpoint `/ad/aco/update/`.|
#|call_to_action_id|string|ID của danh mục lời kêu gọi hành động (CTA portfolio) mà bạn muốn sử dụng trong quảng cáo. CTA portfolio là nhóm các lời kêu gọi hành động được tự động tối ưu hóa. Chi tiết xem [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu chỉ định cả trường này và `call_to_action_list`, trường `call_to_action_list` sẽ bị bỏ qua. |
#| creative_authorized|boolean|Liệu bạn có cho phép hiển thị một số quảng cáo trong TikTok for Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, giá trị mặc định là `false`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: `creative_authorized` chỉ áp dụng cho quảng cáo video. |
#|playable_url|string|Đường dẫn URL của tư liệu chơi thử (playable), chỉ có hiệu lực với vị trí hiển thị Pangle. Bạn có thể lấy URL qua endpoint [/playable/get/](56-playable-ads.md#doc-1737732758495234). Lưu ý rằng mọi quảng cáo trong cùng nhóm quảng cáo đều dùng chung tài nguyên playable.|
#|fallback_type|string|Loại dự phòng. Nếu khán giả chưa cài app, bạn có thể chuyển hướng họ cài đặt app hoặc mở trang web cụ thể. Giá trị cho phép: `APP_INSTALL `, `WEBSITE`. Nếu chọn website, cần chỉ định URL qua trường `landing_page_urls`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Không áp dụng cho Deferred Deeplink. |
#|tracking_info|object|Thông tin theo dõi sự kiện (Tracking information).|
##|impression_tracking_urls|string[]|URL theo dõi lượt hiển thị mặc định. URL do đối tác dữ liệu tạo ra để theo dõi lượt hiển thị quảng cáo của bạn. Thông thường bạn có thể sao chép URL từ nền tảng của họ. <ul><li> Nếu partner ID của ứng dụng (`app_id` chỉ định ở nhóm quảng cáo) là `44` (TikTok Business SDK) hoặc `49` (TikTok App API), bạn không cần truyền trường này. Nếu truyền, trường này sẽ bị bỏ qua. Bạn có thể lấy partner ID qua `partner_id` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li><li> Nếu tự phân bổ (self-attribution) đã bật cho ứng dụng và partner ID không phải `44` hay `49`, bạn không cần truyền trường này vì trường sẽ mặc định theo URL theo dõi lượt hiển thị bạn đã cấu hình cho App. Bạn có thể kiểm tra xem tự phân bổ đã bật chưa qua `self_attribution_enabled` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li></ul>You can pass in only one URL.|
##| click_tracking_urls|string[]|URL theo dõi lượt nhấp. URL do đối tác dữ liệu tạo ra để theo dõi lượt nhấp quảng cáo của bạn. Thông thường bạn có thể sao chép URL từ nền tảng của họ. <ul><li> Nếu partner ID của ứng dụng (`app_id` chỉ định ở nhóm quảng cáo) là `44` (TikTok Business SDK) hoặc `49` (TikTok App API), bạn không cần truyền trường này. Nếu truyền, trường này sẽ bị bỏ qua. Bạn có thể lấy partner ID qua `partner_id` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li><li> Nếu tự phân bổ (self-attribution) đã bật cho ứng dụng và partner ID không phải `44` hay `49`, bạn không cần truyền trường này vì trường sẽ mặc định theo URL theo dõi lượt nhấp bạn đã cấu hình cho App. Bạn có thể kiểm tra xem tự phân bổ đã bật chưa qua `self_attribution_enabled` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li></ul>Bạn chỉ có thể truyền một URL.<br>Hiện tại Pangle không hỗ trợ DCM, Sizmek hay Flashtalking. |
##|tracking_pixel_id|string| ID của TikTok Pixel bạn muốn theo dõi. Bạn có thể sử dụng trường này để đo lường các sự kiện ngoài trang web. Hỗ trợ mục tiêu chiến dịch cho cả quảng cáo Đấu thầu (`REACH`, `VIDEO_VIEWS`, `TRAFFIC`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, `APP_PROMOTION`, `PRODUCT_SALES`, `ENGAGEMENT`) và Tiếp cận & Tần suất (`RF_REACH`). <ul><li>Với mục tiêu Đấu thầu:<br>Nếu `pixel_id` được chỉ định ở cấp nhóm quảng cáo <strong>và</strong> bạn muốn dùng pixel để theo dõi sự kiện offsite, ID TikTok Pixel truyền trong `tracking_pixel_id` phải trùng với ID ở nhóm quảng cáo. Nếu không, bạn có thể truyền bất kỳ ID Pixel nào muốn theo dõi.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Trường này là tính năng danh sách trắng với các mục tiêu `ENGAGEMENT`/ `PRODUCT_SALES` / `APP_PROMOTION`. Liên hệ đại diện TikTok nếu cần hỗ trợ.</li><li>Với mục tiêu Tiếp cận & Tần suất:<br>Bạn có thể truyền bất kỳ ID TikTok Pixel nào muốn theo dõi trong `tracking_pixel_id`.</li></ul>|
##|tracking_app_id | string| ID của ứng dụng bạn muốn theo dõi. Bạn có thể sử dụng trường này để theo dõi các sự kiện app offsite. <br>Trường này hỗ trợ các mục tiêu cho cả quảng cáo Đấu thầu và Tiếp cận & Tần suất.<br>Nếu `app_id` được chỉ định ở cấp nhóm quảng cáo, ID bạn truyền ở đây phải trùng khớp. Ngược lại, bạn có thể truyền bất kỳ ID ứng dụng nào.<br>Bạn có thể lấy `app_id` qua [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Tính năng danh sách trắng cho `APP_PROMOTION`, `PRODUCT_SALES`, `ENGAGEMENT`. Liên hệ đại diện TikTok nếu cần hỗ trợ. |
##| tracking_offline_event_set_ids |string[]| Danh sách ID bộ sự kiện ngoại tuyến muốn theo dõi. <br>Kích thước tối đa: 50. <br>Xem [tại đây](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193) để biết cách tạo và quản lý bộ sự kiện ngoại tuyến. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Theo dõi sự kiện ngoại tuyến là tính năng danh sách trắng. Liên hệ đại diện TikTok nếu cần hỗ trợ.</li><li>Nếu thuộc danh sách trắng, các bộ sự kiện tự động theo dõi hiện có phải được theo dõi trong quảng cáo mới tạo.</li><li>Hỗ trợ các mục tiêu: `REACH`, `VIDEO_VIEWS`, `TRAFFIC`, `LEAD_GENERATION`, `APP_PROMOTION`, `WEB_CONVERSIONS`, và `ENGAGEMENT`.</li></ul>|
#| identity_id {+Conditional}|string| Bắt buộc khi bạn không dùng Spark Ads (`tiktok_item_id`).<br><br>ID danh tính. |
#| identity_type {+Conditional}|string|Bắt buộc khi bạn không dùng Spark Ads (`tiktok_item_id`).<br><br>Loại danh tính. <br><br>Giá trị duy nhất hỗ trợ: `CUSTOMIZED_USER`.  |
#|is_smart_creative|boolean|Có bật tính năng Smart Creative cho nhóm quảng cáo hay không.<br><br>Giá trị hỗ trợ: `true`.<br><br>Để tìm hiểu cách tạo quảng cáo Smart Creative, xem [Smart Creative](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1767322784934914).|
### Ví dụ lệnh cURL (Example)
``` xcodeblock
(code curl http)
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/aco/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_id": "{{adgroup_id}}",
    "media_info_list": [
        {
            "media_info": {
                "video_info":{
                    "video_id":"{{video_id}}"
                    },
                "image_info":[
                    {"web_uri":"{{web_uri}}"}
                ]
            }
        }
    ],
    "title_list": [
        {
            "title": "{{title}}"
        }
    ],
    "landing_page_urls": [
        {
            "landing_page_url": "{{landing_page_url}}"
        }
    ],
     "common_material": {
        "identity_type": "CUSTOMIZED_USER",
        "identity_id": "{{identity_id}}",
        "call_to_action_id": "{{call_to_action_id}}",
        "is_smart_creative":true
    }
}'
(/code);
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
#|advertiser_id|string| ID tài khoản quảng cáo TikTok.|
#|adgroup_id |string| ID nhóm quảng cáo.|
#|media_info_list |object[]| Danh sách thông tin phương tiện truyền thông. |
##|material_id|string|Material ID.|
##|material_operation_status|string|Trạng thái của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (tài nguyên bị vô hiệu hóa).|
##|media_info|object|Media Information.|
###|image_info |object[]| Image information. |
####|web_uri |string| Image ID. |
####|file_name |string| Image name. |
###|video_info |object| Video information. |
####|video_id|string| Video ID. |
####|file_name |string| Video name. |
###|aigc_disclosure_type | string | Có bật nút tự khai báo nội dung do AI tạo (AIGC) để chỉ ra quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo sẽ mang nhãn "Nhà quảng cáo đã gắn nhãn là do AI tạo" khi xem toàn màn hình.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: Bật nút để khai báo quảng cáo chứa nội dung do AI tạo.</li><li>`NOT_DECLARED`: Không khai báo nội dung do AI tạo.</li></ul>|
###| tiktok_item_id |string| ID của bài đăng TikTok được sử dụng làm mẫu quảng cáo (Spark Ads). |
###| identity_id |string| ID danh tính khi sử dụng Spark Ads (`tiktok_item_id`).|
###| identity_type |string|Loại danh tính khi sử dụng Spark Ads (`tiktok_item_id`). Các giá trị enum: `AUTH_CODE`, `TT_USER`. Chi tiết xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
#|title_list |object[]|Danh sách tiêu đề quảng cáo (văn bản quảng cáo). Hiển thị cho người xem như một phần của mẫu quảng cáo để truyền tải thông điệp.|
##|title|string|Tiêu đề quảng cáo (văn bản quảng cáo).|
#|call_to_action_list |object[]|Call-to-action list.|
##|call_to_action|string|Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#|deeplink_list|object[]| Danh sách liên kết sâu (deeplink).|
##|deeplink|string|Vị trí cụ thể trong ứng dụng mà bạn muốn người dùng chuyển đến nếu đã cài đặt app.|
##|deeplink_type|string|Loại liên kết sâu. Giá trị cho phép phụ thuộc mục tiêu chiến dịch. Allowed values: `NORMAL` (supported in Traffic, Conversion), `DEFERRED_DEEPLINK` (supported in App Install ). For an ad that will be included in an iOS 14 campaign, this field cannot be set to `DEFERRED_DEEPLINK`.|
#|display_name_list|object[]|Display names.|
##|app_name|string|Tên ứng dụng.|
##|landing_page_name|string|Tên trang đích.|
#|page_list|object[]|Danh sách ID trang đích.|
##|page_id|string|Page ID.|
#|card_list|object[]|Danh sách ID thẻ tương tác. Giới hạn độ dài: [0,1].|
##|card_id|string|ID Thẻ hiển thị, ID Nhãn dán mã quà tặng, ID Nhãn dán đếm ngược hoặc ID Thẻ tải xuống.|
#|landing_page_urls|object[]|Danh sách URL trang đích.|
##|landing_page_url|string|Đường dẫn URL trang đích.|
#|common_material|object|Tài nguyên dùng chung (Common material).|
##|ad_name|string|Tên quảng cáo.|
##|call_to_action_id|string|ID của danh mục lời kêu gọi hành động (CTA portfolio) mà bạn muốn sử dụng trong quảng cáo. |
##| creative_authorized|boolean|Liệu bạn có cho phép hiển thị một số quảng cáo trong TikTok for Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, giá trị mặc định là `false`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: `creative_authorized` chỉ áp dụng cho quảng cáo video. |
##|playable_url|string|URL tài nguyên chơi thử (Playable).|
##|fallback_type|string|Loại dự phòng. Nếu người xem chưa cài đặt app, bạn có thể chuyển hướng họ đến cài đặt app hoặc mở trang web cụ thể. Các giá trị cho phép: `APP_INSTALL `, `WEBSITE`, `UNSET`. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Không áp dụng cho Deferred Deeplink. |
##|tracking_info|object|Thông tin theo dõi sự kiện (Tracking information).|
###|impression_tracking_urls|string[]|URL theo dõi lượt hiển thị mặc định.|
###| click_tracking_urls|string[]|URL theo dõi lượt nhấp.|
###|tracking_pixel_id|string|ID của TikTok Pixel được theo dõi.|
###|tracking_app_id | string| ID của ứng dụng được theo dõi. |
###| tracking_offline_event_set_ids |string[]|Danh sách ID bộ sự kiện ngoại tuyến được theo dõi.|
##| identity_id|string|ID danh tính khi không sử dụng Spark Ads (`tiktok_item_id`).|
##| identity_type|string|Loại danh tính khi không sử dụng Spark Ads (`tiktok_item_id`). Giá trị duy nhất hỗ trợ là `CUSTOMIZED_USER`. |
##|is_smart_creative|boolean|Liệu tính năng Smart Creative có được bật cho nhóm quảng cáo hay không. |
|request_id |string|Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "title_list": [
            {
                "title": "{{title}}"
            }
        ],
        "common_material": {
            "call_to_action_id": "{{call_to_action_id}}",
            "identity_id": "{{identity_id}}",
            "is_smart_creative": true,
            "identity_type": "CUSTOMIZED_USER"
        },
        "landing_page_urls": [
            {
                "landing_page_url": "{{landing_page_url}}"
            }
        ],
        "adgroup_id": "{{adgroup_id}}",
        "media_info_list": [
            {
                "media_info": {
                    "video_info": {
                        "video_id": "{{video_id}}"
                    },
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ]
                }
            }
        ],
        "advertiser_id": "{{advertiser_id}}"
    }
}
(/code);
```

---

<a id="doc-1739473077112833"></a>
<!-- doc_id: 1739473077112833 -->
<!-- doc_id: 1739473077112833 -->
# Cập nhật tài nguyên Smart Creative (Update Smart Creative materials)
> Đường dẫn: API Reference > Smart Creative > Update Smart Creative materials
Sử dụng endpoint này để chỉnh sửa tài nguyên sáng tạo của quảng cáo Smart Creative. Bạn có thể sửa đổi nút kêu gọi hành động (CTA), tên quảng cáo, hình ảnh và tài nguyên video. Đây là endpoint hoàn toàn mới trong phiên bản v1.3.

Endpoint này hỗ trợ cập nhật tăng dần. Để sửa đổi cài đặt có thể cập nhật, bạn có thể đặt `patch_update` thành `true` và chỉ truyền trường cần cập nhật cùng các trường bắt buộc, bao gồm tham số Header, `advertiser_id`, và `adgroup_id`.

> **Note:** 
> **Lưu ý:** 
> Nếu bạn muốn cập nhật một hoặc nhiều tham số trong trường kiểu mảng, bất kể có đặt `patch_update` thành `true` hay không, bạn cần truyền lại toàn bộ các tham số ban đầu từ khi tạo quảng cáo Smart Creative trong trường mảng đó kèm theo các giá trị cập nhật. Nếu chỉ truyền một phần, có thể dẫn đến lỗi hoặc làm các tham số không truyền bị ghi đè bằng giá trị mặc định hoặc null. • Ví dụ: Nếu ban đầu bạn truyền `tiktok_item_id`, `identity_id`, và `identity_type` trong `media_info_list` khi tạo quảng cáo và chỉ muốn sửa `tiktok_item_id`, bạn vẫn phải truyền cả ba trường trong `media_info_list`. • Nếu bạn chỉ định nhiều tài nguyên trong `media_info_list` và chỉ muốn sửa một tài nguyên, bạn vẫn phải cung cấp thông tin cho toàn bộ các tài nguyên trong `media_info_list`.

  

## Notes
Bảng dưới đây nêu rõ các lưu ý về dữ liệu trả về, phạm vi cập nhật hỗ trợ, chế độ cập nhật và yêu cầu sáng tạo cho endpoint này:

| Type  | Details  |
|---|---|---|
| Returned data | Phản hồi của endpoint `/ad/aco/update/` là kết quả mô phỏng (mock result) trả về các tham số yêu cầu bạn đã truyền vào, do việc xử lý dữ liệu không diễn ra tức thì. Để lấy kết quả chính xác thực tế, vui lòng chờ 2 đến 3 giây sau khi gọi `/ad/aco/update/`, rồi sử dụng endpoint [/ad/aco/get/](60-smart-creative.md#doc-1739473020978177). |
| Supported update scope | Endpoint `/ad/aco/update/` không hỗ trợ cập nhật tài nguyên sáng tạo của quảng cáo Smart Creative cho Chiến dịch Smart+. Tên quảng cáo sinh tự động không thể chỉnh sửa. |
| Creative requirements | Tránh sử dụng trùng lặp tiêu đề, tài nguyên sáng tạo và nút kêu gọi hành động (CTA). |

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/ad/aco/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type ***(Bắt buộc)***|string|Định dạng dữ liệu yêu cầu<br data-tomark-pass>Allowed format: `"application/json"`  |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok. |
| adgroup_id ***(Bắt buộc)*** | string | ID nhóm quảng cáo. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Truyền ID nhóm quảng cáo đã bật Smart Creative. Cài đặt `creative_material_mode` của nhóm quảng cáo phải là `SMART_CREATIVE`. |
| patch_update | boolean | Có sử dụng chế độ cập nhật tăng dần hay không. <br><br>For example, to update the ad texts by using incremental update mode, configure the following settings only: <ul><li> Set `patch_update` to `true`. </li><li> Set `title_list` to the new ad texts.</li><li> Pass the required fields, including the Header parameters, `advertiser_id`, and `adgroup_id`. </li></ul>|
|media_info_list|object[]|Danh sách thông tin phương tiện truyền thông.|
#|media_info |object | Material information. |
##|video_info  |object| Video information. |
###|video_id {+Conditional}|string| Bắt buộc khi truyền `video_info`.<br><br>ID video. <br><br>Bạn có thể lấy ID video khi tải video lên qua endpoint [/file/video/ad/upload/](71-video.md#doc-1737587322856449).<br><br><p><span style="color:darkred"><b>Note</b></span>: To ensure a smooth integration journey, we recommned that you use [/file/video/ad/upload/](71-video.md#doc-1737587322856449) ( with `upload_type` as `UPLOAD_BY_VIDEO_ID`) to bind video ID with your ID tài khoản quảng cáo TikTok. |
###|file_name |string| Video name. |
##|image_info |object[]|  Thông tin hình ảnh. <ul><li>Khi bạn muốn tải tài nguyên ảnh (`video_info` is NOT included in the request), this field will be used as image materials. </li><li>When you want to upload video materials (`video_info` is included in the request), this field will be used as the video cover. Only one picture can be submitted in each `image_info` object. </li></ul> |
###|web_uri {+Conditional}|string|Bắt buộc khi truyền `image_info`.<br><br>ID hình ảnh. <br><br>Bạn có thể tìm thấy ID hình ảnh trong phản hồi sau khi tải ảnh qua endpoint [/file/image/ad/upload/](47-images.md#doc-1739067433456642). |
###|file_name |string| Tên hình ảnh. Nếu sử dụng tài nguyên hình ảnh, trường này dùng để cấu thành tên quảng cáo.|
##| aigc_disclosure_type | string | Chỉ hợp lệ khi `identity_type` within `common_material` is `CUSTOMIZED_USER`. <br><br>Có bật nút tự khai báo nội dung do AI tạo (AIGC) để chỉ ra quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo sẽ mang nhãn "Nhà quảng cáo đã gắn nhãn là do AI tạo" khi xem toàn màn hình.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: Bật nút để khai báo quảng cáo chứa nội dung do AI tạo.</li><li>`NOT_DECLARED`: Không khai báo nội dung do AI tạo.</li></ul>Giá trị mặc định: `NOT_DECLARED`.<br><br>Để tìm hiểu các mục tiêu quảng cáo và định dạng quảng cáo hỗ trợ cho nút gạt cùng các bước sử dụng chi tiết, xem [Nút tự khai báo AIGC](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Bạn chỉ có thể cập nhật trường này khi cập nhật video (`video_id`).</li></ul>|
##| tiktok_item_id |string|ID của bài đăng TikTok được sử dụng làm mẫu quảng cáo (Spark Ads). <br><br>Pass in the `tiktok_item_id` you get from the response of the [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) and [/identity/video/get/](46-identity.md#doc-1740218475032577) endpoints. <br><br><p><span style="color:darkred"><b>Note</b></span>: By using Spark Ads, you confirm that you have the rights to use the music in the videos for commercial purposes.<br>Once you pass in `tiktok_item_id`, you don't have to pass in the objects `image_info`, `video_info`, and `title_list`.|
##| identity_id |string|ID danh tính cho Spark Ads. |
##| identity_type |string|Loại danh tính cho Spark Ads.<br><br>Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`. Chi tiết xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097).|
|title_list|object[]|Danh sách tiêu đề quảng cáo (văn bản quảng cáo). Hiển thị cho người xem như một phần của mẫu quảng cáo để truyền tải thông điệp.|
#|title{+Conditional}|string|Bắt buộc khi truyền `title_list`.<br><br>Tiêu đề quảng cáo (văn bản quảng cáo). If you don't know how to create effective ad texts, you can try the [Smart Text](38-creative-tools.md#doc-1739084248002626) feature, which generates ad text recommendations based on the industry and language. <ul><li> An ad text must be 12-40 characters long and cannot contain emoji.</li><li>Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. </li></ul>|
|call_to_action_list |object[]|Danh sách nút kêu gọi hành động (CTA). <br><p><span style="color:darkred"><b>Lưu ý</b></span>: You can include at most three call-to-action texts (`call_to_action`) in each `call_to_action_list` object. |
#|call_to_action{+Conditional}|string|Bắt buộc khi truyền `call_to_action_list`.<br><br>Văn bản kêu gọi hành động. Xem danh sách giá trị enum tại [Phụ lục - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
|deeplink_list|object[]|Danh sách liên kết sâu (deeplink). Length range: [0,1].<br><p><span style="color:darkred"><b>Note</b></span>: Only one `deeplink` and corresponding `deeplink_type`  can be submitted in each `deeplink_list` object.|
#|deeplink|string|Vị trí cụ thể trong ứng dụng mà bạn muốn người dùng chuyển đến nếu đã cài đặt app.|
#|deeplink_type|string|Loại liên kết sâu. Giá trị phụ thuộc mục tiêu chiến dịch. Các giá trị enum hỗ trợ: `NORMAL` (supported in Traffic, Conversion), `DEFERRED_DEEPLINK` (supported in App Install). The Giá trị mặc định is `NORMAL`. For an ad that will be included in an iOS 14 campaign, this field cannot be set to `DEFERRED_DEEPLINK`.|
|display_name_list **(Điều kiện)**|object[]|Tên hiển thị. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Bạn chỉ có thể truyền một `app_name` hoặc `landing_page_name` trong mỗi đối tượng `display_name_list`.|
#|app_name {+Conditional}|string| Tên ứng dụng hiển thị trong quảng cáo. Nếu không chỉ định, tên trên app store sẽ được sử dụng. Giới hạn: 1-40 ký tự. Nếu tên trên app store vượt quá 40 ký tự, bạn phải truyền tên ứng dụng mới qua trường này.|
#|landing_page_name|string|Tên hiển thị của trang đích, bắt buộc khi mục tiêu quảng cáo là trang đích. Giới hạn độ dài: 1-40 ký tự. |
|avatar_icon_list|object[]|Danh sách ảnh đại diện.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: When you pass in  `identity_id` in `media_info` or `common_material`, you don't need to pass in this object, and when you do, it'll be ignored. <br>You can only pass in only one avatar image ID (`web_uri`). |
#|avatar_icon|object| Avatar image.|
##|web_uri|string| ID của ảnh đại diện. Có thể tải lên thông qua [Upload an image](47-images.md#doc-1739067433456642) endpoint (picture ratio requirement is 1: 1)|
|page_list|object[]|Danh sách ID trang đích.|
#|page_id{+Conditional}|string|Bắt buộc khi truyền `page_list`.<br><br>ID trang đích.<br><br><ul><li>Để lấy danh sách trang trong tài khoản quảng cáo, sử dụng [/page/get/](54-page.md#doc-1820826387779586).</li><li>Để tạo trang tức thì, sử dụng [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881).</li></ul>|
|card_list|object[]|Danh sách ID thẻ tương tác. Giới hạn độ dài: [0,1].|
#|card_id|string|ID Thẻ hiển thị, ID Nhãn dán mã quà tặng, ID Nhãn dán đếm ngược hoặc ID Thẻ tải xuống.<ul><li>Để tìm hiểu cách lấy ID Thẻ hiển thị hoặc ID Thẻ tải xuống, xem [Cards](../09-marketing-api/creatives.md#doc-1749019652141058).</li><li>Để tìm hiểu cách lấy ID Nhãn dán đếm ngược, xem [Stickers](../09-marketing-api/creatives.md#doc-1749019667506177).</li></ul>|
|common_material|object|Tài nguyên dùng chung (Common material).|
#|ad_name |string|Tên quảng cáo. Đặt là " " (chuỗi rỗng) để hệ thống tự động sinh tên. Định dạng tên quảng cáo sinh tự động is: creative name + Thời gian tạo (e.g. adcreative20210111190739). Character limit is 512 and cannot contain emoji.<br><p><span style="color:darkred"><b>Note</b></span>: Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.<br>If you don't specify ad name here, you will not be able to change the name via `/ad/aco/update/` endpoint.|
#|call_to_action_id|string|ID của danh mục lời kêu gọi hành động (CTA portfolio) mà bạn muốn sử dụng trong quảng cáo. CTA portfolio là nhóm các lời kêu gọi hành động được tự động tối ưu hóa. Chi tiết xem [CTA recommendations > Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu chỉ định cả trường này và `call_to_action_list`, trường `call_to_action_list` sẽ bị bỏ qua. |
#|creative_authorized|boolean|Liệu bạn có cho phép hiển thị một số quảng cáo trong TikTok for Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, giá trị mặc định là `false`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: `creative_authorized` chỉ áp dụng cho quảng cáo video. |
#|playable_url|string|Đường dẫn URL của tư liệu chơi thử (playable), chỉ có hiệu lực với vị trí hiển thị Pangle. Bạn có thể lấy URL qua endpoint [/playable/get/](56-playable-ads.md#doc-1737732758495234). Lưu ý rằng mọi quảng cáo trong cùng nhóm quảng cáo đều dùng chung tài nguyên playable.|
#|fallback_type|string|Loại dự phòng. Nếu khán giả chưa cài app, bạn có thể chuyển hướng họ cài đặt app hoặc mở trang web cụ thể.  Các giá trị enum hỗ trợ: `APP_INSTALL `, `WEBSITE`, `UNSET`. If website is chosen, you need to specify the url via `landing_page_urls` field.<br><p><span style="color:darkred"><b>Note</b></span>: Not applicable for Deferred Deeplink. |
#|tracking_info|object|Thông tin theo dõi sự kiện (Tracking information).|
##|impression_tracking_urls|string[]|URL theo dõi lượt hiển thị mặc định. URL do đối tác dữ liệu tạo ra để theo dõi lượt hiển thị quảng cáo của bạn. Thông thường bạn có thể sao chép URL từ nền tảng của họ. <ul><li> Nếu partner ID của ứng dụng (`app_id` chỉ định ở nhóm quảng cáo) là `44` (TikTok Business SDK) hoặc `49` (TikTok App API), bạn không cần truyền trường này. Nếu truyền, trường này sẽ bị bỏ qua. Bạn có thể lấy partner ID qua `partner_id` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li><li> Nếu tự phân bổ (self-attribution) đã bật cho ứng dụng và partner ID không phải `44` hay `49`, bạn không cần truyền trường này vì trường sẽ mặc định theo URL theo dõi lượt hiển thị bạn đã cấu hình cho App. Bạn có thể kiểm tra xem tự phân bổ đã bật chưa qua `self_attribution_enabled` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li></ul>You can pass in only one URL.|
##| click_tracking_urls|string[]|URL theo dõi lượt nhấp. URL do đối tác dữ liệu tạo ra để theo dõi lượt nhấp quảng cáo của bạn. Thông thường bạn có thể sao chép URL từ nền tảng của họ. <ul><li> Nếu partner ID của ứng dụng (`app_id` chỉ định ở nhóm quảng cáo) là `44` (TikTok Business SDK) hoặc `49` (TikTok App API), bạn không cần truyền trường này. Nếu truyền, trường này sẽ bị bỏ qua. Bạn có thể lấy partner ID qua `partner_id` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li><li> Nếu tự phân bổ (self-attribution) đã bật cho ứng dụng và partner ID không phải `44` hay `49`, bạn không cần truyền trường này vì trường sẽ mặc định theo URL theo dõi lượt nhấp bạn đã cấu hình cho App. Bạn có thể kiểm tra xem tự phân bổ đã bật chưa qua `self_attribution_enabled` trả về từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) hoặc [/app/info/](43-events-1-0-p1.md#doc-1740859272887297).</li></ul>Bạn chỉ có thể truyền một URL.<br>Hiện tại Pangle không hỗ trợ DCM, Sizmek hay Flashtalking.|
##|tracking_pixel_id|string| ID của TikTok Pixel bạn muốn theo dõi. Bạn có thể sử dụng trường này để đo lường các sự kiện ngoài trang web. Trường này hỗ trợ mục tiêu chiến dịch cho cả quảng cáo Đấu thầu (`REACH`, `VIDEO_VIEWS`, `TRAFFIC`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, `APP_PROMOTION`, `PRODUCT_SALES`, `ENGAGEMENT`) and Reach & Frequency ads (`RF_REACH`).<ul><li>For Auction objectives<br>If `pixel_id`is specified at the ad group level <strong>and</strong> you want to use pixel to track offsite events, then the ID TikTok Pixel you pass in the `tracking_pixel_id` field must be the same ID that you specified in the `pixel_id` field for the ad group. Otherwise, you can pass in any ID TikTok Pixel that you'd like to track in the `tracking_pixel_id` field.<br><p><span style="color:darkred"><b>Note</b></span>: This field is an allowlist feature if your campaign objective is `ENGAGEMENT`/ `PRODUCT_SALES` (when `product_source` = `CATALOG` / `STORE` and `shopping_ads_type` = `VIDEO`) /`APP_PROMOTION`(when `app_promotion_type` = `APP_RETARGETING` ). If you want to use the field, please reach out to your TikTok representative.</li><li>For Reach & Frequency objectives <br>You can pass in any ID TikTok Pixel that you'd like to track in the `tracking_pixel_id` field.|
##|tracking_app_id | string| ID của ứng dụng bạn muốn theo dõi. Bạn có thể sử dụng trường này để theo dõi offsite app events. <br>This field supports the campaign objectives for both Auction ads (`REACH`, `VIDEO_VIEWS`, `TRAFFIC`,  `WEB_CONVERSIONS`, `LEAD_GENERATION`, `APP_PROMOTION`, `PRODUCT_SALES`, `ENGAGEMENT`) and Reach & Frequency ads (`RF_REACH`).<br>If `app_id` is specified at the ad group level and you want to track offsite app events, then the application ID you pass via this field must be the same ID that you specified at the ad group level. Otherwise, you can pass in any application ID that you'd like to track via this field.<br>You can get application ID (`app_id`) via [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). <br><p><span style="color:darkred"><b>Note</b></span>: Trường này hiện là tính năng danh sách trắng (allowlist) cho các mục tiêu quảng cáo `APP_PROMOTION`, `PRODUCT_SALES` và `ENGAGEMENT`. Nếu bạn muốn truy cập cho ba mục tiêu này, vui lòng liên hệ đại diện TikTok. Otherwise, you will get an error. |
##| tracking_offline_event_set_ids |string[]| Danh sách ID bộ sự kiện ngoại tuyến bạn muốn theo dõi. Bạn có thể sử dụng trường này để đo lường hoạt động ngoại tuyến từ những người đã xem hoặc tương tác với quảng cáo. <br>Kích thước tối đa: 50. <br>Xem [tại đây](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193) để biết thêm chi tiết về tạo và quản lý bộ sự kiện ngoại tuyến. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Theo dõi sự kiện ngoại tuyến hiện là tính năng danh sách trắng. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ.</li><li>Nếu thuộc danh sách trắng, các bộ sự kiện ngoại tuyến tự động theo dõi hiện có phải được theo dõi trong quảng cáo mới tạo.</li><li>Trường này hỗ trợ các mục tiêu chiến dịch: `REACH`, `VIDEO_VIEWS`, `TRAFFIC`, `LEAD_GENERATION`, `APP_PROMOTION`, `WEB_CONVERSIONS`, và `ENGAGEMENT`.</li></ul>|
#| identity_id{+conditional}|string| Identity ID. Bắt buộc khi you are not using Spark Ads (`tiktok_item_id`).|
#| identity_type{+conditional}|string|Loại danh tính. Bắt buộc khi không dùng Spark Ads (`tiktok_item_id`). Giá trị duy nhất hỗ trợ: `CUSTOMIZED_USER`.  |

### Ví dụ lệnh cURL (Example)
#### Cập nhật một tài nguyên video trong quảng cáo Smart Creative (Update one video creative of a Smart Creative ad)
``` xcodeblock
(code curl http)
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/aco/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_id": "{{adgroup_id}}",
    "patch_update":true,
    "media_info_list": [
        {
            "media_info": {
                "video_info": {
                    "video_id": "{{video_id}}" //updated video
                    },
                    "image_info": [
                        {
                        "web_uri": "{{web_uri}}" //updated video cover
                        }
                    ]
                }
        },
        {   
            "media_info": {
                "video_info": {
                    "video_id": "{{video_id}}" //original video 
                    },
                "image_info": [
                    {
                        "web_uri": "{{web_uri}}" //original video cover
                    }
                ]
            }
        }
    ]
}'
(/code);
```

#### Cập nhật văn bản quảng cáo trong quảng cáo Smart Creative (Update the ad texts of a Smart Creative ad)
``` xcodeblock
(code curl http)
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/aco/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_id": "{{adgroup_id}}",
    "patch_update":true,
    "title_list": [
        {
            "title": "{{title}}",
            "title": "{{title}}"
        }
    ]
}'
(/code);
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
#|advertiser_id|string| ID tài khoản quảng cáo TikTok.|
#|adgroup_id |string| ID nhóm quảng cáo.|
#|media_info_list |object[]| Danh sách thông tin phương tiện truyền thông. |
###|material_id|string|Material ID.|
###|material_operation_status|string|Trạng thái của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (tài nguyên bị vô hiệu hóa).|
###|media_info|object|Media Information.|
####|image_info |object[]| Image information. |
#####|web_uri |string| Image ID. |
#####|file_name |string| Image name. |
####|video_info |object| Video information. |
#####|video_id|string| Video ID. |
#####|file_name |string| Video name. |
####|aigc_disclosure_type | string | Có bật nút tự khai báo nội dung do AI tạo (AIGC) để chỉ ra quảng cáo chứa nội dung do AI tạo hay không. Sau khi bật, quảng cáo sẽ mang nhãn "Nhà quảng cáo đã gắn nhãn là do AI tạo" khi xem toàn màn hình.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: Bật nút để khai báo quảng cáo chứa nội dung do AI tạo.</li><li>`NOT_DECLARED`: Không khai báo nội dung do AI tạo.</li></ul>|
####| tiktok_item_id |string| ID của bài đăng TikTok được sử dụng làm mẫu quảng cáo (Spark Ads). |
####| identity_id |string|ID danh tính khi sử dụng Spark Ads (`tiktok_item_id`).|
####| identity_type |string|Loại danh tính khi sử dụng Spark Ads (`tiktok_item_id`). Các giá trị enum: `AUTH_CODE`, `TT_USER`. Chi tiết xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
#|title_list |object[]|Danh sách tiêu đề quảng cáo (văn bản quảng cáo). Hiển thị cho người xem như một phần của mẫu quảng cáo để truyền tải thông điệp.|
##|title|string|Tiêu đề quảng cáo (văn bản quảng cáo).|
#|call_to_action_list |object[]|Call-to-action list.|
##|call_to_action|string|Call-to-action text. Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#|deeplink_list|object[]| Danh sách liên kết sâu (deeplink).|
##|deeplink|string|Vị trí cụ thể trong ứng dụng mà bạn muốn người dùng chuyển đến nếu đã cài đặt app.|
##|deeplink_type|string|Loại liên kết sâu. Giá trị phụ thuộc mục tiêu chiến dịch: `NORMAL` (hỗ trợ trong Traffic, Conversion), `DEFERRED_DEEPLINK` (hỗ trợ trong App Install). Mặc định là `NORMAL`. Chiến dịch iOS 14 không thể đặt thành `DEFERRED_DEEPLINK`.|
#|display_name_list|object[]|Display names.|
##|app_name|string|Tên ứng dụng.|
##|landing_page_name|string|Tên trang đích.|
#|avatar_icon|object|Thông tin ảnh đại diện.|
##|web_uri|string| ID ảnh đại diện.|
#|page_list|object[]|Danh sách ID trang đích.|
##|page_id|string|Page ID.|
#|card_list|object[]|Danh sách ID thẻ tương tác. Giới hạn độ dài: [0,1].|
##|card_id|string|ID Thẻ hiển thị, ID Nhãn dán mã quà tặng, ID Nhãn dán đếm ngược hoặc ID Thẻ tải xuống.|
#|landing_page_urls|object[]|Danh sách URL trang đích.|
##|landing_page_url|string|Đường dẫn URL trang đích.|
#|common_material|object|Tài nguyên dùng chung (Common material).|
##|ad_name|string|Tên quảng cáo.|
##|call_to_action_id|string|ID của danh mục lời kêu gọi hành động (CTA portfolio) mà bạn muốn sử dụng trong quảng cáo. |
##|creative_authorized|boolean|Liệu bạn có cho phép hiển thị một số quảng cáo trong TikTok for Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, giá trị mặc định là `false`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: `creative_authorized` chỉ áp dụng cho quảng cáo video. |
##|playable_url|string|URL tài nguyên chơi thử (Playable).|
##|fallback_type|string|Loại dự phòng. Nếu người xem chưa cài đặt app, bạn có thể chuyển hướng họ đến cài đặt app hoặc mở trang web cụ thể. Các giá trị enum: `APP_INSTALL`, `WEBSITE`, `UNSET`.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Không áp dụng cho Deferred Deeplink. |
##|tracking_info|object|Thông tin theo dõi sự kiện (Tracking information).|
###|impression_tracking_urls|string[]|URL theo dõi lượt hiển thị mặc định.|
###| click_tracking_urls|string[]|URL theo dõi lượt nhấp.|
###|tracking_pixel_id|string|ID của TikTok Pixel được theo dõi. Bạn có thể sử dụng trường này để đo lường các sự kiện ngoài trang web.|
###|tracking_app_id | string| ID của ứng dụng được theo dõi. |
###| tracking_offline_event_set_ids |string[]|Danh sách ID bộ sự kiện ngoại tuyến được theo dõi.|
##| identity_id|string|ID danh tính khi không sử dụng Spark Ads (`tiktok_item_id`).|
##| identity_type|string|Loại danh tính khi không sử dụng Spark Ads (`tiktok_item_id`). Giá trị duy nhất hỗ trợ là `CUSTOMIZED_USER`. |
##|is_smart_creative|boolean|Liệu tính năng Smart Creative có được bật cho nhóm quảng cáo hay không.  |
|request_id |string|Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |

### Ví dụ lệnh cURL (Example)
#### Cập nhật một tài nguyên video trong quảng cáo Smart Creative (Update one video creative of a Smart Creative ad)
``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "call_to_action_list": [],
        "deeplink_list": [
            {
                "deeplink_type": "NORMAL",
                "deeplink": ""
            }
        ],
        "media_info_list": [
            {
                "media_info": {
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "video_info": {
                        "video_id": "{{video_id}}"
                    }
                }
            },
            {
                "media_info": {
                    "image_info": [
                        {
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "video_info": {
                        "video_id": "{{video_id}}"
                    }
                }
            }
        ],
        "advertiser_id": "{{advertiser_id}}",
        "common_material": {
            "fallback_type": null,
            "tracking_info": {
                "click_tracking_urls": [],
                "tracking_app_id": null,
                "tracking_offline_event_set_ids": [
                    "{{tracking_offline_event_set_ids}}",
                    "{{tracking_offline_event_set_ids}}"
                ],
                "impression_tracking_urls": [],
                "vast_moat_enabled": false,
                "tracking_pixel_id": "0"
            },
            "identity_type": "CUSTOMIZED_USER",
            "is_smart_creative": true,
            "creative_authorized": false,
            "call_to_action_id": "{{call_to_action_id}}",
            "playable_url": "",
            "identity_id": "{{identity_id}}",
            "ad_name": null
        },
        "card_list": null,
        "avatar_icon_list": [
            {
                "avatar_icon": {
                    "web_uri": "{{web_uri}}"
                }
            }
        ],
        "adgroup_id": "{{adgroup_id}}",
        "display_name_list": [
            {
                "app_name": "",
                "landing_page_name": "{{landing_page_name}}"
            }
        ],
        "title_list": [
            {
                "material_operation_status": "ENABLE",
                "title": "{{title}}",
                "material_id": "{{material_id}}"
            }
        ],
        "landing_page_urls": [
            {
                "landing_page_url": "{{landing_page_url}}"
            }
        ],
        "page_list": null
    }
}'
(/code);
```
#### Cập nhật văn bản quảng cáo trong quảng cáo Smart Creative (Update the ad texts of a Smart Creative ad)
``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "landing_page_urls": [
            {
                "landing_page_url": "{{landing_page_url}}"
            }
        ],
        "call_to_action_list": [],
        "media_info_list": [
            {
                "media_info": {
                    "image_info": [
                        {
                            "file_name": null,
                            "web_uri": "{{web_uri}}"
                        }
                    ],
                    "aigc_disclosure_type": null,
                    "tiktok_item_id": null,
                    "identity_id": null,
                    "identity_type": null,
                    "material_name": "",
                    "video_info": {
                        "file_name": "",
                        "video_id": "{{video_id}}"
                    }
                }
            }
        ],
        "card_list": null,
        "title_list": [
            {
                "title": "{{title}}",
                "title": "{{title}}"
            }
        ],
        "adgroup_id": "{{adgroup_id}}",
        "advertiser_id": "{{advertiser_id}}",
        "avatar_icon_list": [
            {
                "avatar_icon": {
                    "web_uri": "{{web_uri}}"
                }
            }
        ],
        "display_name_list": [
            {
                "app_name": "",
                "landing_page_name": "{{landing_page_name}}"
            }
        ],
        "common_material": {
            "fallback_type": null,
            "is_smart_creative": true,
            "creative_authorized": false,
            "playable_url": "",
            "identity_id": "{{identity_id}}",
            "tracking_info": {
                "tracking_app_id": null,
                "impression_tracking_urls": [],
                "click_tracking_urls": [],
                "tracking_pixel_id": "0",
                "vast_moat_enabled": false,
                "tracking_offline_event_set_ids": [
                    "{{tracking_offline_event_set_id}}",
                    "{{tracking_offline_event_set_id}}"
                ]
            },
            "call_to_action_id": "{{call_to_action_id}}",
            "identity_type": "CUSTOMIZED_USER",
            "ad_name": null
        },
        "deeplink_list": [
            {
                "deeplink_type": "NORMAL",
                "deeplink": ""
            }
        ],
        "page_list": null
    }
}'
(/code);
```

---

<a id="doc-1739506701165570"></a>
<!-- doc_id: 1739506701165570 -->
<!-- doc_id: 1739506701165570 -->
# Cập nhật trạng thái tài nguyên Smart Creative (Update the statuses of Smart Creative materials)
> Đường dẫn: API Reference > Smart Creative > Update the statuses of Smart Creative materials
Sử dụng endpoint này để cập nhật trạng thái hoạt động của các tài nguyên sáng tạo trong quảng cáo Smart Creative, bao gồm văn bản quảng cáo, hình ảnh và video. Đây là endpoint hoàn toàn mới trong phiên bản v1.3.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/ad/aco/material_status/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type ***(Bắt buộc)***|string|Định dạng dữ liệu yêu cầu<br data-tomark-pass>Allowed format: `"application/json"`  |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok. |
| ad_group_id ***(Bắt buộc)*** | string | ID nhóm quảng cáo. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Truyền ID nhóm quảng cáo đã bật Smart Creative. Cài đặt `creative_material_mode` của nhóm quảng cáo phải là `SMART_CREATIVE`. |
| material_ids ***(Bắt buộc)*** | string[] | Danh sách ID tài nguyên. Bạn chỉ có thể truyền một ID tài nguyên duy nhất. |
| material_status ***(Bắt buộc)*** | string | Trạng thái mới của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (vô hiệu hóa tài nguyên). |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/aco/material_status/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "ad_group_id": "{{ad_group_id}}",
    "material_ids": ["{{material_id}}"],
    "material_status": "DISABLE"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|data |object|Returned data.  |
#|ad_group_id |string| Danh sách ID nhóm quảng cáo. Số lượng: 1-100.|
#|material_ids |string[]| Material IDs.|
#|material_status|string| Trạng thái của tài nguyên. Các giá trị enum hỗ trợ: `ENABLE` (tài nguyên có thể sử dụng), `DISABLE` (tài nguyên bị vô hiệu hóa).|
|request_id |string|Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "material_ids": [
            "{{material_id}}"
        ],
        "ad_group_id": "{{ad_group_id}}",
        "material_status": "DISABLE"
    }
}
(/code);
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart Creative**:

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

