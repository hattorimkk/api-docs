#!/usr/bin/env python3
"""
Biên dịch tiếng Việt cho Docs 13-18 của u124 (do-luong-quang-cao-tom-tat.md).
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOM_TAT_PATH = os.path.join(ROOT, "docs/09-marketing-api/do-luong-quang-cao-tom-tat.md")

with open(TOM_TAT_PATH, "r", encoding="utf-8") as f:
    text = f.read()

docs = re.split(r"(?=<a id=\"doc-\d+\"></a>)", text)

# 1. Cập nhật TOC cho Docs 13-18
toc_replacements = [
    ("- [13. React Native installation (#doc-1876482381311362)](#doc-1876482381311362)",
     "- [13. Cài đặt SDK trên React Native (#doc-1876482381311362)](#doc-1876482381311362)"),
    ("- [14. In-app ad revenue reporting (#doc-1862351923536898)](#doc-1862351923536898)",
     "- [14. Báo cáo doanh thu quảng cáo trong ứng dụng (In-app ad revenue reporting) (#doc-1862351923536898)](#doc-1862351923536898)"),
    ("- [15. Resources for data sharing after user consent (#doc-1824048384831554)](#doc-1824048384831554)",
     "- [15. Chia sẻ dữ liệu sau khi người dùng đồng ý (Data sharing after user consent) (#doc-1824048384831554)](#doc-1824048384831554)"),
    ("- [16. Install Pixel using code (#doc-1739585702922241)](#doc-1739585702922241)",
     "- [16. Cài đặt Pixel bằng mã tùy chỉnh (Install Pixel using code) (#doc-1739585702922241)](#doc-1739585702922241)"),
    ("- [17. Events API and Pixel setup (#doc-1799004052020225)](#doc-1799004052020225)",
     "- [17. Thiết lập đồng thời TikTok Pixel và Events API (#doc-1799004052020225)](#doc-1799004052020225)"),
    ("- [18. Set up events with data layer (#doc-1799004097478658)](#doc-1799004097478658)",
     "- [18. Thiết lập sự kiện với Data Layer trong GTM (#doc-1799004097478658)](#doc-1799004097478658)"),
]

for old, new in toc_replacements:
    if old in docs[0]:
        docs[0] = docs[0].replace(old, new)

# 2. Từ điển thay thế cho Docs 13-18
replacements_13_18 = [
    # Tiêu đề chung
    ("# React Native installation", "# Cài đặt SDK trên React Native (React Native installation)"),
    ("# In-app ad revenue reporting", "# Báo cáo doanh thu quảng cáo trong ứng dụng (In-app ad revenue reporting)"),
    ("# Resources for data sharing after user consent", "# Chia sẻ dữ liệu sau khi người dùng đồng ý (Data sharing after user consent)"),
    ("# Install Pixel using code", "# Cài đặt Pixel bằng mã tùy chỉnh (Install Pixel using code)"),
    ("# Events API and Pixel setup", "# Thiết lập đồng thời TikTok Pixel và Events API (Events API and Pixel setup)"),
    ("# Set up events with data layer", "# Thiết lập sự kiện với Data Layer trong GTM (Set up events with data layer)"),

    # Doc 13
    ("The TikTok App Events SDK for React Native is maintained in a [public GitHub repository](https://github.com/tiktok/tiktok-business-react-native-sdk).",
     "TikTok App Events SDK dành cho React Native được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-react-native-sdk)."),
    ("### Install the npm package", "### Cài đặt gói npm"),
    ("After adding the npm package, install the native iOS pods:", "Sau khi thêm gói npm, cài đặt các pod iOS gốc:"),
    ("Ensure JitPack is available in your project's repository configuration:", "Đảm bảo JitPack có sẵn trong cấu hình kho lưu trữ (repository) của dự án:"),
    ("Developers who have already integrated the native TikTok App Events SDKs for Android (Java, Kotlin) or iOS (Objective-C, Swift) into their React Native projects can migrate to the React Native SDK by:",
     "Các nhà phát triển đã tích hợp SDK TikTok App Events gốc cho Android (Java, Kotlin) hoặc iOS (Objective-C, Swift) vào dự án React Native có thể chuyển đổi sang React Native SDK bằng cách:"),
    ("- Replacing the native SDK dependencies with the `@tiktok-for-business/react-native-sdk` npm package",
     "- Thay thế các phần phụ thuộc SDK gốc bằng gói npm `@tiktok-for-business/react-native-sdk`"),
    ("- Replacing any existing native SDK configurations and method calls with the React Native TypeScript / JavaScript equivalents",
     "- Thay thế các cấu hình và lệnh gọi phương thức SDK gốc bằng các lệnh tương đương trong React Native TypeScript / JavaScript"),
    ("Initialize the SDK as early as possible in your application's lifecycle, before tracking any events.",
     "Khởi tạo SDK càng sớm càng tốt trong vòng đời của ứng dụng, trước khi theo dõi bất kỳ sự kiện nào."),

    # Doc 14
    ("Starting from SDK version 1.5.0, in-app advertising mediation revenue reporting is supported. Simply pass the ad revenue data directly to the TikTok Business SDK as a dictionary/map of key-value pairs.",
     "Bắt đầu từ phiên bản SDK 1.5.0, tính năng báo cáo doanh thu hòa giải quảng cáo trong ứng dụng (ad mediation revenue) được hỗ trợ. Bạn chỉ cần truyền dữ liệu doanh thu quảng cáo trực tiếp tới TikTok Business SDK dưới dạng một từ điển (dictionary/map) các cặp khóa-giá trị."),
    ("•  For MAX and ironSource mediation, ensure all revenue is sent in USD.",
     "• Đối với nền tảng trung gian MAX và ironSource, hãy đảm bảo tất cả doanh thu được gửi theo đơn vị USD."),
    ("•  **The ad-revenue dictionary schema is per-mediation-platform.** The keys the SDK reads are selected by the SDK based on the platform you are using.",
     "• **Lược đồ từ điển doanh thu quảng cáo phụ thuộc vào từng nền tảng trung gian.** Các khóa mà SDK đọc được chọn dựa trên nền tảng bạn sử dụng."),
    ("•  Ensure that parameters are not null.", "• Đảm bảo rằng các tham số không bị null."),
    ("### Other mediation providers", "### Các nhà cung cấp trung gian hòa giải khác"),
    ("Do not use this code for MAX, ironSource, or AdMob mediation.", "Không sử dụng mã này cho nền tảng trung gian MAX, ironSource hoặc AdMob."),

    # Doc 15
    ("## Pre-consent tracking delay", "## Trì hoãn theo dõi trước khi người dùng đồng ý"),
    ("TikTok App Events SDK is designed to automatically transmit data to TikTok upon app open. TikTok provides delay configurations across each supported platform to allow your app to withhold event transmission until consent is granted.",
     "TikTok App Events SDK được thiết kế để tự động truyền dữ liệu tới TikTok khi ứng dụng được mở. TikTok cung cấp các cấu hình trì hoãn trên từng nền tảng nhằm cho phép ứng dụng của bạn giữ lại việc gửi sự kiện cho đến khi người dùng cấp quyền đồng ý."),
    ("By default, the SDK begins logging and sending events automatically upon initialisation. If you need to delay logging until after user consent is granted, use `TTConfig.Builder.setDelayUntilConsent()`.",
     "Theo mặc định, SDK sẽ tự động ghi nhật ký và gửi sự kiện khi khởi tạo. Nếu bạn cần trì hoãn việc ghi nhật ký cho đến sau khi người dùng đồng ý, hãy sử dụng `TTConfig.Builder.setDelayUntilConsent()`."),
    ("Once consent is granted, call `startTrack()` to begin sending all queued and future events to TikTok.",
     "Sau khi sự đồng ý được cấp, hãy gọi lệnh `startTrack()` để bắt đầu gửi tất cả các sự kiện đã xếp hàng đợi và các sự kiện trong tương lai tới TikTok."),
    ("#### **App Tracking Transparency timer**", "#### Bộ hẹn giờ App Tracking Transparency (ATT)"),
    ("To delay sending events on the first launch until users complete the ATT consent flow, you can call `setTrackingDelay()` with a timeout in seconds (default is 0, maximum is 60 seconds).",
     "Để trì hoãn việc gửi sự kiện trong lần khởi chạy đầu tiên cho đến khi người dùng hoàn thành luồng đồng ý ATT, bạn có thể gọi hàm `setTrackingDelay()` với thời gian chờ tính bằng giây (mặc định là 0, tối đa là 60 giây)."),
    ("##### **Manual delay**", "##### Trì hoãn thủ công (Manual delay)"),
    ("Once consent is granted, call `setTrackingEnabled(true)` to begin sending all queued and future events to TikTok.",
     "Sau khi sự đồng ý được cấp, hãy gọi `setTrackingEnabled(true)` để bắt đầu gửi tất cả các sự kiện trong hàng đợi và tương lai tới TikTok."),
    ("## Disabling automatic event collection", "## Tắt tính năng tự động thu thập sự kiện"),
    ("## Disabling Enhance data postback", "## Tắt tính năng tăng cường gửi trả dữ liệu (Enhance data postback)"),
    ("### 1. Events manager front-end toggle", "### 1. Nút bật/tắt trên giao diện Trình quản lý sự kiện"),
    ("### 2. Client-side global toggle", "### 2. Nút bật/tắt toàn cục phía máy khách (Client-side)"),
    ("### 3. Client-side low performance device flag", "### 3. Cờ thiết bị hiệu năng thấp phía máy khách"),

    # Doc 16
    ("# Before you begin", "# Trước khi bắt đầu"),
    ("# Install the pixel", "# Cài đặt Pixel"),
    ("# Event codes", "# Mã sự kiện (Event codes)"),
    ("## Install event code", "## Cài đặt mã sự kiện"),
    ("### Measure an event based on page load", "### Đo lường sự kiện dựa trên lượt tải trang (Page load)"),
    ("### Measure an event based on a button click", "### Đo lường sự kiện dựa trên lượt nhấp nút (Button click)"),
    ("# Bảng tham số (Parameters)", "# Bảng tham số (Parameters)"),
    ("## Adding parameters to event code", "## Thêm tham số vào mã sự kiện"),
    ("## Using dynamic values in your parameters", "## Sử dụng giá trị động trong các tham số"),
    ("# Disable the pixel when a user opts out", "# Vô hiệu hóa Pixel khi người dùng từ chối (Opt-out)"),
    ("# Verify your pixel and event setup", "# Xác minh thiết lập Pixel và sự kiện"),
    ("## 1. Pixel Helper", "## 1. TikTok Pixel Helper"),
    ("## 2. Test Events and Diagnostics", "## 2. Kiểm tra sự kiện và Chẩn đoán (Test Events & Diagnostics)"),
    ("## 3. Debug Mode", "## 3. Chế độ gỡ lỗi (Debug Mode)"),
    ("# FAQs", "# Câu hỏi thường gặp (FAQs)"),
    ("TikTok Pixel is a snippet of code that you can place on your website to track user actions, measure campaign performance, and optimize your TikTok ads.",
     "TikTok Pixel là một đoạn mã bạn có thể nhúng vào trang web để theo dõi hành động của người dùng, đo lường hiệu quả chiến dịch và tối ưu hóa quảng cáo TikTok."),

    # Doc 17
    ("To install TikTok Pixel and configure events sent to TikTok through both Pixel and Events API, you can complete the interactive setup flow in Events Manager.",
     "Để cài đặt TikTok Pixel và cấu hình gửi sự kiện tới TikTok thông qua cả Pixel và Events API, bạn có thể hoàn thành luồng thiết lập tương tác trong Trình quản lý sự kiện."),
    ("The GTM and Events API integration flow will set up **both TikTok Pixel and Events API**. This dual-channel approach maximizes the reliability and coverage of your event data.",
     "Luồng tích hợp GTM và Events API sẽ thiết lập **đồng thời cả TikTok Pixel và Events API**. Phương pháp tiếp cận kênh đôi này tối đa hóa độ tin cậy và độ bao phủ của dữ liệu sự kiện."),
    ("Here are the specific setup guides based on your requirements:\n- For TikTok Pixel only setup, see [TikTok Pixel only setup](do-luong-quang-cao-p2.md#doc-1799004034003969).\n- For Events API only setup, see Set up Events API only integration.",
     "Dưới đây là các hướng dẫn thiết lập cụ thể dựa trên nhu cầu của bạn:\n- Chỉ thiết lập TikTok Pixel: xem [Thiết lập chỉ dùng TikTok Pixel](do-luong-quang-cao-p2.md#doc-1799004034003969).\n- Chỉ thiết lập Events API: xem Thiết lập chỉ dùng Events API."),
    ("### Q1: Something went wrong during the Review and publish resources step. What should I do?",
     "### Q1: Có lỗi xảy ra trong bước Xem lại và xuất bản tài nguyên. Tôi nên làm gì?"),
    ("### Q2: How can I update the tagging server URL?",
     "### Q2: Làm thế nào để cập nhật URL máy chủ gắn thẻ (tagging server)?"),
    ("### Q3: Can I reuse my existing tagging server setup for Events API integration?",
     "### Q3: Tôi có thể tái sử dụng thiết lập máy chủ gắn thẻ hiện có để tích hợp Events API không?"),
    ("### Q4: How can I clean up or re-install?",
     "### Q4: Làm thế nào để dọn dẹp hoặc cài đặt lại?"),
    ("### Q5: How can I set up Events API only integration?",
     "### Q5: Làm thế nào để chỉ thiết lập tích hợp Events API đơn lẻ?"),
    ("### Q6:  How can I pick the right API to use?",
     "### Q6: Làm thế nào để tôi chọn đúng API phù hợp để sử dụng?"),
    ("### Q7: Do I still need to set up `event_id` to dedup events from Events API and Pixel?",
     "### Q7: Tôi có vẫn cần thiết lập `event_id` để khử trùng lặp giữa Events API và Pixel không?"),
    ("### Q8: I manually installed the [TikTok Events API (Official) template](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi) tag instead of using the Events Manager interactive flow. Can I continue using it?",
     "### Q8: Tôi đã cài đặt mẫu thẻ TikTok Events API (Official) thủ công từ thư viện GTM thay vì dùng luồng tương tác. Tôi có thể tiếp tục dùng nó không?"),
    ("### Q9: How can I generate a new access token for my Events API integration if I switched to a different Pixel?",
     "### Q9: Làm thế nào để tạo mã truy cập mới cho Events API nếu tôi chuyển sang một Pixel khác?"),

    # Doc 18
    ("The data layer is an object used by Google Tag Manager (GTM) and `gtag.js` to pass information to tags. You can use the data layer to pass event parameters and user data to TikTok tags.",
     "Lớp dữ liệu (Data Layer) là một đối tượng được sử dụng bởi Google Tag Manager (GTM) và `gtag.js` để truyền thông tin vào các thẻ. Bạn có thể sử dụng lớp dữ liệu để truyền các tham số sự kiện và dữ liệu người dùng tới các thẻ của TikTok."),
    ("We have developed two templates, the [TikTok Pixel template](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-pixel) and the [TikTok Events API (Official) template](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi), to help you easily set up events using the data layer.",
     "Chúng tôi đã phát triển hai mẫu: [TikTok Pixel template](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-pixel) và [TikTok Events API (Official) template](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi), giúp bạn dễ dàng thiết lập các sự kiện bằng Data Layer."),
    ("This document covers the following content:\n- Prerequisites for setting up data layer events\n- An example of a purchase event\n- Overview of the data layer event schema, including recommended event types and parameters",
     "Tài liệu này bao gồm các nội dung sau:\n- Điều kiện tiên quyết để thiết lập sự kiện qua Data Layer\n- Ví dụ về sự kiện mua hàng (Purchase)\n- Tổng quan về lược đồ sự kiện Data Layer, bao gồm các loại sự kiện và tham số đề xuất"),
    ("## A simple `purchase` event", "## Ví dụ sự kiện mua hàng `Purchase` đơn giản"),
    ("## Event name mapping", "## Ánh xạ tên sự kiện (Event name mapping)"),
    ("## Website event parameters", "## Tham số sự kiện trang web"),
    ("### Product data", "### Dữ liệu sản phẩm (Product data)"),
    ("### User data", "### Dữ liệu người dùng (User data)"),
    ("## Send data layer events to server tags", "## Gửi sự kiện Data Layer tới thẻ máy chủ (Server tags)"),
    ("### Set up a Google Tag", "### Thiết lập thẻ Google Tag"),
    ("### Set up a GA4 Event tag", "### Thiết lập thẻ sự kiện GA4"),
    ("#### GA4 Event Parameters", "#### Các tham số sự kiện GA4"),
    ("### Ví dụ lệnh cURL (Example) configuration", "### Cấu hình mẫu"),
    ("### How to set up deduplication", "### Cách thiết lập khử trùng lặp (Deduplication)"),
    ("## Verify events setup", "## Xác minh thiết lập sự kiện"),
    ("## Support", "## Hỗ trợ"),
]

for i in range(13, len(docs)):
    doc_text = docs[i]
    for old, new in replacements_13_18:
        doc_text = doc_text.replace(old, new)
    docs[i] = doc_text

new_text = "".join(docs)
with open(TOM_TAT_PATH, "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Đã cập nhật dịch cho Docs 13-18 trong {TOM_TAT_PATH}")
