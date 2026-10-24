#!/usr/bin/env python3
"""
Biên dịch tiếng Việt cho Docs 7-12 của u124 (do-luong-quang-cao-tom-tat.md).
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOM_TAT_PATH = os.path.join(ROOT, "docs/09-marketing-api/do-luong-quang-cao-tom-tat.md")

with open(TOM_TAT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

docs = re.split(r"(?=<a id=\"doc-\d+\"></a>)", text)

# 1. Cập nhật TOC cho Docs 7-12
toc_replacements = [
    ("- [7. Events API : App (#doc-1739584805049345)](#doc-1739584805049345)",
     "- [7. Events API : App (Sự kiện ứng dụng 1.0) (#doc-1739584805049345)](#doc-1739584805049345)"),
    ("- [8. Report web events and parameters (#doc-1741601162187777)](#doc-1741601162187777)",
     "- [8. Báo cáo sự kiện Web và tham số (1.0) (#doc-1741601162187777)](#doc-1741601162187777)"),
    ("- [9. Report Offline Events and Parameters (#doc-1758053486938113)](#doc-1758053486938113)",
     "- [9. Báo cáo sự kiện Ngoại tuyến và tham số (1.0) (#doc-1758053486938113)](#doc-1758053486938113)"),
    ("- [10. Android installation (#doc-1739585434183746)](#doc-1739585434183746)",
     "- [10. Cài đặt SDK trên Android (#doc-1739585434183746)](#doc-1739585434183746)"),
    ("- [11. iOS installation (#doc-1739585432134657)](#doc-1739585432134657)",
     "- [11. Cài đặt SDK trên iOS (#doc-1739585432134657)](#doc-1739585432134657)"),
    ("- [12. Unity installation (#doc-1824036608950273)](#doc-1824036608950273)",
     "- [12. Cài đặt SDK trên Unity (#doc-1824036608950273)](#doc-1824036608950273)"),
]

for old, new in toc_replacements:
    if old in docs[0]:
        docs[0] = docs[0].replace(old, new)

# 2. Từ điển thay thế cho Docs 7-12
replacements_7_12 = [
    # Tiêu đề chung
    ("# Events API : App", "# Events API : App (Sự kiện ứng dụng 1.0)"),
    ("# Report web events and parameters", "# Báo cáo sự kiện Web và tham số (1.0)"),
    ("# Report Offline Events and Parameters", "# Báo cáo sự kiện Ngoại tuyến và tham số (1.0)"),
    ("# Android installation", "# Cài đặt SDK trên Android (Android installation)"),
    ("# iOS installation", "# Cài đặt SDK trên iOS (iOS installation)"),
    ("# Unity installation", "# Cài đặt SDK trên Unity (Unity installation)"),
    ("## Overview", "## Tổng quan (Overview)"),
    ("## Benefits", "## Lợi ích (Benefits)"),
    ("## Notes", "## Lưu ý (Notes)"),
    ("## Process Overview", "## Quy trình tổng quan (Process Overview)"),
    ("# Supported web events", "# Các sự kiện Web được hỗ trợ"),
    ("# Supported Offline Events", "# Các sự kiện Ngoại tuyến được hỗ trợ"),
    ("# Supported parameters", "# Các tham số được hỗ trợ"),
    ("## Event parameters", "## Tham số sự kiện (Event parameters)"),
    ("## `properties` object parameters", "## Tham số đối tượng `properties`"),
    ("## `context` object parameters", "## Tham số đối tượng `context`"),
    ("### Context object", "### Đối tượng Context (Context object)"),
    ("### Properties object", "### Đối tượng Properties (Properties object)"),
    ("# Report a web event", "# Báo cáo một sự kiện Web"),
    ("# Report web events in bulk", "# Báo cáo sự kiện Web hàng loạt"),
    ("# Report an Offline Event", "# Báo cáo một sự kiện Ngoại tuyến"),
    ("# Report Offline Events in Bulk", "# Báo cáo sự kiện Ngoại tuyến hàng loạt"),
    ("## Report App Events in Bulk", "## Báo cáo sự kiện ứng dụng hàng loạt"),
    ("# User context object parameters", "# Tham số đối tượng ngữ cảnh người dùng (User context)"),
    ("# Properties object parameters", "# Tham số đối tượng thuộc tính (Properties object)"),
    
    # Tiêu đề SDK (Android, iOS, Unity)
    ("## Add the SDK as a build dependency", "## Thêm SDK làm phần phụ thuộc bản dựng (Build dependency)"),
    ("### Maven integration (recommended)", "### Tích hợp qua Maven (Khuyến nghị)"),
    ("### Manual integration", "### Tích hợp thủ công (Manual integration)"),
    ("### Add permissions", "### Khai báo quyền (Permissions)"),
    ("### Proguard obfuscation", "### Cấu hình làm mờ mã Proguard"),
    ("## Configure and initialize the SDK", "## Cấu hình và khởi tạo SDK"),
    ("### Delaying event transmission", "### Trì hoãn truyền phát sự kiện"),
    ("## App event reporting", "## Báo cáo sự kiện ứng dụng"),
    ("### Automatically logged events", "### Các sự kiện được ghi tự động"),
    ("### Manually logged events", "### Các sự kiện ghi thủ công"),
    ("#### Standard events", "#### Các sự kiện tiêu chuẩn (Standard events)"),
    ("#### Adding properties to standard events", "#### Thêm thuộc tính vào sự kiện tiêu chuẩn"),
    ("#### In-app ad revenue", "#### Doanh thu quảng cáo trong ứng dụng (In-app ad revenue)"),
    ("#### Custom events", "#### Các sự kiện tùy chỉnh (Custom events)"),
    ("## Enable Advanced Matching", "## Bật Khớp nâng cao (Advanced Matching)"),
    ("## Enable advanced matching", "## Bật Khớp nâng cao (Advanced Matching)"),
    ("## Verify your integration", "## Xác minh tích hợp của bạn"),
    ("### Codeless test events (recommended)", "### Sự kiện kiểm tra không cần viết mã (Khuyến nghị)"),
    ("### Manual debug mode", "### Chế độ gỡ lỗi thủ công (Manual debug mode)"),
    ("#### Enabling debug mode", "#### Bật chế độ gỡ lỗi"),
    ("#### Disabling debug mode", "#### Tắt chế độ gỡ lỗi"),
    ("### Generate and verify events", "### Tạo và xác minh sự kiện"),
    ("## Additional features and guidance", "## Các tính năng bổ sung và hướng dẫn"),
    ("### CocoaPods integration", "### Tích hợp qua CocoaPods"),
    ("### Swift Package Manager integration", "### Tích hợp qua Swift Package Manager (SPM)"),
    ("### Manual integration (xcframework)", "### Tích hợp thủ công (xcframework)"),
    ("### Configure build settings", "### Cấu hình cài đặt bản dựng (Build settings)"),
    ("### Configure for App Tracking Transparency (ATT)", "### Cấu hình App Tracking Transparency (ATT)"),
    ("### Configure SKAdNetwork updates in your app", "### Cấu hình cập nhật SKAdNetwork trong ứng dụng"),
    ("#### About StoreKit transaction reporting", "#### Về việc báo cáo giao dịch StoreKit"),
    ("### Migrating to Unity from existing native Android or iOS SDKs", "### Di chuyển sang Unity từ Android/iOS SDK gốc hiện có"),
    ("## Platform setup notes", "## Lưu ý thiết lập theo từng nền tảng"),
    ("### Android: Permissions, Proguard, and Gradle options", "### Android: Quyền, Proguard và cấu hình Gradle"),
    ("### iOS: AppTrackingTransparency (ATT) and SKAdNetwork", "### iOS: AppTrackingTransparency (ATT) và SKAdNetwork"),

    # Văn bản mô tả Doc 7
    ("TikTok’s Events API is a secure server-to-server interface that allows advertisers to share the actions that people take on their app with TikTok.",
     "TikTok Events API là một giao diện máy chủ-tới-máy chủ (server-to-server) an toàn cho phép nhà quảng cáo chia sẻ các hành động mà người dùng thực hiện trên ứng dụng của họ với TikTok."),
    ("1. **Streamlined stability and security:** Integrate and iterate without client-side limitations, like connectivity issues or ad-blockers.",
     "1. **Độ ổn định và bảo mật cao:** Tích hợp và vận hành mà không bị ảnh hưởng bởi giới hạn phía máy khách như sự cố kết nối mạng hay trình chặn quảng cáo."),
    ("2. **Configurable privacy controls:** Stay compliant with rapidly evolving requirements with flexible data sharing.",
     "2. **Kiểm soát quyền riêng tư linh hoạt:** Duy trì tuân thủ các quy định bảo mật liên tục thay đổi với cơ chế chia sẻ dữ liệu có thể tùy biến."),
    ("3. **Maximum event measurement:** Capture more events with improved accuracy across different browsers and platforms.",
     "3. **Tối đa hóa hiệu quả đo lường:** Thu thập nhiều sự kiện hơn với độ chính xác nâng cao trên các nền tảng và trình duyệt khác nhau."),
    ("For user-level data on iOS14 or higher, we expect advertisers to adhere to Apple’s policies around App Tracking Transparency. TikTok will not use ATT-restricted data for ad measurement and optimization purposes.",
     "Đối với dữ liệu cấp người dùng trên iOS 14 trở lên, chúng tôi yêu cầu nhà quảng cáo tuân thủ chính sách App Tracking Transparency của Apple. TikTok sẽ không sử dụng dữ liệu bị hạn chế bởi ATT cho mục đích đo lường và tối ưu hóa quảng cáo."),
    ("Currently, we do not accept custom events or personally identifiable information through this API.",
     "Hiện tại, chúng tôi không chấp nhận các sự kiện tùy chỉnh hoặc thông tin nhận dạng cá nhân (PII) qua API này."),
    ("A request only reports events to one mobile app ID. This restriction is mostly because authorization is done at the mobile app ID level.",
     "Một yêu cầu chỉ báo cáo các sự kiện cho một Mobile App ID duy nhất, do việc ủy quyền được thực hiện ở cấp độ Mobile App ID."),
    ("To report a single app event to TikTok, use the `/app/track/` endpoint. To report app events in bulk, use the `/app/batch/` endpoint.",
     "Để báo cáo một sự kiện ứng dụng đơn lẻ tới TikTok, sử dụng điểm cuối `/app/track/`. Để báo cáo sự kiện ứng dụng hàng loạt, sử dụng điểm cuối `/app/batch/`."),

    # Văn bản mô tả Doc 8
    ("This article lists supported web events and parameters when you report web events using [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) or [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225).",
     "Bài viết này liệt kê các sự kiện web và tham số được hỗ trợ khi bạn báo cáo sự kiện web qua điểm cuối [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) hoặc [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225)."),
    ("There are two categories of events on TikTok:\n- **Standard Events**: these are actions with predefined names created by TikTok. Standard events are supported across all TikTok measurement and ad products.\n- **Custom Events**: these are actions that TikTok partners can define themselves beyond the predefined standard events.",
     "Có hai danh mục sự kiện trên TikTok:\n- **Sự kiện tiêu chuẩn (Standard Events)**: Là các hành động có tên được xác định trước bởi TikTok, được hỗ trợ trên toàn bộ sản phẩm đo lường và quảng cáo.\n- **Sự kiện tùy chỉnh (Custom Events)**: Là các hành động do đối tác của TikTok tự định nghĩa ngoài danh sách sự kiện tiêu chuẩn."),
    ("The table below lists 18 standard web events, as well as recommended values in `properties` object.",
     "Bảng dưới đây liệt kê 18 sự kiện web tiêu chuẩn cùng các giá trị được khuyến nghị trong đối tượng `properties`."),
    ("This section introduces supported event parameters, `context` object parameters, and `properties` object parameters.",
     "Phần này giới thiệu các tham số sự kiện, tham số đối tượng `context`, và tham số đối tượng `properties` được hỗ trợ."),

    # Bảng Doc 8 events
    ("When a page is viewed.", "Khi một trang được xem."),
    ("When a search is made.", "Khi một tìm kiếm được thực hiện."),
    ("When an item is added to a wishlist.", "Khi một mặt hàng được thêm vào danh sách yêu thích."),
    ("When an item is added to the shopping cart.", "Khi một mặt hàng được thêm vào giỏ hàng."),
    ("When an application is approved.", "Khi một đơn đăng ký được phê duyệt."),
    ("When the checkout process is started.", "Khi quy trình thanh toán được bắt đầu."),
    ("When payment information is added in the checkout flow.", "Khi thông tin thanh toán được thêm trong luồng thanh toán."),
    ("When a payment is completed.", "Khi giao dịch thanh toán hoàn tất thành công."),
    ("When contact or consultation occurs.", "Khi có liên hệ hoặc tư vấn diễn ra."),
    ("When a button to open an external browser download page is clicked.", "Khi nút mở trang tải xuống trình duyệt bên ngoài được nhấp."),
    ("When a form is submitted.", "Khi biểu mẫu khách hàng tiềm năng được gửi."),
    ("When a registration is completed.", "Khi đăng ký tài khoản hoàn tất."),
    ("When someone begins a free trial of a product or service.", "Khi người dùng bắt đầu dùng thử miễn phí sản phẩm hoặc dịch vụ."),
    ("When someone submits an application.", "Khi người dùng gửi đơn đăng ký."),
    ("When a subscription is made.", "Khi đăng ký thuê bao/dịch vụ được kích hoạt."),
    ("When someone customizes a product.", "Khi người dùng tùy chỉnh sản phẩm."),
    ("When someone tries to find your location.", "Khi người dùng tìm kiếm vị trí cửa hàng/chi nhánh."),
    ("When someone makes an appointment to speak with your business or visit your location.", "Khi người dùng đặt lịch hẹn trao đổi hoặc ghé thăm địa điểm của bạn."),

    # Văn bản mô tả Doc 9
    ("This article lists supported Offline Events and parameters when you report Offline Events using [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) or [/v1.3/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482).",
     "Bài viết này liệt kê các sự kiện ngoại tuyến và tham số được hỗ trợ khi bạn báo cáo sự kiện ngoại tuyến qua điểm cuối [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) hoặc [/v1.3/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482)."),
    ("Events are defined as actions an offline visitor takes to achieve a business goal. Standard events are supported across all TikTok measurement and ad products.",
     "Sự kiện được định nghĩa là các hành động mà khách hàng ngoại tuyến thực hiện để đạt được mục tiêu kinh doanh. Sự kiện tiêu chuẩn được hỗ trợ trên toàn bộ sản phẩm đo lường và quảng cáo của TikTok."),
    ("You can report an Offline Event using [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857).",
     "Bạn có thể báo cáo một sự kiện ngoại tuyến bằng điểm cuối [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857)."),

    # Văn bản SDK Doc 10, 11, 12
    ("The TikTok App Events SDK for Android is maintained in a [public GitHub repository](https://github.com/tiktok/tiktok-business-android-sdk).",
     "TikTok App Events SDK dành cho Android được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-android-sdk)."),
    ("The TikTok App Events SDK for iOS is maintained in a [public GitHub repository](https://github.com/tiktok/tiktok-business-ios-sdk).",
     "TikTok App Events SDK dành cho iOS được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-ios-sdk)."),
    ("The TikTok App Events SDK for Unity is maintained in a [public GitHub repository](https://github.com/tiktok/tiktok-business-unity-sdk).",
     "TikTok App Events SDK dành cho Unity được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-unity-sdk)."),
    ("Before you begin, ensure you have the following from your TikTok for Business account:",
     "Trước khi bắt đầu, hãy đảm bảo bạn đã chuẩn bị các thông tin sau từ tài khoản TikTok For Business:"),
    ("- Your Android App's **App ID** (e.g., `com.example.app`). This is your application's package name.",
     "- **App ID** ứng dụng Android của bạn (ví dụ: `com.example.app`). Đây là tên package của ứng dụng."),
    ("- Your Apple App's **App ID** (e.g., `123456789`). This is your application's numeric Apple App Store ID.",
     "- **App ID** ứng dụng Apple của bạn (ví dụ: `123456789`). Đây là ID chuỗi số trên Apple App Store."),
    ("- A **TikTok App ID** from your app's settings page in Events Manager.",
     "- **TikTok App ID** lấy từ trang cài đặt ứng dụng trong Trình quản lý sự kiện."),
    ("- An **App Secret** for verification.",
     "- **App Secret** phục vụ việc xác thực bảo mật."),
    ("In your `AndroidManifest.xml` file, declare the `INTERNET` and `AD_ID` permissions.",
     "Trong tệp `AndroidManifest.xml`, hãy khai báo các quyền `INTERNET` và `AD_ID`."),
    ("To prevent the SDK from being removed or broken in release builds, add the following rules to your app's `proguard-rules.pro` file:",
     "Để tránh việc SDK bị loại bỏ hoặc lỗi trong các bản dựng phát hành (release builds), hãy thêm các quy tắc sau vào tệp `proguard-rules.pro` của bạn:"),
    ("The SDK only supports initialization and use in the main process and main thread. On the first initialization, the SDK automatically collects an `InstallApp` event.",
     "SDK chỉ hỗ trợ khởi tạo và sử dụng trong tiến trình chính (main process) và luồng chính (main thread). Trong lần khởi tạo đầu tiên, SDK sẽ tự động thu thập sự kiện `InstallApp`."),
    ("We have supported Swift Package Manager since 1.3.8.",
     "Chúng tôi hỗ trợ Swift Package Manager từ phiên bản 1.3.8 trở lên."),
    ("In your `Podfile`, add the `TikTokBusinessSDK` pod:",
     "Trong tệp `Podfile` của bạn, thêm pod `TikTokBusinessSDK`:"),
    ("Install the pod by running the following command in your project directory:",
     "Cài đặt pod bằng cách chạy lệnh sau trong thư mục dự án của bạn:"),
]

for i in range(7, 13):
    doc_text = docs[i]
    for old, new in replacements_7_12:
        doc_text = doc_text.replace(old, new)
    docs[i] = doc_text

new_text = "".join(docs)
with open(TOM_TAT_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Đã cập nhật dịch cho Docs 7-12 trong {TOM_TAT_PATH}")
