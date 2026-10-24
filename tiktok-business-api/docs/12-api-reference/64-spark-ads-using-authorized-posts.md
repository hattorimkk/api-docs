# Spark Ads từ bài đăng được ủy quyền (Spark Ads Using Authorized Posts)

Tài liệu này hướng dẫn cách tạo, quản lý và sử dụng các bài đăng video/ảnh tự nhiên trên TikTok đã được nhà sáng tạo nội dung (Creator) ủy quyền để chạy quảng cáo Spark Ads.

Ngoài phương thức sử dụng mã ủy quyền bài đăng (Authorization Code), bạn cũng có thể tạo Spark Ads qua các phương thức khác:
- Đẩy video quảng cáo đến Tài khoản doanh nghiệp (Business Account) đã liên kết.
- Kéo bài đăng từ Tài khoản doanh nghiệp đã liên kết.
- Kéo bài đăng từ các tài khoản TikTok được ủy quyền trong Business Center.

Xem thêm các bước thực hiện chi tiết tại [hướng dẫn Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).

## Danh sách endpoint trong tài liệu

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/open_api/v1.3/tt_video/info/` | Lấy thông tin chi tiết về bài đăng Spark Ad qua mã ủy quyền |
| `POST` | `/open_api/v1.3/tt_video/authorize/` | Áp dụng mã ủy quyền để kết nối bài đăng vào tài khoản quảng cáo |
| `GET` | `/open_api/v1.3/tt_video/list/` | Lấy danh sách các bài đăng Spark Ad đã được ủy quyền |
| `POST` | `/open_api/v1.3/tt_video/unbind/` | Hủy liên kết bài đăng Spark Ad khi hết hạn hoặc bị thu hồi |

---

## Tổng quan về Spark Ads từ bài đăng được ủy quyền (Spark Ads Using Authorized Posts Overview)
<a id="doc-1738376238825474"></a>
<!-- doc_id: 1738376238825474 -->

Phương thức chạy Spark Ads bằng mã ủy quyền (Authorized Posts) cho phép doanh nghiệp hợp tác với các nhà sáng tạo nội dung (Creators) hoặc đối tác KOC/KOL để chuyển đổi trực tiếp bài đăng tự nhiên của họ thành mẫu quảng cáo TikTok mà không cần truy cập trực tiếp vào tài khoản cá nhân của nhà sáng tạo.

Quy trình tổng thể:
1. Nhà sáng tạo bật tính năng **Quảng cáo (Ad authorization)** trên video bài đăng trong ứng dụng TikTok và tạo **Mã ủy quyền (Auth code)**.
2. Nhà quảng cáo gọi endpoint [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) để kiểm tra thông tin và tính hợp lệ của bài đăng.
3. Nhà quảng cáo gọi endpoint [/tt_video/authorize/](64-spark-ads-using-authorized-posts.md#doc-1738376435339265) để áp dụng mã ủy quyền, đưa video vào thư viện tài nguyên của tài khoản quảng cáo.
4. Tra cứu danh sách video đã ủy quyền qua [/tt_video/list/](64-spark-ads-using-authorized-posts.md#doc-1738376465972226) và tiến hành tạo mẫu quảng cáo Spark Ad.

Các tài liệu liên kết trong nhóm:
* [Lấy thông tin về bài đăng Spark Ad](64-spark-ads-using-authorized-posts.md#doc-1738376324021250)
* [Áp dụng mã ủy quyền](64-spark-ads-using-authorized-posts.md#doc-1738376435339265)
* [Lấy danh sách bài đăng Spark Ad](64-spark-ads-using-authorized-posts.md#doc-1738376465972226)
* [Hủy liên kết bài đăng Spark Ad](64-spark-ads-using-authorized-posts.md#doc-1738376509936641)

---

## Lấy thông tin về bài đăng Spark Ad (Get info about a Spark Ad post)
<a id="doc-1738376324021250"></a>
<!-- doc_id: 1738376324021250 -->

Sử dụng endpoint này để lấy thông tin chi tiết về bài đăng Spark Ad mà bạn đã được ủy quyền sử dụng làm quảng cáo thông qua mã ủy quyền do chủ sở hữu bài đăng cung cấp.

### Trước khi bắt đầu
Đảm bảo bạn đã nhận được mã ủy quyền từ nhà sáng tạo (chủ sở hữu bài đăng TikTok). Nhà sáng tạo có thể tạo mã bằng các bước sau:
1. Mở ứng dụng TikTok, nhấn vào biểu tượng dấu ba chấm (`...`) trên video muốn chia sẻ.
2. Trong ngăn chia sẻ, nhấn vào **Cài đặt quảng cáo (Ad settings)**.
3. Bật tùy chọn **Ủy quyền quảng cáo (Ad authorization)**.
4. Chọn thời hạn ủy quyền (ví dụ: 7 ngày, 30 ngày, 60 ngày hoặc 365 ngày).
5. Tạo và sao chép mã ủy quyền.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/tt_video/info/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `auth_code` **(Bắt buộc)** | string | Mã ủy quyền của bài đăng Spark Ad do người sáng tạo cung cấp. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/tt_video/info/?advertiser_id=7123456789012345678&auth_code=AUTH_CODE_EXAMPLE_123' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
AUTH_CODE = "AUTH_CODE_EXAMPLE_123"
url = "https://business-api.tiktok.com/open_api/v1.3/tt_video/info/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "auth_code": AUTH_CODE
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
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ auth_info` | object | Thông tin thời hạn ủy quyền. |
| `↳↳ auth_start_time` | string | Thời điểm mã ủy quyền bắt đầu có hiệu lực (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| `↳↳ auth_end_time` | string | Thời điểm mã ủy quyền hết hạn (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| `↳ item_info` | object | Thông tin chi tiết về bài đăng Spark Ad. |
| `↳↳ auth_code` | string | Mã ủy quyền của bài đăng. |
| `↳↳ item_id` | string | ID của bài đăng trên TikTok. |
| `↳↳ item_type` | string | Loại bài đăng (`VIDEO`, `CAROUSEL`). |
| `↳↳ text` | string | Nội dung văn bản/chú thích của bài đăng. |
| `↳↳ status` | string | Trạng thái của bài đăng (`NORMAL`, `DELETED`, v.v.). |
| `↳↳ carousel_info` | object | Thông tin đối với bài đăng định dạng ảnh/carousel. |
| `↳↳↳ image_info` | object[] | Danh sách thông tin hình ảnh trong carousel. |
| `↳↳↳ music_info` | object | Thông tin âm nhạc sử dụng trong bài đăng. |
| `↳↳ stitch_original_item_id` | string | ID bài đăng gốc nếu video là dạng Stitch. |
| `↳↳ duet_original_item_id` | string | ID bài đăng gốc nếu video là dạng Duet. |
| `↳↳ is_multi_duet_stitch` | boolean | Cho biết bài đăng có phải là bản Duet hoặc Stitch lồng ghép nhiều video hay không. |
| `↳↳ mentioned_item_ids` | string[] | Danh sách ID video được nhắc đến trong bài đăng. |
| `↳↳ anchor_list` | object[] | Danh sách liên kết neo (anchors) trong bài đăng (ví dụ: liên kết sản phẩm TikTok Shop). |
| `↳↳↳ id` | string | ID của anchor. |
| `↳↳↳ title` | string | Tiêu đề hiển thị của anchor. |
| `↳↳↳ status` | string | Trạng thái xét duyệt anchor (`CHECK_ING`, `PASSED`, `FAILED`). |
| `↳↳↳ product_regions` | string[] | Các khu vực địa lý nơi sản phẩm có thể phân phối. |
| `↳↳↳ url` | string | URL liên kết sản phẩm. |
| `↳↳↳ spu_id` | string | SPU ID nếu anchor liên kết sản phẩm TikTok Shop. |
| `↳↳↳ spu_name` | string | Tên SPU sản phẩm. |
| `↳↳↳ store_id` | string | ID cửa hàng TikTok Shop. |
| `↳ user_info` | object | Thông tin tài khoản TikTok của người sáng tạo. |
| `↳↳ tiktok_name` | string | Tên người dùng tài khoản TikTok (username). |
| `↳↳ identity_id` | string | ID danh tính (Identity ID) sử dụng khi tạo quảng cáo. |
| `↳↳ identity_type` | string | Loại danh tính (`AUTH_CODE`). |
| `↳ video_info` | object | Thông số kỹ thuật của video. |
| `↳↳ video_id` | string | ID video trong hệ thống media. |
| `↳↳ file_name` | string | Tên tệp video. |
| `↳↳ bit_rate` | integer | Tốc độ truyền tải bit (bps). |
| `↳↳ duration` | float | Thời lượng video (giây). |
| `↳↳ size` | integer | Kích thước video (bytes). |
| `↳↳ width` | integer | Chiều rộng khung hình video (pixels). |
| `↳↳ height` | integer | Chiều cao khung hình video (pixels). |
| `↳↳ poster_url` | string | Đường dẫn ảnh bìa video (có hiệu lực trong 1 giờ). |
| `↳↳ preview_url` | string | Đường dẫn xem trước video (có hiệu lực trong 1 giờ). |
| `↳↳ signature` | string | Mã băm MD5 của video để kiểm tra tính toàn vẹn. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "auth_info": {
      "auth_start_time": "2024-03-01 00:00:00",
      "auth_end_time": "2024-06-01 00:00:00"
    },
    "item_info": {
      "auth_code": "AUTH_CODE_EXAMPLE_123",
      "item_id": "7123456789012345678",
      "item_type": "VIDEO",
      "text": "Check out this amazing product! #recommend",
      "status": "NORMAL"
    },
    "user_info": {
      "tiktok_name": "creator_official",
      "identity_id": "7123456789012345678",
      "identity_type": "AUTH_CODE"
    },
    "video_info": {
      "video_id": "v09044g40000cfv0",
      "duration": 15.5,
      "width": 720,
      "height": 1280
    }
  }
}
```

---

## Áp dụng mã ủy quyền (Apply an authorization code)
<a id="doc-1738376435339265"></a>
<!-- doc_id: 1738376435339265 -->

Sử dụng endpoint này để áp dụng mã ủy quyền. Sau khi nhận được mã ủy quyền từ người sáng tạo, quyền sử dụng chưa tự động có hiệu lực trên tài khoản quảng cáo; bạn cần gọi endpoint này để liên kết chính thức bài đăng Spark Ad với tài khoản quảng cáo của mình.

> **Trường hợp Duet / Stitch:**
> Nếu bài đăng là video Duet hoặc Stitch từ một video khác hoặc có nhắc đến một video khác, bạn cần xin mã ủy quyền từ chủ sở hữu của cả hai video trước khi có thể quảng bá bài đăng. Sử dụng `auth_code` để chỉ định mã của bài đăng muốn chạy quảng cáo, và `original_post_auth_code` để chỉ định mã của video gốc.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/tt_video/authorize/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `auth_code` **(Bắt buộc)** | string | Mã ủy quyền của bài đăng Spark Ad do người sáng tạo cung cấp. |
| `original_post_auth_code` | string | Mã ủy quyền của bài đăng gốc nếu bài đăng này là bản Duet hoặc Stitch từ bài đăng khác. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/tt_video/authorize/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "auth_code": "AUTH_CODE_EXAMPLE_123"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/tt_video/authorize/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "auth_code": "AUTH_CODE_EXAMPLE_123"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã lỗi khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi liên kết thành công). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {}
}
```

