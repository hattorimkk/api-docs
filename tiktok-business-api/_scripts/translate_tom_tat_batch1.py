#!/usr/bin/env python3
"""
Biên dịch tiếng Việt cho Docs 1-6 của u124 (do-luong-quang-cao-tom-tat.md).
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOM_TAT_PATH = os.path.join(ROOT, "docs/09-marketing-api/do-luong-quang-cao-tom-tat.md")

with open(TOM_TAT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

docs = re.split(r"(?=<a id=\"doc-\d+\"></a>)", text)
print(f"Tổng số phần tử tài liệu trong tom-tat.md: {len(docs)}")

# 1. Cập nhật TOC cho Docs 1-6
toc_replacements = [
    ("- [1. Setup guide for Web (#doc-1771100865818625)](#doc-1771100865818625)",
     "- [1. Hướng dẫn thiết lập cho Web (Setup guide for Web) (#doc-1771100865818625)](#doc-1771100865818625)"),
    ("- [2. Setup guide for Offline (#doc-1771101027431425)](#doc-1771101027431425)",
     "- [2. Hướng dẫn thiết lập Ngoại tuyến (Setup guide for Offline) (#doc-1771101027431425)](#doc-1771101027431425)"),
    ("- [3. Setup guide for App (#doc-1771101111730178)](#doc-1771101111730178)",
     "- [3. Hướng dẫn thiết lập cho Ứng dụng (Setup guide for App) (#doc-1771101111730178)](#doc-1771101111730178)"),
    ("- [4. Setup guide for CRM (#doc-1835052338764993)](#doc-1835052338764993)",
     "- [4. Hướng dẫn thiết lập CRM (Setup guide for CRM) (#doc-1835052338764993)](#doc-1835052338764993)"),
    ("- [5. Parameters (#doc-1771101151059969)](#doc-1771101151059969)",
     "- [5. Bảng tham số (Parameters) (#doc-1771101151059969)](#doc-1771101151059969)"),
    ("- [6. Payload Converter (#doc-1805266308200514)](#doc-1805266308200514)",
     "- [6. Bộ chuyển đổi tải trọng (Payload Converter) (#doc-1805266308200514)](#doc-1805266308200514)"),
]

for old, new in toc_replacements:
    if old in docs[0]:
        docs[0] = docs[0].replace(old, new)
    else:
        print(f"Cảnh báo TOC: Không tìm thấy {old}")

# Từ điển thay thế các cụm từ tham số và bảng dùng chung trong Docs 1-6
common_replacements = [
    # Tiêu đề chung
    ("# Setup guide for Web", "# Hướng dẫn thiết lập cho Web (Setup guide for Web)"),
    ("# Setup guide for Offline", "# Hướng dẫn thiết lập Ngoại tuyến (Setup guide for Offline)"),
    ("# Setup guide for App", "# Hướng dẫn thiết lập cho Ứng dụng (Setup guide for App)"),
    ("# Setup guide for CRM", "# Hướng dẫn thiết lập CRM (Setup guide for CRM)"),
    ("# Get Started", "# Bắt đầu (Get Started)"),
    ("## Before you begin", "## Trước khi bắt đầu"),
    ("## Sample payload", "## Tải trọng mẫu (Sample payload)"),
    ("## Bảng tham số (Parameters) for reporting Web Events", "## Bảng tham số (Parameters) để báo cáo sự kiện Web"),
    ("## Bảng tham số (Parameters) for reporting Offline Events", "## Bảng tham số (Parameters) để báo cáo sự kiện Ngoại tuyến"),
    ("## Bảng tham số (Parameters) for reporting App Events", "## Bảng tham số (Parameters) để báo cáo sự kiện Ứng dụng"),
    ("## Bảng tham số (Parameters) for reporting CRM Events", "## Bảng tham số (Parameters) để báo cáo sự kiện CRM"),
    ("### Top-level parameters", "### Tham số cấp cao nhất (Top-level parameters)"),
    ("#### `user` parameters", "#### Tham số `user` (`user` parameters)"),
    ("#### `properties` parameters", "#### Tham số `properties` (`properties` parameters)"),
    ("##### `contents` parameters", "##### Tham số `contents` (`contents` parameters)"),
    ("#### `page` parameters", "#### Tham số `page` (`page` parameters)"),
    ("#### `app` parameters", "#### Tham số `app` (`app` parameters)"),
    ("#### `ad` parameters", "#### Tham số `ad` (`ad` parameters)"),
    ("#### `lead` parameters", "#### Tham số `lead` (`lead` parameters)"),
    ("## `user` parameters", "## Tham số `user` (`user` parameters)"),
    ("## `properties` parameters", "## Tham số `properties` (`properties` parameters)"),
    ("### `contents` parameters", "### Tham số `contents` (`contents` parameters)"),
    ("## `page` parameters", "## Tham số `page` (`page` parameters)"),
    ("## `app` parameters", "## Tham số `app` (`app` parameters)"),
    ("## `ad` parameters", "## Tham số `ad` (`ad` parameters)"),
    ("## `lead` parameters", "## Tham số `lead` (`lead` parameters)"),
    ("### 1. Create a Pixel", "### 1. Tạo Pixel"),
    ("### 2. Generate an access token", "### 2. Tạo mã truy cập (Access Token)"),
    ("## 1. Create an Offline Event Set", "## 1. Tạo bộ sự kiện ngoại tuyến (Offline Event Set)"),
    ("## 2. Generate an access token", "## 2. Tạo mã truy cập (Access Token)"),
    ("## 1. Create a CRM Event Set", "## 1. Tạo bộ sự kiện CRM (CRM Event Set)"),
    ("### Option 1: Through Events Manager UI", "### Tùy chọn 1: Qua giao diện Trình quản lý sự kiện (Events Manager UI)"),
    ("### Option 2: Through API", "### Tùy chọn 2: Qua API"),
    ("# Send Offline Events with Events API 2.0", "# Gửi sự kiện ngoại tuyến bằng Events API 2.0"),
    ("# Share Events with Events API", "# Chia sẻ sự kiện bằng Events API"),
    ("# Share matching data within the events", "# Chia sẻ dữ liệu so khớp trong sự kiện"),
    ("# Verify Events setup", "# Xác minh thiết lập sự kiện"),
    ("# Verify Offline Events setup", "# Xác minh thiết lập sự kiện ngoại tuyến"),
    ("# Verify CRM Events setup", "# Xác minh thiết lập sự kiện CRM"),
    ("# Best Practices for Optimal Performance", "# Các phương pháp tối ưu để đạt hiệu suất cao nhất"),
    ("# Create an app and generate your TikTok App ID", "# Tạo ứng dụng và tạo TikTok App ID"),
    ("## Access Events Manager", "## Truy cập Trình quản lý sự kiện"),
    ("## Create your app", "## Tạo ứng dụng của bạn"),
    ("## Provide your app details", "## Cung cấp chi tiết ứng dụng"),
    ("## Generate your TikTok App ID", "## Tạo TikTok App ID của bạn"),
    ("## Generate your access token", "## Tạo mã truy cập của bạn"),
    ("# Report an App Event", "# Báo cáo sự kiện ứng dụng (Report an App Event)"),
    ("# Share CRM Events with Events API", "# Chia sẻ sự kiện CRM bằng Events API"),
    ("# Manage Offline Event Sets *(Không bắt buộc)*", "# Quản lý các bộ sự kiện ngoại tuyến *(Không bắt buộc)*"),
    ("# Measure Offline Event sets in your regular ads or aco ads", "# Đo lường các bộ sự kiện ngoại tuyến trong quảng cáo thông thường hoặc ACO"),
    ("# *(Không bắt buộc)* Manage CRM Event sets", "# Quản lý các bộ sự kiện CRM *(Không bắt buộc)*"),
    
    # Đoạn văn dẫn dắt
    ("This guide walks you through the process of setting up Events API 2.0 for Web.",
     "Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Web."),
    ("This guide walks you through the process of setting up Events API 2.0 for Offline.",
     "Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Ngoại tuyến (Offline)."),
    ("This guide walks you through the process of setting up Events API 2.0 for App.",
     "Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Ứng dụng di động (App)."),
    ("This guide walks you through the process of setting up Events API 2.0 for CRM (Customer relationship management).",
     "Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho hệ thống CRM (Quản lý quan hệ khách hàng)."),
    ("For each parameter value format, refer to the lists below.",
     "Để biết định dạng giá trị của từng tham số, vui lòng tham khảo các danh sách bên dưới."),
    ("Required for reporting Return on Ad Spend (ROAS) or for Value-based Optimization (VBO)",
     "Bắt buộc để báo cáo ROAS hoặc VBO"),
    ("Required for Video Shopping Ads (VSA)", "Bắt buộc cho Video Shopping Ads (VSA)"),
    
    # Nội dung Doc 1
    ("You should have access to TikTok Ads Manager that contains test event functionality and diagnostic tools that would help you during development testing and post integration validation.",
     "Bạn cần có quyền truy cập vào TikTok Ads Manager chứa chức năng kiểm tra sự kiện và các công cụ chẩn đoán giúp bạn trong quá trình thử nghiệm phát triển và xác thực sau tích hợp."),
    ("You must have created a pixel in the TikTok Ads Manager under **Tools** > **Events**.",
     "Bạn phải tạo một pixel trong TikTok Ads Manager tại mục **Công cụ (Tools)** > **Sự kiện (Events)**."),
    ("If you don't already have a pixel, start with the first step to create a pixel. \nIf you already have an existing pixel, skip the first step and start with the second step.",
     "Nếu bạn chưa có pixel, hãy bắt đầu từ bước 1 để tạo pixel mới.\nNếu bạn đã có sẵn pixel, hãy bỏ qua bước 1 và bắt đầu từ bước 2."),
    ("a. In [TikTok Ads Manager](https://ads.tiktok.com/i18n/home), navigate to  **Tools** > **Events** > **Connect data source** > **Web**.",
     "a. Trong [TikTok Ads Manager](https://ads.tiktok.com/i18n/home), điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)** > **Kết nối nguồn dữ liệu (Connect data source)** > **Web**."),
    ("b. Add your website.", "b. Thêm trang web của bạn."),
    ("c. Choose data connection method", "c. Chọn phương thức kết nối dữ liệu:"),
    ("- Option 1: **Partner integrations**", "- Tùy chọn 1: **Tích hợp đối tác (Partner integrations)**"),
    ("- Option 2: **Manual setup**", "- Tùy chọn 2: **Thiết lập thủ công (Manual setup)**"),
    ("For optimal performance, we recommend setting up both TikTok Pixel and Events API. You'll need to name and create the Pixel, then follow the on-screen instructions to complete the setup and Pixel creation process.",
     "Để đạt hiệu suất tối ưu, chúng tôi khuyến nghị thiết lập đồng thời cả TikTok Pixel và Events API. Bạn cần đặt tên và tạo Pixel, sau đó làm theo hướng dẫn trên màn hình để hoàn tất quy trình thiết lập và tạo Pixel."),
    ("To authenticate Events API calls, you need an access token. To learn about how to obtain an access token, refer to [Events API 2.0 > Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058).",
     "Để xác thực các lệnh gọi Events API, bạn cần có mã truy cập (Access Token). Để tìm hiểu cách lấy mã truy cập, hãy tham khảo [Events API 2.0 > Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058)."),
    ("Alternatively, you can **Generate access token** from pixel > **Settings**.",
     "Ngoài ra, bạn có thể bấm **Tạo mã truy cập (Generate access token)** từ mục pixel > **Cài đặt (Settings)**."),
    ("Events are actions a website visitor takes to achieve a business goal, like adding an item to a cart, filling out a form or making a purchase. Prior to integrating with the Events API, we recommend predefining which Events you are interested in sharing with TikTok to achieve your marketing objectives. You can add events and parameters to be sent with your payload.",
     "Sự kiện là các hành động mà khách truy cập trang web thực hiện nhằm đạt được mục tiêu kinh doanh, chẳng hạn như thêm sản phẩm vào giỏ hàng, điền biểu mẫu hoặc mua hàng. Trước khi tích hợp với Events API, chúng tôi khuyên bạn nên xác định trước những Sự kiện nào bạn muốn chia sẻ với TikTok nhằm phục vụ mục tiêu tiếp thị. Bạn có thể thêm các sự kiện và tham số gửi kèm trong tải trọng."),
    ("Events API for Web uses customer information such as TikTok Click IDs (`ttclid`), Advanced Matching, and additional signals like IP address and User Agent to match web visitor events with TikTok users. Once matched, information shared via the Events API can be used to build targeting audiences, inform the optimization algorithm and better measure campaign results.",
     "Events API cho Web sử dụng thông tin khách hàng như TikTok Click ID (`ttclid`), Đối sánh nâng cao (Advanced Matching), cùng các tín hiệu bổ sung như địa chỉ IP và User Agent để khớp các sự kiện của khách truy cập trang web với người dùng TikTok. Sau khi khớp, dữ liệu được chia sẻ có thể dùng để xây dựng tệp đối tượng nhắm mục tiêu, cung cấp tín hiệu cho thuật toán tối ưu hóa và đo lường kết quả chiến dịch tốt hơn."),
    ("After creating the event, you can verify web data connection setup and monitor activity. If you are sending events from both Pixel SDK and Events API, you will need to set up [event deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450).",
     "Sau khi tạo sự kiện, bạn có thể xác minh thiết lập kết nối dữ liệu web và theo dõi hoạt động. Nếu bạn gửi sự kiện từ cả Pixel SDK và Events API, bạn bắt buộc phải thiết lập [khử trùng lặp sự kiện (event deduplication)](do-luong-quang-cao-p1.md#doc-1771100965992450)."),
    ("For best practices of verifying Events API setup, see [Verify Events API setup](do-luong-quang-cao-p1.md#doc-1771100984456193).",
     "Để biết các phương pháp xác minh thiết lập Events API tối ưu nhất, hãy xem [Xác minh thiết lập Events API](do-luong-quang-cao-p1.md#doc-1771100984456193)."),
    ("To achieve optimal performance with the Events API 2.0, we recommend the following settings:",
     "Để đạt hiệu suất tối ưu với Events API 2.0, chúng tôi khuyến nghị áp dụng các cài đặt sau:"),
    ("1. Toggle on both first-party cookies and Automatic Advanced Matching from the Pixel settings in [TikTok Ads Manager](https://ads.tiktok.com/i18n/home) by navigating to **Tools** > **Events** > **Data sources**  > select a pixel > **Settings** tab. Refer to the screenshot below:",
     "1. Bật cả cookie bên thứ nhất (first-party cookies) và Khớp nâng cao tự động (Automatic Advanced Matching) trong phần cài đặt Pixel tại [TikTok Ads Manager](https://ads.tiktok.com/i18n/home) bằng cách điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)** > chọn pixel > tab **Cài đặt (Settings)**."),
    ("2. Set up [TikTok Click ID](do-luong-quang-cao-p1.md#doc-1771100879787009) and [cookies](do-luong-quang-cao-p1.md#doc-1771100936446977).",
     "2. Thiết lập [TikTok Click ID](do-luong-quang-cao-p1.md#doc-1771100879787009) và [cookie](do-luong-quang-cao-p1.md#doc-1771100936446977)."),
    ("3. Send Advanced Matching Data. To learn more about Advanced Matching, refer to [About Advanced Matching for Web](https://ads.tiktok.com/help/article/advanced-matching-web?redirected=2).",
     "3. Gửi dữ liệu Khớp nâng cao (Advanced Matching). Để tìm hiểu thêm về Khớp nâng cao, hãy tham khảo [Giới thiệu về Khớp nâng cao cho Web](https://ads.tiktok.com/help/article/advanced-matching-web?redirected=2)."),
    ("4. Use the recommended event payload format.", "4. Sử dụng định dạng tải trọng sự kiện được khuyến nghị."),
    
    # Doc 2 chi tiết
    ("a. In TikTok Ads Manager, navigate to **Tools** > **Events**.",
     "a. Trong TikTok Ads Manager, điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)**."),
    ("b. Click **Connect data source** > **Offline**.",
     "b. Nhấp vào **Kết nối nguồn dữ liệu (Connect data source)** > **Ngoại tuyến (Offline)**."),
    ("c. Enter the **Offline event set name** and select **Create**.",
     "c. Nhập **Tên bộ sự kiện ngoại tuyến (Offline event set name)** và chọn **Tạo (Create)**."),
    ("d. Turn on **Auto-tracking**: All future campaigns from this ad account will use this Offline Event Set for ad data connection and attribution.",
     "d. Bật **Tự động theo dõi (Auto-tracking)**: Tất cả các chiến dịch trong tương lai từ tài khoản quảng cáo này sẽ sử dụng Bộ sự kiện ngoại tuyến này để kết nối dữ liệu quảng cáo và phân bổ."),
    ("e. After creating the Offline Event Set, record the Offline Event Set ID (this will be used as the `event_source_id` for sending offline events via Events API).",
     "e. Sau khi tạo Bộ sự kiện ngoại tuyến, hãy ghi lại ID bộ sự kiện ngoại tuyến (giá trị này sẽ được dùng làm `event_source_id` để gửi sự kiện ngoại tuyến qua Events API)."),
    ("You can also create a new Offline Event Set using `/offline/create/`.",
     "Bạn cũng có thể tạo một Bộ sự kiện ngoại tuyến mới bằng điểm cuối `/offline/create/`."),
     
    # Doc 3 chi tiết
    ("A user in an Admin or Toán tử điều kiện role needs to perform these steps in your Ads Manager account.",
     "Người dùng có vai trò Quản trị viên (Admin) hoặc Nhà điều hành (Operator) cần thực hiện các bước này trong tài khoản Ads Manager."),
    ("Fill in your app download URL and proceed. The app icon, app name, and app ID will be populated automatically.",
     "Điền URL tải xuống ứng dụng của bạn và tiếp tục. Biểu tượng ứng dụng, tên ứng dụng và ID ứng dụng sẽ tự động được điền."),
    ("Select **\"Use TikTok Events API\"** and proceed.",
     "Chọn **\"Sử dụng TikTok Events API\"** và tiếp tục."),
    ("The app is now created, and you will see some recommended events for your app. Recommendations are provided for specific verticals. Once you have noted these down, click **Finish** to be taken to your app detail page.",
     "Ứng dụng hiện đã được tạo và bạn sẽ thấy một số sự kiện được đề xuất cho ứng dụng của mình dựa theo ngành nghề cụ thể. Sau khi ghi lại, hãy nhấp vào **Hoàn tất (Finish)** để chuyển tới trang chi tiết ứng dụng."),
    ("Your **App ID** will be in either reverse DNS format (Android), or short numerical string (iOS) typically present in app store or play store URLs. Your **TikTok App ID** is a longer numerical string, and specific to your ad account. This will be used as the `event_source_id` for sending app events via Events API 2.0.",
     "**App ID** của bạn sẽ ở định dạng reverse DNS (Android) hoặc chuỗi số ngắn (iOS) thường thấy trong URL của App Store hoặc Google Play Store. **TikTok App ID** của bạn là một chuỗi số dài hơn, mang tính định danh riêng cho tài khoản quảng cáo của bạn. ID này sẽ được dùng làm `event_source_id` để gửi các sự kiện ứng dụng qua Events API 2.0."),

    # Doc 4 chi tiết
    ("Create a CRM Event Set using [/crm/create/](../12-api-reference/43-events-1-0-p2.md#doc-1861366342223874).",
     "Tạo một Bộ sự kiện CRM bằng điểm cuối [/crm/create/](../12-api-reference/43-events-1-0-p2.md#doc-1861366342223874)."),
    ("After creating the CRM Event Set, record the CRM Event Set ID (this will be used as the `event_source_id` for sending CRM events via Events API).",
     "Sau khi tạo Bộ sự kiện CRM, hãy ghi lại ID bộ sự kiện CRM (giá trị này sẽ được dùng làm `event_source_id` để gửi sự kiện CRM qua Events API)."),
    ("After you create an CRM Event Set, you need to upload CRM Events to your CRM Event Set. Events are defined as actions a visitor takes on your CRM system to achieve a business goal.",
     "Sau khi tạo Bộ sự kiện CRM, bạn cần tải các Sự kiện CRM lên Bộ sự kiện CRM của mình. Sự kiện được định nghĩa là các hành động mà khách hàng tiềm năng thực hiện trên hệ thống CRM của bạn để đạt được mục tiêu kinh doanh."),
    ("For details of supported CRM events, see [Supported Events - CRM Standard Events](do-luong-quang-cao-p1.md#doc-1771101186666498).",
     "Để biết chi tiết về các sự kiện CRM được hỗ trợ, hãy xem [Các sự kiện được hỗ trợ - Sự kiện CRM tiêu chuẩn](do-luong-quang-cao-p1.md#doc-1771101186666498)."),

    # Doc 5 chi tiết
    ("All top-level parameters that are labeled as \"Required\" are required for all event sources (web, app, offline, or CRM (Customer relationship management) systems).",
     "Tất cả các tham số cấp cao nhất được gắn nhãn \"Bắt buộc\" đều bắt buộc đối với tất cả các nguồn sự kiện (hệ thống web, app, offline hoặc CRM)."),

    # Doc 6 chi tiết
    ("This guide takes you through the process of using the Payload Converter for the Events API.",
     "Hướng dẫn này sẽ dẫn dắt bạn qua quy trình sử dụng Bộ chuyển đổi tải trọng (Payload Converter) cho Events API."),
    ("The Payload Converter provides a solution that automatically identifies the channel of an external payload, such as Meta, at TikTok's server side. It then converts it into a format equivalent for TikTok. As a result, advertisers can directly send pre-constructed events to TikTok via Events API.",
     "Payload Converter cung cấp một giải pháp tự động nhận diện kênh của tải trọng bên ngoài (chẳng hạn như Meta) tại phía máy chủ của TikTok, sau đó chuyển đổi sang định dạng tương đương cho TikTok. Nhờ đó, nhà quảng cáo có thể trực tiếp gửi các sự kiện đã cấu trúc sẵn sang TikTok thông qua Events API."),
    ("Please follow these [steps](do-luong-quang-cao-tom-tat.md#doc-1771100865818625) to get started with web data connection with TikTok to start sending events to TikTok using the Payload Converter.",
     "Vui lòng thực hiện theo [các bước này](do-luong-quang-cao-tom-tat.md#doc-1771100865818625) để bắt đầu kết nối dữ liệu web với TikTok trước khi gửi sự kiện bằng Payload Converter."),
    ("To send new events, make a `POST` request to Events API's endpoint: [https://business-api.tiktok.com/open_api/v1.3/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).",
     "Để gửi các sự kiện mới, hãy thực hiện yêu cầu `POST` tới điểm cuối của Events API: [https://business-api.tiktok.com/open_api/v1.3/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)."),
    ("The following **Demos of the Payload Converter** demonstrate how to send Meta Events via the TikTok Events API. Once the events arrive at TikTok, the payload converter will be triggered to convert the Meta Event into a TikTok Event.",
     "Các **bản demo Payload Converter** sau đây minh họa cách gửi sự kiện Meta qua TikTok Events API. Khi sự kiện đến TikTok, bộ chuyển đổi tải trọng sẽ tự động kích hoạt để chuyển đổi Sự kiện Meta thành Sự kiện TikTok tương đương."),
    ("If advertisers are already using the Meta Conversion API SDK, you can reuse the existing Meta code. By merely adding the \"Access-Token\" and \"X-Event-Source-ID\", you can effortlessly send Meta events to TikTok (for specific operations, refer to the following Java SDK example).",
     "Nếu nhà quảng cáo đã sử dụng Meta Conversions API SDK, bạn có thể tái sử dụng mã Meta hiện có. Chỉ cần thêm các tiêu đề \"Access-Token\" và \"X-Event-Source-ID\", bạn có thể dễ dàng gửi các sự kiện Meta sang TikTok (xem chi tiết trong ví dụ Java SDK bên dưới)."),
    ("After setting up the Payload Converter integration and before sending live events to TikTok, you can send test events to verify that the data connection is working properly. Please follow [these steps](do-luong-quang-cao-p1.md#doc-1771100984456193) to generate the test event code to include in the payload to send to TikTok. Once you have the test event code, please refer to the examples below on how to include the test event code to the payload.",
     "Sau khi thiết lập tích hợp Payload Converter và trước khi gửi sự kiện thực tế tới TikTok, bạn có thể gửi các sự kiện kiểm tra để xác minh kết nối dữ liệu hoạt động bình thường. Vui lòng làm theo [các bước này](do-luong-quang-cao-p1.md#doc-1771100984456193) để tạo mã sự kiện kiểm tra đưa vào tải trọng gửi tới TikTok."),
    ("Go to the **Test Events** tab of the Pixel in Events Manager, and look for the test event in the **Event Activity** section. Any issues with the payload will show up to help you resolve the issues.",
     "Chuyển đến tab **Kiểm tra sự kiện (Test Events)** của Pixel trong Trình quản lý sự kiện và tìm sự kiện kiểm tra trong phần **Hoạt động sự kiện (Event Activity)**. Mọi vấn đề với tải trọng sẽ hiển thị để giúp bạn giải quyết sự cố."),
    ("Make sure to remove `test_event_code` before switching to 'Production' mode.",
     "Hãy đảm bảo xóa bỏ trường `test_event_code` trước khi chuyển sang chế độ sản xuất chính thức ('Production')."),
    ("Deduplication is needed for advertisers who are using both TikTok Pixel SDK and Events API to send the same event, allowing TikTok to better report/optimize your campaign performance. Learn more about [Event Deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450).",
     "Khử trùng lặp là bắt buộc đối với nhà quảng cáo sử dụng cả TikTok Pixel SDK và Events API để gửi cùng một sự kiện, giúp TikTok báo cáo và tối ưu hóa hiệu suất chiến dịch tốt hơn. Tìm hiểu thêm về [Khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1771100965992450)."),
    ("When sending other platform's payload to Events API (i.e. leveraging the Payload Converter feature), you can set up [Cookie Deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450) to deduplicate events between TikTok Pixel and Events API.",
     "Khi gửi tải trọng của nền tảng khác tới Events API (tức tận dụng tính năng Payload Converter), bạn có thể thiết lập [Khử trùng lặp qua Cookie](do-luong-quang-cao-p1.md#doc-1771100965992450) để khử trùng lặp sự kiện giữa TikTok Pixel và Events API."),
    ("You will need to [enable first-party cookies](do-luong-quang-cao-p1.md#doc-1771100936446977) in your TikTok Pixel settings, and also send an extra `X-Ttp-Cookie` http request header with your Events API request. The `X-Ttp-Cookie` header's value should be the cookie value of TikTok first-party cookie (`_ttp`).  An example curl request:",
     "Bạn sẽ cần [bật cookie bên thứ nhất](do-luong-quang-cao-p1.md#doc-1771100936446977) trong cài đặt TikTok Pixel của mình và gửi thêm tiêu đề yêu cầu HTTP `X-Ttp-Cookie` cùng với yêu cầu Events API. Giá trị của tiêu đề `X-Ttp-Cookie` phải là giá trị cookie bên thứ nhất của TikTok (`_ttp`). Ví dụ yêu cầu cURL:"),
    ("For API error response handling, please refer to [this doc](do-luong-quang-cao-p1.md#doc-1771101162079234).",
     "Để xử lý phản hồi lỗi API, vui lòng tham khảo [tài liệu này](do-luong-quang-cao-p1.md#doc-1771101162079234)."),
    ("## Deduplication with Payload Converter", "## Khử trùng lặp với Payload Converter"),
    ("## Responses & Errors", "## Phản hồi và Xử lý lỗi (Responses & Errors)"),
    ("## Send Requests", "## Gửi yêu cầu (Send Requests)"),
    ("## Verify Events Setup", "## Xác minh thiết lập sự kiện (Verify Events Setup)"),
    ("### Java Non-SDK Sample", "### Mã mẫu Java không dùng SDK (Java Non-SDK Sample)"),
    ("### Python Non-SDK Sample", "### Mã mẫu Python không dùng SDK (Python Non-SDK Sample)"),
    ("### Python SDK", "### Python SDK"),
    ("### Java SDK", "### Java SDK"),
    ("### cURL", "### cURL"),
]

# Áp dụng thay thế cho từng doc 1 đến 6
for i in range(1, 7):
    doc_text = docs[i]
    for old, new in common_replacements:
        if old in doc_text:
            doc_text = doc_text.replace(old, new)
    docs[i] = doc_text

# Ghi lại file tom-tat.md
new_text = "".join(docs)
with open(TOM_TAT_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Đã cập nhật Docs 1-6 trong {TOM_TAT_PATH} (Độ dài: {len(new_text)})")
