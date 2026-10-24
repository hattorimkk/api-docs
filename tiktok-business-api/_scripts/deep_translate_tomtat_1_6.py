#!/usr/bin/env python3
"""
Dịch triệt để 100% tiếng Việt cho Docs 1-6 trong do-luong-quang-cao-tom-tat.md
Bao gồm toàn bộ bảng tham số và các đoạn văn xuôi/hướng dẫn còn lại.
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOM_TAT_PATH = os.path.join(ROOT, "docs/09-marketing-api/do-luong-quang-cao-tom-tat.md")

with open(TOM_TAT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

docs = re.split(r"(?=<a id=\"doc-\d+\"></a>)", text)

# Bản đồ thay thế văn xuôi và câu dẫn
prose_map = {
    "> By using Events API endpoints, you agree to the [TikTok Business Products (Data) Terms](https://ads.tiktok.com/i18n/official/policy/business-products-terms) and that you will not share sensitive data with TikTok.":
    "> **Quan trọng:** Bằng việc sử dụng các điểm cuối Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.",
    
    "- Once you create a pixel, you can send events via web site through [installing the pixel base code](do-luong-quang-cao-tom-tat.md#doc-1739585702922241) or send events via Events API. The recommended best practice is to send both that would maximize your event coverage and campaign performance. Furthermore, with the dual channels setup, your campaign performance is protected against event disruption as the event signals will still come in from one channel when the other fails. If you are sending events from both Pixel SDK and Events API, you will need to set up [event deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450).":
    "- Khi tạo pixel xong, bạn có thể gửi sự kiện qua trang web bằng cách [cài đặt mã cơ sở pixel](do-luong-quang-cao-tom-tat.md#doc-1739585702922241) hoặc gửi sự kiện qua Events API. Phương pháp tối ưu được khuyến nghị là gửi qua cả hai kênh để tối đa hóa phạm vi thu thập sự kiện và hiệu suất chiến dịch. Thiết lập kênh đôi giúp bảo vệ chiến dịch khỏi bị gián đoạn dữ liệu vì tín hiệu vẫn được gửi từ kênh còn lại nếu một kênh gặp sự cố. Nếu gửi sự kiện từ cả Pixel SDK và Events API, bạn bắt buộc phải thiết lập [khử trùng lặp sự kiện (event deduplication)](do-luong-quang-cao-p1.md#doc-1771100965992450).",

    "- If you select \"**Partner Integrations**\" , follow the on-screen steps to complete the setup process through one of the integration partners.":
    "- Nếu chọn \"**Tích hợp đối tác (Partner Integrations)**\", hãy làm theo các bước trên màn hình để hoàn tất quy trình thiết lập qua một trong các đối tác tích hợp.",

    "- If you choose \"**Manual Setup**\", you'll have the following setup options:\n\t- **TikTok Pixel** only\n\t- **Events API** only\n\t- **TikTok Pixel + Events** API":
    "- Nếu chọn \"**Thiết lập thủ công (Manual Setup)**\", bạn có các tùy chọn sau:\n\t- Chỉ dùng **TikTok Pixel**\n\t- Chỉ dùng **Events API**\n\t- Dùng đồng thời **TikTok Pixel + Events API**",

    "- **TikTok Pixel** only": "- Chỉ dùng **TikTok Pixel**",
    "- **Events API** only": "- Chỉ dùng **Events API**",
    "- **TikTok Pixel + Events** API": "- Dùng đồng thời **TikTok Pixel + Events API**",

    "As a best practice, we encourage you to send both email and phone numbers for all visitor events. Additionally, we recommend capturing visitors' emails and phone numbers early in the funnel for best results. This increases the probability of matching customers with people on TikTok. Finally, you can pass an External ID, such as a membership ID, along with the email and phone numbers for the best matching results. To learn more about External ID, refer to [Set up External ID](do-luong-quang-cao-p1.md#doc-1771100952291330).":
    "Theo phương pháp tối ưu, chúng tôi khuyến khích bạn gửi cả email và số điện thoại cho tất cả các sự kiện của khách truy cập. Chúng tôi cũng khuyên bạn nên thu thập email và số điện thoại của khách sớm trong phễu chuyển đổi để đạt kết quả tốt nhất, gia tăng xác suất so khớp khách hàng với người dùng TikTok. Bạn cũng có thể truyền External ID (chẳng hạn như mã thành viên) cùng với email và số điện thoại để đạt kết quả so khớp cao nhất. Xem thêm tại [Thiết lập External ID](do-luong-quang-cao-p1.md#doc-1771100952291330).",

    "> To generate sample code in cURL, Python, or Node.js format for reporting Web Events via the Events API 2.0, use [the Payload Helper for Web](do-luong-quang-cao-p1.md#doc-1807346079965186).":
    "> Để tạo mã mẫu theo định dạng cURL, Python hoặc Node.js để báo cáo sự kiện Web qua Events API 2.0, hãy sử dụng [Công cụ hỗ trợ tải trọng cho Web (Payload Helper for Web)](do-luong-quang-cao-p1.md#doc-1807346079965186).",

    "> To generate sample code in cURL, Python, or Node.js format for reporting App Events via the Events API 2.0, use [the Payload Helper for App](do-luong-quang-cao-p1.md#doc-1807346142109729).":
    "> Để tạo mã mẫu theo định dạng cURL, Python hoặc Node.js để báo cáo sự kiện Ứng dụng qua Events API 2.0, hãy sử dụng [Công cụ hỗ trợ tải trọng cho App (Payload Helper for App)](do-luong-quang-cao-p1.md#doc-1807346142109729).",

    "> Reporting App Events using Events API 2.0 is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.":
    "> **Lưu ý:** Tính năng báo cáo sự kiện ứng dụng bằng Events API 2.0 hiện chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.",

    "- If you want to create a new Offline Event Set, please start from the first step. \n- If you want to use an existing Offline Event Set, you can start from the second step.":
    "- Nếu muốn tạo Bộ sự kiện ngoại tuyến mới, vui lòng bắt đầu từ bước 1.\n- Nếu muốn sử dụng Bộ sự kiện ngoại tuyến hiện có, bạn có thể bắt đầu từ bước 2.",

    "- If you want to create a new CRM Event Set, please start from the first step. \n- If you want to use an existing CRM Event Set, you can start from the second step.":
    "- Nếu muốn tạo Bộ sự kiện CRM mới, vui lòng bắt đầu từ bước 1.\n- Nếu muốn sử dụng Bộ sự kiện CRM hiện có, bạn có thể bắt đầu từ bước 2.",

    "- If you do not already have a data connection set up, select **\"Get started\"**.\n- If you already have other data connections set up, select **\"Connect data source\"**.\n\nSelect **\"App\"** and proceed.":
    "- Nếu bạn chưa thiết lập kết nối dữ liệu nào, chọn **\"Bắt đầu (Get started)\"**.\n- Nếu bạn đã thiết lập các kết nối khác, chọn **\"Kết nối nguồn dữ liệu (Connect data source)\"**.\n\nChọn **\"Ứng dụng (App)\"** và tiếp tục.",

    "To get started with app creation, navigate to **Tools ➤ Events** in your TikTok Ads Manager account.":
    "Để bắt đầu tạo ứng dụng, hãy điều hướng đến **Công cụ (Tools) ➤ Sự kiện (Events)** trong tài khoản TikTok Ads Manager của bạn.",

    "To authenticate Events API calls, you need an access token. You can generate one in the \"**Settings**\" tab. To learn more about how to generate an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058).":
    "Để xác thực lệnh gọi Events API, bạn cần có mã truy cập (Access Token). Bạn có thể tạo mã trong tab \"**Cài đặt (Settings)**\". Để tìm hiểu thêm cách tạo mã truy cập, hãy tham khảo [Events API 2.0 - Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).",

    "To report an event  (such as `LaunchAPP` or `Purchase`) from a mobile app (Android or iOS) to TikTok, call the Events API 2.0 endpoint [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).":
    "Để báo cáo sự kiện (chẳng hạn như `LaunchAPP` hoặc `Purchase`) từ ứng dụng di động (Android hoặc iOS) tới TikTok, hãy gọi điểm cuối Events API 2.0 [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).",

    "1. Upload Offline Events to your Offline Event Set\n\nAfter you create an Offline Event Set, you need to upload Offline Events to your Offline Event Set. Events are defined as actions a visitor takes on your physical store to achieve a business goal. \n\nFor details of supported offline events, see [Supported events - Offline Standard Events](do-luong-quang-cao-p1.md#doc-1771101186666498).":
    "1. Tải sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến\n\nSau khi tạo Bộ sự kiện ngoại tuyến, bạn cần tải các sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến của mình. Sự kiện được định nghĩa là các hành động mà khách hàng thực hiện tại cửa hàng thực tế để hoàn thành mục tiêu kinh doanh.\n\nĐể biết chi tiết về các sự kiện ngoại tuyến được hỗ trợ, hãy xem [Các sự kiện được hỗ trợ - Sự kiện ngoại tuyến tiêu chuẩn](do-luong-quang-cao-p1.md#doc-1771101186666498).",

    "Note that another alternative for uploading Offline Events to an Offline Event set is via **file** upload on Events Manager. To learn more about uploading Offline Events via a file, refer to [the Help Center article](https://ads.tiktok.com/help/article?aid=10007204).":
    "Lưu ý rằng một phương án thay thế khác để tải Sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến là tải tệp lên trong Trình quản lý sự kiện. Để tìm hiểu thêm về tải sự kiện ngoại tuyến qua tệp, tham khảo [bài viết Trung tâm trợ giúp](https://ads.tiktok.com/help/article?aid=10007204).",

    "Note that another alternative for uploading CRM Events to a CRM Event set is via **file** upload on Events Manager. To learn more about uploading CRM Events via a file, refer to [the Help Center article](https://ads.tiktok.com/help/article/crm-event-set-audience?lang=en).":
    "Lưu ý rằng một phương án thay thế khác để tải Sự kiện CRM lên Bộ sự kiện CRM là tải tệp lên trong Trình quản lý sự kiện. Để tìm hiểu thêm về tải sự kiện CRM qua tệp, tham khảo [bài viết Trung tâm trợ giúp](https://ads.tiktok.com/help/article/crm-event-set-audience?lang=en).",

    "You can manage your Offline Event Sets in the following ways:\n- Get the Offline Event Sets under an advertiser account via [/offline/get/](../12-api-reference/43-events-1-0-p1.md#doc-1765596808589313).\n- Update the name or the Auto Tracking setting of an Offline Event Set via [/offline/update/](../12-api-reference/43-events-1-0-p1.md#doc-1765596741157889).\n- Delete an Offline Event Set via [/offline/delete/](../12-api-reference/43-events-1-0-p1.md#doc-1765596790860802).":
    "Bạn có thể quản lý các Bộ sự kiện ngoại tuyến theo các cách sau:\n- Lấy các Bộ sự kiện ngoại tuyến thuộc tài khoản quảng cáo qua điểm cuối [/offline/get/](../12-api-reference/43-events-1-0-p1.md#doc-1765596808589313).\n- Cập nhật tên hoặc cài đặt Tự động theo dõi qua điểm cuối [/offline/update/](../12-api-reference/43-events-1-0-p1.md#doc-1765596741157889).\n- Xóa Bộ sự kiện ngoại tuyến qua điểm cuối [/offline/delete/](../12-api-reference/43-events-1-0-p1.md#doc-1765596790860802).",

    "You can manage your CRM Event sets in the following ways:\n- Get the CRM Event sets under an advertiser account via [/crm/list/](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898).":
    "Bạn có thể quản lý các Bộ sự kiện CRM theo các cách sau:\n- Lấy danh sách các Bộ sự kiện CRM thuộc tài khoản quảng cáo qua điểm cuối [/crm/list/](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898).",

    "Specify the Offline Event Sets that you want to measure in your ads via `tracking_offline_event_set_ids` when creating campaigns or ads.":
    "Chỉ định các Bộ sự kiện ngoại tuyến mà bạn muốn đo lường trong quảng cáo thông qua trường `tracking_offline_event_set_ids` khi tạo chiến dịch hoặc quảng cáo.",

    "To increase the accuracy of targeting and optimization models, it is highly recommended to include multiple types of matching data. You can use Advanced Matching, TikTok Click IDs (`ttclid`), and Cookies to attribute conversions.":
    "Để gia tăng độ chính xác của mô hình nhắm mục tiêu và tối ưu hóa, chúng tôi rất khuyến nghị bạn gửi kèm nhiều loại dữ liệu so khớp. Bạn có thể sử dụng Đối sánh nâng cao (Advanced Matching), TikTok Click ID (`ttclid`) và Cookie để phân bổ chuyển đổi.",

    "Information about the order and product associated with the event. Providing this information allows you to use value-based optimization and gives you reporting on return on ad spend (ROAS).":
    "Thông tin về đơn hàng và sản phẩm gắn với sự kiện. Việc cung cấp thông tin này cho phép bạn sử dụng tối ưu hóa dựa trên giá trị (VBO) và xem báo cáo về lợi tức chi tiêu quảng cáo (ROAS).",

    "Use the `ad` parameters to share information about the advertiser's website with Events API 2.0.":
    "Sử dụng các tham số `ad` để chia sẻ thông tin về trang web của nhà quảng cáo với Events API 2.0.",

    "Use the `ad` parameters to share information about the advertiser's app or website with Events API 2.0.":
    "Sử dụng các tham số `ad` để chia sẻ thông tin về ứng dụng hoặc trang web của nhà quảng cáo với Events API 2.0.",

    "Use the `app` parameters to share information about the advertiser's app with Events API 2.0. The `app` parameters are required for app events.":
    "Sử dụng các tham số `app` để chia sẻ thông tin về ứng dụng của nhà quảng cáo với Events API 2.0. Các tham số `app` là bắt buộc đối với sự kiện ứng dụng.",

    "Use the `lead` parameters to share information about the leads in a CRM system with Events API 2.0. The `lead` parameters are required for CRM events.":
    "Sử dụng các tham số `lead` để chia sẻ thông tin về khách hàng tiềm năng trong hệ thống CRM với Events API 2.0. Các tham số `lead` là bắt buộc đối với sự kiện CRM.",

    "> **Note:** You need to replace the dummy data in the example with your own data.":
    "> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của bạn.",
}

# Các thay thế cho bảng tham số
table_phrase_replacements = [
    ("This field is used to specify the type of events you are uploading through Events API.",
     "Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API."),
    ("The allowed enum value:", "Các giá trị enum được phép:"),
    ("Các giá trị enum hỗ trợ: •  `web`: The events took place on your website and are measured by a Pixel Code.   • `app`: The events took place on your app and are measured by a TikTok App ID. • `offline` : The conversions took place in a physical store and are measured by an Offline Event Set ID. • `crm`: The lead events took place in a CRM system and are measured by a CRM Event Set ID.",
     "Các giá trị enum hỗ trợ: • `web`: Sự kiện diễn ra trên website và được đo lường bằng Pixel Code. • `app`: Sự kiện diễn ra trên ứng dụng và được đo lường bằng TikTok App ID. • `offline`: Chuyển đổi diễn ra tại cửa hàng thực tế và được đo lường bằng Offline Event Set ID. • `crm`: Sự kiện lead diễn ra trong hệ thống CRM và được đo lường bằng CRM Event Set ID."),
    ("`web`: The events took place on your website and are measured by a Pixel Code.",
     "`web`: Sự kiện diễn ra trên trang web và được đo lường bằng Pixel Code."),
    ("`app`: The events took place on your app and are measured by a TikTok App ID.",
     "`app`: Sự kiện diễn ra trên ứng dụng và được đo lường bằng TikTok App ID."),
    ("`offline`: The conversions took place in a physical store and are measured by an Offline Event Set ID.",
     "`offline`: Sự kiện chuyển đổi diễn ra tại cửa hàng thực tế và được đo lường bằng Offline Event Set ID."),
    ("`crm`: The lead events took place on a CRM system and are tracked by a CRM Event Set ID.",
     "`crm`: Sự kiện khách hàng tiềm năng diễn ra trên hệ thống CRM và được theo dõi bằng CRM Event Set ID."),
    ("`crm`: The lead events took place in a CRM system and are measured by a CRM Event Set ID.",
     "`crm`: Sự kiện khách hàng tiềm năng diễn ra trong hệ thống CRM và được đo lường bằng CRM Event Set ID."),
    ("An Event Source ID that is used to measure events.",
     "ID nguồn sự kiện dùng để đo lường các sự kiện."),
    ("When `event_source` is set to `web`, specify a Pixel Code through this field.",
     "Khi `event_source` là `web`, hãy chỉ định Pixel Code qua trường này."),
    ("When `event_source` is set to `offline`, specify an Offline Event Set ID through this field.",
     "Khi `event_source` là `offline`, hãy chỉ định Offline Event Set ID qua trường này."),
    ("When `event_source` is set to `app`, specify a TikTok App ID through this field.",
     "Khi `event_source` là `app`, hãy chỉ định TikTok App ID qua trường này."),
    ("When `event_source` is set to `crm`, specify an CRM Event Set ID through this field.",
     "Khi `event_source` là `crm`, hãy chỉ định CRM Event Set ID qua trường này."),
    ("When `event_source` is set to `crm`, specify a CRM Event Set ID through this field.",
     "Khi `event_source` là `crm`, hãy chỉ định CRM Event Set ID qua trường này."),
    ("An object array of the events you want to report.   •  If you are sending a single event, pass one object in the array.  •  If you are batching multiple events in a single payload, you can report up to 1000 objects in one request. If a request contains more than 1,000 events, the **entire request will be rejected**.   •  To optimize campaign performance, it's **highly recommended to send the event in real-time (without batching)** as soon as it is seen on the advertiser's server.",
     "Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn."),
    ("Conversion event name. It can be either a Standard Event or a Custom Event.",
     "Tên sự kiện chuyển đổi. Có thể là Sự kiện tiêu chuẩn (Standard Event) hoặc Sự kiện tùy chỉnh (Custom Event)."),
    ("Conversion event name. ⏎ • For web and app events, it can be either a Standard Event or Custom Event. • For offline events, it can only be a Standard Event. • For CRM events, it can only be a Custom Event.",
     "Tên sự kiện chuyển đổi. ⏎ • Với sự kiện web và app: Có thể là Sự kiện tiêu chuẩn hoặc Tùy chỉnh. • Với sự kiện offline: Chỉ hỗ trợ Sự kiện tiêu chuẩn. • Với sự kiện CRM: Chỉ hỗ trợ Sự kiện tùy chỉnh."),
    ("Do not use sensitive words in the name of Custom Events. Otherwise, the responsibility for any consequences that may arise will be borne by you.",
     "Không sử dụng các từ ngữ nhạy cảm trong tên Sự kiện tùy chỉnh; nếu không, bạn sẽ chịu trách nhiệm cho mọi hậu quả phát sinh."),
    ("The time when the event occurred, indicated as a Unix timestamp measured in seconds, and in UTC+0 time zone.",
     "Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0."),
    ("Required if you are sending web events (`event_source` = `web`) from both TikTok browser pixel and Events API.",
     "Bắt buộc nếu bạn gửi sự kiện web (`event_source` = `web`) từ cả TikTok browser pixel và Events API."),
    ("Required in any of the following scenarios: • You are sending web events (`event_source` = `web`) from both TikTok browser pixel and Events API. • You are sending CRM events (`event_source` = `crm`) from both Events API and by uploading CSV files on Events Manager.",
     "Bắt buộc trong các trường hợp: • Bạn gửi sự kiện web (`event_source` = `web`) từ cả TikTok pixel trình duyệt và Events API. • Bạn gửi sự kiện CRM (`event_source` = `crm`) từ cả Events API và tệp CSV trên Trình quản lý sự kiện."),
    ("The ID that is used to identify a unique event. It can be hashed or unhashed.",
     "Mã ID dùng để định danh duy nhất một sự kiện. Có thể băm hoặc không băm."),
    ("TikTok uses the `event_source_id`, `event_id` and `event` to deduplicate the same event sent multiple times from a single channel or across multiple channels (for instance browser pixel and Events API).",
     "TikTok sử dụng bộ ba `event_source_id`, `event_id` và `event` để khử trùng lặp cùng một sự kiện gửi nhiều lần từ một kênh hoặc giữa nhiều kênh (chẳng hạn giữa browser pixel và Events API)."),
    ("Information about the customer. ⏎ To view the list of fields included in the `user` object, refer to the \"`user` parameters\" section below.",
     "Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần \"Tham số `user`\" bên dưới."),
    ("Information about the product, order and additional information to help improve ad performance. ⏎ To view the list of fields included in the `properties` object, refer to the \"`properties` parameters\" section below.",
     "Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần \"Tham số `properties`\" bên dưới."),
    ("Information about the web page. ⏎ To view the list of fields included in the `page` object, refer to the \"`page` parameters\" section below.",
     "Thông tin về trang web. ⏎ Để xem danh sách các trường trong đối tượng `page`, hãy xem phần \"Tham số `page`\" bên dưới."),
    ("Information about the app. ⏎ To view the list of fields included in the `app` object, refer to the \"`app` parameters\" section below.",
     "Thông tin về ứng dụng di động. ⏎ Để xem danh sách các trường trong đối tượng `app`, hãy xem phần \"Tham số `app`\" bên dưới."),
    ("Information about the ad. ⏎ To view the list of fields included in the `ad` object, refer to the \"`ad` parameters\" section below.",
     "Thông tin về quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `ad`, hãy xem phần \"Tham số `ad`\" bên dưới."),
    ("Information about the lead. ⏎ To view the list of fields included in the lead object, refer to the \"`lead` parameters\" section below.",
     "Thông tin về khách hàng tiềm năng (lead). ⏎ Để xem danh sách các trường trong đối tượng `lead`, hãy xem phần \"Tham số `lead`\" bên dưới."),
    ("To learn more about the Limited Data Use feature, refer to [Events API 2.0 - Limited Data Use](do-luong-quang-cao-p1.md#doc-1771101204435970).",
     "Để tìm hiểu thêm về tính năng Sử dụng dữ liệu hạn chế, hãy xem [Events API 2.0 - Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970)."),
    
    # Bảng User
    ("**SHA-256 hashing is required.** ⏎ The email address, or email addresses of the customer.",
     "**Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng."),
    ("**SHA-256 hashing is required. ** ⏎ The phone number or phone numbers of the customer.",
     "**Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng."),
    ("**SHA-256 hashing is required. ** ⏎ External ID, a unique identifier on the advertiser's side, such as loyalty membership IDs, user IDs, and external cookie IDs.",
     "**Bắt buộc băm SHA-256.** ⏎ External ID, mã định danh duy nhất từ phía nhà quảng cáo như mã thành viên, ID người dùng và cookie ngoài."),
    ("Cookie ID. ⏎ If you also use Pixel SDK and have enabled cookies, Pixel SDK automatically saves a unique identifier in the `_ttp` cookie. The value of `_ttp` is used to match website visitor events with TikTok ads. You can extract the value of `_ttp` and attach the value here.",
     "Cookie ID. ⏎ Nếu bạn cũng sử dụng Pixel SDK và đã bật cookie, Pixel SDK sẽ tự động lưu mã định danh duy nhất vào cookie `_ttp`. Giá trị của `_ttp` được dùng để khớp các sự kiện người truy cập với quảng cáo TikTok. Bạn có thể trích xuất giá trị `_ttp` và gắn vào đây."),
    ("Non-hashed ** public IP** address of the user's device. ⏎ To increase the probability of matching website visitor events with TikTok ads, we recommend sending both `ip` and `user_agent`. ⏎ Both IPv4 and IPv6 addresses are supported. For IPv6 addresses, both full and compressed formats are acceptable.",
     "Địa chỉ **IP công cộng (public IP)** không băm của thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. Hỗ trợ cả IPv4 và IPv6 (dạng đầy đủ hoặc rút gọn)."),
    ("Non-hashed user agent from the user’s device. ⏎ To increase the probability of matching website visitor events with TikTok ads, we recommend sending both `ip` and `user_agent`.",
     "Chuỗi User Agent không băm từ thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`."),
    ("The BCP 47 language identifier.", "Mã định danh ngôn ngữ theo chuẩn BCP 47."),
    ("For reference, refer to [the IETF BCP 47 standardized code](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).",
     "Để tham khảo, xem [Mã tiêu chuẩn IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt)."),
    ("TikTok Click ID, a data connection parameter appended to a landing page URL by TikTok.",
     "TikTok Click ID, tham số kết nối dữ liệu được TikTok gắn vào URL trang đích."),

    # Bảng Properties
    ("Unique ID or array of multiple IDs of the products or content.",
     "ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung."),
    ("We recommend using `sku_id` or `item_group_id` that matches the `sku_id` or `item_group_id` you set up in the catalog, if available.",
     "Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog)."),
    ("This field is required for Video Shopping Ads (VSA).",
     "Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA)."),
    ("Relevant products in an event with product information. ⏎ To view the list of fields included in the contents object, refer to the \"`contents` parameters\" section below.",
     "Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần \"Tham số `contents`\" bên dưới."),
    ("The type of content in the event. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.",
     "Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`."),
    ("•  When the `content_id` in the `contents` parameter is specified as `sku_id`, set this field to `product`.",
     "• Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`."),
    ("•  When the `content_id` in the `contents` parameter is specified as `item_group_id`, set this field to `product_group`.",
     "• Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`."),
    ("**Recommended for revenue related events. ** ⏎ The ISO 4217 currency code.",
     "**Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217."),
    ("**Recommended for revenue related events. ** ⏎ Value of the order or items sold. ⏎ The value should always be formatted as an integer or decimal (for instance, 10.00) regardless of the location, currency, or other factors. It should not contain any currency symbols, special characters, letters, or commas. ⏎ **Note**: `price` specifies the price for a single item, and `value` specifies the total price of the order. For example, if you have two items each sold for ten dollars, the `price` parameter would be `10.00` and the `value` parameter would be `20.00`.",
     "**Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng."),
    ("The quantity of items.", "Số lượng các mặt hàng."),
    ("The user-entered string for search.", "Chuỗi tìm kiếm do người dùng nhập."),
    ("Description of the item or page.", "Mô tả của mặt hàng hoặc trang web."),
    ("Order ID.", "Mã định danh đơn hàng (Order ID)."),
    ("Shop ID.", "Mã định danh cửa hàng (Shop ID)."),
    ("A categorical label indicating the customer segment associated with the conversion event. ⏎ Các giá trị enum hỗ trợ: • `new`: A new customer. • `returning`: A returning customer.",
     "Nhãn phân loại phân khúc khách hàng liên quan đến sự kiện chuyển đổi. ⏎ Các giá trị enum hỗ trợ: • `new`: Khách hàng mới. • `returning`: Khách hàng quay lại."),

    # Bảng contents
    ("The price of the item. ⏎ **Note**: `price` specifies the price for a single item, and `value` specifies the total price of the order. For example, if you have two items each sold for ten dollars, the `price` parameter would be `10.00` and the `value` parameter would be `20.00`.",
     "Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng."),
    ("Unique ID of the product or content. ⏎ We recommend using `sku_id` or `item_group_id` if you have one. ⏎ If you have set up `sku_id` or `item_group_id` in the catalog, the ID should match the `sku_id` or `item_group_id`.",
     "ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm."),
    ("Category of the page or product.", "Danh mục của trang hoặc sản phẩm."),
    ("Name of the page or product.", "Tên của trang hoặc sản phẩm."),
    ("Brand name of the product item.", "Tên thương hiệu của mặt hàng sản phẩm."),

    # Bảng page
    ("The browser URL where the event happened, for example, the value of `location.href` in the client side Javascript. ⏎ It is recommended to use the full URL, including all URLparameters.",
     "URL trình duyệt nơi sự kiện diễn ra, ví dụ giá trị của `location.href` trong JavaScript phía máy khách. ⏎ Khuyến nghị sử dụng URL đầy đủ, bao gồm toàn bộ tham số truy vấn."),
    ("The referrer URL.", "URL giới thiệu (referrer URL)."),

    # Bảng ad
    ("The TikTok ID chiến dịch quảng cáo associated with the touchpoint, typically parsed from the landing URL or deeplink.",
     "ID chiến dịch quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink."),
    ("The TikTok ID nhóm quảng cáo associated with the touchpoint, typically parsed from the landing URL or deeplink.",
     "ID nhóm quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink."),
    ("The TikTok ID mẫu quảng cáo associated with the touchpoint, typically parsed from the landing URL or deeplink.",
     "ID mẫu quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink."),
    ("Attribution provider.", "Nhà cung cấp dịch vụ phân bổ (Attribution provider)."),
    ("Attribution share score. ⏎ A score provided by you per conversion, representing the portion of credit TikTok should receive for the conversion. A greater value indicates a larger credit share for TikTok. ⏎ Examples: • 0.0: No credit. • 0.5: Partial credit. • 1.0: Full credit.",
     "Điểm tỷ lệ phân bổ (Attribution share score). ⏎ Điểm số do bạn cung cấp cho mỗi chuyển đổi, đại diện cho phần công nhận mà TikTok nhận được (từ `0.0` đến `1.0`)."),
    ("The portion of the conversion's ROAS that your attribution system assigns to this TikTok touchpoint. ⏎ Typical usage: multiply the conversion value by the touchpoint's credit share (`attribution_share`) and pass the result here.",
     "Phần giá trị chuyển đổi mà hệ thống phân bổ của bạn gán cho điểm chạm TikTok này (thường bằng giá trị chuyển đổi nhân với `attribution_share`)."),
    ("The attribution model that is used to attribute the event.",
     "Mô hình phân bổ được sử dụng để phân bổ cho sự kiện."),
    ("The type of TikTok touchpoint that received credit for this event.",
     "Loại điểm chạm TikTok nhận được ghi nhận cho sự kiện này."),
    ("The time the TikTok touchpoint occurred, expressed as a Unix timestamp in seconds in the UTC+0 time zone.",
     "Thời điểm điểm chạm TikTok diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0."),
    ("The URL where the touchpoint was captured. ⏎ An example is the landing page URL that a user reached after clicking a TikTok ad.",
     "URL nơi điểm chạm được ghi nhận, ví dụ như URL trang đích mà người dùng truy cập sau khi nhấp quảng cáo TikTok."),
    ("The click-through attribution window, expressed in **hours**.",
     "Cửa sổ phân bổ nhấp chuột (click-through attribution window), tính bằng **giờ**."),
    ("The view-through attribution window, expressed in **hours**.",
     "Cửa sổ phân bổ lượt xem (view-through attribution window), tính bằng **giờ**."),
    ("The technical method used to associate the touchpoint with the conversion.",
     "Phương thức kỹ thuật được sử dụng để liên kết điểm chạm với chuyển đổi."),
    ("The reason your system declined to assign attribution credit to TikTok for this event.",
     "Lý do hệ thống của bạn từ chối gán công nhận phân bổ cho TikTok đối với sự kiện này."),
    ("The unique identifier of the marketing campaign or UTM parameter set that produced the touchpoint.",
     "Mã định danh duy nhất của chiến dịch tiếp thị hoặc bộ tham số UTM tạo ra điểm chạm."),
    ("The traffic source that referred the user to the landing page, as captured in the `utm_source` URL parameter.",
     "Nguồn lưu lượng truy cập giới thiệu người dùng đến trang đích, được ghi lại trong tham số URL `utm_source`."),
    ("The marketing medium that delivered the traffic, as captured in the `utm_medium` URL parameter.",
     "Phương tiện tiếp thị phân phối lưu lượng truy cập, được ghi lại trong tham số URL `utm_medium`."),
    ("The campaign name that produced the touchpoint, as captured in the `utm_campaign` URL parameter.",
     "Tên chiến dịch tạo ra điểm chạm, được ghi lại trong tham số URL `utm_campaign`."),
]

# Áp dụng cho docs 1 đến 6
for i in range(1, 7):
    doc_text = docs[i]
    for old, new in prose_map.items():
        doc_text = doc_text.replace(old, new)
    for old, new in table_phrase_replacements:
        doc_text = doc_text.replace(old, new)
    docs[i] = doc_text

new_text = "".join(docs)
with open(TOM_TAT_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Đã cập nhật dịch nâng cao cho Docs 1-6 trong {TOM_TAT_PATH}")
