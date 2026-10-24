# Chẩn đoán quảng cáo (Ad Diagnosis)
<a id="doc-1738674938808321"></a>
<!-- doc_id: 1738674938808321 -->

Chẩn đoán quảng cáo (Ad diagnosis) là tính năng giúp phân tích các nhóm quảng cáo của bạn, phát hiện các vấn đề tiềm ẩn và cung cấp các đề xuất khắc phục hoặc cải thiện hiệu suất. Ad Diagnosis API cho phép bạn lấy kết quả chẩn đoán cho các nhóm quảng cáo cùng các đề xuất cải thiện liên quan đến nội dung sáng tạo (creative), giá thầu (bid), ngân sách (budget) hoặc theo dõi sự kiện (event tracking).

Nhóm API này bao gồm endpoint sau:
* [Lấy kết quả chẩn đoán cho các nhóm quảng cáo](06-ad-diagnosis.md#doc-1738674986981378)

---

## Lấy kết quả chẩn đoán cho các nhóm quảng cáo (`Get diagnoses for ad groups`)
<a id="doc-1738674986981378"></a>
<!-- doc_id: 1738674986981378 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/get/`

**Mục đích**: Sử dụng endpoint này để lấy kết quả chẩn đoán bao gồm các vấn đề phát hiện được và đề xuất cải thiện cho các nhóm quảng cáo đang hoạt động. Các nhóm quảng cáo không có đề xuất nào sẽ không được trả về trong danh sách kết quả.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

Lưu ý: TikTok API yêu cầu các tham số kiểu đối tượng/mảng phải được mã hóa URL dưới dạng chuỗi JSON trong query string.

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| filtering | object | Không bắt buộc | Điều kiện lọc kết quả chẩn đoán (chuỗi JSON đối tượng). |
| ↳ adgroup_ids | string[] | Không bắt buộc | Danh sách các ID nhóm quảng cáo cần lấy chẩn đoán. Kích thước tối đa: 20 ID. |
| ↳ issue_category | string[] | Không bắt buộc | Danh mục các vấn đề cần chẩn đoán. Các giá trị cho phép:<br>• `CREATIVE`: Các vấn đề liên quan đến nội dung sáng tạo video.<br>• `BID_AND_BUDGET`: Các vấn đề liên quan đến giá thầu và ngân sách.<br>• `EVENT_TRACK`: Các vấn đề liên quan đến theo dõi sự kiện chuyển đổi pixel.<br>Lưu ý: Nếu chỉ định nhiều giá trị, hệ thống sẽ trả về các chẩn đoán thuộc bất kỳ danh mục nào được chọn. Nếu không chỉ định, toàn bộ danh mục sẽ được trả về. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'filtering={"adgroup_ids":["1723456789012345"],"issue_category":["CREATIVE","BID_AND_BUDGET","EVENT_TRACK"]}' https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "filtering": json.dumps({
        "adgroup_ids": ["1723456789012345"],
        "issue_category": ["CREATIVE", "BID_AND_BUDGET", "EVENT_TRACK"]
    }),
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu chẩn đoán trả về. |
| ↳ results | object[] | Danh sách các nhóm quảng cáo cùng các chẩn đoán tương ứng. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ diagnosis | object | Kết quả chẩn đoán chi tiết cho nhóm quảng cáo. |
| ↳↳↳ diagnosis_time | string | Thời gian yêu cầu chẩn đoán (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ suggestions | object[] | Danh sách các đề xuất cải thiện cho nhóm quảng cáo. |
| ↳↳↳↳ creative | object[] | Đề xuất cho các nội dung sáng tạo trong nhóm quảng cáo (trả về mảng rỗng `[]` nếu không phát hiện vấn đề). |
| ↳↳↳↳↳ suggestion_time | string | Thời điểm phát hiện vấn đề và tạo đề xuất (UTC+0). |
| ↳↳↳↳↳ vid | string | Video ID liên quan đến vấn đề. |
| ↳↳↳↳↳ name | string | Tên quảng cáo. |
| ↳↳↳↳↳ ad_id | string | ID quảng cáo. |
| ↳↳↳↳↳ issue_suggestion | string | Đề xuất giải quyết vấn đề nội dung sáng tạo:<br>• `NOBGM`: Video thiếu nhạc nền, cần bổ sung nhạc nền (có thể dùng [/creative/quick_optimization/create/](38-creative-tools.md#doc-1739355078757377)).<br>• `VIDEO_LENGTH`: Thời lượng video quá ngắn, cần tăng thời lượng video.<br>• `VIDEO_RESOLUTION`: Độ phân giải video quá thấp, cần thay thế video có độ phân giải cao hơn. |
| ↳↳↳↳↳ suggestion_id | string | ID định danh của đề xuất. |
| ↳↳↳↳ bid_and_budget | object[] | Đề xuất liên quan đến giá thầu và ngân sách (trả về mảng rỗng `[]` nếu không có vấn đề). |
| ↳↳↳↳↳ suggestion_time | string | Thời điểm phát hiện vấn đề và tạo đề xuất (UTC+0). |
| ↳↳↳↳↳ suggestion_id | string | ID đề xuất. |
| ↳↳↳↳↳ issue_suggestion | string | Đề xuất giải quyết vấn đề giá thầu/ngân sách:<br>• `SUGGEST_BID`: Cung cấp mức giá thầu gợi ý mới.<br>• `SUGGEST_BUDGET`: Cung cấp mức ngân sách gợi ý mới.<br>• `NOBID_SWITCH`: Chuyển sang chiến lược giá thầu Phân phối tối đa (Maximum Delivery).<br>• `BUDGET_EDR`: Cung cấp khuyến nghị về Ngân sách EDR. Xem thêm tại [Estimated Delivery Results](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1746463274713089).<br>• `BID_EDR`: Cung cấp khuyến nghị về Giá thầu EDR. |
| ↳↳↳↳↳ bid | number | Giá thầu hiện tại của nhóm quảng cáo (trả về khi `issue_suggestion` là `SUGGEST_BID`). |
| ↳↳↳↳↳ budget | number | Ngân sách hiện tại của nhóm quảng cáo (trả về khi `issue_suggestion` là `SUGGEST_BID`, `SUGGEST_BUDGET`, hoặc `NOBID_SWITCH`). |
| ↳↳↳↳↳ suggest_bid | number | Giá thầu gợi ý nên áp dụng (khi `issue_suggestion` là `SUGGEST_BID`). |
| ↳↳↳↳↳ suggest_budget | number | Ngân sách gợi ý nên áp dụng (khi `issue_suggestion` là `SUGGEST_BUDGET` hoặc `NOBID_SWITCH`). |
| ↳↳↳↳↳ cost_floor | number | Mức chi phí tối thiểu ước tính (khi `issue_suggestion` là `SUGGEST_BID`). |
| ↳↳↳↳↳ bid_edr_info | object[] | Dữ liệu khuyến nghị Giá thầu EDR (trả về mảng rỗng nếu không phải `BID_EDR`). Gồm 9 tập dữ liệu mô phỏng tỷ lệ tăng giá thầu từ -10% đến 30% (bước nhảy 5%) và kết quả ước tính tương ứng. |
| ↳↳↳↳↳↳ recommended_bid | number | Mức giá thầu khuyến nghị. Áp dụng bằng cách cập nhật vào trường `conversion_bid_price` qua endpoint [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) trong ngày. |
| ↳↳↳↳↳↳ bid_increase_ratio | number | Tỷ lệ tăng giá thầu ước tính. |
| ↳↳↳↳↳↳ estimated_cost | number | Chi phí ước tính sau khi thay đổi giá thầu. |
| ↳↳↳↳↳↳ cost_uplift | number | Mức chi phí gia tăng ước tính. |
| ↳↳↳↳↳↳ cost_uplift_ratio | number | Tỷ lệ chi phí gia tăng ước tính. |
| ↳↳↳↳↳ budget_edr_info | object[] | Dữ liệu khuyến nghị Ngân sách EDR (trả về mảng rỗng nếu không phải `BUDGET_EDR`). Gồm 15 tập dữ liệu mô phỏng tỷ lệ tăng ngân sách từ -20% đến 50% (bước nhảy 5%) và kết quả ước tính tương ứng. |
| ↳↳↳↳↳↳ recommended_budget | number | Mức ngân sách khuyến nghị. Áp dụng qua endpoint [/adgroup/budget/update/](07-ad-groups-p3.md#doc-1739591133130817) trong ngày. |
| ↳↳↳↳↳↳ budget_increase_ratio | number | Tỷ lệ tăng ngân sách ước tính. |
| ↳↳↳↳↳↳ estimated_conversion | number | Số lượt chuyển đổi ước tính. |
| ↳↳↳↳↳↳ conversion_uplift | number | Số lượng chuyển đổi tăng thêm ước tính. |
| ↳↳↳↳↳↳ conversion_uplift_ratio | number | Tỷ lệ chuyển đổi gia tăng ước tính. |
| ↳↳↳↳↳↳ cpa | number | Chi phí cho mỗi chuyển đổi (CPA) ước tính. |
| ↳↳↳↳↳↳ cpa_uplift | number | Mức thay đổi CPA ước tính. |
| ↳↳↳↳↳↳ cpa_uplift_ratio | number | Tỷ lệ thay đổi CPA ước tính. |
| ↳↳↳↳↳↳ impression | number | Số lượt hiển thị ước tính. |
| ↳↳↳↳ event_track | object[] | Đề xuất liên quan đến theo dõi sự kiện chuyển đổi (trả về mảng rỗng nếu không có vấn đề). |
| ↳↳↳↳↳ suggestion_time | string | Thời điểm phát hiện vấn đề và tạo đề xuất (UTC+0). |
| ↳↳↳↳↳ suggestion_id | string | ID đề xuất theo dõi sự kiện. |
| ↳↳↳↳↳ issue_suggestion | string | Đề xuất giải quyết vấn đề sự kiện:<br>• `PIXEL`: Pixel không ghi nhận hoạt động nào trong 7 ngày qua. Hãy kiểm tra lại cài đặt pixel của bạn. |
| ↳↳↳↳↳ pixel_id | string | ID của Pixel gặp vấn đề. |
| ↳↳↳↳↳ pixel_code | string | Mã đoạn mã Pixel (Pixel code). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "results": [
      {
        "adgroup_id": "1723456789012345",
        "adgroup_name": "Nhóm quảng cáo Mùa hè",
        "diagnosis": {
          "diagnosis_time": "2026-05-21 00:00:01",
          "suggestions": [
            {
              "creative": [],
              "bid_and_budget": [
                {
                  "suggestion_id": "sug_bid_123456",
                  "suggestion_time": "2026-05-21 00:00:01",
                  "issue_suggestion": "SUGGEST_BID",
                  "bid": 2.5,
                  "suggest_bid": 3.0,
                  "budget": 100.0,
                  "cost_floor": 2.0,
                  "bid_edr_info": [],
                  "budget_edr_info": []
                }
              ],
              "event_track": [
                {
                  "suggestion_id": "sug_pixel_789012",
                  "suggestion_time": "2026-05-21 00:00:01",
                  "issue_suggestion": "PIXEL",
                  "pixel_id": "C71234567890123456",
                  "pixel_code": "PIXEL_CODE_SAMPLE"
                }
              ]
            }
          ]
        }
      }
    ]
  }
}
```
