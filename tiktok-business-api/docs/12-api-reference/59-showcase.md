# Showcase

Tài liệu này cung cấp các endpoint quản lý và truy vấn Showcase (Tủ trưng bày sản phẩm) trên TikTok. Showcase cho phép khách hàng mua sắm trực tiếp từ tài khoản của người bán (seller) hoặc nhà sáng tạo (creator). Bạn có thể tìm thấy tab Showcase khi nhấn vào biểu tượng túi mua sắm trên trang hồ sơ của tài khoản TikTok. Để tìm hiểu thêm về cách sử dụng Showcase, xem [tại đây](https://ads.tiktok.com/help/article?aid=10013245&redirected=1). Showcase API cho phép bạn lấy các danh tính (identity) có quyền Showcase thuộc một tài khoản quảng cáo, lấy thông tin chi tiết của Showcase bao gồm các quốc gia/khu vực mà Showcase có thể nhắm mục tiêu, và danh sách các sản phẩm khả dụng trong Showcase.

Xem [Tạo Video Shopping Ads với sản phẩm từ Showcase](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1759232259360770) để tìm hiểu cách dùng Showcase tạo Video Shopping Ads.

Nhóm này bao gồm các endpoint sau:
- [Lấy danh tính có quyền Showcase theo tài khoản quảng cáo](59-showcase.md#doc-1759233549899778)
- [Lấy các khu vực khả dụng cho Showcase thông qua danh tính](59-showcase.md#doc-1759233561597954)
- [Lấy các sản phẩm khả dụng trong Showcase](59-showcase.md#doc-1759233576199169)

---

## Tổng quan Showcase (`Showcase`)
<a id="doc-1759233493240834"></a>
<!-- doc_id: 1759233493240834 -->

> Đường dẫn: API Reference > Showcase

Showcase là tính năng trên TikTok cho phép khách hàng mua sắm trực tiếp từ tài khoản của người bán hoặc người sáng tạo nội dung. Bạn có thể tìm thấy tab Showcase khi nhấn vào biểu tượng giỏ hàng trên trang hồ sơ của một tài khoản TikTok. Tìm hiểu thêm về Showcase [tại đây](https://ads.tiktok.com/help/article?aid=10013245&redirected=1).

Showcase API cho phép bạn:
- Lấy danh sách danh tính có quyền Showcase trong một tài khoản quảng cáo.
- Xem chi tiết về Showcase, bao gồm quốc gia/khu vực có thể phân phối và danh sách các sản phẩm đang có sẵn trong Showcase.

Xem thêm hướng dẫn: [Create Video Shopping Ads with products from Showcase](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1759232259360770).

---

## Lấy danh tính có quyền Showcase (`Get identities with Showcase permission under an ad account`)
<a id="doc-1759233549899778"></a>
<!-- doc_id: 1759233549899778 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/showcase/identity/get/`

**Mục đích**: Lấy danh sách các danh tính (identities) có quyền Showcase thuộc một tài khoản quảng cáo.

> [!NOTE]
> Chỉ những danh tính có quyền Showcase mới có thể được sử dụng để tạo Quảng cáo mua sắm dạng video (Video Shopping Ads) với các sản phẩm từ Showcase. Xem chi tiết các bước tại [Create Video Shopping Ads with products from Showcase](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1759232259360770).

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token (mã truy cập) đã được ủy quyền. Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của nhà quảng cáo (advertiser ID). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách đầy đủ mã phản hồi và mô tả xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Trả về `0` khi thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất cho yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `identity_list` | object[] | Danh sách danh tính có quyền Showcase. |
| ↳↳ `identity_id` | string | ID của danh tính mà Showcase được liên kết. |
| ↳↳ `identity_type` | string | Loại danh tính. Giá trị enum:<br>• `TT_USER`: Người dùng TikTok (TikTok User).<br>• `BC_AUTH_TT`: Người dùng tài khoản TikTok trong Business Center (TikTok Account User in Business Center).<br>Xem thêm tại [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ `identity_authorized_bc_id` | string | Trả về khi `identity_type` là `BC_AUTH_TT`. ID của Business Center mà Showcase (được gắn với danh tính người dùng tài khoản TikTok trong BC) liên kết cùng. |

### Ví dụ

#### curl
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/showcase/identity/get/?advertiser_id=7123456789012345678' \
--header 'Access-Token: act.example12345abcdef'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/showcase/identity/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202306011234560102452431071406594F",
    "data": {
        "identity_list": [
            {
                "identity_type": "BC_AUTH_TT",
                "identity_id": "7123456789012345679",
                "identity_authorized_bc_id": "7123456789012345680"
            },
            {
                "identity_type": "BC_AUTH_TT",
                "identity_id": "7123456789012345681",
                "identity_authorized_bc_id": "7123456789012345680"
            }
        ]
    }
}
```

---

## Lấy khu vực khả dụng cho Showcase qua danh tính (`Get the available regions for a Showcase via identity`)
<a id="doc-1759233561597954"></a>
<!-- doc_id: 1759233561597954 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/showcase/region/get/`

**Mục đích**: Lấy danh sách các quốc gia hoặc khu vực mà Showcase có thể nhắm mục tiêu, bằng cách chỉ định danh tính được liên kết với Showcase và có quyền đối với Showcase.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token (mã truy cập) đã được ủy quyền. Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của nhà quảng cáo (advertiser ID). |
| `identity_id` | string | Có | ID của danh tính được liên kết với Showcase và danh tính này cần có quyền đối với Showcase. |
| `identity_type` | string | Có | Loại danh tính. Giá trị enum:<br>• `TT_USER`: Người dùng TikTok.<br>• `BC_AUTH_TT`: Người dùng tài khoản TikTok trong Business Center.<br>Xem thêm tại [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| `identity_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID của Business Center liên kết với danh tính người dùng tài khoản TikTok trong Business Center. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID nhật ký duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `region_codes` | string[] | Danh sách mã quốc gia hoặc khu vực (ví dụ: `["ID"]`) mà Showcase có thể nhắm mục tiêu. Để biết thêm mã quốc gia/khu vực tương ứng, xem [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |

### Ví dụ

#### curl
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/showcase/region/get/?identity_id=7123456789012345679&identity_type=BC_AUTH_TT&advertiser_id=7123456789012345678&identity_authorized_bc_id=7123456789012345680' \
--header 'Access-Token: act.example12345abcdef'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/showcase/region/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "identity_id": "7123456789012345679",
    "identity_type": "BC_AUTH_TT",
    "identity_authorized_bc_id": "7123456789012345680"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202306011234560102452431071406595F",
    "data": {
        "region_codes": [
            "ID"
        ]
    }
}
```

---

## Lấy danh sách sản phẩm trong Showcase (`Get the available products in a Showcase`)
<a id="doc-1759233576199169"></a>
<!-- doc_id: 1759233576199169 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/showcase/product/get/`

**Mục đích**: Lấy danh sách các sản phẩm trong Showcase mà bạn có thể dùng để nhắm mục tiêu đến các quốc gia hoặc khu vực đã chỉ định.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token (mã truy cập) đã được ủy quyền. Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của nhà quảng cáo (advertiser ID). |
| `identity_id` | string | Có | ID của danh tính được liên kết với Showcase và danh tính cần có quyền đối với Showcase. |
| `identity_type` | string | Có | Loại danh tính. Giá trị enum:<br>• `TT_USER`: Người dùng TikTok.<br>• `BC_AUTH_TT`: Người dùng tài khoản TikTok trong Business Center.<br>Xem thêm tại [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| `identity_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID của Business Center liên kết với danh tính người dùng tài khoản TikTok trong Business Center. |
| `region_codes` | string[] | Có | Danh sách mã quốc gia hoặc khu vực mà bạn muốn dùng sản phẩm trong Showcase để nhắm mục tiêu (truyền mảng JSON, ví dụ `["ID"]`). |
| `filtering` | object | Không | Điều kiện lọc. |
| ↳ `item_group_ids` | string[] | Không | Danh sách ID SPU của sản phẩm (Product SPU IDs). Tối đa: 10 ID. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. Giới hạn: ≥ 1. |
| `page_size` | number | Không | Số bản ghi mỗi trang. Mặc định: `10`. Giới hạn: [1, 1000]. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID nhật ký duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `showcase_products` | object[] | Danh sách sản phẩm trong Showcase bạn có thể dùng để nhắm tới các quốc gia hoặc khu vực đã chỉ định. |
| ↳↳ `item_group_id` | string | SPU ID của sản phẩm. |
| ↳↳ `title` | string | Tiêu đề sản phẩm. |
| ↳↳ `product_image_url` | string | URL hình ảnh của sản phẩm. |
| ↳↳ `min_price` | string | Giá thấp nhất của sản phẩm.<br>> [!NOTE]<br>> Nếu bạn thiết lập một mức giá cố định cho sản phẩm, giá trị `min_price` và `max_price` sẽ bằng nhau. |
| ↳↳ `max_price` | string | Giá cao nhất của sản phẩm.<br>> [!NOTE]<br>> Nếu bạn thiết lập một mức giá cố định cho sản phẩm, giá trị `min_price` và `max_price` sẽ bằng nhau. |
| ↳↳ `currency` | string | Mã tiền tệ của các mức giá (`min_price` và `max_price`). Để tìm hiểu loại tiền tệ tương ứng với mã, xem [Tỷ lệ xác minh và độ chính xác ngân sách của từng loại tiền tệ](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| ↳↳ `category` | string | Ngành hàng / danh mục của sản phẩm. |
| ↳↳ `status` | string | Trạng thái sản phẩm. Giá trị enum:<br>• `AVAILABLE`: Sản phẩm có sẵn để sử dụng trong quảng cáo.<br>• `NOT_AVAILABLE`: Sản phẩm không khả dụng để sử dụng trong quảng cáo. |
| ↳↳ `catalog_id` | string | *(Sắp ngừng hỗ trợ - To be deprecated)* ID của danh mục sản phẩm (catalog) mà sản phẩm (`item_group_id`) thuộc về.<br>> [!NOTE]<br>> Kể từ ngày 30 tháng 6 năm 2024, trường này không còn được trả về. |
| ↳↳ `store_id` | string | ID của cửa hàng mà sản phẩm (`item_group_id`) thuộc về. Lưu ý loại cửa hàng duy nhất được hỗ trợ là TikTok Shop. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi trên mỗi trang. |
| ↳↳ `total_number` | number | Tổng số bản ghi kết quả. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### curl
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/showcase/product/get/?identity_id=7123456789012345679&identity_type=BC_AUTH_TT&advertiser_id=7123456789012345678&region_codes=%5B%22ID%22%5D&page=1&page_size=10' \
--header 'Access-Token: act.example12345abcdef'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/showcase/product/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "identity_id": "7123456789012345679",
    "identity_type": "BC_AUTH_TT",
    "region_codes": json.dumps(["ID"]),
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202306011234560102452431071406596F",
    "data": {
        "showcase_products": [
            {
                "category": "Women's Clothing",
                "title": "Summer Dress",
                "status": "AVAILABLE",
                "item_group_id": "1723456789012345",
                "store_id": "7123456789012345688",
                "catalog_id": "7123456789012345699",
                "currency": "IDR",
                "min_price": "100000",
                "product_image_url": "https://p16-va.tiktokcdn.com/obj/tos-maliva-p-0068/dress.jpg",
                "max_price": "120000"
            }
        ],
        "page_info": {
            "total_page": 1,
            "page_size": 10,
            "total_number": 1,
            "page": 1
        }
    }
}
```
