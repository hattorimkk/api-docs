# Quản lý Catalog (Catalog Management)

Nhóm API Quản lý Catalog (Catalog Management) cung cấp bộ công cụ toàn diện giúp doanh nghiệp khởi tạo, cấu hình, theo dõi và quản lý vòng đời của các danh mục sản phẩm (Catalog) thuộc Business Center trên TikTok. Thông qua nhóm API này, bạn có thể thiết lập các loại hình danh mục chuyên biệt (Thương mại điện tử, Khách sạn, Chuyến bay, Điểm đến, Phim truyền hình ngắn tập, Ô tô hoặc Bán hàng đa kênh Online-to-Offline), quản lý danh sách từ khóa biến số mẫu quảng cáo (Lexicon), phân bổ quyền truy cập và kiểm tra tình trạng kiểm duyệt sản phẩm. Tài liệu này cung cấp chi tiết kỹ thuật cho toàn bộ các endpoint thuộc nhóm Quản lý Catalog trong phiên bản API v1.3.

## Mục lục các endpoint

| Endpoint | Phương thức | Mục đích |
|---|---|---|
| [/catalog/create/](25-catalog-management.md#doc-1740306481704961) | `POST` | Khởi tạo danh mục sản phẩm mới kèm cấu hình quốc gia và đơn vị tiền tệ |
| [/catalog/update/](25-catalog-management.md#doc-1740306544966657) | `POST` | Chỉnh sửa tên hiển thị của danh mục sản phẩm |
| [/catalog/delete/](25-catalog-management.md#doc-1740310064588801) | `POST` | Xóa danh mục sản phẩm khỏi Business Center |
| [/catalog/get/](25-catalog-management.md#doc-1740315452868610) | `GET` | Lấy danh sách hoặc thông tin chi tiết các danh mục thuộc Business Center |
| [/catalog/lexicon/get/](25-catalog-management.md#doc-1740488375815169) | `GET` | Lấy danh sách từ vựng biến số (Lexicon) sử dụng trong mẫu quảng cáo của Catalog |
| [/catalog/capitalize/](25-catalog-management.md#doc-1740490222539778) | `POST` | Di chuyển danh mục sản phẩm từ tài khoản quảng cáo sang Business Center |
| [/catalog/available_country/get/](25-catalog-management.md#doc-1740491257516034) | `GET` | Lấy danh sách các quốc gia/khu vực mà quảng cáo của Catalog có thể phân phối tới |
| [/catalog/location_currency/get/](25-catalog-management.md#doc-1740491571747841) | `GET` | Lấy danh sách các địa điểm hỗ trợ và tiền tệ tương ứng cho Catalog API |
| [/catalog/overview/](25-catalog-management.md#doc-1740492470201345) | `GET` | Lấy thống kê tổng quan số lượng sản phẩm theo từng trạng thái kiểm duyệt |

---

## Tổng quan Quản lý Catalog (`Catalog Management`)
<a id="doc-1740132866693122"></a>
<!-- doc_id: 1740132866693122 -->

> Đường dẫn: API Reference > Catalog Management

> [!IMPORTANT]
> Bằng việc sử dụng các endpoint của Catalog API, bạn đồng ý với [Điều khoản Danh mục sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và xác nhận tuân thủ [Chính sách quảng cáo của TikTok (TikTok Advertising Policies)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem xét kỹ các chính sách này và đảm bảo rằng các sản phẩm tải lên danh mục không vi phạm quy định.

Danh mục sản phẩm (Catalog) là tài sản lưu trữ thông tin về các mặt hàng bạn muốn quảng bá trên TikTok. Sử dụng Catalog là giải pháp lý tưởng cho các nhà bán lẻ trực tuyến muốn tạo và quản lý quảng cáo cho nhiều mặt hàng cùng lúc một cách hiệu quả:
- Xem thêm [Tổng quan (Overview)](../09-marketing-api/catalog.md#doc-1754263078057986) và [Hướng dẫn (Guides)](../09-marketing-api/catalog.md#doc-1754263100123137) để tìm hiểu các khái niệm, lợi ích và cách tạo, quản lý Catalog.

Nhóm tài liệu này bao gồm các endpoint sau:
* [Tạo Catalog (Create a catalog)](25-catalog-management.md#doc-1740306481704961)
* [Cập nhật tên Catalog (Update the name of a catalog)](25-catalog-management.md#doc-1740306544966657)
* [Xóa Catalog (Delete a catalog)](25-catalog-management.md#doc-1740310064588801)
* [Lấy danh sách Catalog (Get catalogs)](25-catalog-management.md#doc-1740315452868610)
* [Lấy danh sách từ vựng Catalog (Get the lexicon list for a catalog)](25-catalog-management.md#doc-1740488375815169)
* [Chuyển Catalog sang Business Center (Migrate a catalog to a BC)](25-catalog-management.md#doc-1740490222539778)
* [Lấy danh sách khu vực khả dụng (Get available regions)](25-catalog-management.md#doc-1740491257516034)
* [Lấy danh sách địa điểm và tiền tệ (Get locations and currencies)](25-catalog-management.md#doc-1740491571747841)
* [Lấy tổng quan Catalog (Get the overview of a catalog)](25-catalog-management.md#doc-1740492470201345)

---

## Tạo Catalog (`Create a catalog`)
<a id="doc-1740306481704961"></a>
<!-- doc_id: 1740306481704961 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/create/`

**Mục đích**: Khởi tạo và thiết lập một danh mục sản phẩm mới trong Business Center bằng cách chỉ định tên, loại danh mục, khu vực mục tiêu chính và đơn vị tiền tệ.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center sở hữu Catalog. |
| `name` | string | Bắt buộc | Tên danh mục sản phẩm. Giới hạn độ dài: 128 ký tự. |
| `catalog_type` | string | Bắt buộc | Loại danh mục sản phẩm.<br>Giá trị enum:<br>• `ECOM`: Danh mục thương mại điện tử (E-commerce).<br>• `HOTEL`: Danh mục khách sạn.<br>• `FLIGHT`: Danh mục chuyến bay.<br>• `DESTINATION`: Danh mục điểm đến du lịch.<br>• `ENTERTAINMENT`: Danh mục giải trí (tính năng chỉ dành cho danh sách cho phép allowlist, hiện đang thử nghiệm Alpha).<br>• `AUTO_VEHICLE`: Danh mục kho xe ô tô (Auto-Inventory). Xem bảng mã khu vực và tiền tệ hỗ trợ bên dưới.<br>• `AUTO_MODEL`: Danh mục mẫu xe ô tô (Auto-Model). Xem bảng mã khu vực và tiền tệ hỗ trợ bên dưới.<br>• `MINI_SERIES`: Danh mục phim truyền hình ngắn tập (tính năng đang thử nghiệm có giới hạn).<br>• `GENERIC`: Danh mục chung.<br>• `ONLINE_TO_OFFLINE`: Danh mục bán hàng trực tuyến sang ngoại tuyến (O2O). Xem bảng mã khu vực và tiền tệ hỗ trợ bên dưới. |
| `catalog_conf` | object | Bắt buộc | Thông tin cấu hình chi tiết của Catalog. |
| ↳ `region_code` | string | Bắt buộc | Mã quốc gia/khu vực mục tiêu chính (ví dụ: `US`, `VN`). Lấy danh sách qua [/catalog/available_country/get/](25-catalog-management.md#doc-1740491257516034). Xem đối chiếu tại [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010).<br>**Lưu ý**: Sau khi thiết lập, trường này **không thể chỉnh sửa**. |
| ↳ `currency` | string | Bắt buộc | Đơn vị tiền tệ chính của khu vực mục tiêu (ví dụ: `USD`, `VND`). Xem chi tiết tại [Budget verification ratio and precision of each currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433).<br>**Lưu ý**: Sau khi thiết lập, trường này **không thể chỉnh sửa**. |
| ↳ `channel` | string | Không bắt buộc | Kênh tạo danh mục. Enum: `PARTNER` (Đối tác), `CLIENT` (Nhà quảng cáo trực tiếp). Không thể sửa sau khi đặt. |
| ↳ `additional_config_list` | object[] | Không bắt buộc | Chỉ hợp lệ khi `catalog_type` là `MINI_SERIES`. Danh sách các khu vực mục tiêu bổ sung. Không giới hạn kích thước tối đa. Không thể sửa sau khi đặt. |
| ↳↳ `region_code` | string | Điều kiện | Bắt buộc khi có truyền `additional_config_list`. Mã vùng bổ sung (ví dụ: `GB`). Không được trùng lặp. |
| ↳↳ `currency` | string | Điều kiện | Bắt buộc khi có truyền `additional_config_list`. Tiền tệ tương ứng với khu vực bổ sung (ví dụ: `GBP`). Mỗi khu vực chỉ được chỉ định 1 loại tiền tệ. |

### Danh sách mã khu vực và tiền tệ cho Catalog Auto-Inventory và Auto-Model

Bảng dưới đây liệt kê các giá trị `region_code` và đơn vị `currency` tương ứng được hỗ trợ cho loại danh mục Auto-Inventory và Auto-Model:

| Region | `region_code` value | `currency` value |
|---|---|---|
| Argentina | `AR` | `ARS` |
| Australia | `AU` | `AUD` |
| Austria | `AT` | `EUR` |
| Azerbaijan | `AZ` | `AZN` |
| Bahrain | `BH` | `BHD` |
| Bangladesh | `BD` | `BDT` |
| Belarus | `BY` | `BYN` |
| Belgium | `BE` | `EUR` |
| Brazil | `BR` | `BRL` |
| Cambodia | `KH` | `KHR` |
| Canada | `CA` | `CAD` |
| Chile | `CL` | `CLP` |
| Colombia | `CO` | `COP` |
| Czechia | `CZ` | `CZK` |
| Denmark | `DK` | `DKK` |
| Ecuador | `EC` | `USD` |
| Egypt | `EG` | `EGP` |
| Finland | `FI` | `EUR` |
| France | `FR` | `EUR` |
| Germany | `DE` | `EUR` |
| Greece | `GR` | `EUR` |
| Hungary | `HU` | `HUF` |
| Indonesia | `ID` | `IDR` |
| Iraq | `IQ` | `IQD` |
| Ireland | `IE` | `EUR` |
| Israel | `IL` | `ILS` |
| Italy | `IT` | `EUR` |
| Japan | `JP` | `JPY` |
| Kazakhstan | `KZ` | `KZT` |
| Korea | `KR` | `KRW` |
| Kuwait | `KW` | `KWD` |
| Malaysia | `MY` | `MYR` |
| Mexico | `MX` | `MXN` |
| Morocco | `MA` | `MAD` |
| Netherlands | `NL` | `EUR` |
| New Zealand | `NZ` | `NZD` |
| Norway | `NO` | `NOK` |
| Oman | `OM` | `OMR` |
| Pakistan | `PK` | `PKR` |
| Peru | `PE` | `PEN` |
| Philippines | `PH` | `PHP` |
| Poland | `PL` | `PLN` |
| Portugal | `PT` | `EUR` |
| Qatar | `QA` | `QAR` |
| Romania | `RO` | `RON` |
| Russia | `RU` | `RUB` |
| Saudi Arabia | `SA` | `SAR` |
| Serbia | `RS` | `RSD` |
| Singapore | `SG` | `SGD` |
| South Africa | `ZA` | `ZAR` |
| Spain | `ES` | `EUR` |
| Sweden | `SE` | `SEK` |
| Switzerland | `CH` | `CHF` |
| Taiwan, China | `TW` | `TWD` |
| Thailand | `TH` | `THB` |
| Turkey | `TR` | `TRY` |
| Ukraine | `UA` | `UAH` |
| United Arab Emirates | `AE` | `AED` |
| United Kingdom | `GB` | `GBP` |
| United States | `US` | `USD` |
| Uruguay | `UY` | `UYU` |
| Vietnam | `VN` | `VND` |

### Danh sách mã khu vực và tiền tệ cho Catalog Online-to-Offline

| Region | `region_code` value | `currency` value |
|---|---|---|
| Indonesia | `ID` | `IDR` |
| Malaysia | `MY` | `MYR` |
| Thailand | `TH` | `THB` |
| Vietnam | `VN` | `VND` |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách mã lỗi xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `catalog_id` | string | ID của danh mục sản phẩm vừa được khởi tạo thành công. |

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "name": "Ecom_Fashion_Catalog_VN",
    "catalog_type": "ECOM",
    "catalog_conf": {
        "region_code": "VN",
        "currency": "VND"
    }
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7100000000000000001",
    "name": "Ecom_Fashion_Catalog_VN",
    "catalog_type": "ECOM",
    "catalog_conf": {
        "region_code": "VN",
        "currency": "VND"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082101",
  "data": {
    "catalog_id": "7200000000000000001"
  }
}
```


---

## Cập nhật tên Catalog (`Update the name of a catalog`)
<a id="doc-1740306544966657"></a>
<!-- doc_id: 1740306544966657 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/update/`

**Mục đích**: Thay đổi tên hiển thị của một danh mục sản phẩm (Catalog) hiện có trong Business Center.

> [!NOTE]
> Danh mục bắt buộc phải thuộc quyền quản lý của một Business Center. Nếu danh mục hiện vẫn thuộc quyền quản lý của tài khoản quảng cáo (ad account), bạn phải di chuyển danh mục sang Business Center trước thông qua endpoint [/catalog/capitalize/](25-catalog-management.md#doc-1740490222539778).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center quản lý Catalog. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `name` | string | Bắt buộc | Tên mới cho danh mục sản phẩm. Giới hạn độ dài tối đa 128 ký tự. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách đầy đủ xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `catalog_id` | string | ID của danh mục sản phẩm vừa được cập nhật. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/update/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "name": "Ecom_Fashion_Catalog_VN_Updated"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082102",
  "data": {
    "catalog_id": "7200000000000000001"
  }
}
```

---

## Xóa Catalog (`Delete a catalog`)
<a id="doc-1740310064588801"></a>
<!-- doc_id: 1740310064588801 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/delete/`

**Mục đích**: Xóa vĩnh viễn một danh mục sản phẩm hiện có khỏi Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center mà Catalog trực thuộc. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm cần xóa. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `catalog_id` | string | ID của danh mục sản phẩm đã bị xóa. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/delete/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082103",
  "data": {
    "catalog_id": "7200000000000000001"
  }
}
```

---

## Lấy danh sách Catalog (`Get catalogs`)
<a id="doc-1740315452868610"></a>
<!-- doc_id: 1740315452868610 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/get/`

**Mục đích**: Lấy thông tin chi tiết về một danh mục cụ thể hoặc danh sách tất cả các danh mục thuộc về một Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Không bắt buộc | ID danh mục sản phẩm. Nếu không chỉ định, hệ thống sẽ trả về tất cả các danh mục thuộc Business Center. |
| `page` | number | Không bắt buộc | Số trang hiện tại. Giá trị mặc định: `1`. Khoảng giá trị: `>= 1`. |
| `page_size` | number | Không bắt buộc | Số lượng bản ghi trên một trang. Giá trị mặc định: `10`. Khoảng giá trị: `1-1000`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi trên một trang. |
| ↳↳ `total_number` | number | Tổng số danh mục tìm thấy. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |
| ↳ `list` | object[] | Danh sách các danh mục sản phẩm. |
| ↳↳ `catalog_id` | string | ID danh mục sản phẩm. |
| ↳↳ `catalog_name` | string | Tên danh mục sản phẩm. |
| ↳↳ `catalog_type` | string | Loại danh mục (`ECOM`, `HOTEL`, `FLIGHT`, `DESTINATION`, `ENTERTAINMENT`, `AUTO_VEHICLE`, `AUTO_MODEL`, `MINI_SERIES`, `GENERIC`, `ONLINE_TO_OFFLINE`). |
| ↳↳ `ad_creation_eligible` | string | Đủ điều kiện tạo quảng cáo hay không (`AVAILABLE`: đủ điều kiện khi chứa số sản phẩm tối thiểu yêu cầu; `NOT_AVAILABLE`: không thể dùng cho quảng cáo). |
| ↳↳ `create_time` | string | Thời gian tạo danh mục. |
| ↳↳ `update_time` | string | Thời gian cập nhật danh mục gần nhất. |
| ↳↳ `bc_info` | object | Thông tin Business Center sở hữu. |
| ↳↳↳ `bc_id` | string | ID Business Center. |
| ↳↳↳ `bc_name` | string | Tên Business Center. |
| ↳↳↳ `picture_url` | string | URL ảnh đại diện của Business Center. |
| ↳↳ `catalog_conf` | object | Thông tin cấu hình chi tiết của Catalog. |
| ↳↳↳ `country` | string | Mã vùng quốc gia mục tiêu chính. |
| ↳↳↳ `currency` | string | Đơn vị tiền tệ chính. |
| ↳↳↳ `channel` | string | Kênh tạo danh mục (`PARTNER` hoặc `CLIENT`). |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=10'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082104",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    },
    "list": [
      {
        "catalog_id": "7200000000000000001",
        "catalog_name": "Ecom_Fashion_Catalog_VN",
        "catalog_type": "ECOM",
        "ad_creation_eligible": "AVAILABLE",
        "create_time": "2023-10-23 10:00:00",
        "update_time": "2023-10-23 11:00:00",
        "bc_info": {
          "bc_id": "7100000000000000001",
          "bc_name": "Global_Agency_BC",
          "picture_url": ""
        },
        "catalog_conf": {
          "country": "VN",
          "currency": "VND",
          "channel": "CLIENT"
        }
      }
    ]
  }
}
```

---

## Lấy danh sách từ vựng Catalog (`Get the lexicon list for a catalog`)
<a id="doc-1740488375815169"></a>
<!-- doc_id: 1740488375815169 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/lexicon/get/`

**Mục đích**: Lấy danh sách các biến từ vựng (Lexicon) của Catalog. Từ vựng là danh sách các biến số (chẳng hạn như tên nhãn hiệu, mô tả, giá tiền) mà bạn có thể chèn động vào nội dung văn bản quảng cáo khi quảng bá sản phẩm từ Catalog.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách các biến từ vựng của Catalog. |
| ↳↳ `lexicon_id` | string | ID từ vựng. |
| ↳↳ `catalog_id` | string | ID Catalog. |
| ↳↳ `name` | string | Tên biến từ vựng (ví dụ: `brand`, `description`). |
| ↳↳ `type` | string | Loại từ vựng (ví dụ: `META`). |
| ↳↳ `metadata` | string | Trường siêu dữ liệu tương ứng (ví dụ: `brand.brandName`, `description`). |
| ↳↳ `default_value` | string | Từ mặc định thay thế nếu trường dữ liệu bị trống. |
| ↳↳ `update_time` | string | Thời gian cập nhật từ vựng. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/lexicon/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001' \
--data-urlencode 'catalog_id=7200000000000000001'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"
CATALOG_ID = "7200000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/lexicon/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "catalog_id": CATALOG_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082105",
  "data": {
    "list": [
      {
        "lexicon_id": "11375",
        "catalog_id": "7200000000000000001",
        "name": "brand",
        "type": "META",
        "metadata": "brand.brandName",
        "default_value": "",
        "update_time": "2023-10-23 10:00:00"
      },
      {
        "lexicon_id": "11382",
        "catalog_id": "7200000000000000001",
        "name": "description",
        "type": "META",
        "metadata": "description",
        "default_value": "",
        "update_time": "2023-10-23 10:00:00"
      }
    ]
  }
}
```


---

## Chuyển Catalog sang Business Center (`Migrate a catalog to a BC`)
<a id="doc-1740490222539778"></a>
<!-- doc_id: 1740490222539778 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/capitalize/`

**Mục đích**: Di chuyển một danh mục sản phẩm (Catalog) đang nằm dưới quyền quản lý của tài khoản quảng cáo (ad account) sang trực thuộc quản lý của Business Center.

> [!NOTE]
> Để có thể di chuyển Catalog sang Business Center, bạn phải đáp ứng đồng thời hai điều kiện sau:
> - Bạn là chủ sở hữu (Owner) của tài khoản quảng cáo chứa Catalog đó.
> - Bạn là Quản trị viên (Admin) của Business Center đích. Nếu chưa có Business Center, hãy tạo mới trong TikTok Ads Manager theo hướng dẫn tại [Cách tạo Business Center](https://ads.tiktok.com/help/article?aid=12789).
> 
> Nếu không thỏa mãn một trong hai điều kiện trên, request sẽ báo lỗi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID của tài khoản quảng cáo đang sở hữu Catalog. |
| `bc_id` | string | Bắt buộc | ID của Business Center đích mà bạn muốn chuyển Catalog sang. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm cần di chuyển. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/capitalize/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082106",
  "data": {}
}
```

---

## Lấy danh sách khu vực khả dụng (`Get available regions`)
<a id="doc-1740491257516034"></a>
<!-- doc_id: 1740491257516034 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/available_country/get/`

**Mục đích**: Truy vấn danh sách các quốc gia và khu vực mà quảng cáo cho một danh mục sản phẩm có thể phân phối tới.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `region_codes` | string[] | Danh sách các mã đại diện cho quốc gia hoặc khu vực mà quảng cáo của Catalog có thể hiển thị tới. Xem bảng đối chiếu tên khu vực tại [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/available_country/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/available_country/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"bc_id": BC_ID}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082107",
  "data": {
    "region_codes": [
      "VN",
      "US",
      "TH",
      "SG",
      "MY",
      "ID"
    ]
  }
}
```

---

## Lấy danh sách địa điểm và tiền tệ (`Get locations and currencies`)
<a id="doc-1740491571747841"></a>
<!-- doc_id: 1740491571747841 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/location_currency/get/`

**Mục đích**: Lấy danh sách toàn bộ các địa điểm (mã viết tắt quốc gia hoặc khu vực) được hỗ trợ bởi Catalog Management API và các đơn vị tiền tệ tương ứng cho từng địa điểm.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
Endpoint này không yêu cầu tham số query string bắt buộc nào khác ngoài header xác thực.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách các địa điểm và đơn vị tiền tệ được hỗ trợ. |
| ↳↳ `location` | string | Mã quốc gia hoặc khu vực (ví dụ: `"VN"`, `"DE"`, `"US"`). Xem [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳ `currency` | string[] | Danh sách các mã tiền tệ được hỗ trợ cho địa điểm đó (ví dụ: `["VND"]`, `["EUR"]`). Xem [Appendix - Currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/location_currency/get/' \
--header 'Access-Token: your_access_token_here'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/location_currency/get/"
headers = {"Access-Token": ACCESS_TOKEN}

response = requests.get(url, headers=headers)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082108",
  "data": {
    "list": [
      {
        "location": "VN",
        "currency": [
          "VND"
        ]
      },
      {
        "location": "US",
        "currency": [
          "USD"
        ]
      },
      {
        "location": "DE",
        "currency": [
          "EUR"
        ]
      }
    ]
  }
}
```

---

## Lấy thông tin tổng quan của Catalog (`Get the overview of a catalog`)
<a id="doc-1740492470201345"></a>
<!-- doc_id: 1740492470201345 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/overview/`

**Mục đích**: Lấy số lượng sản phẩm trong một danh mục theo các trạng thái kiểm duyệt khác nhau (đã duyệt `approved`, bị từ chối `rejected`, và đang chờ xử lý `processing`), bao gồm cả sản phẩm liên kết với TikTok Shopping.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách mã lỗi xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `approved` | number | Số lượng sản phẩm đã được phê duyệt trong danh mục. |
| ↳ `rejected` | number | Số lượng sản phẩm bị từ chối trong danh mục. |
| ↳ `processing` | number | Số lượng sản phẩm đang chờ xử lý kiểm duyệt trong danh mục. |
| ↳ `organic_approved` | number | Số lượng sản phẩm đã duyệt liên kết với TikTok Shopping. |
| ↳ `organic_rejected` | number | Số lượng sản phẩm bị từ chối liên kết với TikTok Shopping. |
| ↳ `organic_processing` | number | Số lượng sản phẩm đang chờ xử lý liên kết với TikTok Shopping. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/overview/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001' \
--data-urlencode 'catalog_id=7200000000000000001'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"
CATALOG_ID = "7200000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/overview/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "catalog_id": CATALOG_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082109",
  "data": {
    "approved": 1250,
    "rejected": 15,
    "processing": 35,
    "organic_approved": 850,
    "organic_rejected": 5,
    "organic_processing": 10
  }
}
```
