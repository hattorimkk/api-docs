# An toàn thương hiệu (Brand Safety)

Nhóm API An toàn thương hiệu (Brand Safety) cho phép nhà quảng cáo thiết lập và quản lý các tiêu chuẩn an toàn thương hiệu bên thứ nhất (First-party Brand Safety) ở cấp tài khoản quảng cáo thông qua Trung tâm An toàn Thương hiệu (Brand Safety Hub). Các cài đặt này giúp bảo vệ uy tín thương hiệu khi phân phối quảng cáo trực tuyến trên TikTok, bao gồm bộ lọc kho nội dung (Inventory Filter) và các biện pháp kiểm soát tính phù hợp như Loại trừ danh mục (Category Exclusion) và Độ nhạy cảm ngành dọc (Vertical Sensitivity).

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan an toàn thương hiệu | - | - | Khái quát trung tâm kiểm soát an toàn thương hiệu và các cấp độ bộ lọc nội dung |
| Lấy cài đặt Trung tâm An toàn Thương hiệu | `GET` | `/open_api/v1.3/tiktok_inventory_filters/get/` | Tra cứu cấu hình an toàn thương hiệu mặc định cấp tài khoản quảng cáo |
| Cài đặt hoặc cập nhật Trung tâm An toàn Thương hiệu | `POST` | `/open_api/v1.3/tiktok_inventory_filters/update/` | Cập nhật bộ lọc kho nội dung, danh mục loại trừ và độ nhạy cảm ngành |

---

## Tổng quan an toàn thương hiệu (`Brand Safety`)
<a id="doc-1830112418755778"></a>
<!-- doc_id: 1830112418755778 -->

Các giải pháp An toàn thương hiệu được thiết kế nhằm bảo vệ danh tiếng thương hiệu của các doanh nghiệp khi quảng cáo trực tuyến. Trung tâm An toàn Thương hiệu (Brand Safety Hub) là nơi tập trung ở cấp độ tài khoản quảng cáo, nơi bạn có thể cấu hình các tùy chọn an toàn thương hiệu bên thứ nhất. Các cài đặt này sẽ tự động áp dụng cho các chiến dịch trong tương lai.