---

## Lấy danh sách bài đăng Spark Ad (Get Spark Ad posts)
<a id="doc-1738376465972226"></a>
<!-- doc_id: 1738376465972226 -->

Sử dụng endpoint này để lấy danh sách các bài đăng Spark Ad đã được áp dụng ủy quyền vào tài khoản quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/tt_video/list/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `item_types` | string[] | Lọc theo loại bài đăng Spark Ad. Enum: `VIDEO` (Video), `CAROUSEL` (Bài đăng ảnh xoay vòng). |
| `keyword` | string | Từ khóa tìm kiếm theo nội dung văn bản hoặc ID bài đăng TikTok. |
| `page` | number | Số trang hiện tại (mặc định: `1`). |
| `page_size` | number | Kích thước trang (mặc định: `20`, tối đa: `50`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/tt_video/list/?advertiser_id=7123456789012345678&page=1&page_size=20' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/tt_video/list/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 20
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
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ list` | object[] | Danh sách các bài đăng Spark Ad đã được ủy quyền. |
| `↳↳ item_info` | object | Thông tin chi tiết về bài đăng Spark Ad (`item_id`, `item_type`, `text`, `status`, `auth_code`). |
| `↳↳ video_info` | object | Thông số video (`video_id`, `duration`, `width`, `height`, `poster_url`). |
| `↳↳ user_info` | object | Thông tin tài khoản sáng tạo TikTok (`tiktok_name`, `identity_id`, `identity_type`). |
| `↳↳ auth_info` | object | Thông tin thời hạn ủy quyền (`auth_start_time`, `auth_end_time`). |
| `↳ page_info` | object | Thông tin phân trang. |
| `↳↳ page` | number | Trang hiện tại. |
| `↳↳ page_size` | number | Số lượng kết quả mỗi trang. |
| `↳↳ total_number` | number | Tổng số lượng bài đăng được ủy quyền. |
| `↳↳ total_page` | number | Tổng số trang kết quả. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "list": [
      {
        "item_info": {
          "item_id": "7123456789012345678",
          "item_type": "VIDEO",
          "text": "Loving this product! #ad",
          "status": "NORMAL"
        },
        "user_info": {
          "tiktok_name": "creator_name",
          "identity_id": "7123456789012345678",
          "identity_type": "AUTH_CODE"
        },
        "auth_info": {
          "auth_start_time": "2024-03-01 00:00:00",
          "auth_end_time": "2024-06-01 00:00:00"
        }
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 20,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

## Hủy liên kết bài đăng Spark Ad (Unbind a Spark Ad post)
<a id="doc-1738376509936641"></a>
<!-- doc_id: 1738376509936641 -->

Sử dụng endpoint này để hủy liên kết một bài đăng Spark Ad sau khi thời hạn ủy quyền đã kết thúc hoặc mã ủy quyền đã bị thu hồi bởi người sáng tạo. Thao tác hủy liên kết sẽ gỡ bỏ bài đăng khỏi danh sách bài đăng Spark Ad khả dụng của tài khoản quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/tt_video/unbind/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `item_id` **(Bắt buộc)** | string | ID của bài đăng Spark Ad cần hủy liên kết. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/tt_video/unbind/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "item_id": "7123456789012345678"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
ITEM_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/tt_video/unbind/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "item_id": ITEM_ID
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
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi hủy liên kết thành công). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {}
}
```
