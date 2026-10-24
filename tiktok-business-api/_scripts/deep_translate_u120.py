import os, re

def deep_translate_u120():
    path = "docs/09-marketing-api/bao-cao-p3.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Intros and notes
    replacements = [
        # Basic filters notes
        ("> -  If the provided filter field `field_name` and `data_level` don't match, the system will return an error: \"Invalid value for filter field: xxxx is not supported\". For example, if `data_level` is `AUCTION_AD`, you can only set `field_name` to a filter field at the ad level (such as `ad_ids`).",
         "> - Nếu trường bộ lọc `field_name` và cấp dữ liệu `data_level` không khớp, hệ thống sẽ trả về lỗi: \"Invalid value for filter field: xxxx is not supported\". Ví dụ: Nếu `data_level` là `AUCTION_AD`, bạn chỉ có thể đặt `field_name` là trường bộ lọc ở cấp quảng cáo (chẳng hạn `ad_ids`)."),
        ("> - In asynchronous basic reports, the only supported filter fields are `campaign_ids`, `adgroup_ids`, and `ad_ids`.",
         "> - Trong các báo cáo cơ bản bất đồng bộ, các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids` và `ad_ids`."),
        ("> -  Basic reports now include data for Auction ads, Reach & Frequency ads, and TopView ads. To filter data for a specific buying type, use [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) to run a basic report. Within the filtering object, specify the `buying_type` field and enter the values of either `AUCTION`, `RESERVATION_TOP_VIEW`, or `RESERVATION_RF`.",
         "> - Báo cáo cơ bản hiện bao gồm dữ liệu cho quảng cáo Đấu thầu (Auction), quảng cáo Tiếp cận & Tần suất (R&F) và quảng cáo TopView. Để lọc dữ liệu theo loại hình mua cụ thể, hãy gọi [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353). Trong đối tượng lọc, chỉ định trường `buying_type` với một trong các giá trị `AUCTION`, `RESERVATION_TOP_VIEW` hoặc `RESERVATION_RF`."),
        ("> -  For TopView ads, cost-related metrics at ad level and cost-related metrics for audience breakdown will only include data for ads delivered after January 18th, 2024.",
         "> - Đối với quảng cáo TopView, các chỉ số liên quan đến chi phí ở cấp quảng cáo và theo phân tích đối tượng chỉ bao gồm dữ liệu của các quảng cáo phân phối sau ngày 18 tháng 1 năm 2024."),
        ("> -  The reporting data for [Product GMV max ads](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) and LIVE GMV max ads created from TikTok Shop is excluded from synchronous Auction basic reports, audience reports, playable ad reports, and DSA reports. Shopping Ads created via API or TikTok Ads Manager are not affected.",
         "> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo đấu thầu cơ bản đồng bộ, báo cáo đối tượng, báo cáo tương tác và báo cáo DSA. Quảng cáo mua sắm tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng."),

        # Audience reports intro & notes
        ("Audience reports are a type of report from which you can get audience data, including age, gender, region, or interest.",
         "Báo cáo đối tượng (Audience reports) là loại báo cáo cho phép bạn truy xuất dữ liệu nhân khẩu học và hành vi của đối tượng khán giả tiếp cận, bao gồm độ tuổi, giới tính, vùng địa lý hoặc sở thích."),
        ("> **Notes** • The data in audience reports is not real-time data. There is 10-12 hours of processing latency for audience data. • Running audience reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode. • We have optimized reporting performance for audience reports with the dimension of `behavior_id` via [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353). To learn more about this optimization, refer to [Audience reports-Supported dimensions](bao-cao-p3.md#doc-1751454103714818).",
         "> **Lưu ý:** • Dữ liệu trong báo cáo đối tượng không phải là dữ liệu thời gian thực mà có độ trễ xử lý khoảng 10-12 giờ. • Không hỗ trợ chạy báo cáo đối tượng ở chế độ CHUNK (`query_mode` = `CHUNK`). Chế độ CHUNK chỉ hỗ trợ cho báo cáo cơ bản đồng bộ. • Hiệu năng truy vấn cho báo cáo đối tượng theo chiều `behavior_id` đã được tối ưu hóa qua endpoint [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353). Xem chi tiết tại [Báo cáo đối tượng - Các chiều dữ liệu hỗ trợ](bao-cao-p3.md#doc-1751454103714818)."),
        ("Currently, this optimization is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.",
         "Hiện tại, tính năng tối ưu hóa này chỉ dành cho danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt."),
        ("See [here](bao-cao-p3.md#doc-1751454103714818) for supported dimensions of audience reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751454103714818) để tra cứu các chiều dữ liệu hỗ trợ trong báo cáo đối tượng."),
        ("See [here](bao-cao-p3.md#doc-1751454162042882) for supported metrics of audience reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751454162042882) để tra cứu các chỉ số hỗ trợ trong báo cáo đối tượng."),
        ("See [here](bao-cao-p3.md#doc-1751454172429314) for supported filters of audience reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751454172429314) để tra cứu các bộ lọc hỗ trợ trong báo cáo đối tượng."),
        ("Lifetime metrics for audience reports are not available in v1.3.",
         "Các chỉ số trọn đời (lifetime metrics) cho báo cáo đối tượng không khả dụng trong phiên bản API v1.3."),

        # Use cases in Audience reports
        ("**1. Query age and gender breakdown of an ad group over a period of time.**",
         "**1. Truy vấn phân tích theo độ tuổi và giới tính của một nhóm quảng cáo trong một khoảng thời gian.**"),
        ("**2. Query the region distribution of all undeleted ad groups under certain campaigns over a period of time.**",
         "**2. Truy vấn phân bổ theo vùng địa lý của tất cả nhóm quảng cáo chưa bị xóa thuộc các chiến dịch nhất định.**"),

        # Playable ad reports intro & notes
        ("Playable ad reports are a type of report from which you can get data about playable creatives.",
         "Báo cáo quảng cáo tương tác (Playable ad reports) là loại báo cáo cho phép bạn truy xuất dữ liệu hiệu suất của các mẫu quảng cáo tương tác dạng playable."),
        ("> **Note:**  • Playable ads report returns data of playable creatives. `data_level` is not required in your request.  • Running playable ad reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode.",
         "> **Lưu ý:** • Báo cáo quảng cáo tương tác trả về dữ liệu của các tài nguyên playable. Bạn không cần truyền `data_level` trong yêu cầu. • Không hỗ trợ chạy báo cáo tương tác ở chế độ CHUNK (`query_mode` = `CHUNK`)."),
        ("See [here](bao-cao-p3.md#doc-1751617879104514) for supported dimensions of playable ad reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751617879104514) để biết các chiều dữ liệu hỗ trợ trong báo cáo quảng cáo tương tác."),
        ("See [here](bao-cao-p3.md#doc-1762405483224065) for supported metrics for a dimension in playable ad reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1762405483224065) để biết các chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo quảng cáo tương tác."),
        ("See [here](bao-cao-p3.md#doc-1751617882108929) for supported metrics of playable ad reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751617882108929) để biết các chỉ số hỗ trợ trong báo cáo quảng cáo tương tác."),
        ("See [here](bao-cao-p3.md#doc-1751617884206210) for supported filters of playable ad reports.",
         "Xem [tại đây](bao-cao-p3.md#doc-1751617884206210) để biết các bộ lọc hỗ trợ trong báo cáo quảng cáo tương tác."),

        # DSA reports intro & notes
        ("DSA reports are a type of report from which you can get comprehensive data about dynamic showcase ads (DSA), including catalog-level, SPU-level, and SKU-level data.",
         "Báo cáo DSA (Dynamic Showcase Ads) là loại báo cáo cho phép bạn truy xuất dữ liệu toàn diện về quảng cáo danh mục sản phẩm động, bao gồm dữ liệu ở cấp danh mục (catalog), cấp nhóm sản phẩm (SPU) và cấp mã sản phẩm cụ thể (SKU)."),
        ("> **Note:** • Running DSA reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode. • In synchronous DSA reports, the results only include data for the current catalog, and the historical data of deleted catalogs cannot be retrieved.",
         "> **Lưu ý:** • Không hỗ trợ chạy báo cáo DSA ở chế độ CHUNK (`query_mode` = `CHUNK`). • Trong báo cáo DSA đồng bộ, kết quả chỉ bao gồm dữ liệu cho danh mục hiện tại, dữ liệu lịch sử của danh mục đã xóa không thể truy xuất."),

        # Reservation ad reports intro & notes
        ("Reservation ad reports are a type of report from which you can get data about reservation ads.",
         "Báo cáo quảng cáo đặt trước (Reservation ad reports) là loại báo cáo cho phép bạn lấy dữ liệu về các quảng cáo đặt trước (như Reach & Frequency, TopView)."),
        ("> **Important:**\n> To retrieve the reporting data of TopView ads, use the [basic reports](bao-cao-p1.md#doc-1738864915188737).",
         "> **Quan trọng:**\n> Để lấy dữ liệu báo cáo cho quảng cáo TopView, vui lòng sử dụng [Báo cáo cơ bản (Basic reports)](bao-cao-p1.md#doc-1738864915188737)."),

        # Business Center reports intro & notes
        ("Business Center reports are a type of report from which you can get comprehensive data about ad accounts in a Business Center, including spend and performance data, video play data, as well as data for in-app events.",
         "Báo cáo Business Center (Business Center reports) là loại báo cáo cho phép bạn trích xuất dữ liệu tổng hợp về các tài khoản quảng cáo thuộc Business Center, bao gồm chi phí chi tiêu, số liệu hiệu suất, số liệu phát video và các sự kiện trong ứng dụng."),
        ("> **Note:** Currently, Business Center reports only support synchronous mode. To learn about how to create a synchronous Business Center report, refer to [Run a synchronous report](bao-cao-p1.md#doc-1738864778664961).",
         "> **Lưu ý:** Hiện tại, báo cáo Business Center chỉ hỗ trợ chế độ đồng bộ (synchronous mode). Để tìm hiểu cách tạo báo cáo Business Center đồng bộ, tham khảo [Chạy báo cáo đồng bộ](bao-cao-p1.md#doc-1738864778664961)."),
        ("A dimension is an attribute to group your data by. Business Center reports support the following dimensions.",
         "Chiều dữ liệu (Dimension) là thuộc tính dùng để nhóm và phân loại dữ liệu báo cáo của bạn. Báo cáo Business Center hỗ trợ các chiều dữ liệu sau:"),

        # Dimension intros across sections
        ("A dimension is an attribute to group your data by. Audience reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.",
         "Chiều dữ liệu (Dimension) là thuộc tính dùng để nhóm và phân loại dữ liệu báo cáo. Báo cáo đối tượng hỗ trợ các chiều dữ liệu sau. Xin lưu ý rằng hệ thống hiện chưa hỗ trợ toàn bộ các chiều dữ liệu có trên TikTok Ads Manager."),
        ("A dimension is an attribute to group your data by. Playable ad reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.",
         "Chiều dữ liệu (Dimension) là thuộc tính dùng để nhóm và phân loại dữ liệu báo cáo. Báo cáo quảng cáo tương tác hỗ trợ các chiều dữ liệu sau:"),
        ("A dimension is an attribute to group your data by. DSA reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.",
         "Chiều dữ liệu (Dimension) là thuộc tính dùng để nhóm và phân loại dữ liệu báo cáo. Báo cáo DSA hỗ trợ các chiều dữ liệu sau:"),
        ("A dimension is an attribute to group your data by. Reservation ad reports support the following dimensions. Please note that currently, we don't support all dimensions available on Reservation Ad Platform.",
         "Chiều dữ liệu (Dimension) là thuộc tính dùng để nhóm và phân loại dữ liệu báo cáo. Báo cáo quảng cáo đặt trước hỗ trợ các chiều dữ liệu sau:"),

        # Metrics intros across sections
        ("You can use the following metrics in audience reports. Metrics that have no consumption will be returned as `-`. Please note that currently, we don't support all metrics available on TikTok Ads Manager.",
         "Bạn có thể sử dụng các chỉ số sau trong báo cáo đối tượng. Các chỉ số không phát sinh chi tiêu sẽ được trả về dưới dạng `-`. Lưu ý rằng hiện tại hệ thống chưa hỗ trợ tất cả các chỉ số có trên TikTok Ads Manager."),
        ("You can use the following metrics in playable ad reports. Metrics that have no consumption will be returned as `-`. Please note that currently, we don't support all metrics available on TikTok Ads Manager.",
         "Bạn có thể sử dụng các chỉ số sau trong báo cáo quảng cáo tương tác. Các chỉ số không phát sinh chi tiêu sẽ trả về `-`."),
        ("You can use the following metrics in DSA reports. Metrics that have no consumption will be returned as `-`. Please note that currently, we don't support all metrics available on TikTok Ads Manager.",
         "Bạn có thể sử dụng các chỉ số sau trong báo cáo DSA. Các chỉ số không phát sinh chi tiêu sẽ trả về `-`."),
        ("You can use the following metrics in reservation ad reports. Metrics that have no consumption will be returned as `-`. Please note that currently, we don't support all metrics available on Reservation Ad Platform.",
         "Bạn có thể sử dụng các chỉ số sau trong báo cáo quảng cáo đặt trước. Các chỉ số không phát sinh chi tiêu sẽ trả về `-`."),

        # Dimension descriptions in tables
        ("| Group by day |", "| Nhóm theo ngày (Group by day) |"),
        ("| Group by hour |", "| Nhóm theo giờ (Group by hour) |"),
        ("| Group by gender |", "| Nhóm theo giới tính (Group by gender) |"),
        ("| Group by age |", "| Nhóm theo độ tuổi (Group by age) |"),
        ("| Group by location code.", "| Nhóm theo mã vị trí địa lý (Location code)."),
        ("| Group by location ID.", "| Nhóm theo mã định danh vị trí (Location ID)."),
        ("| Group by Designated Market Area (DMA).", "| Nhóm theo Khu vực thị trường chỉ định (DMA)."),
        ("| Group by audience network |", "| Nhóm theo mạng lưới kết nối của đối tượng (Audience network) |"),
        ("| Group by audience language |", "| Nhóm theo ngôn ngữ của đối tượng (Audience language) |"),
        ("| Grouped by operating system |", "| Nhóm theo hệ điều hành thiết bị (Operating system) |"),
        ("| Group by device model |", "| Nhóm theo mẫu thiết bị (Device model) |"),
        ("| Group by telecom operator |", "| Nhóm theo nhà mạng viễn thông (Telecom operator) |"),
        ("| Group by internet connection type |", "| Nhóm theo loại kết nối Internet |"),
        ("| Group by campaign ID |", "| Nhóm theo ID chiến dịch (Campaign ID) |"),
        ("| Group by ad group ID |", "| Nhóm theo ID nhóm quảng cáo (Ad group ID) |"),
        ("| Group by ad ID |", "| Nhóm theo ID mẫu quảng cáo (Ad ID) |"),
        ("| Group by playable creative ID |", "| Nhóm theo ID tài nguyên tương tác (Playable ID) |"),
        ("| Group by country or region code. |", "| Nhóm theo mã quốc gia hoặc khu vực (Country/Region code) |"),
        ("| Group by catalog ID |", "| Nhóm theo ID danh mục sản phẩm (Catalog ID) |"),
        ("| Group by SPU ID |", "| Nhóm theo ID sản phẩm tiêu chuẩn (SPU ID) |"),
        ("| Group by SKU ID |", "| Nhóm theo ID đơn vị lưu kho (SKU ID) |"),
        ("| Group by brand |", "| Nhóm theo thương hiệu (Brand) |"),
        ("| Group by product category |", "| Nhóm theo danh mục sản phẩm (Product category) |"),
        ("| Group by advertiser ID |", "| Nhóm theo ID tài khoản nhà quảng cáo (Advertiser ID) |"),
        ("| Group by placement |", "| Nhóm theo vị trí hiển thị quảng cáo (Placement) |"),
        ("| Group by week |", "| Nhóm theo tuần (Group by week) |"),
        ("| Group by month |", "| Nhóm theo tháng (Group by month) |"),
    ]

    for o, n in replacements:
        text = text.replace(o, n)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done deep_translate_u120")

if __name__ == "__main__":
    deep_translate_u120()
