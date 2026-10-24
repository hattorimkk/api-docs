import re

path = "tiktok-business-api/docs/api-reference/62-upgraded-smartplus-p1.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    # Breadcrumbs
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Get Upgraded Smart+ Campaigns", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Lấy danh sách chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Create an Upgraded Smart+ Campaign", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Tạo chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Update an Upgraded Smart+ Campaign", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Cập nhật chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Update the operation statuses of Upgraded Smart+ Campaigns", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Create an asynchronous copy task for an Upgraded Smart+ Campaign", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Campaigns > Get the results of an asynchronous copy task for an Upgraded Smart+ Campaign", "> Đường dẫn: API Reference > Smart+ nâng cấp > Chiến dịch > Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp"),
    ("> Đường dẫn: API Reference > Upgraded Smart+ > Ad groups", "> Đường dẫn: API Reference > Smart+ nâng cấp > Nhóm quảng cáo"),

    # Callout notes
    ("> Starting at the end of September 2026, you can no longer create non-CBO (Campaign Budget Optimization) App Install VBO campaigns via the API. Specifically, this restriction applies to campaigns where `app_promotion_type` is set to `APP_INSTALL` and `budget_optimize_on` is `false` at the campaign level, while `optimization_goal` is set to `VALUE` at the ad group level. This change is being made because these configurations have demonstrated significantly weaker delivery performance compared to their CBO counterparts. This change applies to new campaign creation only and does not affect existing campaign setups. To ensure a smooth API integration, we recommend that you enable the CBO setting for your App Install VBO campaigns by setting `budget_optimize_on` to `true` at the campaign level.",
     "> Bắt đầu từ cuối tháng 9 năm 2026, bạn sẽ không còn có thể tạo các chiến dịch VBO Cài đặt ứng dụng không dùng CBO (Tối ưu hóa ngân sách chiến dịch) qua API. Cụ thể, hạn chế này áp dụng cho các chiến dịch có `app_promotion_type` được đặt thành `APP_INSTALL` và `budget_optimize_on` là `false` ở cấp chiến dịch, trong khi `optimization_goal` được đặt thành `VALUE` ở cấp nhóm quảng cáo. Thay đổi này được thực hiện vì các cấu hình này cho thấy hiệu suất phân phối yếu hơn đáng kể so với các chiến dịch sử dụng CBO. Thay đổi này chỉ áp dụng cho việc tạo mới chiến dịch và không ảnh hưởng đến các thiết lập chiến dịch hiện có. Để đảm bảo tích hợp API diễn ra suôn sẻ, chúng tôi khuyến nghị bạn nên bật cài đặt CBO cho các chiến dịch VBO Cài đặt ứng dụng bằng cách đặt `budget_optimize_on` thành `true` ở cấp chiến dịch."),

    ("We recommend waiting approximately five minutes after creating a task using [/smart_plus/campaign/copy/task/create/](62-upgraded-smartplus-p1.md#doc-1866528879472641) before checking the results.",
     "Chúng tôi khuyến nghị nên đợi khoảng 5 phút sau khi tạo tác vụ bằng endpoint [/smart_plus/campaign/copy/task/create/](62-upgraded-smartplus-p1.md#doc-1866528879472641) trước khi kiểm tra kết quả."),

    ("Ad groups are the middle level of advertising. You can set specific ad placements, target audiences, budgets, schedule, bids, and optimization goals for each ad group at the ad group level.",
     "Nhóm quảng cáo là cấp độ trung gian trong cấu trúc phân cấp quảng cáo. Bạn có thể thiết lập các vị trí hiển thị quảng cáo cụ thể, đối tượng nhắm mục tiêu, ngân sách, lịch chạy, giá thầu và mục tiêu tối ưu hóa cho từng nhóm quảng cáo ở cấp nhóm quảng cáo."),

    # Example subheaders for copy task
    ("#### Default copy mode: all settings duplicated exactly from source campaign", "#### Chế độ sao chép mặc định: nhân bản chính xác tất cả cài đặt từ chiến dịch nguồn"),
    ("#### Default copy mode: campaign-level overrides and shared schedule for new ad groups", "#### Chế độ sao chép mặc định: ghi đè cấp chiến dịch và dùng chung lịch chạy cho các nhóm quảng cáo mới"),
    ("#### Custom copy mode: campaign-level overrides, shared schedule for new ad groups, and ad group-level overrides", "#### Chế độ sao chép tùy chỉnh: ghi đè cấp chiến dịch, dùng chung lịch chạy cho nhóm quảng cáo mới và ghi đè cấp nhóm quảng cáo"),
    ("#### Custom copy mode: campaign-level overrides, shared schedule for new ad groups, ad group-level overrides, and ad-level overrides", "#### Chế độ sao chép tùy chỉnh: ghi đè cấp chiến dịch, dùng chung lịch chạy cho nhóm quảng cáo mới, ghi đè cấp nhóm quảng cáo và ghi đè cấp quảng cáo"),

    # Code and response descriptions
    ("| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../phu-luc/phu-luc-p1.md#doc-1737172488964097). |",
     "| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../phu-luc/phu-luc-p1.md#doc-1737172488964097). |"),
    ("| ↳↳ create_time | string | The time when the campaign was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time) |",
     "| ↳↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |"),
    ("| ↳↳ modify_time | string | The time when the campaign was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time) |",
     "| ↳↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |"),
    ("| ↳↳ app_promotion_type | string | App promotion type. ⏎ Enum value: • `APP_INSTALL`: App install. Get new users to install your app. • `APP_RETARGETING`: App retargeting. Re-engage existing app users to take action in your app. • `MINIS`: TikTok Mini or Series. Promote your Series, mini series, or mini game by optimizing for organic and ads traffic. |",
     "| ↳↳ app_promotion_type | string | Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác người dùng ứng dụng hiện tại để thực hiện hành động trong ứng dụng. • `MINIS`: TikTok Mini hoặc Series. Quảng bá Series, phim ngắn nhiều tập hoặc mini game bằng cách tối ưu hóa lưu lượng truy cập tự nhiên và quảng cáo. |"),
    ("| ↳↳ campaign_type | string | Campaign type. ⏎ Currently, we support `REGULAR_CAMPAIGN` and `IOS14_CAMPAIGN`. |",
     "| ↳↳ campaign_type | string | Loại chiến dịch. ⏎ Hiện tại hỗ trợ `REGULAR_CAMPAIGN` và `IOS14_CAMPAIGN`. |"),
    ("| ↳↳ app_id | string | The App ID of the app to promote. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |",
     "| ↳↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |"),
    ("| ↳↳ budget_mode | string | Budget mode. ⏎ • When `budget_optimize_on` is `true` or not specified, the enum values are: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily campaign budget. It is the average daily budget over a week. Daily costs will not exceed 125% of the average daily budget. Weekly costs will not exceed the average daily budget * 7. • `BUDGET_MODE_TOTAL`: Lifetime campaign budget. • When `budget_optimize_on` is `false`, the enum values are: • `BUDGET_MODE_INFINITE`: No limit for all ad groups under this campaign. • `BUDGET_MODE_DAY`: Daily budget limit for all ad groups under this campaign. • `BUDGET_MODE_TOTAL`: Total budget limit for all ad groups under this campaign. |",
     "| ↳↳ budget_mode | string | Chế độ ngân sách. ⏎ • Khi `budget_optimize_on` là `true` hoặc không chỉ định, các giá trị enum gồm: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. Là mức ngân sách hàng ngày trung bình trong một tuần. Chi phí hàng ngày sẽ không vượt quá 125% ngân sách trung bình và chi phí hàng tuần không vượt quá 7 lần ngân sách hàng ngày trung bình. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • Khi `budget_optimize_on` là `false`, các giá trị enum gồm: • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách cho các nhóm quảng cáo trong chiến dịch này. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày cho tất cả các nhóm quảng cáo trong chiến dịch. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách cho tất cả các nhóm quảng cáo trong chiến dịch. |"),
    ("| ↳↳ budget | float | • When `budget_optimize_on` is `true` or not specified, this field represents fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. • When `budget_optimize_on` is `false`, this field represents the limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_DAY`, this field represents the daily limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_TOTAL`, this field represents the total limit for all ad groups under this campaign. |",
     "| ↳↳ budget | float | • Khi `budget_optimize_on` là `true` hoặc không chỉ định, trường này đại diện cho ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách chiến dịch cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. • Khi `budget_optimize_on` là `false`, trường này đại diện cho hạn mức cho tất cả nhóm quảng cáo trong chiến dịch. • Khi `budget_mode` là `BUDGET_MODE_DAY`, trường này đại diện cho hạn mức hàng ngày. • Khi `budget_mode` là `BUDGET_MODE_TOTAL`, trường này đại diện cho hạn mức tổng ngân sách. |"),
    ("| ↳↳ current_budget | float | Returned only when `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`. ⏎ Current campaign budget for a campaign with Goal-based budget increase enabled. |",
     "| ↳↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách chiến dịch hiện tại cho chiến dịch đã bật tự động tăng ngân sách theo mục tiêu. |"),
    ("| ↳↳ po_number | string | PO (purchase order) number. ⏎ PO numbers are useful for invoice tracking and reconciliation. ⏎ [Learn more about PO numbers on monthly invoices](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |",
     "| ↳↳ po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |"),
    ("| ↳↳ rta_id | string | Realtime API (RTA) ID, the RTA strategy identifier. |",
     "| ↳↳ rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. |"),
    ("| po_number | string | PO (purchase order) number. ⏎ PO numbers are useful for invoice tracking and reconciliation. ⏎ [Learn more about PO numbers on monthly invoices](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |",
     "| po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |"),
    ("| rta_id | string | Realtime API (RTA) ID, the RTA strategy identifier. ⏎ The RTA enables you to integrate real-time audience data to customize ad auction and targeting, thereby delivering better performance. ⏎ To obtain the list of RTA IDs associated with your ad account, contact your TikTok representative. ⏎ **Note**:  • Enabling RTA for your ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • You can not update `rta_id` after campaign creation. |",
     "| rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. ⏎ RTA cho phép bạn tích hợp dữ liệu đối tượng thời gian thực để tùy chỉnh đấu thầu và nhắm mục tiêu quảng cáo, qua đó mang lại hiệu suất tốt hơn. ⏎ Để lấy danh sách ID RTA liên kết với tài khoản quảng cáo, hãy liên hệ với đại diện TikTok của bạn. ⏎ **Lưu ý**: • Bật RTA cho quảng cáo hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn sử dụng, vui lòng liên hệ với đại diện TikTok của bạn. • Bạn không thể cập nhật `rta_id` sau khi tạo chiến dịch. |"),
    ("| ↳ create_time | string | The time when the campaign was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). |",
     "| ↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |"),
    ("| ↳ modify_time | string | The time when the campaign was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). |",
     "| ↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |"),
    ("| ↳ objective_type | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. |",
     "| ↳ objective_type | string | Mục tiêu quảng cáo. ⏎ Hiện tại hỗ trợ `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`. |"),
    ("| ↳ budget_mode | string | Budget mode. ⏎ Supported values: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily campaign budget. • `BUDGET_MODE_TOTAL`: Lifetime campaign budget. • `BUDGET_MODE_DAY`: Daily budget limit for all ad groups under this campaign. • `BUDGET_MODE_TOTAL`: Total budget limit for all ad groups under this campaign. • `BUDGET_MODE_INFINITE`: No budget limit for all ad groups under this campaign. |",
     "| ↳ budget_mode | string | Chế độ ngân sách. ⏎ Các giá trị được hỗ trợ: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày cho tất cả các nhóm quảng cáo trong chiến dịch. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách cho tất cả các nhóm quảng cáo trong chiến dịch. • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách cho các nhóm quảng cáo trong chiến dịch. |"),
    ("| ↳ budget | float | • When `budget_optimize_on` is `true` or not specified, this field represents fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. • When `budget_optimize_on` is `false`, this field represents the limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_DAY`, this field represents the daily limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_TOTAL`, this field represents the total limit for all ad groups under this campaign. |",
     "| ↳ budget | float | • Khi `budget_optimize_on` là `true` hoặc không chỉ định, trường này đại diện cho ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách chiến dịch cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. • Khi `budget_optimize_on` là `false`, trường này đại diện cho hạn mức cho tất cả nhóm quảng cáo trong chiến dịch. • Khi `budget_mode` là `BUDGET_MODE_DAY`, trường này đại diện cho hạn mức hàng ngày. • Khi `budget_mode` là `BUDGET_MODE_TOTAL`, trường này đại diện cho hạn mức tổng ngân sách. |"),
    ("| ↳ current_budget | float | Returned only when `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`. ⏎ Current campaign budget for a campaign with Goal-based budget increase enabled. |",
     "| ↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách chiến dịch hiện tại cho chiến dịch đã bật tự động tăng ngân sách theo mục tiêu. |"),
    ("| ↳ roas_bid | float | Returned when CBO is enabled (`budget_optimize_on` is `true`) and `deep_bid_type` is `VO_MIN_ROAS`. ⏎ Target ROAS for Value-Based Optimization. |",
     "| ↳ roas_bid | float | Được trả về khi CBO được bật (`budget_optimize_on` là `true`) và `deep_bid_type` là `VO_MIN_ROAS`. ⏎ ROAS mục tiêu cho Tối ưu hóa theo giá trị (Value-Based Optimization). |"),
    ("| ↳ po_number | string | PO (purchase order) number. ⏎ PO numbers are useful for invoice tracking and reconciliation. ⏎ [Learn more about PO numbers on monthly invoices](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |",
     "| ↳ po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |"),
    ("| ↳ rta_id | string | Realtime API (RTA) ID, the RTA strategy identifier. |",
     "| ↳ rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. |"),
    ("| campaign_id | string | ID chiến dịch quảng cáo. |",
     "| campaign_id | string | ID chiến dịch quảng cáo. |"),

    # Copy task tables
    ("| ↳ adgroup_error_list | object[] | The errors encountered during the process of copying specific ad groups. |",
     "| ↳ adgroup_error_list | object[] | Các lỗi phát sinh trong quá trình sao chép các nhóm quảng cáo cụ thể. |"),
    ("| ↳↳ campaign_name | string | The name of the newly created campaign. ⏎ If the campaign copy process fails, this field is still returned to indicate the campaign that was not successfully copied. |",
     "| ↳↳ campaign_name | string | Tên của chiến dịch mới được tạo. ⏎ Nếu quá trình sao chép chiến dịch thất bại, trường này vẫn được trả về để cho biết chiến dịch chưa được sao chép thành công. |"),
    ("| ↳↳ campaign_error_infos | string[] | The errors encountered during the campaign copy process. ⏎ If no errors occurred, the value of this field is an empty list (`[]`). |",
     "| ↳↳ campaign_error_infos | string[] | Các lỗi phát sinh trong quá trình sao chép chiến dịch. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |"),
    ("| ↳↳↳ adgroup_name | string | The name of the newly created ad group. ⏎ If the ad group copy process fails, this field is still returned to indicate the ad group that was not successfully copied. |",
     "| ↳↳↳ adgroup_name | string | Tên của nhóm quảng cáo mới được tạo. ⏎ Nếu quá trình sao chép nhóm quảng cáo thất bại, trường này vẫn được trả về để cho biết nhóm quảng cáo chưa được sao chép thành công. |"),
    ("| ↳↳↳ adgroup_error_list | string[] | The errors encountered during the ad group copy process. ⏎ If no errors occurred, the value of this field is an empty list (`[]`). |",
     "| ↳↳↳ adgroup_error_list | string[] | Các lỗi phát sinh trong quá trình sao chép nhóm quảng cáo. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |"),
    ("| ↳↳↳↳ ad_name | string | The name of the newly created ad. ⏎ If the ad copy process fails, this field is still returned to indicate the ad that was not successfully copied. |",
     "| ↳↳↳↳ ad_name | string | Tên của quảng cáo mới được tạo. ⏎ Nếu quá trình sao chép quảng cáo thất bại, trường này vẫn được trả về để cho biết quảng cáo chưa được sao chép thành công. |"),
    ("| ↳↳↳↳ ad_error_list | string[] | The errors encountered during the ad copy process. ⏎ If no errors occurred, the value of this field is an empty list (`[]`). |",
     "| ↳↳↳↳ ad_error_list | string[] | Các lỗi phát sinh trong quá trình sao chép quảng cáo. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |"),
]

applied = 0
for src, dst in replacements:
    if src in text:
        text = text.replace(src, dst)
        applied += 1
    else:
        print(f"Warning: NOT FOUND: {src[:60]}")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Applied {applied}/{len(replacements)} replacements to 62-upgraded-smartplus-p1.md")