> [!NOTE]
> - Hiện tại, các cấu hình thông qua Brand Safety API sẽ tự động áp dụng cho các [Chiến dịch Smart+ (Smart+ Campaigns)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1767959274087425) trong tương lai, nhưng sẽ không tự động áp dụng cho các chiến dịch thông thường được tạo qua [/campaign/create/](24-campaign.md#doc-1739318962329602).
> - Để tìm hiểu chi tiết về các tính năng an toàn thương hiệu khả dụng, xem [An toàn thương hiệu](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505).

Nhóm này bao gồm các endpoint sau:
- [Lấy cài đặt Trung tâm An toàn Thương hiệu](22-brand-safety.md#doc-1830112550443073): Tra cứu cấu hình an toàn thương hiệu cấp tài khoản.
- [Cài đặt hoặc cập nhật Trung tâm An toàn Thương hiệu](22-brand-safety.md#doc-1830112569774274): Thiết lập hoặc sửa đổi cấu hình an toàn thương hiệu.

---

## Lấy cài đặt Trung tâm An toàn Thương hiệu của tài khoản quảng cáo (`Get the Brand Safety Hub settings of an ad account`)
<a id="doc-1830112550443073"></a>
<!-- doc_id: 1830112550443073 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/tiktok_inventory_filters/get/`

**Mục đích**: Lấy các cài đặt hiện tại trong Trung tâm An toàn Thương hiệu của một tài khoản quảng cáo, bao gồm Bộ lọc kho nội dung TikTok (TikTok Inventory Filter) và các biện pháp kiểm soát tính phù hợp như Loại trừ danh mục (Category Exclusion) và Độ nhạy cảm ngành dọc (Vertical Sensitivity).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo TikTok. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `cover_all_ad_objectives` | boolean | Cho biết có áp dụng cài đặt an toàn thương hiệu cho tất cả các mục tiêu quảng cáo hay không.<br>• `true`: Áp dụng cho mọi mục tiêu (Reach, Video Views, Community Interaction, Traffic, App Promotion, Lead Generation, Website Conversions, Product Sales).<br>• `false`: Chỉ áp dụng cho các mục tiêu Tiếp cận (Reach), Lượt xem video (Video Views) và Tương tác cộng đồng (Community Interaction). |
| ↳ `brand_safety_type` | string | Cấp độ bộ lọc kho nội dung áp dụng cho bảng tin Dành cho bạn (For You), Đang theo dõi (Following), Trang hồ sơ (Profile) và Trang tìm kiếm (Search feed).<br><br>**Enum**:<br>• `EXPANDED_INVENTORY`: Kho nội dung mở rộng (quảng cáo không xuất hiện cạnh nội dung không phù hợp rõ ràng, nhưng có thể xuất hiện cạnh nội dung có chủ đề trưởng thành).<br>• `STANDARD_INVENTORY`: Kho nội dung tiêu chuẩn (phù hợp với hầu hết các thương hiệu).<br>• `LIMITED_INVENTORY`: Kho nội dung giới hạn (không xuất hiện cạnh nội dung có chủ đề trưởng thành).<br>• `NO_BRAND_SAFETY`: Toàn bộ kho nội dung không áp dụng giải pháp an toàn thương hiệu. |
| ↳ `category_exclusion_ids` | string[] | Danh sách ID các danh mục nội dung mà bạn muốn tránh hiển thị quảng cáo bên cạnh. Tra cứu chi tiết danh mục qua [/tool/content_exclusion/info/](70-tools-p2.md#doc-1769738105333826). *(Lưu ý: Không áp dụng cho mục tiêu Doanh số sản phẩm Product Sales).* |
| ↳ `vertical_sensitivity_id` | string | ID danh mục ngành nghề nhạy cảm cần loại trừ. Tra cứu qua [/tool/content_exclusion/info/](70-tools-p2.md#doc-1769738105333826). *(Lưu ý: Không áp dụng cho các mục tiêu Traffic, App Promotion, Lead Generation, Website Conversions, Product Sales).* |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/tiktok_inventory_filters/get/?advertiser_id=6789012345678901234" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
ADVERTISER_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/tiktok_inventory_filters/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
params = {"advertiser_id": ADVERTISER_ID}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000801111222333444555",
  "data": {
    "brand_safety_type": "STANDARD_INVENTORY",
    "category_exclusion_ids": [
      "201"
    ],
    "cover_all_ad_objectives": true,
    "vertical_sensitivity_id": "1001"
  }
}
```

---

## Cài đặt hoặc cập nhật Trung tâm An toàn Thương hiệu (`Set or update the Brand Safety Hub settings of an ad account`)
<a id="doc-1830112569774274"></a>
<!-- doc_id: 1830112569774274 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/tiktok_inventory_filters/update/`

**Mục đích**: Thiết lập hoặc cập nhật cấu hình Trung tâm An toàn Thương hiệu cho một tài khoản quảng cáo.

> [!NOTE]
> Khi cập nhật cài đặt an toàn thương hiệu, bạn cần chỉ định đồng thời cả ba tham số: `brand_safety_type`, `category_exclusion_ids`, và `vertical_sensitivity_id`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo TikTok. |
| `cover_all_ad_objectives` | boolean | Không | Áp dụng cài đặt cho tất cả các mục tiêu quảng cáo (`true`) hay chỉ áp dụng cho Tiếp cận, Lượt xem video và Tương tác cộng đồng (`false`). Mặc định: `false`. |
| `brand_safety_type` | string | Có | Cấp độ bộ lọc kho nội dung.<br><br>**Enum**:<br>• `EXPANDED_INVENTORY`: Kho nội dung mở rộng.<br>• `STANDARD_INVENTORY`: Kho nội dung tiêu chuẩn.<br>• `LIMITED_INVENTORY`: Kho nội dung giới hạn. |
| `category_exclusion_ids` | string[] | Không | Danh sách ID danh mục nội dung muốn loại trừ (chỉ hợp lệ khi `brand_safety_type` là `STANDARD_INVENTORY` hoặc `LIMITED_INVENTORY`). Lấy danh sách ID qua [/tool/content_exclusion/get/](70-tools-p2.md#doc-1769738074686465). |
| `vertical_sensitivity_id` | string | Không | ID danh mục ngành nghề nhạy cảm cần loại trừ (chỉ hợp lệ khi `brand_safety_type` là `STANDARD_INVENTORY` hoặc `LIMITED_INVENTORY`). Lấy danh sách ID qua [/tool/content_exclusion/get/](70-tools-p2.md#doc-1769738074686465). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về sau khi cập nhật thành công. |
| ↳ `cover_all_ad_objectives` | boolean | Trạng thái áp dụng cho tất cả mục tiêu quảng cáo. |
| ↳ `brand_safety_type` | string | Cấp độ bộ lọc kho nội dung đã lưu (`EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`). |
| ↳ `category_exclusion_ids` | string[] | Danh sách ID danh mục loại trừ đã cấu hình. |
| ↳ `vertical_sensitivity_id` | string | ID ngành nghề nhạy cảm đã cấu hình. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/tiktok_inventory_filters/update/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "cover_all_ad_objectives": true,
    "brand_safety_type": "STANDARD_INVENTORY",
    "category_exclusion_ids": ["201"],
    "vertical_sensitivity_id": "1001"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000080222333444555666",
  "data": {
    "brand_safety_type": "STANDARD_INVENTORY",
    "category_exclusion_ids": [
      "201"
    ],
    "cover_all_ad_objectives": true,
    "vertical_sensitivity_id": "1001"
  }
}
```
