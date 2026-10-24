# Tệp (Files)

> Phân hệ API Reference > Files.
> Hướng dẫn tải lên tệp đa phương tiện (video, hình ảnh, âm nhạc, playable) lên kho tệp tạm thời (temporary file repository) của TikTok, bao gồm tải lên tệp đơn và tải lên phân đoạn (chunk upload) cho các tệp dung lượng lớn (> 20 MB, tối đa 100 MB), kiểm tra trùng lặp tên tệp trước khi đẩy vào Thư viện quảng cáo (Asset Library).

---

## Mục lục điều hướng
- [1. Tổng quan phân hệ Tệp (Files)](#1-tong-quan-phan-he-tep-files)
- [2. Tải lên tệp đơn (`POST /open_api/v1.3/file/temporarily/upload/`)](#2-tai-len-tep-don)
- [3. Khởi tạo tác vụ tải lên phân đoạn (`POST /open_api/v1.3/file/start/upload/`)](#3-khoi-tao-tac-vu-tai-len-phan-doan)
- [4. Truyền tải từng phân đoạn tệp (`POST /open_api/v1.3/file/transfer/upload/`)](#4-truyen-tai-tung-phan-doan-tep)
- [5. Hoàn tất tác vụ tải lên phân đoạn (`POST /open_api/v1.3/file/finish/upload/`)](#5-hoan-tat-tac-vu-tai-len-phan-doan)
- [6. Kiểm tra trùng lặp tên tệp (`GET /open_api/v1.3/file/name/check/`)](#6-kiem-tra-trung-lap-ten-tep)
- [7. Mã nguồn mẫu Data Pipeline (Python & cURL)](#7-ma-nguon-mau-data-pipeline)

---

<a id="doc-1737719988918274"></a>
<!-- doc_id: 1737719988918274 -->
<a id="1-tong-quan-phan-he-tep-files"></a>
## 1. Tổng quan phân hệ Tệp (Files)

Bạn có thể tải tệp video, hình ảnh và âm thanh lên kho lưu trữ tệp tạm thời của TikTok. Các tệp trong kho lưu trữ sau đó có thể được chuyển sang Thư viện nội dung (Asset Library / Creatives Library) để sử dụng trong quảng cáo.

> **Lưu ý vòng đời:**
> - Sau khi tệp được tải lên kho tệp tạm thời, tệp sẽ được lưu trữ trong **24 giờ**, sau đó sẽ tự động hết hạn (expire).
> - Nếu tệp dự kiến sử dụng trong quảng cáo đã hết hạn, bạn cần tải lại tệp lên kho tệp.
> - Đối với tệp có dung lượng lớn hơn 20 MB (và tối đa 100 MB), khuyến nghị chia nhỏ tệp thành các phân đoạn (chunks) và sử dụng quy trình chunk upload 3 bước.

Nhóm API này bao gồm các endpoint:
* [Tải lên tệp đơn (`/file/temporarily/upload/`)](44-files.md#doc-1737720893061122)
* [Khởi tạo tác vụ tải lên phân đoạn (`/file/start/upload/`)](44-files.md#doc-1737721229896705)
* [Truyền tải phân đoạn tệp (`/file/transfer/upload/`)](44-files.md#doc-1737721489945601)
* [Hoàn tất tác vụ tải lên phân đoạn (`/file/finish/upload/`)](44-files.md#doc-1737721642924033)
* [Kiểm tra trùng lặp tên tệp (`/file/name/check/`)](44-files.md#doc-1759130033155073)

---

<a id="doc-1737720893061122"></a>
<!-- doc_id: 1737720893061122 -->
<a id="2-tai-len-tep-don"></a>
## 2. Tải lên tệp đơn

Endpoint cho phép tải lên một tệp đơn lẻ trực tiếp hoặc thông qua URL. Tốc độ truyền tải phụ thuộc vào băng thông mạng của bạn. Dung lượng tệp tối đa được hỗ trợ là 100 MB.

Sau khi tệp được tải lên thành công, hệ thống sẽ trả về mã `file_id`. Bạn có thể sử dụng `file_id` này để tham chiếu và chuyển tệp sang Thư viện quảng cáo (Creatives Library).

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/file/temporarily/upload/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): Giá trị cho phép `multipart/form-data` hoặc `application/json`. Khi `upload_type` là `FILE`, bắt buộc dùng `multipart/form-data`. Khi `upload_type` là `URL`, dùng `application/json`.

### Tham số (Parameters)

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `upload_type` | string | **Bắt buộc** | Hình thức tải lên. Giá trị Enum: `FILE` (tải tệp nhị phân trực tiếp), `URL` (kéo từ đường link công khai). |
| `content_type` | string | **Bắt buộc** | Loại nội dung tệp. Giá trị Enum: `image`, `music`, `video`, `playable`. |
| `file` | file | Điều kiện | Tệp nhị phân cần tải lên. Bắt buộc khi `upload_type` = `FILE`. Dung lượng tối đa: 100 MB. <br>**Lưu ý về Carousel Ads:** Để tải nhạc tùy chỉnh cho Quảng cáo quay vòng [Carousel Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713), tệp phải có định dạng MP3 và dung lượng không vượt quá 10 MB. |
| `url` | string | Điều kiện | Đường dẫn URL của tệp cần tải lên (định dạng "http://..." hoặc "https://..."). Bắt buộc khi `upload_type` = `URL`. |
| `signature` | string | Điều kiện | Giá trị mã băm MD5 của tệp (checksum) để phía server kiểm tra tính toàn vẹn dữ liệu. Bắt buộc khi `upload_type` = `FILE`. |
| `name` | string | Không | Tên tệp. Giới hạn tối đa 100 ký tự (mỗi ký tự tiếng Trung/Nhật tính là 3 ký tự, tiếng Anh tính là 1 ký tự). |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu tệp đã tải lên. |
| ↳ `file_id` | string | ID của tệp đã tải lên. Hợp lệ trong vòng 24 giờ. |
| ↳ `signature` | string | Giá trị MD5 của tệp. |
| ↳ `file_size` | number | Kích thước tệp tính bằng byte. |
| ↳ `create_time` | string | Thời điểm tệp được tải lên theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). Ví dụ: `2026-03-23 07:39:14`. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000104",
  "data": {
    "file_id": "v02010g40000xxxxxx",
    "signature": "d41d8cd98f00b204e9800998ecf8427e",
    "file_size": 1548290,
    "create_time": "2026-03-23 08:00:00"
  }
}
```

---

<a id="doc-1737721229896705"></a>
<!-- doc_id: 1737721229896705 -->
<a id="3-khoi-tao-tac-vu-tai-len-phan-doan"></a>
## 3. Khởi tạo tác vụ tải lên phân đoạn (Start chunk upload task)

Endpoint dùng để khởi tạo tác vụ tải lên một tệp lớn theo từng phân đoạn.

Sau khi tác vụ được khởi tạo thành công, bạn nhận được `upload_id` để tiếp tục gọi [/file/transfer/upload/](44-files.md#doc-1737721489945601) tải lên từng phân đoạn.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/file/start/upload/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): `application/json`.

### Tham số (Parameters)

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `size` | number | **Bắt buộc** | Tổng dung lượng tệp tính bằng Byte. |
| `content_type` | string | **Bắt buộc** | Định dạng tệp. Giá trị Enum: `image`, `video`, và `music`. |
| `name` | string | Không | Tên tệp. Độ dài tối đa 100 ký tự. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Thông tin tác vụ vừa khởi tạo. |
| ↳ `upload_id` | string | ID tác vụ upload. Cần sử dụng trường này trong toàn bộ các request tiếp theo của cùng tác vụ. |
| ↳ `file_name` | string | Tên tệp. |
| ↳ `start_offset` | number | Vị trí byte bắt đầu của phân đoạn đầu tiên. |
| ↳ `end_offset` | number | Vị trí byte kết thúc của phân đoạn đầu tiên. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000105",
  "data": {
    "upload_id": "up_task_1234567890",
    "file_name": "promo_video_hd.mp4",
    "start_offset": 0,
    "end_offset": 10485760
  }
}
```

---

<a id="doc-1737721489945601"></a>
<!-- doc_id: 1737721489945601 -->
<a id="4-truyen-tai-tung-phan-doan-tep"></a>
## 4. Truyền tải từng phân đoạn tệp (Transfer a file chunk)

Endpoint truyền tải từng phân đoạn tệp lên server. Khi giá trị `start_offset` trả về bằng với giá trị `end_offset`, điều đó có nghĩa là phân đoạn cuối cùng đã được tải lên hoàn tất. Khi đó, bạn gọi [/file/finish/upload/](44-files.md#doc-1737721642924033) để kết thúc tiến trình.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/file/transfer/upload/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): `multipart/form-data`.

### Tham số (Parameters)

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `upload_id` | string | **Bắt buộc** | ID tác vụ upload nhận được từ `/file/start/upload/`. |
| `signature` | string | **Bắt buộc** | Mã băm MD5 của riêng phân đoạn này (checksum xác thực toàn vẹn dữ liệu). |
| `start_offset` | number | **Bắt buộc** | Vị trí offset bắt đầu của phân đoạn hiện tại. |
| `file` | file | **Bắt buộc** | Dữ liệu nhị phân của phân đoạn tệp. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID log duy nhất nhận diện request. |
| `data` | object | Thông tin tiến độ tải phân đoạn. |
| ↳ `start_offset` | number | Vị trí bắt đầu của phân đoạn đã được ghi nhận. |
| ↳ `end_offset` | number | Vị trí kết thúc của phân đoạn. Khi `start_offset` == `end_offset`, toàn bộ phân đoạn đã hoàn tất. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000106",
  "data": {
    "start_offset": 10485760,
    "end_offset": 20971520
  }
}
```

---

<a id="doc-1737721642924033"></a>
<!-- doc_id: 1737721642924033 -->
<a id="5-hoan-tat-tac-vu-tai-len-phan-doan"></a>
## 5. Hoàn tất tác vụ tải lên phân đoạn (Finish a chunk upload task)

Endpoint gọi để hoàn tất toàn bộ quy trình upload sau khi tất cả các phân đoạn đã được đẩy lên thành công.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/file/finish/upload/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): `application/json`.

### Tham số (Parameters)

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `upload_id` | string | **Bắt buộc** | ID tác vụ upload cần hoàn tất. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID log duy nhất nhận diện request. |
| `data` | object | Dữ liệu tệp tổng hợp cuối cùng. |
| ↳ `file_id` | string | ID của tệp đã tải lên thành công. Sử dụng ID này để chuyển tệp vào Thư viện quảng cáo. Hiệu lực 24 giờ. |
| ↳ `file_name` | string | Tên của tệp đã tải lên. |
| ↳ `create_time` | string | Thời gian tạo theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). Ví dụ: `2026-03-23 07:39:14`. |
| ↳ `size` | number | Tổng dung lượng tệp tính bằng byte. |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000107",
  "data": {
    "file_id": "v02010g40000chunk999",
    "file_name": "promo_video_hd.mp4",
    "size": 25165824,
    "create_time": "2026-03-23 08:30:15"
  }
}
```

---

<a id="doc-1759130033155073"></a>
<!-- doc_id: 1759130033155073 -->
<a id="6-kiem-tra-trung-lap-ten-tep"></a>
## 6. Kiểm tra trùng lặp tên tệp (Check the names of files)

Endpoint kiểm tra xem một hoặc nhiều tên tệp đã được sử dụng cho hình ảnh hoặc video trong cùng tài khoản quảng cáo hay chưa.

> **Quy tắc quan trọng:** Hình ảnh hoặc video thuộc cùng một tài khoản nhà quảng cáo (`advertiser_id`) không được phép trùng tên. Nếu bạn không kiểm tra trước và gặp lỗi trùng tên khi gọi API tải ảnh [/file/image/ad/upload/](47-images.md#doc-1739067433456642) hoặc tải video [/file/video/ad/upload/](71-video.md#doc-1737587322856449), bạn sẽ phải tiến hành upload lại tệp.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/file/name/check/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số Query (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `files` | object[] | Điều kiện | Danh sách đối tượng tên tệp cần kiểm tra hàng loạt (tối đa 20 phần tử). Bắt buộc truyền khi muốn kiểm tra nhiều tên tệp cùng lúc. |
| ↳ `file_name` | string | Điều kiện | Bắt buộc khi truyền `files`. Tên tệp cần kiểm tra. |
| ↳ `file_type` | string | Không | Loại tệp. Giá trị Enum: `VIDEO` (video), `IMAGE` (hình ảnh). Mặc định là `VIDEO`. |
| `file_name` | string | Điều kiện | Tên tệp đơn lẻ cần kiểm tra. Bắt buộc khi không truyền `files`. |
| `file_type` | string | Điều kiện | Loại tệp đơn lẻ. Giá trị Enum: `VIDEO`, `IMAGE`. Mặc định `VIDEO`. Bắt buộc khi không truyền `files`. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu kiểm tra trùng lặp. |
| ↳ `duplicate` | boolean | Trả về khi kiểm tra tệp đơn lẻ (không truyền `files`). `true` = bị trùng lặp tên, `false` = tên khả dụng. |
| ↳ `duplicate_material_id` | string | Trả về khi `duplicate` là `true`. Mã định danh nội dung (material ID) của hình ảnh hoặc video đang sử dụng tên tệp này. |
| ↳ `batch_results` | object[] | Trả về khi truyền `files` (kiểm tra hàng loạt). |
| ↳↳ `file_name` | string | Tên tệp được kiểm tra. |
| ↳↳ `duplicate` | boolean | Trạng thái trùng lặp (`true` hoặc `false`). |
| ↳↳ `duplicate_material_id` | string | Mã định danh nội dung đang dùng tên này (nếu `duplicate` là `true`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000108",
  "data": {
    "batch_results": [
      {
        "file_name": "banner_summer_2026.png",
        "duplicate": false
      },
      {
        "file_name": "video_intro_v1.mp4",
        "duplicate": true,
        "duplicate_material_id": "v02010g40000abcdef12345"
      }
    ]
  }
}
```

---

<a id="7-ma-nguon-mau-data-pipeline"></a>
## 7. Mã nguồn mẫu Data Pipeline (Python & cURL)

### cURL kiểm tra trùng lặp và tải lên tệp
```bash
# 1. Kiểm tra hàng loạt tên tệp trước khi upload
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/file/name/check/?advertiser_id=YOUR_ADVERTISER_ID&files=%5B%7B%22file_name%22%3A%22promo.mp4%22%2C%22file_type%22%3A%22VIDEO%22%7D%5D" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"

# 2. Tải tệp tạm thời qua URL
curl -s -X POST "https://business-api.tiktok.com/open_api/v1.3/file/temporarily/upload/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "upload_type": "URL",
    "content_type": "image",
    "url": "https://example.com/images/banner.jpg",
    "name": "banner_march_2026.jpg"
  }'
```

### Python script hoàn chỉnh quy trình kiểm tra và tải tệp
```python
import hashlib
import json
import os
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {"Access-Token": ACCESS_TOKEN}

def check_file_name_duplicate(advertiser_id, file_name, file_type="VIDEO"):
    """Kiểm tra xem tên tệp đã tồn tại trong tài khoản quảng cáo chưa."""
    url = f"{BASE_URL}/file/name/check/"
    params = {
        "advertiser_id": advertiser_id,
        "file_name": file_name,
        "file_type": file_type
    }
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        is_dup = res.get("data", {}).get("duplicate", False)
        print(f"Tệp '{file_name}' trùng lặp: {is_dup}")
        return is_dup
    else:
        print(f"Lỗi kiểm tra: {res.get('code')} - {res.get('message')}")
        return False

def upload_file_temporarily(advertiser_id, file_path, content_type="video"):
    """Tải tệp đơn lẻ lên kho tệp tạm thời kèm checksum MD5."""
    url = f"{BASE_URL}/file/temporarily/upload/"
    
    # Tính MD5 checksum
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    signature = hasher.hexdigest()
    
    file_name = os.path.basename(file_path)
    
    data = {
        "advertiser_id": advertiser_id,
        "upload_type": "FILE",
        "content_type": content_type,
        "signature": signature,
        "name": file_name
    }
    
    with open(file_path, "rb") as f:
        files = {"file": (file_name, f)}
        res = requests.post(url, headers=headers, data=data, files=files).json()
        
    if res.get("code") == 0:
        file_id = res.get("data", {}).get("file_id")
        print(f"Tải lên thành công! file_id: {file_id} (Hiệu lực 24h)")
        return file_id
    else:
        print(f"Lỗi upload: {res.get('code')} - {res.get('message')}")
        return None

if __name__ == "__main__":
    check_file_name_duplicate(ADVERTISER_ID, "promo_2026.mp4", "VIDEO")
```

