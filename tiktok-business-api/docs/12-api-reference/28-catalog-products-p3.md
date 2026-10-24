# Sản phẩm Catalog (Catalog Products) — phần 3/3

> Phân hệ: API Reference > Catalog Products > Get the product handling log.
> Hướng dẫn kiểm tra trạng thái xử lý sản phẩm sau khi tải lên hoặc xóa hàng loạt trong Catalog, theo dõi chi tiết các lỗi dữ liệu sản phẩm và tải về danh sách sản phẩm bị lỗi dưới dạng tệp CSV.

---

## Mục lục điều hướng
- [1. Lấy nhật ký xử lý sản phẩm (`GET /open_api/v1.3/catalog/product/log/`)](#1-lay-nhat-ky-xu-ly-san-pham)
- [2. Mã nguồn mẫu Data Retrieval (Python & cURL)](#2-ma-nguon-mau-data-retrieval)

---

<a id="doc-1740570027173889"></a>
<!-- doc_id: 1740570027173889 -->
<a id="1-lay-nhat-ky-xu-ly-san-pham"></a>
## 1. Lấy nhật ký xử lý sản phẩm (Get the product handling log)

Sử dụng endpoint này để kiểm tra xem các sản phẩm đã được tải lên hoặc xóa thành công hay chưa, và các bước khắc phục cần thiết nếu quá trình xử lý gặp lỗi.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/catalog/product/log/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số (Parameters)

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | **Bắt buộc** | ID của Business Center sở hữu Catalog. |
| `catalog_id` | string | **Bắt buộc** | ID của Catalog. |
| `feed_log_id` | string | **Bắt buộc** | ID nhật ký xử lý sản phẩm (nhận được sau khi gọi API tải lên tệp feed hoặc tải lên theo schema). |
| `language` | string | Không | Ngôn ngữ hiển thị thông báo lỗi và gợi ý khắc phục. Giá trị hỗ trợ: `en` (Tiếng Anh), `zh-CN` (Tiếng Trung), `ja-JP` (Tiếng Nhật), `de` (Tiếng Đức), `es` (Tiếng Tây Ban Nha), `fr` (Tiếng Pháp), `hi-IN` (Tiếng Hindi), `id` (Tiếng Indonesia), `it` (Tiếng Ý), `ko` (Tiếng Hàn), `ms` (Tiếng Mã Lai), `ru` (Tiếng Nga), `th` (Tiếng Thái), `tr` (Tiếng Thổ Nhĩ Kỳ), `vi` (Tiếng Việt). Mặc định: `en`. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). |
| `request_id` | string | ID duy nhất nhận diện request phục vụ tra cứu log. |
| `data` | object | Dữ liệu nhật ký xử lý sản phẩm. |
| ↳ `status` | string | Trạng thái xử lý của tác vụ. Giá trị: `PROCESSING` (Đang xử lý), `SUCCESS` (Thành công hoàn toàn), `FAILED` (Thất bại), `PARTIAL_SUCCESS` (Thành công một phần). |
| ↳ `catalog_id` | number/string | ID định danh của Catalog. |
| ↳ `total_count` | number | Tổng số sản phẩm có trong yêu cầu xử lý. |
| ↳ `update_count` | number | Số sản phẩm được cập nhật thành công. |
| ↳ `insert_count` | number | Số sản phẩm mới được thêm thành công. |
| ↳ `delete_count` | number | Số sản phẩm được xóa thành công. |
| ↳ `failed_count` | number | Số lượng sản phẩm gặp lỗi không thể xử lý. |
| ↳ `start_time` | string | Thời điểm bắt đầu xử lý (`YYYY-MM-DD HH:MM:SS`). |
| ↳ `end_time` | string | Thời điểm kết thúc xử lý (`YYYY-MM-DD HH:MM:SS`). |
| ↳ `error_details` | object | Chi tiết các lỗi phát sinh trong quá trình xác thực dữ liệu sản phẩm. |
| ↳↳ `issues` | object[] | Danh sách các vấn đề cụ thể về trường dữ liệu. |
| ↳↳↳ `field` | string | Tên trường bị lỗi (ví dụ: `age_group`, `gender`, `price`). |
| ↳↳↳ `issue` | string | Mô tả ngắn gọn lỗi (ví dụ: `Invalid value: age_group`). |
| ↳↳↳ `suggestion` | string | Hướng dẫn gợi ý cách khắc phục và danh sách giá trị hợp lệ. |
| ↳↳↳ `affected_product_count` | number | Số lượng sản phẩm bị ảnh hưởng bởi lỗi này. |
| ↳↳↳ `affected_product_item_list` | object[] | Danh sách chi tiết các sản phẩm bị ảnh hưởng kèm mã `sku_id` và giá trị không hợp lệ. |
| ↳↳ `download_path` | object | Bản đồ đường dẫn tải tệp CSV chi tiết lỗi theo từng mã ngôn ngữ (ví dụ: `vi`, `en`, `zh-CN`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000110",
  "data": {
    "status": "PARTIAL_SUCCESS",
    "catalog_id": 6865965734837634822,
    "total_count": 100,
    "update_count": 98,
    "failed_count": 2,
    "start_time": "2026-03-23 05:15:09",
    "end_time": "2026-03-23 05:15:15",
    "error_details": {
      "issues": [
        {
          "field": "age_group",
          "issue": "Invalid value: age_group",
          "suggestion": "Trường 'age_group' nhận giá trị không hợp lệ. Giá trị hỗ trợ gồm: newborn/infant/toddler/kids/adult",
          "affected_product_count": 1,
          "affected_product_item_list": [
            {
              "sku_id": "SKU_SHOE_001",
              "title": "Giày chạy bộ thể thao",
              "value": "teen"
            }
          ]
        }
      ],
      "download_path": {
        "en": "https://tosv.tiktokcdn.com/obj/dpafeed/errors_en.csv",
        "vi": "https://tosv.tiktokcdn.com/obj/dpafeed/errors_vi.csv"
      }
    }
  }
}
```

---

<a id="2-ma-nguon-mau-data-retrieval"></a>
## 2. Mã nguồn mẫu Data Retrieval (Python & cURL)

### cURL tra cứu nhật ký xử lý sản phẩm
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/catalog/product/log/?bc_id=YOUR_BC_ID&catalog_id=YOUR_CATALOG_ID&feed_log_id=YOUR_FEED_LOG_ID&language=vi" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script theo dõi tiến độ xử lý Feed
```python
import time
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BC_ID = "YOUR_BC_ID"
CATALOG_ID = "YOUR_CATALOG_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {"Access-Token": ACCESS_TOKEN}

def poll_product_handling_log(bc_id, catalog_id, feed_log_id, max_retries=10, delay=5):
    """
    Thăm dò trạng thái nhật ký xử lý sản phẩm cho đến khi hoàn thành (SUCCESS/FAILED/PARTIAL_SUCCESS).
    """
    url = f"{BASE_URL}/catalog/product/log/"
    params = {
        "bc_id": bc_id,
        "catalog_id": catalog_id,
        "feed_log_id": feed_log_id,
        "language": "vi"
    }
    
    for attempt in range(max_retries):
        res = requests.get(url, headers=headers, params=params).json()
        if res.get("code") == 0:
            data = res.get("data", {})
            status = data.get("status")
            print(f"Lần kiểm tra {attempt + 1}: Trạng thái = {status}")
            
            if status in ("SUCCESS", "FAILED", "PARTIAL_SUCCESS"):
                total = data.get("total_count", 0)
                updated = data.get("update_count", 0)
                failed = data.get("failed_count", 0)
                print(f"Hoàn tất: Tổng = {total}, Thành công = {updated}, Lỗi = {failed}")
                
                # Kiểm tra lỗi chi tiết nếu có
                if failed > 0:
                    issues = data.get("error_details", {}).get("issues", [])
                    print(f"Chi tiết {len(issues)} loại lỗi:")
                    for issue in issues:
                        print(f" - [{issue.get('field')}] {issue.get('issue')}: {issue.get('suggestion')}")
                return data
        else:
            print(f"Lỗi truy vấn: {res.get('code')} - {res.get('message')}")
            
        time.sleep(delay)
        
    print("Hết thời gian chờ xử lý!")
    return None

if __name__ == "__main__":
    poll_product_handling_log(BC_ID, CATALOG_ID, "FEED_LOG_123456")
```

