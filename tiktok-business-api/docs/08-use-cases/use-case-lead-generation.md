# Use case: Lead generation

Tài liệu này hướng dẫn toàn diện các tình huống sử dụng thu thập khách hàng tiềm năng (Lead Generation) trên TikTok. Bạn sẽ tìm hiểu cách trích xuất dữ liệu khách hàng tiềm năng dành cho nhà quảng cáo thông qua tác vụ tải xuống hoặc nhận thông báo thời gian thực qua Webhook, cũng như quy trình tích hợp dành cho đối tác CRM để xuất dữ liệu khách hàng tiềm năng và gửi lại (postback) các sự kiện CRM nhằm tối ưu hóa chuyển đổi.

## Thu thập khách hàng tiềm năng (`Lead generation`)
<a id="doc-1739289524101122"></a>
<!-- doc_id: 1739289524101122 -->

> Đường dẫn: Use Cases > Lead generation

Chương này bao gồm các tình huống sử dụng sau:

- [Lấy dữ liệu khách hàng tiềm năng với vai trò nhà quảng cáo (Obtain leads as advertisers)](use-case-lead-generation.md#doc-1806817494948930)
- [Xuất khách hàng tiềm năng và gửi lại sự kiện CRM (Export leads and postback CRM events)](use-case-lead-generation.md#doc-1806817505894402)

## Lấy dữ liệu khách hàng tiềm năng với vai trò nhà quảng cáo (`Obtain leads as advertisers`)
<a id="doc-1806817494948930"></a>
<!-- doc_id: 1806817494948930 -->

> Đường dẫn: Use Cases > Lead generation > Obtain leads as advertisers

Bài viết này hướng dẫn bạn từng bước lấy thông tin khách hàng tiềm năng (leads) từ chiến dịch Lead Generation với tư cách là nhà quảng cáo.

### Giới thiệu (Introduction)

Khi tạo chiến dịch Lead Generation, bạn có thể gia tăng lượt chuyển đổi và thúc đẩy lưu lượng truy cập trang web. Lead Generation giúp bạn thu thập các tín hiệu có giá trị từ những người quan tâm đến doanh nghiệp của bạn. **Bạn có thể sử dụng API để truy cập nhanh dữ liệu khách hàng tiềm năng theo một trong các phương thức sau:**
- **Tải xuống dữ liệu khách hàng tiềm năng (Download leads)**
- **Đăng ký nhận dữ liệu khách hàng tiềm năng qua Webhook (Subscribe to leads via webhooks)**

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
  - Để thiết lập webhook cho leads, bạn cần các quyền liên quan cho các endpoint được liệt kê trong mục "Các bước thực hiện". Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho từng endpoint và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền.
- Bạn đã tạo các quảng cáo Lead Generation. Xem [Tạo quảng cáo Lead Generation](use-case-tao-chien-dich-p1.md#doc-1739470742024193) để biết các bước tạo chi tiết.

### Các bước thực hiện (Steps)

#### Tải xuống khách hàng tiềm năng (Download leads)

> [!NOTE]
> Để bảo vệ thông tin khách hàng, chỉ quản trị viên tài khoản quảng cáo (ad account admins) mới có thể tạo và truy vấn tác vụ tải xuống lead hoặc tải xuống danh sách khách hàng tiềm năng.

1. Gửi yêu cầu GET tới endpoint [/page/lead/task/](../12-api-reference/48-leads.md#doc-1739052936772610) để tạo tác vụ tải xuống leads.
2. Khi trạng thái tác vụ chuyển sang `SUCCEED`, hãy gửi yêu cầu GET tới endpoint [/page/lead/task/download/](../12-api-reference/48-leads.md#doc-1739053563877378) để tải dữ liệu khách hàng tiềm năng về.

#### Đăng ký nhận dữ liệu khách hàng tiềm năng qua Webhook (Subscribe to leads via webhooks)

Webhook cho phép bạn tích hợp quảng cáo Lead Generation với hệ thống CRM của mình và nhận cập nhật theo thời gian thực cho cả khách hàng tiềm năng từ Biểu mẫu tức thì (Instant Form) và Tin nhắn trực tiếp (Direct Message).

##### Tạo đăng ký (Create a subscription)
Để tìm hiểu cách đăng ký webhook nhận leads, hãy xem [Đăng ký nhận leads](use-case-webhook.md#doc-1810521739537409).

##### Kiểm thử đăng ký (Test the subscription)
Sau khi đăng ký thành công, bạn có thể thực hiện theo quy trình dưới đây để kiểm thử toàn diện quy trình thu thập khách hàng tiềm năng:
Xin lưu ý rằng bạn chỉ có thể tạo một lead thử nghiệm cho mỗi trang (page). Bạn bắt buộc phải xóa lead thử nghiệm hiện có trước khi tạo một lead thử nghiệm mới.

1. Gửi yêu cầu POST tới endpoint [/page/lead/mock/create/](../12-api-reference/48-leads.md#doc-1739047132614722) để tạo một lead thử nghiệm.
2. Gửi yêu cầu GET tới endpoint [/page/lead/mock/get/](../12-api-reference/48-leads.md#doc-1739048460493826) để lấy lead thử nghiệm.
3. Gửi yêu cầu POST tới endpoint [/page/lead/mock/delete/](../12-api-reference/48-leads.md#doc-1739049313198081) để xóa lead thử nghiệm.

### Các lưu ý bổ sung (Additional notes)

#### Xác thực tải trọng (Validate payloads)

Chúng tôi ký tất cả các payload thông báo sự kiện bằng chữ ký **HMAC-SHA256** và đưa chữ ký đó vào header **X-Open-Signature** của yêu cầu. Chúng tôi khuyến nghị bạn nên xác thực payload.

Để xác thực payload:
1. Tạo chữ ký **HMAC-SHA256** bằng cách nhập payload và **App Secret** của ứng dụng.

Dưới đây là một ví dụ về cách tạo chữ ký:

Tải trọng mẫu (Sample payload):
```json
{
   "request_id":{{request_id}},
   "object":{{object}},
   "entry": [
     {
       "id": {{id}},
       "page_id":{{page_id}},
       "page_name":"hello_world",
       "campaign_id":{{campaign_id}},
       "campaign_name":"{{campaign_name}}",
       "adgroup_id":{{adgroup_id}},
       "adgroup_name":"{{adgroup_name}}",
       "ad_id":{{ad_id}},
       "ad_name":"{{ad_name}}",
       "create_time":{{create_time}},
       "changes": [
         {
           "field": "phone_number",
           "value": "{{phone_number}}"
         },
         {
           "field": "email",
           "value": "{{email}}"
         },
         {
           "field": "name",
           "value": "{{name}}"
         }
       ]
     }
   ],
   "time": {{time}}
}
```

App Secret mẫu: `5b5c09c880c9af2c69e39b18024f255d3****`

Truyền cả payload và App Secret của ứng dụng vào hàm mã hóa **HMAC-SHA256** để nhận chuỗi kết quả được mã hóa. Chuỗi này chính là chữ ký. Ví dụ, bạn có thể nhận được: `48fa5d1c81597afc6d15bf5aa588f45df8f0b22d0c0d66d8a2977b368a3f****`.

2. So sánh chữ ký của bạn với chữ ký trong header **X-Open-Signature**. Nếu hai chữ ký khớp nhau, payload là xác thực.

Lưu ý rằng chúng tôi tạo chữ ký bằng cách sử dụng phiên bản *unicode đã thoát* (escaped unicode) của payload, với các chữ số thập lục phân viết thường (lowercase hex digits). Nếu bạn chỉ tính toán trên các byte đã giải mã, bạn sẽ nhận được chữ ký khác. Ví dụ: chuỗi `äöå` phải được thoát thành `\u00e4\u00f6\u00e5`.

#### Phản hồi thông báo sự kiện (Respond to event notifications)

Endpoint của bạn phải phản hồi tất cả các thông báo sự kiện bằng mã trạng thái HTTPS 200 OK.

#### Tần suất gửi (Frequency)

Các thông báo sự kiện được tổng hợp và gửi theo đợt (batch) với mức **tối đa** là 1.000 bản cập nhật. Tuy nhiên việc gửi theo đợt không được đảm bảo tuyệt đối, vì vậy hãy đảm bảo máy chủ của bạn có thể xử lý từng webhook riêng lẻ.
Nếu bất kỳ bản cập nhật nào gửi tới máy chủ của bạn thất bại, API sẽ thử lại ngay lập tức, sau đó thử lại thêm một vài lần với tần suất giảm dần trong vòng 24 giờ tiếp theo. Máy chủ của bạn nên xử lý loại bỏ trùng lặp (deduplication) trong những trường hợp này. Các phản hồi không được xác nhận nhận thành công sẽ bị hủy bỏ sau 24 giờ.

#### Các thao tác sau khi đăng ký (Post-subscription operations)

Nếu không còn nhu cầu nhận thông báo leads cho một trang nữa, bạn có thể hủy đăng ký. Bạn có thể xem danh sách tất cả các gói đăng ký của nhà quảng cáo. Xem chi tiết tại [Lấy danh sách đăng ký](../12-api-reference/66-subscription.md#doc-1739093832125442) và [Hủy đăng ký](../12-api-reference/66-subscription.md#doc-1739094758789122).

#### Lấy nhật ký đăng ký biểu mẫu và tải xuống lead (Get form subscription and lead download logs)

Bạn có thể sử dụng endpoint [/changelog/task/create/](../12-api-reference/34-change-log.md#doc-1738811219460097) để lấy nhật ký thay đổi cho các hoạt động như đăng ký biểu mẫu, hủy đăng ký biểu mẫu và tải xuống khách hàng tiềm năng từ biểu mẫu. Hãy thiết lập các trường dữ liệu như sau:
- Truyền danh sách ID trang vào mảng `object_ids`.
- Đặt `object_type` thành `INSTANT_FORM`.
- Đặt `operation_types` thành sự kết hợp của `DOWNLOAD_LEADS`, `SUBSCRIBE_FORM` và `UNSUBSCRIBE_FORM`.

### Tài liệu liên quan (Related docs)

- [Leads API](../12-api-reference/48-leads.md#doc-1739047069984834)
- [Hướng dẫn Lead Generation](https://ads.tiktok.com/help/article/build-instant-form?lang=en) trên Trung tâm trợ giúp TikTok Business

## Xuất khách hàng tiềm năng và gửi lại sự kiện CRM (`Export leads and postback CRM events`)
<a id="doc-1806817505894402"></a>
<!-- doc_id: 1806817505894402 -->

> Đường dẫn: Use Cases > Lead generation > Export leads and postback CRM events

Bài viết này hướng dẫn bạn từng bước xuất khách hàng tiềm năng và gửi lại (postback) các sự kiện CRM (Quản lý quan hệ khách hàng) với tư cách là đối tác CRM.

### Giới thiệu (Introduction)

Là một đối tác CRM, bạn có thể tích hợp với TikTok Lead Generation, cho phép khách hàng của bạn xuất leads trực tiếp vào hệ thống CRM của họ mà không yêu cầu bất kỳ kỹ năng lập trình nào.

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
- Để xuất khách hàng tiềm năng và gửi lại sự kiện CRM, bạn cần có các quyền liên quan. Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho các endpoint (bao gồm các endpoint trong mục "Các bước thực hiện") và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền. Hãy đảm bảo ứng dụng nhà phát triển của bạn có các phạm vi quyền sau:
  - **Ad Account Management** > **Ad Account Information**
  - **Creative Management** > **Instant Page Management**
  - **Lead Management** > **Leads Retrieval**
  - **Lead Management** > **Test Leads**
  - **CRM Event Management** > **Read CRM Event Sets**
  - **Measurement** > **Report Conversion Event**
- Bạn có thể sử dụng **/user/info/** để lấy thông tin chi tiết của người dùng nhằm cá nhân hóa trải nghiệm cho họ.
- Bạn đã lấy được danh sách Biểu mẫu tức thì (Instant Forms) trong tài khoản quảng cáo bằng cách gọi [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586) với các tham số sau:
  - `business_type` đặt thành `LEAD_GEN`
  - `status` đặt thành `PUBLISHED`
- Bạn đã lấy các trường của Biểu mẫu tức thì để thực hiện ánh xạ trường (field mapping) bằng cách gọi [/page/field/get/](../12-api-reference/48-leads.md#doc-1739054080455681).

### Các bước thực hiện (Steps)

Để thiết lập tích hợp với quảng cáo TikTok Lead Generation, hãy thực hiện theo các bước sau:

#### 1. Truy cập dữ liệu khách hàng tiềm năng (Access leads data)

Chọn một trong các phương án sau:

##### Phương án 1: Nhận leads qua Webhook
**Đăng ký nhận thông báo từ Biểu mẫu tức thì hoặc tin nhắn trực tiếp** bằng cách gọi [/subscription/subscribe/](../12-api-reference/66-subscription.md#doc-1739092028876801). Để tìm hiểu thêm về các bước thực hiện, xem [Đăng ký nhận leads](use-case-webhook.md#doc-1810521739537409). Sau khi hoàn tất đăng ký, bạn có thể nhận các bản cập nhật thời gian thực về khách hàng tiềm năng.

> [!NOTE]
> Nếu sau này bạn muốn hủy đăng ký, hãy sử dụng endpoint [/subscription/unsubscribe/](../12-api-reference/66-subscription.md#doc-1739094758789122).

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/subscription/subscribe/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "app_id": "{{app_id}}", 
    "secret": "{{secret}}",
    "subscription_detail": {
        "advertiser_id": "{{advertiser_id}}", 
        "access_token": "{{access_token}}", 
        "page_id": "{{page_id}}"
    }, 
    "subscribe_entity": "LEAD", 
    "callback_url": "{{callback_url}}" // khi có lead mới, dịch vụ sẽ gửi yêu cầu POST chứa dữ liệu lead tới callback URL này
}'
```

Phản hồi thành công (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "subscription_id": "{{subscription_id}}"
    },
    "request_id": "{{request_id}}"
}
```

##### Phương án 2: Tải xuống leads qua tác vụ (Download leads via tasks)
i. **Tạo tác vụ tải xuống lead** bằng cách gọi endpoint [/page/lead/task/](../12-api-reference/48-leads.md#doc-1739052936772610). Lưu ý rằng do các yêu cầu về tuân thủ dữ liệu, dữ liệu khách hàng tiềm năng của nhà quảng cáo được lưu trữ riêng biệt tại ba khu vực: Châu Âu (bao gồm Khu vực Kinh tế Châu Âu - EEA, Thụy Sĩ và Vương quốc Anh), Hoa Kỳ và Phần còn lại của thế giới.

Để biết thông tin chi tiết về cấu hình header cho tác vụ tải lead giữa các khu vực, hãy tham khảo các ví dụ code dưới đây:

**Tạo tác vụ tải xuống cho lead tại Châu Âu**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/?advertiser_id={{advertiser_id}}&page_id={{page_id}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'x-lead-region: eu'
```

**Tạo tác vụ tải xuống cho lead tại Hoa Kỳ**
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/?advertiser_id={{advertiser_id}}&page_id={{page_id}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'x-lead-region: us'
```

**Tạo tác vụ tải xuống cho lead tại các khu vực khác**
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/?advertiser_id={{advertiser_id}}&page_id={{page_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi thành công (Successful response)
```http
// curl
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "status": "CREATED",
        "task_id": "{{task_id}}"
    }
}
```

ii. Khi `status` của tác vụ là `SUCCEED`, hãy **tải xuống leads** bằng cách gọi endpoint [/page/lead/task/download/](../12-api-reference/48-leads.md#doc-1739053563877378). Tham khảo các ví dụ sau để cấu hình header tương ứng theo từng khu vực:

**Tải xuống lead cho Châu Âu**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/?advertiser_id={{advertiser_id}}&task_id={{task_id}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'x-lead-region: eu'
```

**Tải xuống lead cho Hoa Kỳ**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/?advertiser_id={{advertiser_id}}&task_id={{task_id}}' \
--header 'Access-Token: {{Access-Token}}' \
--header 'x-lead-region: us'
```

**Tải xuống lead cho các khu vực khác**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/?advertiser_id={{advertiser_id}}&task_id={{task_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

#### 2. Kiểm thử leads (Test your leads)

**Kiểm thử leads** bằng cách sử dụng các endpoint sau:
- [/page/lead/mock/create/](../12-api-reference/48-leads.md#doc-1739047132614722)
- [/page/lead/mock/get/](../12-api-reference/48-leads.md#doc-1739048460493826)
- [/page/lead/mock/delete/](../12-api-reference/48-leads.md#doc-1739049313198081)

#### 3. Gửi lại sự kiện CRM (Postback CRM events)

Sử dụng CRM Events API để gửi lại dữ liệu sự kiện cho TikTok có thể giúp tạo ra những khách hàng tiềm năng có chất lượng cao hơn và có nhiều khả năng chuyển đổi hơn.

Hãy thực hiện theo các bước sau để gửi lại sự kiện CRM:

i. **Lấy các Bộ sự kiện CRM (CRM Event Sets) trong tài khoản quảng cáo của bạn** bằng cách gọi [/crm/list/](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898).

ii. **Gửi lại dữ liệu sự kiện CRM của bạn** bằng cách gọi [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761). Đặt `event_source` thành `crm` và đặt `event_source_id` thành một trong các ID Bộ sự kiện CRM lấy được từ bước i.

Ví dụ:
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "event_source": "crm",
    "event_source_id": "CCM52VJC77U1F3L1CJRG",
    "partner_name": "Name of the Partner",
    "data": [
        {
            "event": "qualified",
            "event_time": 1687673101,
            "lead": {
                "lead_id": "lead_id",
                "lead_event_source": "Lead_gen_partner_name"
            }
        }
    ]
}'
```

#### 4. Niêm yết CRM của bạn trên TikTok Ads Manager (List your CRM on TikTok Ads Manager)

Sau khi hoàn thành các bước trên, bạn có thể mở rộng tệp khách hàng của mình bằng cách tăng cường mức độ nhận diện trên TikTok.

Hãy điền vào [Biểu mẫu niêm yết trên TikTok Ads Manager (TikTok Ads Manager Listing form)](https://ads.tiktok.com/leads_management/crm_listing_form?lane_id=master) để nền tảng CRM của bạn có thể được các nhà quảng cáo khám phá và lựa chọn trực tiếp trên TikTok Ads Manager.
