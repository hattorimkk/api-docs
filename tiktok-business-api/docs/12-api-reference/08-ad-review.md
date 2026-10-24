# Duyệt quảng cáo (Ad Review)

Nhóm API Duyệt quảng cáo (Ad Review API) cho phép bạn tra cứu thông tin xét duyệt chi tiết cho các nhóm quảng cáo (ad groups) và quảng cáo (ads), bao gồm trạng thái duyệt, lý do từ chối và đề xuất khắc phục, hoặc gửi yêu cầu đánh giá lại (kháng nghị) sau khi bị từ chối.

Nhóm này bao gồm các endpoint sau:

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/open_api/v1.3/adgroup/review_info/` | Lấy thông tin xét duyệt của các nhóm quảng cáo |
| `GET` | `/open_api/v1.3/ad/review_info/` | Lấy thông tin xét duyệt của các quảng cáo |
| `POST` | `/open_api/v1.3/adgroup/appeal/` | Kháng nghị quyết định từ chối duyệt |

---

## Tổng quan về Duyệt quảng cáo (Ad Review)
<a id="doc-1740554223900674"></a>
<!-- doc_id: 1740554223900674 -->

Ad Review API cho phép bạn theo dõi quy trình kiểm duyệt quảng cáo tự động và thủ công của TikTok đối với nhóm quảng cáo và mẫu quảng cáo:
- Kiểm tra trạng thái duyệt (`review_status`): Đã được duyệt hoàn toàn (`ALL_AVAILABLE`), được phân phối một phần (`PART_AVAILABLE`), hoặc bị từ chối (`UNAVAILABLE`).
- Xem chi tiết nguyên nhân từ chối (`reasons`) và gợi ý điều chỉnh (`suggestion`) đối với hình ảnh, video, văn bản hay âm thanh.
- Gửi yêu cầu kháng nghị (`appeal`) khi nội dung quảng cáo tuân thủ chính sách nhưng bị hệ thống từ chối nhầm lẫn.

Danh sách các tài liệu liên quan trong nhóm:
* [Lấy thông tin duyệt của nhóm quảng cáo (Get review info of ad groups)](08-ad-review.md#doc-1740554277061634)
* [Lấy thông tin duyệt của quảng cáo (Get review info of ads)](08-ad-review.md#doc-1740559669226498)
* [Kháng nghị quyết định từ chối duyệt (Appeal a rejection)](08-ad-review.md#doc-1740571821728770)

---

## Lấy thông tin duyệt của các nhóm quảng cáo (Get review info of ad groups)
<a id="doc-1740554277061634"></a>
<!-- doc_id: 1740554277061634 -->

Sử dụng endpoint này để lấy thông tin chi tiết về quá trình xét duyệt của các nhóm quảng cáo.

Một nhóm quảng cáo cần phải được phê duyệt trước khi có thể bắt đầu phân phối, và có thể bị từ chối do nhiều nguyên nhân khác nhau, chẳng hạn như vị trí phân phối không phù hợp hoặc tùy chọn nhắm mục tiêu vi phạm chính sách. Dựa trên lý do từ chối và gợi ý nhận được, bạn có thể điều chỉnh nhóm quảng cáo cho phù hợp để được phê duyệt.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/adgroup/review_info/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập xác thực người dùng. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `adgroup_ids` **(Bắt buộc)** | string[] | Danh sách ID các nhóm quảng cáo. Hỗ trợ tối đa 20 ID nhóm quảng cáo trong mỗi yêu cầu. Dưới định dạng chuỗi JSON mã hóa URL. |
| `lang` | string | Ngôn ngữ trả về cho các lý do từ chối và đề xuất (ví dụ: `en`, `zh`, v.v.). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/adgroup/review_info/?advertiser_id=7123456789012345678&adgroup_ids=%5B%221765432109876599%22%5D&lang=en' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import json
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/review_info/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_ids": json.dumps(["1765432109876599"]),
    "lang": "en"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu kết quả phản hồi. |
| `↳ ad_review_map` | object | Cấu trúc dữ liệu xét duyệt hai chiều ở cấp độ mẫu quảng cáo (ad level). Khóa cấp 1 là `adgroup_id`. Khóa cấp 2 là `ad_id`. |
| `↳↳ ad_id` | string | ID của quảng cáo.<br>**Lưu ý:** Đối với nhóm quảng cáo Smart+ bị thất bại xét duyệt một phần hoặc toàn bộ (`review_status` trong `ad_group_review_map` là `PART_AVAILABLE` hoặc `UNAVAILABLE`), `ad_id` trong `ad_review_map` không đại diện cho một ad ID thực tế và không thể dùng với [/ad/review_info/](08-ad-review.md#doc-1740559669226498) để lấy chi tiết duyệt cấp quảng cáo. Thay vào đó, hãy coi mỗi `ad_id` như một tài nguyên sáng tạo (material) trong Smart+ Campaign. Để nắm rõ nguyên nhân từ chối, hãy kiểm tra `reject_info` trong `ad_review_map` do [/adgroup/review_info/](08-ad-review.md#doc-1740554277061634) trả về. Sau đó cập nhật Smart+ Campaign tương ứng qua [/campaign/spc/update/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334250066945). |
| `↳↳ is_approved` | boolean | Cho biết quảng cáo đã được phê duyệt hay chưa (`true`/`false`). |
| `↳↳ review_status` | string | Trạng thái xét duyệt của quảng cáo.<br>Enum: `ALL_AVAILABLE` (quảng cáo đã được duyệt và có thể phân phối bình thường), `PART_AVAILABLE` (quảng cáo đã được duyệt và chỉ có thể phân phối tại một số quốc gia mục tiêu đã chỉ định), `UNAVAILABLE` (quảng cáo đã được duyệt và không thể phân phối). |
| `↳↳ appeal_status` {-To-be-deprecated} | string | Trạng thái kháng nghị của quảng cáo.<br>**Lưu ý:** Giá trị của trường này luôn là `null`. |
| `↳↳ forbidden_placements` | string[] | Danh sách các vị trí phân phối (placements) không vượt qua xét duyệt. Enum xem tại [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi đối tượng không vượt qua xét duyệt. Enum xem tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ forbidden_locations` | string[] | Các khu vực địa lý mục tiêu không vượt qua xét duyệt. Enum xem tại [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| `↳↳ forbidden_operation_systems` | string[] | Các hệ điều hành của đối tượng khán giả không vượt qua xét duyệt. Enum xem tại [Enumeration - Operating Systems](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ last_audit_time` | string | **Lưu ý:** Giá trị của trường này luôn là `null`. Thời điểm gần nhất quảng cáo được xét duyệt. |
| `↳↳ reject_info` | object[] | Danh sách thông tin chi tiết về việc từ chối duyệt. |
| `↳↳↳ suggestion` | string | Đề xuất khắc phục sau khi xét duyệt. |
| `↳↳↳ reasons` | string[] | Danh sách các nguyên nhân từ chối xét duyệt. |
| `↳↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi bị từ chối duyệt. Enum xem tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ forbidden_locations` | string[] | Các khu vực địa lý bị từ chối duyệt. Enum xem tại [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| `↳↳↳ forbidden_placements` | string[] | Các vị trí phân phối bị từ chối duyệt. Enum xem tại [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ content_info` | object | Thông tin nội dung của quảng cáo đã được xét duyệt. |
| `↳↳↳↳ image_content` | object | Nội dung hình ảnh. |
| `↳↳↳↳↳ image_id` | string | ID của hình ảnh được xét duyệt. |
| `↳↳↳↳ video_content` | object | Nội dung video được xét duyệt. |
| `↳↳↳↳↳ video_id` | string | ID của video đang được xét duyệt. |
| `↳↳↳↳ text_content` | string | Nội dung văn bản quảng cáo. |
| `↳↳↳↳ content_type` | string | Loại nội dung được xét duyệt.<br>Enum: `MODE_STRING`, `MODE_IMAGE`, `MODE_VIDEO`, `MODE_CAROUSEL_MUSIC` (Âm nhạc trong quảng cáo Carousel). |
| `↳↳↳↳ carousel_music_content` | object | Chỉ trả về khi `content_type` là `MODE_CAROUSEL_MUSIC`. Nội dung âm nhạc trong quảng cáo Carousel đã được duyệt. |
| `↳↳↳↳↳ music_id` | string | ID của đoạn nhạc sử dụng trong quảng cáo Carousel. |
| `↳ ad_group_review_map` | object | Dữ liệu xét duyệt ở cấp độ nhóm quảng cáo, tổ chức theo `adgroup_id`. Khóa cấp 1 là `adgroup_id`. |
| `↳↳ adgroup_id` | string | ID của nhóm quảng cáo. |
| `↳↳ is_approved` | boolean | Cho biết nhóm quảng cáo đã được phê duyệt hay chưa. |
| `↳↳ review_status` | string | Trạng thái xét duyệt của nhóm quảng cáo.<br>Enum: `ALL_AVAILABLE` (nhóm quảng cáo đã được duyệt và tất cả quảng cáo bên trong đều có thể phân phối), `PART_AVAILABLE` (nhóm quảng cáo đã được duyệt và chỉ một số quảng cáo bên trong có thể phân phối), `UNAVAILABLE` (nhóm quảng cáo đã được duyệt và toàn bộ quảng cáo bên trong không thể phân phối).<br>**Lưu ý:** Xem chi tiết hướng dẫn xử lý đối với Smart+ ad group tương tự như mô tả tại `ad_review_map`. |
| `↳↳ appeal_status` | string | Trạng thái kháng nghị của nhóm quảng cáo. Enum xem tại [Enumeration - Ad Group Review Appeal Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Để kháng nghị quyết định từ chối nhóm quảng cáo, hãy gọi [/adgroup/appeal/](08-ad-review.md#doc-1740571821728770); khi đó trường này sẽ chuyển thành `APPEALING` (Đang kháng nghị). |
| `↳↳ forbidden_placements` | string[] | Danh sách các vị trí phân phối không vượt qua xét duyệt. |
| `↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi đối tượng không vượt qua xét duyệt. |
| `↳↳ forbidden_locations` | string[] | Các khu vực địa lý mục tiêu không vượt qua xét duyệt. |
| `↳↳ forbidden_operation_systems` | string[] | Các hệ điều hành của đối tượng khán giả không vượt qua xét duyệt. |
| `↳↳ last_audit_time` | string | Thời điểm gần nhất nhóm quảng cáo được xét duyệt (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. Ví dụ: `2023-01-01 00:00:00`.<br>**Lưu ý:** Trường này chỉ có giá trị thời gian xét duyệt thực tế khi nhóm quảng cáo bị từ chối (`rejected`). |
| `↳↳ contain_rejected_ads` | boolean | Cho biết có quảng cáo nào trong nhóm quảng cáo này bị từ chối hay không. |
| `↳↳ reject_info` | object[] | Chi tiết thông tin từ chối xét duyệt ở cấp nhóm quảng cáo. |
| `↳↳↳ suggestion` | string | Đề xuất khắc phục sau khi xét duyệt. |
| `↳↳↳ reasons` | string[] | Danh sách các lý do từ chối xét duyệt. |
| `↳↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi bị từ chối duyệt. Enum xem tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ forbidden_locations` | string[] | Các khu vực địa lý bị từ chối duyệt. Enum xem tại [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| `↳↳↳ forbidden_placements` | string[] | Các vị trí phân phối bị từ chối duyệt. Enum xem tại [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ content_info` | object | Nội dung quảng cáo được xét duyệt. |
| `↳↳↳↳ image_content` | object | Nội dung hình ảnh. |
| `↳↳↳↳↳ image_id` | string | ID của hình ảnh được xét duyệt. |
| `↳↳↳↳ video_content` | object | Nội dung video được xét duyệt. |
| `↳↳↳↳↳ video_id` | string | ID của video đang được xét duyệt. |
| `↳↳↳↳ text_content` | string | Văn bản quảng cáo. |
| `↳↳↳↳ content_type` | string | Loại nội dung được xét duyệt (`MODE_STRING`, `MODE_IMAGE`, `MODE_VIDEO`, `MODE_CAROUSEL_MUSIC`). |
| `↳↳↳↳ carousel_music_content` | object | Nội dung âm nhạc Carousel khi `content_type` là `MODE_CAROUSEL_MUSIC`. |
| `↳↳↳↳↳ music_id` | string | ID của bản nhạc sử dụng trong quảng cáo Carousel. |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu để theo dõi và đối soát. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "LOG_ID",
  "data": {
    "ad_review_map": {
      "1765432109876599": {
        "1765432109876588": {
          "reject_info": [
            {
              "content_info": {
                "text_content": null,
                "content_type": "MODE_VIDEO",
                "image_content": {
                  "image_id": "tos-maliva-p-0000/0ba31ad4244c48d3a61e42ea3f91649e"
                },
                "video_content": {
                  "video_id": "v09044g40000cfv0"
                }
              },
              "forbidden_locations": [
                "RU"
              ],
              "suggestion": "Please add background audio or modify the unclear audio. For more policy details, please check 'Ad Caption/Text, Image and Video' in 'TikTok Advertising Policies - Ad Creatives'.",
              "reasons": [
                "The ad or video has no background audio or the background audio is incoherent/unclear."
              ]
            }
          ],
          "is_approved": true,
          "last_audit_time": null,
          "forbidden_placements": [
            "PLACEMENT_HELO",
            "PLACEMENT_TIKTOK",
            "PLACEMENT_TOPBUZZ"
          ],
          "ad_id": "1765432109876588",
          "review_status": "PART_AVAILABLE",
          "appeal_status": null,
          "forbidden_locations": [
            "RU"
          ],
          "forbidden_operation_systems": [
            "IOS"
          ],
          "forbidden_ages": []
        }
      }
    },
    "ad_group_review_map": {
      "1765432109876599": {
        "reasons": [
          "some reason"
        ],
        "contain_rejected_ads": true,
        "is_approved": true,
        "forbidden_placements": [
          "PLACEMENT_TOPBUZZ",
          "PLACEMENT_HELO",
          "PLACEMENT_TIKTOK"
        ],
        "adgroup_id": "1765432109876599",
        "review_status": "PART_AVAILABLE",
        "appeal_status": "NOT_APPEALED",
        "forbidden_locations": [
          "RU"
        ],
        "forbidden_operation_systems": [
          "IPHONE"
        ],
        "forbidden_ages": []
      }
    }
  }
}
```


---

## Lấy thông tin duyệt của các quảng cáo (Get review info of ads)
<a id="doc-1740559669226498"></a>
<!-- doc_id: 1740559669226498 -->

Sử dụng endpoint này để lấy thông tin chi tiết về việc xét duyệt của các quảng cáo cụ thể.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/ad/review_info/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập xác thực người dùng. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `ad_ids` **(Bắt buộc)** | string[] | Danh sách ID các quảng cáo cần kiểm tra. Số lượng: 1–100 ID. Dưới định dạng chuỗi JSON mã hóa URL. |
| `lang` | string | Ngôn ngữ phản hồi cho kết quả lý do từ chối và đề xuất (ví dụ: `en`, `zh`, v.v.). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/ad/review_info/?advertiser_id=7123456789012345678&ad_ids=%5B%221765432109876588%22%5D&lang=en' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import json
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/ad/review_info/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "ad_ids": json.dumps(["1765432109876588"]),
    "lang": "en"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu kết quả phản hồi. |
| `↳ ad_review_map` | object | Dữ liệu xét duyệt ở cấp độ quảng cáo, tổ chức theo `ad_id`. |
| `↳↳ ad_id` | string | ID của quảng cáo. |
| `↳↳ is_approved` | boolean | Cho biết quảng cáo đã được phê duyệt hay chưa (`true`/`false`). |
| `↳↳ review_status` | string | Trạng thái xét duyệt của quảng cáo.<br>Enum: `ALL_AVAILABLE` (quảng cáo đã được duyệt và có thể phân phối bình thường), `PART_AVAILABLE` (quảng cáo đã được duyệt và chỉ có thể phân phối tại một số quốc gia mục tiêu đã chỉ định), `UNAVAILABLE` (quảng cáo đã được duyệt và không thể phân phối). |
| `↳↳ appeal_status` {-To-be-deprecated} | string | Trạng thái kháng nghị của quảng cáo.<br>**Lưu ý:** Giá trị của trường này luôn là `null`. |
| `↳↳ forbidden_placements` | string[] | Danh sách các vị trí phân phối không vượt qua xét duyệt. Enum xem tại [Enumeration - Ad Management - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi đối tượng không vượt qua xét duyệt. Enum xem tại [Enumeration - Audience Age Range](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ forbidden_locations` | string[] | Các khu vực địa lý mục tiêu không vượt qua xét duyệt. Enum xem tại [Appendix - location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| `↳↳ forbidden_operation_systems` | string[] | Các hệ điều hành của đối tượng khán giả không vượt qua xét duyệt. Enum xem tại [Enumeration - Audience Operating System](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳ last_audit_time` | string | **Lưu ý:** Giá trị của trường này luôn là `null`. Thời điểm gần nhất quảng cáo được xét duyệt. |
| `↳↳ reject_info` | object[] | Chi tiết thông tin về các lý do từ chối xét duyệt. |
| `↳↳↳ suggestion` | string | Đề xuất khắc phục sau khi xét duyệt. |
| `↳↳↳ reasons` | string[] | Danh sách các lý do từ chối xét duyệt. |
| `↳↳↳ forbidden_ages` | string[] | Các nhóm độ tuổi bị từ chối duyệt. Enum xem tại [Enumeration - Audience Age Range](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ forbidden_locations` | string[] | Các khu vực địa lý bị từ chối duyệt. Enum xem tại [Appendix - location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| `↳↳↳ forbidden_placements` | string[] | Các vị trí phân phối bị từ chối duyệt. Enum xem tại [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `↳↳↳ content_info` | object | Thông tin nội dung của quảng cáo đã được xét duyệt. |
| `↳↳↳↳ image_content` | object | Nội dung hình ảnh. |
| `↳↳↳↳↳ image_id` | string | ID của hình ảnh được xét duyệt. |
| `↳↳↳↳ video_content` | object | Nội dung video được xét duyệt. |
| `↳↳↳↳↳ video_id` | string | ID của video đang được xét duyệt. |
| `↳↳↳↳ text_content` | string | Văn bản quảng cáo. |
| `↳↳↳↳ content_type` | string | Loại nội dung được xét duyệt.<br>Enum: `MODE_STRING`, `MODE_IMAGE`, `MODE_VIDEO`, `MODE_CAROUSEL_MUSIC` (Âm nhạc trong quảng cáo Carousel). |
| `↳↳↳↳ carousel_music_content` | object | Chỉ trả về khi `content_type` là `MODE_CAROUSEL_MUSIC`. Nội dung âm nhạc trong quảng cáo Carousel đã được duyệt. |
| `↳↳↳↳↳ music_id` | string | ID của bản nhạc sử dụng trong quảng cáo Carousel. |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu để theo dõi và đối soát. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "LOG_ID",
  "data": {
    "ad_review_map": {
      "1765432109876588": {
        "reject_info": [
          {
            "content_info": {
              "text_content": null,
              "content_type": "MODE_VIDEO",
              "image_content": {
                "image_id": "tos-maliva-p-0000/0ba31ad4244c48d3a61e42ea3f91649e"
              },
              "video_content": {
                "video_id": "v09044g40000cfv0"
              }
            },
            "suggestion": "Please add background audio or modify the unclear audio. For more policy details, please check 'Ad Caption/Text, Image and Video' in 'TikTok Advertising Policies - Ad Creatives'.",
            "reasons": [
              "The ad or video has no background audio or the background audio is incoherent/unclear."
            ]
          }
        ],
        "is_approved": true,
        "last_audit_time": null,
        "forbidden_placements": [
          "PLACEMENT_HELO",
          "PLACEMENT_TIKTOK",
          "PLACEMENT_TOPBUZZ"
        ],
        "ad_id": "1765432109876588",
        "review_status": "PART_AVAILABLE",
        "appeal_status": null,
        "forbidden_locations": [
          "RU"
        ],
        "forbidden_operation_systems": [
          "IOS"
        ],
        "forbidden_ages": []
      }
    }
  }
}
```

---

## Kháng nghị quyết định từ chối duyệt (Appeal a rejection)
<a id="doc-1740571821728770"></a>
<!-- doc_id: 1740571821728770 -->

Sử dụng endpoint này để kháng nghị quyết định từ chối duyệt, tức là yêu cầu đánh giá lại nhóm quảng cáo khi nhóm quảng cáo của bạn bị từ chối trong quá trình xét duyệt.

Sau khi gửi kháng nghị, bạn cần đợi một khoảng thời gian rồi gọi lại endpoint [/adgroup/review_info/](08-ad-review.md#doc-1740554277061634) để kiểm tra trạng thái kháng nghị (`appeal_status`) và xem trạng thái duyệt (`review_status`) đã được cập nhật hay chưa.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/adgroup/appeal/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập xác thực người dùng. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị cố định: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `adgroup_id` **(Bắt buộc)** | string | ID của nhóm quảng cáo cần gửi kháng nghị. |
| `ad_id` | string | ID của quảng cáo. Không bắt buộc. |
| `appeal_reason` | string | Lý do giải trình cho yêu cầu kháng nghị. |
| `attachment_list` | string[] | Danh sách liên kết tài liệu/hình ảnh chứng minh đính kèm. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/appeal/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "adgroup_id": "1765432109876599",
    "ad_id": "1765432109876588",
    "appeal_reason": "The creative complies with TikTok advertising policy guidelines.",
    "attachment_list": [
      "https://example.com/certificates/license.pdf"
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/appeal/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_id": "1765432109876599",
    "ad_id": "1765432109876588",
    "appeal_reason": "The creative complies with TikTok advertising policy guidelines.",
    "attachment_list": [
        "https://example.com/certificates/license.pdf"
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi gửi kháng nghị thành công). |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu để theo dõi và đối soát. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "data": {},
  "request_id": "2020031110223101018904922300361F64"
}
```
