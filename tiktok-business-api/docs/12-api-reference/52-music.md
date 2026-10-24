# Âm nhạc (Music)
<a id="doc-1740052369141761"></a>
<!-- doc_id: 1740052369141761 -->

Âm nhạc là một loại tài nguyên sáng tạo quan trọng trong quảng cáo TikTok. Bạn có thể tham khảo [Tải video, hình ảnh và âm nhạc](../09-marketing-api/creatives.md#doc-1738963828459521) để tìm hiểu quy trình lựa chọn âm nhạc phù hợp. Bạn cũng có thể sử dụng `music_id` trong các công cụ sáng tạo như [Video thông minh (Smart Video)](38-creative-tools.md#doc-1739352294717441) và [Nhạc nền video thông minh (Smart Video Soundtrack)](38-creative-tools.md#doc-1739089635852289). Ngoài ra, âm nhạc có thể được đưa vào gói video thông qua endpoint [/catalog/video_package/create/](31-catalog-video-templates.md#doc-1740665273039873) bằng cách chỉ định qua trường `music_id`.

Âm nhạc cũng có thể được sử dụng trong Quảng cáo xoay vòng (Carousel Ads). Xem thêm [tại đây](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713) để tìm hiểu cách tạo quảng cáo Carousel.

Nhóm API này bao gồm các endpoint sau:
* [Tải lên một bản nhạc](52-music.md#doc-1740052650395650)
* [Lấy danh sách âm nhạc](52-music.md#doc-1740053909509122)

---

## Tải lên một bản nhạc (`Upload a piece of music`)
<a id="doc-1740052650395650"></a>
<!-- doc_id: 1740052650395650 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/file/music/upload/`

**Mục đích**: Sử dụng endpoint này để tải lên bản nhạc và lấy ID âm nhạc (`music_id`), thêm nhạc vào danh sách Yêu thích (Liked list) hoặc Lịch sử (History list), hoặc xóa nhạc khỏi danh sách Yêu thích.

> [!WARNING]
> **Lưu ý bản quyền (Copyright Notice)**: Hãy đảm bảo bạn có đầy đủ quyền tác quyền và quyền sở hữu trí tuệ đối với bản nhạc tải lên. Mọi vi phạm bản quyền tác giả sẽ do bạn hoàn toàn chịu trách nhiệm.

### So sánh v1.2 và v1.3 (`Comparing v1.2 and v1.3`)

| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | `/v1.2/file/music/upload/` | `/v1.3/file/music/upload/` |
| Request parameter data type | `advertiser_id`: number | `advertiser_id`: string |
| New request parameters | / | `music_scene`<br>`material_action`<br>`material_id` |
| Response parameter deprecated in v1.3 | / | `name`: string |
| New response parameters | / | `author`<br>`liked`<br>`cover_url` |

### Tiêu đề HTTP (Header)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng bản tin yêu cầu:<br>• Nếu `upload_type` là `UPLOAD_BY_FILE`: sử dụng `multipart/form-data`.<br>• Nếu `upload_type` là `UPLOAD_BY_FILE_ID`: sử dụng `application/json`. |

### Tham số (Parameters)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| music_scene | string | Không | Kịch bản sử dụng bản nhạc. Giá trị enum:<br>• `CREATIVE_ASSET`: Dùng cho Công cụ sáng tạo.<br>• `CAROUSEL_ADS`: Quảng cáo không phải mua sắm (Non-Shopping) - Định dạng xoay vòng (Carousel).<br>• `CATALOG_CAROUSEL`: Quảng cáo mua sắm (VSA) - Định dạng xoay vòng.<br>Giá trị mặc định: `CREATIVE_ASSET`. |
| upload_type | string | Có điều kiện | Khi `music_scene` được đặt thành `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`, bạn cần truyền hoặc `upload_type` hoặc `material_action`. Khi `music_scene` là `CREATIVE_ASSET` hoặc không truyền, trường này là tùy chọn và mặc định là `UPLOAD_BY_FILE`.<br>Phương thức tải nhạc lên:<br>• `UPLOAD_BY_FILE`: Tải file nhạc trực tiếp.<br>• `UPLOAD_BY_FILE_ID`: Tải nhạc thông qua file ID đã có. |
| material_action | string | Có điều kiện | Khi `music_scene` là `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`, bạn cần truyền hoặc `upload_type` hoặc `material_action`. Không hỗ trợ khi `music_scene` là `CREATIVE_ASSET`. Khi truyền trường này, bạn cũng cần truyền `material_id`.<br>Loại thao tác thực hiện với bản nhạc:<br>• `ADD_TO_LIKED`: Thêm nhạc vào danh sách Yêu thích (tối đa 1.000 bản nhạc).<br>• `ADD_TO_HISTORY`: Thêm nhạc vào danh sách Lịch sử.<br>• `REMOVE_FROM_LIKED`: Xóa nhạc khỏi danh sách Yêu thích. |
| music_file | file | Có điều kiện | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE` hoặc không chỉ định. File âm nhạc tải lên. Lưu ý: Khi dùng cho `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`, file nhạc phải đáp ứng yêu cầu: định dạng MP3, kích thước không vượt quá 10 MB. |
| music_signature | string | Có điều kiện | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE` hoặc không chỉ định. Mã MD5 của file âm nhạc (dùng để máy chủ xác thực tính toàn vẹn). |
| file_name | string | Không | Chỉ có hiệu lực khi truyền `upload_type`. Tên bản nhạc. Giới hạn độ dài: 1-100 ký tự. Mặc định là tên file cục bộ. |
| file_id | string | Có điều kiện | Bắt buộc khi `upload_type` là `UPLOAD_BY_FILE_ID`. Mã ID của file trong kho tài nguyên lưu trữ. Lấy `file_id` qua endpoint [Tải file lên (Upload Files)](44-files.md#doc-1737719988918274). File tương ứng phải là MP3 và $\le 10$ MB khi dùng cho Carousel Ads. |
| material_id | string | Có điều kiện | Bắt buộc khi `music_scene` là `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL` và có truyền `material_action`. ID tài nguyên của bản nhạc dùng cho việc thêm/xóa khỏi danh sách Yêu thích hoặc Lịch sử. Lấy qua endpoint này khi tải nhạc lên hoặc qua endpoint [/file/music/get/](52-music.md#doc-1740053909509122). |

### Phản hồi

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Mã trạng thái phản hồi (0: Thành công))](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ music_id | string | ID định danh của bản nhạc. |
| ↳ material_id | string | ID tài nguyên của bản nhạc. |
| ↳ sources | string[] | Nguồn bản nhạc: `USER` là nhạc do nhà quảng cáo tải lên; `SYSTEM` là nhạc hệ thống. |
| ↳ author | string | Chỉ trả về đối với nhạc có thể sử dụng trong Carousel Ads. Tác giả của bản nhạc. |
| ↳ liked | boolean | Chỉ trả về đối với nhạc trong Carousel Ads. Cho biết bản nhạc đã được thêm vào danh sách Yêu thích hay chưa. |
| ↳ cover_url | string | Chỉ trả về đối với nhạc trong Carousel Ads. URL ảnh bìa của bản nhạc. |
| ↳ url | string | Đường dẫn nghe bản nhạc. Thời hạn hiệu lực: 12 giờ. |
| ↳ duration | float | Thời lượng bản nhạc tính bằng giây. Chỉ trả về cho nhạc hệ thống. |
| ↳ style | string | Phong cách âm nhạc. Chỉ trả về cho nhạc hệ thống. |
| ↳ signature | string | Chuỗi băm MD5 của file âm nhạc. |
| ↳ file_name | string | Tên file âm nhạc. |
| ↳ copyright | string | Thông tin bản quyền:<br>• `MUSIC_FORBID_VIDEO_ALLOW`: Bản nhạc không được phép tải xuống riêng lẻ, nhưng video tạo từ bản nhạc đó được phép tải xuống.<br>• `MUSIC_FORBID_VIDEO_FORBID`: Cả bản nhạc và video tạo ra đều không được phép tải xuống. |
| ↳ create_time | string | Thời điểm tạo bản nhạc theo giờ UTC (định dạng `YYYY-MM-DDTHH:mm:ssZ`). Chỉ trả về cho nhạc do nhà quảng cáo tải lên. |
| ↳ modify_time | string | Thời điểm chỉnh sửa bản nhạc theo giờ UTC. Chỉ trả về cho nhạc tùy chỉnh của nhà quảng cáo. |

### Ví dụ gọi API

#### cURL (Tải file trực tiếp)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/file/music/upload/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: multipart/form-data' \
--form 'advertiser_id="7123456789012345678"' \
--form 'upload_type="UPLOAD_BY_FILE"' \
--form 'music_file=@"/path/to/soundtrack.mp3"' \
--form 'music_signature="e360fd0e868c3183a0da849d38726739"' \
--form 'file_name="summer_vibes"'
```

#### Python
```python
import requests
import hashlib

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/file/music/upload/"

file_path = "/path/to/soundtrack.mp3"
with open(file_path, "rb") as f:
    file_bytes = f.read()
    file_md5 = hashlib.md5(file_bytes).hexdigest()

headers = {
    "Access-Token": ACCESS_TOKEN
}

files = {
    "music_file": ("soundtrack.mp3", file_bytes, "audio/mpeg")
}

data = {
    "advertiser_id": ADVERTISER_ID,
    "upload_type": "UPLOAD_BY_FILE",
    "music_signature": file_md5,
    "file_name": "summer_vibes"
}

response = requests.post(url, headers=headers, data=data, files=files)
res_json = response.json()
print("Music ID:", res_json.get("data", {}).get("music_id"))
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048F1A2B3",
    "data": {
        "music_id": "6836297245562994693",
        "material_id": "6836297245562994693",
        "file_name": "summer_vibes",
        "sources": [
            "USER"
        ],
        "copyright": "MUSIC_FORBID_VIDEO_ALLOW",
        "url": "https://sf-tk-sg.ibytedtos.com/obj/iesmusic-cn-local/v1/m/42b00000ca0384107766",
        "signature": "e360fd0e868c3183a0da849d38726739",
        "create_time": "2026-06-10T07:39:14Z",
        "modify_time": "2026-06-10T07:39:14Z"
    }
}
```

---

## Lấy danh sách âm nhạc (`Get the music list`)
<a id="doc-1740053909509122"></a>
<!-- doc_id: 1740053909509122 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/file/music/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các bản nhạc khả dụng có thể sử dụng cho việc tạo video hoặc tạo Quảng cáo xoay vòng (Carousel Ads). Danh sách sẽ bao gồm cả nhạc do nhà quảng cáo tự tải lên lẫn nhạc có sẵn trong Thư viện Âm thanh Thương mại (Commercial Music Library). Thư viện âm thanh ít khi thay đổi thường xuyên, do đó bạn nên lưu bộ nhớ đệm (cache) và cập nhật danh sách hàng tháng.

> [!WARNING]
> **Quy định bản quyền**: Các sản phẩm video sáng tạo được tạo bằng âm nhạc do hệ thống TikTok cung cấp chỉ được phép phân phối trên nền tảng TikTok. Bạn không được phép tải xuống, phân phối hoặc biểu diễn video và/hoặc file âm nhạc đó trên bất kỳ phương tiện truyền thông nào khác ngoài TikTok, trừ khi có sự đồng ý riêng từ chủ sở hữu bản quyền âm nhạc.

### So sánh v1.2 và v1.3 (`Comparing v1.2 and v1.3`)

| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | `/v1.2/file/music/get/` | `/v1.3/file/music/get/` |
| Request parameter data type | `advertiser_id`: number | `advertiser_id`: string |
| New request parameters | / | `music_scene`<br>`search_type`<br>`keyword`<br>`image_urls`<br>`catalog_id`<br>`catalog_authorized_bc_id`<br>`sku_ids`<br>`product_set_id`<br>`item_group_ids`<br>`carousel_image_index` |
| Response parameter deprecated in v1.3 | / | `id`: string |
| New response parameters | / | `author`<br>`liked`<br>`cover_url` |

### Tiêu đề HTTP (Header)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| music_scene | string | Không | Kịch bản sử dụng bản nhạc. Giá trị enum:<br>• `CREATIVE_ASSET`: Dùng cho Công cụ sáng tạo.<br>• `CAROUSEL_ADS`: Dùng cho Carousel Ads không phải mua sắm.<br>• `CATALOG_CAROUSEL`: Dùng cho Carousel Ads danh mục mua sắm (VSA).<br>Mặc định: `CREATIVE_ASSET`. |
| search_type | string | Có điều kiện | Bắt buộc khi `music_scene` là `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`. Không hỗ trợ khi `music_scene` là `CREATIVE_ASSET`.<br>Loại tìm kiếm âm nhạc:<br>• `SEARCH_BY_KEYWORD`: Tìm kiếm mờ theo từ khóa (kèm tham số `keyword`).<br>• `SEARCH_BY_RECOMMEND`: Lấy nhạc đề xuất dựa trên hình ảnh Carousel (`image_urls`) hoặc sản phẩm Catalog (`catalog_id`, `catalog_authorized_bc_id`). Tối đa trả về 500 bài hát đề xuất.<br>• `SEARCH_BY_LIKED`: Lấy danh sách nhạc Yêu thích (tối đa 1.000 bài).<br>• `SEARCH_BY_HISTORY`: Lấy danh sách nhạc Lịch sử.<br>• `SEARCH_BY_MUSIC_ID`: Tìm kiếm theo danh sách ID âm nhạc (`music_ids`).<br>• `SEARCH_BY_SOURCE`: Lọc theo nguồn âm nhạc (`sources`).<br>Lưu ý: Với các loại `SEARCH_BY_RECOMMEND`, `SEARCH_BY_LIKED`, `SEARCH_BY_MUSIC_ID`, phân trang không được hỗ trợ và các tham số `page`, `page_size` sẽ bị bỏ qua. |
| filtering | object | Không | Điều kiện lọc tìm kiếm chi tiết. |
| ↳ keyword | string | Có điều kiện | Bắt buộc khi `search_type = SEARCH_BY_KEYWORD`. Từ khóa tìm kiếm âm nhạc. |
| ↳ image_urls | string[] | Có điều kiện | Bắt buộc khi `music_scene = CAROUSEL_ADS` và `search_type = SEARCH_BY_RECOMMEND`. Mảng từ 2 đến 35 URL hình ảnh cần gợi ý nhạc. Yêu cầu ảnh: định dạng JPG/JPEG/PNG, dung lượng $\le 50$ MB, và cờ `is_carousel_usable = true` từ endpoint kiểm tra ảnh. |
| ↳ music_ids | string[] | Có điều kiện | Bắt buộc khi `search_type = SEARCH_BY_MUSIC_ID`. Danh sách tối đa 100 ID âm nhạc. |
| ↳ catalog_id | string | Có điều kiện | Bắt buộc khi `music_scene = CATALOG_CAROUSEL` và `search_type = SEARCH_BY_RECOMMEND`. ID danh mục sản phẩm (ID danh mục sản phẩm). |
| ↳ catalog_authorized_bc_id | string | Có điều kiện | Bắt buộc khi `music_scene = CATALOG_CAROUSEL` và `search_type = SEARCH_BY_RECOMMEND`. ID của Business Center có quyền truy cập danh mục sản phẩm. |
| ↳ item_group_ids | string[] | Có điều kiện | Danh sách SPU ID sản phẩm (tối đa 20) khi gợi ý nhạc cho VSA Carousel Ads chọn động từ bộ sản phẩm. |
| ↳ product_set_id | string | Có điều kiện | ID bộ sản phẩm khi gợi ý nhạc cho VSA Carousel Ads chọn động từ bộ sản phẩm. |
| ↳ sku_ids | string[] | Có điều kiện | Danh sách SKU ID (từ 2 đến 20) khi gợi ý nhạc cho VSA Carousel Ads từ các sản phẩm cụ thể. |
| ↳ carousel_image_index | integer | Không | Chỉ số chọn ảnh phụ trong mảng `additional_image_urls` cho VSA Carousel Ads (từ 0 đến 9). Mặc định là ảnh chính của sản phẩm. |
| ↳ material_ids | string[] | Không | Không hỗ trợ trong kịch bản Carousel. Danh sách ID tài nguyên âm nhạc (tối đa 100). |
| ↳ styles | string[] | Không | Không hỗ trợ trong kịch bản Carousel. Phong cách âm nhạc (tối đa 1 phong cách). |
| ↳ sources | string[] | Có điều kiện | Nguồn âm nhạc: `USER` (nhạc tải lên) hoặc `SYSTEM` (nhạc hệ thống). Bắt buộc là `USER` khi dùng `search_type = SEARCH_BY_SOURCE` cho Carousel Ads. |
| page | number | Không | Số trang cần lấy. Mặc định: `1`. Tích số `page * page_size` không được vượt quá 100.000. |
| page_size | number | Không | Số lượng kết quả mỗi trang. Mặc định: `1000` (hoặc `200` khi tìm theo từ khóa hoặc lịch sử). Phạm vi: 1-1.000. |

### Phản hồi

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi API. `0` biểu thị thành công. Xem [Mã trả về (Mã trạng thái phản hồi (0: Thành công))](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ musics | list | Danh sách dữ liệu các bản nhạc. |
| ↳↳ music_id | string | ID định danh của bản nhạc. |
| ↳↳ material_id | string | ID tài nguyên của bản nhạc. |
| ↳↳ sources | string[] | Nguồn bản nhạc: `USER` hoặc `SYSTEM`. |
| ↳↳ author | string | Tác giả bản nhạc (chỉ dành cho nhạc Carousel). |
| ↳↳ liked | boolean | Đã lưu vào danh sách Yêu thích hay chưa (chỉ dành cho nhạc Carousel). |
| ↳↳ cover_url | string | URL ảnh bìa của bản nhạc. |
| ↳↳ url | string | Đường dẫn nghe bản nhạc (hiệu lực 12 giờ). |
| ↳↳ duration | float | Thời lượng bản nhạc tính bằng giây (chỉ trả về cho nhạc hệ thống). |
| ↳↳ style | string | Phong cách âm nhạc (chỉ trả về cho nhạc hệ thống). |
| ↳↳ signature | string | Mã băm MD5 của file nhạc. |
| ↳↳ name | string | Tên bản nhạc. |
| ↳↳ file_name | string | Tên file bản nhạc. |
| ↳↳ copyright | string | Thông tin bản quyền (`MUSIC_FORBID_VIDEO_ALLOW` hoặc `MUSIC_FORBID_VIDEO_FORBID`). |
| ↳↳ create_time | string | Thời điểm tạo bản nhạc theo giờ UTC. |
| ↳↳ modify_time | string | Thời điểm chỉnh sửa bản nhạc theo giờ UTC. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số bản ghi tìm được. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ gọi API

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/file/music/get/?advertiser_id=7123456789012345678&music_scene=CREATIVE_ASSET&page=1&page_size=20' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/file/music/get/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "music_scene": "CREATIVE_ASSET",
    "page": 1,
    "page_size": 20
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for music in data.get("data", {}).get("musics", [])[:5]:
    print(f"Bản nhạc: {music.get('name') or music.get('file_name')} | ID: {music.get('music_id')} | Thời lượng: {music.get('duration')}s")
    print(f"  - Link nghe thử: {music.get('url')}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048F4E5D6",
    "data": {
        "page_info": {
            "page": 1,
            "page_size": 20,
            "total_number": 1,
            "total_page": 1
        },
        "musics": [
            {
                "music_id": "6707429901383565318",
                "material_id": "6707429901383565318",
                "name": "Her World",
                "file_name": "Her World",
                "style": "Teen",
                "duration": 127.5,
                "sources": [
                    "SYSTEM"
                ],
                "copyright": "MUSIC_FORBID_VIDEO_ALLOW",
                "signature": "bdb2ff10fb44bb38151c98bfee94de89",
                "url": "http://sf-tk-sg.ibytedtos.com/obj/cc-music-sg/6650280667860962050"
            }
        ]
    }
}
```
