# Quy tắc tự động (Automated Rules)
<a id="doc-1738763978290178"></a>
<!-- doc_id: 1738763978290178 -->

Quy tắc tự động (Automated Rules) giúp bạn tự động hóa việc quản lý và tối ưu hóa các chiến dịch, nhóm quảng cáo và quảng cáo trên TikTok. Khi các điều kiện được định nghĩa trước được thỏa mãn (ví dụ: chi phí vượt ngưỡng, CPA quá cao, hoặc tỷ lệ chuyển đổi đạt mục tiêu), hệ thống sẽ tự động thực hiện các hành động tương ứng như bật/tắt đối tượng, điều chỉnh giá thầu, tăng giảm ngân sách hoặc gửi thông báo qua email.

Nhóm API này bao gồm các endpoint sau:
* [Tạo quy tắc tự động](11-automated-rules.md#doc-1738767670852610)
* [Lấy quy tắc theo ID](11-automated-rules.md#doc-1738768750822466)
* [Lấy danh sách quy tắc theo bộ lọc](11-automated-rules.md#doc-1738768861976578)
* [Lấy kết quả thực thi quy tắc](11-automated-rules.md#doc-1738769076676609)
* [Lấy chi tiết kết quả thực thi](11-automated-rules.md#doc-1738769098314754)
* [Cập nhật quy tắc tự động](11-automated-rules.md#doc-1738769123170306)
* [Cập nhật trạng thái quy tắc](11-automated-rules.md#doc-1738769144119298)
* [Liên kết / Hủy liên kết quy tắc](11-automated-rules.md#doc-1738769164954626)

---

## Tạo quy tắc tự động (`Create rules`)
<a id="doc-1738767670852610"></a>
<!-- doc_id: 1738767670852610 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/create/`

**Mục đích**: Sử dụng endpoint này để tạo các quy tắc tự động mới cho tài khoản quảng cáo. Mỗi quy tắc bao gồm đối tượng áp dụng, điều kiện kích hoạt, hành động thực hiện, cài đặt thông báo và lịch trình kiểm tra.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| rules | object[] | Bắt buộc | Danh sách các quy tắc cần tạo. |
| ↳ name | string | Bắt buộc | Tên quy tắc tự động. |
| ↳ apply_objects | object[] | Bắt buộc | Các đối tượng áp dụng quy tắc (chiến dịch, nhóm quảng cáo hoặc quảng cáo). |
| ↳↳ dimension | string | Bắt buộc | Cấp độ đối tượng áp dụng. Giá trị enum: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳ dimension_ids | string[] | Không bắt buộc | Danh sách ID của các đối tượng cụ thể. |
| ↳↳ pre_condition_type | string | Bắt buộc | Điều kiện lọc đối tượng áp dụng:<br>• `SELECTED`: Chỉ áp dụng cho các đối tượng chỉ định qua `dimension_ids`.<br>• `ALL_ACTIVE_CAMPAIGN`: Áp dụng cho tất cả chiến dịch đang hoạt động.<br>• `ALL_ACTIVE_AD_GROUP`: Áp dụng cho tất cả nhóm quảng cáo đang hoạt động.<br>• `ALL_ACTIVE_AD`: Áp dụng cho tất cả quảng cáo đang hoạt động.<br>• `ALL_ACTIVE_AD_GROUP_UNDER_SELECTED`: Áp dụng cho tất cả nhóm quảng cáo đang hoạt động thuộc chiến dịch được chọn.<br>• `ALL_ACTIVE_AD_UNDER_SELECTED`: Áp dụng cho tất cả quảng cáo đang hoạt động thuộc đối tượng được chọn.<br>• `ALL_INACTIVE_CAMPAIGN`: Tất cả chiến dịch không hoạt động.<br>• `ALL_INACTIVE_AD_GROUP`: Tất cả nhóm quảng cáo không hoạt động.<br>• `ALL_INACTIVE_AD`: Tất cả quảng cáo không hoạt động.<br>• `ALL_INACTIVE_AD_GROUP_UNDER_SELECTED`: Tất cả nhóm quảng cáo không hoạt động thuộc chiến dịch được chọn.<br>• `ALL_INACTIVE_AD_UNDER_SELECTED`: Tất cả quảng cáo không hoạt động thuộc đối tượng được chọn. |
| ↳ conditions | object[] | Bắt buộc | Danh sách các điều kiện để kích hoạt quy tắc. |
| ↳↳ subject_type | string | Bắt buộc | Chỉ số hoặc tiêu chí làm căn cứ cho điều kiện. Các giá trị enum:<br>• `COST`<br>• `DAILY_BUDGET_SPENDING_RATE`<br>• `LIFETIME_BUDGET_SPENDING_RATE`<br>• `IMPRESSION`<br>• `CLICK`<br>• `CONVERSION`<br>• `CONVERSION_SKAN`<br>• `CVR`<br>• `CVR_SKAN`<br>• `CPA`<br>• `CPM`<br>• `CPC`<br>• `CTR`<br>• `COST_PER_RESULT`<br>• `RESULT`<br>• `RESULT_RATE`<br>• `BID_STRATEGY`: Các giá trị `values` hợp lệ gồm: `COST_CAP`, `BID_CAP`, `MAX_CONVERSION`, `LOWEST_COST`.<br>• `OPTIMIZATION_GOAL`: Các giá trị `values` gồm: `CONVERT`, `CLICK`, `SHOW`, `REACH`, `INSTALL`, `IN_APP_EVENT`, `LEAD_GENERATION`, `TWO_SECOND_VIDEO_VIEW`, `SIX_SECOND_VIDEO_VIEW`.<br>• `OBJECTIVE`: Các giá trị `values` gồm: `TRAFFIC`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `VIDEO_VIEWS`, `REACH`, `LEAD_GENERATION`.<br>• `NAME`: Tên đối tượng.<br>• `DAYS_SINCE_CREATION`: Số ngày kể từ khi tạo (toán tử: `GT`, `LT`, `BETWEEN`, `MATCH`).<br>• `NO_CONDITION`: Quy tắc không có điều kiện (chỉ thực thi theo thời gian). Khi dùng giá trị này, chỉ truyền duy nhất `[{"subject_type":"NO_CONDITION"}]`.<br>• `ROAS_PURCHASE`<br>• `ROAS_IMPRESSION_ADS`<br>• `ROAS_PURCHASE_SKAN`<br>• `ROAS_COMPLETE_PAYMENT`<br>• `ROAS_PURCHASES_ONSITE`<br>• `NOT_REAL_TIME_CPA`<br>• `NOT_REAL_TIME_CONVERSION`<br>• `NOT_REAL_TIME_CVR`. |
| ↳↳ range_type | string | Không bắt buộc | Khoảng thời gian dữ liệu xét điều kiện. Enum: `TODAY`, `YESTERDAY`, `PAST_THREE_DAYS`, `PAST_FIVE_DAYS`, `PAST_SEVEN_DAYS`, `LIFETIME`. |
| ↳↳ match_type | string | Không bắt buộc | Toán tử so sánh: `GT` (lớn hơn), `LT` (nhỏ hơn), `BETWEEN` (ở giữa), `MATCH`. Khi `subject_type` là `NAME`, có thể dùng thêm: `CONTAINS`, `NOT_CONTAINS`, `START_WITH`, `END_WITH`, `STRING_EQUAL`. |
| ↳↳ values | string[] | Không bắt buộc | Giá trị so sánh của điều kiện. Nếu `match_type` là `BETWEEN`, mảng gồm 2 giá trị. Tuân thủ quy tắc xác thực bên dưới. |
| ↳↳ calculation_type | string | Không bắt buộc | Cách tính toán chi phí (chỉ áp dụng khi `subject_type` là `COST`). Mặc định: `OF_EACH_OBJECT`. Enum: `ALL_OBJECTS`, `OF_EACH_OBJECT`. |
| ↳ actions | object[] | Bắt buộc | Danh sách hành động thực hiện khi thỏa mãn điều kiện. |
| ↳↳ subject_type | string | Bắt buộc | Loại hành động: `TURN_ON` (bật), `TURN_OFF` (tắt), `MESSAGE` (chỉ gửi thông báo), `DAILY_BUDGET` (chỉnh ngân sách ngày), `LIFETIME_BUDGET` (chỉnh ngân sách trọn đời), `BID` (chỉnh giá thầu). |
| ↳↳ action_type | string | Không bắt buộc | Thao tác điều chỉnh: `INCREASE` (tăng), `DECREASE` (giảm), `ADJUST_TO` (đặt thành giá trị cố định). |
| ↳↳ value_type | string | Không bắt buộc | Loại giá trị điều chỉnh: `EXACT` (số tiền cụ thể) hoặc `PERCENT` (phần trăm). |
| ↳↳ value | object | Điều kiện | Giá trị điều chỉnh (bắt buộc khi `subject_type` là `DAILY_BUDGET`, `LIFETIME_BUDGET` hoặc `BID`). |
| ↳↳↳ value | float | Điều kiện | Số tiền hoặc tỷ lệ phần trăm muốn tăng, giảm hoặc đặt thành. |
| ↳↳↳ limit | float | Điều kiện | Mức giới hạn trần (khi `INCREASE`) hoặc sàn (khi `DECREASE`) của ngân sách / giá thầu. |
| ↳↳ frequency_info | object | Không bắt buộc | Cài đặt tần suất thực hiện hành động điều chỉnh. |
| ↳↳↳ type | string | Không bắt buộc | Tần suất: `ONLY_ONCE`, `ONCE_IN_24_H`, `ONCE_IN_48_H`, `ONCE_IN_1_W`, `CUSTOM`. |
| ↳↳↳ custom_frequency_type | string | Không bắt buộc | Loại tần suất tùy chỉnh: `N_MINTUE_Y_TIMES`, `N_HOUR_Y_TIMES`, `N_DAY_Y_TIMES`. |
| ↳↳↳ time | number | Không bắt buộc | Giá trị `N` trong tần suất tùy chỉnh. |
| ↳↳↳ count | number | Không bắt buộc | Giá trị `Y` trong tần suất tùy chỉnh. |
| ↳ notification | object | Bắt buộc | Cài đặt gửi thông báo khi quy tắc chạy. |
| ↳↳ notification_type | string | Bắt buộc | Loại thông báo: `TASK_FINISH` (khi hoàn thành tác vụ `MESSAGE`), `ANY_CHANGES` (mọi thay đổi khi hành động khác `MESSAGE`), `NOT_NOTIFICATION` (không thông báo). |
| ↳↳ email_setting | object | Không bắt buộc | Cài đặt gửi email. |
| ↳↳↳ notification_period | string | Không bắt buộc | Chu kỳ gửi email: `EVERY_TIME` (mỗi lần chạy), `TIME_SCHEDULE` (gửi tổng hợp theo giờ cố định). |
| ↳↳↳ email_exec_time | string[] | Điều kiện | Giờ gửi email tổng hợp (ví dụ `["12:00"]`), bắt buộc khi `notification_period` là `TIME_SCHEDULE`. |
| ↳↳↳ no_result_notification | boolean | Không bắt buộc | Có gửi thông báo khi không có kết quả hay không. Mặc định: `false`. |
| ↳↳↳ mute_option | string | Không bắt buộc | Tắt tiếng thông báo email trong ngày: `MUTE`, `UNMUTE`. |
| ↳ rule_exec_info | object | Bắt buộc | Lịch trình chạy quy tắc tự động. |
| ↳↳ exec_time_type | string | Bắt buộc | Tần suất chạy: `PER_HALF_HOUR` (mỗi 30 phút), `CUSTOM` (giờ tùy chỉnh), `HALF_HOUR_IN_SPECIFIC_TIME_PERIOD` (mỗi 30 phút trong khoảng thời gian nhất định), `SPECIFIC_TIME_ACCURATE_ONCE` (chạy đúng 1 lần vào thời điểm chỉ định). |
| ↳↳ exec_time | string | Không bắt buộc | Thời gian chạy cụ thể (định dạng "HH:MM" cho `CUSTOM` hoặc "YYYY-MM-DD HH:MM" cho `SPECIFIC_TIME_ACCURATE_ONCE`). |
| ↳↳ time_period_info | object[] | Không bắt buộc | Cấu hình khoảng thời gian khi `exec_time_type` là `HALF_HOUR_IN_SPECIFIC_TIME_PERIOD`. |
| ↳↳↳ num | integers[] | Điều kiện | Danh sách số biểu thị ngày trong tuần (1-7) hoặc ngày trong tháng (1-28). |
| ↳↳↳ start_time | string | Không bắt buộc | Giờ bắt đầu khoảng thời gian (ví dụ: "09:00"). |
| ↳↳↳ end_time | string | Không bắt buộc | Giờ kết thúc khoảng thời gian (ví dụ: "22:00"). |
| ↳↳↳ date_type | string | Không bắt buộc | Loại lịch: `DAY`, `WEEK`, `MONTH`. |
| ↳ tzone | string | Không bắt buộc | Múi giờ người dùng. Xem [Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089). |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN` (mặc định), `JA`. |

### Quy tắc xác thực giá trị (`values`)

| subject_type | Quy tắc xác thực giá trị values |
|---|---|
| NAME | Giới hạn độ dài chuỗi: (0, 512] ký tự. |
| COST <br> CPA <br> NOT_REAL_TIME_CPA <br> CPM <br> CPC <br> COST_PER_RESULT | Độ chính xác phụ thuộc đơn vị tiền tệ của tài khoản quảng cáo. Xem [Currency-specific precision](../15-appendix/phu-luc-p1.md#doc-1772544628718594). <br>Khoảng giá trị: [0, 100000000]. |
| DAILY_BUDGET_SPENDING_RATE <br> LIFETIME_BUDGET_SPENDING_RATE <br> CVR <br> CVR_SKAN <br> NOT_REAL_TIME_CVR <br> CTR <br> RESULT_RATE | Độ chính xác: 0.01. <br>Khoảng giá trị: [0, 100]. |
| IMPRESSION <br> CLICK <br> CONVERSION <br> CONVERSION_SKAN <br> NOT_REAL_TIME_CONVERSION <br> RESULT | Độ chính xác: 1 (số nguyên). <br>Khoảng giá trị: [0, 10000000000]. |
| ROAS_PURCHASE <br> ROAS_IMPRESSION_ADS <br> ROAS_PURCHASE_SKAN <br> ROAS_COMPLETE_PAYMENT <br> ROAS_PURCHASES_ONSITE | Độ chính xác: 0.01. <br>Khoảng giá trị: [0, 100000]. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "rules": [{
    "name": "Tự động tắt nhóm quảng cáo CPA cao",
    "apply_objects": [{
      "dimension": "ADGROUP",
      "pre_condition_type": "ALL_ACTIVE_AD_GROUP"
    }],
    "conditions": [{
      "subject_type": "CPA",
      "range_type": "TODAY",
      "match_type": "GT",
      "values": ["50.0"]
    }],
    "actions": [{
      "subject_type": "TURN_OFF"
    }],
    "notification": {
      "notification_type": "ANY_CHANGES"
    },
    "rule_exec_info": {
      "exec_time_type": "PER_HALF_HOUR"
    }
  }]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rule_ids | string[] | Danh sách các ID của quy tắc tự động vừa được tạo. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "rule_ids": [
      "1738769999999999"
    ]
  }
}
```

---

## Lấy quy tắc theo ID (`Get rules by ID`)
<a id="doc-1738768750822466"></a>
<!-- doc_id: 1738768750822466 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/get/`

**Mục đích**: Sử dụng endpoint này để truy vấn thông tin cấu hình chi tiết và lịch sử kiểm tra gần nhất của các quy tắc tự động theo danh sách ID quy tắc (`rule_ids`).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| rule_ids | string[] | Bắt buộc | Danh sách ID quy tắc cần lấy thông tin (chuỗi JSON mảng). Kích thước tối đa: 100 ID. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'rule_ids=["1738769999999999"]' https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "rule_ids": json.dumps(["1738769999999999"]),
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rules | object[] | Danh sách chi tiết các quy tắc tự động. |
| ↳↳ rule_id | string | ID quy tắc tự động. |
| ↳↳ rule_status | string | Trạng thái quy tắc: `ON` (đang bật), `OFF` (đã tắt), `DELETED` (đã xóa). |
| ↳↳ name | string | Tên quy tắc. |
| ↳↳ create_datetime | string | Thời gian tạo quy tắc. |
| ↳↳ apply_objects | object[] | Đối tượng áp dụng quy tắc. |
| ↳↳↳ dimesion | string | Cấp độ đối tượng áp dụng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳↳ dimension_ids | string[] | Danh sách ID đối tượng. |
| ↳↳↳ bind_type | string | Loại liên kết: `BIND`, `UNBIND`. |
| ↳↳↳ pre_condition_type | string | Điều kiện tiền lọc đối tượng. |
| ↳↳ conditions | object[] | Danh sách điều kiện kích hoạt. |
| ↳↳↳ subject_type | string | Chỉ số/tiêu chí điều kiện. |
| ↳↳↳ range_type | string | Khoảng thời gian dữ liệu. |
| ↳↳↳ match_type | string | Toán tử so sánh. |
| ↳↳↳ values | string[] | Giá trị so sánh. |
| ↳↳↳ calculation_type | string | Loại tính toán chi phí (`ALL_OBJECTS`, `OF_EACH_OBJECT`). |
| ↳↳ action | object | Hành động được thực thi. |
| ↳↳↳ subject_type | string | Loại hành động. |
| ↳↳↳ action_type | string | Thao tác điều chỉnh (`INCREASE`, `DECREASE`, `ADJUST_TO`). |
| ↳↳↳ value_type | string | Đơn vị giá trị (`EXACT`, `PERCENT`). |
| ↳↳↳ frequency_info | object | Tần suất hành động. |
| ↳↳↳↳ custom_frequency_type | string | Loại tần suất tùy chỉnh. |
| ↳↳↳↳ time | number | Khoảng thời gian `N`. |
| ↳↳↳↳ count | number | Số lần `Y`. |
| ↳↳ notification | object | Cấu hình thông báo. |
| ↳↳↳ notification_type | string | Loại thông báo. |
| ↳↳↳ email_setting | object | Cài đặt email. |
| ↳↳↳↳ notification_period | string | Chu kỳ thông báo. |
| ↳↳↳↳ email_exec_time | string[] | Giờ gửi email. |
| ↳↳↳↳ no_result_notification | boolean | Gửi thông báo khi không có kết quả. |
| ↳↳ rule_exec_info | object | Lịch trình chạy quy tắc. |
| ↳↳↳ exec_time_type | string | Loại lịch chạy. |
| ↳↳↳ exec_time | string | Thời gian chạy. |
| ↳↳↳ time_period_info | object[] | Khoảng thời gian chỉ định. |
| ↳↳↳↳ start_time | string | Giờ bắt đầu. |
| ↳↳↳↳ end_time | string | Giờ kết thúc. |
| ↳↳↳↳ date_type | string | Loại ngày (`DAY`, `WEEK`, `MONTH`). |
| ↳↳↳↳ num | number[] | Danh sách ngày trong tuần hoặc tháng. |
| ↳↳ last_check_result_summary | object | Tóm tắt kết quả kiểm tra quy tắc gần nhất. |
| ↳↳↳ task_exec_id | string | ID lượt thực thi tác vụ. |
| ↳↳↳ check_datetime | string | Thời gian kiểm tra. |
| ↳↳↳ exec_datetime | string | Thời gian thực thi. |
| ↳↳↳ no_change | number | Số đối tượng không có thay đổi. |
| ↳↳↳ change_success | number | Số đối tượng áp dụng thay đổi thành công. |
| ↳↳↳ change_fail | number | Số đối tượng thay đổi thất bại. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số quy tắc. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy danh sách quy tắc theo bộ lọc (`Get rules by filters`)
<a id="doc-1738768861976578"></a>
<!-- doc_id: 1738768861976578 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/list/`

**Mục đích**: Sử dụng endpoint này để truy vấn danh sách quy tắc tự động theo các tiêu chí lọc như tên quy tắc, trạng thái quy tắc, cấp độ đối tượng áp dụng hoặc loại hành động.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| filtering | object | Không bắt buộc | Điều kiện lọc danh sách quy tắc (chuỗi JSON đối tượng). |
| ↳ rule_name | string | Không bắt buộc | Lọc theo tên quy tắc. |
| ↳ rule_status | string | Không bắt buộc | Trạng thái quy tắc: `ON`, `OFF`. |
| ↳ data_dimension | string | Không bắt buộc | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳ action_type | string | Không bắt buộc | Loại hành động: `TURN_ON`, `TURN_OFF`, `MESSAGE`, `DAILY_BUDGET`, `LIFETIME_BUDGET`, `BID`. |
| ↳ exec_time_type | string | Không bắt buộc | Loại thời gian thực thi: `PER_HALF_HOUR`, `CUSTOM`, `HALF_HOUR_IN_SPECIFIC_TIME_PERIOD`, `SPECIFIC_TIME_ACCURATE_ONCE`. |
| page | number | Không bắt buộc | Số trang hiện tại. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Giá trị từ 1-100. Mặc định: 10. |
| tzone | string | Không bắt buộc | Múi giờ tài khoản. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'filtering={"rule_status":"ON","data_dimension":"ADGROUP"}' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/list/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "filtering": json.dumps({"rule_status": "ON", "data_dimension": "ADGROUP"}),
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rules | object[] | Danh sách quy tắc thỏa mãn điều kiện lọc. |
| ↳↳ rule_info | object | Cấu hình chi tiết của quy tắc. |
| ↳↳↳ rule_id | string | ID quy tắc. |
| ↳↳↳ rule_status | string | Trạng thái: `ON`, `OFF`, `DELETED`. |
| ↳↳↳ status | string | Trạng thái kích hoạt. |
| ↳↳↳ name | string | Tên quy tắc. |
| ↳↳↳ create_datetime | string | Thời gian tạo. |
| ↳↳↳ apply_objects | object[] | Đối tượng áp dụng. |
| ↳↳↳↳ dimesion | string | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳↳↳ dimension_ids | string[] | Danh sách ID đối tượng. |
| ↳↳↳↳ bind_type | string | Loại liên kết: `BIND`, `UNBIND`. |
| ↳↳↳↳ pre_condition_type | string | Điều kiện tiền lọc. |
| ↳↳↳ conditions | object[] | Điều kiện kích hoạt. |
| ↳↳↳↳ subject_type | string | Chỉ số/tiêu chí điều kiện. |
| ↳↳↳↳ range_type | string | Khoảng thời gian dữ liệu. |
| ↳↳↳↳ match_type | string | Toán tử so sánh. |
| ↳↳↳↳ values | string[] | Giá trị so sánh. |
| ↳↳↳↳ calculation_type | string | Loại tính toán chi phí. |
| ↳↳↳ action | object | Hành động thực hiện. |
| ↳↳↳↳ subject_type | string | Loại hành động. |
| ↳↳↳↳ action_type | string | Thao tác điều chỉnh. |
| ↳↳↳↳ value_type | string | Đơn vị giá trị. |
| ↳↳↳↳ frequency_info | object | Tần suất hành động. |
| ↳↳↳↳↳ custom_frequency_type | string | Tần suất tùy chỉnh. |
| ↳↳↳↳↳ time | number | Tham số thời gian. |
| ↳↳↳↳↳ count | number | Số lần thực hiện. |
| ↳↳↳ notification | object | Cấu hình thông báo. |
| ↳↳↳↳ notification_type | string | Loại thông báo. |
| ↳↳↳↳ email_setting | object | Cài đặt email. |
| ↳↳↳↳↳ notification_period | string | Chu kỳ gửi email. |
| ↳↳↳↳↳ email_exec_time | string[] | Giờ gửi email. |
| ↳↳↳↳↳ no_result_notification | boolean | Gửi thông báo khi không có kết quả. |
| ↳↳↳ rule_exec_info | object | Lịch trình chạy quy tắc. |
| ↳↳↳↳ exec_time_type | string | Loại lịch chạy. |
| ↳↳↳↳ exec_time | string | Giờ chạy cụ thể. |
| ↳↳↳↳ time_period_info | object[] | Khoảng thời gian cụ thể. |
| ↳↳↳↳↳ start_time | string | Giờ bắt đầu. |
| ↳↳↳↳↳ end_time | string | Giờ kết thúc. |
| ↳↳↳↳↳ date_type | string | Loại ngày (`DAY`, `WEEK`, `MONTH`). |
| ↳↳↳↳↳ num | number[] | Ngày áp dụng trong tuần hoặc tháng. |
| ↳↳ last_check_result_summary | object | Tóm tắt kết quả kiểm tra gần nhất. |
| ↳↳↳ task_exec_id | string | ID lượt thực thi tác vụ. |
| ↳↳↳ check_datetime | string | Thời gian kiểm tra. |
| ↳↳↳ exec_datetime | string | Thời gian thực thi. |
| ↳↳↳ no_change | number | Số đối tượng không đổi. |
| ↳↳↳ change_success | number | Số đối tượng thay đổi thành công. |
| ↳↳↳ change_fail | number | Số đối tượng thay đổi thất bại. |
| ↳ page | number | Trang hiện tại. |
| ↳ page_size | number | Kích thước trang. |

---

## Lấy kết quả thực thi quy tắc (`Get rule results`)
<a id="doc-1738769076676609"></a>
<!-- doc_id: 1738769076676609 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/list/`

**Mục đích**: Sử dụng endpoint này để lấy lịch sử kết quả thực thi của các quy tắc tự động trong một khoảng thời gian, bao gồm số lượng đối tượng được kiểm tra và số thay đổi thành công hoặc thất bại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| rule_id | string | Không bắt buộc | ID quy tắc cụ thể muốn xem kết quả. |
| start_time | string | Bắt buộc | Ngày bắt đầu khoảng thời gian truy vấn (`YYYY-MM-DD`). |
| end_time | string | Bắt buộc | Ngày kết thúc khoảng thời gian truy vấn (`YYYY-MM-DD`). |
| filtering | object | Không bắt buộc | Điều kiện lọc bổ sung. |
| ↳ data_dimension | string | Không bắt buộc | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳ action_type | string | Không bắt buộc | Loại hành động: `TURN_ON`, `TURN_OFF`, `MESSAGE`, `DAILY_BUDGET`, `LIFETIME_BUDGET`, `BID`. |
| ↳ status | string | Không bắt buộc | Trạng thái thực thi. |
| page | number | Không bắt buộc | Số trang hiện tại. Mặc định: 1. |
| page_size | number | Không bắt buộc | Kích thước trang. Mặc định: 10. |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN`, `JA`. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "start_time=2026-05-01" --data-urlencode "end_time=2026-05-30" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/list/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "start_time": "2026-05-01",
    "end_time": "2026-05-30",
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rules | object[] | Danh sách các kết quả thực thi quy tắc. |
| ↳↳ task_exec_id | string | ID lượt thực thi tác vụ quy tắc. |
| ↳↳ rule_id | string | ID quy tắc. |
| ↳↳ rule_info | object | Thông tin quy tắc. |
| ↳↳↳ name | string | Tên quy tắc. |
| ↳↳↳ rule_status | string | Trạng thái quy tắc: `ON`, `OFF`, `DELETED`. |
| ↳↳↳ create_datetime | string | Thời gian tạo. |
| ↳↳↳ apply_objects | object[] | Đối tượng áp dụng. |
| ↳↳↳↳ dimesion | string | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳↳↳ dimension_ids | string[] | Danh sách ID đối tượng. |
| ↳↳↳↳ bind_type | string | Loại liên kết: `BIND`, `UNBIND`. |
| ↳↳↳↳ pre_condition_type | string | Điều kiện tiền lọc. |
| ↳↳↳ conditions | object[] | Danh sách điều kiện. |
| ↳↳↳↳ subject_type | string | Chỉ số/tiêu chí điều kiện. |
| ↳↳↳↳ range_type | string | Khoảng thời gian dữ liệu. |
| ↳↳↳↳ match_type | string | Toán tử so sánh. |
| ↳↳↳↳ values | string[] | Giá trị so sánh. |
| ↳↳↳↳ calculation_type | string | Loại tính toán chi phí. |
| ↳↳↳ action | object | Hành động thực hiện. |
| ↳↳↳↳ subject_type | string | Loại hành động. |
| ↳↳↳↳ action_type | string | Thao tác điều chỉnh. |
| ↳↳↳↳ value_type | string | Đơn vị giá trị. |
| ↳↳↳↳ frequency_info | object | Tần suất hành động. |
| ↳↳↳↳↳ custom_frequency_type | string | Tần suất tùy chỉnh. |
| ↳↳↳↳↳ time | number | Tham số thời gian. |
| ↳↳↳↳↳ count | number | Số lần thực hiện. |
| ↳↳↳ notification | object | Cấu hình thông báo. |
| ↳↳↳↳ notification_type | string | Loại thông báo. |
| ↳↳↳↳ email_setting | object | Cài đặt email. |
| ↳↳↳↳↳ notification_period | string | Chu kỳ gửi email. |
| ↳↳↳↳↳ email_exec_time | string[] | Giờ gửi email. |
| ↳↳↳↳↳ no_result_notification | boolean | Gửi thông báo khi không có kết quả. |
| ↳↳↳ rule_exec_info | object | Lịch trình chạy quy tắc. |
| ↳↳↳↳ exec_time_type | string | Loại lịch chạy. |
| ↳↳↳↳ exec_time | string | Giờ chạy cụ thể. |
| ↳↳↳↳ time_period_info | object[] | Khoảng thời gian cụ thể. |
| ↳↳↳↳↳ start_time | string | Giờ bắt đầu. |
| ↳↳↳↳↳ end_time | string | Giờ kết thúc. |
| ↳↳↳↳↳ date_type | string | Loại ngày (`DAY`, `WEEK`, `MONTH`). |
| ↳↳↳↳↳ num | number[] | Ngày áp dụng trong tuần hoặc tháng. |
| ↳↳ last_check_result_summary | object | Tóm tắt kết quả kiểm tra gần nhất. |
| ↳↳↳ check_datetime | string | Thời gian kiểm tra. |
| ↳↳↳ exec_datetime | string | Thời gian thực thi. |
| ↳↳↳ no_change | number | Số lượng đối tượng không có thay đổi. |
| ↳↳↳ change_success | number | Số lượng đối tượng thay đổi thành công. |
| ↳↳↳ change_fail | number | Số lượng đối tượng thay đổi thất bại. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số kết quả. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy chi tiết kết quả thực thi (`Get result details`)
<a id="doc-1738769098314754"></a>
<!-- doc_id: 1738769098314754 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/get/`

**Mục đích**: Sử dụng endpoint này để xem chi tiết kết quả thực thi của từng đối tượng cụ thể (chiến dịch, nhóm quảng cáo hoặc quảng cáo) trong một lượt chạy tác vụ, bao gồm trạng thái thành công hay thất bại và thông báo lỗi tương ứng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| exec_id | string | Bắt buộc | ID lượt thực thi tác vụ (`task_exec_id`). |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN`, `JA`. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "exec_id=task_exec_123456789" https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/result/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "exec_id": "task_exec_123456789",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rule_id | string | ID quy tắc tự động. |
| ↳ result_details | object[] | Danh sách chi tiết kết quả thực thi trên từng đối tượng. |
| ↳↳ result_detail | object | Thông tin chi tiết kết quả. |
| ↳↳↳ object_dimension | string | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳↳ object_dimension_id | string | ID đối tượng (ví dụ ID nhóm quảng cáo). |
| ↳↳↳ object_name | string | Tên đối tượng. |
| ↳↳↳ action_subject_type | string | Loại hành động đã áp dụng (`TURN_ON`, `TURN_OFF`, `BID`, `DAILY_BUDGET`, v.v.). |
| ↳↳↳ status | string | Trạng thái thực thi: `SUCCESS` (thành công), `FAIL` (thất bại), `NO_CHANGE` (không thay đổi). |
| ↳↳↳ error_message | string | Thông báo lỗi nếu thực thi thất bại. |

---

## Cập nhật quy tắc tự động (`Update rules`)
<a id="doc-1738769123170306"></a>
<!-- doc_id: 1738769123170306 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/update/`

**Mục đích**: Sử dụng endpoint này để chỉnh sửa toàn bộ cấu hình của một hoặc nhiều quy tắc tự động hiện có, bao gồm tên, đối tượng áp dụng, điều kiện kích hoạt, hành động và lịch trình thực thi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| rules | object[] | Bắt buộc | Danh sách các quy tắc cần cập nhật. |
| ↳ rule_id | string | Bắt buộc | ID quy tắc tự động cần cập nhật. |
| ↳ name | string | Bắt buộc | Tên quy tắc tự động mới. |
| ↳ apply_objects | object[] | Bắt buộc | Danh sách đối tượng áp dụng quy tắc. |
| ↳↳ dimension | string | Bắt buộc | Cấp độ đối tượng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳↳ dimension_ids | string[] | Không bắt buộc | Danh sách ID đối tượng cụ thể. |
| ↳↳ pre_condition_type | string | Bắt buộc | Điều kiện tiền lọc đối tượng. |
| ↳ conditions | object[] | Bắt buộc | Danh sách điều kiện kích hoạt quy tắc. |
| ↳↳ subject_type | string | Bắt buộc | Chỉ số/tiêu chí điều kiện. |
| ↳↳ range_type | string | Không bắt buộc | Khoảng thời gian dữ liệu. |
| ↳↳ match_type | string | Không bắt buộc | Toán tử so sánh. |
| ↳↳ values | string[] | Không bắt buộc | Giá trị so sánh của điều kiện. |
| ↳↳ calculation_type | string | Không bắt buộc | Loại tính toán chi phí (`ALL_OBJECTS`, `OF_EACH_OBJECT`). |
| ↳ actions | object[] | Bắt buộc | Danh sách hành động thực hiện khi thỏa mãn điều kiện. |
| ↳↳ subject_type | string | Bắt buộc | Loại hành động: `TURN_ON`, `TURN_OFF`, `MESSAGE`, `DAILY_BUDGET`, `LIFETIME_BUDGET`, `BID`. |
| ↳↳ action_type | string | Không bắt buộc | Thao tác điều chỉnh: `INCREASE`, `DECREASE`, `ADJUST_TO`. |
| ↳↳ value_type | string | Không bắt buộc | Đơn vị giá trị: `EXACT`, `PERCENT`. |
| ↳↳ use_limit | boolean | Không bắt buộc | Có sử dụng giới hạn ngân sách / giá thầu hay không. |
| ↳↳ limit | float | Không bắt buộc | Giá trị giới hạn trần hoặc sàn. |
| ↳↳ frequency_info | object | Không bắt buộc | Cài đặt tần suất hành động. |
| ↳↳↳ custom_frequency_type | string | Không bắt buộc | Tần suất tùy chỉnh. |
| ↳↳↳ time | number | Không bắt buộc | Tham số thời gian `N`. |
| ↳↳↳ count | number | Không bắt buộc | Số lần `Y`. |
| ↳ notification | object | Bắt buộc | Cài đặt thông báo. |
| ↳↳ notification_type | string | Bắt buộc | Loại thông báo: `TASK_FINISH`, `ANY_CHANGES`, `NOT_NOTIFICATION`. |
| ↳↳ email_setting | object | Không bắt buộc | Cài đặt gửi email. |
| ↳↳↳ notification_period | string | Không bắt buộc | Chu kỳ gửi email. |
| ↳↳↳ email_exec_time | string[] | Không bắt buộc | Giờ gửi email. |
| ↳↳↳ no_result_notification | boolean | Không bắt buộc | Gửi thông báo khi không có kết quả. |
| ↳↳↳ mute_option | string | Không bắt buộc | Tắt tiếng thông báo: `MUTE`, `UNMUTE`. |
| ↳ rule_exec_info | object | Bắt buộc | Lịch trình chạy quy tắc. |
| ↳↳ exec_time_type | string | Bắt buộc | Loại lịch chạy. |
| ↳↳ exec_time | string | Không bắt buộc | Thời gian chạy cụ thể. |
| ↳↳ time_period_info | object[] | Không bắt buộc | Khoảng thời gian cụ thể. |
| ↳↳↳ start_time | string | Không bắt buộc | Giờ bắt đầu. |
| ↳↳↳ end_time | string | Không bắt buộc | Giờ kết thúc. |
| ↳↳↳ date_type | string | Không bắt buộc | Loại ngày (`DAY`, `WEEK`, `MONTH`). |
| ↳↳↳ num | number[] | Không bắt buộc | Ngày áp dụng trong tuần hoặc tháng. |
| ↳ tzone | string | Không bắt buộc | Múi giờ người dùng. |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN`, `JA`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "rules": [{
    "rule_id": "1738769999999999",
    "name": "Cập nhật tên quy tắc tự động",
    "apply_objects": [{
      "dimension": "ADGROUP",
      "pre_condition_type": "ALL_ACTIVE_AD_GROUP"
    }],
    "conditions": [{
      "subject_type": "CPA",
      "range_type": "TODAY",
      "match_type": "GT",
      "values": ["60.0"]
    }],
    "actions": [{
      "subject_type": "TURN_OFF"
    }],
    "notification": {
      "notification_type": "ANY_CHANGES"
    },
    "rule_exec_info": {
      "exec_time_type": "PER_HALF_HOUR"
    }
  }]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ rule_ids | string[] | Danh sách ID các quy tắc đã được cập nhật thành công. |

---

## Cập nhật trạng thái quy tắc (`Update the statuses of rules`)
<a id="doc-1738769144119298"></a>
<!-- doc_id: 1738769144119298 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/update/status/`

**Mục đích**: Sử dụng endpoint này để bật (enable), tắt (disable) hoặc xóa (delete) hàng loạt quy tắc tự động.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| rule_ids | string[] | Bắt buộc | Danh sách các ID quy tắc cần cập nhật trạng thái. Kích thước tối đa: 100 ID. |
| operate_type | string | Bắt buộc | Thao tác trạng thái cần thực hiện. Các giá trị enum:<br>• `ENABLE`: Bật quy tắc.<br>• `DISABLE`: Tắt quy tắc.<br>• `DELETE`: Xóa quy tắc. |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN`, `JA`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/update/status/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "rule_ids": ["1738769999999999"],
  "operate_type": "ENABLE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Liên kết / Hủy liên kết quy tắc (`Bind/Unbind rules`)
<a id="doc-1738769164954626"></a>
<!-- doc_id: 1738769164954626 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/batch_bind/`

**Mục đích**: Sử dụng endpoint này để liên kết thêm đối tượng mới vào quy tắc tự động hoặc gỡ bỏ liên kết đối tượng khỏi quy tắc mà không cần chỉnh sửa toàn bộ nội dung quy tắc.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| bind_info | object[] | Bắt buộc | Danh sách thông tin liên kết đối tượng. |
| ↳ rule_id | string | Bắt buộc | ID quy tắc tự động. |
| ↳ bind_type | string | Bắt buộc | Thao tác liên kết: `BIND` (gắn thêm đối tượng), `UNBIND` (gỡ bỏ đối tượng). |
| ↳ dimension | string | Bắt buộc | Cấp độ đối tượng áp dụng: `CAMPAIGN`, `ADGROUP`, `AD`. |
| ↳ dimension_ids | string[] | Bắt buộc | Danh sách ID đối tượng cụ thể cần gắn hoặc gỡ bỏ. |
| lang | string | Không bắt buộc | Ngôn ngữ thông báo lỗi: `ZH`, `EN`, `JA`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/optimizer/rule/batch_bind/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "bind_info": [{
    "rule_id": "1738769999999999",
    "bind_type": "BIND",
    "dimension": "ADGROUP",
    "dimension_ids": ["1723456789012345"]
  }]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202607290700180102440530181709ABE4",
  "data": {}
}
```
