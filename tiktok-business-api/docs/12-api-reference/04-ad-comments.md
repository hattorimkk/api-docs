# Bình luận quảng cáo (Ad Comments)
<a id="doc-1738086266983426"></a>
<!-- doc_id: 1738086266983426 -->

Đối với các quảng cáo video tiêu chuẩn hoặc Spark Ads được tạo bởi những người dùng đã liên kết với Tài khoản Doanh nghiệp TikTok (TikTok Business Account), nếu bạn đã bật tính năng bình luận, bạn có thể quản lý các bình luận bên dưới quảng cáo bằng Ad Comments API. Bạn có thể lấy danh sách bình luận, cập nhật trạng thái ẩn/hiện, phản hồi, xóa, hoặc tạo tác vụ xuất dữ liệu bình luận.

Bạn cũng có thể thiết lập danh sách từ khóa bị chặn (blocked words). Nếu một bình luận chứa từ khóa bị chặn, bình luận đó sẽ bị ẩn với tất cả mọi người ngoại trừ chính người đã đăng bình luận. Để xem các endpoint quản lý từ khóa bị chặn, hãy xem [Ad Comments - Blocked Words](05-ad-comments-blocked-words.md#doc-1739029198660609).

Nhóm API này bao gồm các endpoint sau:
* [Lấy danh sách bình luận](04-ad-comments.md#doc-1738086301876225)
* [Lấy bình luận liên quan](04-ad-comments.md#doc-1738086824859650)
* [Cập nhật trạng thái bình luận](04-ad-comments.md#doc-1738086844585985)
* [Trả lời bình luận](04-ad-comments.md#doc-1738957702411265)
* [Xóa bình luận](04-ad-comments.md#doc-1738957772267522)
* [Tạo tác vụ xuất bình luận](04-ad-comments.md#doc-1738088144215041)
* [Kiểm tra trạng thái tác vụ xuất bình luận](04-ad-comments.md#doc-1738088242659330)
* [Tải về dữ liệu bình luận đã xuất](04-ad-comments.md#doc-1738088341958658)

---

## Lấy danh sách bình luận (`Get comments`)
<a id="doc-1738086301876225"></a>
<!-- doc_id: 1738086301876225 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/comment/list/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách bình luận bên dưới các quảng cáo video của một tài khoản quảng cáo. Bạn cần chỉ định điều kiện tìm kiếm và khoảng thời gian cho các bình luận muốn lấy. Endpoint này hỗ trợ trả về bình luận cho cả quảng cáo trả phí thông thường và Spark Ads.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| search_field | string | Bắt buộc | Trường dùng để tìm kiếm lọc bình luận. Giá trị enum: • `ADGROUP_ID`: Lọc theo ID nhóm quảng cáo. |
| search_value | string | Bắt buộc | Giá trị tìm kiếm. Khi `search_field` là `ADGROUP_ID`, truyền ID nhóm quảng cáo vào trường này. Lấy danh sách nhóm quảng cáo qua [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922). |
| start_time | string | Bắt buộc | Ngày bắt đầu của khoảng thời gian cần lấy bình luận, định dạng `YYYY-MM-DD`. |
| end_time | string | Bắt buộc | Ngày kết thúc của khoảng thời gian cần lấy bình luận, định dạng `YYYY-MM-DD`. |
| comment_type | string[] | Không bắt buộc | Loại bình luận. Giá trị enum: `ALL`, `COMMENT`, `REPLY`. Mặc định: `["ALL"]`. |
| comment_status | string[] | Không bắt buộc | Trạng thái bình luận: `ALL`, `PUBLIC`, `HIDDEN`. |
| hit_blockedword | boolean | Không bắt buộc | Lọc bình luận có chứa từ khóa bị chặn hay không. |
| sort_field | string | Không bắt buộc | Trường dùng để sắp xếp kết quả. Giá trị enum: • `CREATE_TIME`: Thời gian tạo.<br>• `LIKES`: Số lượt thích.<br>• `REPLIES`: Số lượt trả lời.<br>Mặc định: `CREATE_TIME`. |
| sort_type | string | Không bắt buộc | Thứ tự sắp xếp. Giá trị enum: `ASC` (tăng dần), `DESC` (giảm dần). Mặc định: `DESC`. |
| page | number | Không bắt buộc | Số trang hiện tại. Giá trị: ≥ 1. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-100. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "search_field=ADGROUP_ID" --data-urlencode "search_value=1723456789012345" --data-urlencode "start_time=2026-05-01" --data-urlencode "end_time=2026-05-30" --data-urlencode 'comment_type=["ALL"]' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/comment/list/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/comment/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "search_field": "ADGROUP_ID",
    "search_value": "1723456789012345",
    "start_time": "2026-05-01",
    "end_time": "2026-05-30",
    "comment_type": json.dumps(["ALL"]),
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã định danh duy nhất của yêu cầu để tra cứu nhật ký. |
| data | object | Dữ liệu trả về. |
| ↳ comments | object[] | Danh sách bình luận. |
| ↳↳ comment_id | string | ID bình luận. |
| ↳↳ content | string | Nội dung bình luận. |
| ↳↳ likes | number | Số lượt thích bình luận. |
| ↳↳ replies | number | Số lượt trả lời bình luận. |
| ↳↳ comment_type | string | Loại bình luận: `COMMENT` (bình luận gốc) hoặc `REPLY` (câu trả lời cho bình luận gốc). |
| ↳↳ original_comment_id | string | ID của bình luận gốc. Chỉ trả về khi `comment_type` là `REPLY`. |
| ↳↳ comment_status | string | Trạng thái bình luận: `PUBLIC` (công khai), `HIDDEN` (bị ẩn). |
| ↳↳ hit_blockedword | boolean | Cho biết bình luận có chứa từ khóa bị chặn hay không. |
| ↳↳ is_pinned | boolean | Bình luận có được ghim lên đầu hay không. |
| ↳↳ can_delete | boolean | Bình luận có thể bị xóa bởi tài khoản hiện tại hay không. |
| ↳↳ create_time | string | Thời gian bình luận được tạo. |
| ↳↳ user_id | string | ID của người dùng TikTok đã đăng bình luận. |
| ↳↳ user_name | string | Tên người dùng TikTok. |
| ↳↳ user_avatar_url | string | URL ảnh đại diện của người dùng. |
| ↳↳ identity_id | string | ID danh tính liên kết. |
| ↳↳ identity_type | string | Loại danh tính: `CUSTOMIZED_USER`, `TT_USER`. Xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ is_auth_ttba | boolean | Người dùng có liên kết với TikTok Business Account hay không. |
| ↳↳ is_auth_comment_manage_scope | boolean | Người dùng có quyền quản lý bình luận hay không. |
| ↳↳ ad_id | string | ID quảng cáo chứa bình luận. |
| ↳↳ ad_name | string | Tên quảng cáo chứa bình luận. |
| ↳↳ ad_text | string | Tiêu đề/văn bản quảng cáo. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo chứa bình luận. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ campaign_id | string | ID chiến dịch chứa bình luận. |
| ↳↳ campaign_name | string | Tên chiến dịch. |
| ↳↳ app | string | App ID ứng dụng được quảng bá. |
| ↳↳ tiktok_item_id | string | ID video TikTok liên kết (Spark Ads). |
| ↳↳ video_play_url | string | URL phát video quảng cáo. |
| ↳↳ video_cover_url | string | URL ảnh bìa video quảng cáo. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi mỗi trang. |
| ↳↳ total_number | number | Tổng số bình luận tìm thấy. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "comments": [
      {
        "comment_id": "6917508027378253825",
        "content": "Sản phẩm dùng rất thích, đóng gói cẩn thận!",
        "likes": 5,
        "replies": 1,
        "comment_type": "COMMENT",
        "original_comment_id": null,
        "comment_status": "PUBLIC",
        "hit_blockedword": false,
        "is_pinned": false,
        "can_delete": false,
        "create_time": "2026-05-14 07:04:16 +0000 UTC",
        "user_id": "6123456789123456789",
        "user_name": "nguyenvana",
        "user_avatar_url": "https://p16-va.tiktokcdn.com/avatar.jpeg",
        "identity_id": "123456789",
        "identity_type": "TT_USER",
        "is_auth_ttba": true,
        "is_auth_comment_manage_scope": true,
        "ad_id": "1684147917059121",
        "ad_name": "Ad Name Mùa Hè",
        "ad_text": "Khuyến mãi hấp dẫn",
        "adgroup_id": "1684147923311633",
        "adgroup_name": "Ad Group 1",
        "campaign_id": "1684147923311617",
        "campaign_name": "Summer Campaign",
        "app": null,
        "tiktok_item_id": "7001234567890123456",
        "video_play_url": "https://v16-webapp.tiktok.com/video.mp4",
        "video_cover_url": "https://p16-va.tiktokcdn.com/cover.jpeg"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

## Lấy bình luận liên quan (`Get related comments`)
<a id="doc-1738086824859650"></a>
<!-- doc_id: 1738086824859650 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/comment/reference/`

**Mục đích**: Sử dụng endpoint này để lấy các bình luận liên quan. Đối với một bình luận gốc, bạn có thể lấy chính bình luận đó và toàn bộ các phản hồi (replies) bên dưới nó. Đối với một phản hồi, bạn có thể lấy phản hồi đó cùng với bình luận gốc của nó.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| comment_id | string | Bắt buộc | ID bình luận cần tra cứu. |
| comment_type | string | Bắt buộc | Loại bình luận: `COMMENT` (bình luận gốc) hoặc `REPLY` (câu trả lời). |
| original_comment_id | string | Không bắt buộc | ID của bình luận gốc. Chỉ áp dụng khi `comment_type` là `REPLY`. |
| page | number | Không bắt buộc | Số trang hiện tại. Giá trị: ≥ 1. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-1000. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "comment_id=6917508027378253825" --data-urlencode "comment_type=COMMENT" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/comment/reference/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/comment/reference/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "comment_id": "6917508027378253825",
    "comment_type": "COMMENT",
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ comments | object[] | Danh sách bình luận và phản hồi liên quan. |
| ↳↳ comment_id | string | ID bình luận. |
| ↳↳ content | string | Nội dung bình luận. |
| ↳↳ comment_type | string | Loại bình luận: `COMMENT` hoặc `REPLY`. |
| ↳↳ comment_status | string | Trạng thái: `PUBLIC`, `HIDDEN`. |
| ↳↳ hit_blockedword | boolean | Có chứa từ khóa bị chặn hay không. |
| ↳↳ create_time | string | Thời gian tạo bình luận. |
| ↳↳ user_name | string | Tên người dùng đăng bình luận. |
| ↳↳ user_id | string | ID người dùng TikTok đăng bình luận. |
| ↳↳ user_avatar_url | string | URL ảnh đại diện của người dùng. |
| ↳↳ reply_user_info | object | Thông tin người dùng của bình luận gốc được trả lời. Chỉ hợp lệ đối với câu trả lời (bình luận cấp 2 trở xuống); trả về `null` cho bình luận cấp 1. |
| ↳↳ is_pinned | boolean | Bình luận có được ghim hay không. |
| ↳↳ can_delete | boolean | Có thể xóa bình luận hay không. |
| ↳↳ identity_id | string | ID danh tính. |
| ↳↳ identity_type | string | Loại danh tính: `CUSTOMIZED_USER`, `TT_USER`. Xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ is_auth_ttba | boolean | Người dùng có liên kết với TikTok Business Account hay không. |
| ↳↳ is_auth_comment_manage_scope | boolean | Có quyền quản lý bình luận hay không. |
| ↳↳ original_comment_id | string | ID của bình luận gốc. |
| ↳↳ tiktok_item_id | string | ID video TikTok liên kết (Spark Ads). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số bình luận. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Cập nhật trạng thái bình luận (`Update the statuses of comments`)
<a id="doc-1738086844585985"></a>
<!-- doc_id: 1738086844585985 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/comment/status/update/`

**Mục đích**: Sử dụng endpoint này để thay đổi trạng thái của một danh sách bình luận từ công khai (public) sang bị ẩn (hidden), hoặc ngược lại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| comment_ids | string[] | Bắt buộc | Danh sách các ID bình luận cần cập nhật trạng thái. |
| operation | string | Bắt buộc | Loại thao tác cập nhật. Các giá trị enum:<br>• `HIDDEN`: Đổi trạng thái bình luận thành bị ẩn.<br>• `PUBLIC`: Đổi trạng thái bình luận thành công khai. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/comment/status/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "comment_ids": ["6917508027378253825"],
  "operation": "PUBLIC"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```

---

## Trả lời bình luận (`Reply to a comment`)
<a id="doc-1738957702411265"></a>
<!-- doc_id: 1738957702411265 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/comment/post/`

**Mục đích**: Sử dụng endpoint này để trả lời một bình luận bên dưới quảng cáo. Đối với các quảng cáo TikTok được tạo bởi người dùng liên kết với loại danh tính TikTok User hoặc Custom User (`identity_type` = `TT_USER` hoặc `CUSTOMIZED_USER`), người dùng có quyền quản lý bình luận có thể trả lời các bình luận cấp 1 bên dưới quảng cáo.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| ad_id | string | Bắt buộc | ID quảng cáo chứa bình luận. |
| tiktok_item_id | string | Bắt buộc | ID video TikTok của bài đăng quảng cáo. |
| comment_id | string | Bắt buộc | ID của bình luận mà bạn muốn trả lời. |
| comment_type | string | Bắt buộc | Loại bình luận. Hiện tại chỉ hỗ trợ giá trị `REPLY`. |
| text | string | Bắt buộc | Nội dung văn bản của câu trả lời. |
| identity_type | string | Bắt buộc | Loại danh tính liên kết với người dùng: `CUSTOMIZED_USER` (Người dùng tùy chỉnh) hoặc `TT_USER` (Người dùng TikTok). Xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| identity_id | string | Bắt buộc | ID danh tính. |

### Ví dụ

```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" -H "Content-Type: application/json" -X POST -d '{
    "advertiser_id": "7123456789012345678",
    "ad_id": "1684147917059121",
    "tiktok_item_id": "7001234567890123456",
    "comment_id": "6917508027378253825",
    "comment_type": "REPLY",
    "text": "Cảm ơn bạn đã ủng hộ sản phẩm của chúng tôi!",
    "identity_type": "TT_USER",
    "identity_id": "123456789"
}' https://business-api.tiktok.com/open_api/v1.3/comment/post/
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về sau khi đăng câu trả lời. |
| ↳ comment_id | string | ID của câu trả lời vừa được tạo thành công. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "comment_id": "6917509999999999999"
  }
}
```

---

## Xóa bình luận (`Delete a comment`)
<a id="doc-1738957772267522"></a>
<!-- doc_id: 1738957772267522 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/comment/delete/`

**Mục đích**: Sử dụng endpoint này để xóa một bình luận. Đối với người dùng đã thêm bình luận vào các quảng cáo TikTok tạo bởi danh tính Custom User hoặc TikTok User (`identity_type` = `CUSTOMIZED_USER` hoặc `TT_USER`), họ có thể xóa bình luận của chính mình.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| ad_id | string | Bắt buộc | ID quảng cáo chứa bình luận. |
| tiktok_item_id | string | Bắt buộc | ID video TikTok liên kết với quảng cáo. |
| comment_id | string | Bắt buộc | ID của bình luận cần xóa. |
| identity_type | string | Bắt buộc | Loại danh tính: `CUSTOMIZED_USER` hoặc `TT_USER`. Xem [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| identity_id | string | Bắt buộc | ID danh tính. |

### Ví dụ

```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" -H "Content-Type: application/json" -X POST -d '{
    "advertiser_id": "7123456789012345678",
    "ad_id": "1684147917059121",
    "tiktok_item_id": "7001234567890123456",
    "comment_id": "6917509999999999999",
    "identity_type": "TT_USER",
    "identity_id": "123456789"
}' https://business-api.tiktok.com/open_api/v1.3/comment/delete/
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```

---

## Tạo tác vụ xuất bình luận (`Create a comment export task`)
<a id="doc-1738088144215041"></a>
<!-- doc_id: 1738088144215041 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/comment/task/create/`

**Mục đích**: Sử dụng endpoint này để tạo một tác vụ xuất bình luận bất đồng bộ. Sau khi tác vụ được tạo, bạn dùng [/comment/task/check/](04-ad-comments.md#doc-1738088242659330) để theo dõi trạng thái tác vụ. Khi tác vụ hoàn tất thành công, bạn gọi [/comment/task/download/](04-ad-comments.md#doc-1738088341958658) để tải về tệp dữ liệu đã xuất.

Dữ liệu xuất ra có các cột tiêu đề: Content, Likes, Replies, Comment Type, Create Time, Campaign Name, Ad Group Name, Ad Name. Nếu bình luận có nhắc tên người dùng (mention), tên sẽ được hiển thị dạng "@user_name".

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| comment_status | string[] | Không bắt buộc | Trạng thái bình luận cần xuất: `ALL`, `PUBLIC`, `HIDDEN`. Mặc định: `["ALL"]`. |
| comment_type | string[] | Không bắt buộc | Loại bình luận: `ALL`, `COMMENT`, `REPLY`. Mặc định: `["ALL"]`. |
| search_field | string | Không bắt buộc | Trường tìm kiếm lọc dữ liệu: `ADGROUP_ID`. |
| search_value | string | Không bắt buộc | Giá trị tìm kiếm (ví dụ ID nhóm quảng cáo). |
| comment_ids | string[] | Không bắt buộc | Danh sách các ID bình luận cụ thể muốn xuất. |
| sort_field | string | Không bắt buộc | Trường sắp xếp: `CREATE_TIME`, `LIKES`, `REPLIES`. |
| sort_type | string | Không bắt buộc | Thứ tự sắp xếp: `ASC`, `DESC`. |
| start_time | string | Không bắt buộc | Ngày bắt đầu khoảng thời gian cần lấy kết quả (`YYYY-MM-DD`). |
| end_time | string | Không bắt buộc | Ngày kết thúc khoảng thời gian cần lấy kết quả (`YYYY-MM-DD`). |
| lang | string | Không bắt buộc | Ngôn ngữ của tiêu đề cột trong tệp xuất: `EN`, `JA`, `ZH`. Mặc định: `EN`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/comment/task/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "search_field": "ADGROUP_ID",
  "search_value": "1723456789012345",
  "lang": "EN"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID tác vụ xuất dữ liệu vừa được tạo. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "task_id": "export_task_123456789"
  }
}
```

---

## Kiểm tra trạng thái tác vụ xuất bình luận (`Get the status of a comment export task`)
<a id="doc-1738088242659330"></a>
<!-- doc_id: 1738088242659330 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/comment/task/check/`

**Mục đích**: Sử dụng endpoint này để kiểm tra tiến độ và trạng thái của một tác vụ xuất bình luận. Khi tác vụ hoàn thành, bạn có thể gọi [/comment/task/download/](04-ad-comments.md#doc-1738088341958658) để tải dữ liệu về.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| task_id | string | Bắt buộc | ID tác vụ xuất dữ liệu cần kiểm tra. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "task_id=export_task_123456789" https://business-api.tiktok.com/open_api/v1.3/comment/task/check/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/comment/task/check/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": "export_task_123456789",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID tác vụ xuất dữ liệu. |
| ↳ status | string | Trạng thái tác vụ: `PROCESSING` (đang xử lý), `RUNNING`, `SUCCEED` / `SUCCESS` (thành công), `FAILED` (thất bại). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "task_id": "export_task_123456789",
    "status": "SUCCEED"
  }
}
```

---

## Tải về dữ liệu bình luận đã xuất (`Download exported comments`)
<a id="doc-1738088341958658"></a>
<!-- doc_id: 1738088341958658 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/comment/task/download/`

**Mục đích**: Sử dụng endpoint này để tải về nội dung dữ liệu bình luận sau khi tác vụ xuất dữ liệu đã hoàn tất thành công. Dữ liệu được trả về ở định dạng CSV với các cột tiêu đề: Content, Likes, Replies, Comment Type, Create Time, Campaign Name, Ad Group Name, Ad Name.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| task_id | string | Bắt buộc | ID tác vụ xuất dữ liệu đã hoàn tất. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "task_id=export_task_123456789" https://business-api.tiktok.com/open_api/v1.3/comment/task/download/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/comment/task/download/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": "export_task_123456789",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ csv | string | Nội dung dữ liệu bình luận dạng chuỗi CSV. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "csv": "Content,Likes,Replies,Comment Type,Create Time,Campaign Name,Ad Group Name,Ad Name
"Sản phẩm tuyệt vời!",10,2,"COMMENT","2026-05-14 07:04:16","Summer Campaign","Ad Group 1","Ad Name 1"
"
  }
}
```
