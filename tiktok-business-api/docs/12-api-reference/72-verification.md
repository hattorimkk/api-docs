# Xác minh (Verification)

> Phân hệ: apiref:Verification.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Verification (#doc-1870687451913217)](#doc-1870687451913217)
- [2. Get available verification document types for a region (#doc-1870687810081794)](#doc-1870687810081794)
- [3. Upload verification documents (#doc-1870687812502530)](#doc-1870687812502530)
- [4. Submit a verification request for your account (#doc-1870687936881281)](#doc-1870687936881281)
- [5. Check the verification status of your account (#doc-1870687815670786)](#doc-1870687815670786)

---

<a id="doc-1870687451913217"></a>
<!-- doc_id: 1870687451913217 -->
<!-- doc_id: 1870687451913217 -->
# Verification
> Đường dẫn: API Reference > Verification
When you create a Business Center or ad account on TikTok, you'll be asked to verify your business information. This process ensures a secure ecosystem by authenticating the identities of all advertisers and businesses operating on the platform. Verification API enables you to upload required verification documents and complete either business or personal identity verification for your accounts.

For step-by-step instructions on the verification workflow, see [Verify your Business Center account or ad account on TikTok](../09-marketing-api/business-center.md#doc-1870688178806290).

This group consists of the following endpoints:
- [Get available verification document types for a region](72-verification.md#doc-1870687810081794)
- [Upload verification documents](72-verification.md#doc-1870687812502530)
- [Submit a verification request for your account](72-verification.md#doc-1870687936881281)
- [Check the verification status of your account](72-verification.md#doc-1870687815670786)

---

<a id="doc-1870687810081794"></a>
<!-- doc_id: 1870687810081794 -->
<!-- doc_id: 1870687810081794 -->
# Get available verification document types for a region
> Đường dẫn: API Reference > Verification > Get available verification document types for a region
Sử dụng endpoint này để truy xuất a list of supported verification document types for a specific country or region.

Once you identify the appropriate business or personal identification documents required for your Business Center or ad account, proceed to upload them using [/account/verification/upload/](72-verification.md#doc-1870687812502530).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/account/verification/filetype/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| business_type  ****(Bắt buộc)**** | string | The type of verification you want to perform. ⏎ Các giá trị enum hỗ trợ: • `BUSINESS`: business verification. • `INDIVIDUAL`: individual identity verification. |
| region_iso_code  ****(Bắt buộc)**** | string | The country or region code for your business (Business Center account or ad account), in ISO 3166 format. ⏎ Example: `US`. ⏎ • To retrieve the country or region code of your Business Center account, use [/bc/get/](12-bc-management.md#doc-1737115687501826) and check the returned `registered_area` parameter. • To retrieve the country or region code of your ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `country` parameter. |

### Ví dụ lệnh cURL (Example)
#### For business verification
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/account/verification/filetype/?business_type=BUSINESS&region_iso_code=US' \
--header 'Access-Token: {{Access-Token}}'
```

#### For individual identity verification
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/account/verification/filetype/?business_type=INDIVIDUAL&region_iso_code=US' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ file_types | object[] | A list of verification document types you can upload for the specified country or region (`region_iso_code`). |
| ↳↳ file_type_name | string | The name of the business verification document or personal identification document. • If you set `business_type` to `BUSINESS` in the request, this field represents the business verification document name. • If you set `business_type` to `INDIVIDUAL` in the request, this field represents the personal identification document name. |
| ↳↳ file_type_code | string | The code of the business verification document or personal identification document. • If you set `business_type` to `BUSINESS` in the request, this field represents the business verification document code. • If you set `business_type` to `INDIVIDUAL` in the request, this field represents the personal identification document code. |

### Ví dụ lệnh cURL (Example)
#### For business verification
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "file_types": [
            {
                "file_type_code": "127724548",
                "file_type_name": "Documents issued by the IRS (Internal Revenue Service) showing the Employer Identification Number (EIN)"
            }
        ]
    }
}
```

#### For individual identity verification
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "file_types": [
            {
                "file_type_code": "5",
                "file_type_name": "Passport"
            },
            {
                "file_type_code": "6",
                "file_type_name": "Driver's License"
            },
            {
                "file_type_code": "131104004",
                "file_type_name": "Permanent Resident Card (Green Card)"
            },
            {
                "file_type_code": "131104260",
                "file_type_name": "Passport Card"
            },
            {
                "file_type_code": "131104516",
                "file_type_name": "State-issued Non-Driver ID"
            }
        ]
    }
}
```

---

<a id="doc-1870687812502530"></a>
<!-- doc_id: 1870687812502530 -->
<!-- doc_id: 1870687812502530 -->
# Upload verification documents
> Đường dẫn: API Reference > Verification > Upload verification documents
Sử dụng endpoint này để tải lên your verification documents.

After successfully uploading your documents, call [/account/verification/submit/](72-verification.md#doc-1870687936881281) to officially submit your account verification request.

## Before you begin
- Confirm the supported business or personal identification document types for your account by calling [/account/verification/filetype/](72-verification.md#doc-1870687810081794).
- Familiarize yourself with common pitfalls by reviewing the [List of common rejection reasons and suggestions for verification failures](https://ads.tiktok.com/help/article/list-of-common-rejection-reasons-and-suggestions-for-verification-failures).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/account/verification/upload/

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `multipart/form-data`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| image_file1  ****(Bắt buộc)**** | file | A verification document. ⏎ You can specify either a business verification document or a personal identification document. ⏎ For a personal identification verification request which usually requires two images (front and back), you can provide the front image via `image_file1` and the back image via `image_file2`. ⏎ File size: within 10 MB. ⏎ Supported formats: JPEG, PNG, and JPG. |
| image_file2 | file | An additional verification document. ⏎ You can specify either a business verification document or a personal identification document. ⏎ For a personal identification verification request which usually requires two images (front and back), you can provide the front image via `image_file1` and the back image via `image_file2`. ⏎ File size: within 10 MB. ⏎ Supported formats: JPEG, PNG, and JPG. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/account/verification/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'image_file1=@"{{image_file1}}"'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ qualification_image_ids | string[] | A list of qualification image IDs. ⏎ The number of IDs can be 1 or 2, depending on the total number of files you uploaded. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "qualification_image_ids": [
            "{{qualification_image_id}}"
        ]
    }
}
```

---

<a id="doc-1870687936881281"></a>
<!-- doc_id: 1870687936881281 -->
<!-- doc_id: 1870687936881281 -->
# Submit a verification request for your account
> Đường dẫn: API Reference > Verification > Submit a verification request for your account
Use this endpoint to submit a verification request for your Business Center account or ad account.

After you have submitted a verification request, you can monitor your approval progress using [/account/verification/status/](72-verification.md#doc-1870687815670786).

## Before you begin
Ensure you have already uploaded your verification documents via [/account/verification/upload/](72-verification.md#doc-1870687812502530) and have your `qualification_image_ids` ready.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/account/verification/submit/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id **(Điều kiện)** | string | Phải chỉ định một trong hai trường `advertiser_id` hoặc `bc_id`. ⏎ The ID of the ad account that you want to submit a verification request for. • If you are submitting your own verification document, you need to hold admin or Toán tử điều kiện access to the ad account. You can verify this access by using [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401), passing `ADVERTISER` as the `asset_type`, and ensuring the `advertiser_role` returns `ADMIN` or `Toán tử điều kiện`. • If you are reusing a verification document from others, you need to have the proper permissions: • To reuse a verification document from another ad account, you need to have admin or Toán tử điều kiện access to the ad account. Verify this via [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) (pass `ADVERTISER` as `asset_type` and ensure `advertiser_role` is `ADMIN` or `Toán tử điều kiện`). • To reuse a verification document from another Business Center account, you need to have admin access to the Business Center account. Verify this via [/bc/get/](12-bc-management.md#doc-1737115687501826) and ensure the `user_role` returns `ADMIN`. |
| bc_id **(Điều kiện)** | string | Phải chỉ định một trong hai trường `advertiser_id` hoặc `bc_id`. ⏎ The ID of the Business Center account that you want to submit a verification request for. ⏎ You need to have admin access to the Business Center account. ⏎ If you want to a verification document from another Business Center account, you need to have admin access to the Business Center account. Verify this via [/bc/get/](12-bc-management.md#doc-1737115687501826) and ensure the `user_role` returns `ADMIN`. |
| business_form **(Điều kiện)** | object | Either `business_form` or `individual_form` has to be set. ⏎ Details of your business verification information. ⏎ Specify this field if you want to submit a business verification request. |
| ↳ company_name **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The business name. ⏎ The business name you specify here must exactly match the name on your verification documents. You cannot change your business name after the verification is complete. ⏎ Giới hạn độ dài: 128 characters. |
| ↳ website_url **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The URL of the company website. ⏎ Giới hạn độ dài: 512 characters. |
| ↳ industry_code **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The industry category that your business belongs to. ⏎ Các giá trị enum hỗ trợ: • `NOT_APPLICABLE`: Not applicable. • `ALCOHOL`: Alcohol. • `OTC`: OTC. • `DATING_APP`: Dating app. • `FINANCIAL_SERVICES`: Financial services. |
| ↳ region_iso_code **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The country or region code for your business (Business Center account or ad account), in ISO 3166 format. ⏎ Example: `US`. ⏎ • To retrieve the country or region code of your Business Center account, use [/bc/get/](12-bc-management.md#doc-1737115687501826) and check the returned `registered_area` parameter. • To retrieve the country or region code of your ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `country` parameter. |
| ↳ file_type_code **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The code of the verification document. ⏎ To obtain the code of a verification document available for your business, use [/account/verification/filetype/](72-verification.md#doc-1870687810081794). |
| ↳ license_no **(Điều kiện)** | string | Bắt buộc khi `business_form` is specified. ⏎ The certificate number of your verification document. ⏎ Make sure the number you specify here is the same as the number on the document. It can’t be changed after submission. ⏎ Giới hạn độ dài: 128 characters. |
| ↳ qualification_image_ids **(Điều kiện)** | string[] | Bắt buộc khi `business_form` is specified. ⏎ A list of qualification image IDs for business verification documents. ⏎ You need to specify exactly one ID. ⏎ To obtain the qualification image ID of a business verification document, use [/account/verification/upload/](72-verification.md#doc-1870687812502530). |
| individual_form **(Điều kiện)** | object | Either `business_form` or `individual_form` has to be set. ⏎ Details of your individual identity verification information. ⏎ Specify this field when you want to submit an individual identity verification request. |
| ↳ individual_name **(Điều kiện)** | string | Bắt buộc khi `individual_form` is specified. ⏎ Full legal name. ⏎ The name you specify here must exactly match the name on your verification documents. You cannot change the name after the verification is complete. ⏎ Giới hạn độ dài: 128 characters. |
| ↳ region_iso_code **(Điều kiện)** | string | Bắt buộc khi `individual_form` is specified. ⏎ The country or region code for your business (Business Center account or ad account), in ISO 3166 format. ⏎ Example: `US`. ⏎ • To retrieve the country or region code of your Business Center account, use [/bc/get/](12-bc-management.md#doc-1737115687501826) and check the returned `registered_area` parameter. • To retrieve the country or region code of your ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `country` parameter. |
| ↳ file_type_code **(Điều kiện)** | string | Bắt buộc khi `individual_form` is specified. ⏎ The code of the verification document. ⏎ To obtain the code of a verification document available for your business, use [/account/verification/filetype/](72-verification.md#doc-1870687810081794). |
| ↳ identity_no **(Điều kiện)** | string | Bắt buộc khi `individual_form` is specified. ⏎ ID number. ⏎ Make sure the number you specify here matches the number on your government issued ID (driver's license, passport, etc.) This can't be changed after submission. ⏎ Giới hạn độ dài: 128 characters. |
| ↳ website_url **(Điều kiện)** | string | Bắt buộc khi `individual_form` is specified. ⏎ The URL of the company website. ⏎ Giới hạn độ dài: 512 characters. |
| ↳ qualification_image_ids **(Điều kiện)** | string[] | Bắt buộc khi `individual_form` is specified. ⏎ A list of qualification image IDs for personal identification documents. ⏎ You need to specify exactly two IDs, representing the front image and the back image. ⏎ To obtain the qualification image ID of a personal identification document, use [/account/verification/upload/](72-verification.md#doc-1870687812502530). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/account/verification/submit/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "business_form": {
        "company_name": "{{company_name}}",
        "website_url": "{{website_url}}",
        "industry_code": "OTC",
        "region_iso_code": "US",
        "file_type_code": "{{file_type_code}}",
        "license_no": "{{license_no}}",
        "qualification_image_ids": [
            "{{qualification_image_ids}}"
        ]
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1870687815670786"></a>
<!-- doc_id: 1870687815670786 -->
<!-- doc_id: 1870687815670786 -->
# Check the verification status of your account
> Đường dẫn: API Reference > Verification > Check the verification status of your account
Sử dụng endpoint này để truy xuất the current verification status of your Business Center or ad account.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/account/verification/status/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id **(Điều kiện)** | string | Phải chỉ định một trong hai trường `advertiser_id` hoặc `bc_id`. ⏎ The ID of the ad account that you want to check the verification status for. ⏎ To retrieve the list of ad accounts that you can access, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) and set `asset_type` to `ADVERTISER`. |
| bc_id **(Điều kiện)** | string | Phải chỉ định một trong hai trường `advertiser_id` hoặc `bc_id`. ⏎ The ID of the Business Center account that you want to check the verification status for. ⏎ To retrieve the list of Business Centers that you can access, use [/bc/get/](12-bc-management.md#doc-1737115687501826). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/account/verification/status/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ qualification_id | string | The qualification image ID of the verification document you submitted for your Business Center or ad account. ⏎ If you want to create Organization Accounts within an Agency Business Center, you can pass this ID to `qualification_id` in [/bc/oa/create/](15-bc-assets.md#doc-1855027199571138). |
| ↳ verification_status | string | The current verification status of the ad account or Business Center account. ⏎ Các giá trị enum hỗ trợ: • `NOT_SUBMITTED`: The verification has not been submitted. • `REVIEWING`: The verification is currently under review. • `VERIFIED`: The account has been verified successfully. • `FAILED`: The verification has failed. • `EXPIRED`: The verification has expired. |
| ↳ rejection_reason | string | Returned only when `verification_status` is `FAILED`. ⏎ The reason for rejecting the verification request. ⏎ For common rejection reasons and troubleshooting suggestions, see [List of common rejection reasons and suggestions for verification failures](https://ads.tiktok.com/help/article/list-of-common-rejection-reasons-and-suggestions-for-verification-failures). |
| ↳ audit_time | string | The time when the review of the verification request was completed, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0 time). ⏎ Example: `2026-07-08 10:30:58`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "audit_time": "2026-07-08 10:30:58",
        "qualification_id": "{{qualification_id}}",
        "rejection_reason": "{{rejection_reason}}",
        "verification_status": "FAILED"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Xác minh (Verification)**:

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

