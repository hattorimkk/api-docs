# Bộ sản phẩm Catalog

> Phân hệ: apiref:Catalog Product Sets.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Catalog Product Sets (#doc-1740132953884673)](#doc-1740132953884673)
- [2. Get product sets (#doc-1740570556295169)](#doc-1740570556295169)
- [3. Get products in a product set (#doc-1740571478441986)](#doc-1740571478441986)
- [4. Create a product set by conditions (#doc-1740572891104257)](#doc-1740572891104257)
- [5. Create a product set by file (#doc-1846770644217858)](#doc-1846770644217858)
- [6. Update a product set (#doc-1740572974725122)](#doc-1740572974725122)
- [7. Delete product sets (#doc-1740573143966722)](#doc-1740573143966722)

---

<a id="doc-1740132953884673"></a>
<!-- doc_id: 1740132953884673 -->
<!-- doc_id: 1740132953884673 -->
# Catalog Product Sets
> Đường dẫn: API Reference > Catalog Product Sets
> **Important:** By using Catalog API endpoints, you agree to the [Product Catalog Terms](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) and certify that you are abiding by the [TikTok Advertising Policies](https://ads.tiktok.com/help/article?aid=6685586866860720134). Please review these policies and ensure that the items you upload to your catalog don't breach them.

A catalog is an asset that allows you to store information about the products you want to promote on TikTok. Using a catalog is a great solution for anyone who is looking for an efficient way to create and manage ads that feature a variety of products, like an online retailer. Catalog Product Sets API enables you to manage product sets in a catalog under your Business Center.

See [Overview](../09-marketing-api/catalog.md#doc-1754263078057986) and [Guides](../09-marketing-api/catalog.md#doc-1754263100123137) to learn about the concepts and benefits of catalogs, and to find out how to create and manage catalogs.

This group consists of the following endpoints:
* [Get product sets](29-catalog-product-sets.md#doc-1740570556295169)
* [Get products in product set](29-catalog-product-sets.md#doc-1740571478441986)
* [Create a product set by conditions](29-catalog-product-sets.md#doc-1740572891104257)
* [Create a product set by file](29-catalog-product-sets.md#doc-1846770644217858)
* [Update a product set](29-catalog-product-sets.md#doc-1740572974725122)
* [Delete product sets](29-catalog-product-sets.md#doc-1740573143966722)

---

<a id="doc-1740570556295169"></a>
<!-- doc_id: 1740570556295169 -->
<!-- doc_id: 1740570556295169 -->
# Get product sets
> Đường dẫn: API Reference > Catalog Product Sets > Get product sets
Sử dụng endpoint này để lấy thông tin a list of product sets or one specified product set in a catalog under your Business Center.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). ⏎ To obtain the list of Business Centers that you can access, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id  ****(Bắt buộc)**** | string | The ID of the catalog that you want to get product sets from. ⏎ To obtain the list of catalogs that you can access, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) and set `asset_type` to `CATALOG`. |
| product_set_id | string | ID bộ sản phẩm bạn muốn lấy thông tin. ⏎ • If this field is not passed, the system will return the complete list of product sets associated with the catalog (`catalog_id`). • If this field is passed, the system will only return the specified product set. |
| return_product_count | boolean | Có thực hiện return the response parameter `product_count`. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `true`. ⏎ **Note**: For product sets with too many products, returning `product_count` might trigger timeout errors. To avoid timeout issues in such cases, set this field to `false`. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -X GET -H "Access-Token:YOUR_ACCESS_TOKEN" \
--data-urlencode "bc_id=BC_ID" \
--data-urlencode "catalog_id=CATALOG_ID" \
--data-urlencode "product_set_id=SET_ID" \

https://business-api.tiktok.com/open_api/v1.3/catalog/set/get/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The request ID. |
| data | object | The returned data. |
| ↳ list | object[] | A list of product sets. |
| ↳↳ product_count | number | Returned only when `return_product_count` is `true` or not passed in the request. ⏎ Number of products in this product set. |
| ↳↳ product_set_id | string | The product set ID. |
| ↳↳ catalog_id | string | The ID danh mục sản phẩm. |
| ↳↳ product_set_name | string | The name of the product set. |
| ↳↳ conditions | object | The filter conditions. |
| ↳↳↳ and/or | object[] | The logical Toán tử điều kiện that will be applied to multiple filter conditions. You must specify either `and` or `or`. `and` stands for the AND logical Toán tử điều kiện. `or` stands for the OR logical Toán tử điều kiện. |
| ↳↳↳↳ field | string | The field that the filter will be applied to. Để xem danh sách giá trị enum, xem [Appendix - Product Set - Filter fields](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳↳↳ operation | string | The filter Toán tử điều kiện. Để xem danh sách giá trị enum, xem [Appendix - Product Set - Operators](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳↳↳ value | string/string[] | The expected value. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "list": [
            {                
				"product_set_id": "1767",
				"product_count": 8,
                "name": "test_create",
                "catalog_id": "6873077759237687045",
                "conditions": {
                    "or": [
                        {
                            "field": "price",
                            "operation": "LT",
                            "value": "250"
                        },
                        {
                            "field": "sale_price_effective_start_date",
                            "operation": "GTE",
                            "value": "2021-03-04 12:00:00"
                        }
                    ]
                }
            }
        ]
    },
    "request_id": "2021030908581701023102608005883C"
}
```

---

<a id="doc-1740571478441986"></a>
<!-- doc_id: 1740571478441986 -->
<!-- doc_id: 1740571478441986 -->
# Get products in a product set
> Đường dẫn: API Reference > Catalog Product Sets > Get products in a product set
Sử dụng endpoint này để lấy thông tin products in a product set.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/product/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | The ID of the catalog that you want to get product sets from. |
| product_set_id  ****(Bắt buộc)**** | string | ID bộ sản phẩm bạn muốn lấy thông tin. |
| page | number | The number of the current page. The Giá trị mặc định is 1. |
| page_size | number | The page size. The default size is 20. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -X GET -H "Access-Token:YOUR_ACCESS_TOKEN" \
-H "Content-Type:application/json" \
-d '{\"bc_id\": BC_ID,\"catalog_id\": CATALOG_ID,\"product_set_id\": SET_ID},\"page\": PAGE,\"page_size\": PAGE_SIZE' \
https://business-api.tiktok.com/open_api/v1.3/catalog/set/info/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The request ID. |
| data | object | Returned data. |
| ↳ product_set_id | string | The product set ID. |
| ↳ catalog_id | string | The ID danh mục sản phẩm. |
| ↳ product_count | name | The number of products in the product set. |
| ↳ products | object[] | A list of products. |
| ↳↳ product_id | number | The product ID. |
| ↳↳ product_name | string | The product name. |
| ↳↳ sku_id | string | Returned only for E-commerce catalog products. ⏎ A unique ID for the E-commerce product. |
| ↳↳ hotel_id | string | Returned only for hotel catalog products. ⏎ A unique ID for the hotel. |
| ↳↳ flight_id | string | Returned only for flight catalog products. ⏎ A unique ID for the flight. |
| ↳↳ destination_id | string | Returned only for destination catalog products. ⏎ A unique ID for the destination. |
| ↳↳ vehicle_id | string | Returned only for products in an Auto-Inventory or Auto-Model catalog. ⏎ A unique ID for the vehicle. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "product_count": 2,
        "page_info": {
            "total_number": 2,
            "page": 1,
            "page_size": 20,
            "total_page": 1
        },
        "products": [
            {
                "sku_id": "test_2",
                "product_id": 6933990518728918789,
                "product_name": "pro_2"
            },
            {
                "sku_id": "test_1",
                "product_id": 6933990518728935173,
                "product_name": "pro_1"
            }
        ],
        "catalog_id": 6873077759237687045,
        "product_set_id": 1547
    },
    "request_id": "20210301065500010231016022235FAE"
}
```

---

<a id="doc-1740572891104257"></a>
<!-- doc_id: 1740572891104257 -->
<!-- doc_id: 1740572891104257 -->
# Create a product set by conditions
> Đường dẫn: API Reference > Catalog Product Sets > Create a product set by conditions
Sử dụng endpoint này để tạo a product set by conditions in a catalog under your Business Center.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | The ID danh mục sản phẩm. |
| product_set_name  ****(Bắt buộc)**** | string | The product set name. ⏎ Giới hạn độ dài: 128 characters. |
| conditions  ****(Bắt buộc)**** | object | The filter conditions. ⏎ **Note**: If you pass multiple conditions through this object, we recommend limiting the combined total number of values in the conditions to a maximum of 1,024. Otherwise, a timeout is likely to occur. |
| ↳ and/or  ****(Bắt buộc)**** | object[] | The logical Toán tử điều kiện that will be applied to the filter conditions. You must specify either `and` or `or`. `and` stands for the AND logical Toán tử điều kiện. `or` stands for the OR logical Toán tử điều kiện. |
| ↳↳ field ****(Bắt buộc)**** | string | The field that the filter will be applied to. Để xem danh sách giá trị enum, xem [Product set operators and fields – Filter fields](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳ operation ****(Bắt buộc)**** | string | The filter Toán tử điều kiện. Để xem danh sách giá trị enum, xem [Product set operators and fields – Operators](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳ value ****(Bắt buộc)**** | string/string[] | The expected value. ⏎ Depending on the Toán tử điều kiện you specify via `operation`, this field can be a single value or multiple values in a list. See [Product set operators and fields – Operators](../09-marketing-api/catalog.md#doc-1740673108747265) to learn about the type of value you need to specify. ⏎ **Note**: If you pass multiple values through this field, the maximum allowed number of values is 1,024. |

### Ví dụ lệnh cURL (Example)-the object Conditions
```example
// conditions
    "conditions": {
        "and": [
            {
                "field": "gender",
                "operation": "EQUAL",
                "value": "MALE"
            },
            {
                "field": "price",
                "operation": "GTE",
                "value": "50"
            },
            {
                "field": "brand",
                "operation": "I_CONTAIN",
                "value": ["TikTok", "Global App Bundle"]
            }
        ]
    }
```

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/set/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "product_set_name": "{{product_set_name}}",
    "conditions": {
        "and": [
            {
                "field": "gender",
                "operation": "EQUAL",
                "value": "MALE"
            },
            {
                "field": "price",
                "operation": "GTE",
                "value": "50"
            },
            {
                "field": "brand",
                "operation": "I_CONTAIN",
                "value": [
                    "TikTok",
                    "Global App Bundle"
                ]
            }
        ]
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The request ID. |
| data | object | Returned data. |
| ↳ product_set_id | string | The product set ID. |
| ↳ product_set_name | string | The product set name. |
| ↳ product_count | number | The number of products in the product set. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "product_set_id": "{{product_set_id}}",
        "product_set_name": "{{product_set_name}}",
        "product_count": 2
    }
}
```

---

<a id="doc-1846770644217858"></a>
<!-- doc_id: 1846770644217858 -->
<!-- doc_id: 1846770644217858 -->
# Create a product set by file
> Đường dẫn: API Reference > Catalog Product Sets > Create a product set by file
Sử dụng endpoint này để tạo an E-commerce product set by uploading a CSV file containing SKU IDs in an E-commerce catalog under your Business Center.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/upload/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `multipart/form-data`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). ⏎ To retrieve the list of Business Centers that you have access to, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id  ****(Bắt buộc)**** | string | ID danh mục sản phẩm. ⏎ To retrieve the list of E-commerce catalogs within a Business Center, use [/catalog/get/](25-catalog-management.md#doc-1740315452868610). For E-commerce catalogs, `catalog_type` will be `ECOM`. |
| product_set_name  ****(Bắt buộc)**** | string | The product set name. ⏎ Giới hạn độ dài: 28 characters. ⏎ **Note**: Duplicate product set names are not supported. To retrieve the names of existing product sets created in a catalog, use [/catalog/set/get/](29-catalog-product-sets.md#doc-1740570556295169) and check the returned `product_set_name`. |
| file  ****(Bắt buộc)**** | file | A file containing product SKU IDs. ⏎ To obtain the list of SKU IDs for products within an E-commerce catalog, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402) and check the returned `sku_id`. ⏎ Thông số khuyến nghị： • Maximum row count: 5,000. • Format：.csv only.Use [the CSV template file](https://bytedance.sg.larkoffice.com/sheets/GlkOsKz7RhRhfLtN0gblmYcjgjd) for uploading. |
| file_signature  ****(Bắt buộc)**** | string | The MD5 hash of the file that is used for server verification to confirm file integrity. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/set/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'bc_id="{{bc_id}}"' \
--form 'catalog_id="{{catalog_id}}"' \
--form 'product_set_name="{{product_set_name}}"' \
--form 'file=@"/{{file_path}}"' \
--form 'file_signature="{{file_signature}}"'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ product_set_id | string | The product set ID. |
| ↳ product_set_name | string | The product set name. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "product_set_id": "{{product_set_id}}",
        "product_set_name": "{{product_set_name}}"
    }
}
```

---

<a id="doc-1740572974725122"></a>
<!-- doc_id: 1740572974725122 -->
<!-- doc_id: 1740572974725122 -->
# Update a product set
> Đường dẫn: API Reference > Catalog Product Sets > Update a product set
Sử dụng endpoint này để cập nhật filter conditions or name of a product set. You only need to include the fields that you want to update the values for.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | The ID danh mục sản phẩm. |
| product_set_id  ****(Bắt buộc)**** | string | The product set ID. |
| product_set_name**(Điều kiện)** | string | You need to pass at least `product_set_name` or `conditions` or both. ⏎ The product set name. ⏎ Giới hạn độ dài: 128 characters. |
| conditions**(Điều kiện)** | object | You need to pass at least `product_set_name` or `conditions` or both. ⏎ The filter conditions. ⏎ **Note**: If you pass multiple conditions through this object, we recommend limiting the combined total number of values in the conditions to a maximum of 1,024. Otherwise, a timeout is likely to occur. |
| ↳ and/or**(Điều kiện)** | object[] | Bắt buộc khi `conditions` is passed. ⏎ The logical Toán tử điều kiện that will be applied to the filter conditions. You must specify either `and` or `or`. `and` stands for the AND logical Toán tử điều kiện. `or` stands for the OR logical Toán tử điều kiện. |
| ↳↳ field**(Điều kiện)** | string | Bắt buộc khi `conditions` is passed. ⏎ The field that the filter will be applied to. Để xem danh sách giá trị enum, xem [Product set operators and fields – Filter fields](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳ operation**(Điều kiện)** | string | Bắt buộc khi `conditions` is passed. ⏎ The filter Toán tử điều kiện. Để xem danh sách giá trị enum, xem [Product set operators and fields – Operators](../09-marketing-api/catalog.md#doc-1740673108747265). |
| ↳↳ value**(Điều kiện)** | string/string[] | Bắt buộc khi `conditions` is passed. ⏎ The expected value. ⏎ Depending on the Toán tử điều kiện you specify via `operation`, this field can be a single value or multiple values in a list. See [Product set operators and fields – Operators](../09-marketing-api/catalog.md#doc-1740673108747265) to learn about the type of value you need to specify. ⏎ **Note**: If you pass multiple values through this field, the maximum allowed number of values is 1,024. |

### Ví dụ lệnh cURL (Example)-the object Conditions
```example
// conditions
    "conditions": {
        "and": [
            {
                "field": "gender",
                "operation": "EQUAL",
                "value": "MALE"
            },
            {
                "field": "price",
                "operation": "GTE",
                "value": 50
            },
            {
                "field": "brand",
                "operation": "I_CONTAIN",
                "value": ["TikTok", "xxxxx"]
            }
        ]
    }
```

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -X POST -H "Access-Token:YOUR_ACCESS_TOKEN" \
-H "Content-Type:application/json" \
-d '{\"bc_id\": BC_ID,\"catalog_id\": CATALOG_ID,\"name\": NAME},\"conditions\": [CONDITIONS]}' \
https://business-api.tiktok.com/open_api/v1.3/catalog/set/update/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The request ID. |
| data | object | Returned data. |
| ↳ product_set_id | string | The product set ID. |
| ↳ product_set_name | string | The product set name. |
| ↳ product_count | number | The number of products in the product set. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "count": 20,
        "product_set_id": "1566",
        "name": "test_create"
    },
    "request_id": "20210228131918010231010121650793"
}
```

---

<a id="doc-1740573143966722"></a>
<!-- doc_id: 1740573143966722 -->
<!-- doc_id: 1740573143966722 -->
# Delete product sets
> Đường dẫn: API Reference > Catalog Product Sets > Delete product sets
Sử dụng endpoint này để xóa product sets in a catalog under a Business Center.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/set/delete/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"` . |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | The product ID danh mục sản phẩm. |
| product_set_ids  ****(Bắt buộc)**** | string[] | The IDs of the product sets that you want to delete. You can include 1 to 10 IDs in the list. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -X POST -H "Access-Token:YOUR_ACCESS_TOKEN" \
-H "Content-Type:application/json" \
-d '{\"bc_id\": BC_ID,\"catalog_id\": CATALOG_ID,\"product_set_ids\": SET_IDS}' \
https://business-api.tiktok.com/open_api/v1.3/catalog/set/delete/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The request ID. |
| data | object | The returned data. |
| ↳ product_set_ids | string[] | The IDs of the product sets that have been deleted. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "product_set_ids": [
            "1865",
            "1863",
            "1791"
        ]
    },
    "request_id": "2021031410042301023101010646846F"
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Bộ sản phẩm Catalog**:

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

