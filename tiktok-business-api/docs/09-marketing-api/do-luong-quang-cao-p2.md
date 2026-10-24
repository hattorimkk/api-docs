# Hướng dẫn đo lường quảng cáo (Ad Measurement) — phần 2/2

> Phân hệ: guide:Marketing API/Ad Measurement.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Nâng cấp SDK (Upgrading the SDK) (#doc-1876487882210706)](#doc-1876487882210706)
- [2. SDK kết hợp TikTok App Events và Pangle (#doc-1828926473158657)](#doc-1828926473158657)
- [3. Cấu hình báo cáo sự kiện trong tích hợp Pangle SDK hiện có (#doc-1862344912338497)](#doc-1862344912338497)
- [4. Các tính năng bổ sung (Additional features) (#doc-1862350524297618)](#doc-1862350524297618)
- [5. Đo lường dự đoán nâng cao (Advanced Predictive Measurement) (#doc-1862348642630658)](#doc-1862348642630658)
- [6. Deeplink và Deeplink trì hoãn (Deferred Deeplink) (#doc-1862348999629826)](#doc-1862348999629826)
- [7. Tăng cường gửi trả dữ liệu (Enhance data postback) (#doc-1862351781303361)](#doc-1862351781303361)
- [8. Báo cáo SKAdNetwork và ánh xạ lược đồ (#doc-1862352021568001)](#doc-1862352021568001)
- [9. Các phương pháp tuân thủ tối ưu (#doc-1862352195035138)](#doc-1862352195035138)
- [10. Sử dụng dữ liệu hạn chế (Limited Data Use) (#doc-1774559446000642)](#doc-1774559446000642)
- [11. Kiểm soát giới hạn độ tuổi (Age Gating) (#doc-1824048170680450)](#doc-1824048170680450)
- [12. Tài liệu tham khảo (Reference) (#doc-1862286300697794)](#doc-1862286300697794)
- [13. Hằng số và lớp sự kiện chuẩn (Standard event constants and classes) (#doc-1862287695864834)](#doc-1862287695864834)
- [14. Ứng dụng di động (Mobile apps) (#doc-1739583651652673)](#doc-1739583651652673)
- [15. Các sự kiện ứng dụng được hỗ trợ (Supported app events) (#doc-1739585574120449)](#doc-1739585574120449)
- [16. TikTok Pixel (#doc-1739583652957185)](#doc-1739583652957185)
- [17. Các sự kiện Pixel được hỗ trợ (Supported Pixel events) (#doc-1739585696931842)](#doc-1739585696931842)
- [18. Khớp nâng cao (Advanced Matching) (#doc-1739585700402178)](#doc-1739585700402178)
- [19. Chế độ đồng ý Cookie Pixel (Pixel Cookie consent mode) (#doc-1795929012554754)](#doc-1795929012554754)
- [20. Làm việc với Single Page Applications (SPA) (#doc-1801524003169281)](#doc-1801524003169281)
- [21. Làm việc với Chính sách bảo mật nội dung (CSP) (#doc-1739585704427522)](#doc-1739585704427522)
- [22. Chế độ gỡ lỗi (Debug mode) (#doc-1739585706138625)](#doc-1739585706138625)
- [23. Sử dụng dữ liệu hạn chế (Limited Data Use) (#doc-1770092377990145)](#doc-1770092377990145)
- [24. Tích hợp Google Tag Manager (GTM) (#doc-1799004006287425)](#doc-1799004006287425)
- [25. Thiết lập chỉ dùng TikTok Pixel (#doc-1799004034003969)](#doc-1799004034003969)
- [26. Các thay đổi vùng chứa GTM (GTM container changes) (#doc-1799004081342466)](#doc-1799004081342466)
- [27. Thiết lập sự kiện thủ công (Set up events manually) (#doc-1799004110681154)](#doc-1799004110681154)
- [28. Xác minh thiết lập GTM (Verify GTM setup) (#doc-1799004129683458)](#doc-1799004129683458)
- [29. Tham chiếu API (API reference) (#doc-1740963089558529)](#doc-1740963089558529)

---

<a id="doc-1876487882210706"></a>
<!-- doc_id: 1876487882210706 -->
<!-- doc_id: 1876487882210706 -->
# Nâng cấp SDK (Upgrading the SDK)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Nâng cấp SDK
> **Lưu ý:** 
> Trước khi nâng cấp TikTok App Events SDK, hãy xem lại các thay đổi mới nhất trong [Lịch sử phát hành](do-luong-quang-cao-p1.md#doc-1739584951798785) để nắm bắt các tác động tiềm ẩn đối với bản cài đặt hiện tại của bạn.

## Android
### 1. Nâng cấp các gói phụ thuộc (dependencies)
Cập nhật tệp `build.gradle` cấp ứng dụng của bạn để tham chiếu đến phiên bản SDK mới nhất:

```http
// curl
dependencies {
    // Update the version number to the latest release
    implementation 'com.github.tiktok:tiktok-business-android-sdk:1.7.1'
}
```

### 2. Đồng bộ hóa dự án
Nhấp vào **Sync Project with Gradle Files** trong Android Studio để tải và tích hợp phiên bản mới.

## iOS
### 1. Nâng cấp qua CocoaPods
Cập nhật `Podfile` của bạn với phiên bản TikTok App Events SDK mới:

```http
// curl
./gradlew clean assembleDebug
```

Chạy lệnh sau trong Terminal để cập nhật:
```bash
pod update TikTokBusinessSDK
```

### 2. Nâng cấp qua Swift Package Manager
Nếu bạn sử dụng Swift Package Manager (SPM), hãy chọn dự án trong Xcode, chuyển đến tab **Package Dependencies**, chọn TikTokBusinessSDK và nhấp vào **Update Package**.

## Unity
1. Tải về gói `.unitypackage` phiên bản mới nhất từ kho lưu trữ chính thức của TikTok.
2. Trong Unity Editor, điều hướng tới **Assets** > **Import Package** > **Custom Package...** và chọn gói đã tải về.
3. Xem lại danh sách các tệp cập nhật và nhấp vào **Import** để ghi đè các tệp cũ.

## React Native
Cập nhật gói thư viện npm:
```bash
npm install tiktok-business-sdk@latest
# hoặc dùng yarn
yarn upgrade tiktok-business-sdk@latest
```
Sau đó đối với iOS, chạy lệnh cập nhật pods:
```bash
cd ios && pod update
```

---

<a id="doc-1828926473158657"></a>
<!-- doc_id: 1828926473158657 -->
<!-- doc_id: 1828926473158657 -->
# SDK kết hợp TikTok App Events và Pangle (Combined TikTok App Events and Pangle SDK)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > SDK kết hợp TikTok App Events và Pangle
## Tổng quan (Overview)
1. TikTok App Events SDK phiên bản 7.1.0.4 trở lên cho Android và phiên bản 7.7.0.0 trở lên cho iOS là một bộ SDK kết hợp (Combined SDK), bao gồm cả mô-đun TikTok App Events và Pangle SDK.
2. Bộ SDK kết hợp này cho phép các nhà phát triển vừa kiếm tiền qua mạng lưới quảng cáo Pangle, vừa theo dõi và báo cáo sự kiện ứng dụng cho TikTok thông qua một tích hợp duy nhất.
3. Nếu bạn đã tích hợp Pangle SDK, bạn có thể dễ dàng kích hoạt tính năng báo cáo sự kiện ứng dụng mà không cần cài đặt thêm thư viện riêng lẻ.

Xem chi tiết cấu hình tại [Cấu hình báo cáo sự kiện trong tích hợp Pangle SDK hiện có](do-luong-quang-cao-p2.md#doc-1862344912338497).

---

<a id="doc-1862344912338497"></a>
<!-- doc_id: 1862344912338497 -->
<!-- doc_id: 1862344912338497 -->
# Cấu hình báo cáo sự kiện trong tích hợp Pangle SDK hiện có
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > SDK kết hợp TikTok App Events và Pangle > Cấu hình báo cáo sự kiện trong tích hợp Pangle SDK hiện có
> **Quan trọng:** 
> Việc sử dụng TikTok App Events SDK tuân thủ [Điều khoản thương mại TikTok For Business](https://ads.tiktok.com/i18n/official/policy/commercial-terms).

## Cấu hình trên Android
Để kích hoạt báo cáo sự kiện ứng dụng TikTok trong ứng dụng đã tích hợp Pangle SDK trên Android:
1. Thêm cấu hình TikTok App ID trong tệp `AndroidManifest.xml` hoặc truyền vào khi khởi tạo Pangle SDK.
2. Gọi hàm khởi tạo mô-đun sự kiện:

```http
// curl
// project/build.gradle
allprojects {
    repositories {
        google()
    }
}
```

## Cấu hình trên iOS
Để kích hoạt báo cáo sự kiện ứng dụng trên iOS:
1. Thêm cấu hình TikTok App ID và TikTok App Secret vào mã khởi tạo SDK.
2. Khởi tạo mô-đun TikTok Events khi ứng dụng khởi chạy trong `AppDelegate`:

```http
// curl
// app/build.gradle
android {
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  }
}

dependencies {
    // Required for automatic event reporting and lifecycle tracking
    implementation 'androidx.lifecycle:lifecycle-process:2.3.1'
    implementation 'androidx.lifecycle:lifecycle-common-java8:2.3.1'

    // Required for automatic in-app purchase reporting
    implementation 'com.android.billingclient:billing:6.1.0'

    // Required for Play Store install referrer attribution
    implementation 'com.android.installreferrer:installreferrer:2.2'
}
```

---

<a id="doc-1862350524297618"></a>
<!-- doc_id: 1862350524297618 -->
<!-- doc_id: 1862350524297618 -->
# Các tính năng bổ sung (Additional features)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các tính năng bổ sung
Phần này cung cấp tài liệu chi tiết về các tính năng nâng cao của TikTok App Events SDK:
- [**Đo lường dự đoán nâng cao (Advanced Predictive Measurement)**](do-luong-quang-cao-p2.md#doc-1862348642630658): Tăng cường đo lường chuyển đổi bằng cách tận dụng các tín hiệu thiết bị bổ sung từ SDK để cải thiện độ chính xác phân bổ.
- [**Deeplink và Deeplink trì hoãn (Deferred Deeplink)**](do-luong-quang-cao-p2.md#doc-1862348999629826): Điều hướng người dùng trực tiếp đến trang nội dung cụ thể trong ứng dụng sau khi nhấp vào quảng cáo hoặc sau khi cài đặt ứng dụng.
- [**Tăng cường gửi trả dữ liệu (Enhance data postback)**](do-luong-quang-cao-p2.md#doc-1862351781303361): Tự động thu thập siêu dữ liệu trang và hành vi nhấp nút trong ứng dụng để tối ưu hóa mô hình quảng cáo.
- [**Báo cáo SKAdNetwork và ánh xạ lược đồ**](do-luong-quang-cao-p2.md#doc-1862352021568001): Tích hợp khung SKAdNetwork của Apple để đo lường chuyển đổi bảo vệ quyền riêng tư trên iOS.

---

<a id="doc-1862348642630658"></a>
<!-- doc_id: 1862348642630658 -->
<!-- doc_id: 1862348642630658 -->
# Đo lường dự đoán nâng cao (Advanced Predictive Measurement)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các tính năng bổ sung > Đo lường dự đoán nâng cao
Tính năng Đo lường dự đoán nâng cao (khả dụng từ iOS SDK phiên bản 1.5.0 trở đi) cho phép TikTok sử dụng các tín hiệu thiết bị bổ sung như hãng sản xuất, dòng máy và phiên bản hệ điều hành được thu thập từ TikTok App Events SDK để xây dựng mô hình dự đoán hiệu suất phân bổ, giúp nhà quảng cáo tối ưu hóa chiến dịch hiệu quả hơn trong môi trường hạn chế nhận dạng cá nhân.

Để sử dụng tính năng này, hãy đảm bảo bạn nâng cấp SDK lên phiên bản mới nhất và bật tùy chọn tương ứng trong TikTok Events Manager.

---

<a id="doc-1862348999629826"></a>
<!-- doc_id: 1862348999629826 -->
<!-- doc_id: 1862348999629826 -->
# Deeplink và Deeplink trì hoãn (Deeplinks and deferred deeplinks)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các tính năng bổ sung > Deeplink và Deeplink trì hoãn
## Liên kết sâu thông thường (Deeplinks)
Deeplink được xử lý trực tiếp ở cấp độ ứng dụng gốc. Nếu bạn đã hỗ trợ Universal Links (trên iOS) hoặc App Links (trên Android), người dùng đã cài đặt ứng dụng khi nhấp vào quảng cáo sẽ được mở trực tiếp vào trang nội dung tương ứng trong app.

## Liên kết sâu trì hoãn (Deferred Deeplinks)
Deferred Deeplink cho phép điều hướng người dùng đến nội dung cụ thể trong ứng dụng ngay cả khi họ **chưa cài đặt ứng dụng** tại thời điểm nhấp vào quảng cáo:
1. Người dùng chưa cài đặt ứng dụng nhấp vào quảng cáo TikTok.
2. Người dùng được chuyển hướng đến App Store / Google Play để tải và cài đặt ứng dụng.
3. Khi người dùng mở ứng dụng lần đầu tiên, TikTok App Events SDK sẽ truy xuất liên kết đích ban đầu và chuyển tiếp cho mã ứng dụng của bạn xử lý.

### Cách triển khai trên Android:
```http
// curl
// Request a deferred deeplink using this method after successful SDK initialisation
TikTokBusinessSdk.fetchDeferredDeeplinkWithCompletion(new TikTokBusinessSdk.FetchDeferredDeeplinkCompletion() {
    @Override
    public void completion(String deepLinkUrl, ErrorData errorData) {
        if(TextUtils.isEmpty(deepLinkUrl)){
            Log.e("DeferredDeeplink","Failed to fetch deferred deeplink. Code:" + errorData.getCode() + " Msg:"+ errorData.getMsg());
        } else {
            Log.e("DeferredDeeplink","Deferred deeplink fetched:" + deepLinkUrl);
            Uri uri = Uri.parse(deepLinkUrl);
            Intent intent = new Intent(Intent.ACTION_VIEW);
            intent.setData(uri);
            getActivity().startActivity(intent);
        }
    }
});
```

### Cách triển khai trên iOS:
```http
// curl
// Swift
// Request a deferred deeplink using this method after successful SDK initialisation
TikTokBusiness.fetchDeferredDeeplink { url, error **in**
    **if** error != **nil** {
        print("Failed to fetch deferred deeplink: \(String(describing: error?.localizedDescription))")
    } **else** {
        print("Deferred deeplink fetched: \(url!.absoluteString)")
        **if** url != **nil** && UIApplication.shared.canOpenURL(url!) {
            UIApplication.shared.open(url!, options: [:], completionHandler: **nil**)
        }
    }
}
```

---

<a id="doc-1862351781303361"></a>
<!-- doc_id: 1862351781303361 -->
<!-- doc_id: 1862351781303361 -->
# Tăng cường gửi trả dữ liệu (Enhance data postback)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các tính năng bổ sung > Tăng cường gửi trả dữ liệu
Tính năng Tăng cường gửi trả dữ liệu (Enhance data postback - khả dụng từ SDK phiên bản 1.4.0 trở đi) tự động thu thập thông tin trang trong ứng dụng như siêu dữ liệu và các lượt nhấp nút bấm thông qua App Events SDK. Tính năng này giúp tối ưu hóa thuật toán phân phối quảng cáo của TikTok.

## Cơ chế kiểm soát tính năng (Feature controls)
Bảng dưới đây mô tả các cấp độ kiểm soát tính năng:

| Control type | Interface | Purpose | Scope |
|---|---|---|---|
| Front-end toggle | TikTok Events Manager | Bật hoặc tắt tính năng trên toàn bộ thiết bị. Sử dụng tùy chọn này để quản trị tập trung. | Toàn cầu (Global) |
| Client-side global toggle | Cấu hình SDK | Vô hiệu hóa tính năng trên mã nguồn client của ứng dụng. | Mã nguồn ứng dụng |
| Client-side low performance flag | Cấu hình SDK | Tối ưu hóa hiệu năng tính năng trên các thiết bị cấu hình thấp. | Thiết bị người dùng |

---

<a id="doc-1862352021568001"></a>
<!-- doc_id: 1862352021568001 -->
<!-- doc_id: 1862352021568001 -->
# Báo cáo SKAdNetwork và ánh xạ lược đồ (SKAdNetwork reporting and schema mapping)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các tính năng bổ sung > Báo cáo SKAdNetwork và ánh xạ lược đồ
TikTok App Events SDK hỗ trợ khung phân bổ SKAdNetwork (SKAN) của Apple để bảo vệ quyền riêng tư người dùng trên iOS.

## Các kịch bản cập nhật SKAN Conversion Value (CV)

| Scenario | Who updates SKAN CV | TikTok SDK SKAdNetwork support | SKAN schema in Events Manager |
|---|---|---|---|
| You use an MMP SDK and want to use the MMP's SKAN schema. | MMP SDK | Disable | Do not configure a schema in Events Manager. |
| You do not have an MMP, but another non-MMP SDK already updates SKAN CVs. | Other SDK (non-MMP) | Disable | Do not configure a schema in Events Manager. |
| You want the TikTok SDK to update SKAN CVs. | TikTok App Events SDK | Enable | Upload a SKAN schema to Events Manager. |

## Cấu trúc lược đồ ánh xạ SKAN 3.0

| conversion_value | event_name | min_revenue_usd | max_revenue_usd |
|---|---|---|---|
| Integer from 1-63. | The standard or custom event name to match. | The minimum revenue (inclusive) in USD. | The maximum revenue (inclusive) in USD. |

## Cấu trúc lược đồ ánh xạ SKAN 4.0

| postback_index | fine_conversion_value | coarse_conversion_value | event_name | min_revenue_usd | max_revenue_usd |
|---|---|---|---|---|---|
| The conversion window (0, 1, or 2). | Integer from 0-63. Only applicable for `postback_index` 0. | low, medium, or high. | The event name to match. | The minimum revenue (inclusive). | The maximum revenue (inclusive). |

---

<a id="doc-1862352195035138"></a>
<!-- doc_id: 1862352195035138 -->
<!-- doc_id: 1862352195035138 -->
# Các phương pháp tuân thủ tối ưu (Compliance best practices)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các phương pháp tuân thủ tối ưu
Nhằm đảm bảo tuân thủ các quy định pháp luật về quyền riêng tư và bảo vệ dữ liệu người dùng trên toàn cầu, TikTok cung cấp các tính năng hỗ trợ tuân thủ:
- [**Sử dụng dữ liệu hạn chế (Limited data use)**](do-luong-quang-cao-p2.md#doc-1774559446000642): Tính năng giúp doanh nghiệp kiểm soát việc sử dụng dữ liệu sự kiện tại các bang cụ thể của Hoa Kỳ.
- [**Kiểm soát giới hạn độ tuổi (Age Gating)**](do-luong-quang-cao-p2.md#doc-1824048170680450): Cơ chế ngăn chặn việc chia sẻ dữ liệu liên quan đến trẻ em dưới độ tuổi quy định cho TikTok.

---

<a id="doc-1774559446000642"></a>
<!-- doc_id: 1774559446000642 -->
<!-- doc_id: 1774559446000642 -->
# Sử dụng dữ liệu hạn chế (Limited Data Use)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các phương pháp tuân thủ tối ưu > Sử dụng dữ liệu hạn chế
Tính năng **"Sử dụng dữ liệu hạn chế" (Limited Data Use - LDU)** cho **TikTok App Events SDK** giúp các doanh nghiệp kiểm soát tốt hơn cách dữ liệu sự kiện ứng dụng được xử lý trong các hệ thống của TikTok, hỗ trợ tuân thủ các đạo luật quyền riêng tư tại Hoa Kỳ.

## Triển khai trên Android
Để bật LDU trên Android, thiết lập cờ `limitDataUse` trước khi gửi sự kiện:
```http
// curl
TikTokBusinessSdk.TTConfig ttConfig = new TikTokBusinessSdk.TTConfig(context)
        .setAppId("APP_ID")
        .setTTAppId("TIKTOK_APP_ID")
        .ttConfig.enableLimitedDataUse(); //Limited data use flag
TikTokBusinessSdk.initializeSdk(ttConfig);
```

## Triển khai trên iOS
Để bật LDU trên iOS, gọi hàm tương ứng trên cấu hình SDK:
```http
// curl
let config = TiTokConfig.init(appId: "APP_ID", tiktokAppId: TIKTOK_APP_ID)
config?.enableLDUMode() //Limited data use flag
TikTokBusiness.initializeSdk(config)
```

---

<a id="doc-1824048170680450"></a>
<!-- doc_id: 1824048170680450 -->
<!-- doc_id: 1824048170680450 -->
# Kiểm soát giới hạn độ tuổi (Age Gating)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Các phương pháp tuân thủ tối ưu > Kiểm soát giới hạn độ tuổi
Dữ liệu từ hoặc về Trẻ em (theo định nghĩa tại Điều 2.8 của [Điều khoản sản phẩm thương mại của TikTok](https://ads.tiktok.com/i18n/official/policy/business-products-terms)) tuyệt đối không được chia sẻ với TikTok for Business. 

TikTok App Events SDK cung cấp cơ chế gắn cờ độ tuổi để tự động vô hiệu hóa việc theo dõi và thu thập dữ liệu nếu người dùng là trẻ em chưa đủ độ tuổi quy định:

### Trên Android:
```http
// curl
// Disable auto start and do not fully initialize the SDK at this point
TTConfig ttConfig = new TTConfig(context)
                    .disableAutoStart(); // disable sending data here
...
```

### Trên iOS:
```http
// curl
// After the age gate is passed, fully initialize and start the sdk.
TikTokBusinessSdk.initializeSdk(ttConfig); // initialize the SDK
TiktokBusiness.startTrack(); // start sending data
```

---

<a id="doc-1862286300697794"></a>
<!-- doc_id: 1862286300697794 -->
<!-- doc_id: 1862286300697794 -->
# Tài liệu tham khảo (Reference)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Tài liệu tham khảo
- [**Hằng số và lớp sự kiện chuẩn (Standard event constants and classes)**](do-luong-quang-cao-p2.md#doc-1862287695864834): Liệt kê toàn bộ các hằng số tên sự kiện chuẩn và các lớp tiện ích được định nghĩa sẵn trong TikTok App Events SDK.

---

<a id="doc-1862287695864834"></a>
<!-- doc_id: 1862287695864834 -->
<!-- doc_id: 1862287695864834 -->
# Hằng số và lớp sự kiện chuẩn (Standard event constants and classes)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Tài liệu tham khảo > Hằng số và lớp sự kiện chuẩn
Tài liệu này cung cấp danh sách các hằng số tên sự kiện chuẩn trong TikTok App Events SDK. Việc sử dụng các hằng số này giúp đảm bảo tính nhất quán của dữ liệu sự kiện trên cả hai nền tảng Android và iOS.

## Danh sách hằng số sự kiện chuẩn (Standard event constants)

| Event | Android Constant | iOS Constant |
|---|---|---|
| `AchieveLevel` | `TikTokAppEvent.ACHIEVE_LEVEL` | `TikTokAppEventAchieveLevel` |
| `AddPaymentInfo` | `TikTokAppEvent.ADD_PAYMENT_INFO` | `TikTokAppEventAddPaymentInfo` |
| `AddToCart` | `TikTokAppEvent.ADD_TO_CART` | `TikTokAppEventAddToCart` |
| `AddToWishlist` | `TikTokAppEvent.ADD_TO_WISHLIST` | `TikTokAppEventAddToWishlist` |
| `Checkout` | `TikTokAppEvent.CHECKOUT` | `TikTokAppEventCheckout` |
| `CompleteTutorial` | `TikTokAppEvent.COMPLETE_TUTORIAL` | `TikTokAppEventCompleteTutorial` |
| `CreateGroup` | `TikTokAppEvent.CREATE_GROUP` | `TikTokAppEventCreateGroup` |
| `CreateRole` | `TikTokAppEvent.CREATE_ROLE` | `TikTokAppEventCreateRole` |
| `GenerateLead` | `TikTokAppEvent.GENERATE_LEAD` | `TikTokAppEventGenerateLead` |
| `InAppADClick` | `TikTokAppEvent.IN_APP_AD_CLICK` | `TikTokAppEventInAppADClick` |
| `InAppAdImpr` | `TikTokAppEvent.IN_APP_AD_IMPR` | `TikTokAppEventInAppADImpr` |
| `InstallApp` | `TikTokAppEvent.INSTALL_APP` | `TikTokAppEventInstallApp` |
| `JoinGroup` | `TikTokAppEvent.JOIN_GROUP` | `TikTokAppEventJoinGroup` |
| `LaunchAPP` | `TikTokAppEvent.LAUNCH_APP` | `TikTokAppEventLaunchAPP` |
| `LoanApplication` | `TikTokAppEvent.LOAN_APPLICATION` | `TikTokAppEventLoanApplication` |
| `LoanApproval` | `TikTokAppEvent.LOAN_APPROVAL` | `TikTokAppEventLoanApproval` |
| `LoanDisbursal` | `TikTokAppEvent.LOAN_DISBURSAL` | `TikTokAppEventLoanDisbursal` |
| `Login` | `TikTokAppEvent.LOGIN` | `TikTokAppEventLogin` |
| `Purchase` | `TikTokAppEvent.PURCHASE` | `TikTokAppEventPurchase` |
| `Rate` | `TikTokAppEvent.RATE` | `TikTokAppEventRate` |
| `Registration` | `TikTokAppEvent.REGISTRATION` | `TikTokAppEventRegistration` |
| `Search` | `TikTokAppEvent.SEARCH` | `TikTokAppEventSearch` |
| `SpendCredits` | `TikTokAppEvent.SPEND_CREDITS` | `TikTokAppEventSpendCredits` |
| `StartTrial` | `TikTokAppEvent.START_TRIAL` | `TikTokAppEventStartTrial` |
| `Subscribe` | `TikTokAppEvent.SUBSCRIBE` | `TikTokAppEventSubscribe` |
| `UnlockAchievement` | `TikTokAppEvent.UNLOCK_ACHIEVEMENT` | `TikTokAppEventUnlockAchievement` |
| `ViewContent` | `TikTokAppEvent.VIEW_CONTENT` | `TikTokAppEventViewContent` |
| `ImpressionLevelAdRevenue` | `TikTokAppEvent.IMPRESSION_LEVEL_AD_REVENUE` | `TikTokAppEventImpressionLevelAdRevenue` |

---

<a id="doc-1739583651652673"></a>
<!-- doc_id: 1739583651652673 -->
<!-- doc_id: 1739583651652673 -->
# Ứng dụng di động (Mobile apps)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Mobile apps
> **Quan trọng:** 
> Bằng việc sử dụng các điểm cuối Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

Để quảng bá ứng dụng di động (App) với TikTok For Business, bạn cần tạo một ứng dụng di động trong [Trình quản lý sự kiện TikTok (TikTok Event Manager)](https://ads.tiktok.com/help/article?aid=6754384850179850245) hoặc thông qua TikTok API for Business. Mỗi ứng dụng có thể được tham chiếu bởi nhiều quảng cáo dưới một tài khoản nhà quảng cáo và có thể được thiết lập làm đối tượng quảng bá. Ứng dụng được đề cập trong bài viết này không phải là ứng dụng nhà phát triển được tạo trên cổng TikTok API for Business, mà là ứng dụng di động thực tế mà bạn muốn quảng bá.

Các điểm cuối sau đây có sẵn để bạn quản lý ứng dụng di động:

* [Lấy danh sách ứng dụng (Get app list)](../12-api-reference/43-events-1-0-p1.md#doc-1740859313270786)
* [Lấy thông tin ứng dụng (Get app info)](../12-api-reference/43-events-1-0-p1.md#doc-1740859272887297)
* [Tạo ứng dụng (Create app)](../12-api-reference/43-events-1-0-p1.md#doc-1740859280958466)
* [Cập nhật ứng dụng (Update app)](../12-api-reference/43-events-1-0-p1.md#doc-1740859300069378)
* [Lấy sự kiện ứng dụng (Get app events)](../12-api-reference/43-events-1-0-p1.md#doc-1740859338750977)
* [Lấy sự kiện nhắm mục tiêu lại của ứng dụng (Get app retargeting events)](../12-api-reference/43-events-1-0-p1.md#doc-1740859371033601)

`Lưu ý` 

* ID ứng dụng (App ID) trong bài viết này đề cập đến ID của ứng dụng được quảng bá. Giá trị này chỉ có thể nhận được thông qua điểm cuối `/app/list/`.
* Ứng dụng không thể xóa sau khi đã tạo. Chúng chỉ có thể được chỉnh sửa.
* Bạn có thể cấu hình kết nối dữ liệu của bên thứ ba (MMP) để giám sát hiệu quả quảng cáo, vui lòng tham khảo [bài viết Trung tâm trợ giúp](https://ads.tiktok.com/help/article?aid=6669666107177041925) để biết thêm chi tiết.

> Liên kết liên quan
>
>* [Báo cáo sự kiện ứng dụng (Report app events)](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266)
>* [Quy trình tạo ứng dụng di động mới](https://ads.tiktok.com/help/article?aid=6754384850179850245)
>* [Ghi nhận phân bổ quảng cáo TikTok Ads](https://ads.tiktok.com/help/article?aid=6704457722424721413)

---

<a id="doc-1739585574120449"></a>
<!-- doc_id: 1739585574120449 -->
<!-- doc_id: 1739585574120449 -->
# Các sự kiện ứng dụng được hỗ trợ (Supported app events)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Mobile apps > Supported app events
> **Lưu ý:** Tên sự kiện phục vụ mục đích kết nối dữ liệu (trường `event`) khác với tên sự kiện khi tạo nhóm quảng cáo (trường `optimization_event`). Vui lòng xem các cột tương ứng để biết giá trị chính xác.

| Event name for event data connection (value for event field){25} | Description | Recommended values for properties field | Event name for ad group creation (value for optimization_event) |
|---|---|---|---|
| AchieveLevel | Đạt được một cấp độ (Achieve a level) |  | `UPDATE_LEVEL` |
| AddPaymentInfo | Thêm thông tin thanh toán (Add payment information) |  | `ADD_PAYMENT_INFO` |
| AddToCart | Thêm vào giỏ hàng (Add to cart) | `content_type`, `content_id`, `description`, `currency`, `value` | `IN_APP_CART` |
| AddToWishlist | Thêm vào danh sách yêu thích (Add to wishlist) | `content_type`, `content_id`, `description`, `currency`, `value` | `ADD_TO_WISHLIST` |
| Checkout | Bắt đầu thanh toán đơn hàng (Checkout) | `description`, `content_id`, `quantity`, `currency`, `value` | `IN_APP_ORDER` |
| CompleteTutorial | Hoàn thành hướng dẫn (Complete the tutorial) |  | `COMPLETE_TUTORIAL` |
| CreateGroup | Tạo nhóm (Create a group) |  | `CREATE_GROUP` |
| CreateRole | Tạo vai trò nhân vật (Create a role) |  | `CREATE_GAMEROLE` |
| GenerateLead | Tạo khách hàng tiềm năng (Generate a lead) |  | `SALES_LEAD` |
| InAppADClick | Nhấp vào quảng cáo trong ứng dụng (In-app ad click) |  | `IN_APP_AD_CLICK` |
| InAppADImpr | Lượt hiển thị quảng cáo trong ứng dụng (In-app ad impression) |  | `IN_APP_AD_IMPR` |
| InstallApp | Cài đặt ứng dụng (Install the app) |  | `ACTIVE` |
| JoinGroup | Tham gia nhóm (Join a group) |  | `JOIN_GROUP` |
| LaunchAPP | Khởi chạy ứng dụng (Launch the app) |  | `LAUNCH_APP` |
| LoanApplication | Nộp đơn xin vay (Apply for a loan) |  | `LOAN_APPLY` |
| LoanApproval | Khoản vay được duyệt (Loan is approved) |  | `LOAN_CREDIT` |
| LoanDisbursal | Giải ngân khoản vay (Loan is disbursed) |  | `LOAN_COMPLETION` |
| Login | Đăng nhập thành công (Log in successfully) |  | `LOGIN` |
| Purchase | Mua hàng hoàn tất (Purchase) | `content_type`, `content_id`, `description`, `currency`, `value` | `ACTIVE_PAY` |
| Rate | Đánh giá xếp hạng (Rate) |  | `RATE` |
| Registration | Hoàn tất đăng ký tài khoản (Complete the registration) |  | `ACTIVE_REGISTER` |
| Search | Tìm kiếm nội dung (Search) |  | `SEARCH` |
| SpendCredits | Tiêu dùng tín dụng/điểm (Spend credits) |  | `SPEND_CREDITS` |
| StartTrial | Bắt đầu dùng thử (Start the trial) |  | `START_TRIAL` |
| Subscribe | Đăng ký thuê bao (Subscribe) |  | `SUBSCRIBE` |
| UnlockAchievement | Mở khóa thành tựu (Unlock an achievement) |  | `UNLOCK_ACHIEVEMENT` |
| ViewContent | Xem chi tiết nội dung (View details) | `content_type`, `content_id`, `description`, `currency`, `value` | `IN_APP_DETAIL_UV` |

---

<a id="doc-1739583652957185"></a>
<!-- doc_id: 1739583652957185 -->
<!-- doc_id: 1739583652957185 -->
# TikTok Pixel
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel
> **Quan trọng:** 
> Bằng việc sử dụng các điểm cuối Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

TikTok Pixel là công cụ kết nối dữ liệu sự kiện trang web do TikTok For Business cung cấp. Công cụ này giúp việc đo lường hiệu quả quảng cáo trở nên dễ dàng hơn bằng cách nhúng đoạn mã pixel vào trang web. Bạn có thể định nghĩa nhiều sự kiện để đo lường các hành vi khác nhau của người dùng dưới mỗi pixel. `ID TikTok Pixel` và `Sự kiện Pixel` có **mối quan hệ một-nhiều (one-to-many).**

> Liên kết liên quan
>* [Giới thiệu về TikTok Pixel](https://ads.tiktok.com/help/article?aid=6669727593823993861)
>* [Quản lý sự kiện Pixel](https://ads.tiktok.com/help/article?aid=573722398920296903)

---

<a id="doc-1739585696931842"></a>
<!-- doc_id: 1739585696931842 -->
<!-- doc_id: 1739585696931842 -->
# Các sự kiện Pixel được hỗ trợ (Supported Pixel events)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Supported Pixel events
# Sự kiện Pixel (Pixel events)

Vui lòng xem toàn bộ 18 sự kiện Web tiêu chuẩn trong bảng dưới đây:

| Event name for ad creation (optimization_event) | Event name for event data connection (event) | Description | Recommended fields ⏎ in properties object |
|---|---|---|---|
| `ON_WEB_DETAIL` | ViewContent | Khi một trang web hoặc chi tiết sản phẩm được xem. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `ON_WEB_SEARCH` | Search | Khi một tìm kiếm được thực hiện trên trang web. |  |
| `ON_WEB_ADD_TO_WISHLIST` | AddToWishlist | Khi một mặt hàng được thêm vào danh sách yêu thích. |  |
| `ON_WEB_CART` | AddToCart | Khi một mặt hàng được thêm vào giỏ hàng mua sắm. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `INITIATE_ORDER` | InitiateCheckout | Khi quy trình thanh toán bắt đầu được khởi chạy. |  |
| `ADD_BILLING` | AddPaymentInfo | Khi thông tin thanh toán được nhập trong luồng thanh toán. |  |
| `SHOPPING` | Purchase | Khi một giao dịch thanh toán mua hàng hoàn tất thành công. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `CONSULT` | Contact | Khi có hành động liên hệ hoặc tư vấn diễn ra. |  |
| `DOWNLOAD_START` | Download | Khi nút mở trang tải xuống trình duyệt bên ngoài được nhấp. |  |
| `FORM` | Lead | Khi người dùng gửi một biểu mẫu khách hàng tiềm năng. |  |
| `ON_WEB_REGISTER` | CompleteRegistration | Khi một tài khoản hoàn tất quy trình đăng ký. |  |
| `ON_WEB_SUBSCRIBE` | Subscribe | Khi một gói thuê bao/đăng ký dịch vụ được kích hoạt. |  |
|  | CustomizeProduct | Khi người dùng tùy chỉnh thuộc tính của một sản phẩm. |  |
|  | FindLocation | Khi người dùng cố gắng tìm kiếm vị trí cửa hàng/chi nhánh của bạn. |  |
|  | Schedule | Khi người dùng đặt lịch hẹn gặp hoặc ghé thăm địa điểm. |  |
|  | ApplicationApproval | Khi một đơn đăng ký được phê duyệt. |  |
|  | StartTrial | Khi người dùng bắt đầu dùng thử miễn phí sản phẩm hoặc dịch vụ. | `currency`, `value` |
|  | SubmitApplication | Khi người dùng gửi một đơn đăng ký hoàn chỉnh. |  |
|  | LandingPageView | Khi người dùng truy cập thành công vào trang đích sau khi nhấp vào quảng cáo. |  |
|  | EngagedSession | Khi người dùng nhấp vào quảng cáo và ở lại trang đích trên 10 giây hoặc chuyển sang xem trang cấp hai. |  |

---

<a id="doc-1739585700402178"></a>
<!-- doc_id: 1739585700402178 -->
<!-- doc_id: 1739585700402178 -->
# Khớp nâng cao (Advanced Matching)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Advanced Matching
## Giới thiệu về Khớp nâng cao (Advanced Matching)
Khớp nâng cao giúp bạn tối ưu hóa quảng cáo TikTok và thúc đẩy hiệu quả bằng cách so khớp thông tin khách hàng với người dùng trên TikTok. Dữ liệu khách hàng đã băm (hashed) có thể được chia sẻ cùng với bất kỳ sự kiện TikTok nào nhằm ghi nhận phân bổ nhiều chuyển đổi hơn, xây dựng tệp đối tượng lớn hơn và cải thiện khả năng tối ưu hóa chiến dịch.
 
Có hai cách để kích hoạt Khớp nâng cao: thủ công (manual) hoặc tự động (automatic).
 
- **Khớp nâng cao thủ công (Manual Advanced Matching)** là việc truyền thông tin khách hàng từ trang web của bạn tới TikTok. Điều này có thể được triển khai bằng mã lập trình cho từng sự kiện trên trang web của bạn; hoặc nếu bạn đang sử dụng tích hợp đối tác, bạn có thể bật Khớp nâng cao thủ công trong cài đặt chia sẻ dữ liệu của nền tảng đối tác. Với tùy chọn này, bạn có sự linh hoạt hoàn toàn trong việc cấu hình loại thông tin nào và cho sự kiện nào bạn muốn gửi tới TikTok.
- **Khớp nâng cao tự động (Automatic Advanced Matching)** tự động nhận diện thông tin khách hàng như email, số điện thoại và các mã định danh khác từ các trường nhập biểu mẫu, văn bản tĩnh hiển thị trên trang web và các biến trang web quan trọng (ví dụ: `window.dataLayer`, `window.utag`). Dữ liệu này được băm trực tiếp trên trình duyệt bằng thuật toán tiêu chuẩn ngành (SHA-256) trước khi gửi an toàn tới TikTok phục vụ mục đích đo lường và phân bổ quảng cáo.
 
**Chúng tôi khuyến nghị nhà quảng cáo sử dụng đồng thời cả Khớp nâng cao thủ công và Khớp nâng cao tự động cùng lúc, vì cấu hình này tối đa hóa toàn diện hiệu quả của giải pháp.**

**Hướng dẫn này dành cho việc triển khai Khớp nâng cao thủ công với TikTok Pixel. Để bật Khớp nâng cao tự động, bạn có thể thực hiện trong cài đặt Trình quản lý sự kiện (Events Manager). Tìm hiểu thêm về Khớp nâng cao tự động và cách bật trong [trung tâm trợ giúp](https://ads.tiktok.com/help/article/advanced-matching-web?lang=en).**
  
### Quyền riêng tư (Privacy)
Theo tiêu chuẩn bảo mật ngành, email và số điện thoại của khách hàng sẽ được băm bằng thuật toán SHA256 trước khi gửi tới máy chủ TikTok để so khớp. TikTok đạt chứng nhận ISO 27001 tại Hoa Kỳ và Vương quốc Anh. Tìm hiểu thêm về cách thông tin này được sử dụng trong [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms).

## Bắt đầu với Khớp nâng cao thủ công
### Trước khi bắt đầu
- Cần có nhân sự kỹ thuật để triển khai Khớp nâng cao thủ công.
- Bạn phải có quyền truy cập và chỉnh sửa mã nguồn trang web.
- Bạn phải có khả năng thêm dữ liệu đối tượng an toàn về mặt riêng tư vào các tham số.
- Tại thời điểm này, bạn cần thiết lập sẵn các sự kiện trong mã trang web. Nếu chưa, hãy tham khảo [Cài đặt Pixel bằng mã](do-luong-quang-cao-tom-tat.md#doc-1739585702922241) để tìm hiểu cách thiết lập sự kiện.

1. Điều hướng tới sự kiện (hoặc đoạn mã sự kiện) mà bạn muốn triển khai Khớp nâng cao. Dưới đây là ví dụ về sự kiện 'AddToCart' (Thêm vào giỏ hàng) bao gồm các tham số:

```javascript
// JavaScript
ttq.track('AddToCart', {
    contents: [
    {
      content_id: '301',
      content_name: 'running shoes',
      content_category: 'Shoes > Sneakers > running shoes',
      brand: 'your brand name',
      quantity: 1,
      price: 8,
    }],
    content_type: 'product',
    value: 9.2,
    currency: 'USD',  
});
```

2. Sử dụng hàm `ttq.identify` để khởi đầu mã Khớp nâng cao trước khi gọi mã sự kiện (ví dụ: `ttq.track`).
3. Dưới hàm `ttq.identify`, có hai phương thức truyền email và số điện thoại thông qua các tham số `email` và `phone_number`:

- a. Truyền giá trị thô và hệ thống sẽ tự động băm ở phía client:

```javascript
// JavaScript
ttq.identify({
    email: 'email@example.com',
    phone_number: '+15551234567',
})
```
- **Lưu ý quan trọng khi truyền giá trị gốc chưa băm:**
	- Số điện thoại:
		- Chuẩn hóa số điện thoại của bạn về định dạng E.164, kết hợp giữa `+{mã quốc gia}{số điện thoại}`.
		- Đề xuất sử dụng thư viện [libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) để phân tích định dạng E.164.

- b. Truyền giá trị đã băm sẵn:
  
```javascript
// JavaScript
ttq.identify({
    email: '0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b', 
    phone_number: '9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd',
    external_id: '936a185caaa266bb9cbe981e9e05cb78cd732b0b3280eb944412bb6f8f8f07af',
})
```

- **Lưu ý quan trọng khi truyền giá trị đã băm:**
	- Email:
		- Bắt buộc chuyển đổi tất cả ký tự thành chữ thường (lowercase) trước khi băm.
	    - Cần loại bỏ khoảng trắng thừa ở đầu/cuối chuỗi (trim) trước khi băm.
		- Không thực hiện bất kỳ hình thức chuẩn hóa nào khác đối với email trước khi băm.
		- Chỉ chấp nhận SHA-256. Đề xuất sử dụng gói thư viện: [js-sha256](https://github.com/emn178/js-sha256).
	- Số điện thoại:
		- Chuẩn hóa số điện thoại về định dạng E.164 (`+{mã quốc gia}{số điện thoại}`) trước khi băm.
	- ID bên ngoài (External ID):
		- Cắt bỏ khoảng trắng thừa ở đầu/cuối trước khi băm và đảm bảo tính nhất quán của External ID sử dụng.

4. Sau khi thêm mã Khớp nâng cao vào các sự kiện, hãy sử dụng tiện ích mở rộng [TikTok Pixel Helper](https://chrome.google.com/webstore/detail/tiktok-pixel-helper/aelgobmabdmlfmiblddjfnjodalhidnn) để kiểm tra việc cài đặt thành công:
  	1. Cài đặt Pixel Helper và truy cập trang web của bạn.
  	2. Thử nghiệm từng sự kiện với tư cách là khách hàng, mỗi sự kiện phát hiện được sẽ hiển thị trong Pixel Helper.
  	3. Mở chi tiết sự kiện và tìm dấu tích màu xanh lá cây ('green check'), biểu thị không phát hiện vấn đề nào với sự kiện này.
  	4. Chuyển đến phần **Chi tiết tham số (Parameter Details)** dưới chi tiết sự kiện.
  	5. Tìm mục **Khớp nâng cao (Advanced Matching)** và kiểm tra xem cả hai trường **email** và **phone** có hiển thị hay không. Điều này xác nhận hệ thống đã nhận diện mã Khớp nâng cao hợp lệ cho cả email và số điện thoại.

Để tìm hiểu thêm về Pixel Helper, hãy xem bài viết [Trợ giúp TikTok Pixel](https://ads.tiktok.com/help/article?aid=9661).

### Thông tin định danh được hỗ trợ (Identity information supported)

| user_properties | Formatting Requirements | Contents example |
|---|---|---|
| email | Chưa băm hoặc chữ thường và băm SHA-256.<br><br>Đối với giá trị chưa băm:<ul><li>TikTok sẽ tự động băm giá trị bằng sha256 trước khi dữ liệu đi vào hệ thống.</li></ul><br>Đối với định dạng băm SHA-256:<ul><li>Cắt bỏ khoảng trắng thừa ở đầu và cuối, đồng thời chuyển toàn bộ ký tự thành chữ thường trước khi băm.</li><li>Không thực hiện bất kỳ hình thức chuẩn hóa nào khác đối với email trước khi băm.</li><li>Chỉ chấp nhận SHA-256. Gói thư viện đề xuất: [GitHub - emn178/js-sha256: Hàm băm SHA-256 / SHA-224 đơn giản cho JavaScript hỗ trợ UTF-8](https://github.com/emn178/js-sha256)</li></ul> | `email@example.com` |
| phone_number | Chưa băm hoặc băm SHA-256.<br><br><ul><li>Chuẩn hóa số điện thoại sang định dạng E.164, kết hợp giữa `+ [mã quốc gia][số điện thoại]`. Ví dụ số điện thoại Mỹ theo định dạng E.164: `+12133734253`.</li><li>Khuyến nghị sử dụng [libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) để phân tích cú pháp E.164.</li></ul><br>Đối với giá trị chưa băm:<ul><li>TikTok sẽ tự động băm giá trị bằng sha256 trước khi đưa vào hệ thống.</li></ul><br>Đối với định dạng băm SHA-256:<ul><li>Chỉ chấp nhận SHA-256. Gói thư viện đề xuất: [GitHub - emn178/js-sha256](https://github.com/emn178/js-sha256)</li></ul> | `+15551234567` |
| external_id <br><br>ID duy nhất từ nhà quảng cáo, chẳng hạn như ID thẻ thành viên, ID người dùng và ID cookie bên ngoài.| Chưa băm hoặc băm SHA-256.<br><br>Cắt bỏ khoảng trắng ở đầu và cuối trước khi băm và đảm bảo bạn áp dụng nhất quán ID bên ngoài đã chọn.<br><br>Đối với định dạng băm SHA-256: <ul><li>Chỉ chấp nhận SHA-256. Gói thư viện đề xuất: [GitHub - emn178/js-sha256](https://github.com/emn178/js-sha256)</li></ul>||
  
### Các phương pháp thực hành tối ưu (Best practices)

Có một số phương pháp tối ưu cần lưu ý khi triển khai Khớp nâng cao:
- **Sử dụng đồng thời cả Khớp nâng cao thủ công và tự động nếu có thể.** Việc kích hoạt cả hai giải pháp đảm bảo bạn nhận được lợi ích tối đa từ việc so khớp. Phiên bản thủ công yêu cầu viết mã nên có thể cần đến hỗ trợ của lập trình viên.
- **Tối đa hóa lợi ích của Khớp nâng cao với Cookie.** Chúng tôi khuyến nghị kết hợp cả giải pháp Tự động và Thủ công với cookie của bên thứ nhất để đạt hiệu quả cao nhất. Đảm bảo bật cookie của bên thứ nhất trong cài đặt Trình quản lý sự kiện. Đọc thêm tại [Sử dụng Cookie với TikTok Pixel](https://ads.tiktok.com/help/article/using-cookies-with-tiktok-pixel?redirected=1).
- Đối với Khớp nâng cao thủ công, chúng tôi khuyến khích bạn gửi cả email và số điện thoại cho tất cả các sự kiện của khách truy cập. Chúng tôi cũng khuyên bạn nên thu thập email và số điện thoại của khách truy cập ở giai đoạn sớm trong phễu chuyển đổi để đạt kết quả tốt nhất. Điều này gia tăng xác suất so khớp khách hàng với người dùng trên TikTok.

Khớp nâng cao thủ công (MAM):
• Gửi email và số điện thoại cho **mọi sự kiện** trên trang web của bạn hoặc **càng thường xuyên càng tốt**. • Đảm bảo bạn sử dụng mã động để truyền các giá trị hoặc thông tin động liên quan đến sự kiện tới TikTok. Tránh gửi giá trị không hợp lệ hoặc giá trị tĩnh (hardcoded) trong mã Khớp nâng cao. • Truyền chuỗi rỗng khi không có thông tin khách hàng thay vì sử dụng khoảng trắng, chuỗi "undefined" hoặc các giá trị mặc định khác. • Kiểm tra kỹ lưỡng xem bạn đã sử dụng đúng tham số Khớp nâng cao khi gửi email và số điện thoại hay chưa.

---

<a id="doc-1795929012554754"></a>
<!-- doc_id: 1795929012554754 -->
<!-- doc_id: 1795929012554754 -->
# Chế độ đồng ý Cookie Pixel (Pixel Cookie consent mode)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Pixel Cookie consent mode
Chế độ đồng ý cookie của TikTok Pixel cung cấp hai giải pháp:
 - **Giải pháp từ chối mặc định (Default opt-out):** Giải pháp này sẽ ngăn pixel chia sẻ dữ liệu với TikTok cho đến khi có sự đồng ý rõ ràng từ phía người dùng.
 - **Giải pháp đồng ý mặc định (Default opt-in):** Giải pháp này sẽ cho phép pixel chia sẻ dữ liệu với TikTok cho đến khi người dùng chủ động thu hồi sự đồng ý.

# Giải pháp từ chối mặc định (Default opt-out)
 1. Trong mã cơ sở của pixel, thêm `"holdConsent"`, `"revokeConsent"` và `"grantConsent"` vào mảng `ttq.methods`.
 2. Gọi hàm `ttq.holdConsent()` trước khi tải pixel thông qua lệnh `ttq.load()`. Thao tác này sẽ xếp các sự kiện vào hàng đợi nhưng không chia sẻ chúng cho đến khi trạng thái đồng ý của người dùng thay đổi.
 3. Dựa trên lựa chọn của người dùng:
- Nếu người dùng đồng ý (grant consent), gọi lệnh `ttq.grantConsent()`. Thao tác này sẽ gửi các sự kiện lên máy chủ TikTok, bao gồm cả các sự kiện đã được xếp hàng đợi trước đó trong phiên.  
- Nếu người dùng từ chối (reject consent), gọi lệnh `ttq.revokeConsent()`. Thao tác này sẽ ngăn chặn các sự kiện gửi lên máy chủ TikTok, bao gồm cả các sự kiện đã xếp hàng đợi trước đó trong phiên.
 4. Nếu người dùng thay đổi tùy chọn của họ, hãy gọi `ttq.grantConsent()` hoặc `ttq.revokeConsent()` tương ứng để bật hoặc tắt việc chia sẻ dữ liệu qua pixel. Lưu ý rằng việc gọi `ttq.revokeConsent()` không làm ảnh hưởng đến dữ liệu đã gửi lên máy chủ TikTok trước đó.      

> **Lưu ý:** 
> Khi áp dụng, nhà quảng cáo nên triển khai giải pháp này trên mọi trang web có cài đặt TikTok Pixel.

**Trường hợp sử dụng 1: Trang web mặc định từ chối (opt-out) trước khi người dùng đưa ra lựa chọn rõ ràng**

```javascript
// JavaScript
<script>
 // Thêm các phương thức mới "holdConsent", "revokeConsent", và "grantConsent" vào mảng ttq.methods
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};

  // Giữ trạng thái đồng ý (Hold consent) trước khi gọi 'ttq.load'
  ttq.holdConsent();
  ttq.load('YOUR_TIKTOK_PIXEL_ID');
  ttq.page();
}(window, document, 'ttq');
</script>
```

Khi người dùng đưa ra quyết định:
- Khi người dùng từ chối sự đồng ý:
```javascript
ttq.revokeConsent();
```
- Khi người dùng chấp thuận sự đồng ý:
```javascript
ttq.grantConsent();
```

# Giải pháp đồng ý mặc định (Default opt-in)
 1. Trong mã cơ sở của pixel, thêm `"revokeConsent"` và `"grantConsent"` vào mảng `ttq.methods`.
 2. Gọi lệnh `ttq.load()` để khởi tạo pixel. Tất cả sự kiện sẽ được gửi tới máy chủ TikTok theo mặc định.
 3. Dựa trên lựa chọn của người dùng:
- Nếu người dùng đồng ý, gọi `ttq.grantConsent()`. Thao tác này cho phép các sự kiện do người dùng kích hoạt tiếp tục được gửi tới máy chủ TikTok.
- Nếu người dùng từ chối, gọi `ttq.revokeConsent()`. Thao tác này sẽ ngăn chặn các sự kiện trong tương lai gửi tới máy chủ TikTok.
 4. Nếu người dùng thay đổi lựa chọn, hãy gọi `ttq.grantConsent()` hoặc `ttq.revokeConsent()` tương ứng để bật hoặc tắt chia sẻ dữ liệu. Việc gọi `ttq.revokeConsent()` không làm ảnh hưởng đến dữ liệu đã gửi trước đó.

> **Lưu ý:** 
> Khi áp dụng, nhà quảng cáo nên triển khai giải pháp này trên mọi trang web có cài đặt TikTok Pixel.

---

<a id="doc-1801524003169281"></a>
<!-- doc_id: 1801524003169281 -->
<!-- doc_id: 1801524003169281 -->
# Làm việc với Single Page Applications (SPA)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Work with Single Page Applications
Ứng dụng trang đơn (Single Page Application - SPA) là một loại ứng dụng web tải một trang HTML duy nhất và tự động cập nhật nội dung khi người dùng tương tác, giúp trải nghiệm duyệt mượt mà và phản hồi nhanh hơn. 

Sau khi mã cơ sở Pixel đã được cài đặt trên trang web của bạn, bạn có thể định cấu hình cách TikTok Pixel phản ứng với các thay đổi trạng thái lịch sử (history state changes) trên các trang SPA.

## Cài đặt mặc định (Default setting)
Theo mặc định, TikTok Pixel sẽ báo cáo một sự kiện lượt xem trang (pageview) khi người dùng truy cập trang web SPA của bạn. Bất cứ khi nào trạng thái trình duyệt thay đổi và URL web được cập nhật, TikTok Pixel sẽ tự động đo lường thêm một lượt xem trang bổ sung đại diện cho lượt xem trên URL mới.

## Cài đặt thay thế (Alternative setting)
Nếu bạn không muốn TikTok Pixel tự động nhận diện khi người dùng truy cập một URL cụ thể trong trang web SPA, bạn có tùy chọn tắt tính năng đo lường lượt xem trang tự động khi nội dung thay đổi (mặc dù điều này không được khuyến nghị). 

Để thực hiện, bạn có thể thiết lập tham số `historyObserver` thành `false` khi tải TikTok Pixel:

```javascript
// JavaScript
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};

  ttq.load("<pixel_code>", {
    historyObserver: false, // Dừng đo lường sự kiện pageview tự động khi thay đổi URL (không khuyến nghị)
  });
  
  ttq.page();
}(window, document, 'ttq');
</script>
```

> **Lưu ý:** 
> Nếu bạn cài đặt TikTok Pixel thông qua Google Tag Manager trong Trình quản lý sự kiện của TikTok, bạn có thể tìm và chỉnh sửa mã cơ sở Pixel dưới thẻ `TT- -Web-Tag-Pixel_Setup`.

**Tìm hiểu thêm:**
- Truy cập [Tài liệu Google Tag Manager](https://marketingplatform.google.com/about/tag-manager/) để đo lường sự kiện bằng Tag Manager.
- Gỡ lỗi bằng cách sử dụng [TikTok Pixel Helper](https://chromewebstore.google.com/detail/tiktok-pixel-helper/aelgobmabdmlfmiblddjfnjodalhidnn) để xem kết nối dữ liệu sự kiện.

---

<a id="doc-1739585704427522"></a>
<!-- doc_id: 1739585704427522 -->
<!-- doc_id: 1739585704427522 -->
# Làm việc với Chính sách bảo mật nội dung (CSP)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Work with CSP
Nếu Chính sách bảo mật nội dung (Content Security Policy - CSP) được kích hoạt trên trang web của bạn, để TikTok Pixel hoạt động bình thường, bạn cần thêm các cấu hình và miền sau vào các chỉ thị CSP khác nhau:

- Đối với chỉ thị `frame-src`, hãy thêm các cấu hình dưới đây:
    - `bytedance:`
    - `sslocal:`
	
> **Lưu ý:** 
> `frame-src` là một chỉ thị của Chính sách bảo mật nội dung (CSP) kiểm soát các nguồn mà các phần tử `<iframe>` hoặc `<frame>` có thể tải. Các trình duyệt sẽ chặn mọi frame từ các miền hoặc giao thức không được liệt kê trong danh sách cho phép. Đối với TikTok Pixel, bạn bắt buộc phải đưa vào `bytedance:` và `sslocal:` để việc theo dõi và hiển thị webview/ứng dụng tải chính xác; nếu không, Pixel có thể gặp lỗi.

- Đối với các chỉ thị `script-src`, `img-src` và `connect-src`, vui lòng thêm các miền: `analytics.tiktok.com`, `analytics-ipv6.tiktokw.us`, và `ads.tiktok.com`.

> **Lưu ý:** 
> `analytics-ipv6.tiktokw.us` là tên miền liên kết với các dịch vụ phân tích dữ liệu của TikTok, đặc biệt phục vụ việc theo dõi và phân tích qua các địa chỉ IPv6.

**Ví dụ cấu hình CSP Header:**

```http
Content-Security-Policy: frame-src 'self' bytedance: sslocal:; script-src 'self' analytics.tiktok.com analytics-ipv6.tiktokw.us ads.tiktok.com; img-src 'self' analytics.tiktok.com analytics-ipv6.tiktokw.us ads.tiktok.com; connect-src 'self' analytics.tiktok.com analytics-ipv6.tiktokw.us ads.tiktok.com;
```

---

<a id="doc-1739585706138625"></a>
<!-- doc_id: 1739585706138625 -->
<!-- doc_id: 1739585706138625 -->
# Chế độ gỡ lỗi (Debug mode)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Debug mode
Nếu bạn cần xem chi tiết chuyên sâu trong quá trình gỡ lỗi thiết lập pixel, chế độ gỡ lỗi (debug mode) sẵn sàng hỗ trợ bạn.

# Cách mở chế độ gỡ lỗi
Có hai bước để kích hoạt chế độ gỡ lỗi:

  1. Mở [Liên kết SDK](https://analytics.tiktok.com/i18n/pixel/events.js), và thực thi lệnh sau trong Console trình duyệt:
     ```javascript
     document.cookie="pixel_debug=true; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/; SameSite=None; Secure";
     ```
  
  2. Tải lại (refresh) trang web của bạn.
- Kiểm tra các thông điệp gỡ lỗi:
Vui lòng mở Developer Console trên trình duyệt của bạn trước. Sau đó, TikTok Pixel sẽ xuất các bản ghi gỡ lỗi trực tiếp tại Console. Thông tin nhật ký bắt đầu bằng tiền tố `[TT]`.

# Bản ghi của một số điểm nút quan trọng (Logs of some key nodes)
- Khi bạn gọi lệnh `ttq.load()`
- Khi bạn gọi lệnh `ttq.identify()` hoặc `ttq.instance().identify()`
- Khi bạn gọi lệnh `ttq.page()` hoặc `ttq.track()` hoặc `ttq.instance().track()`. Trước khi báo cáo một sự kiện, hệ thống sẽ in ra console các thông tin `adInfo` và `appInfo`.
- Khi hệ thống lấy thông tin từ cache, url hoặc bridge.

---

<a id="doc-1770092377990145"></a>
<!-- doc_id: 1770092377990145 -->
<!-- doc_id: 1770092377990145 -->
# Sử dụng dữ liệu hạn chế (Limited Data Use)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Limited Data Use
**"Sử dụng dữ liệu hạn chế" (Limited Data Use - LDU)** cho **Events API** và **Pixel** là tính năng cung cấp cho doanh nghiệp quyền kiểm soát tốt hơn đối với cách dữ liệu sự kiện của họ được sử dụng trong hệ thống của TikTok.

Nhằm hỗ trợ doanh nghiệp tuân thủ quyền từ chối bán hoặc chia sẻ dữ liệu cá nhân theo một số luật bảo mật cấp tiểu bang tại Hoa Kỳ, TikTok cung cấp tính năng LDU. LDU cho Pixel và Events API giúp doanh nghiệp kiểm soát chặt chẽ cách dữ liệu sự kiện được xử lý trong hệ thống của TikTok. Tính năng này được áp dụng tại các tiểu bang Hoa Kỳ sau: California, Colorado, Connecticut, Utah, Virginia, Iowa, Minnesota, Tennessee, Maryland, Delaware, Florida, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas, Indiana, Kentucky.

Các doanh nghiệp nên tham vấn cố vấn pháp lý về cách sử dụng sản phẩm của TikTok nhằm tuân thủ pháp luật hiện hành. Để biết chi tiết về luật bảo vệ dữ liệu mới của các tiểu bang, vui lòng xem [Điều khoản pháp lý cập nhật](https://ads.tiktok.com/i18n/official/article?aid=10015015).

# Giới thiệu về Sử dụng dữ liệu hạn chế
Doanh nghiệp có thể cung cấp các tùy chọn trên trang web để người dùng chọn từ chối bán hoặc chia sẻ dữ liệu của họ.  
- Nếu doanh nghiệp sử dụng các công cụ như Events API hoặc Pixel để chia sẻ sự kiện với TikTok, doanh nghiệp có thể gửi cho TikTok một tham số để chỉ định rằng nhà quảng cáo muốn xử lý hạn chế dữ liệu sự kiện được chia sẻ.
- TikTok sẽ nhận diện tham số này như một yêu cầu xử lý dữ liệu hạn chế và sẽ hạn chế các hoạt động xử lý tương ứng nếu sự kiện được chia sẻ xảy ra tại một địa điểm hợp lệ. 

Các doanh nghiệp chọn sử dụng LDU có thể nhận thấy tác động đến quy mô tệp đối tượng tại các tiểu bang được áp dụng và hiệu quả chiến dịch quảng cáo (do dữ liệu LDU không được sử dụng cho mục đích tối ưu hóa).

## Triển khai Sử dụng dữ liệu hạn chế (Pixel)
Có hai cách để kích hoạt LDU: bật cho toàn bộ sự kiện dưới pixel, hoặc bật theo từng sự kiện cụ thể (viết mã tùy chỉnh):

**1) Bật cho toàn bộ sự kiện dưới Pixel**
 - Tải mã cơ sở pixel cho một pixel mới / cập nhật pixel hiện có.
 - Mở mã cơ sở pixel bằng trình soạn thảo văn bản và tìm đoạn mã chứa `ttq.load`.
 - Thêm `,{limited_data_use:true}` ngay sau mã pixel, đừng quên dấu phẩy `,`.
 - Dán mã pixel vào phần tiêu đề `<head>` trên trang web của bạn và tiếp tục như bình thường.

**2) Bật theo từng sự kiện (Viết mã tùy chỉnh)**
 - Thêm cờ chia sẻ dữ liệu hạn chế vào lệnh gọi mã tùy chỉnh.
 - Ví dụ: `ttq.track('Purchase')` sẽ chuyển thành:
   ```javascript
   ttq.track('Purchase', {"limited_data_use": true});
   ```

---

<a id="doc-1799004006287425"></a>
<!-- doc_id: 1799004006287425 -->
<!-- doc_id: 1799004006287425 -->
# Tích hợp Google Tag Manager (GTM)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration
Google Tag Manager (GTM) là một hệ thống quản lý thẻ cho phép bạn thêm nhanh chóng và dễ dàng các đoạn mã đo lường và các phân đoạn mã liên quan, thường được gọi chung là [thẻ (tags)](https://support.google.com/tagmanager/answer/3281060), vào trang web hoặc ứng dụng di động của bạn.

Với GTM, bạn có thể thiết lập TikTok Pixel để gửi các sự kiện trên trang web tới TikTok. Ngoài ra, bạn có thể sử dụng GTM để cấu hình [Events API phía máy chủ (server-side)](https://ads.tiktok.com/help/article/events-api-gtm?lang=en).

Tài liệu này bao gồm hướng dẫn từng bước về cách sử dụng quy trình tương tác của Trình quản lý sự kiện (Events Manager) để thiết lập thẻ TikTok Pixel trên trang web của bạn bằng GTM. Để tìm hiểu thêm về thiết lập Events API qua GTM, hãy tham khảo [Thiết lập TikTok Pixel & Events API đồng thời](do-luong-quang-cao-tom-tat.md#doc-1799004052020225).

## Điều kiện tiên quyết (Prerequisites)
Trước khi bắt đầu, hãy đảm bảo bạn có:
- Quyền truy cập quản trị viên vào tài khoản Google Tag Manager của bạn.
- Đã cài đặt mã vùng chứa (container code) GTM trên trang web của bạn.
- Tài khoản TikTok For Business với quyền truy cập vào Trình quản lý sự kiện.

## Bắt đầu (Get started)
Để bắt đầu tích hợp TikTok với Google Tag Manager:
1. Đăng nhập vào tài khoản TikTok Ads Manager và điều hướng đến **Trình quản lý sự kiện (Events Manager)**.
2. Chọn **Web Events** và nhấp vào nút **Thiết lập sự kiện Web (Set Up Web Events)**.
3. Chọn tùy chọn tích hợp đối tác tự động thông qua **Google Tag Manager**.
4. Thực hiện xác thực liên kết tài khoản Google của bạn với TikTok để cấp quyền quản lý vùng chứa GTM tương ứng.

---

<a id="doc-1799004034003969"></a>
<!-- doc_id: 1799004034003969 -->
<!-- doc_id: 1799004034003969 -->
# Thiết lập chỉ dùng TikTok Pixel (TikTok Pixel only setup)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > TikTok Pixel only setup
Để cài đặt TikTok Pixel và cấu hình các sự kiện gửi tới TikTok qua Google Tag Manager (GTM), bạn có thể hoàn tất quy trình thiết lập tương tác trong Trình quản lý sự kiện (Events Manager).

## Điều kiện tiên quyết (Prerequisites)
Trước khi bắt đầu, hãy đảm bảo bạn đáp ứng các yêu cầu sau:
- Tài khoản Google có quyền truy cập vào tài khoản và vùng chứa (container) GTM của bạn. Bạn phải có các quyền: **Xuất bản (Publish), Phê duyệt (Approve), Chỉnh sửa (Edit) và Đọc (Read)** trên vùng chứa GTM.
- Mã đoạn mã vùng chứa GTM đã được cài đặt đúng cách trên trang web của bạn.
- Trang web của bạn không có lỗi cú pháp hoặc thẻ bị hỏng trong vùng chứa GTM hiện tại.

## Hướng dẫn thiết lập (Setup guide)
1. Đăng nhập vào Trình quản lý sự kiện (Events Manager) trên TikTok For Business, chọn **Web Events** và chọn **Thiết lập sự kiện Web (Set Up Web Events)**.
2. Chọn phương thức kết nối dữ liệu: **TikTok Pixel**.
3. Chọn phương thức thiết lập: **Tự động qua đối tác (Automatically Set Up Web Events via Partner)** và chọn **Google Tag Manager**.
4. Đăng nhập và ủy quyền tài khoản Google kết nối với TikTok.
5. Chọn Tài khoản GTM (Account), Vùng chứa (Container) và Không gian làm việc (Workspace) mong muốn.
6. Xem lại các tài nguyên sẽ được tạo và xuất bản: Hệ thống sẽ tự động tạo thẻ mã cơ sở TikTok Pixel và các biến cần thiết trong vùng chứa GTM của bạn. Chi tiết về các tài nguyên được tạo, xem tại [Các thay đổi vùng chứa GTM](do-luong-quang-cao-p2.md#doc-1799004081342466).
7. Sau khi xuất bản thành công, mã TikTok Pixel sẽ tự động tải cùng trang web của bạn. Bạn có thể sử dụng [Công cụ kiểm tra sự kiện](https://ads.tiktok.com/help/article/test-tiktok-pixel-events-video-walkthrough?lang=en) hoặc tiện ích mở rộng [TikTok Pixel Helper](https://ads.tiktok.com/help/article/tiktok-pixel-helper-2.0) để xác minh cài đặt.

## Câu hỏi thường gặp (FAQs)
### Q1: Có lỗi xảy ra trong bước Xem lại và xuất bản tài nguyên. Tôi nên làm gì?
**Trả lời:** Nếu bạn gặp sự cố khi xem lại và xuất bản tài nguyên, hãy thực hiện các bước khắc phục sau:
1. Đảm bảo bạn có đủ quyền trên vùng chứa GTM (Publish, Approve, Edit, Read).
2. Kiểm tra xem vùng chứa có lỗi tồn tại từ trước hay không bằng chế độ **Xem trước (Preview)** của GTM.
3. Khắc phục sự cố và thử xuất bản lại từ luồng thiết lập của Trình quản lý sự kiện.
4. Nếu sự cố vẫn tiếp diễn, hãy dọn dẹp không gian làm việc và cài đặt lại.

### Q2: Ban đầu tôi chọn thiết lập sự kiện bằng Công cụ tạo sự kiện (Event Builder), nhưng hiện tại muốn chuyển sang dùng Data Layer của GTM. Tôi nên làm thế nào?
**Trả lời:** Để chuyển sang API Data Layer của GTM, hãy thực hiện:
1. Chạy lại luồng thiết lập trong Trình quản lý sự kiện.
2. Trong quá trình thiết lập, chọn **Sử dụng API lớp dữ liệu của Google Tag Manager (Use Google Tag Manager data layer APIs)**. Thao tác này sẽ tự động cài đặt bổ sung các thẻ và biến hỗ trợ lớp dữ liệu.

### Q3: Làm thế nào để dọn dẹp hoặc cài đặt lại?
**Trả lời:** Trong một số trường hợp (như nâng cấp lên tích hợp kép Pixel & Events API hoặc đặt lại cài đặt gốc), bạn có thể:
1. Tạo một workspace sao lưu trong cùng vùng chứa GTM để lưu lại cấu hình hiện tại.
2. Trong workspace mặc định, xóa các thẻ, biến và trình kích hoạt TikTok đã cài đặt trước đó.
3. Chạy lại luồng thiết lập tương tác để cài đặt lại.
4. Sao chép lại các tùy chỉnh quan trọng từ workspace sao lưu nếu cần.

### Q4: Tôi đã tự cài đặt mẫu TikTok Pixel Template thủ công từ Thư viện GTM. Tôi có thể tiếp tục dùng nó không?
**Trả lời:** Hoàn toàn có thể. Nếu bạn đã cài đặt thẻ mẫu TikTok Pixel Template từ thư viện GTM Community Template Gallery, bạn có thể tiếp tục sử dụng bình thường và giữ nguyên các tùy biến đã thiết lập.

## Hỗ trợ (Support)
- Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ [Bộ phận hỗ trợ khách hàng TikTok Ads](https://ads.tiktok.com/help/article/contact-tiktok-business-support) hoặc chuyên viên đại diện kinh doanh TikTok của bạn.
- Báo cáo lỗi kỹ thuật hoặc yêu cầu tính năng trên GitHub tại [Kho lưu trữ mẫu GTM của TikTok](https://github.com/tiktok/gtm-template-pixel/issues).

---

<a id="doc-1799004081342466"></a>
<!-- doc_id: 1799004081342466 -->
<!-- doc_id: 1799004081342466 -->
# Các thay đổi vùng chứa GTM (GTM container changes)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > GTM container changes
Bảng sau đây phác thảo các thẻ (tags), biến (variables) và trình kích hoạt (triggers) được tạo trong tài khoản GTM (Google Tag Manager) của bạn bởi luồng thiết lập tương tác của Trình quản lý sự kiện. Lưu ý rằng các tùy chọn cài đặt cụ thể mà bạn chọn có thể tạo ra các thành phần khác nhau.

> **Lưu ý:** 
> Những thay đổi này sẽ tự động được áp dụng vào vùng chứa GTM của bạn sau khi bạn hoàn tất luồng thiết lập phía máy chủ hoặc máy khách.

## Tích hợp TikTok Pixel (TikTok Pixel integration)

### Sử dụng Event Builder làm phương thức thiết lập sự kiện

| Container | Item | Type | Name | Purpose |
|---|---|---|---|---|
| --- | --- | - | --- | --- |
| Web | Tag | Custom HTML | TT-{PixelCode}-Web-Tag-Pixel_Setup | Thẻ này cài đặt mã cơ sở của TikTok Pixel trên trang web của bạn. |

### Sử dụng API Data Layer của GTM làm phương thức thiết lập sự kiện

| Vùng chứa (Container) | Mục (Item) | Loại (Type) | Tên (Name) | Mục đích (Purpose) |
|---|---|---|---|---|
| Web | Tag | Custom HTML | `TT-{PixelCode}-Web-Tag-Pixel_Setup` | Cài đặt mã cơ sở của TikTok Pixel trên trang web. |
| Web | Tag | TikTok Pixel | `TT-{PixelCode}-Web-Tag-Pixel_Event` | Gửi các sự kiện kích hoạt trên trang web tới TikTok. |
| Web | Trigger | Custom Event | `TT-{PixelCode}-Web-Trigger-Custom_Event` | Chọn lọc các sự kiện sẽ được gửi tới TikTok. |
| Web | Template | TikTok Pixel | TikTok Pixel | Mẫu template hỗ trợ xử lý và gửi sự kiện chuẩn hóa. |

## Tích hợp đồng thời TikTok Pixel & Events API

| Vùng chứa (Container) | Mục (Item) | Loại (Type) | Tên (Name) | Mục đích (Purpose) |
|---|---|---|---|---|
| Web | Tag | Google Tag | `TT-{PixelCode}-Web-Tag-GA4_Config` | Cấu hình URL máy chủ gắn thẻ (tagging server URL) cần thiết cho tích hợp Events API. |
| Web | Tag | Google Analytics: GA4 Event | `TT-{PixelCode}-Web-Tag-GA4_Event` | Cấu hình dữ liệu gửi tới máy chủ gắn thẻ. |
| Web | Tag | Custom HTML | `TT-{PixelCode}-Web-Tag-Pixel_Setup` | Cài đặt mã cơ sở của TikTok Pixel trên trang web. |
| Web | Tag | TikTok Pixel | `TT-{PixelCode}-Web-Tag-Pixel_Event` | Gửi các sự kiện từ trang web tới TikTok. |
| Web | Trigger | Custom Event | `TT-{PixelCode}-Web-Trigger-Custom_Event` | Chọn lọc các sự kiện sẽ gửi tới TikTok. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-User_Data` | Trích xuất dữ liệu người dùng cho các sự kiện phía máy chủ. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-Items` | Trích xuất danh sách mặt hàng cho các sự kiện phía máy chủ. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-Currency` | Trích xuất tiền tệ cho các sự kiện phía máy chủ. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-Value` | Trích xuất giá trị doanh thu cho các sự kiện phía máy chủ. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-External_ID` | Trích xuất ID bên ngoài (External ID) cho sự kiện máy chủ. |
| Web | Variable | Custom JavaScript | `TT-{PixelCode}-Web-Variable-Event_ID` | Trích xuất ID sự kiện (Event ID) phục vụ chống trùng lặp. |
| Web | Template | TikTok Pixel | TikTok Pixel | Mẫu template xử lý và gửi sự kiện tới TikTok. |
| Server | Tag | TikTok Events API (Official) | `TT-{PixelCode}-Server-Tag-EAPI_Event` | Gửi các sự kiện phía máy chủ tới TikTok Events API. |
| Server | Trigger | Custom | `TT-{PixelCode}-Server-Trigger-All_Event` | Chọn lọc các sự kiện phía máy chủ gửi tới TikTok Events API. |
| Server | Template | TikTok Events API (Official) | TikTok Events API (Official) | Mẫu template phía server xử lý và gửi sự kiện tới Events API. |

---

<a id="doc-1799004110681154"></a>
<!-- doc_id: 1799004110681154 -->
<!-- doc_id: 1799004110681154 -->
# Thiết lập sự kiện thủ công (Set up events manually)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > Set up events manually
Để thiết lập các sự kiện TikTok theo cách thủ công mà không cần sử dụng Data Layer, bạn có thể sử dụng tính năng ghi đè tham số mẫu (template parameter override). Các hướng dẫn được cung cấp trong tài liệu này có thể áp dụng cho cả mẫu TikTok Pixel và mẫu Events API.

> **Lưu ý:** 
> Tuy nhiên, bạn nên chuyển sang sử dụng Lớp dữ liệu GTM (Data Layer) vì phương pháp này mang lại khả năng mở rộng và độ tin cậy cao hơn, đặc biệt nếu trang web của bạn đã sử dụng Data Layer GTM để gửi sự kiện đến các nền tảng khác như Google Analytics. Để biết thêm thông tin, hãy xem [Thiết lập sự kiện với Data Layer](do-luong-quang-cao-tom-tat.md#doc-1799004097478658).

## Cấu hình tên sự kiện (Event name configuration)
Chọn **Tên sự kiện TikTok (Event Name)** mà bạn muốn thẻ gửi đi. Tên sự kiện phải tương ứng với trình kích hoạt (trigger) mà bạn gắn với thẻ. Bạn có thể sử dụng biến làm sự kiện hoặc chọn từ danh sách các tên sự kiện web tiêu chuẩn của TikTok (ví dụ: `ViewContent` và `AddToCart`). Tìm hiểu thêm về [Các sự kiện Pixel được TikTok hỗ trợ](do-luong-quang-cao-p2.md#doc-1739585696931842).

## Dữ liệu người dùng (User data)
Để cấu hình thủ công thông tin người dùng cho [Khớp nâng cao (Advanced Matching)](do-luong-quang-cao-p2.md#doc-1739585700402178), hãy chỉ định các tham số dưới mục **Dữ liệu người dùng (User Data)** trong cài đặt thẻ. Bạn có thể sử dụng các biến GTM để chỉ định các tham số này.

### Định dạng tham số Khớp nâng cao đã băm SHA256 (SHA256 AM parameters format)

| Field | Format requirement |
|---|---|
| SHA256 Hashed Email | • **Cắt bỏ** khoảng trắng đầu và cuối của mỗi email trước khi băm. • **Chuyển thành chữ thường** tất cả các ký tự trước khi băm. • **Băm** giá trị email đã chuẩn hóa bằng SHA-256. |
| SHA256 Hashed Phone | • **Chuẩn hóa** số điện thoại về [định dạng E.164](https://www.twilio.com/docs/glossary/what-e164), `+{mã quốc gia}{số điện thoại}`. Ví dụ: "+12133734253". • **Mã quốc gia** bắt buộc phải có và có tiền tố là dấu `+`, không có bất kỳ dấu ngoặc đơn hoặc số `0` nào ở đầu. • **Loại bỏ khoảng trắng, chữ cái hoặc ký hiệu** ngoại trừ dấu `+`. • **Băm** giá trị số điện thoại đã chuẩn hóa bằng SHA-256. |
| SHA256 Hashed External ID | **Cắt bỏ** khoảng trắng đầu và cuối trước khi băm bằng SHA-256. |

### Định dạng tham số Khớp nâng cao dạng văn bản thô (Plain AM parameters format)

| Field | Format requirement |
|---|---|
| Email | • **Cắt bỏ** khoảng trắng đầu và cuối của mỗi email. • **Chuyển thành chữ thường** tất cả các ký tự. |
| Phone | • **Chuẩn hóa** số điện thoại về [định dạng E.164](https://www.twilio.com/docs/glossary/what-e164), `+{mã quốc gia}{số điện thoại}`. Ví dụ: "+12133734253". • **Mã quốc gia** bắt buộc phải có và có tiền tố là dấu `+`, không chứa dấu ngoặc hoặc số `0` ở đầu. • **Loại bỏ khoảng trắng, chữ cái hoặc ký hiệu** ngoại trừ dấu `+`. |
| External ID | **Cắt bỏ** khoảng trắng đầu và cuối chuỗi. |

## Dữ liệu sản phẩm (Product data)

| Field | Description | Required for reporting Return on Ad Spend (ROAS) or for Value-based Optimization (VBO) | Required for Video Shopping Ads (VSA) |
|---|---|---|---|
| currency | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Ví dụ: `EUR`, `USD`, `VND`, `JPY`. ⏎ **Danh sách các loại tiền tệ hiện được hỗ trợ**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR`. | ✅ |  |
| value | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng dưới dạng số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí địa lý, loại tiền tệ hay các yếu tố khác. Giá trị không được chứa bất kỳ ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy nào. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của đơn hàng. | ✅ |  |
| query | Chuỗi văn bản được nhập bởi người dùng. ⏎ Ví dụ: nếu người dùng tìm kiếm sản phẩm trên trang web của bạn, bạn có thể chuyển từ khóa tìm kiếm đó. Nếu người dùng nhập mã giảm giá khi thanh toán, bạn có thể chuyển mã đó. |  |  |
| description | Mô tả về mặt hàng hoặc trang web. |  |  |
| contents | Mảng chứa các đối tượng nội dung (content objects). ⏎ Để xem danh sách các trường trong đối tượng `contents`, xem bảng tham số `contents` dưới đây. |  |  |

### Các tham số trong đối tượng `contents`

| Field | Description | Required for reporting ROAS or for VBO | Required for VSA |
|---|---|---|---|
| price | Giá của một mặt hàng đơn lẻ. ⏎ Ví dụ: `10`, `10.5`. |  |  |
| quantity | Số lượng mặt hàng. |  |  |
| content_id | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Chúng tôi khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ⏎ Nếu bạn đã thiết lập danh mục sản phẩm (catalog), ID này phải khớp với `sku_id` hoặc `item_group_id` trong danh mục. |  | ✅ |
| content_type | Loại nội dung trong sự kiện. ⏎ Các giá trị enum được hỗ trợ: `product`, `product_group`. • Khi `content_id` trong `contents` là `sku_id`, hãy đặt trường này là `product`. • Khi `content_id` trong `contents` là `item_group_id`, hãy đặt trường này là `product_group`. |  | ✅ |
| content_category | Danh mục của trang hoặc sản phẩm. |  |  |
| content_name | Tên của trang hoặc sản phẩm. |  |  |
| brand | Tên thương hiệu của sản phẩm. |  |  |

## Xác minh thiết lập sự kiện (Verify events setup)
Sau khi hoàn tất cấu hình thủ công, hãy sử dụng chế độ Xem trước (Preview) trong GTM và tiện ích TikTok Pixel Helper để kiểm tra việc gửi sự kiện và tính đầy đủ của các tham số trước khi xuất bản.

## Hỗ trợ (Support)
- Liên hệ [Bộ phận hỗ trợ TikTok Business](https://ads.tiktok.com/help/article/contact-tiktok-business-support) nếu bạn cần trợ giúp thêm.

---

<a id="doc-1799004129683458"></a>
<!-- doc_id: 1799004129683458 -->
<!-- doc_id: 1799004129683458 -->
# Xác minh thiết lập GTM (Verify GTM setup)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > Verify GTM setup
## Xác minh thiết lập TikTok Pixel

Sau khi hoàn tất việc tích hợp TikTok Pixel, bạn có thể xác minh xem việc thiết lập đã thành công hay chưa bằng các phương pháp sau:

1. **Sử dụng tiện ích mở rộng TikTok Pixel Helper:**
   - Cài đặt tiện ích [TikTok Pixel Helper](https://chrome.google.com/webstore/detail/tiktok-pixel-helper/aelgobmabdmlfmiblddjfnjodalhidnn) trên trình duyệt Chrome.
   - Truy cập trang web của bạn và mở tiện ích mở rộng để kiểm tra xem TikTok Pixel ID có xuất hiện và các sự kiện có được kích hoạt thành công hay không.
   - Kiểm tra các chi tiết tham số như Khớp nâng cao (Advanced Matching), `value`, `currency`, v.v.

2. **Sử dụng Chế độ xem trước của Google Tag Manager (GTM Preview mode):**
   - Mở không gian làm việc GTM của bạn và nhấp vào nút **Preview** ở góc trên bên phải.
   - Nhập URL trang web của bạn để mở cửa sổ Tag Assistant.
   - Kiểm tra xem các thẻ `TT-{PixelCode}-Web-Tag-Pixel_Setup` và `TT-{PixelCode}-Web-Tag-Pixel_Event` có kích hoạt (fired) thành công khi các tương tác tương ứng diễn ra trên trang web hay không.

## Xác minh thiết lập TikTok Events API
### Sử dụng Công cụ kiểm tra sự kiện và Chế độ xem trước GTM
1. Trong Trình quản lý sự kiện TikTok, chuyển đến mục **Test Events (Kiểm tra sự kiện)** dưới tab Pixel của bạn.
2. Sao chép **Mã kiểm tra sự kiện (Test Event Code)** được cung cấp.
3. Trong GTM, mở thẻ TikTok Events API (Server container) và dán Mã kiểm tra sự kiện vào trường tương ứng.
4. Kích hoạt sự kiện trên trang web của bạn và theo dõi tab Kiểm tra sự kiện trong Trình quản lý sự kiện TikTok theo thời gian thực để đảm bảo dữ liệu sự kiện phía máy chủ được ghi nhận chính xác.
5. Kiểm tra tính năng chống trùng lặp: Đảm bảo cùng một sự kiện phát ra từ cả Pixel và Events API có cùng `event_id` để TikTok loại bỏ trùng lặp thành công.
6. **Lưu ý:** Các sự kiện kiểm tra sẽ không được tính vào báo cáo chiến dịch hoặc tối ưu hóa. Sau khi xác minh thành công, hãy nhớ **xóa Mã kiểm tra sự kiện** khỏi thẻ và **lưu, xuất bản lại vùng chứa GTM của bạn**.

---

<a id="doc-1740963089558529"></a>
<!-- doc_id: 1740963089558529 -->
<!-- doc_id: 1740963089558529 -->
# Tham chiếu API (API reference)
> Đường dẫn: Marketing API > Ad Measurement > API reference
> **Quan trọng:** 
> Bằng việc sử dụng các điểm cuối Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

Events API bao gồm 4 nhóm điểm cuối chính: App Events API (Sự kiện ứng dụng), Pixel Events API (Sự kiện Web), Offline Events API (Sự kiện ngoại tuyến), và CRM Events API.

# App Events API (Sự kiện ứng dụng)

> **Lưu ý:** Events API - App hiện đang trong giai đoạn Beta. Nếu bạn muốn sử dụng API này, vui lòng liên hệ đại diện TikTok của bạn. Tài khoản của bạn cần được thêm vào danh sách cho phép (allowlist) trước khi bạn có thể báo cáo sự kiện bằng [/v1.3/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) hoặc [/v1.3/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569).

* [Báo cáo sự kiện ứng dụng (Report an App Event)](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266)
* [Báo cáo sự kiện ứng dụng hàng loạt (Report App Events in bulk)](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
* [Lấy thông tin ứng dụng (Get info of an app)](../12-api-reference/43-events-1-0-p1.md#doc-1740859272887297)
* [Tạo ứng dụng (Create an app)](../12-api-reference/43-events-1-0-p1.md#doc-1740859280958466)
* [Cập nhật thông tin ứng dụng (Update an app)](../12-api-reference/43-events-1-0-p1.md#doc-1740859300069378)
* [Lấy danh sách ứng dụng (Get the app list)](../12-api-reference/43-events-1-0-p1.md#doc-1740859313270786)
* [Lấy các sự kiện chuyển đổi ứng dụng (Get App Conversion Events)](../12-api-reference/43-events-1-0-p1.md#doc-1740859338750977)
* [Lấy các sự kiện nhắm mục tiêu lại của ứng dụng (Get App Retargeting Events)](../12-api-reference/43-events-1-0-p1.md#doc-1740859371033601)

# Pixel Events API (Sự kiện Web)

* [Báo cáo sự kiện Web (Report a Web Event)](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890)
* [Báo cáo sự kiện Web hàng loạt (Report Web Events in bulk)](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225)
* [Lấy danh sách Pixel (Get pixels)](../12-api-reference/43-events-1-0-p1.md#doc-1740858697598978)
* [Tạo Pixel mới (Create a pixel)](../12-api-reference/43-events-1-0-p1.md#doc-1740858779758593)
* [Cập nhật cấu hình Pixel (Update a pixel)](../12-api-reference/43-events-1-0-p1.md#doc-1740858799524865)
* [Tạo sự kiện Pixel (Create Pixel Events)](../12-api-reference/43-events-1-0-p1.md#doc-1740858807646209)
* [Cập nhật sự kiện Pixel (Update a Pixel Event)](../12-api-reference/43-events-1-0-p1.md#doc-1740858823774210)
* [Xóa sự kiện Pixel (Delete a Pixel Event)](../12-api-reference/43-events-1-0-p1.md#doc-1740858862104578)
* [Lấy sự kiện Trang tức thì (Get Instant Page events)](../12-api-reference/43-events-1-0-p1.md#doc-1740898639412226)
* [Lấy số liệu thống kê sự kiện Pixel (Get Pixel Event statistics)](../12-api-reference/43-events-1-0-p1.md#doc-1740858904557570)

# Offline Events API (Sự kiện ngoại tuyến)

* [Tạo bộ sự kiện ngoại tuyến (Create an Offline Event set)](../12-api-reference/43-events-1-0-p1.md#doc-1758427576470529)
* [Cập nhật bộ sự kiện ngoại tuyến (Update an Offline Event set)](../12-api-reference/43-events-1-0-p1.md#doc-1765596741157889)
* [Xóa bộ sự kiện ngoại tuyến (Delete an Offline Event set)](../12-api-reference/43-events-1-0-p1.md#doc-1765596790860802)
* [Lấy danh sách bộ sự kiện ngoại tuyến (Get Offline Event sets)](../12-api-reference/43-events-1-0-p1.md#doc-1765596808589313)
* [Báo cáo sự kiện ngoại tuyến (Report an Offline Event)](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857)
* [Báo cáo sự kiện ngoại tuyến hàng loạt (Report Offline Events in Bulk)](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482)

# CRM Events API
* [Lấy các bộ sự kiện CRM (Get CRM Event Sets)](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898)
- **Tạo bộ sự kiện CRM (Create a CRM Event Set)**

---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Hướng dẫn đo lường quảng cáo (Ad Measurement) — phần 2/2**:

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

