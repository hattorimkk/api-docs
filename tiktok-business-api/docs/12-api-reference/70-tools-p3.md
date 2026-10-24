# Công cụ tra cứu (Tools) — phần 3/3

> Phân hệ: apiref:Tools.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Get bid protection history (#doc-1874392516418561)](#doc-1874392516418561)
- [2. Get rule sets within an ad account (#doc-1879581236824514)](#doc-1879581236824514)
- [3. Create, update, or delete a rule set within an ad account (#doc-1879581240885250)](#doc-1879581240885250)

---

<a id="doc-1874392516418561"></a>
<!-- doc_id: 1874392516418561 -->
<!-- doc_id: 1874392516418561 -->
# Get bid protection history
> Đường dẫn: API Reference > Tools > Get bid protection history
Sử dụng endpoint này để truy xuất your bid protection history and ad credits from the past 60 days for a list of Upgraded Smart+ Campaigns or Upgraded Smart+ Ad Groups.

Results are calculated daily and updated every 24 hours.

# Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/report/bid_protection/detail/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| data_level  ****(Bắt buộc)**** | string | The data level. ⏎ Các giá trị enum hỗ trợ: • `CAMPAIGN`: Campaign level. • `ADGROUP`: Ad group level. |
| query_ids  ****(Bắt buộc)**** | string[] | The list of IDs to query. ⏎ The maximum allowed size is 200 divided by the time range you define using `start_date` and `end_date`. For example, if you set `start_date` to `2026-08-01` and `end_date` to `2026-08-11` (a 10-day range), the maximum number of IDs you can specify in `query_ids` is 20 (200 divided by 10). ⏎ • When `data_level` is `CAMPAIGN`, specify a list of Upgraded Smart+ Campaign IDs. • To retrieve Upgraded Smart+ Campaign IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). • When `data_level` is `ADGROUP`, specify a list of Upgraded Smart+ Ad Group IDs. • To retrieve Upgraded Smart+ Ad Group IDs, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). ⏎ All IDs must belong to the same advertiser. |
| start_date  ****(Bắt buộc)**** | string | The start date for your bid protection history query, in the format of `YYYY-MM-DD` (ad account timezone). ⏎ Ensure the start date is within the past 60 days and is earlier than or equal to your `end_date`. |
| end_date  ****(Bắt buộc)**** | string | The end date for your bid protection history query, in the format of `YYYY-MM-DD` (ad account timezone). ⏎ Ensure the end date is within 60 days after your `start_date` and is later than or equal to the `start_date`. |

## Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/report/bid_protection/detail/get/?advertiser_id={{advertiser_id}}&data_level=CAMPAIGN&query_ids=["{{query_id}}"]&start_date={{start_date}}&end_date={{end_date}}' \
--header 'Access-Token: {{Access-Token}}'
```

# Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ bid_protection_records | object[] | The details of the bid protection records you queried. |
| ↳↳ data_level | string | The data level. ⏎ Các giá trị enum hỗ trợ: • `CAMPAIGN`: Campaign level. • `ADGROUP`: Ad group level. |
| ↳↳ query_id | string | The specific ID you queried. • When `data_level` is `CAMPAIGN`, this field represents an Upgraded Smart+ ID chiến dịch quảng cáo. • When `data_level` is `ADGROUP`, this field represents an Upgraded Smart+ ID nhóm quảng cáo. |
| ↳↳ record_date | string | The date when the record was generated, in the format of `YYYY-MM-DD` (ad account timezone). |
| ↳↳ bid_protection_daily_status | string | The bid protection status on the date. ⏎ Các giá trị enum hỗ trợ: • `UNDER_PROTECTION`: Active. The campaign is active today; results are calculated on a daily basis. • `INELIGIBLE`: Ineligible. Bid protection is ineligible for this date because this campaign or ad group status was paused or deleted. • `CONFIRMING`: Pending. Bid protection results are pending and most ad credits will be updated in 8 to 10 days. • `PAYMENT_COMPLETE`: Credit issued. Ad credits have been issued. • `TARGET_MET`: Target met. The bid target was met, so no ad credits were issued. |
| ↳↳ status_detail | string | The specific details of the bid protection status on the date. |
| ↳↳ credit_amount | string | The ad credit amount for the date, scaled by a factor of 100,000. ⏎ The value does not represent the exact monetary amount directly. To determine the actual amount, divide this value by 100,000. ⏎ For example, if you receive a `credit_amount` of `3000000` in USD, you can calculate the true value by dividing it by 100,000, which gives you an actual ad credit of 30 USD. |
| ↳↳ currency | string | The currency for the ad credits amount, in the format of [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code. ⏎ Example: `USD`. |

## Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "bid_protection_records": [
            {
                "bid_protection_daily_status": "TARGET_MET",
                "credit_amount": "0",
                "currency": "",
                "data_level": "CAMPAIGN",
                "record_date": "{{query_date}}",
                "query_id": "{{query_id}}",
                "status_detail": "{{status_detail}}"
            },
            {
                "bid_protection_daily_status": "PAYMENT_COMPLETE",
                "credit_amount": "712000000",
                "currency": "JPY",
                "data_level": "CAMPAIGN",
                "record_date": "2026-08-11",
                "query_id": "1872494183280162",
                "status_detail": "Ad credits have been issued."
            },
            {
                "bid_protection_daily_status": "INELIGIBLE",
                "credit_amount": "0",
                "currency": "",
                "data_level": "CAMPAIGN",
                "record_date": "{{query_date}}",
                "query_id": "{{query_id}}",
                "status_detail": "{{status_detail}}"
            },
            {
                "bid_protection_daily_status": "CONFIRMING",
                "credit_amount": "0",
                "currency": "",
                "data_level": "CAMPAIGN",
                "record_date": "{{query_date}}",
                "query_id": "{{query_id}}",
                "status_detail": "{{status_detail}}"
            }
        ]
    }
}
```

---

<a id="doc-1879581236824514"></a>
<!-- doc_id: 1879581236824514 -->
<!-- doc_id: 1879581236824514 -->
# Get rule sets within an ad account
> Đường dẫn: API Reference > Tools > Get rule sets within an ad account
Sử dụng endpoint này để truy xuất value rule sets within an ad account.

A rule set defines how much more certain audiences, conversion locations, and operating systems matter to your business. Our system will then optimize outcomes based on these rules.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| with_rules | boolean | Có thực hiện return rule details (the object array `rules`) in the response. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| value_rule_set_ids | string[] | A list of rule set IDs to filter the results by. ⏎ No max size. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/get/?advertiser_id={{advertiser_id}}&with_rules=true' \
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
| ↳ value_rule_sets | object[] | Details of rule sets within the ad account. |
| ↳↳ create_time | string | The time when the rule set was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0 time). ⏎ Example: `2026-01-01 00:00:01`. |
| ↳↳ value_rule_set_id | string | The ID of the rule set. |
| ↳↳ rule_set_name | string | The name of the rule set. |
| ↳↳ rules | object[] | Details of rules in the rule set. |
| ↳↳↳ order | number | The order of the rule in the rule set. ⏎ When you configure multiple rules in a rule set, this order indicates their priority. The system will prioritize rule application based on the rule order. If a person meets the criteria for multiple rules, we'll only apply the first applicable rule in the list. ⏎ For example: ⏎ Rule 1: Increase bid by 20% for ages 25–34 in the United States ⏎ Rule 2: Increase bid by 50% for iOS operating system ⏎ So a US-based iOS user aged 25–34 matches both rules, but only gets a 20% bid increase because Rule 1 comes first. |
| ↳↳↳ rule_id | string | Rule ID. |
| ↳↳↳ rule_name | string | Rule name. |
| ↳↳↳ criteria | object[] | Details of criteria for the rule. |
| ↳↳↳↳ criteria_type | string | Criterion type. ⏎ Các giá trị enum hỗ trợ: • `CRITERIA_TYPE_GENDER`: Genders. • `CRITERIA_TYPE_AGE`: Ages. • `CRITERIA_TYPE_LOCATION`: Locations. • `CRITERIA_TYPE_OS`: Operating systems. • `CRITERIA_TYPE_AUDIENCE`: Audience tags. |
| ↳↳↳↳ value | object | Details of value or values for the criterion. |
| ↳↳↳↳↳ gender | string | Returned when `criteria_type` is `CRITERIA_TYPE_GENDER`. ⏎ Gender. ⏎ Các giá trị enum hỗ trợ: • `GENDER_MALE`: Male. • `GENDER_FEMALE`: Female. |
| ↳↳↳↳↳ age_groups | string[] | Returned when `criteria_type` is `CRITERIA_TYPE_AGE`. ⏎ A list of age groups. ⏎ Các giá trị enum hỗ trợ: • `AGE_18_24`: 18-24. • `AGE_25_34`: 25-34. • `AGE_35_44`: 35-44. • `AGE_45_54`: 45-54. • `AGE_55_100`: 55+. |
| ↳↳↳↳↳ location | object | Returned when `criteria_type` is `CRITERIA_TYPE_LOCATION`. ⏎ Details of values for the location criterion. |
| ↳↳↳↳↳↳ location_ids | string[] | A list of location IDs. |
| ↳↳↳↳↳↳ region_codes | string[] | A list of region codes. |
| ↳↳↳↳↳↳ province_ids | string[] | A list of province IDs. |
| ↳↳↳↳↳↳ city_ids | string[] | A list of city IDs. |
| ↳↳↳↳↳ operating_systems | string[] | Returned when `criteria_type` is `CRITERIA_TYPE_OS`. ⏎ A list of operating systems. ⏎ Các giá trị enum hỗ trợ: • `ANDROID`: Android. • `IOS`: iOS. |
| ↳↳↳↳↳ audience_ids | string[] | Returned when `criteria_type` is `CRITERIA_TYPE_AUDIENCE`. ⏎ A list of audience IDs. |
| ↳↳↳ adjust_percentage | number | Bid adjustment percentage. • For bid increases: [1, 50]. • For bid decreases: [-70, -1]. ⏎ An `adjust_percentage` of -70 represents a bid decrease of 70% when the conditions defined in `criteria` are met. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "value_rule_sets": [
            {
                "create_time": "{{create_time}}",
                "rule_set_name": "{{rule_set_name}}",
                "rules": [
                    {
                        "adjust_percentage": -50,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_AGE",
                                "value": {
                                    "age_groups": [
                                        "AGE_18_24"
                                    ]
                                }
                            },
                            {
                                "criteria_type": "CRITERIA_TYPE_GENDER",
                                "value": {
                                    "gender": "GENDER_FEMALE"
                                }
                            }
                        ],
                        "order": 1,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    },
                    {
                        "adjust_percentage": 20,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_GENDER",
                                "value": {
                                    "gender": "GENDER_MALE"
                                }
                            },
                            {
                                "criteria_type": "CRITERIA_TYPE_OS",
                                "value": {
                                    "operating_systems": [
                                        "ANDROID"
                                    ]
                                }
                            }
                        ],
                        "order": 2,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    }
                ],
                "value_rule_set_id": "{{value_rule_set_id}}"
            },
            {
                "create_time": "{{create_time}}",
                "rule_set_name": "{{rule_set_name}}",
                "rules": [
                    {
                        "adjust_percentage": 12,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_AGE",
                                "value": {
                                    "age_groups": [
                                        "AGE_25_34"
                                    ]
                                }
                            }
                        ],
                        "order": 1,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    }
                ],
                "value_rule_set_id": "{{value_rule_set_id}}"
            },
            {
                "create_time": "{{create_time}}",
                "rule_set_name": "{{rule_set_name}}",
                "rules": [
                    {
                        "adjust_percentage": 15,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_LOCATION",
                                "value": {
                                    "location": {
                                        "location_ids": [
                                            "{{location_id}}"
                                        ],
                                        "province_ids": [
                                            "{{province_id}}"
                                        ]
                                    }
                                }
                            }
                        ],
                        "order": 1,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    }
                ],
                "value_rule_set_id": "{{value_rule_set_id}}"
            },
            {
                "create_time": "{{create_time}}",
                "rule_set_name": "{{rule_set_name}}",
                "rules": [
                    {
                        "adjust_percentage": 10,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_GENDER",
                                "value": {
                                    "gender": "GENDER_FEMALE"
                                }
                            }
                        ],
                        "order": 1,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    }
                ],
                "value_rule_set_id": "{{value_rule_set_id}}"
            },
            {
                "create_time": "{{create_time}}",
                "rule_set_name": "{{rule_set_name}}",
                "rules": [
                    {
                        "adjust_percentage": -10,
                        "criteria": [
                            {
                                "criteria_type": "CRITERIA_TYPE_OS",
                                "value": {
                                    "operating_systems": [
                                        "IOS"
                                    ]
                                }
                            }
                        ],
                        "order": 1,
                        "rule_id": "{{rule_id}}",
                        "rule_name": "{{rule_name}}"
                    }
                ],
                "value_rule_set_id": "{{value_rule_set_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1879581240885250"></a>
<!-- doc_id: 1879581240885250 -->
<!-- doc_id: 1879581240885250 -->
# Create, update, or delete a rule set within an ad account
> Đường dẫn: API Reference > Tools > Create, update, or delete a rule set within an ad account
Sử dụng endpoint này để tạo, update, or delete a rule set within an ad account.

> **Note:** 
> - Creating rule sets is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.
> - You can create up to 20 rule sets for each ad account.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/create_or_update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| operation_type  ****(Bắt buộc)**** | string | Operation type. ⏎ Các giá trị enum hỗ trợ: • `CREATE`: To create a new rule set. • `UPDATE`: To update an existing rule set. • `DELETE`: To delete an existing rule set. |
| value_rule_set  ****(Bắt buộc)**** | object | Details of the rule set. |
| ↳ value_rule_set_id **(Điều kiện)** | string | • Bắt buộc khi `operation_type` is `UPDATE` or `DELETE`. • Not supported when `operation_type` is `CREATE`. ⏎ The ID of the rule set that you want to update or delete. ⏎ To retrieve existing rule sets within an ad account, use [/smart_plus/value_rule_set/get/](70-tools-p3.md#doc-1879581236824514). |
| ↳ rule_set_name **(Điều kiện)** | string | • Bắt buộc khi `operation_type` is `CREATE`. • Optional when `operation_type` is `UPDATE`. • Not supported when `operation_type` is `DELETE`. ⏎ The name of the rule set. ⏎ Giới hạn độ dài: 512 characters. ⏎ **Note**: Duplicate rule set names are not supported. |
| ↳ rules **(Điều kiện)** | object[] | • Bắt buộc khi `operation_type` is `CREATE`. • Optional when `operation_type` is `UPDATE`. • Not supported when `operation_type` is `DELETE`. ⏎ Details of rules in the rule set. ⏎ Each rule set can contain up to 10 rules. ⏎ **Note**: Duplicate rules or criteria are not supported in one rule set. |
| ↳↳ order **(Điều kiện)** | number | Bắt buộc khi `rules` is specified. ⏎ The order of the rule in the rule set. ⏎ Use consecutive integers starting from 1 (for example, 1, 2, and 3, rather than 1, 3, and 5). ⏎ When you configure multiple rules in a rule set, this order indicates their priority. The system will prioritize rule application based on the rule order. If a person meets the criteria for multiple rules, we'll only apply the first applicable rule in the list. ⏎ For example: ⏎ Rule 1: Increase bid by 20% for ages 25–34 in the United States ⏎ Rule 2: Increase bid by 50% for iOS operating system ⏎ So a US-based iOS user aged 25–34 matches both rules, but only gets a 20% bid increase because Rule 1 comes first. |
| ↳↳ rule_id | string | Chỉ hợp lệ khi `operation_type` is `UPDATE`. ⏎ Rule ID. • When this field is specified, the `rule_id` will stay the same after the rule set update. • When this field is not specified, the system will generate a new `rule_id` after the rule set update. |
| ↳↳ rule_name **(Điều kiện)** | string | Bắt buộc khi `rules` is specified. ⏎ Rule name. |
| ↳↳ criteria **(Điều kiện)** | object[] | Bắt buộc khi `rules` is specified. ⏎ Details of criteria for the rule. ⏎ You can specify up to two criteria per rule. If you include two criteria in a single rule, the system triggers the rule only when a person meets both criteria. |
| ↳↳↳ criteria_type **(Điều kiện)** | string | Bắt buộc khi `criteria` is specified. ⏎ Criterion type. ⏎ Các giá trị enum hỗ trợ: • `CRITERIA_TYPE_GENDER`: Genders. • `CRITERIA_TYPE_AGE`: Ages. • `CRITERIA_TYPE_LOCATION`: Locations. • `CRITERIA_TYPE_OS`: Operating systems. • `CRITERIA_TYPE_AUDIENCE`: Audience |
| ↳↳↳ value **(Điều kiện)** | object | Bắt buộc khi `criteria` is specified. ⏎ Details of value or values for the criterion. |
| ↳↳↳↳ gender **(Điều kiện)** | string | Bắt buộc khi `criteria_type` is `CRITERIA_TYPE_GENDER`. ⏎ Gender. ⏎ Các giá trị enum hỗ trợ: • `GENDER_MALE`: Male. • `GENDER_FEMALE`: Female. |
| ↳↳↳↳ age_groups **(Điều kiện)** | string[] | Bắt buộc khi `criteria_type` is `CRITERIA_TYPE_AGE`. ⏎ A list of age groups. ⏎ Các giá trị enum hỗ trợ: • `AGE_18_24`: 18-24. • `AGE_25_34`: 25-34. • `AGE_35_44`: 35-44. • `AGE_45_54`: 45-54. • `AGE_55_100`: 55+. |
| ↳↳↳↳ location **(Điều kiện)** | object | Bắt buộc khi `criteria_type` is `CRITERIA_TYPE_LOCATION`. ⏎ Details of values for the location criterion. |
| ↳↳↳↳↳ location_ids **(Điều kiện)** | string[] | Bắt buộc khi `location` is specified. ⏎ A list of location IDs. • To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) or [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. • To get the list of location IDs, see [Location IDs](../15-appendix/phu-luc-p1.md#doc-1737172315193346). |
| ↳↳↳↳ operating_systems **(Điều kiện)** | string[] | Bắt buộc khi `criteria_type` is `CRITERIA_TYPE_OS`. ⏎ A list of operating systems. ⏎ Các giá trị enum hỗ trợ: • `ANDROID`: Android. • `IOS`: iOS. |
| ↳↳↳↳ audience_ids **(Điều kiện)** | string[] | Bắt buộc khi `criteria_type` is `CRITERIA_TYPE_AUDIENCE`. ⏎ A list of audience IDs. ⏎ The audience can be a custom audience, lookalike audience, or saved audience. ⏎ Kích thước tối đa: 5. ⏎ Ensure each audience is valid. • To retrieve valid custom or lookalike audience IDs within an ad account, use [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746) and select audiences with `is_valid` as `true`. • To retrieve saved audience IDs within an ad account, use [/dmp/saved_audience/list/](09-audience.md#doc-1780154619404290). ⏎ **Note**: Duplicate audience IDs are not supported. |
| ↳↳ adjust_percentage **(Điều kiện)** | number | Bắt buộc khi `rules` is specified. ⏎ Bid adjustment percentage. • For bid increases: [1, 50]. • For bid decreases: [-70, -1]. ⏎ An `adjust_percentage` of -70 represents a bid decrease of 70% when the conditions defined in `criteria` are met. |

### Ví dụ lệnh cURL (Example)
#### Create a rule set
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/create_or_update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
---data '{
    "advertiser_id": "{{advertiser_id}}",
    "operation_type": "CREATE",
    "value_rule_set": {
        "rule_set_name": "{{rule_set_name}}",
        "rules": [
            {
                "order": 1,
                "rule_name": "{{rule_name}}",
                "criteria": [
                    {
                        "criteria_type": "CRITERIA_TYPE_GENDER",
                        "value": {
                            "gender": "GENDER_FEMALE"
                        }
                    }
                ],
                "adjust_percentage": 10
            }
        ]
    }
}'
```

#### Update a rule set
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/create_or_update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "operation_type": "UPDATE",
    "value_rule_set": {
        "value_rule_set_id": "{{value_rule_set_id}}",
        "rule_set_name": "{{rule_set_name}}",
        "rules": [
            {
                "order": 1,
                "rule_name": "{{rule_name}}",
                "criteria": [
                    {
                        "criteria_type": "CRITERIA_TYPE_AUDIENCE",
                        "value": {
                            "audience_ids": [
                                "{{audience_ids}}"
                            ]
                        }
                    }
                ],
                "adjust_percentage": 8
            }
        ]
    }
}'
```

#### Delete a rule set
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/value_rule_set/create_or_update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "operation_type": "DELETE",
    "value_rule_set": {
        "value_rule_set_id": "{{value_rule_set_id}}"
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
| ↳ value_rule_set_id | string | The ID of the rule set. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "value_rule_set_id": "{{value_rule_set_id}}"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Công cụ tra cứu (Tools) — phần 3/3**:

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

