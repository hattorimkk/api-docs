# Reach & Frequency

Reach & Frequency (R&F - Phạm vi tiếp cận & Tần suất) là loại hình mua chiến dịch quảng cáo cho phép các nhà quảng cáo trên TikTok For Business lập kế hoạch và đặt mua quảng cáo trước với lưu lượng và chi phí được đảm bảo. Để tìm hiểu thêm chi tiết và cách tạo chiến dịch R&F, xem [tại đây](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739470723315713).

> [!NOTE]
> Tính năng Reach & Frequency hiện đang ở giai đoạn phát hành rộng rãi (GA). Các nhà phát triển có thể xây dựng tích hợp với tính năng này. Tuy nhiên, các tích hợp sẽ chỉ hoạt động nếu tài khoản quảng cáo được đưa vào danh sách cho phép (allowlisted). Để đưa tài khoản vào allowlist, vui lòng liên hệ đại diện TikTok của bạn.

Nhóm này bao gồm các endpoint sau:
- [Lấy ước tính lượng tồn kho (Get inventory estimates)](57-reach-and-frequency.md#doc-1738235487941633)
- [Tạo nhóm quảng cáo R&F (Create an R&F ad group)](57-reach-and-frequency.md#doc-1738235338194945)
- [Cập nhật nhóm quảng cáo R&F (Update an R&F ad group)](57-reach-and-frequency.md#doc-1738235402874882)
- [Hủy đơn đặt hàng quảng cáo R&F (Cancel the R&F ad order)](57-reach-and-frequency.md#doc-1740489099367425)
- [Lấy thông tin ước tính của các nhóm quảng cáo R&F (Get estimated info of R&F ad groups)](57-reach-and-frequency.md#doc-1740489551354881)
- [Truy vấn hợp đồng (Query contracts)](57-reach-and-frequency.md#doc-1740489855138818)
- [Lấy múi giờ phân phối R&F (Get R&F time zones)](57-reach-and-frequency.md#doc-1740490147129345)

---

## Tổng quan Reach & Frequency (`Reach & Frequency`)
<a id="doc-1738235311704065"></a>
<!-- doc_id: 1738235311704065 -->

> Đường dẫn: API Reference > Reach & Frequency

Reach & Frequency (R&F) là loại hình mua quảng cáo hỗ trợ nhà quảng cáo TikTok For Business đặt trước lượng hiển thị và người tiếp cận theo tần suất mong muốn với ngân sách và CPM cố định.

Để xem chi tiết cách tạo và triển khai chiến dịch R&F, xem [Create a Reach & Frequency campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739470723315713).

> [!NOTE]
> Tính năng này yêu cầu tài khoản quảng cáo phải được duyệt vào danh sách cho phép (allowlist). Vui lòng liên hệ với người quản lý tài khoản TikTok của bạn để được hỗ trợ cấp quyền trước khi gọi API trên môi trường production.

Danh sách các endpoint trong nhóm:
* [Get inventory estimates](57-reach-and-frequency.md#doc-1738235487941633): Dự báo tồn kho quảng cáo dựa trên cấu hình nhắm mục tiêu và ngân sách.
* [Create an R&F ad group](57-reach-and-frequency.md#doc-1738235338194945): Tạo nhóm quảng cáo R&F và khóa tồn kho dự kiến.
* [Update an R&F ad group](57-reach-and-frequency.md#doc-1738235402874882): Chỉnh sửa cấu hình nhóm quảng cáo R&F.
* [Cancel the R&F ad order](57-reach-and-frequency.md#doc-1740489099367425): Rút lại / hủy đơn hàng R&F để dừng phân phối.
* [Get estimated info of R&F ad groups](57-reach-and-frequency.md#doc-1740489551354881): Truy vấn chi phí và phân bổ tần suất ước tính theo ngày.
* [Query contracts](57-reach-and-frequency.md#doc-1740489855138818): Tra cứu hợp đồng R&F thương mại khả dụng theo ngày.
* [Get R&F time zones](57-reach-and-frequency.md#doc-1740490147129345): Lấy múi giờ phân phối R&F theo mã quốc gia/khu vực.

---

## Lấy ước tính lượng tồn kho (`Get inventory estimates`)
<a id="doc-1738235487941633"></a>
<!-- doc_id: 1738235487941633 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/rf/inventory/estimate/`

**Mục đích**: Lấy dữ liệu dự báo tồn kho (inventory estimates) cho quảng cáo Reach & Frequency, bao gồm ngân sách, số lượt hiển thị, số người tiếp cận và CPM dự kiến.

Xem thêm [About Reach & Frequency - Inventory estimate](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1744571201117186) để tìm hiểu chi tiết về cơ chế ước tính tồn kho và ánh xạ giữa kết quả trả về từ endpoint này với giao diện TikTok Ads Manager.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token (mã truy cập) đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
> [!NOTE]
> Tham số `audience_info` là đối tượng JSON nên cần được serialize và URL-encode trong query string (ví dụ: `audience_info={"location_ids":["123"]}`).

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo (Advertiser ID). |
| `audience_info` | object | Có | Quy tắc nhắm mục tiêu đối tượng (Audience targeting rules). |
| ↳ `audience_ids` | string[] | Không | Danh sách ID tệp đối tượng tùy chỉnh cần nhắm tới. Đối với quảng cáo R&F, tệp đối tượng phải được tạo hoặc cập nhật với `audience_sub_type` đặt thành `REACH_FREQUENCY`. |
| ↳ `excluded_audience_ids` | string[] | Không | Danh sách ID tệp đối tượng cần loại trừ. Tệp phải có `audience_sub_type` là `REACH_FREQUENCY`. |
| ↳ `age_groups` | string[] | Không | Nhóm tuổi nhắm mục tiêu. Nếu vị trí nhắm mục tiêu gồm Israel hoặc Brazil, không được dùng `AGE_13_17`. Chi tiết enum xem tại [Enumeration - Audience Age Range](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `gender` | string | Không | Giới tính nhắm mục tiêu. Chi tiết enum xem tại [Enumeration - Audience Gender](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `languages` | string[] | Không | Ngôn ngữ nhắm mục tiêu. Chi tiết enum xem tại [Enumeration - Audience Language](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `location_ids` | string[] | Có | Danh sách ID vị trí nhắm mục tiêu (quốc gia/vùng lãnh thổ, tỉnh/thành, khu vực thị trường DMA). Chỉ hỗ trợ nhắm mục tiêu trong cùng một quốc gia/vùng lãnh thổ duy nhất. Xem danh sách mã tại **Location IDs**. |
| ↳ `operating_systems` | string[] | Không | Hệ điều hành. Chi tiết enum xem tại [Enumeration - Audience Operation System](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `network_types` | string[] | Không | Loại mạng kết nối. Mặc định: `unlimited`. Chi tiết enum xem tại [Enumeration - Audience Network Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `device_model_ids` | string[] | Không | Danh sách ID mẫu thiết bị nhắm mục tiêu (hiện chỉ hỗ trợ ID ở cấp độ thương hiệu brand-level). Khi truyền trường này, không được truyền `device_price_ranges`. Xem chi tiết tại [Device Models](70-tools-p1.md#doc-1737172880570369). Chỉ những thiết bị có `is_active` = `True` mới được dùng. |
| ↳ `device_price_ranges` | number[] | Không | Khoảng giá thiết bị (bội số của 50). `10000` biểu thị 1.000+.<br>> [!IMPORTANT]<br>> Giới hạn trên bạn thiết lập sẽ tự động cộng thêm 50 để làm giới hạn trên thực tế. Ví dụ thiết lập `[0, 250]` thì thực tế áp dụng là `[0, 300]`. |
| ↳ `carrier_ids` | string[] | Không | ID nhà mạng viễn thông. Sử dụng endpoint [/tool/carrier/](70-tools-p1.md#doc-1737168013095938) để lấy danh sách giá trị. |
| ↳ `interest_category_ids` | string[] | Không | Phân loại sở thích. Người dùng không khớp với sở thích sẽ bị loại trừ khi phân phối. Để trống nếu muốn nhắm tới tất cả. Dùng [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961) để lấy danh sách. |
| ↳ `brand_safety_type` | string | Không | Loại giải pháp an toàn thương hiệu. Mặc định: `NO_BRAND_SAFETY`. Giá trị enum:<br>• `NO_BRAND_SAFETY`: Không sử dụng giải pháp an toàn thương hiệu (toàn bộ kho quảng cáo).<br>• `EXPANDED_INVENTORY`: Kho quảng cáo mở rộng (đã loại bỏ hầu hết nội dung không phù hợp, không có chủ đề người lớn).<br>• `STANDARD_INVENTORY`: Kho quảng cáo tiêu chuẩn (nội dung phù hợp cho hầu hết thương hiệu).<br>• `LIMITED_INVENTORY`: Kho quảng cáo giới hạn (loại bỏ hoàn toàn nội dung nhạy cảm).<br>• `THIRD_PARTY`: Sử dụng giải pháp của bên thứ ba (yêu cầu allowlist).<br>Dùng [/tool/region/](70-tools-p1.md#doc-1737189539571713) để tra cứu quốc gia/khu vực hỗ trợ. |
| ↳ `contextual_tag_ids` | string[] | Không | Danh sách ID thẻ ngữ cảnh (contextual tags). Dùng [/tool/contextual_tag/get/](70-tools-p2.md#doc-1747747118654465) để lấy danh sách thẻ khả dụng (tính năng cần allowlist). Chỉ hỗ trợ mục tiêu `RF_REACH`. Không hỗ trợ khi `brand_safety_type` là `THIRD_PARTY` hoặc `feed_type` là `TOP_FEED`. Nếu chiến dịch là `PULSE`, bắt buộc phải truyền thẻ loại `PREMIUM`. |
| `schedule_start_time` | string | Có | Thời gian bắt đầu phân phối (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Giá trị HH:MM:SS phải tương đương với 00:00:00 theo múi giờ địa phương của khu vực nhắm mục tiêu.<br>> [!NOTE]<br>> Luôn sử dụng Giờ Chuẩn (Standard Time), bỏ qua Giờ Mùa Hè (Daylight Saving Time). |
| `schedule_end_time` | string | Có | Thời gian kết thúc phân phối (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Giá trị HH:MM:SS phải tương đương với 23:59:59 theo múi giờ địa phương của khu vực nhắm mục tiêu. Khoảng cách giữa `schedule_start_time` và `schedule_end_time` không được vượt quá **30 ngày**. |
| `frequency` | number | Có | Tần suất hiển thị. Kết hợp với `frequency_schedule` để giới hạn số lần quảng cáo hiển thị tới một người dùng.<br>Ví dụ: `frequency` = 2 và `frequency_schedule` = 3 nghĩa là quảng cáo hiển thị tối đa 2 lần trong mỗi 3 ngày.<br>Điều kiện bắt buộc:<br>• 1 ≤ `frequency` ≤ `frequency_schedule`<br>• 1 ≤ `frequency_schedule` ≤ min(`schedule_end_time` - `schedule_start_time`, 30)<br>• Tần suất trung bình không vượt quá 4 lần/ngày. |
| `frequency_schedule` | number | Có | Chu kỳ tần suất (tính theo ngày). Xem quy tắc tại trường `frequency`. |
| `objective_type` | string | Có | Mục tiêu quảng cáo. Giá trị enum: `RF_REACH`. |
| `cpv_video_duration` | string | Không | Thời lượng xem video mục tiêu. Giá trị enum: `SIX_SECONDS`, `TWO_SECONDS`. |
| `feed_type` | string | Không | Tùy chọn nguồn cấp dữ liệu. Giá trị enum:<br>• `STANDARD_FEED`: Nguồn cấp tiêu chuẩn (lượng tồn kho lớn, giá CPM thông thường).<br>• `TOP_FEED`: Nguồn cấp Top Feed (lượng tồn kho giới hạn, giá CPM cao hơn). |
| `rf_purchased_type` | string | Không | Loại hình mua quảng cáo. Giá trị enum:<br>• `FIXED_SHOW`: Mua theo số lượt hiển thị cố định.<br>• `FIXED_REACH`: Mua theo số lượng người tiếp cận cố định.<br>• `FIXED_BUDGET`: Mua theo ngân sách cố định. |
| `budget` | float | Điều kiện | Ngân sách. Bắt buộc khi `rf_purchased_type` = `FIXED_BUDGET`. |
| `purchased_impression` | number | Điều kiện | Số lượt hiển thị muốn mua, **tính theo đơn vị 1.000 lượt** (ví dụ 100 nghĩa là 100.000 lượt). Bắt buộc khi `rf_purchased_type` = `FIXED_SHOW`. |
| `purchased_reach` | number | Điều kiện | Số lượng người tiếp cận muốn mua, **tính theo đơn vị 1.000 người**. Bắt buộc khi `rf_purchased_type` = `FIXED_REACH`. |
| `rf_campaign_type` | string | Không | Khi `objective_type` là `RF_REACH`, dùng trường này để thiết lập chiến dịch là TikTok Pulse để nhận các thẻ ngữ cảnh cao cấp. Giá trị enum: `STANDARD` (chiến dịch R&F tiêu chuẩn), `PULSE` (chiến dịch TikTok Pulse). Nếu chọn `PULSE`, chỉ có một `location_id` được trả về. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Trả về `0` khi thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `default_result` | object | Kết quả dự báo tồn kho theo giá trị cố định bạn đã chỉ định (`purchased_impression`, `budget` hoặc `purchased_reach`). |
| ↳↳ `base_info` | object | Thông tin cơ bản của kết quả dự báo. |
| ↳↳↳ `budget` | float | Tổng ngân sách ước tính. |
| ↳↳↳ `cpm` | float | Chi phí cho mỗi 1.000 lượt hiển thị (CPM = `budget` / `impression`). |
| ↳↳↳ `impression` | number | Tổng lượt hiển thị dự kiến, **đơn vị 1.000 lượt** (ví dụ 110 biểu thị 110.000 lượt hiển thị). |
| ↳↳↳ `reach` | number | Tổng số người tiếp cận dự kiến, **đơn vị 1.000 người** (ví dụ 110 biểu thị 110.000 người). |
| ↳↳↳ `max_reach` | number | Tổng số người tiếp cận tối đa có thể đặt trước dựa trên loại feed, thiết lập nhắm mục tiêu và thời lượng chiến dịch, **đơn vị 1.000 người**. |
| ↳↳↳ `average_frequency` | float | Tần suất hiển thị trung bình trên mỗi người (`average_frequency` = `impression` / `reach`). |
| ↳↳ `daily_cost` | object[] | Chi phí tiêu thụ dự kiến theo từng ngày. |
| ↳↳↳ `date` | string | Ngày, định dạng `"YYYY-MM-DD"`. |
| ↳↳↳ `cost` | float | Chi phí dự kiến trong ngày đó. |
| ↳↳ `frequency_per_person` | object[] | Phân phối số lần hiển thị trên mỗi người dùng. |
| ↳↳↳ `frequency` | number | Số lần hiển thị trên mỗi người. |
| ↳↳↳ `percentage` | float | Tỷ lệ phần trăm người dùng đạt mức tần suất đó (ví dụ `0.423` nghĩa là khoảng 42,3% người dùng sẽ thấy quảng cáo ở mức tần suất này). |
| ↳ `results` | object[] | Kết quả dự báo tồn kho cho các mức ngân sách khác nhau. Cấu trúc mỗi object tương tự như `default_result` (gồm `base_info`, `daily_cost`, `frequency_per_person`). |

### Ví dụ

#### curl
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/rf/inventory/estimate/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'objective_type=RF_REACH' \
  --data-urlencode 'audience_info={"location_ids":["6252001"]}' \
  --data-urlencode 'schedule_start_time=2025-03-01 05:00:00' \
  --data-urlencode 'schedule_end_time=2025-03-10 04:59:59' \
  --data-urlencode 'frequency=2' \
  --data-urlencode 'frequency_schedule=3' \
  --data-urlencode 'rf_purchased_type=FIXED_BUDGET' \
  --data-urlencode 'budget=10000'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/rf/inventory/estimate/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "objective_type": "RF_REACH",
    "audience_info": json.dumps({
        "location_ids": ["6252001"],
        "gender": "GENDER_FEMALE",
        "age_groups": ["AGE_18_24", "AGE_25_34"]
    }),
    "schedule_start_time": "2025-03-01 05:00:00",
    "schedule_end_time": "2025-03-10 04:59:59",
    "frequency": 2,
    "frequency_schedule": 3,
    "rf_purchased_type": "FIXED_BUDGET",
    "budget": 5000.0
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201015300102452431071406593C",
    "data": {
        "default_result": {
            "base_info": {
                "budget": 14202.37,
                "cpm": 2.75,
                "impression": 5157,
                "reach": 2991,
                "max_reach": 17291,
                "average_frequency": 1.72
            },
            "daily_cost": [
                {
                    "date": "2025-03-01",
                    "cost": 3587.52
                },
                {
                    "date": "2025-03-02",
                    "cost": 3565.18
                }
            ],
            "frequency_per_person": [
                {
                    "frequency": 1,
                    "percentage": 0.28
                },
                {
                    "frequency": 2,
                    "percentage": 0.72
                }
            ]
        },
        "results": [
            {
                "base_info": {
                    "budget": 659.8,
                    "cpm": 1.58,
                    "impression": 418,
                    "reach": 239,
                    "average_frequency": 1.75
                },
                "daily_cost": [
                    {
                        "date": "2025-03-01",
                        "cost": 163.09
                    }
                ],
                "frequency_per_person": [
                    {
                        "frequency": 1,
                        "percentage": 0.248
                    },
                    {
                        "frequency": 2,
                        "percentage": 0.752
                    }
                ]
            }
        ]
    }
}
```


---

## Tạo nhóm quảng cáo R&F (`Create an R&F ad group`)
<a id="doc-1738235338194945"></a>
<!-- doc_id: 1738235338194945 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/create/`

**Mục đích**: Tạo một nhóm quảng cáo Reach & Frequency (R&F) và đặt trước lượng tồn kho quảng cáo.

Xem thêm hướng dẫn chi tiết tại [Create a Reach & Frequency campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1744571205201922).

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST: JSON body)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `request_id` | string | Có | ID yêu cầu để hỗ trợ tính năng lưu giữ trạng thái trùng lặp (idempotency), tránh gửi hai lần cùng một yêu cầu tạo nhóm. Giá trị là chuỗi số nguyên 64-bit (ví dụ: `"1234567890123"`). |
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `campaign_id` | string | Có | ID chiến dịch mà nhóm quảng cáo này trực thuộc. |
| `adgroup_name` | string | Có | Tên nhóm quảng cáo. Tối đa 100 ký tự, không chứa biểu tượng cảm xúc (emoji). |
| `promotion_type` | string | Có | Loại đối tượng quảng bá. Giá trị enum: `APP_ANDROID`, `APP_IOS`, `WEBSITE`, `WEBSITE_OR_DISPLAY`. Nếu `objective_type` là `RF_REACH`, hãy chọn `WEBSITE_OR_DISPLAY`. |
| `share_disabled` | boolean | Không | Có vô hiệu hóa tính năng chia sẻ quảng cáo sang các nền tảng bên thứ ba hay không. Mặc định: `false`. |
| `comment_disabled` | boolean | Không | Có cấm người dùng bình luận vào quảng cáo trên TikTok hay không. Mặc định: `false`. |
| `video_download_disabled` | boolean | Không | Có cấm người dùng tải video quảng cáo trên TikTok về máy hay không. Mặc định: `false`. *(Không thể chỉnh sửa sau khi tạo)*. |
| `optimization_event` | string | Không | Sự kiện chuyển đổi cho nhóm quảng cáo. Bắt buộc khi quảng bá ứng dụng có tracking URL. Xem [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) hoặc dùng [/app/external_action/](43-events-1-0-p1.md#doc-1740859338750977). |
| `app_id` | string | Không | ID của ứng dụng di động được quảng bá. |
| `audience_ids` | string[] | Không | Danh sách ID tệp đối tượng tùy chỉnh cần nhắm mục tiêu. Tệp phải được tạo với `audience_sub_type` là `REACH_FREQUENCY`. Không hỗ trợ tệp tương tự (Lookalike Audience). |
| `excluded_audience_ids` | string[] | Không | Danh sách ID tệp đối tượng cần loại trừ (`audience_sub_type` = `REACH_FREQUENCY`). Không hỗ trợ Lookalike Audience. |
| `age_groups` | string[] | Không | Nhóm tuổi nhắm mục tiêu. Nếu vị trí nhắm mục tiêu gồm Israel hoặc Brazil, không được dùng `AGE_13_17`. Xem chi tiết enum tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Tại Mỹ, việc nhắm tới 13–17 tuổi có các hạn chế riêng, xem [New age restrictions for ads on TikTok](../15-appendix/phu-luc-p1.md#doc-1788755983247362). |
| `gender` | string | Không | Giới tính nhắm mục tiêu. Giá trị enum: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. Xem [Enumeration - Audience Gender](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `languages` | string[] | Không | Danh sách mã ngôn ngữ nhắm mục tiêu. Xem [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `location_ids` | string[] | Có | Danh sách ID vị trí nhắm mục tiêu. Tất cả ID phải thuộc cùng một quốc gia hoặc khu vực. Xem **Location IDs**. |
| `is_hfss` | boolean | Không | Nội dung quảng bá có phải là thực phẩm HFSS (nhiều chất béo, muối hoặc đường) hay không. Lưu ý thị trường châu Âu cấm quảng cáo thực phẩm HFSS cho người chưa thành niên. |
| `operating_systems` | string[] | Không | Hệ điều hành thiết bị nhắm mục tiêu. Giá trị enum: `ANDROID`, `IOS`, `PC`. |
| `network_types` | string[] | Không | Loại kết nối mạng. Mặc định: `unlimited`. Xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `device_model_ids` | string[] | Không | ID mẫu thiết bị nhắm mục tiêu (hỗ trợ cấp độ thương hiệu). Xem [Device Models](70-tools-p1.md#doc-1737172880570369). |
| `device_price_ranges` | number[] | Không | Khoảng giá thiết bị (bội số của 50). `10000` biểu thị 1.000+. Giới hạn trên thực tế sẽ được cộng thêm 50. |
| `carrier_ids` | string[] | Không | Danh sách ID nhà mạng viễn thông. Nhà mạng chỉ hợp lệ khi `in_use` = `true`. Xem [/tool/carrier/](70-tools-p1.md#doc-1737168013095938). |
| `interest_category_ids` | string[] | Không | Danh mục sở thích nhắm mục tiêu. Xem [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). |
| `rf_purchased_type` | string | Không | Loại hình mua quảng cáo. Giá trị enum:<br>• `FIXED_SHOW`: Mua theo số lượt hiển thị cố định.<br>• `FIXED_REACH`: Mua theo số lượng người tiếp cận cố định.<br>• `FIXED_BUDGET`: Mua theo ngân sách cố định. |
| `budget` | float | Không | Ngân sách. Điền số tiền này dựa trên dữ liệu trả về từ API dự báo tồn kho [/rf/inventory/estimate/](57-reach-and-frequency.md#doc-1738235487941633). |
| `purchased_impression` | number | Không | Số lượt hiển thị đặt mua, **tính theo đơn vị 1.000 lượt**. |
| `purchased_reach` | number | Không | Số lượng người tiếp cận đặt mua, **tính theo đơn vị 1.000 người**. |
| `schedule_start_time` | string | Không | Thời gian bắt đầu phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| `schedule_end_time` | string | Không | Thời gian kết thúc phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| `frequency` | number | Không | Tần suất hiển thị quảng cáo tới mỗi người dùng. Kết hợp với `frequency_schedule`. |
| `frequency_schedule` | number | Không | Chu kỳ tần suất (tính bằng số ngày). |
| `optimization_goal` | string | Không | Mục tiêu tối ưu hóa kết quả. Phải khớp với `objective_type` của chiến dịch. Giá trị enum: `REACH`, `VIDEO_VIEW`, `CLICK`, `POST_ENGAGEMENT`, `INSTALL`. |
| `cpv_video_duration` | string | Không | Thời lượng xem video mục tiêu. Giá trị enum: `SIX_SECONDS`. |
| `brand_safety_type` | string | Không | Loại an toàn thương hiệu. Giá trị enum: `NO_BRAND_SAFETY`, `EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`, `THIRD_PARTY`. |
| `brand_safety_partner` | string | Không | Đối tác an toàn thương hiệu bên thứ ba khi `brand_safety_type` là `THIRD_PARTY`. Giá trị enum: `IAS`, `OPEN_SLATE` (DoubleVerify). |
| `category_exclusion_ids` | string[] | Không | ID các danh mục loại trừ nội dung. |
| `feed_type` | string | Không | Tùy chọn nguồn cấp dữ liệu: `STANDARD_FEED`, `TOP_FEED`. |
| `delivery_mode` | string | Không | Chiến lược lập lịch và sắp xếp phân phối quảng cáo. Giá trị enum:<br>• `STANDARD`: Phân phối tiêu chuẩn đồng đều.<br>• `SCHEDULE`: Phân phối theo lịch trình cụ thể (bắt buộc truyền `schedules` trong `schedule_infos`).<br>• `SEQUENCE`: Phân phối tuần tự theo thứ tự (bắt buộc truyền `expected_orders` trong `schedule_infos`).<br>• `VIEW_OPTIMIZE`: Tối ưu hóa lượt xem video 6 giây.<br>• `OPTIMIZE` *(deprecated)*: Tối ưu hiệu suất. |
| `schedule_infos` | object[] | Không | Thông tin phân phối quảng cáo. Khi `delivery_mode` là `SEQUENCE`, số lượng object biểu thị số quảng cáo được chỉ định thứ tự. |
| ↳ `schedules` | object[] | Điều kiện | Bắt buộc khi `delivery_mode` là `SCHEDULE`. Chi tiết khung giờ phân phối cho từng quảng cáo (phải liên tục và bao phủ trọn vẹn khoảng thời gian của nhóm). |
| ↳↳ `start_time` | string | Không | Thời gian bắt đầu phân phối của quảng cáo, định dạng `"YYYY-MM-DD HH:MM:SS"`. |
| ↳↳ `end_time` | string | Không | Thời gian kết thúc phân phối của quảng cáo, định dạng `"YYYY-MM-DD HH:MM:SS"`. |
| ↳ `expected_orders` | number[] | Điều kiện | Bắt buộc khi `delivery_mode` là `SEQUENCE`. Thứ tự hiển thị quảng cáo trong nhóm (ví dụ: `[1]` biểu thị quảng cáo này phân phối đầu tiên). |
| `contextual_tag_ids` | string[] | Không | Danh sách ID thẻ ngữ cảnh. Không hỗ trợ với `THIRD_PARTY` hoặc `TOP_FEED`. Nếu chiến dịch là `PULSE`, bắt buộc phải chứa thẻ loại `PREMIUM`. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳ `campaign_id` | string | ID chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳ `adgroup_id` | string | ID của nhóm quảng cáo R&F vừa được tạo thành công. |
| ↳ `adgroup_name` | string | Tên nhóm quảng cáo. |
| ↳ `promotion_type` | string | Loại đối tượng quảng bá. |
| ↳ `share_disabled` | boolean | Trạng thái vô hiệu hóa chia sẻ. |
| ↳ `comment_disabled` | boolean | Trạng thái vô hiệu hóa bình luận. |
| ↳ `video_download_disabled` | boolean | Trạng thái vô hiệu hóa tải video. |
| ↳ `optimization_event` | string | Sự kiện tối ưu hóa. |
| ↳ `app_id` | string | ID ứng dụng di động được quảng bá. |
| ↳ `audience_ids` | string[] | Danh sách ID tệp đối tượng nhắm mục tiêu. |
| ↳ `excluded_audience_ids` | string[] | Danh sách ID tệp đối tượng loại trừ. |
| ↳ `age_groups` | string[] | Danh sách nhóm tuổi nhắm mục tiêu. |
| ↳ `gender` | string | Giới tính nhắm mục tiêu. |
| ↳ `languages` | string[] | Danh sách mã ngôn ngữ nhắm mục tiêu. |
| ↳ `location_ids` | string[] | Danh sách ID vị trí nhắm mục tiêu. |
| ↳ `is_hfss` | boolean | Có phải thực phẩm HFSS hay không. |
| ↳ `operating_systems` | string[] | Hệ điều hành thiết bị nhắm mục tiêu. |
| ↳ `network_types` | string[] | Loại kết nối mạng nhắm mục tiêu. |
| ↳ `device_model_ids` | string[] | Danh sách ID mẫu thiết bị nhắm mục tiêu. |
| ↳ `device_price_ranges` | number[] | Khoảng giá thiết bị nhắm mục tiêu. |
| ↳ `carrier_ids` | string[] | Danh sách ID nhà mạng viễn thông. |
| ↳ `interest_category_ids` | string[] | Danh mục sở thích nhắm mục tiêu. |
| ↳ `rf_purchased_type` | string | Loại hình mua quảng cáo (`FIXED_SHOW`, `FIXED_REACH`, `FIXED_BUDGET`). |
| ↳ `budget` | float | Ngân sách nhóm quảng cáo. |
| ↳ `purchased_impression` | number | Số lượt hiển thị đặt mua, đơn vị 1.000 lượt. |
| ↳ `purchased_reach` | number | Số người tiếp cận đặt mua, đơn vị 1.000 người. |
| ↳ `schedule_start_time` | string | Thời gian bắt đầu phân phối (UTC+0). |
| ↳ `schedule_end_time` | string | Thời gian kết thúc phân phối (UTC+0). |
| ↳ `frequency` | number | Tần suất hiển thị. |
| ↳ `frequency_schedule` | number | Chu kỳ tần suất (ngày). |
| ↳ `optimization_goal` | string | Mục tiêu tối ưu hóa. |
| ↳ `cpv_video_duration` | string | Thời lượng xem video CPV mục tiêu. |
| ↳ `brand_safety_type` | string | Loại an toàn thương hiệu. |
| ↳ `brand_safety_partner` | string | Đối tác an toàn thương hiệu. |
| ↳ `category_exclusion_ids` | string[] | Danh mục loại trừ nội dung. |
| ↳ `feed_type` | string | Tùy chọn nguồn cấp dữ liệu (`STANDARD_FEED`, `TOP_FEED`). |
| ↳ `delivery_mode` | string | Chiến lược phân phối (`STANDARD`, `SCHEDULE`, `SEQUENCE`, `VIEW_OPTIMIZE`). |
| ↳ `schedule_infos` | object[] | Danh sách thông tin phân phối chi tiết. |
| ↳↳ `schedules` | object[] | Chi tiết lịch trình phân phối. |
| ↳↳↳ `start_time` | string | Thời gian bắt đầu phân phối. |
| ↳↳↳ `end_time` | string | Thời gian kết thúc phân phối. |
| ↳↳ `expected_orders` | number[] | Thứ tự phân phối quảng cáo trong nhóm. |
| ↳↳ `is_draft` | boolean | Trạng thái thông tin phân phối có đang ở chế độ bản nháp (chưa gắn với quảng cáo cụ thể nào) hay không. |
| ↳↳ `schedule_id` | string | ID lịch trình. Truyền giá trị này vào tham số `schedule_id` khi tạo quảng cáo qua [/ad/create/](02-ads-p1.md#doc-1739953377508354). Khi đã gắn thành công với quảng cáo, `is_draft` sẽ chuyển sang `false` và `schedule_id` sẽ nhận giá trị ID của quảng cáo. |
| ↳ `notice` | string | Thông báo hệ thống. |
| ↳ `contextual_tag_ids` | string[] | Danh sách ID thẻ ngữ cảnh. |

### Ví dụ

#### curl
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/create/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "request_id": "16892348923489234",
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1723456789012345",
    "adgroup_name": "RF_Brand_Awareness_Q1",
    "promotion_type": "WEBSITE_OR_DISPLAY",
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "age_groups": ["AGE_18_24", "AGE_25_34"],
    "schedule_start_time": "2025-03-01 05:00:00",
    "schedule_end_time": "2025-03-10 04:59:59",
    "frequency": 2,
    "frequency_schedule": 3,
    "rf_purchased_type": "FIXED_BUDGET",
    "budget": 5000.0,
    "feed_type": "STANDARD_FEED",
    "delivery_mode": "STANDARD",
    "optimization_goal": "REACH"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
CAMPAIGN_ID = "1723456789012345"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "request_id": "98765432101234567",
    "advertiser_id": ADVERTISER_ID,
    "campaign_id": CAMPAIGN_ID,
    "adgroup_name": "RF_Vietnam_Campaign_AdGroup",
    "promotion_type": "WEBSITE_OR_DISPLAY",
    "location_ids": ["6252001"],
    "schedule_start_time": "2025-03-01 05:00:00",
    "schedule_end_time": "2025-03-10 04:59:59",
    "frequency": 2,
    "frequency_schedule": 3,
    "rf_purchased_type": "FIXED_BUDGET",
    "budget": 5000.0,
    "feed_type": "STANDARD_FEED",
    "delivery_mode": "STANDARD",
    "optimization_goal": "REACH"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Create R&F adgroup response:", data)
if data.get("code") == 0:
    print(f"Created successfully. Ad Group ID: {data['data']['adgroup_id']}")
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201120000102452431071406594D",
    "data": {
        "advertiser_id": "7123456789012345678",
        "campaign_id": "1723456789012345",
        "adgroup_id": "1723456789099888",
        "adgroup_name": "RF_Brand_Awareness_Q1",
        "promotion_type": "WEBSITE_OR_DISPLAY",
        "location_ids": ["6252001"],
        "budget": 5000.0,
        "rf_purchased_type": "FIXED_BUDGET",
        "purchased_impression": 1818,
        "purchased_reach": 1050,
        "schedule_start_time": "2025-03-01 05:00:00",
        "schedule_end_time": "2025-03-10 04:59:59",
        "frequency": 2,
        "frequency_schedule": 3,
        "optimization_goal": "REACH",
        "delivery_mode": "STANDARD",
        "feed_type": "STANDARD_FEED",
        "notice": ""
    }
}
```


---

## Cập nhật nhóm quảng cáo R&F (`Update an R&F ad group`)
<a id="doc-1738235402874882"></a>
<!-- doc_id: 1738235402874882 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/update/`

**Mục đích**: Cập nhật thông tin và cấu hình nhắm mục tiêu cho nhóm quảng cáo Reach & Frequency (R&F) đã tạo.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST: JSON body)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `adgroup_id` | string | Có | ID của nhóm quảng cáo R&F cần cập nhật. Chiến dịch trực thuộc phải có `objective_type` là `RF_REACH`. |
| `adgroup_name` | string | Không | Tên mới của nhóm quảng cáo (tối đa 100 ký tự, không chứa emoji). |
| `share_disabled` | boolean | Không | Vô hiệu hóa tính năng chia sẻ quảng cáo sang bên thứ ba. |
| `comment_disabled` | boolean | Không | Vô hiệu hóa bình luận của người dùng trên TikTok. |
| `audience_ids` | string[] | Không | Danh sách ID tệp đối tượng tùy chỉnh cần nhắm mục tiêu (`audience_sub_type` = `REACH_FREQUENCY`). Không dùng Lookalike. |
| `excluded_audience_ids` | string[] | Không | Danh sách ID tệp đối tượng cần loại trừ (`audience_sub_type` = `REACH_FREQUENCY`). Không dùng Lookalike. |
| `age_groups` | string[] | Không | Nhóm tuổi nhắm mục tiêu. Chi tiết enum xem tại [Enumeration - Audience Age Range](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `gender` | string | Không | Giới tính nhắm mục tiêu. Xem [Enumeration - Audience Gender](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `languages` | string[] | Không | Danh sách mã ngôn ngữ nhắm mục tiêu. Xem [Enumeration - Audience Language](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `location_ids` | string[] | Không | Danh sách ID vị trí nhắm mục tiêu (trong cùng một quốc gia/khu vực). Xem [Reach & Frequency](57-reach-and-frequency.md#doc-1738235311704065). |
| `is_hfss` | boolean | Không | Nội dung quảng bá có phải là thực phẩm HFSS hay không. |
| `operating_systems` | string[] | Không | Hệ điều hành thiết bị nhắm mục tiêu. Xem [Enumeration - Audience Operating System](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `network_types` | string[] | Không | Loại kết nối mạng nhắm mục tiêu. Mặc định: `unlimited`. |
| `device_model_ids` | string[] | Không | ID mẫu thiết bị nhắm mục tiêu (cấp thương hiệu). Khi truyền trường này, không được truyền `device_price_ranges`. Xem [Device Models](70-tools-p1.md#doc-1737172880570369). |
| `device_price_ranges` | number[] | Không | Khoảng giá thiết bị (bội số của 50). Giới hạn trên thực tế sẽ được cộng thêm 50. |
| `carrier_ids` | string[] | Không | Danh sách ID nhà mạng viễn thông. Xem [Appendix - Carriers](70-tools-p1.md#doc-1737168013095938). |
| `interest_category_ids` | string[] | Không | Danh mục sở thích nhắm mục tiêu. Xem [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). |
| `rf_purchased_type` | string | Không | Loại hình mua quảng cáo: `FIXED_SHOW`, `FIXED_REACH`, `FIXED_BUDGET`. |
| `budget` | float | Không | Ngân sách nhóm quảng cáo. Điền theo kết quả từ API dự báo tồn kho. |
| `purchased_impression` | number | Không | Số lượt hiển thị đặt mua, **đơn vị 1.000 lượt**. Điền theo kết quả dự báo tồn kho. |
| `purchased_reach` | number | Không | Số người tiếp cận đặt mua, **đơn vị 1.000 người**. Điền theo kết quả dự báo tồn kho. |
| `schedule_start_time` | string | Không | Thời gian bắt đầu phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. Khoảng cách với `schedule_end_time` tối đa 90 ngày. Phút và giây phải là `00:00` theo múi giờ địa phương. |
| `schedule_end_time` | string | Không | Thời gian kết thúc phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. Khoảng cách với `schedule_start_time` tối đa 90 ngày. Phút và giây phải là `59:59` theo múi giờ địa phương. |
| `frequency` | number | Không | Tần suất hiển thị quảng cáo tới mỗi người. Kết hợp với `frequency_schedule`. |
| `frequency_schedule` | number | Không | Chu kỳ tần suất (ngày). |
| `feed_type` | string | Không | Nguồn cấp dữ liệu: `STANDARD_FEED`, `TOP_FEED`. |
| `delivery_mode` | string | Không | Chiến lược phân phối: `STANDARD`, `SCHEDULE`, `SEQUENCE`, `VIEW_OPTIMIZE`, `OPTIMIZE`. |
| `schedule_infos` | object[] | Không | Thông tin phân phối chi tiết. |
| ↳ `schedules` | object[] | Điều kiện | Bắt buộc khi `delivery_mode` là `SCHEDULE`. Lịch trình phân phối chi tiết. |
| ↳↳ `start_time` | string | Không | Thời gian bắt đầu phân phối của quảng cáo, định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ `end_time` | string | Không | Thời gian kết thúc phân phối của quảng cáo, định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳ `expected_orders` | number[] | Điều kiện | Bắt buộc khi `delivery_mode` là `SEQUENCE`. Thứ tự hiển thị quảng cáo trong nhóm (ví dụ: `[1]`). |
| `contextual_tag_ids` | string[] | Không | Danh sách ID thẻ ngữ cảnh. Xem [/tool/contextual_tag/get/](70-tools-p2.md#doc-1747747118654465). |
| `brand_safety_type` | string | Không | Loại an toàn thương hiệu: `EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`. (Tính năng cần allowlist). |
| `category_exclusion_ids` | string[] | Không | Danh sách ID danh mục nội dung loại trừ. Chỉ có thể cập nhật khi nhóm chưa đến giờ chạy hoặc đã đến giờ chạy nhưng đang ở trạng thái `DISABLE` và chi phí bằng 0. Dùng [/tool/content_exclusion/get/](70-tools-p2.md#doc-1769738074686465) để lấy danh sách. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳ `campaign_id` | string | ID chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳ `adgroup_id` | string | ID nhóm quảng cáo R&F vừa cập nhật. |
| ↳ `share_disabled` | boolean | Trạng thái vô hiệu hóa chia sẻ quảng cáo. |
| ↳ `adgroup_name` | string | Tên nhóm quảng cáo. |
| ↳ `promotion_type` | string | Loại đối tượng quảng bá. |
| ↳ `optimization_event` | string | Sự kiện tối ưu hóa. |
| ↳ `app_id` | string | ID ứng dụng di động được quảng bá. |
| ↳ `comment_disabled` | boolean | Trạng thái vô hiệu hóa bình luận. |
| ↳ `audience_ids` | string[] | Danh sách ID tệp đối tượng nhắm mục tiêu. |
| ↳ `excluded_audience_ids` | string[] | Danh sách ID tệp đối tượng loại trừ. |
| ↳ `age_groups` | string[] | Nhóm tuổi nhắm mục tiêu. |
| ↳ `gender` | string | Giới tính nhắm mục tiêu. |
| ↳ `languages` | string[] | Danh sách mã ngôn ngữ nhắm mục tiêu. |
| ↳ `location_ids` | string[] | Danh sách ID vị trí nhắm mục tiêu. |
| ↳ `is_hfss` | boolean | Có phải thực phẩm HFSS hay không. |
| ↳ `operating_systems` | string[] | Hệ điều hành thiết bị nhắm mục tiêu. |
| ↳ `network_types` | string[] | Loại kết nối mạng nhắm mục tiêu. |
| ↳ `device_model_ids` | string[] | Danh sách ID mẫu thiết bị nhắm mục tiêu. |
| ↳ `device_price_ranges` | number[] | Khoảng giá thiết bị nhắm mục tiêu. |
| ↳ `carrier_ids` | string[] | Danh sách ID nhà mạng viễn thông. |
| ↳ `interest_category_ids` | string[] | Danh mục sở thích nhắm mục tiêu. |
| ↳ `rf_purchased_type` | string | Loại hình mua quảng cáo (`FIXED_SHOW`, `FIXED_REACH`, `FIXED_BUDGET`). |
| ↳ `budget` | float | Ngân sách nhóm quảng cáo. |
| ↳ `purchased_impression` | number | Số lượt hiển thị đặt mua, **đơn vị 1.000 lượt**. |
| ↳ `purchased_reach` | number | Số người tiếp cận đặt mua, **đơn vị 1.000 người**. |
| ↳ `schedule_start_time` | string | Thời gian bắt đầu phân phối (UTC+0). |
| ↳ `schedule_end_time` | string | Thời gian kết thúc phân phối (UTC+0). |
| ↳ `frequency` | number | Tần suất hiển thị. |
| ↳ `frequency_schedule` | number | Chu kỳ tần suất (ngày). |
| ↳ `optimization_goal` | string | Mục tiêu tối ưu hóa. |
| ↳ `cpv_video_duration` | string | Thời lượng xem video CPV mục tiêu. |
| ↳ `brand_safety_type` | string | Loại an toàn thương hiệu. |
| ↳ `brand_safety_partner` | string | Đối tác an toàn thương hiệu. |
| ↳ `category_exclusion_ids` | string[] | Danh mục loại trừ nội dung. |
| ↳ `video_download_disabled` | boolean | Trạng thái vô hiệu hóa tải video. |
| ↳ `feed_type` | string | Tùy chọn nguồn cấp dữ liệu (`STANDARD_FEED`, `TOP_FEED`). |
| ↳ `delivery_mode` | string | Chiến lược phân phối (`STANDARD`, `SCHEDULE`, `SEQUENCE`, `VIEW_OPTIMIZE`). |
| ↳ `schedule_infos` | object[] | Danh sách thông tin phân phối chi tiết. |
| ↳↳ `schedules` | object[] | Chi tiết lịch trình phân phối. |
| ↳↳↳ `start_time` | string | Thời gian bắt đầu phân phối. |
| ↳↳↳ `end_time` | string | Thời gian kết thúc phân phối. |
| ↳↳ `expected_orders` | number[] | Thứ tự phân phối quảng cáo trong nhóm. |
| ↳↳ `is_draft` | boolean | Trạng thái bản nháp. |
| ↳↳ `schedule_id` | string | ID lịch trình liên kết quảng cáo. |
| ↳ `notice` | string | Thông báo hệ thống. |
| ↳ `contextual_tag_ids` | string[] | Danh sách ID thẻ ngữ cảnh. |

### Ví dụ

#### curl
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/update/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_id": "7123456789012345678",
    "adgroup_id": "1723456789099888",
    "adgroup_name": "RF_Brand_Awareness_Q1_Updated",
    "budget": 6000.0,
    "rf_purchased_type": "FIXED_BUDGET"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
ADGROUP_ID = "1723456789099888"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/update/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_id": ADGROUP_ID,
    "adgroup_name": "RF_Vietnam_Campaign_Updated",
    "budget": 6500.0,
    "rf_purchased_type": "FIXED_BUDGET"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Update R&F adgroup response:", data)
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201145000102452431071406595E",
    "data": {
        "advertiser_id": "7123456789012345678",
        "campaign_id": "1723456789012345",
        "adgroup_id": "1723456789099888",
        "adgroup_name": "RF_Vietnam_Campaign_Updated",
        "budget": 6500.0,
        "rf_purchased_type": "FIXED_BUDGET",
        "notice": ""
    }
}
```


---

## Hủy đơn đặt hàng quảng cáo R&F (`Cancel the R&F ad order`)
<a id="doc-1740489099367425"></a>
<!-- doc_id: 1740489099367425 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/rf/order/cancel/`

**Mục đích**: Rút lại đơn hàng quảng cáo R&F để tạm dừng phân phối quảng cáo. Khi đơn hàng bị rút lại, trạng thái của nhóm quảng cáo sẽ chuyển sang "**Closed**" (Đã đóng). Lưu ý rằng những quảng cáo đang ở trạng thái "**Delivering**" (Đang phân phối) sẽ không thể rút lại.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST: JSON body)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `adgroup_ids` | string[] | Có | Danh sách ID các nhóm quảng cáo cần rút lại đơn đặt hàng (ID phải thuộc về nhóm quảng cáo R&F). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `fail_adgroup_ids` | string[] | Danh sách ID nhóm quảng cáo mà yêu cầu rút lại đơn hàng bị thất bại. |
| ↳ `success_adgroup_ids` | string[] | Danh sách ID nhóm quảng cáo rút lại đơn hàng thành công. |

### Ví dụ

#### curl
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/rf/order/cancel/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_id": "7123456789012345678",
    "adgroup_ids": [
        "1723456789099888"
    ]
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
ADGROUP_IDS = ["1723456789099888"]

url = "https://business-api.tiktok.com/open_api/v1.3/rf/order/cancel/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_ids": ADGROUP_IDS
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Cancel R&F order response:", data)
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201200000102452431071406596F",
    "data": {
        "fail_adgroup_ids": []
    }
}
```

---

## Lấy thông tin ước tính của các nhóm quảng cáo R&F (`Get estimated info of R&F ad groups`)
<a id="doc-1740489551354881"></a>
<!-- doc_id: 1740489551354881 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/estimated/info/`

**Mục đích**: Truy vấn dữ liệu chi phí và phân bổ tần suất ước tính theo ngày cho các nhóm quảng cáo Reach & Frequency. Nếu nhóm quảng cáo không có dữ liệu ước tính hợp lệ, sẽ không có bản ghi nào tương ứng được trả về.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `adgroup_ids` | string[] | Có | Danh sách ID các nhóm quảng cáo cần truy vấn dữ liệu ước tính (mảng chuỗi JSON, ví dụ `["1723456789099888"]`). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `estimated_info` | object[] | Danh sách thông tin ước tính của các nhóm quảng cáo. |
| ↳↳ `adgroup_id` | string | ID nhóm quảng cáo. |
| ↳↳ `base_info` | object | Thông tin cơ bản. |
| ↳↳↳ `budget` | float | Tổng ngân sách. |
| ↳↳↳ `cpm` | float | Chi phí mỗi 1.000 lượt hiển thị (CPM). |
| ↳↳↳ `impression` | number | Tổng số lượt hiển thị, **tính theo đơn vị 1.000 lượt**. |
| ↳↳↳ `reach` | number | Số lượng người tiếp cận, **tính theo đơn vị 1.000 người**. |
| ↳↳↳ `average_frequency` | float | Tần suất bình quân trên mỗi người (`average_frequency` = `impression` / `reach`). |
| ↳↳ `daily_cost` | object[] | Chi phí tiêu thụ theo từng ngày. |
| ↳↳↳ `cost` | float | Chi phí trong ngày. |
| ↳↳↳ `date` | string | Ngày, định dạng `"YYYY-MM-DD"`. |
| ↳↳ `frequency_per_person` | object[] | Phân bổ số lượt hiển thị trên mỗi người dùng. |
| ↳↳↳ `frequency` | number | Tần suất hiển thị. |
| ↳↳↳ `percentage` | float | Tỷ lệ phần trăm người dùng đạt mức tần suất tương ứng. |

### Ví dụ

#### curl
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/estimated/info/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'adgroup_ids=["1723456789099888"]'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
ADGROUP_IDS = ["1723456789099888"]

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/rf/estimated/info/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_ids": json.dumps(ADGROUP_IDS)
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201215000102452431071406597A",
    "data": {
        "estimated_info": [
            {
                "adgroup_id": "1723456789099888",
                "base_info": {
                    "budget": 5000.0,
                    "cpm": 2.75,
                    "impression": 1818,
                    "reach": 1050,
                    "average_frequency": 1.73
                },
                "daily_cost": [
                    {
                        "date": "2025-03-01",
                        "cost": 500.0
                    }
                ],
                "frequency_per_person": [
                    {
                        "frequency": 1,
                        "percentage": 0.35
                    },
                    {
                        "frequency": 2,
                        "percentage": 0.65
                    }
                ]
            }
        ]
    }
}
```

---

## Truy vấn hợp đồng (`Query contracts`)
<a id="doc-1740489855138818"></a>
<!-- doc_id: 1740489855138818 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/rf/contract/query/`

**Mục đích**: Tra cứu thông tin hợp đồng quảng cáo thương mại Reach & Frequency. Vì các hợp đồng có thời hạn cụ thể, bạn cần chỉ định một ngày (`included_date`) để kiểm tra ngày bắt đầu và kết thúc của các hợp đồng hợp lệ bao gồm ngày đó.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `included_date` | string | Có | Ngày cần kiểm tra hợp đồng, định dạng `"YYYY-MM-DD"`. |
| `rf_campaign_type` | string | Không | Loại chiến dịch R&F. Giá trị enum: `STANDARD` (R&F tiêu chuẩn), `PULSE` (TikTok Pulse). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `has_valid_contract` | boolean | Có tìm thấy hợp đồng hợp lệ hay không (`true` hoặc `false`). Ngày bắt đầu và kết thúc chính xác sẽ được trả về khi trường này là `true`.<br>• Nếu không đặt `rf_campaign_type` là `PULSE`, trường này là `true` khi `included_date` nằm trong thời hạn hợp đồng R&F (`[start_date, end_date]`).<br>• Nếu đặt `rf_campaign_type` là `PULSE`, trường này là `true` khi `included_date` nằm trong thời hạn hợp đồng TikTok Pulse (`[pulse_start_date, pulse_end_date]`). |
| ↳ `pulse_start_date` | string | Ngày bắt đầu hợp đồng TikTok Pulse (trả về khi `rf_campaign_type` là `PULSE`). |
| ↳ `pulse_end_date` | string | Ngày kết thúc hợp đồng TikTok Pulse (trả về khi `rf_campaign_type` là `PULSE`).<br>> [!NOTE]<br>> Lịch phân phối của nhóm quảng cáo Pulse (`[schedule_start_time, schedule_end_time]`) phải nằm trong phần giao nhau giữa `[start_date, end_date]` và `[pulse_start_date, pulse_end_date]`. |
| ↳ `start_date` | string | Ngày bắt đầu hợp đồng Reach & Frequency. |
| ↳ `end_date` | string | Ngày kết thúc hợp đồng Reach & Frequency. |

### Ví dụ

#### curl
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/rf/contract/query/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'included_date=2025-03-01'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/rf/contract/query/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "included_date": "2025-03-01"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Contract query response:", data)
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502201230000102452431071406598B",
    "data": {
        "has_valid_contract": true,
        "start_date": "2025-01-01",
        "end_date": "2025-06-30"
    }
}
```

---

## Lấy múi giờ phân phối R&F (`Get R&F time zones`)
<a id="doc-1740490147129345"></a>
<!-- doc_id: 1740490147129345 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/rf/delivery/timezone/`

**Mục đích**: Lấy danh sách múi giờ phân phối quảng cáo Reach & Frequency tương ứng với vị trí (mã quốc gia) được chỉ định (chỉ áp dụng cho quảng cáo R&F).

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo (Advertiser ID). |
| `region_codes` | string[] | Có | Danh sách mã quốc gia cần truy vấn (mảng chuỗi JSON, ví dụ `["US", "GB", "DE"]`). Xem [Appendix - Location Code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `timezone_info` | object[] | Thông tin múi giờ theo từng khu vực. |
| ↳↳ `region_code` | string | Mã quốc gia / khu vực. |
| ↳↳ `delivery_timezone` | string[] | Danh sách các múi giờ phân phối được hỗ trợ (ví dụ `["Etc/GMT-0"]`, `["Etc/GMT+5"]`). |

### Ví dụ

#### curl
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/rf/delivery/timezone/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'region_codes=["DE","FR","IT","ES"]'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/rf/delivery/timezone/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "region_codes": json.dumps(["US", "GB"])
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Timezone query response:", data)
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202011181434430101151531921C36FC53",
    "data": {
        "timezone_info": [
            {
                "region_code": "GB",
                "delivery_timezone": [
                    "Etc/GMT-0"
                ]
            },
            {
                "region_code": "US",
                "delivery_timezone": [
                    "Etc/GMT+5"
                ]
            }
        ]
    }
}
```
