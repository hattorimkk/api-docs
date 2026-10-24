# Dynamic Scene (đã ngừng hỗ trợ)
<a id="doc-1740133053109249"></a>
<!-- doc_id: 1740133053109249 -->

> [!WARNING]
> **Nhóm API Dynamic Scene đã ngừng hỗ trợ (Deprecated)**. Nhóm API này trước đây từng được thử nghiệm giới hạn (beta allowlist) và hiện không còn được khuyến nghị cho các dự án mới. Tài liệu dưới đây được lưu trữ dưới dạng tóm tắt (digest) nhằm phục vụ mục đích tra cứu lịch sử hệ thống.
> 
> Xem chi tiết tài liệu chính thức đầy đủ tại: `https://business-api.tiktok.com/portal/docs?id=1740133053109249`

### Tổng quan giải pháp
Dynamic Scene (Phân cảnh động) từng là một giải pháp tự động hóa nội dung sáng tạo, ứng dụng học máy (machine learning) để tự động phân tích và lắp ghép các phân cảnh đơn lẻ do nhà quảng cáo cung cấp (`slots`) với các thành phần quảng cáo khác (nhạc nền BGM, hiệu ứng chuyển cảnh) để tạo ra các biến thể video hoàn chỉnh. Mục tiêu là giúp nâng cao hiệu suất quảng cáo và tối ưu hóa thời gian sản xuất video.

