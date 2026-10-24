# Báo cáo creative (Creative Reports)

> Phân hệ: apiref:Creative Reports.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Báo cáo tài sản sáng tạo (Creative Reports) (#doc-1749092271949826)](#doc-1749092271949826)
- [2. Báo cáo cơ bản về tài sản sáng tạo (Creative basic reports) (#doc-1740662135093314)](#doc-1740662135093314)
- [3. Các chỉ số được hỗ trợ trong báo cáo cơ bản về creative (#doc-1861363088053250)](#doc-1861363088053250)
- [4. Báo cáo thông tin chi tiết video (Video Insights reports) (#doc-1789700050715650)](#doc-1789700050715650)
- [5. Các chỉ số được hỗ trợ trong báo cáo Video Insights (#doc-1789703614085122)](#doc-1789703614085122)
- [6. Thông tin chuyên sâu về tài sản sáng tạo (Creative Insights) (#doc-1738824477276162)](#doc-1738824477276162)
- [7. Lấy điểm chuẩn quảng cáo (Get ad benchmarks) (#doc-1738824501176321)](#doc-1738824501176321)
- [8. Lấy hiệu suất theo từng giây (Get in-second performance) (#doc-1738825259075586)](#doc-1738825259075586)

---

<a id="doc-1749092271949826"></a>
<!-- doc_id: 1749092271949826 -->
<!-- doc_id: 1749092271949826 -->
# Báo cáo tài sản sáng tạo (Creative Reports)
> Đường dẫn: API Reference > Creative Reports
Báo cáo ở cấp độ tài sản sáng tạo (creative asset) là điều thiết yếu để hiểu cách tài sản sáng tạo của nhà quảng cáo tương tác và tạo sự cộng hưởng với đối tượng mục tiêu. Thông tin này sau đó có thể được sử dụng để cải thiện các nội dung sáng tạo trong tương lai và tinh chỉnh đối tượng mục tiêu.

Nhóm này bao gồm các bộ endpoint sau: 
- [Creative basic reports](37-creative-reports.md#doc-1740662135093314): Giúp bạn lấy các chỉ số hiệu suất cơ bản ở cấp độ tài sản sáng tạo cũng như các thuộc tính của tài sản sáng tạo như chiều cao và chiều rộng cho các quảng cáo không phải Spark Ads (non-Spark Ads) trong một tài khoản quảng cáo.
- [Video Insights reports](37-creative-reports.md#doc-1789700050715650): Hiển thị dữ liệu hiệu suất của nhiều video trên một hoặc nhiều tài khoản quảng cáo, bao gồm cả Spark Ads và non-Spark Ads.
- [Creative insights](37-creative-reports.md#doc-1738824477276162): Sử dụng các thông tin chuyên sâu về dữ liệu để tạo ra quảng cáo TikTok đạt hiệu quả cao nhất.

---

<a id="doc-1740662135093314"></a>
<!-- doc_id: 1740662135093314 -->
<!-- doc_id: 1740662135093314 -->
# Báo cáo cơ bản về tài sản sáng tạo (Creative basic reports)
> Đường dẫn: API Reference > Creative Reports > Creative basic reports
# Chạy báo cáo cơ bản về tài sản sáng tạo (Run a creative basic report)
Sử dụng endpoint này để chạy báo cáo cơ bản về các tài sản sáng tạo (creative assets).

> **Lưu ý:** 
> Báo cáo cơ bản về tài sản sáng tạo bao gồm dữ liệu của cả tài sản sáng tạo chưa bị xóa và đã bị xóa.

## Điều kiện tiên quyết trước khi bắt đầu
Tạo quảng cáo hoặc chiến dịch bằng [/ad/create/](02-ads-p1.md#doc-1739953377508354), [/ad/aco/create/](60-smart-creative.md#doc-1739473063234626), hoặc [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) để đảm bảo dữ liệu chi phí được tạo ở cấp độ tài sản sáng tạo. Nếu bạn chưa tạo bất kỳ quảng cáo hoặc chiến dịch nào, hoặc nếu quảng cáo/chiến dịch của bạn chưa phát sinh chi phí, bạn có thể nhận được kết quả rỗng.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/report/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)***| string| Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
| Content-Type ***(Bắt buộc)*** | string | Loại nội dung của yêu cầu (Request content type). <br>Giá trị chấp nhận: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok |
| material_type ***(Bắt buộc)*** | string | Loại tài sản sáng tạo. Các giá trị enum hỗ trợ: `VIDEO`, `IMAGE`, `INSTANT_PAGE`. |
| lifetime | boolean | Có thực hiện truy vấn toàn bộ dữ liệu lịch sử hay không. <br><br>Nếu trường này được đặt thành `true`, bạn không cần chỉ định `start_date` và `end_date`. <br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>Giá trị mặc định: `false`. |
| start_date **(Điều kiện)** | string | Bắt buộc khi `lifetime` được đặt thành `false`. <br><br>Thời gian bắt đầu, khoảng đóng. Định dạng: `YYYY-MM-DD`, ví dụ: 2020-01-01 (theo múi giờ của nhà quảng cáo). |
| end_date **(Điều kiện)** | string | Bắt buộc khi `lifetime` được đặt thành `false`. <br><br>Thời gian kết thúc, khoảng đóng. Định dạng: `YYYY-MM-DD`, ví dụ: 2020-01-01 (theo múi giờ của nhà quảng cáo). |
| info_fields | string[] | Thông tin bạn muốn nhận về tài sản sáng tạo. Giá trị mặc định là [`material_id`, `video_id`, `image_id`, `page_id`]. Giá trị cho phép: Tất cả các trường dữ liệu hiển thị trong mục `info` của dữ liệu phản hồi. |
| metrics_fields | string[] | Dữ liệu chỉ số hoặc thứ nguyên bạn cần. Giá trị mặc định là: [`impressions`, `spend`]. Phạm vi giá trị: tất cả các trường trong mục `metrics` của phản hồi. |
| filtering | object | Điều kiện lọc dữ liệu |
#| material_id | string[] | ID tài sản sáng tạo. Bạn có thể chỉ định tối đa 10 ID tài sản sáng tạo để lọc kết quả. |
#| material_name | string | Tên tài sản sáng tạo. Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| ad_name | string | Tên quảng cáo. Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| ad_id | string[] | Danh sách ID quảng cáo bạn muốn lọc. Hỗ trợ truy vấn hàng loạt. |
#| adgroup_name | string | Tên nhóm quảng cáo bạn muốn lọc. Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| adgroup_id | string[] | Danh sách ID nhóm quảng cáo bạn muốn lọc. Hỗ trợ truy vấn hàng loạt. |
#| campaign_name | string | Tên chiến dịch bạn muốn lọc. Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| campaign_id | string[] | Danh sách ID chiến dịch bạn muốn lọc. Hỗ trợ truy vấn hàng loạt. |
#| country_code | string[] | Danh sách mã vị trí địa lý bạn muốn lọc. Để xem danh sách giá trị enum, xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
#| placement | list | Danh sách vị trí hiển thị quảng cáo bạn muốn lọc. Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#| page_id | string[] | Danh sách ID trang tức thì (Instant page ID). |
#| page_status | string[] | Trạng thái trang tức thì. Các giá trị enum hỗ trợ: `DRAFT`, `READY`. |
#| page_biz_type | string[] | Loại hình kinh doanh của trang tức thì. Các giá trị enum hỗ trợ: `CUSTOM`, `APP_PROFILE`, `INSTANT_FORM`. |
#| page_template_type | string[] | Các loại mẫu trang tức thì. Khi `page_biz_type` bao gồm `CUSTOM`, các giá trị cho phép là <ul><li>`CUSTOMIZED`</li><li>`INTRODUCTION`</li><li>`BRAND_STORY`</li><li>`SALES_PRODUCT`</li><li>`MOVIE_TRAILER`</li></ul><p>Khi `page_biz_type` bao gồm `INSTANT_FORM`, các giá trị enum là `NORMAL_FORM` và `ADVANCED_FORM`.</p> |
#| app_profile_country | string[] | Mã quốc gia hoặc khu vực mà trang tức thì được triển khai. Có hiệu lực khi `instant_page_biz_type` bao gồm `APP_PROFILE`. |
#| app_profile_external_app_id | string[] | ID ứng dụng mà trang tức thì chuyển hướng đến. Có hiệu lực khi `instant_page_biz_type` bao gồm `APP_PROFILE`. |
#| customized_page_external_action | string[] | Các sự kiện chuyển đổi dành riêng cho trang tức thì TikTok. Danh sách giá trị enum xem tại: [Phụ lục - Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
#| spend | object | Khoảng tổng chi phí |
##| min | float | Giá trị tối thiểu, khoảng mở. Để trống nghĩa là không giới hạn giá trị tối thiểu. |
##| max | float | Giá trị tối đa, khoảng mở. Để trống nghĩa là không giới hạn giá trị tối đa. |
#| conversion | object | Giá trị chuyển đổi |
##| min | float | Giá trị tối thiểu, khoảng mở. Nếu không chỉ định, không giới hạn giá trị tối thiểu. |
##| max | float | Giá trị tối đa, khoảng mở. Nếu không chỉ định, không giới hạn giá trị tối đa. |
| sort_field | string | Trường dùng để sắp xếp. Hỗ trợ sắp xếp theo thời gian tạo của tài sản sáng tạo và tất cả các dữ liệu chỉ số. Mặc định không sắp xếp. |
| sort_type | string | Thứ tự sắp xếp kết quả. Các giá trị enum hỗ trợ: `ASC`, `DESC`. Giá trị mặc định: `DESC`. |
| page | number | Số trang hiện tại cần lấy dữ liệu. Giá trị mặc định: 1, phạm vi: ≥ 1. |
| page_size | number | Kích thước trang (số lượng kết quả mỗi trang). Giá trị mặc định: 10, phạm vi: 1-1000. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/creative/report/get/?advertiser_id={{advertiser_id}}&material_type=VIDEO&lifetime=false&start_date=2023-01-01&end_date=2023-08-01&info_fields=["material_id", "video_id", "image_id","page_id"]&metrics_fields=["spend","impressions","clicks"]&page=1&page_size=10' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Để biết chi tiết, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
#| list | object[] | Thông tin báo cáo |
##| info | object | Thông tin tài sản sáng tạo |
###| material_id | string | ID tài sản sáng tạo |
###| video_id | string | ID video |
###| image_id | string | ID hình ảnh |
###| source | string | Nguồn của tài sản sáng tạo. Để xem danh sách giá trị enum, xem [Enumeration - Material Source](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
###| country_code | string[] | Mã quốc gia hoặc khu vực. Để xem danh sách giá trị enum, xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
###| placement | string[] | Vị trí hiển thị. Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
###| num_ads | number | Số lượng quảng cáo. |
###| total_active_days | number | Tổng số ngày hoạt động. Một ngày hoạt động là ngày có phát sinh chi tiêu (`spend` > 0). Trường này chỉ hỗ trợ tài sản sáng tạo loại `VIDEO`. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: </p><ul><li>Chỉ số này chỉ được hỗ trợ khi `lifetime` được đặt thành `false` trong yêu cầu.</li><li>Khi `lifetime` được đặt thành `true` trong yêu cầu, giá trị của trường này sẽ là 0.</li></ul> |
###| related_ad_ids | string[] | Danh sách ID của các quảng cáo liên quan. Trường này chỉ hỗ trợ tài sản sáng tạo loại `VIDEO`. |
###| adgroup_number | number | Số lượng nhóm quảng cáo liên quan. Trường này chỉ hỗ trợ tài sản sáng tạo loại `VIDEO`. |
###| related_adgroup_ids | string[] | Danh sách ID của các nhóm quảng cáo liên quan. Trường này chỉ hỗ trợ tài sản sáng tạo loại `VIDEO`. |
###| page_id | string | ID trang tức thì. |
###| page_status | string | Trạng thái trang tức thì. Các giá trị enum hỗ trợ: `DRAFT`, `READY`. |
###| page_biz_type | string[] | Loại hình kinh doanh của trang tức thì. Các giá trị enum hỗ trợ: `CUSTOM`, `APP_PROFILE`, `INSTANT_FORM`. |
###| page_template_type | string[] | Các loại mẫu trang tức thì. Khi `page_biz_type` bao gồm `CUSTOM`, các giá trị cho phép là <ul><li>`CUSTOMIZED`</li><li>`INTRODUCTION`</li><li>`BRAND_STORY`</li><li>`SALES_PRODUCT`</li><li>`MOVIE_TRAILER`</li></ul>Khi `page_biz_type` bao gồm `INSTANT_FORM`, các giá trị cho phép là `NORMAL_FORM` và `ADVANCED_FORM`. |
###| page_thumbnail | string | Liên kết đến ảnh thu nhỏ của trang. |
###| app_profile_country | string[] | Mã quốc gia hoặc khu vực mà trang tức thì được triển khai. Hợp lệ khi `instant_page_biz_type` bao gồm `APP_PROFILE`. |
###| app_profile_external_app_id | string[] | ID ứng dụng mà trang tức thì chuyển hướng đến. Có hiệu lực khi `instant_page_biz_type` bao gồm `APP_PROFILE`. |
###| app_profile_icon | string | Biểu tượng ứng dụng. |
###| customized_page_external_action | string[] | Các sự kiện chuyển đổi dành riêng cho trang tức thì tùy chỉnh. |
##| metrics | object | Dữ liệu chỉ số. Vui lòng xem [Bảng chỉ số](37-creative-reports.md#doc-1861363088053250) để biết chi tiết. |
#| page_info | object | Thông tin phân trang |
##| page | number | Số trang hiện tại cần lấy dữ liệu |
##| page_size | number | Kích thước trang (số kết quả mỗi trang) |
##| total_number | number | Tổng số kết quả |
##| total_page | number | Tổng số trang |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "metrics": {
                    "clicks": "0",
                    "impressions": "0",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "clicks": "17",
                    "impressions": "30",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "clicks": "0",
                    "impressions": "0",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "spend": "0",
                    "clicks": "0",
                    "impressions": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "spend": "0",
                    "clicks": "3",
                    "impressions": "3"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "clicks": "0",
                    "impressions": "0",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "clicks": "0",
                    "impressions": "0",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "clicks": "0",
                    "impressions": "0",
                    "spend": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "impressions": "11",
                    "spend": "0",
                    "clicks": "1"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "spend": "0",
                    "clicks": "0",
                    "impressions": "0"
                },
                "info": {
                    "page_id": null,
                    "image_id": null,
                    "video_id": "{{video_id}}",
                    "material_id": "{{material_id}}"
                }
            }
        ],
        "page_info": {
            "total_number": 560,
            "total_page": 56,
            "page_size": 10,
            "page": 1
        }
    }
}
(/code);
```

---

<a id="doc-1861363088053250"></a>
<!-- doc_id: 1861363088053250 -->
<!-- doc_id: 1861363088053250 -->
# Các chỉ số được hỗ trợ trong báo cáo cơ bản về creative (Supported metrics in creative basic reports)
> Đường dẫn: API Reference > Creative Reports > Creative basic reports > Supported metrics in creative basic reports
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| spend | string | Ước tính tổng số tiền bạn đã chi tiêu cho chiến dịch, nhóm quảng cáo hoặc quảng cáo trong thời gian phát. Đơn vị tiền tệ phụ thuộc vào tài khoản nhà quảng cáo của bạn. |
| cpc | string | Chi phí trung bình bạn đã trả cho mỗi lượt nhấp (CPC). |
| cpm | string | Chi phí trung bình bạn đã trả cho mỗi 1.000 lượt hiển thị (CPM). |
| impressions | string | Số lần quảng cáo của bạn xuất hiện trên màn hình (Lượt hiển thị). |
| clicks | string | Số lượt nhấp vào quảng cáo của bạn. |
| ctr | string | Tỷ lệ phần trăm số lần mọi người nhìn thấy quảng cáo của bạn và thực hiện nhấp chuột (CTR). |
| conversion | string | Số lần quảng cáo đạt được kết quả, dựa trên mục tiêu phụ bạn đã chọn. Vì một chiến dịch có thể có nhiều mục tiêu phụ khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. Vui lòng vào cấp nhóm quảng cáo hoặc quảng cáo để xem. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| cost_per_conversion | string | Số tiền trung bình bạn đã chi cho mỗi lượt chuyển đổi. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| conversion_rate | string | Tỷ lệ phần trăm kết quả bạn nhận được trên tổng số lượt nhấp vào quảng cáo. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| real_time_conversion | string | Số lần quảng cáo đạt được kết quả theo thời gian thực, dựa trên mục tiêu và cài đặt bạn đã chọn. (Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra). |
| real_time_cost_per_conversion | string | Số tiền trung bình bạn đã chi cho mỗi lượt chuyển đổi theo thời gian thực. (Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra). |
| real_time_conversion_rate | string | Tỷ lệ phần trăm kết quả bạn nhận được trên tổng số lượt nhấp vào quảng cáo theo thời gian thực. (Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra). |
| video_play_actions | string | Số lần video của bạn bắt đầu phát. Không tính lượt phát lại. |
| video_watched_2s | string | Số lần video của bạn được phát ít nhất 2 giây. Không tính lượt phát lại. |
| video_watched_6s | string | Số lần video của bạn được phát ít nhất 6 giây, hoặc được phát hết toàn bộ. Không tính lượt phát lại. |
| average_video_play | string | Thời gian xem video trung bình trên mỗi lượt xem video đơn lẻ, bao gồm cả thời gian xem lại video. |
| video_views_p25 | string | Số lần video của bạn được phát đến 25% thời lượng. Không tính lượt phát lại. |
| video_views_p50 | string | Số lần video của bạn được phát đến 50% thời lượng. Không tính lượt phát lại. |
| video_views_p75 | string | Số lần video của bạn được phát đến 75% thời lượng. Không tính lượt phát lại. |
| video_views_p100 | string | Số lần video của bạn được phát đến 100% thời lượng. Không tính lượt phát lại. |
| real_time_app_install | string | Số lần ứng dụng di động được cài đặt được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra). |
| real_time_app_install_cost | string | Chi phí trung bình cho mỗi sự kiện cài đặt ứng dụng. (Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra). |
| app_install | string | Số lần ứng dụng di động được cài đặt được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| cost_per_app_install | string | Chi phí trung bình cho mỗi sự kiện cài đặt ứng dụng. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| registration | string | Số lượt registrations duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_registration | string | Chi phí trung bình cho mỗi sự kiện registration duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| registration_rate | string | Tỷ lệ phần trăm các sự kiện registration duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| purchase | string | Số sự kiện mua hàng (purchase) duy nhất diễn ra trong ứng dụng của bạn được ghi nhận bởi đối tác đo lường. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| cost_per_purchase | string | Chi phí trung bình của mỗi sự kiện mua hàng duy nhất. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| purchase_rate | string | Tỷ lệ phần trăm các sự kiện mua hàng duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tổng số được tính dựa trên thời điểm mỗi lượt hiển thị quảng cáo diễn ra). |
| app_event_add_to_cart | string | Số lượt times a user added items to a shopping cart duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_app_event_add_to_cart | string | Chi phí trung bình cho mỗi sự kiện add to cart event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| app_event_add_to_cart_rate | string | Tỷ lệ phần trăm các sự kiện add to cart duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| checkout | string | Số lượt times a user made a checkout duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_checkout | string | Chi phí trung bình cho mỗi sự kiện checkout event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| checkout_rate | string | Tỷ lệ phần trăm các sự kiện checkout duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| view_content | string | Số lượt times a user viewed content duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_view_content | string | Chi phí trung bình cho mỗi sự kiện view content event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| view_content_rate | string | Tỷ lệ phần trăm các sự kiện view content duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| next_day_open | string | Số lượt day 2 retentions duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_next_day_open | string | Chi phí trung bình cho mỗi sự kiện day 2 retention event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| next_day_open_rate | string | Tỷ lệ phần trăm các sự kiện day 2 retention duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| add_payment_info | string | Số lượt times a user added payment info duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_add_payment_info | string | Chi phí trung bình cho mỗi sự kiện add payment info event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| add_payment_info_rate | string | Tỷ lệ phần trăm các sự kiện add payment info duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| add_to_wishlist | string | Số lượt times users added items to a wishlist duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_add_to_wishlist | string | Chi phí trung bình cho mỗi sự kiện add to wishlist event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| add_to_wishlist_rate | string | Tỷ lệ phần trăm các sự kiện add to wishlist duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| launch_app | string | Số lượng sự kiện unique times a user launched your mobile app that were recorded as app. |
| cost_per_launch_app | string | Chi phí trung bình cho mỗi sự kiện launch app event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| launch_app_rate | string | Tỷ lệ phần trăm các sự kiện launch app duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| complete_tutorial | string | Số lượt times a user completed a tutorial duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_complete_tutorial | string | Chi phí trung bình cho mỗi sự kiện complete tutorial event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| complete_tutorial_rate | string | Tỷ lệ phần trăm các sự kiện complete tutorial duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| create_group | string | Số lần duy nhất người dùng created a group trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_create_group | string | Chi phí trung bình cho mỗi sự kiện create group event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| create_group_rate | string | Tỷ lệ phần trăm các sự kiện create group duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| join_group | string | Số lần duy nhất người dùng joined a group trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_join_group | string | Chi phí trung bình cho mỗi sự kiện join group event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| join_group_rate | string | Tỷ lệ phần trăm các sự kiện join group duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| create_gamerole | string | Số lần duy nhất người dùng created a character or role trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_create_gamerole | string | Chi phí trung bình cho mỗi sự kiện create role event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| create_gamerole_rate | string | Tỷ lệ phần trăm các sự kiện create role duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| spend_credits | string | Số lần duy nhất người dùng spent credit trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_spend_credits | string | Chi phí trung bình cho mỗi sự kiện spend credits event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| spend_credits_rate | string | Tỷ lệ phần trăm các sự kiện spend credits duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| achieve_level | string | Số lượt times a user achieved a level duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_achieve_level | string | Chi phí trung bình cho mỗi sự kiện achieve level event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| achieve_level_rate | string | Tỷ lệ phần trăm các sự kiện achieve level duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| unlock_achievement | string | Số lượng sự kiện unique times that a user unlocked an achievement in your mobile game app that were recorded as app. |
| cost_per_unlock_achievement | string | Chi phí trung bình cho mỗi sự kiện unlock achievement event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| unlock_achievement_rate | string | Tỷ lệ phần trăm các sự kiện unlock achievement duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| sales_lead | string | Số lượt leads generated duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_sales_lead | string | Chi phí trung bình cho mỗi sự kiện generate lead event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| sales_lead_rate | string | Tỷ lệ phần trăm các sự kiện generate lead duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| in_app_ad_click | string | Số lượng sự kiện unique in-app ad click. |
| cost_per_in_app_ad_click | string | Chi phí trung bình cho mỗi sự kiện in-app ad click event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| in_app_ad_click_rate | string | Tỷ lệ phần trăm các sự kiện in-app ad click duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| in_app_ad_impr | string | Số lượng sự kiện unique in-app ad impression. |
| cost_per_in_app_ad_impr | string | Chi phí trung bình cho mỗi sự kiện in-app ad impression event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| in_app_ad_impr_rate | string | Tỷ lệ phần trăm các sự kiện in-app ad impression duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_apply | string | Số lượt times a user applied for a loan duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_loan_apply | string | Chi phí trung bình cho mỗi sự kiện loan apply event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_apply_rate | string | Tỷ lệ phần trăm các sự kiện loan apply duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_credit | string | Số lượt times a user was approved a loan duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_loan_credit | string | Chi phí trung bình cho mỗi sự kiện loan approval event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_credit_rate | string | Tỷ lệ phần trăm các sự kiện loan approval duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_disbursement | string | Số lượt loan disbursal duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_loan_disbursement | string | Chi phí trung bình cho mỗi sự kiện loan disbursal event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| loan_disbursement_rate | string | Số lượt loan disbursals duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| login | string | Số lượt logins duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_login | string | Chi phí trung bình cho mỗi sự kiện login event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| login_rate | string | Tỷ lệ phần trăm các sự kiện login duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| ratings | string | Số lượt ratings duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_ratings | string | Chi phí trung bình cho mỗi sự kiện rate event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| ratings_rate | string | Tỷ lệ phần trăm các sự kiện rate duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| search | string | Số lượt searches duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_search | string | Chi phí trung bình cho mỗi sự kiện search event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| search_rate | string | Tỷ lệ phần trăm các sự kiện search duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| start_trial | string | Số lượt times a user started a trial duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_start_trial | string | Chi phí trung bình cho mỗi sự kiện start trial event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| start_trial_rate | string | Tỷ lệ phần trăm các sự kiện start trial duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| subscribe | string | Số lượt subscriptions duy nhất trong ứng dụng di động được ghi nhận là sự kiện ứng dụng và được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| cost_per_subscribe | string | Chi phí trung bình cho mỗi sự kiện subscribe event duy nhất được phân bổ cho quảng cáo của bạn. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| subscribe_rate | string | Tỷ lệ phần trăm các sự kiện subscribe duy nhất trên tổng số sự kiện cài đặt ứng dụng. (Tính theo thời điểm diễn ra mỗi lượt hiển thị quảng cáo). |
| total_registration | string | Tổng số lượt Registration (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_registration | string | Chi phí trên mỗi lượt Registration (Tính theo thời điểm bạn bị tính phí). |
| total_purchase | string | Tổng số lượt Purchase (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_purchase | string | Chi phí trên mỗi lượt Purchase (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_purchase | string | Giá trị trên mỗi lượt Purchase (Tính theo thời điểm bạn bị tính phí). |
| total_purchase_value | string | Tổng giá trị Purchase (Tính theo thời điểm bạn bị tính phí). |
| total_app_event_add_to_cart | string | Tổng số lượt Add to Cart (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_app_event_add_to_cart | string | Chi phí trên mỗi lượt Add to Cart (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_app_event_add_to_cart | string | Giá trị trên mỗi lượt Add to Cart (Tính theo thời điểm bạn bị tính phí). |
| total_app_event_add_to_cart_value | string | Tổng giá trị Add to Cart (Tính theo thời điểm bạn bị tính phí). |
| total_checkout | string | Tổng số lượt Checkout (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_checkout | string | Chi phí trên mỗi lượt Checkout (Tính theo thời điểm bạn bị tính phí). |
| value_per_checkout | string | Giá trị trên mỗi lượt Checkout (Tính theo thời điểm bạn bị tính phí). |
| total_checkout_value | string | Tổng giá trị Checkout (Tính theo thời điểm bạn bị tính phí). |
| total_view_content | string | Tổng số lượt View Content (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_view_content | string | Chi phí trên mỗi lượt View Content (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_view_content | string | Giá trị trên mỗi lượt View Content (Tính theo thời điểm bạn bị tính phí). |
| total_view_content_value | string | Tổng giá trị View Content (Tính theo thời điểm bạn bị tính phí). |
| total_next_day_open | string | Tổng số lượt Day 2 Retention (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_next_day_open | string | Chi phí trên mỗi lượt Day 2 Retention (Tính theo thời điểm bạn bị tính phí). |
| total_add_payment_info | string | Tổng số lượt Add Payment Info (Tính theo thời điểm bạn bị tính phí). |
| cost_total_add_payment_info | string | Chi phí trên mỗi lượt Add Payment Info (Tính theo thời điểm bạn bị tính phí). |
| total_add_to_wishlist | string | Tổng số lượt Add to Wishlist (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_add_to_wishlist | string | Chi phí trên mỗi lượt Add to Wishlist (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_add_to_wishlist | string | Giá trị trên mỗi lượt Add to Wishlist (Tính theo thời điểm bạn bị tính phí). |
| total_add_to_wishlist_value | string | Tổng giá trị Add to Wishlist (Tính theo thời điểm bạn bị tính phí). |
| total_launch_app | string | Tổng số lượt Launch App (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_launch_app | string | Chi phí trên mỗi lượt Launch App (Tính theo thời điểm bạn bị tính phí). |
| total_complete_tutorial | string | Tổng số lượt Complete Tutorial (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_complete_tutorial | string | Chi phí trên mỗi lượt Complete Tutorial (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_complete_tutorial | string | Giá trị trên mỗi lượt Complete Tutorial (Tính theo thời điểm bạn bị tính phí). |
| total_complete_tutorial_value | string | Tổng giá trị Complete Tutorial (Tính theo thời điểm bạn bị tính phí). |
| total_create_group | string | Tổng số lượt Create Group (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_create_group | string | Chi phí trên mỗi lượt Create Group (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_create_group | string | Giá trị trên mỗi lượt Create Group (Tính theo thời điểm bạn bị tính phí). |
| total_create_group_value | string | Tổng giá trị Create Group (Tính theo thời điểm bạn bị tính phí). |
| total_join_group | string | Tổng số lượt Join Group (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_join_group | string | Chi phí trên mỗi lượt Join Group (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_join_group | string | Giá trị trên mỗi lượt Join Group (Tính theo thời điểm bạn bị tính phí). |
| total_join_group_value | string | Tổng giá trị Join Group (Tính theo thời điểm bạn bị tính phí). |
| total_create_gamerole | string | Tổng số lượt Create Role (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_create_gamerole | string | Chi phí trên mỗi lượt Create Role (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_create_gamerole | string | Giá trị trên mỗi lượt Create Role (Tính theo thời điểm bạn bị tính phí). |
| total_create_gamerole_value | string | Tổng giá trị Create Role (Tính theo thời điểm bạn bị tính phí). |
| total_spend_credits | string | Tổng số lượt Spend Credit (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_spend_credits | string | Chi phí trên mỗi lượt Spend Credit (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_spend_credits | string | Giá trị trên mỗi lượt Spend Credit (Tính theo thời điểm bạn bị tính phí). |
| total_spend_credits_value | string | Tổng giá trị Spend Credit (Tính theo thời điểm bạn bị tính phí). |
| total_achieve_level | string | Tổng số lượt Achieve Level (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_achieve_level | string | Chi phí trên mỗi lượt Achieve Level (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_achieve_level | string | Giá trị trên mỗi lượt Achieve Level (Tính theo thời điểm bạn bị tính phí). |
| total_achieve_level_value | string | Tổng giá trị Achieve Level (Tính theo thời điểm bạn bị tính phí). |
| total_unlock_achievement | string | Tổng số lượt Unlock Achievement (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_unlock_achievement | string | Chi phí trên mỗi lượt Unlock Achievement (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_unlock_achievement | string | Giá trị trên mỗi lượt Unlock Achievement (Tính theo thời điểm bạn bị tính phí). |
| total_unlock_achievement_value | string | Tổng giá trị Unlock Achievement (Tính theo thời điểm bạn bị tính phí). |
| total_sales_lead | string | Tổng số lượt Generate Lead (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_sales_lead | string | Chi phí trên mỗi lượt Generate Lead (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_sales_lead | string | Giá trị trên mỗi lượt Generate Lead (Tính theo thời điểm bạn bị tính phí). |
| total_sales_lead_value | string | Tổng giá trị Generate Lead (Tính theo thời điểm bạn bị tính phí). |
| total_in_app_ad_click | string | Tổng số lượt In App Ad Click (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_in_app_ad_click | string | Chi phí trên mỗi lượt In App Ad Click (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_in_app_ad_click | string | Giá trị trên mỗi lượt In App Ad Click (Tính theo thời điểm bạn bị tính phí). |
| total_in_app_ad_click_value | string | Tổng giá trị In App Ad Click (Tính theo thời điểm bạn bị tính phí). |
| total_in_app_ad_impr | string | Tổng số lượt In App Ad Impr (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_in_app_ad_impr | string | Chi phí trên mỗi lượt In App Ad Impr (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_in_app_ad_impr | string | Giá trị trên mỗi lượt In App Ad Impr (Tính theo thời điểm bạn bị tính phí). |
| total_in_app_ad_impr_value | string | Tổng giá trị In App Ad Impr (Tính theo thời điểm bạn bị tính phí). |
| total_loan_apply | string | Tổng số lượt Loan Apply (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_loan_apply | string | Chi phí trên mỗi lượt Loan Apply (Tính theo thời điểm bạn bị tính phí). |
| total_loan_credit | string | Tổng số lượt Loan Approval (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_loan_credit | string | Chi phí trên mỗi lượt Loan Approval (Tính theo thời điểm bạn bị tính phí). |
| total_loan_disbursement | string | Tổng số lượt Loan Disbursement (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_loan_disbursement | string | Chi phí trên mỗi lượt Loan Disbursement (Tính theo thời điểm bạn bị tính phí). |
| total_login | string | Tổng số lượt Login (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_login | string | Chi phí trên mỗi lượt Login (Tính theo thời điểm bạn bị tính phí). |
| total_ratings | string | Tổng số lượt Rate (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_ratings | string | Chi phí trên mỗi lượt Rate (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_ratings | string | Giá trị trên mỗi lượt Rate (Tính theo thời điểm bạn bị tính phí). |
| total_ratings_value | string | Tổng giá trị Rate (Tính theo thời điểm bạn bị tính phí). |
| total_search | string | Tổng số lượt Search (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_search | string | Chi phí trên mỗi lượt Search (Tính theo thời điểm bạn bị tính phí). |
| total_start_trial | string | Tổng số lượt Start Trial (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_start_trial | string | Chi phí trên mỗi lượt Start Trial (Tính theo thời điểm bạn bị tính phí). |
| total_subscribe | string | Tổng số lượt Subscribe (Tính theo thời điểm bạn bị tính phí). |
| cost_per_total_subscribe | string | Chi phí trên mỗi lượt Subscribe (Tính theo thời điểm bạn bị tính phí). |
| value_per_total_subscribe | string | Giá trị trên mỗi lượt Subscribe (Tính theo thời điểm bạn bị tính phí). |
| total_subscribe_value | string | Tổng giá trị Subscribe (Tính theo thời điểm bạn bị tính phí). |
| vta_conversion | string | Tỷ lệ phần trăm các sự kiện cài đặt ứng dụng bạn nhận được trên tổng số lượt nhấp vào quảng cáo. |
| cost_per_vta_conversion | string | Chi phí trung bình cho mỗi sự kiện cài đặt ứng dụng được phân bổ theo lượt hiển thị (VTA). |
| vta_registration | string | Số lượng sự kiện registration được phân bổ theo lượt hiển thị (VTA), dựa trên thông tin nhận được từ đối tác đo lường của bạn. |
| cost_per_vta_registration | string | Chi phí trung bình cho mỗi sự kiện registration được phân bổ theo lượt hiển thị (VTA). |
| vta_purchase | string | Số lượng sự kiện in-app payment được phân bổ theo lượt hiển thị (VTA), dựa trên thông tin nhận được từ đối tác đo lường của bạn. |
| cost_per_vta_purchase | string | Chi phí trung bình cho mỗi sự kiện payment được phân bổ theo lượt hiển thị (VTA). |
| vta_complete_payment | string | Sự kiện hoàn tất thanh toán VTA được phân bổ cho người dùng chỉ xem quảng cáo của bạn. |
| cost_per_vta_payments_completed | string | Chi phí trung bình cho mỗi sự kiện hoàn tất thanh toán VTA được phân bổ cho người dùng chỉ xem quảng cáo của bạn. |
| vta_complete_payment_value | string | Tổng giá trị các sự kiện hoàn tất thanh toán VTA được phân bổ cho người dùng chỉ xem quảng cáo của bạn. |
| vta_complete_payment_roas | string | Lợi tức chi tiêu quảng cáo (ROAS) từ các sự kiện hoàn tất thanh toán VTA được phân bổ cho người dùng chỉ xem quảng cáo của bạn. |
| cta_conversion | string | Số sự kiện cài đặt ứng dụng trong ứng dụng diễn ra trên ứng dụng di động của bạn và được phân bổ theo số lượt nhấp (CTA). |
| cost_per_cta_conversion | string | Chi phí trung bình cho mỗi sự kiện cài đặt ứng dụng được phân bổ theo lượt nhấp. |
| cta_registration | string | Số sự kiện registration trong ứng dụng được phân bổ theo lượt nhấp (CTA), dựa trên thông tin nhận được từ đối tác đo lường của bạn. |
| cost_per_cta_registration | string | Chi phí trung bình cho sự kiện đăng ký trong ứng dụng được phân bổ theo lượt nhấp. |
| cta_purchase | string | Số sự kiện payment trong ứng dụng được phân bổ theo lượt nhấp (CTA), dựa trên thông tin nhận được từ đối tác đo lường của bạn. |
| cost_per_cta_purchase | string | Chi phí trung bình cho mỗi sự kiện thanh toán được phân bổ theo lượt nhấp. |
| complete_payment_roas | string | Tổng lợi tức trên chi tiêu quảng cáo (ROAS) từ các sự kiện hoàn tất thanh toán được phân bổ cho quảng cáo của bạn. |
| complete_payment | string | Số lượng sự kiện complete payment. |
| cost_per_complete_payment | string | Chi phí trung bình cho mỗi sự kiện complete payment. |
| complete_payment_rate | string | Tỷ lệ phần trăm các sự kiện complete payment trên tổng số lượt nhấp. |
| value_per_complete_payment | string | Giá trị trung bình thu được từ các sự kiện complete payment. |
| total_complete_payment_rate | string | Tổng giá trị thu được từ các sự kiện complete payment. |
| page_browse_view | string | Số lượng sự kiện page browse. |
| cost_per_page_browse_view | string | Chi phí trung bình cho mỗi sự kiện page browse. |
| page_browse_view_rate | string | Tỷ lệ phần trăm các sự kiện page browse trên tổng số lượt nhấp. |
| total_page_browse_view_value | string | Giá trị trung bình thu được từ các sự kiện page browse. |
| value_per_page_browse_view | string | Tổng giá trị thu được từ các sự kiện page browse. |
| button_click | string | Số lượng sự kiện button click. |
| cost_per_button_click | string | Chi phí trung bình cho mỗi sự kiện button click. |
| button_click_rate | string | Tỷ lệ phần trăm các sự kiện button click trên tổng số lượt nhấp. |
| value_per_button_click | string | Giá trị trung bình thu được từ các sự kiện button click. |
| total_button_click_value | string | Tổng giá trị thu được từ các sự kiện button click. |
| online_consult | string | Số lượng sự kiện online consultation. |
| cost_per_online_consult | string | Chi phí trung bình cho mỗi sự kiện online consultation. |
| online_consult_rate | string | Tỷ lệ phần trăm các sự kiện online consultation trên tổng số lượt nhấp. |
| value_per_online_consult | string | Giá trị trung bình thu được từ các sự kiện online consultation. |
| total_online_consult_value | string | Tổng giá trị thu được từ các sự kiện online consultation. |
| user_registration | string | Số lượng sự kiện user registration. |
| cost_per_user_registration | string | Chi phí trung bình cho mỗi sự kiện user registration. |
| user_registration_rate | string | Tỷ lệ phần trăm các sự kiện user registration trên tổng số lượt nhấp. |
| value_per_user_registration | string | Giá trị trung bình thu được từ các sự kiện user registration. |
| total_user_registration_value | string | Tổng giá trị thu được từ các sự kiện user registration. |
| product_details_page_browse | string | Số lượng sự kiện product details page browse. |
| cost_per_product_details_page_browse | string | Chi phí trung bình cho mỗi sự kiện product details page browse. |
| product_details_page_browse_rate | string | Tỷ lệ phần trăm các sự kiện product details page browse trên tổng số lượt nhấp. |
| value_per_product_details_page_browse | string | Giá trị trung bình thu được từ các sự kiện product details page browse. |
| total_product_details_page_browse_value | string | Tổng giá trị thu được từ các sự kiện product details page browse. |
| web_event_add_to_cart | string | Số lượng sự kiện add to cart. |
| cost_per_web_event_add_to_cart | string | Chi phí trung bình cho mỗi sự kiện add to cart. |
| web_event_add_to_cart_rate | string | Tỷ lệ phần trăm các sự kiện add to cart trên tổng số lượt nhấp. |
| value_per_web_event_add_to_cart | string | Giá trị trung bình thu được từ các sự kiện add to cart. |
| total_web_event_add_to_cart_value | string | Tổng giá trị thu được từ các sự kiện add to cart. |
| on_web_order | string | Số lượng sự kiện place an order. |
| cost_per_on_web_order | string | Chi phí trung bình cho mỗi sự kiện place an order. |
| on_web_order_rate | string | Tỷ lệ phần trăm các sự kiện place an order trên tổng số lượt nhấp. |
| value_per_on_web_order | string | Giá trị trung bình thu được từ các sự kiện place an order. |
| total_on_web_order_value | string | Tổng giá trị thu được từ các sự kiện place an order. |
| form_detail | string | Số lượng sự kiện details page browse (form). |
| cost_per_form_detail | string | Chi phí trung bình cho mỗi sự kiện details page browse (form). |
| form_detail_rate | string | Tỷ lệ phần trăm các sự kiện details page browse (form) trên tổng số lượt nhấp. |
| value_per_form_detail | string | Giá trị trung bình thu được từ các sự kiện details page browse (form). |
| total_form_detail_value | string | Tổng giá trị thu được từ các sự kiện details page browse (form). |
| form_button | string | Số lượng sự kiện button click (form). |
| cost_per_form_button | string | Chi phí trung bình cho mỗi sự kiện button click (form). |
| form_button_rate | string | Tỷ lệ phần trăm các sự kiện button click (form) trên tổng số lượt nhấp. |
| value_per_form_button | string | Giá trị trung bình thu được từ các sự kiện button click (form). |
| total_form_button_value | string | Tổng giá trị thu được từ các sự kiện button click (form). |
| form | string | Số lượng sự kiện form submission. |
| cost_per_form | string | Chi phí trung bình cho mỗi sự kiện form submission. |
| form_rate | string | Tỷ lệ phần trăm các sự kiện form submission trên tổng số lượt nhấp. |
| value_per_form | string | Giá trị trung bình thu được từ các sự kiện form submission. |
| total_form_value | string | Tổng giá trị thu được từ các sự kiện form submission. |
| page_browse_consultation | string | Số lượng sự kiện details page browse (consultation). |
| cost_per_page_browse_consultation | string | Chi phí trung bình cho mỗi sự kiện details page browse (consultation). |
| page_browse_consultation_rate | string | Số lượng sự kiện button click (consultation). |
| value_per_page_browse_consultation | string | Giá trị trung bình thu được từ các sự kiện button click (consultation). |
| total_page_browse_consultation_value | string | Tổng giá trị thu được từ các sự kiện button click (consultation). |
| button_click_consultation | string | Số lượng sự kiện button click (consultation). |
| cost_per_button_click_consultation | string | Chi phí trung bình cho mỗi sự kiện button click (consultation). |
| button_click_consultation_rate | string | Tỷ lệ phần trăm các sự kiện button click (consultation) trên tổng số lượt nhấp. |
| value_per_button_click_consultation | string | Giá trị trung bình thu được từ các sự kiện button click (consultation). |
| total_button_click_consultation_value | string | Tổng giá trị thu được từ các sự kiện button click (consultation). |
| consultation | string | Số lượng sự kiện consultation. |
| cost_per_consultation | string | Chi phí trung bình cho mỗi sự kiện consultation. |
| consultation_rate | string | Tỷ lệ phần trăm các sự kiện consultation trên tổng số lượt nhấp. |
| value_per_consultation | string | Giá trị trung bình thu được từ các sự kiện consultation. |
| total_consultation_value | string | Tổng giá trị thu được từ các sự kiện consultation. |
| download_detail | string | Số lượng sự kiện details page browse (app download). |
| cost_per_download_detail | string | Chi phí trung bình cho mỗi sự kiện details page browse (app download). |
| download_detail_rate | string | Tỷ lệ phần trăm các sự kiện details page browse (app download) trên tổng số lượt nhấp. |
| value_per_download_detail | string | Giá trị trung bình thu được từ các sự kiện details page browse (app download). |
| total_download_detail_value | string | Tổng giá trị thu được từ các sự kiện details page browse (app download). |
| download_button | string | Số lượng sự kiện button click (app download). |
| cost_per_download_button | string | Chi phí trung bình cho mỗi sự kiện button click (app download). |
| download_button_rate | string | Tỷ lệ phần trăm các sự kiện button click (app download) trên tổng số lượt nhấp. |
| value_per_download_button | string | Giá trị trung bình thu được từ các sự kiện button click (app download). |
| total_download_button_value | string | Giá trị trung bình thu được từ các sự kiện button click (app download). |
| download_start | string | Số lượng sự kiện download button click. |
| cost_per_download_start | string | Chi phí trung bình cho mỗi sự kiện download button click. |
| download_start_rate | string | Tỷ lệ phần trăm các sự kiện download button click trên tổng số lượt nhấp. |
| value_per_download_start | string | Giá trị trung bình thu được từ các sự kiện download button click. |
| total_download_start_value | string | Tổng giá trị thu được từ các sự kiện download button click. |
| initiate_checkout | string | Số lượng sự kiện initiate checkout. |
| cost_per_initiate_checkout | string | Chi phí trung bình cho mỗi sự kiện initiate checkout. |
| initiate_checkout_rate | string | Tỷ lệ phần trăm các sự kiện initiate checkout trên tổng số lượt nhấp. |
| value_per_initiate_checkout | string | Giá trị trung bình thu được từ các sự kiện initiate checkout. |
| total_initiate_checkout_value | string | Tổng giá trị thu được từ các sự kiện initiate checkout. |
| add_billing | string | Số lượng sự kiện add billing. |
| cost_per_add_billing | string | Chi phí trung bình cho mỗi sự kiện add billing. |
| add_billing_rate | string | Tỷ lệ phần trăm các sự kiện add billing trên tổng số lượt nhấp. |
| value_per_add_billing | string | Giá trị trung bình thu được từ các sự kiện add billing. |
| total_add_billing_value | string | Tổng giá trị thu được từ các sự kiện add billing. |
| page_event_search | string | Số lượng sự kiện search. |
| cost_per_page_event_search | string | Chi phí trung bình cho mỗi sự kiện search. |
| page_event_search_rate | string | Tỷ lệ phần trăm các sự kiện search trên tổng số lượt nhấp. |
| value_per_page_event_search | string | Giá trị trung bình thu được từ các sự kiện search. |
| total_page_event_search_value | string | Tổng giá trị thu được từ các sự kiện search. |
| onsite_shopping_roas | string | Lợi tức chi tiêu quảng cáo (ROAS) của sự kiện hoàn tất thanh toán trên trang (onsite). |
| onsite_shopping | string | Số lượng sự kiện hoàn tất thanh toán trên trang (onsite). |
| cost_per_onsite_shopping | string | Chi phí trung bình cho mỗi sự kiện hoàn tất thanh toán trên trang (onsite). |
| onsite_shopping_rate | string | Tỷ lệ phần trăm các sự kiện hoàn tất thanh toán trên trang trên tổng số lượt nhấp. |
| value_per_onsite_shopping | string | Giá trị trung bình thu được từ các sự kiện hoàn tất thanh toán trên trang. |
| total_onsite_shopping_value | string | Tổng giá trị thu được từ các sự kiện hoàn tất thanh toán trên trang. |
| onsite_initiate_checkout_count | string | Số lượng sự kiện onsite initiate checkout. |
| cost_per_onsite_initiate_checkout_count | string | Chi phí trung bình cho các sự kiện initiate checkout trên trang (onsite). |
| onsite_initiate_checkout_count_rate | string | Tỷ lệ phần trăm các sự kiện onsite initiate checkout trên tổng số lượt nhấp. |
| value_per_onsite_initiate_checkout_count | string | Giá trị trung bình thu được từ các sự kiện initiate checkout trên trang (onsite). |
| total_onsite_initiate_checkout_count_value | string | Tổng giá trị thu được từ các sự kiện initiate checkout trên trang (onsite). |
| onsite_on_web_detail | string | Số lượng sự kiện onsite product details page view. |
| cost_per_onsite_on_web_detail | string | Chi phí trung bình cho các sự kiện product details page view trên trang (onsite). |
| onsite_on_web_detail_rate | string | Tỷ lệ phần trăm các sự kiện onsite product details page view trên tổng số lượt nhấp. |
| value_per_onsite_on_web_detail | string | Giá trị trung bình thu được từ các sự kiện product details page view trên trang (onsite). |
| total_onsite_on_web_detail_value | string | Tổng giá trị thu được từ các sự kiện product details page view trên trang (onsite). |
| onsite_add_to_wishlist | string | Số lượng sự kiện onsite all to wishlist. |
| cost_per_onsite_add_to_wishlist | string | Chi phí trung bình cho các sự kiện all to wishlist trên trang (onsite). |
| onsite_add_to_wishlist_rate | string | Tỷ lệ phần trăm các sự kiện onsite all to wishlist trên tổng số lượt nhấp. |
| value_per_onsite_add_to_wishlist | string | Giá trị trung bình thu được từ các sự kiện all to wishlist trên trang (onsite). |
| total_onsite_add_to_wishlist_value | string | Tổng giá trị thu được từ các sự kiện all to wishlist trên trang (onsite). |
| onsite_add_billing | string | Số lượng sự kiện onsite add billing. |
| cost_per_onsite_add_billing | string | Chi phí trung bình cho các sự kiện add billing trên trang (onsite). |
| onsite_add_billing_rate | string | Tỷ lệ phần trăm các sự kiện onsite add billing trên tổng số lượt nhấp. |
| value_per_onsite_add_billing | string | Giá trị trung bình thu được từ các sự kiện add billing trên trang (onsite). |
| total_onsite_add_billing_value | string | Tổng giá trị thu được từ các sự kiện add billing trên trang (onsite). |
| onsite_on_web_cart | string | Số lượng sự kiện onsite add to cart. |
| cost_per_onsite_on_web_cart | string | Chi phí trung bình cho các sự kiện add to cart trên trang (onsite). |
| onsite_on_web_cart_rate | string | Tỷ lệ phần trăm các sự kiện onsite add to cart trên tổng số lượt nhấp. |
| value_per_onsite_on_web_cart | string | Giá trị trung bình thu được từ các sự kiện add to cart trên trang (onsite). |
| total_onsite_on_web_cart_value | string | Tổng giá trị thu được từ các sự kiện add to cart trên trang (onsite). |
| onsite_form | string | Số lượng sự kiện onsite form submission. |
| cost_per_onsite_form | string | Chi phí trung bình cho các sự kiện form submission trên trang (onsite). |
| onsite_form_rate | string | Tỷ lệ phần trăm các sự kiện onsite form submission trên tổng số lượt nhấp. |
| value_per_onsite_form | string | Giá trị trung bình thu được từ các sự kiện form submission trên trang (onsite). |
| total_onsite_form_value | string | Tổng giá trị thu được từ các sự kiện form submission trên trang (onsite). |
| onsite_download_start | string | Số lượng sự kiện nhấp vào cửa hàng ứng dụng trên trang (onsite). |
| cost_per_onsite_download_start | string | Chi phí trung bình của các sự kiện nhấp vào cửa hàng ứng dụng trên trang. |
| onsite_download_start_rate | string | Tỷ lệ phần trăm các sự kiện nhấp vào cửa hàng ứng dụng trên trang trên tổng số lượt nhấp. |
| ix_page_view_count | string | Số lượng sự kiện xem trang trên trang (onsite page view). |
| cost_per_ix_page_view_count | string | Chi phí trung bình của một sự kiện xem trang trên trang. |
| ix_page_view_count_rate | string | Tỷ lệ phần trăm các sự kiện xem trang trên trang trên tổng số sự kiện. |
| ix_button_click_count | string | Số lượng sự kiện nhấp nút kêu gọi hành động (CTA) trên trang. |
| cost_per_ix_button_click_count | string | Chi phí trung bình của sự kiện nhấp nút kêu gọi hành động trên trang. |
| ix_button_click_count_rate | string | Tỷ lệ phần trăm các sự kiện nhấp nút kêu gọi hành động trên trang trên tổng số sự kiện. |
| ix_product_click_count | string | Số lượng sự kiện nhấp vào sản phẩm trên trang. |
| cost_per_ix_product_click_count | string | Chi phí trung bình của sự kiện nhấp vào sản phẩm trên trang. |
| ix_product_click_count_rate | string | Tỷ lệ phần trăm các sự kiện nhấp vào sản phẩm trên trang trên tổng số sự kiện. |

---
<a id="doc-1789700050715650"></a>
<!-- doc_id: 1789700050715650 -->
<!-- doc_id: 1789700050715650 -->
# Báo cáo thông tin chi tiết video (Video Insights reports)
> Đường dẫn: API Reference > Creative Reports > Video Insights reports
# Chạy báo cáo thông tin chi tiết video (Run a Video Insights report)

Sử dụng endpoint này để chạy báo cáo Video Insights về các video trên một hoặc nhiều tài khoản quảng cáo, bao gồm cả Spark Ads và non-Spark Ads.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/report/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| report_type ***(Bắt buộc)*** | string | Loại báo cáo. <br><br>Các giá trị enum hỗ trợ: <ul><li>`VIDEO_INSIGHT`: Báo cáo Video Insights cho một hoặc nhiều tài khoản nhà quảng cáo.</li></ul> |
| advertiser_id **(Điều kiện)** | string | Phải đặt một trong hai trường `advertiser_id` hoặc `advertiser_ids`. <br><br>ID tài khoản quảng cáo TikTok mà bạn muốn chạy báo cáo. |
| advertiser_ids **(Điều kiện)** | string[] | Phải đặt một trong hai trường `advertiser_id` hoặc `advertiser_ids`. <br><br>Danh sách ID nhà quảng cáo mà bạn muốn chạy báo cáo. <br><br>Kích thước tối đa: 50. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Bạn cần có quyền truy cập vào tất cả các tài khoản quảng cáo tương ứng. Để lấy danh sách tài khoản quảng cáo trong Business Center mà bạn có quyền truy cập, sử dụng [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401).</li><li>Nếu đơn vị tiền tệ giữa các tài khoản quảng cáo khác nhau, đơn vị tiền tệ của các chỉ số sẽ mặc định là USD.</li></ul> |
| start_date ***(Bắt buộc)*** | string | Ngày bắt đầu truy vấn, khoảng đóng, theo định dạng `YYYY-MM-DD` (giờ UTC+0). <br><br>Ví dụ: `2024-01-01`. <br><br>Khoảng thời gian truy vấn tối đa xác định bởi `start_date` và `end_date` là 365 ngày. |
| end_date ***(Bắt buộc)*** | string | Ngày kết thúc truy vấn, khoảng đóng, theo định dạng `YYYY-MM-DD` (giờ UTC+0). <br><br>Ví dụ: `2024-01-01`. <br><br>Khoảng thời gian truy vấn tối đa xác định bởi `start_date` và `end_date` là 365 ngày. |
| metrics_fields | string[] | Các chỉ số bạn muốn lấy dữ liệu. <br><br>  <ul><li>Nếu trường này không được truyền, tất cả các chỉ số được hỗ trợ trong báo cáo Video Insights sẽ được trả về theo mặc định.</li><li>Để tìm các chỉ số được hỗ trợ, xem [Các chỉ số được hỗ trợ trong báo cáo Video Insights](37-creative-reports.md#doc-1789703614085122).</li></ul> |
| filtering | object | Điều kiện lọc dữ liệu. |
#| material_id | string[] | Danh sách ID tài sản video. <br><br>Kích thước tối đa: 20. <br><br>Để lấy ID tài sản của một video, sử dụng [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
#| material_name | string | Tên tài sản video. <br><br>Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| tiktok_item_ids | string[] | Danh sách ID của các bài đăng TikTok Spark Ads mà video đã được sử dụng để tạo. <br><br>Kích thước tối đa: 20. <br><br>Để lấy ID bài đăng TikTok, sử dụng [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) hoặc [/identity/video/get/](46-identity.md#doc-1740218475032577). |
#| country_code | string[] | Danh sách mã vị trí địa lý nơi video được phân phối. <br><br>Để xem danh sách giá trị enum, xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
#| creative_formats | string[] | Danh sách định dạng sáng tạo. <br><br>Các giá trị enum hỗ trợ: <ul><li>`VIDEO_16_9`: Video (16:9).</li><li>`VIDEO_1_1`: Video (1:1).</li><li>`VIDEO_9_16`: Video (9:16).</li><li>`OTHER`: Khác (Other).</li></ul> |
#| video_material_sources | string[] | Danh sách nguồn tài sản video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`UPLOADED_TO_TIKTOK_ADS_MANAGER`: Tải lên Trình quản lý quảng cáo TikTok.</li><li>`UPLOADED_TO_CATALOG`: Tải lên Catalog.</li><li>`CREATIVE_TOOL_SMART_VIDEO`: Công cụ sáng tạo - Smart Video.</li><li>`CREATIVE_TOOL_QUICK_OPTIMIZATION`: Công cụ sáng tạo - Tối ưu hóa nhanh.</li><li>`CREATIVE_TOOL_VIDEO_TEMPLATE`: Công cụ sáng tạo - Mẫu video.</li><li>`CREATIVE_TOOL_SMART_VIDEO_SOUNDTRACK`: Công cụ sáng tạo - Nhạc nền Smart Video.</li><li>`CREATIVE_TOOL_TIKTOK_VIDEO_EDITOR`: Công cụ sáng tạo - Trình chỉnh sửa video TikTok.</li><li>`TIKTOK_CREATIVE_EXCHANGE`: Sàn giao dịch sáng tạo TikTok (TikTok Creative Exchange).</li><li>`CATALOG_VIDEO_TEMPLATE`: Mẫu video Catalog.</li><li>`DYNAMIC_VIDEO_EDITOR`: Trình chỉnh sửa video động.</li><li>`CREATIVE_CHALLENGE`: Thử thách sáng tạo.</li><li>`AUTOMATED_CREATIVE_OPTIMIZATION`: Tối ưu hóa mẫu quảng cáo tự động.</li><li>`OTHER`: Khác.</li><li>`QUICK_GENERATION`: Tạo nhanh.</li><li>`CREATIVE_CENTER_VIDEO_UPLOAD`: Creative Center - Tải lên video.</li><li>`CREATIVE_CENTER_TIKTOK_VIDEO_EDITOR`: Creative Center - Trình chỉnh sửa video TikTok.</li><li>`CREATIVE_CENTER_VIDEO_TEMPLATE`: Creative Center - Mẫu video.</li><li>`DYNAMIC_SCENE`: Phân cảnh động.</li><li>`SMART_OPTIMIZATION_TOOL`: Công cụ tối ưu hóa thông minh.</li></ul> |
#| placement | string[] | Danh sách vị trí hiển thị quảng cáo cho video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`PLACEMENT_TIKTOK`: TikTok.</li><li>`PLACEMENT_PANGLE`: Pangle.</li><li>`PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle.</li></ul> |
#| identities | string[] | Các loại danh tính được sử dụng để phân phối video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`SPARK_ADS`: Danh tính Spark Ads, bao gồm Authorized User, TikTok User và người dùng tài khoản TikTok trong Business Center.</li><li>`NON_SPARK_ADS`: Danh tính non-Spark Ads, tức là danh tính Custom User.</li></ul> <br>Để tìm hiểu thêm về các loại danh tính, xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
#| ad_name | string | Tên quảng cáo. <br><br>Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| ad_id | string[] | Danh sách ID quảng cáo. <br><br>Hỗ trợ truy vấn hàng loạt. <br><br>Kích thước tối đa: 20. |
#| adgroup_name | string | Tên nhóm quảng cáo. <br><br>Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| adgroup_id | string[] | Danh sách ID nhóm quảng cáo. <br><br>Kích thước tối đa: 20. |
#| campaign_name | string | Tên chiến dịch. <br><br>Hỗ trợ tìm kiếm gần đúng (fuzzy search). |
#| campaign_id | string[] | Danh sách ID chiến dịch. <br><br>Kích thước tối đa: 20. |
| sort_field | string | Trường dùng để sắp xếp. <br><br>Các trường được hỗ trợ được liệt kê tại [Các chỉ số được hỗ trợ trong báo cáo Video Insights](37-creative-reports.md#doc-1789703614085122). |
| sort_type | string | Thứ tự sắp xếp kết quả. <br><br> Các giá trị enum hỗ trợ: `ASC`, `DESC`. <br> Giá trị mặc định: `DESC`.|
| page | number | Số trang hiện tại cần lấy dữ liệu. <br><br>Giá trị mặc định: 1. <br>Phạm vi: ≥ 1. |
| page_size | number | Kích thước trang (số kết quả mỗi trang). <br><br>Giá trị mặc định: 10. <br>Phạm vi giá trị: 1-1.000. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/creative/report/get/?report_type=VIDEO_INSIGHT&advertiser_id={{advertiser_id}}&start_date=2023-12-24&end_date=2024-01-23' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
|data |object|Returned data.|
#| list | object[] | Dữ liệu Video insights. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Theo mặc định, chỉ các video có tổng chi phí (`spend`) lớn hơn 0 mới được bao gồm. Các video không phát sinh chi phí sẽ bị lọc bỏ. |
##| metrics | object | Dữ liệu chỉ số cho video. <br><br> <ul><li>Nếu `metrics_fields` không được truyền trong yêu cầu, tất cả các chỉ số được hỗ trợ trong báo cáo Video Insights sẽ được trả về theo mặc định. Để xem các chỉ số được hỗ trợ, xem [Các chỉ số được hỗ trợ trong báo cáo Video Insights](37-creative-reports.md#doc-1789703614085122).</li><li>Nếu `metrics_fields` được truyền trong yêu cầu, chỉ các chỉ số được chỉ định sẽ được trả về.</li></ul> |
##| info | object | Thông tin tài sản video. |
###| material_id | string | ID tài sản video. |
###| material_name | string | Tên tài sản video. |
###| create_time | string | Thời gian video được tạo, theo định dạng [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601). <br><br>Ví dụ: "2024-01-01T00:00:01Z". |
###| tiktok_item_ids | string[] | Chỉ trả về khi video (`material_id`) đã được sử dụng để tạo Spark Ads. <br><br>Danh sách ID các bài đăng TikTok Spark Ads được tạo bằng video này. |
###| country_code | string[] | Danh sách mã vị trí địa lý nơi video (`material_id`) đã được phân phối. <br><br>Để xem danh sách giá trị enum, xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
###| video_material_source | string | Nguồn tài sản video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`UPLOADED_TO_TIKTOK_ADS_MANAGER`: Tải lên Trình quản lý quảng cáo TikTok.</li><li>`UPLOADED_TO_CATALOG`: Tải lên Catalog.</li><li>`CREATIVE_TOOL_SMART_VIDEO`: Công cụ sáng tạo - Smart Video.</li><li>`CREATIVE_TOOL_QUICK_OPTIMIZATION`: Công cụ sáng tạo - Tối ưu hóa nhanh.</li><li>`CREATIVE_TOOL_VIDEO_TEMPLATE`: Công cụ sáng tạo - Mẫu video.</li><li>`CREATIVE_TOOL_SMART_VIDEO_SOUNDTRACK`: Công cụ sáng tạo - Nhạc nền Smart Video.</li><li>`CREATIVE_TOOL_TIKTOK_VIDEO_EDITOR`: Công cụ sáng tạo - Trình chỉnh sửa video TikTok.</li><li>`TIKTOK_CREATIVE_EXCHANGE`: Sàn giao dịch sáng tạo TikTok (TikTok Creative Exchange).</li><li>`CATALOG_VIDEO_TEMPLATE`: Mẫu video Catalog.</li><li>`DYNAMIC_VIDEO_EDITOR`: Trình chỉnh sửa video động.</li><li>`CREATIVE_CHALLENGE`: Thử thách sáng tạo.</li><li>`AUTOMATED_CREATIVE_OPTIMIZATION`: Tối ưu hóa mẫu quảng cáo tự động.</li><li>`OTHER`: Khác.</li><li>`QUICK_GENERATION`: Tạo nhanh.</li><li>`CREATIVE_CENTER_VIDEO_UPLOAD`: Creative Center - Tải lên video.</li><li>`CREATIVE_CENTER_TIKTOK_VIDEO_EDITOR`: Creative Center - Trình chỉnh sửa video TikTok.</li><li>`CREATIVE_CENTER_VIDEO_TEMPLATE`: Creative Center - Mẫu video.</li><li>`DYNAMIC_SCENE`: Phân cảnh động.</li><li>`SMART_OPTIMIZATION_TOOL`: Công cụ tối ưu hóa thông minh.</li></ul><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu không thể xác định nguồn tài sản của video, giá trị trường này có thể là null.</p> |
###| placement | string[] | Vị trí hiển thị quảng cáo của video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`PLACEMENT_TIKTOK`: TikTok.</li><li>`PLACEMENT_PANGLE`: Pangle.</li><li>`PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle.</li></ul> |
###| identity | string | Loại danh tính được sử dụng để phân phối video. <br><br>Các giá trị enum hỗ trợ: <ul><li>`SPARK_ADS`: Danh tính Spark Ads, bao gồm Authorized User, TikTok User và người dùng tài khoản TikTok trong Business Center.</li><li>`NON_SPARK_ADS`: Danh tính non-Spark Ads, tức là danh tính Custom User.</li></ul> <br>Để tìm hiểu thêm về các loại danh tính, xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
###| currency | string | Mã tiền tệ mà dữ liệu chỉ số trong `metrics` được tính toán. <br><br>Ví dụ: USD. <br><br>Để tìm hiểu về đơn vị tiền tệ tương ứng với mã tiền tệ, xem [Tỷ lệ xác minh ngân sách và độ chính xác của từng loại tiền tệ](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |

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
                "metrics": {
                    "impressions": "63727",
                    "cpm": "10.27",
                    "ctr": "0.38",
                    "organic_video_views": null,
                    "clicks": "243",
                    "cpc": "2.69",
                    "spend": "654.39",
                    "conversion_rate_v2": "0.01",
                    "conversion": "6",
                    "cost_per_conversion": "109.07"
                },
                "info": {
                    "material_name": "{{material_name}}",
                    "identity": "NON_SPARK_ADS",
                    "placement": [
                        "PLACEMENT_TIKTOK"
                    ],
                    "video_material_source": "UPLOADED_TO_TIKTOK_ADS_MANAGER",
                    "currency": "USD",
                    "country_code": [
                        "CA",
                        "US"
                    ],
                    "create_time": "2024-01-11T07:42:46Z",
                    "material_id": "{{material_id}}"
                }
            },
            {
                "metrics": {
                    "impressions": "200626",
                    "cpm": "4.62",
                    "ctr": "1.36",
                    "organic_video_views": "58242.0",
                    "clicks": "2732",
                    "cpc": "0.34",
                    "spend": "927.25",
                    "conversion_rate_v2": "0.01",
                    "conversion": "17",
                    "cost_per_conversion": "54.54"
                },
                "info": {
                    "material_name": "{{material_name}}",
                    "tiktok_item_ids": [
                        "{{tiktok_item_id}}"
                    ],
                    "identity": "SPARK_ADS",
                    "placement": [
                        "PLACEMENT_TIKTOK"
                    ],
                    "video_material_source": null,
                    "currency": "USD",
                    "country_code": [
                        "CA",
                        "US"
                    ],
                    "create_time": "2023-09-25T08:47:43Z",
                    "material_id": "{{material_id}}"
                }
            }
        ],
        "page_info": {
            "total_number": 2,
            "total_page": 1,
            "page_size": 10,
            "page": 1
        }
    }
}
```

---

<a id="doc-1789703614085122"></a>
<!-- doc_id: 1789703614085122 -->
<!-- doc_id: 1789703614085122 -->
# Các chỉ số được hỗ trợ trong báo cáo Video Insights (Supported metrics in Video Insights reports)
> Đường dẫn: API Reference > Creative Reports > Video Insights reports > Supported metrics in Video Insights reports
Bạn có thể sử dụng các chỉ số sau trong báo cáo Video Insights. Lưu ý rằng hiện tại chúng tôi chưa hỗ trợ toàn bộ các chỉ số Video Insights có sẵn trên Trình quản lý quảng cáo TikTok (TikTok Ads Manager).

## Các chỉ số dữ liệu cơ bản (Basic Data Metrics)
Các chỉ số dữ liệu cơ bản là dữ liệu về chi tiêu và hiệu suất của các quảng cáo sử dụng video đó.

| Tên chỉ số (Metric Name) | Kiểu dữ liệu | Mô tả | Chi tiết |
|---|---|---|---|
| spend | string | Tổng chi phí | Ước tính tổng số tiền bạn đã chi tiêu cho chiến dịch, nhóm quảng cáo hoặc quảng cáo trong thời gian phát. |
| cpc | string | CPC | Số tiền trung bình bạn đã chi cho mỗi lượt nhấp trả phí. |
| cpm | string | CPM | Số tiền trung bình bạn đã chi cho mỗi 1.000 lượt hiển thị trả phí. |
| impressions | string | Lượt hiển thị | Số lần quảng cáo của bạn xuất hiện trên màn hình. |
| clicks | string | Lượt nhấp | Số lượt nhấp vào quảng cáo của bạn. |
| ctr | string | CTR | Tỷ lệ phần trăm số lần mọi người nhìn thấy quảng cáo của bạn và thực hiện nhấp chuột. |
| conversion | string | Lượt chuyển đổi | Số lần quảng cáo của bạn đạt được kết quả dựa trên mục tiêu và cài đặt bạn đã chọn. Tổng số được tính dựa trên thời điểm diễn ra mỗi lượt hiển thị quảng cáo. |
| cost_per_conversion | string | CPA | Số tiền trung bình bạn đã chi cho mỗi lượt chuyển đổi trả phí. Tổng số được tính dựa trên thời điểm diễn ra mỗi lượt hiển thị quảng cáo. |
| conversion_rate_v2 | string | CVR (Hiển thị) | Tỷ lệ phần trăm lượt chuyển đổi trên tổng số lượt hiển thị quảng cáo của bạn. Tổng số được tính dựa trên thời điểm diễn ra mỗi lượt hiển thị quảng cáo. |
| real_time_conversion | string | Chuyển đổi theo thời gian thực | Số lần quảng cáo trả phí của bạn đạt được kết quả dựa trên mục tiêu và cài đặt bạn đã chọn. |
| real_time_cost_per_conversion | string | CPA theo thời gian thực | Số tiền trung bình bạn đã chi cho mỗi lượt chuyển đổi trả phí. Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| real_time_conversion_rate_v2 | string | CVR theo thời gian thực (Hiển thị) | Tỷ lệ phần trăm lượt chuyển đổi trên tổng số lượt hiển thị quảng cáo của bạn. Tổng số dựa trên thời điểm lượt chuyển đổi thực tế diễn ra. |
| result | string | Kết quả | Số lần quảng cáo trả phí của bạn đạt được kết quả, dựa trên mục tiêu tối ưu hóa bạn đã chọn. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. Vui lòng vào cấp nhóm quảng cáo hoặc quảng cáo để xem kết quả. |
| cost_per_result | string | Chi phí trên mỗi kết quả | Chi phí trung bình cho mỗi kết quả đạt được từ quảng cáo của bạn. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. Vui lòng vào cấp nhóm quảng cáo hoặc quảng cáo để xem chi phí trên mỗi kết quả. |
| result_rate | string | Tỷ lệ kết quả | Tỷ lệ phần trăm kết quả bạn đạt được trên tổng số lượt xem/lượt nhấp vào quảng cáo của bạn. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. Vui lòng vào cấp nhóm quảng cáo hoặc quảng cáo để xem tỷ lệ kết quả. |
| real_time_result | string | Kết quả theo thời gian thực | Số lần quảng cáo trả phí của bạn đạt được kết quả theo thời gian thực, dựa trên mục tiêu tối ưu hóa bạn đã chọn. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. |
| real_time_cost_per_result | string | Chi phí trên mỗi kết quả theo thời gian thực | Chi phí trung bình cho mỗi kết quả từ quảng cáo của bạn theo thời gian thực. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. |
| real_time_result_rate | string | Tỷ lệ kết quả theo thời gian thực | Tỷ lệ phần trăm kết quả bạn đạt được trên tổng số lượt xem/lượt nhấp vào quảng cáo theo thời gian thực. Vì một chiến dịch có thể có nhiều mục tiêu tối ưu hóa khác nhau, thống kê này không hỗ trợ ở cấp chiến dịch. |
| secondary_goal_result | string | Kết quả mục tiêu phụ | Số lần quảng cáo của bạn mang lại kết quả dự kiến dựa trên mục tiêu phụ bạn đã chọn. |
| secondary_goal_result_rate | string | Tỷ lệ kết quả mục tiêu phụ | Tỷ lệ phần trăm kết quả mục tiêu phụ diễn ra trên tổng số lượt hiển thị quảng cáo của bạn. |
| cost_per_secondary_goal_result | string | Chi phí trên mỗi kết quả mục tiêu phụ | Chi phí trung bình cho mỗi kết quả mục tiêu phụ từ quảng cáo của bạn. |
| skan_result | string | Kết quả (SKAN) | Số lần quảng cáo của bạn đạt được kết quả, dựa trên mục tiêu tối ưu hóa bạn đã chọn. Do giới hạn của SKAdNetwork (SKAN), dữ liệu có thể không đầy đủ. |
| skan_cost_per_result | string | Chi phí trên mỗi kết quả (SKAN) | Chi phí trung bình cho mỗi kết quả từ quảng cáo của bạn. Do giới hạn của SKAdNetwork (SKAN), dữ liệu có thể chỉ là một phần. |
| skan_result_rate | string | Tỷ lệ kết quả (SKAN) | Tỷ lệ phần trăm kết quả đạt được trên tổng số lượt xem/lượt nhấp vào quảng cáo của bạn. Do giới hạn của SKAdNetwork (SKAN), dữ liệu có thể không đầy đủ. |
| skan_conversion | string | Lượt chuyển đổi (SKAN) | Số lần quảng cáo của bạn đạt được kết quả dựa trên mục tiêu và cài đặt bạn đã chọn. Dữ liệu có thể chỉ là một phần do giới hạn SKAdNetwork (SKAN). |
| skan_cost_per_conversion | string | CPA (SKAN) | Số tiền trung bình bạn đã chi cho mỗi lượt chuyển đổi. Dữ liệu có thể chỉ là một phần do giới hạn SKAdNetwork (SKAN). |
| skan_conversion_rate_v2 | string | CVR (SKAN, hiển thị) | Tỷ lệ phần trăm lượt chuyển đổi trên tổng số lượt hiển thị quảng cáo của bạn. Dữ liệu có thể không đầy đủ do giới hạn SKAdNetwork (SKAN). |

## Các chỉ số phát video (Video Play Metrics)
Các chỉ số phát video là dữ liệu về hiệu suất lượt xem của video.

| Tên chỉ số (Metric Name) | Kiểu dữ liệu | Mô tả | Chi tiết |
|---|---|---|---|
| video_play_actions | string | Lượt xem video trả phí | Số lần video của bạn được phát qua lưu lượng truy cập trả phí. Không tính lượt phát lại. |
| organic_video_views | string | Lượt xem video tự nhiên | Số lần video của bạn được phát từ lưu lượng truy cập tự nhiên, không tính lượt phát lại. ⏎ Dữ liệu này khả dụng sau khi quảng cáo trả phí chạy, nhưng sẽ dừng khi quảng cáo ngừng hoạt động hơn 7 ngày. ⏎ **Lưu ý**: • Chỉ có dữ liệu sau ngày 21/01/2020. • Không hỗ trợ lọc theo vị trí (`country_code`) khi yêu cầu chỉ số này. |
| video_watched_2s | string | Lượt xem video 2 giây | Số lần video của bạn được phát ít nhất 2 giây. Không tính lượt phát lại. |
| video_watched_6s | string | Lượt xem video 6 giây | Số lần video của bạn được phát ít nhất 6 giây, hoặc được phát toàn bộ. Không tính lượt phát lại. |
| video_views_p100 | string | Lượt xem video 100% | Số lần video của bạn được phát đến 100% thời lượng. Không tính lượt phát lại. |
| video_views_p75 | string | Lượt xem video 75% | Số lần video của bạn được phát đến 75% thời lượng. Không tính lượt phát lại. |
| video_views_p50 | string | Lượt xem video 50% | Số lần video của bạn được phát đến 50% thời lượng. Không tính lượt phát lại. Hiện không bao gồm dữ liệu từ Pangle. |
| video_views_p25 | string | Lượt xem video 25% | Số lần video của bạn được phát đến 25% thời lượng. Không tính lượt phát lại. |
| average_video_play | string | Thời gian xem trung bình mỗi lượt xem | Thời gian trung bình video của bạn được phát trên mỗi lượt xem video đơn lẻ, bao gồm cả thời gian xem lại. |

## Các chỉ số tương tác (Engagement Metrics)
Các chỉ số tương tác, chẳng hạn như số lượt thích và bình luận, là dữ liệu về cách mọi người tương tác với video của bạn.

| Tên chỉ số (Metric Name) | Kiểu dữ liệu | Mô tả | Chi tiết |
|---|---|---|---|
| follows | string | Người theo dõi trả phí | Số lượng người theo dõi nhận được từ lưu lượng truy cập trả phí trong vòng 1 ngày kể từ khi nhìn thấy quảng cáo trả phí này. Việc hủy theo dõi có thể làm giảm số lượng này. Chỉ số này chỉ áp dụng cho Spark Ads. |
| likes | string | Lượt thích trả phí | Số lượt thích video của bạn nhận được từ người dùng trong vòng 1 ngày kể từ khi nhìn thấy quảng cáo trả phí này. Việc bỏ thích có thể làm giảm số lượng này. |
| comments | string | Bình luận trả phí | Số lượng bình luận video sáng tạo của bạn nhận được trong vòng 1 ngày kể từ khi người dùng xem quảng cáo trả phí. |
| shares | string | Lượt chia sẻ trả phí | Số lần video của bạn được mọi người chia sẻ trong vòng 1 ngày kể từ khi nhìn thấy quảng cáo trả phí này. |
| profile_visits | string | Lượt truy cập hồ sơ trả phí | Số lượt truy cập hồ sơ mà quảng cáo trả phí mang lại trong chiến dịch. Chỉ số này chỉ dành cho Spark Ads. |
| profile_visits_rate | string | Tỷ lệ truy cập hồ sơ trả phí | Tỷ lệ lượt truy cập hồ sơ trên mỗi lượt hiển thị mà quảng cáo trả phí mang lại trong chiến dịch. Chỉ số này chỉ dành cho Spark Ads. |
| earned_page_video_views | string | Lượt xem video trang lan truyền (Earned) | Số lần người dùng bắt đầu phát video trên trang TikTok bạn thiết lập sau khi xem quảng cáo của bạn trong cùng một phiên ứng dụng TikTok. Với mỗi lượt hiển thị video, các lượt phát được tính riêng và không tính lượt phát lại. |
| earned_page_video_views_p100 | string | Lượt xem video trang lan truyền 100% | Số lần video trên trang TikTok bạn thiết lập được phát đến 100% thời lượng sau khi xem quảng cáo của bạn trong cùng một phiên ứng dụng TikTok. Với mỗi lượt hiển thị video, các lượt phát được tính riêng và không tính lượt phát lại. |
| earned_page_clicks | string | Lượt nhấp trang lan truyền (tất cả) | Số lượt nhấp vào trang TikTok bạn thiết lập sau khi xem quảng cáo của bạn trong cùng một phiên ứng dụng TikTok. Bao gồm cả các lượt nhấp vì mục đích xã hội và tương tác. |

---

<a id="doc-1738824477276162"></a>
<!-- doc_id: 1738824477276162 -->
<!-- doc_id: 1738824477276162 -->
# Thông tin chuyên sâu về sáng tạo (Creative Insights)
> Đường dẫn: API Reference > Creative Reports > Creative Insights
Sử dụng nhóm endpoint này để lấy dữ liệu hiệu suất của quảng cáo so với điểm chuẩn ngành (benchmarks) và dữ liệu hiệu suất theo từng giây (in-second performance).

Nhóm này bao gồm các endpoint sau:
* [Lấy điểm chuẩn quảng cáo (Get ad benchmarks)](37-creative-reports.md#doc-1738824501176321)
* [Lấy hiệu suất theo từng giây (Get in-second performance)](37-creative-reports.md#doc-1738825259075586)

---

<a id="doc-1738824501176321"></a>
<!-- doc_id: 1738824501176321 -->
<!-- doc_id: 1738824501176321 -->
# Lấy điểm chuẩn quảng cáo (Get ad benchmarks)
> Đường dẫn: API Reference > Creative Reports > Creative Insights > Get ad benchmarks
Sử dụng endpoint này để lấy dữ liệu hiệu suất của quảng cáo so sánh với điểm chuẩn ngành (benchmarks).

> **Lưu ý:** Tất cả dữ liệu trả về qua endpoint này có độ trễ từ 30-48 giờ.

## Điều kiện tiên quyết trước khi bắt đầu
Đảm bảo rằng mỗi quảng cáo bạn muốn so sánh với điểm chuẩn đã tích lũy ít nhất 1.000 lượt hiển thị trong khung thời gian so sánh. Nếu quảng cáo có ít hơn 1.000 lượt hiển thị trong khung thời gian so sánh, kết quả sẽ để trống. Để kiểm tra lượt hiển thị của một quảng cáo trong một khoảng thời gian cụ thể, gọi [/report/integrated/get/](58-reporting.md#doc-1740302848100353) để tạo báo cáo. Truyền `start_date` và `end_date` đồng thời thêm chỉ số `impressions` vào trường `metrics`.

## Các chỉ số được hỗ trợ (Supported metrics)

| Chỉ số (Metric) | Mô tả chi tiết |
|---|---|
| - | - |
| cost | Chi phí (Cost) |
| click | Lượt nhấp (Clicks) |
| impression | Lượt hiển thị (Impressions) |
| conversion | Lượt chuyển đổi (Conversion) |
| cpa | Chi phí trên mỗi hành động (Cost per action) |
| cpc | Chi phí trên mỗi lượt nhấp (Cost per click) |
| cpm | Chi phí trên mỗi 1.000 lượt hiển thị (Cost per mille) |
| cpv | Chi phí trên mỗi lượt xem (Cost per view) |
| ctr | Tỷ lệ nhấp chuột (Click-through rate) |
| cvr | Tỷ lệ chuyển đổi (Conversion rate) |
| pvr | Tỷ lệ xem trang (Page view rate) |
| profile_visits_rate | Tỷ lệ truy cập trang hồ sơ (Profile visit rate) |
| video_views | Lượt xem video (Video views) |
| video_watched_2s | Lượt xem video ít nhất 2 giây |
| video_watched_6s | Lượt xem video ít nhất 6 giây |
| video_views_p25 | Lượt xem video đến 25% thời lượng |
| video_views_p50 | Lượt xem video đến 50% thời lượng |
| video_views_p75 | Lượt xem video đến 75% thời lượng |
| video_views_p100 | Lượt xem video hết 100% thời lượng |
| average_video_play | Tỷ lệ phát video trung bình |

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/report/ad_benchmark/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| compare_time_window | string | Khung thời gian so sánh (tính bằng ngày). Enum: `7` (mặc định), `14`, `30`, `60`. |
| dimensions ****(Bắt buộc)**** | string[] | Danh sách các thứ nguyên để so sánh. Cho phép từ 1-4 thứ nguyên. Enum: `LOCATION`, `AD_CATEGORY`, `EXTERNAL_ACTION`, `PLACEMENT`. |
| metrics_fields | string[] | Các chỉ số bạn muốn lấy. Mặc định tất cả các chỉ số sẽ được trả về. Xem mục **Các chỉ số được hỗ trợ** để biết danh sách chi tiết. |
| filtering ****(Bắt buộc)**** | object | Điều kiện lọc dữ liệu. Bạn phải chỉ định một và chỉ một trong ba điều kiện cho phép (`ad_ids`, `adgroup_ids`, hoặc `campaign_ids`). |
| ↳ ad_ids | string[] | Danh sách ID quảng cáo bạn muốn lấy kết quả đối chuẩn |
| ↳ adgroup_ids | string[] | Danh sách ID nhóm quảng cáo bạn muốn lấy kết quả đối chuẩn |
| ↳ campaign_ids | string[] | Danh sách ID chiến dịch bạn muốn lấy kết quả đối chuẩn |
| sort_field | string | Trường dùng để sắp xếp. Theo mặc định, kết quả sẽ được sắp xếp theo `CREATE_TIME`. |
| sort_type | string | Thứ tự sắp xếp. Enum: `ASC` (bắt đầu từ mục tạo sớm nhất), `DES` (bắt đầu từ mục tạo muộn nhất). |
| page | number | Số trang cần lấy dữ liệu |
| page_size | number | Kích thước trang (số kết quả mỗi trang) |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/report/ad_benchmark/get/?advertiser_id={{advertiser_id}}&dimensions=["LOCATION"]&filtering={{filtering}}&sort_field=AD_ID&sort_type=ASC&page=1&page_size=10&metrics_fields=["cost","impression","click","cpa"]' \
--header 'Content-Type: application/json' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã lỗi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID duy nhất của yêu cầu (Request ID) |
| data | object | Dữ liệu trả về |
| ↳ compare_date | string | Ngày thực hiện phép so sánh |
| ↳ list | object | Danh sách kết quả. ⏎ **Lưu ý**: Nếu một quảng cáo tích lũy ít hơn 1.000 lượt hiển thị trong khung thời gian so sánh (`compare_time_window`), dữ liệu chỉ số đối chuẩn sẽ để trống. |
| ↳↳ info | object | Thông tin về đối tượng cần lấy dữ liệu đối chuẩn |
| ↳↳↳ ad_id | string | ID mẫu quảng cáo |
| ↳↳↳ location | string | Mã quốc gia hoặc khu vực gồm 2 chữ cái |
| ↳↳↳ placement | string | Vị trí hiển thị (Placement) |
| ↳↳↳ ad_category | number | ID danh mục sở thích cấp 2. Để xem danh sách danh mục, xem [Lấy danh mục sở thích](70-tools-p1.md#doc-1737174348712961). ⏎ Để xác định tên tương ứng cho các ID danh mục sở thích liên quan đến trò chơi, xem [Danh mục sở thích](../15-appendix/phu-luc-p1.md#doc-1738865030529025). |
| ↳↳↳ external_action | string | Hành động bên ngoài (sự kiện chuyển đổi) của quảng cáo |
| ↳↳ metrics | object | Danh sách chỉ số và giá trị |
| ↳↳↳ metric_name | number | Các chỉ số được trả về, xác định bởi thiết lập qua `metrics_fields` trong yêu cầu. ⏎ Sau tên chỉ số là một số thập phân một chữ số, trong phạm vi giá trị [0.0, 1.0]. Con số này thể hiện mức độ hiệu quả của chỉ số hiện tại của quảng cáo khi so sánh với các quảng cáo khác xét theo các thứ nguyên (`dimensions`) bạn chỉ định trong yêu cầu. Ví dụ: `"video_watched_6s": 0.6` có nghĩa là dữ liệu chỉ số "video_watched_6s" của quảng cáo vượt trội hơn khoảng 60% tổng số quảng cáo theo các thứ nguyên đã chỉ định. ⏎ Xem mục **Các chỉ số được hỗ trợ** để biết danh sách chỉ số hỗ trợ. |
| ↳ page_info | object | Thông tin phân trang |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu |
| ↳↳ total_page | number | Tổng số trang |
| ↳↳ page_size | number | Kích thước trang (số kết quả mỗi trang). Mặc định: 10 |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "2021120912121801024524603910501234",
    "data": {
        "compare_date": "2021-12-05",
        "list": [
            {
                "info": {
                    "placement": "TIKTOK",
                    "ad_id": "1234943678835714",
                    "location": "VN",
                    "ad_category": "0",
                    "external_action": "FORM_BUTTON"
                },
                "metrics": {
                    "video_watched_6s": 0.6,
                    "video_views_p25": 0.4,
                    "click": 0.8,
                    "video_views_p100": 0.4,
                    "average_video_play": 0.2,
                    "video_views_p50": 0.4,
                    "cpm": 0.1,
                    "profile_visits_rate": 0.9,
                    "cost": 0.7,
                    "impression": 0.8,
                    "cpa": 0.8,
                    "video_views_p75": 0.4,
                    "cpv": 0.0,
                    "cpc": 0.1,
                    "cvr": 0.2,
                    "ctr": 0.4,
                    "video_watched_2s": 0.7,
                    "pvr": 0.2,
                    "conversion": 0.6,
                    "video_views": 0.8
                }
            },
            {
                "info": {
                    "ad_id": "1234003068951586"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "total_page": 1,
            "page_size": 10,
            "total_number": 2
        }
    }
}
```

---

<a id="doc-1738825259075586"></a>
<!-- doc_id: 1738825259075586 -->
<!-- doc_id: 1738825259075586 -->
# Lấy hiệu suất theo từng giây (Get in-second performance)
> Đường dẫn: API Reference > Creative Reports > Creative Insights > Get in-second performance
Sử dụng endpoint này để lấy dữ liệu hiệu suất theo từng giây (in-second performance) của quảng cáo hoặc dữ liệu Video Insights của một video.

Để tìm hiểu cách sử dụng dữ liệu Video Insights, xem [Creative insights - Dữ liệu video insights](../09-marketing-api/creatives.md#doc-1749023065231362).

> **Lưu ý:** 
> - Thông thường thời lượng của một video quảng cáo không quá 60 giây và video thường đạt hiệu suất tốt nhất trong vòng 60 giây đầu, vì vậy dữ liệu hiệu suất được cung cấp cho 60 giây đầu tiên của video. Nếu video dài hơn 60 giây (thường gặp ở video trên mạng Pangle), tất cả dữ liệu sau giây thứ 60 sẽ được cộng dồn vào giây thứ 60.
> - Tất cả dữ liệu trả về qua endpoint này có độ trễ 1 giờ.

## Các chỉ số được hỗ trợ (Supported metrics)

| Report type ⏎ (report_type) | Metric | Type | Description |
|---|---|---|---|
| `AD` | `view_count` | number[] | Số lượt xem quảng cáo nhận được trong giây hiện tại. |
| `AD` | `click_count` | number[] | Số lượt nhấp vào quảng cáo trong giây hiện tại. |
| `AD` | `slide_count` | number[] | Số lần người xem lướt từ quảng cáo sang trang hồ sơ (profile page) trong giây hiện tại. |
| `AD` | `convert_count` | number[] | Số lần người xem quảng cáo hoàn thành sự kiện chuyển đổi trong giây hiện tại. |
| `AD` | `break_count` | number[] | Số người xem dừng xem quảng cáo trong giây hiện tại. |
| `AD` | `like_count` | number[] | Số lượt thích quảng cáo nhận được trong giây hiện tại. |
| `AD` | `share_count` | number[] | Số lượt chia sẻ quảng cáo nhận được trong giây hiện tại. |
| `AD` | `comment_count` | number[] | Số lượt bình luận quảng cáo nhận được trong giây hiện tại. |
| `VIDEO` | `clicks` | integer[] | Số lượt nhấp vào video trong giây hiện tại. |
| `VIDEO` | `conversions` | integer[] | Số lần người xem video hoàn thành sự kiện chuyển đổi trong giây hiện tại. |
| `VIDEO` | `drop_off` | integer[] | Số người xem dừng xem video trong giây hiện tại. |
| `VIDEO` | `retain` | integer[] | Số người xem tiếp tục xem video trong giây hiện tại. |
| `VIDEO` | `ctr` | number[] | Tỷ lệ phần trăm số lượt nhấp nhận được trên tổng số lượt xem video trong giây hiện tại (CTR theo giây). |
| `VIDEO` | `cvr` | number[] | Tỷ lệ phần trăm lượt chuyển đổi nhận được trên tổng số lượt nhấp vào video trong giây hiện tại (CVR theo giây). |

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/report/video_performance/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| report_type | string | Loại báo cáo. ⏎ Các giá trị enum hỗ trợ: • `AD` (sắp ngừng hỗ trợ): Báo cáo cung cấp dữ liệu hiệu suất theo từng giây trên quảng cáo. • `VIDEO`: Báo cáo Video Insights về một video. Giá trị mặc định: `AD`. ⏎ **Lưu ý**: Giá trị enum `AD` sẽ ngừng hỗ trợ trong phiên bản API tiếp theo. Chúng tôi khuyến nghị bạn nên sử dụng `VIDEO`. |
| metrics_fields | string[] | Các chỉ số bạn muốn lấy. Mặc định tất cả các chỉ số được hỗ trợ cho `report_type` bạn chỉ định sẽ được trả về. Xem mục **Các chỉ số được hỗ trợ** để biết danh sách chi tiết. |
| filtering ****(Bắt buộc)**** | object | Điều kiện lọc dữ liệu. • Khi `report_type` được đặt là `AD` hoặc không truyền, bạn cần chỉ định `ad_ids`, `adgroup_ids`, hoặc `campaign_ids`. • Khi `report_type` được đặt là `VIDEO`, bạn cần chỉ định một trong hai trường `material_ids` hoặc `video_ids`. |
| ↳ ad_ids **(Điều kiện)** | string[] | Khi `report_type` được đặt là `AD` hoặc không truyền, bạn cần chỉ định `ad_ids`, `adgroup_ids`, hoặc `campaign_ids`. ⏎ Danh sách ID quảng cáo bạn muốn lấy dữ liệu hiệu suất theo giây. ⏎ **Lưu ý**: Hiện tại giới hạn số `ad_ids` bạn truyền là 200. |
| ↳ adgroup_ids **(Điều kiện)** | string[] | Khi `report_type` được đặt là `AD` hoặc không truyền, bạn cần chỉ định `ad_ids`, `adgroup_ids`, hoặc `campaign_ids`. ⏎ Danh sách ID nhóm quảng cáo bạn muốn lấy dữ liệu hiệu suất theo giây. |
| ↳ campaign_ids **(Điều kiện)** | string[] | Khi `report_type` được đặt là `AD` hoặc không truyền, bạn cần chỉ định `ad_ids`, `adgroup_ids`, hoặc `campaign_ids`. ⏎ Danh sách ID chiến dịch bạn muốn lấy dữ liệu hiệu suất theo giây. |
| ↳ material_ids **(Điều kiện)** | string[] | Khi `report_type` được đặt là `VIDEO`, bạn cần chỉ định một trong hai trường `material_ids` hoặc `video_ids`. ⏎ ID tài sản (Material ID) của video bạn muốn lấy dữ liệu Video Insights. ⏎ Kích thước tối đa: 1. |
| ↳ video_ids **(Điều kiện)** | string[] | Khi `report_type` được đặt là `VIDEO`, bạn cần chỉ định một trong hai trường `material_ids` hoặc `video_ids`. ⏎ ID video mà bạn muốn lấy dữ liệu Video Insights. ⏎ Kích thước tối đa: 1. |
| ↳ start_time | string | Chỉ hợp lệ khi `report_type` được đặt là `VIDEO`. ⏎ Nếu bạn muốn chỉ định khoảng thời gian cho dữ liệu Video Insights, bạn cần truyền cả `start_time` và `end_time`, đồng thời đặt `lifetime` là `false`. ⏎ Thời gian bắt đầu truy vấn (khoảng đóng) theo định dạng `YYYY-MM-DD hh:mm:ss` (giờ UTC+0). |
| ↳ end_time | string | Chỉ hợp lệ khi `report_type` được đặt là `VIDEO`. ⏎ Nếu bạn muốn chỉ định khoảng thời gian cho dữ liệu Video Insights, bạn cần truyền cả `start_time` và `end_time`, đồng thời đặt `lifetime` là `false`. ⏎ Thời gian kết thúc truy vấn (khoảng đóng) theo định dạng `YYYY-MM-DD hh:mm:ss` (giờ UTC+0). |
| ↳ lifetime | boolean | Chỉ hợp lệ khi `report_type` được đặt là `VIDEO`. ⏎ Nếu bạn muốn chỉ định khoảng thời gian cho dữ liệu Video Insights, bạn cần truyền cả `start_time` và `end_time`, đồng thời đặt `lifetime` là `false`. ⏎ Có thực hiện yêu cầu toàn bộ dữ liệu lịch sử cho các chỉ số hay không. ⏎ Giá trị mặc định: `true`. |
| sort_field | string | Trường dùng để sắp xếp. Theo mặc định, kết quả sẽ được sắp xếp theo `CREATE_TIME`. |
| sort_type | string | Thứ tự sắp xếp. Các giá trị enum hỗ trợ: `ASC` (bắt đầu từ mục tạo sớm nhất), `DES` (bắt đầu từ mục tạo muộn nhất). |
| page | number | Số trang hiện tại cần lấy dữ liệu. Giá trị mặc định: 1. |
| page_size | number | Kích thước trang (số kết quả mỗi trang). Phạm vi giá trị: 1-500. Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)

```http
// Request
curl --location -g --request GET 'https://business-api.tiktok.com/open_api/v1.3/report/video_performance/get/?filtering={"ad_ids":[<ad_id>]}&advertiser_id=<advertiser_id>' \
--header 'Access-Token: <ACCESS-TOKEN>'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã lỗi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID duy nhất của yêu cầu (Request ID). |
| data | object | Dữ liệu trả về. |
| ↳ list | object | Danh sách kết quả. |
| ↳↳ info | object | Thông tin về đối tượng cần lấy dữ liệu đối chuẩn. |
| ↳↳↳ ad_id | string | ID mẫu quảng cáo. |
| ↳↳↳ video_id | string | ID video. |
| ↳↳↳ duration | number | Thời lượng video (tính bằng giây). |
| ↳↳ metrics | object | Danh sách chỉ số và giá trị. |
| ↳↳↳ metric_name | number[] | Tên chỉ số và các giá trị tuần tự theo từng giây. ⏎ Ví dụ: `"share_count": [0, 0, 0, 1]` có nghĩa là quảng cáo nhận được 0 lượt chia sẻ trong 2 giây đầu tiên và 1 lượt chia sẻ ở giây thứ 3. Lưu ý giá trị đầu tiên tương ứng với giây thứ 0. ⏎ Xem mục **Các chỉ số được hỗ trợ** để biết danh sách chỉ số hỗ trợ. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu. |
| ↳↳ total_page | number | Tổng số trang. |
| ↳↳ page_size | number | Kích thước trang (số kết quả mỗi trang). Mặc định: 10. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202112091214160102452460391351BB20",
    "data": {
        "list": [
            {
                "info": {
                    "video_id": "123425gc0000c695b6bc77u1sho1s8g0",
                    "ad_id": "1234647413898242",
                    "duration": 18
                },
                "metrics": {
                    "slide_count": [
                        21,
                        7,
                        11,
                        2,
                        2,
                        1,
                        2,
                        0,
                        1,
                        0,
                        0,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "share_count": [
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "comment_count": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "convert_count": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "click_count": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ],
                    "view_count": [
                        19570,
                        14410,
                        6749,
                        4791,
                        3707,
                        2841,
                        2415,
                        1985,
                        1484,
                        1119,
                        858,
                        738,
                        658,
                        579,
                        505,
                        417,
                        311,
                        218
                    ],
                    "break_count": [
                        5160,
                        7661,
                        1958,
                        1084,
                        866,
                        426,
                        430,
                        501,
                        365,
                        261,
                        120,
                        80,
                        79,
                        74,
                        88,
                        106,
                        93,
                        92
                    ],
                    "like_count": [
                        65,
                        3567,
                        3981,
                        972,
                        413,
                        173,
                        140,
                        80,
                        86,
                        58,
                        26,
                        25,
                        14,
                        16,
                        14,
                        7,
                        14,
                        9
                    ]
                }
            }
        ],
        "page_info": {
            "page": 1,
            "total_page": 1,
            "page_size": 10,
            "total_number": 1
        }
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Báo cáo creative (Creative Reports)**:

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

