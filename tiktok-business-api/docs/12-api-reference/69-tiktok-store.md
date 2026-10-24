# TikTok Store

> Phân hệ: apiref:TikTok Store.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. TikTok Store (#doc-1740661959804929)](#doc-1740661959804929)
- [2. Get available stores under an ad account (#doc-1752267762718722)](#doc-1752267762718722)
- [3. Get products within a TikTok Shop (#doc-1793482248880130)](#doc-1793482248880130)

---

<a id="doc-1740661959804929"></a>
<!-- doc_id: 1740661959804929 -->
<!-- doc_id: 1740661959804929 -->
# TikTok Store
> Đường dẫn: API Reference > TikTok Store
A TikTok store is an entity that merchants can use to manage and sell products on TikTok. TikTok Store API enables you to retrieve first-party stores (TikTok Shops) under an ad account and products within TikTok Shops.

See [Get started](../09-marketing-api/tiktok-store.md#doc-1739581925704769) to learn about the roles and concepts commonly used in TikTok Store and the general workflow.

This group consists of the following endpoint:
* [Get available stores under an ad account](69-tiktok-store.md#doc-1752267762718722)
* [Get products within a TikTok Shop](69-tiktok-store.md#doc-1793482248880130)

---

<a id="doc-1752267762718722"></a>
<!-- doc_id: 1752267762718722 -->
<!-- doc_id: 1752267762718722 -->
# Get available stores under an ad account
> Đường dẫn: API Reference > TikTok Store > Get available stores under an ad account
Sử dụng endpoint này để lấy thông tin the list of available first-party stores (TikTok Shops) under an ad account.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/store/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id | string | ID of the first-party store (TikTok Shop) that you want to filter by. If not specified, the results for all available `store_id` under the specified advertiser account will be returned. <br><p><span style="color:darkred"><b>Note</b></span>: To get the TikTok Shop ID, you can use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401):<ul><li>When in the response `asset_type` is `TIKTOK_SHOP`, the returned `asset_id` is the TikTok Shop ID.</li></ul> |
| store_type | string | Store type that you want to filter by. <br>Các giá trị enum hỗ trợ: `TIKTOK_SHOP` (TikTok Shop) .<br>If not specified, the results for all stores under the specified advertiser account will be returned. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api/open_api/v1.3/store/list/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
#| stores | object[] | Information about the available stores under the ad account. |
##| store_authorized_bc_id | string | ID of the Business Center that is authorized to access the store (`store_id`). One store may be accessed by more than one Business Center. |
##| store_id | string | ID of the TikTok Shop. See [Create Video Shopping Ads with products from TikTok Shopping-Create an ad group](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361719059457) to learn about how to use `store_id` to create Shopping Ads |
##| store_type | string | Store type. Các giá trị enum hỗ trợ: `TIKTOK_SHOP` (TikTok Shop). |
##| store_name | string | Store name. |
##|store_code | string | Returned when the  `store_type` of the store is `TIKTOK_SHOP`.<br><br>The shop code of the first-party store (TikTok Shop).|
##| catalog_id {-To-be-deprecated}| string | ID of the catalog that is bound to the store. One catalog can be bound to only one store. |
##| targeting_region_codes | string[] | Region codes that the store can be used to target. See [Appendix-Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010) to find out what the region codes stand for. |
| request_id | string | The log ID of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "stores": [
            {
                "tiktok_account_binding_status": null,
                "store_id": "{{store_id}}",
                "store_type": "TIKTOK_SHOP",
                "catalog_id": "{{catalog_id}}",
                "store_authorized_bc_id": "{{store_authorized_bc_id}}",
                "store_name": "{{store_name}}",
				"store_code": "{{store_code}}",
                "targeting_region_codes": [
                    "ID"
                ]
            }
        ]
    }
}
```

---

<a id="doc-1793482248880130"></a>
<!-- doc_id: 1793482248880130 -->
<!-- doc_id: 1793482248880130 -->
# Get products within a TikTok Shop
> Đường dẫn: API Reference > TikTok Store > Get products within a TikTok Shop
Sử dụng endpoint này để truy xuất the products within a first-party store (TikTok Shop).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/store/product/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID). <br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| store_id ***(Bắt buộc)*** | string | TikTok Shop ID. <br><br>To obtain the ID list of TikTok Shops associated with an ad account, use [/store/list/](69-tiktok-store.md#doc-1752267762718722). |
| filtering | object | Điều kiện lọc dữ liệu. |
#| item_group_ids | string[] | Product SPU (standard product unit) IDs. <br><br>Kích thước tối đa: 10. |
#| ad_creation_eligible | string | The type of ad or campaign that the products are eligible for. <br><br> Các giá trị enum hỗ trợ: <ul><li>`CUSTOM_SHOP_ADS`: Shopping Ads, including [Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361719059457) and [Product Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1785886237030401).</li><li>`GMV_MAX`: [Product GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009220448257).</li></ul><br> If this field is not specified, the response will not include the eligibility of the products for Product GMV Max Campaigns. |
#| product_name | string | Product name. |
#| product_status | string | Valid when `ad_creation_eligible` is `GMV_MAX`.<br><br>The status of the product.<br><br>Các giá trị enum hỗ trợ: <br><ul><li>`AVAILABLE`: The product is available for use in ads. </li><li>`NOT_AVAILABLE`: The product is not available for use in ads. </li><li>`ALL`: All products will be returned. </li></ul>Giá trị mặc định: `ALL`. |
#| exclude_gmv_max_occupied_products | boolean | Có thực hiện exclude products that are already part of a GMV Max Campaign. <br><br>Các giá trị được hỗ trợ: <br><ul><li>`true`: Exclude products that are already part of a GMV Max Campaign.</li><li>`false`: Include all products, Liệu or not they are already part of a GMV Max Campaign.</li></ul>|
| advertiser_id **(Điều kiện)** | string | Bắt buộc khi `ad_creation_eligible` is passed. <br><br> ID tài khoản quảng cáo TikTok. |
| sort_field | string | Field to sort by. <br><br> Các giá trị enum hỗ trợ: <ul><li>`min_price`: the returned `min_price` field.</li><li>`historical_sales`: the returned `historical_sales` field. </li><li>`update_time`: the returned `update_time` field. </li></ul>  |
| sort_type | string | Thứ tự sắp xếp kết quả. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ASC`: ascending. </li><li>`DESC`: descending. </li></ul> |
| page | integer | Current number of pages. <br><br>Giá trị mặc định: 1. <br><br>Value range: ≥ 1. |
| page_size | integer | Page size. <br><br> Giá trị mặc định: 10. <br><br>Value range: 1-100. |
### Ví dụ lệnh cURL (Example)

#### Get products available for Product GMV Max Campaigns
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/store/product/get/?store_id={{store_id}}&bc_id={{bc_id}}&filtering={"ad_creation_eligible":"GMV_MAX"}&advertiser_id={{advertiser_id}}&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

#### Get products available for Shopping Ads
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/store/product/get/?store_id={{store_id}}&bc_id={{bc_id}}&filtering={"ad_creation_eligible":"CUSTOM_SHOP_ADS"}&advertiser_id={{advertiser_id}}&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

#### Get products within a TikTok Shop without using the `ad_creation_eligible` filter
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/store/product/get/?bc_id={{bc_id}}&store_id={{store_id}}&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| store_products | object[] | The list of products within the TikTok Shop. |
##| store_id | string | TikTok Shop ID. |
##| item_group_id | string | SPU ID of the product. |
##| catalog_id{-Deprecated} | string | The ID of the catalog that the product (`item_group_id`) belongs to.<br><br><p><span style="color:darkred"><b>Note</b></span>: Starting June 30th, 2024, this field returns a null value. |
##| title | string | The title of the product. |
##| product_image_url | string | The URL of the product image. |
##| min_price | string | The minimum price of the product. <br><br><p><span style="color:darkred"><b>Note</b></span>: If you specify one fixed price for the product, the values of `min_price` and `max_price` will be the same. |
##| max_price | string | The maximum price of the product. <br><br><p><span style="color:darkred"><b>Note</b></span>: If you specify one fixed price for the product, the values of `min_price` and `max_price` will be the same. |
##| currency | string | The code of the currency in which the prices (`min_price` and `max_price`) are specified. <br><br>To learn about the currency that a currency code corresponds to, see [Budget verification ratio and precision of each currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
##| historical_sales | number | The historical sales of the product, indicating the number of times the product has been sold. |
##| category | string | The category of the product. |
##| quantity | number | The number of products within the TikTok Shop.<br><br>Example: 5. |
##| status | string | The ad delivery availability status of the product.<br><br>Các giá trị enum hỗ trợ: <ul><li> `AVAILABLE`: The product is available for use in ads.</li><li>`NOT_AVAILABLE`: The product is not available for use in ads.</li></ul>|
##| update_time | string | The Unix/Epoch date-time when the product was last updated, in the format of `YYYY-MM-DD` (UTC time).<br>Example: `2026-01-01 00:00:00`. |
##| gmv_max_ads_status | string | Returned only when the filter field `ad_creation_eligible` is passed in the request. <br><br> The status of the product in an enabled Product GMV Max Campaign. <br><br> Các giá trị enum hỗ trợ: <ul><li>`OCCUPIED`: The product is being promoted in an enabled Product GMV Max Campaign.</li><li>`UNOCCUPIED`: The product is not being promoted in an enabled Product GMV Max Campaign.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>: If status is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`, the product can be used in a Product GMV Max Campaign. |
##| is_running_custom_shop_ads | boolean | Returned only when the filter field `ad_creation_eligible` is set to `GMV_MAX` in the request. <br><br>Liệu product is being promoted in enabled Video Shopping Ads or Product Shopping Ads. <br><br> Các giá trị được hỗ trợ: `true`, `false`. <br><br> If `is_running_custom_shop_ads` is `true`, you can call [/gmv_max/occupied_custom_shop_ads/list/](45-gmv-max-p2.md#doc-1822001136924674) and set `occupied_asset_type` to `SPU` to find out the specific Video Shopping Ads or Product Shopping Ads that are using the product. To disable these ads, use [/ad/status/update/](02-ads-p2.md#doc-1739953422970882) and set `operation_status` to `DISABLE`. |
#| page_info | object | Pagination information. |
##| page | number | Current Số trang cần lấy dữ liệu. |
##| page_size | number | Paging size. |
##| total_number | number | Tổng số kết quả tìm thấy. |
##| total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
#### Get products available for Product GMV Max Campaigns
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "store_products": [
            {
                "status": "AVAILABLE",
                "product_image_url": "{{product_image_url}}",
                "catalog_id": null,
                "category": "{{category}}",
                "historical_sales": 0,
			    "quantity": 2,
                "item_group_id": "{{item_group_id}}",
                "max_price": "1000",
                "store_id": "{{store_id}}",
                "min_price": "1000",
                "currency": "IDR",
                "title": "{{title}}",
                "gmv_max_ads_status": "OCCUPIED",
                "is_running_custom_shop_ads": true,
                "update_time": "2026-08-19 03:03:33"
            },
            {
                "status": "AVAILABLE",
                "product_image_url": "{{product_image_url}}",
                "catalog_id": null,
                "category": "{{category}}",
                "historical_sales": 0,
				"quantity": 2,
                "item_group_id": "{{item_group_id}}",
                "max_price": "100",
                "store_id": "{{store_id}}",
                "min_price": "100",
                "currency": "IDR",
                "title": "{{title}}",
                "gmv_max_ads_status": "OCCUPIED",
                "is_running_custom_shop_ads": false,
                "update_time": "2026-08-19 03:03:33"
            }
        ],
        "page_info": {
            "total_number": 2,
            "page_size": 100,
            "page": 1,
            "total_page": 1
        }
    }
}
```

#### Get products available for Shopping Ads
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "page": 1,
            "total_number": 2,
            "page_size": 100,
            "total_page": 1
        },
        "store_products": [
            {
                "category": "{{category}}",
                "currency": "IDR",
                "max_price": "1000",
                "catalog_id": null,
                "gmv_max_ads_status": "UNOCCUPIED",
                "product_image_url": "{{product_image_url}}",
                "historical_sales": 0,
				"quantity": 2,
                "store_id": "{{store_id}}",
                "item_group_id": "{{item_group_id}}",
                "title": "{{title}}",
                "status": "AVAILABLE",
                "min_price": "1000",
                "update_time": "2026-08-19 03:03:33"
            },
            {
                "category": "{{category}}",
                "currency": "IDR",
                "max_price": "100",
                "catalog_id": null,
                "gmv_max_ads_status": "UNOCCUPIED",
                "product_image_url": "{{product_image_url}}",
                "historical_sales": 0,
				"quantity": 2,
                "store_id": "{{store_id}}",
                "item_group_id": "{{item_group_id}}",
                "title": "{{title}}",
                "status": "AVAILABLE",
                "min_price": "100",
                "update_time": "2026-08-19 03:03:33"
            }
        ]
    }
}
```

#### Get products within a TikTok Shop without using the `ad_creation_eligible` filter
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "total_page": 1,
            "page": 1,
            "page_size": 100,
            "total_number": 2
        },
        "store_products": [
            {
                "currency": "GBP",
                "category": "Fashion Accessories > Eyewear > Glasses Cases & Accessories",
                "catalog_id": "{{catalog_id}}",
                "max_price": "0.07",
                "status": "AVAILABLE",
                "title": "{{title}}",
                "product_image_url": "{{product_image_url}}",
                "store_id": "{{store_id}}",
                "item_group_id": "{{item_group_id}}",
                "min_price": "0.07",
				"quantity": 2,
                "historical_sales": 18,
                "update_time": "2026-08-19 03:03:33"
            },
            {
                "currency": "GBP",
                "category": "Womenswear & Underwear > Women's Tops > Vests",
                "catalog_id": "{{catalog_id}}",
                "max_price": "0.7",
                "status": "NOT_AVAILABLE",
                "title": "{{title}}",
                "product_image_url": "{{product_image_url}}",
                "store_id": "{{store_id}}",
                "item_group_id": "{{item_group_id}}",
                "min_price": "0.7",
				"quantity": 2,
                "historical_sales": 0,
                "update_time": "2026-08-19 03:03:33"
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **TikTok Store**:

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