Quy trình làm việc chuẩn của Dynamic Scene bao gồm các bước:
1. Gửi gói nguyên liệu video và nhạc nền qua endpoint [/dynamic_scene/material/submit/](41-deprecated-dynamic-scene.md#doc-1740317263937538) để nhận `material_package_id`.
2. Tạo tác vụ sinh video bất đồng bộ qua endpoint [/dynamic_scene/task/create/](41-deprecated-dynamic-scene.md#doc-1740317320231938) để nhận `task_id`.
3. Kiểm tra tiến độ và nhận danh sách video qua [/dynamic_scene/task/get/](41-deprecated-dynamic-scene.md#doc-1740317337705473) hoặc [/dynamic_scene/get/](41-deprecated-dynamic-scene.md#doc-1740317360823297).
4. Phân tích hiệu quả chuyển đổi theo từng phân cảnh qua endpoint báo cáo [/dynamic_scene/report/get/](41-deprecated-dynamic-scene.md#doc-1740317382510593).

---

## Gửi nguyên liệu phân cảnh (`Submit materials - Deprecated`)
<a id="doc-1740317263937538"></a>
<!-- doc_id: 1740317263937538 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/material/submit/`

> [!WARNING]
> Endpoint này đã ngừng hỗ trợ. Xem tài liệu chính thức: `https://business-api.tiktok.com/portal/docs?id=1740317263937538`

### Mục đích & Khi nào dùng
Sử dụng endpoint này để tải lên các thành phần video gốc và thiết lập cấu trúc câu chuyện (story arc) trước khi tạo video tự động. Kết quả trả về là một mã định danh gói nguyên liệu (`material_package_id`).

### Tham số then chốt
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token xác thực trong Header (`Access-Token: <token>`). |
| advertiser_id | string | Bắt buộc | ID của tài khoản nhà quảng cáo. |
| slots | object[] | Bắt buộc | Danh sách các vị trí phân cảnh (tối đa 6 slot, `order` từ 0 đến 5). Mỗi slot chứa `tag` (nhãn phân cảnh), `video_ids` (tối đa 10 video ID đã tải lên), `mute` (tắt tiếng gốc), `bgm_volume` (âm lượng nhạc nền từ 0 đến 100). |
| auto_soundtrack | boolean | Không | Có sử dụng nhạc nền tự động do hệ thống cung cấp hay không. Mặc định: `false`. |
| music_ids | string[] | Không | Danh sách ID âm nhạc tải lên thủ công qua endpoint tải nhạc. |

### Phản hồi chính
- `material_package_id`: Mã định danh duy nhất của gói tài liệu đã gửi, dùng cho bước tạo tác vụ.

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/material/submit/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "auto_soundtrack": false,
    "slots": [
        {
            "order": 0,
            "tag": "intro",
            "video_ids": ["v10e84g50000c2ee7s5gt180ugq54gm0"],
            "mute": false,
            "bgm_volume": 30
        }
    ]
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/material/submit/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": "7123456789012345678",
    "auto_soundtrack": False,
    "slots": [
        {
            "order": 0,
            "tag": "intro",
            "video_ids": ["v10e84g50000c2ee7s5gt180ugq54gm0"],
            "mute": False,
            "bgm_volume": 30
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Material Package ID:", data.get("data", {}).get("material_package_id"))
```

---

## Tạo tác vụ bất đồng bộ (`Create an async task - Deprecated`)
<a id="doc-1740317320231938"></a>
<!-- doc_id: 1740317320231938 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/create/`

> [!WARNING]
> Endpoint này đã ngừng hỗ trợ. Xem tài liệu chính thức: `https://business-api.tiktok.com/portal/docs?id=1740317320231938`

### Mục đích & Khi nào dùng
Sử dụng endpoint này sau khi đã có `material_package_id` để khởi tạo tiến trình ghép video ngầm trên hệ thống TikTok. Mỗi tác vụ có thể sinh ra tối đa 8 video hoàn chỉnh. Kết quả trả về là một mã định danh tác vụ (`task_id`).

### Tham số then chốt
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token xác thực trong Header. |
| advertiser_id | string | Bắt buộc | ID tài khoản nhà quảng cáo. |
| material_package_id | string | Bắt buộc | Mã gói nguyên liệu nhận được từ endpoint submit material. |

### Phản hồi chính
- `task_id`: Mã tác vụ bất đồng bộ để theo dõi tiến độ xử lý.

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/create/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "material_package_id": "3361016942373889"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": "7123456789012345678",
    "material_package_id": "3361016942373889"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Task ID:", data.get("data", {}).get("task_id"))
```

---

## Lấy kết quả tác vụ bất đồng bộ (`Get the results of an async task - Deprecated`)
<a id="doc-1740317337705473"></a>
<!-- doc_id: 1740317337705473 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/get/`

> [!WARNING]
> Endpoint này đã ngừng hỗ trợ. Xem tài liệu chính thức: `https://business-api.tiktok.com/portal/docs?id=1740317337705473`

### Mục đích & Khi nào dùng
Sử dụng endpoint này để thăm dò (poll) trạng thái của tác vụ sinh video sau khi đã khởi tạo `task_id`. Khi trạng thái chuyển sang `SUCCESS`, bạn sẽ nhận được thông tin chi tiết các video đã tạo kèm URL xem trước.

### Tham số then chốt
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token xác thực trong Header. |
| advertiser_id | string | Bắt buộc | ID tài khoản nhà quảng cáo. |
| task_id | string | Bắt buộc | Mã tác vụ nhận được từ endpoint tạo tác vụ. |

### Phản hồi chính
- `status`: Trạng thái xử lý của tác vụ (`PROCESSING`, `SUCCESS`, `FAIL`).
- `available_quota`: Số lượng video còn lại trong hạn ngạch cho phép tạo.
- `videos`: Mảng chứa tối đa 8 video được tạo, gồm:
  - `video_id`: ID video dùng để tạo quảng cáo.
  - `video_preview_url`: Đường dẫn xem trước video (thời hạn hiệu lực 24 giờ).
  - `music_id`, `music_name`, `music_url`: Thông tin âm nhạc ghép kèm.
  - `duration`, `width`, `height`: Thông số kỹ thuật video.
  - `story_arc`, `slots`: Thứ tự và cấu trúc các phân cảnh đã ghép.

### Ví dụ gọi API

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/get/?advertiser_id=7123456789012345678&task_id=task_example_123' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/task/get/"

params = {
    "advertiser_id": "7123456789012345678",
    "task_id": "task_example_123"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
task_data = data.get("data", {})
print("Task Status:", task_data.get("status"))

for video in task_data.get("videos", []):
    print("  - Video ID:", video.get("video_id"), "| Preview:", video.get("video_preview_url"))
```

---

## Lấy danh sách tất cả video đã tạo (`Get all videos - Deprecated`)
<a id="doc-1740317360823297"></a>
<!-- doc_id: 1740317360823297 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/get/`

> [!WARNING]
> Endpoint này đã ngừng hỗ trợ. Xem tài liệu chính thức: `https://business-api.tiktok.com/portal/docs?id=1740317360823297`

### Mục đích & Khi nào dùng
Sử dụng endpoint này để tra cứu danh sách toàn bộ các video đã được sinh ra từ một gói nguyên liệu (`material_package_id`), hỗ trợ phân trang kết quả để kiểm tra lại các video thành công.

### Tham số then chốt
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token xác thực trong Header. |
| advertiser_id | string | Bắt buộc | ID tài khoản nhà quảng cáo. |
| material_package_id | string | Bắt buộc | ID gói nguyên liệu cần lấy video. |
| page | number | Không | Số trang cần truy vấn. Mặc định: `1`. |
| page_size | number | Không | Số bản ghi trên mỗi trang. Mặc định: `10`. |

### Phản hồi chính
- `list`: Danh sách các video đã tạo kèm `video_id`, `video_preview_url` (hiệu lực 24h), `music_id`, kích thước và thời lượng.
- `page_info`: Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`).

### Ví dụ gọi API

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/get/?advertiser_id=7123456789012345678&material_package_id=3361016942373889&page=1&page_size=10' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/get/"

params = {
    "advertiser_id": "7123456789012345678",
    "material_package_id": "3361016942373889",
    "page": 1,
    "page_size": 10
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for video in data.get("data", {}).get("list", []):
    print("Video ID:", video.get("video_id"), "| Nhạc:", video.get("music_name"))
```

---

## Chạy báo cáo hiệu suất phân cảnh (`Run a report - Deprecated`)
<a id="doc-1740317382510593"></a>
<!-- doc_id: 1740317382510593 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/report/get/`

> [!WARNING]
> Endpoint này đã ngừng hỗ trợ. Xem tài liệu chính thức: `https://business-api.tiktok.com/portal/docs?id=1740317382510593`

### Mục đích & Khi nào dùng
Sử dụng endpoint này để trích xuất báo cáo đo lường hiệu suất chi tiết của từng phân cảnh và từng mẫu video được tạo bởi Dynamic Scene. Báo cáo giúp nhà quảng cáo phân tích cấu trúc kịch bản (`story_arc`) và thứ tự phân cảnh nào mang lại lượt xem hết (`complete_plays`) hoặc tỷ lệ rời bỏ (`break_plays`) cao nhất.

### Tham số then chốt
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token xác thực trong Header. |
| advertiser_id | string | Bắt buộc | ID tài khoản nhà quảng cáo. |
| data_level | string | Bắt buộc | Cấp độ dữ liệu báo cáo. Giá trị hỗ trợ: `ADGROUP`. |
| input_ids | string[] | Bắt buộc | Danh sách ID nhóm quảng cáo (ad group ID) cần truy vấn. |
| dimensions | string[] | Bắt buộc | Các chiều dữ liệu phân nhóm. Bắt buộc phải truyền đầy đủ cả 5 chiều: `["advertiser_id", "adgroup_id", "story_arc", "order", "video_id"]`. |
| metrics | string[] | Không | Danh sách các chỉ số cần đo lường: `clicks`, `complete_plays`, `break_plays`, `ctr`, `complete_play_rate`, `break_play_rate`. |
| start_time | string | Bắt buộc | Ngày bắt đầu truy vấn (`YYYY-MM-DD`). |
| end_time | string | Bắt buộc | Ngày kết thúc truy vấn (`YYYY-MM-DD`), khoảng cách không quá 1 năm so với ngày bắt đầu. |
| filters | object[] | Không | Điều kiện lọc theo trường `field_name` (`story_arc`, `order`), `filter_type` (`IN`), `filter_value`. |
| page | number | Không | Số trang. Mặc định: `1`. |
| page_size | number | Không | Số bản ghi mỗi trang (1-1000). Mặc định: `10`. |

### Phản hồi chính
- `dimensions`: Chứa thông tin nhóm gồm `advertiser_id`, `adgroup_id`, `story_arc`, `order`, `video_id`.
- `metrics`: Các chỉ số đo lường hiệu suất gồm lượt nhấp (`clicks`), lượt xem hết (`complete_plays` / `scene_play_complete`), lượt người xem bỏ dở (`break_plays` / `play_break_count`), tỷ lệ nhấp (`ctr`), tỷ lệ xem hết (`complete_play_rate`), tỷ lệ bỏ dở (`break_play_rate`).

### Ví dụ gọi API

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/report/get/?advertiser_id=7123456789012345678&data_level=ADGROUP&input_ids=%5B%221734945725409298%22%5D&dimensions=%5B%22advertiser_id%22%2C%22adgroup_id%22%2C%22story_arc%22%2C%22order%22%2C%22video_id%22%5D&start_time=2026-06-01&end_time=2026-06-07' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests
import json

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/dynamic_scene/report/get/"

params = {
    "advertiser_id": "7123456789012345678",
    "data_level": "ADGROUP",
    "input_ids": json.dumps(["1734945725409298"]),
    "dimensions": json.dumps(["advertiser_id", "adgroup_id", "story_arc", "order", "video_id"]),
    "start_time": "2026-06-01",
    "end_time": "2026-06-07"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for row in data.get("data", {}).get("list", []):
    dims = row.get("dimensions", {})
    metrics = row.get("metrics", {})
    print(f"Video {dims.get('video_id')} (Thứ tự: {dims.get('order')} - Kịch bản: {dims.get('story_arc')})")
    print(f"  - Clicks: {metrics.get('clicks')} | Hoàn thành: {metrics.get('scene_play_complete')} | Bỏ dở: {metrics.get('play_break_count')}")
```
