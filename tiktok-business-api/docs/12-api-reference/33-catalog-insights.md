# Insight Catalog

> Phân hệ: apiref:Catalog Insights.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Catalog Insights (#doc-1805640759207937)](#doc-1805640759207937)
- [2. Get filters for catalog product insights (#doc-1805640864553985)](#doc-1805640864553985)
- [3. Get trending catalog products (#doc-1805640886872066)](#doc-1805640886872066)
- [4. Get trending catalog product categories (#doc-1805640900563969)](#doc-1805640900563969)

---

<a id="doc-1805640759207937"></a>
<!-- doc_id: 1805640759207937 -->
<!-- doc_id: 1805640759207937 -->
# Catalog Insights
> Đường dẫn: API Reference > Catalog Insights
> **Important:** By using Catalog API endpoints, you agree to the [Product Catalog Terms](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) and certify that you are abiding by the [TikTok Advertising Policies](https://ads.tiktok.com/help/article?aid=6685586866860720134). Please review these policies and ensure that the items you upload to your catalog don't breach them.

A catalog is an asset that allows you to store information about the products you want to promote on TikTok. Using a catalog is a great solution for anyone who is looking for an efficient way to create and manage ads that feature a variety of products, like an online retailer. Catalog Insights API enables you to obtain insights about trending products in your catalog and trending catalog product categories on TikTok.

See [Overview](../09-marketing-api/catalog.md#doc-1754263078057986) and [Guides](../09-marketing-api/catalog.md#doc-1754263100123137) to learn about the concepts and benefits of catalogs, and to find out how to create and manage catalogs. To learn how to access Catalog Product Insights, see [Obtain Catalog Product Insights](../09-marketing-api/catalog.md#doc-1805642743426050).

This group consists of the following endpoints:
- [Get filters for catalog product insights](33-catalog-insights.md#doc-1805640864553985)
- [Get trending catalog products](33-catalog-insights.md#doc-1805640886872066)
- [Get trending catalog product categories](33-catalog-insights.md#doc-1805640900563969)

---

<a id="doc-1805640864553985"></a>
<!-- doc_id: 1805640864553985 -->
<!-- doc_id: 1805640864553985 -->
# Get filters for catalog product insights
> Đường dẫn: API Reference > Catalog Insights > Get filters for catalog product insights
Use this endpoint to obtain the available filters for generating targeted insights on a limited number of products within an E-commerce catalog.

The returned filter values can be used with [/catalog/insight/product/get/](33-catalog-insights.md#doc-1805640886872066) to obtain insights about trending products in your catalog.

>**Note:**  
>  • Catalog Product Insights become available 24 hours after you have uploaded a minimum of 20 products to your E-commerce catalog. •  The insights are refreshed daily at around 4:00 AM UTC time.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/insight/filter/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). ⏎ To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id  ****(Bắt buộc)**** | string | ID danh mục sản phẩm. ⏎ The catalog needs to be an E-commerce catalog that contains at least 20 products. ⏎ To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. ⏎ To verify that the catalog contains at least 20 products, use [/catalog/overview/](25-catalog-management.md#doc-1740492470201345) and check Liệu sum of the values of the returned `approved`, `rejected`, and `processing` fields is equal to or greater than 20. |
| filter_type  ****(Bắt buộc)**** | string | The type of filter options. ⏎ Các giá trị enum hỗ trợ: •  `CATEGORY_ID`: Product category ID.  •  `BRAND`: Product brand name.  • `AVAILABILITY`: Product availability status. |
| page | integer | Current Số trang cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. Value range: ≥ 1. |
| page_size | integer | Page size. ⏎ Giá trị mặc định: 10. Value range: 1-200. ⏎ **Note**: The `page` and `page_size` parameters are provided to allow you to retrieve paginated results in smaller batches, if needed. However, note that this endpoint does not include pagination information in the response. ⏎ If you don't want to retrieve paginated results, set `page_size` to 50 to obtain the complete set of results in a single response. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/insight/filter/get/?bc_id={{bc_id}}&catalog_id={{catalog_id}}&filter_type=AVAILABILITY&page=1&page_size=200' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| brands | string[] | Returned only when `filter_type` is set to `BRAND` in the request.<br><br> The brand names by which you can filter products within the catalog. |
#| availabilities | string[] | Returned only when `filter_type` is set to `AVAILABILITY` in the request. <br><br> The availability statuses by which you can filter products within the catalog. |
#| categories | object[] | Returned only when `filter_type` is set to `CATEGORY_ID` in the request.<br><br>Information about the categories by which you can filter products within the catalog. |
##| category_id| string | The TikTok product category ID assigned to the product, consisting of three levels separated by the number sign (#), in the format of `"level_id_1#level_id_2#level_id_3"`. <br><br>Example: `601152#842248#601302`. |
##| level_info | object | Details of the levels that the category belongs to. |
###| level_id_1 | string | ID của danh mục sản phẩm TikTok cấp 1. |
###| level_name_1 | string | The name of the level-1 TikTok product category. |
###| level_id_2 | string | ID của danh mục sản phẩm TikTok cấp 2. |
###| level_name_2 | string | The name of the level-2 TikTok product category. |
###| level_id_3 | string | ID của danh mục sản phẩm TikTok cấp 3. |
###| level_name_3 | string | The name of the level-3 TikTok product category. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "availabilities": [
            "OUT_OF_STOCK",
            "IN_STOCK"
        ]
    }
}
```

---

<a id="doc-1805640886872066"></a>
<!-- doc_id: 1805640886872066 -->
<!-- doc_id: 1805640886872066 -->
# Get trending catalog products
> Đường dẫn: API Reference > Catalog Insights > Get trending catalog products
Sử dụng endpoint này để truy xuất up to top 50 trending products based on user engagement on TikTok within an E-commerce catalog.  

>**Note:**  
>  • Catalog Product Insights become available 24 hours after you have uploaded a minimum of 20 products to your E-commerce catalog. •  The insights are refreshed daily at around 4:00 AM UTC time.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/insight/product/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br>The catalog needs to be an E-commerce catalog that contains at least 20 products. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br>To verify that the catalog contains at least 20 products, use [/catalog/overview/](25-catalog-management.md#doc-1740492470201345) and check Liệu sum of the values of the returned `approved`, `rejected`, and `processing` fields is equal to or greater than 20. |
| filtering | object | Điều kiện lọc dữ liệu. |
#| category_ids {+Conditional} | string[] | When `filtering` is specified, you need to provide at least one of `category_ids`, `brands`, and `availabilities`. <br><br> A list of TikTok product category IDs to filter the results by.<br><br> Kích thước tối đa: 50. <br><br>Provide one or more category IDs obtained from the `category_id` field in the response of [/catalog/insight/filter/get/](33-catalog-insights.md#doc-1805640864553985). |
#| brands {+Conditional} | string[] | When `filtering` is specified, you need to provide at least one of `category_ids`, `brands`, and `availabilities`. <br><br>A list of product brand names to filter the results by. <br><br>Kích thước tối đa: 50. <br><br>Provide one or more brand names obtained from the `brands` field in the response of [/catalog/insight/filter/get/](33-catalog-insights.md#doc-1805640864553985). |
#| availabilities {+Conditional} | string[] |When `filtering` is specified, you need to provide at least one of `category_ids`, `brands`, and `availabilities`. <br><br>Product availability statuses to filter the results by. <br><br>Các giá trị enum hỗ trợ: <ul><li>`IN_STOCK`: in stock. </li><li>`AVAILABLE_FOR_ORDER`: available for order.</li><li>`PREORDER`: available for pre-order.</li><li>`OUT_OF_STOCK`: out of stock.</li><li>`DISCONTINUED`: discontinued. </li></ul><br>Provide one or more availability statuses obtained from the `availabilities` field in the response of [/catalog/insight/filter/get/](33-catalog-insights.md#doc-1805640864553985). |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/insight/product/get/?bc_id={{bc_id}}&catalog_id={{catalog_id}}' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| product_insights | object[] | The list of up to 50 trending products within the E-commerce catalog, sorted in Sắp xếp giảm dần (DESC) by popularity.  <br><br>For instance, the first item in the list is ranked 1st, indicating the most popular product, and the second item is ranked 2nd, indicating the second most popular product. |
##| product_id | string | The system-generated product ID. |
##| image_url | string | The URL for the product image. |
##| title | string | The title of the product. |
##| description | string | A short description of the product. |
##| sku_id | string | Advertiser-defined unique SKU ID for the Product. |
##| category_info | object | Information about the TikTok product category assigned to the product. |
###| category_id | string | The TikTok product category ID assigned to the product, consisting of three levels separated by the number sign (#), in the format of `"level_id_1#level_id_2#level_id_3"`.<br><br> Example: `601152#842248#601302`. |
###| level_info | object | Details of the levels that the category belongs to. |
####| level_id_1 | string | ID của danh mục sản phẩm TikTok cấp 1. |
####| level_name_1 | string | The name of the level-1 TikTok product category. |
####| level_id_2 | string | ID của danh mục sản phẩm TikTok cấp 2. |
####| level_name_2 | string | The name of the level-2 TikTok product category. |
####| level_id_3 | string | ID của danh mục sản phẩm TikTok cấp 3. |
####| level_name_3 | string | The name of the level-3 TikTok product category. |
##| brand | string | Brand name for the product. |
##| price | object | Price information. |
###| price | float | The base price of the product. |
###| currency | string | Unit of currency. <br><br>  If this field is not specified, the unit of currency for the catalog's target country will be used by default. |
###| sale_price | float | The discounted price of the product if it's on sale. |
###| sale_price_effective_date| string[] | The start and end date and time of sale. |
##| availability | string | The current availability of the product in your store.<br><br>Các giá trị enum hỗ trợ: <ul><li>`IN_STOCK`: in stock. </li><li>`AVAILABLE_FOR_ORDER`: available for order.</li><li>`PREORDER`: available for pre-order.</li><li>`OUT_OF_STOCK`: out of stock.</li><li>`DISCONTINUED`: discontinued. </li></ul> |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "product_insights": [
            {
                "availability": "OUT_OF_STOCK",
                "brand": "{{brand}}",
                "category_info": {
                    "category_id": "605248#905224#906248",
                    "level_info": {
                        "level_id_1": "605248",
                        "level_id_2": "905224",
                        "level_id_3": "906248",
                        "level_name_1": "Fashion Accessories",
                        "level_name_2": "Clothes Accessories",
                        "level_name_3": "Headwear"
                    }
                },
                "description": "{{description}}",
                "image_url": "{{image_url}}",
                "price": {
                    "currency": "USD",
                    "price": 22.99,
                    "sale_price": 17.99,
                    "sale_price_effective_date": null
                },
                "product_id": "{{product_id}}",
                "sku_id": "{{sku_id}}",
                "title": "{{title}}"
            },
            {
                "availability": "OUT_OF_STOCK",
                "brand": "{{brand}}",
                "category_info": {
                    "category_id": "601152#842376#601276",
                    "level_info": {
                        "level_id_1": "601152",
                        "level_id_2": "842376",
                        "level_id_3": "601276",
                        "level_name_1": "Womenswear & Underwear",
                        "level_name_2": "Women's Bottoms",
                        "level_name_3": "Jeans"
                    }
                },
                "description": "{{description}}",
                "image_url": "{{image_url}}",
                "price": {
                    "currency": "USD",
                    "price": 57.99,
                    "sale_price": 49.99,
                    "sale_price_effective_date": null
                },
                "product_id": "{{product_id}}",
                "sku_id": "{{sku_id}}",
                "title": "{{title}}"
            }
        ]
    }
}
```

---

<a id="doc-1805640900563969"></a>
<!-- doc_id: 1805640900563969 -->
<!-- doc_id: 1805640900563969 -->
# Get trending catalog product categories
> Đường dẫn: API Reference > Catalog Insights > Get trending catalog product categories
Sử dụng endpoint này để truy xuất the number of products in your E-commerce catalog that match the top 50 trending product categories based on user engagement on TikTok, along with the product availability percentage.

>**Note:**  
>  • Catalog Product Insights become available 24 hours after you have uploaded a minimum of 20 products to your E-commerce catalog. •  The insights are refreshed daily at around 4:00 AM UTC time.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/insight/category/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID).<br><br>To obtain the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br>The catalog needs to be an E-commerce catalog that contains at least 20 products. <br><br>To obtain the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610) and retrieve `catalog_id` values with `catalog_type` as `ECOM`. <br>To verify that the catalog contains at least 20 products, use [/catalog/overview/](25-catalog-management.md#doc-1740492470201345) and check Liệu sum of the values of the returned `approved`, `rejected`, and `processing` fields is equal to or greater than 20. |
| filtering | object | Điều kiện lọc dữ liệu. |
#| category_ids {+Conditional} | string[] | When `filtering` is specified, this field is required.  <br><br> A list of product category IDs to filter the results by.  <br><br>Kích thước tối đa: 50.  <br><br> To get filtered insights, call `/catalog/insight/filter/get/` first to obtain the top 50 trending product categories on TikTok. Then, select the desired category IDs from the `category_id` field in the response and pass them to this field. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/insight/category/get/?bc_id={{bc_id}}&catalog_id={{catalog_id}}' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| category_insights | object[] | The list of the top 50 trending product categories on TikTok, sorted in Sắp xếp giảm dần (DESC) by popularity. <br><br>For instance, the first item in the list is ranked 1st, indicating the most popular product category, and the second item is ranked 2nd, indicating the second most popular product category. |
##| category_id | string | The TikTok product category ID assigned to the product, consisting of three levels separated by the number sign (#), in the format of `"level_id_1#level_id_2#level_id_3"`. <br><br> Example: `601152#842248#601302`. |
##| level_info | object | Details of the levels that the category belongs to. |
###| level_id_1 | string | ID của danh mục sản phẩm TikTok cấp 1. |
###| level_name_1 | string | The name of the level-1 TikTok product category. |
###| level_id_2 | string | ID của danh mục sản phẩm TikTok cấp 2. |
###| level_name_3 | string | The name of the level-2 TikTok product category. |
###| level_id_3 | string | ID của danh mục sản phẩm TikTok cấp 3. |
###| level_name_3 | string | The name of the level-3 TikTok product category. |
##| total_product_count | integer | The number of products in the catalog (`catalog_id`) that match the product category (`category_id`). |
##| product_availability_rate | float | The total percentage of matching products in this category that are currently in stock in the catalog. <br><br> If the value is too low, you can use [/catalog/product/update/](28-catalog-products-p2.md#doc-1740562287852546) to update the `availability` of the relevant products to `IN_STOCK`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "category_insights": [
            {
                "category_id": "601352#900488#900872",
                "level_info": {
                    "level_id_1": "601352",
                    "level_id_2": "900488",
                    "level_id_3": "900872",
                    "level_name_1": "Shoes",
                    "level_name_2": "Women's Shoes",
                    "level_name_3": "Trainers"
                },
                "product_availability_rate": 0.6666666666666667,
                "total_product_count": 3
            },
            ...
            {
                "category_id": "605248#905608#605268",
                "level_info": {
                    "level_id_1": "605248",
                    "level_id_2": "905608",
                    "level_id_3": "605268",
                    "level_name_1": "Fashion Accessories",
                    "level_name_2": "Jewellery & Accessories",
                    "level_name_3": "Earrings"
                },
                "product_availability_rate": 0.375,
                "total_product_count": 8
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Insight Catalog**:

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

