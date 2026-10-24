import re

path = "tiktok-business-api/docs/api-reference/62-upgraded-smartplus-p1.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

# Let us do direct line replacements
new_lines = []
for l in lines:
    s = l.strip()
    if s.startswith("| rta_id | string | Realtime API"):
        new_lines.append("| rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. ⏎ RTA cho phép bạn tích hợp dữ liệu đối tượng thời gian thực để tùy chỉnh đấu thầu và nhắm mục tiêu, qua đó mang lại hiệu suất tốt hơn. ⏎ Để lấy danh sách ID RTA liên kết với tài khoản quảng cáo, hãy liên hệ với đại diện TikTok của bạn. ⏎ **Lưu ý**: • Bật RTA cho quảng cáo hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Bạn không thể cập nhật `rta_id` sau khi tạo chiến dịch. |")
    elif s.startswith("| ↳ create_time | string | The time when"):
        new_lines.append("| ↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |")
    elif s.startswith("| ↳ modify_time | string | The time when"):
        new_lines.append("| ↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |")
    elif s.startswith("| ↳ objective_type | string | Advertising objective"):
        new_lines.append("| ↳ objective_type | string | Mục tiêu quảng cáo. ⏎ Hiện tại hỗ trợ `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`. |")
    elif s.startswith("| ↳ app_promotion_type | string | App promotion type"):
        new_lines.append("| ↳ app_promotion_type | string | Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác người dùng ứng dụng hiện tại để thực hiện hành động. • `MINIS`: TikTok Mini hoặc Series. Quảng bá Series, phim ngắn nhiều tập hoặc mini game bằng cách tối ưu hóa lưu lượng tự nhiên và quảng cáo. |")
    elif s.startswith("| ↳ campaign_type | string | Campaign Type"):
        new_lines.append("| ↳ campaign_type | string | Loại chiến dịch. ⏎ Hiện tại hỗ trợ `REGULAR_CAMPAIGN` và `IOS14_CAMPAIGN`. |")
    elif s.startswith("| ↳ app_id | string | The App ID"):
        new_lines.append("| ↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |")
    elif s.startswith("| ↳ campaign_name | string | Campaign name."):
        new_lines.append("| ↳ campaign_name | string | Tên chiến dịch. |")
    elif s.startswith("| ↳ budget_mode | string | Budget mode"):
        new_lines.append("| ↳ budget_mode | string | Chế độ ngân sách. ⏎ • Khi `budget_optimize_on` là `true` hoặc không chỉ định, các giá trị enum gồm: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • Khi `budget_optimize_on` là `false`, các giá trị enum gồm: • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách. |")
    elif s == "> add your content":
        continue
    elif s == "This endpoint supports incremental updates.":
        new_lines.append("Endpoint này hỗ trợ cập nhật tăng dần (incremental updates).")
    elif s.startswith("| budget | float | Fixed campaign budget"):
        new_lines.append("| budget | float | Ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. |")
    elif s == "Use this endpoint to enable, pause, or delete Upgraded Smart+ Campaigns.":
        new_lines.append("Sử dụng endpoint này để bật, tạm dừng hoặc xóa các Chiến dịch Smart+ nâng cấp.")
    elif s.startswith("| ↳ campaign_list | object[] | A list of campaigns"):
        new_lines.append("| ↳ campaign_list | object[] | Danh sách các chiến dịch mà thao tác được thực hiện thành công. |")
    elif s.startswith("| ↳↳ campaign_id | string | The ID of the campaign for which the operation was successful"):
        new_lines.append("| ↳↳ campaign_id | string | ID của chiến dịch mà thao tác được thực hiện thành công. |")
    elif s.startswith("| ↳ error_list | object[] | A list of errors"):
        new_lines.append("| ↳ error_list | object[] | Danh sách các lỗi và các chiến dịch thất bại tương ứng. |")
    elif s.startswith("| ↳↳ campaign_id | string | The ID of the campaign for which the operation failed"):
        new_lines.append("| ↳↳ campaign_id | string | ID của chiến dịch mà thao tác thất bại. |")
    elif s.startswith("| ↳↳ error_message | string | The error message associated with the failed campaign"):
        new_lines.append("| ↳↳ error_message | string | Thông báo lỗi liên quan đến chiến dịch thất bại. |")
    elif s.startswith("You can only copy one campaign at a time. To learn about the detailed steps, see [Copy an Upgraded Smart+ Campaign]"):
        new_lines.append("Bạn chỉ có thể sao chép một chiến dịch tại một thời điểm. Để tìm hiểu các bước chi tiết, xem [Sao chép chiến dịch Smart+ nâng cấp](../huong-dan/use-case-tao-chien-dich-p2.md#doc-1866530635467777).")
    elif s.startswith("> - The rate limits for this endpoint are 1 query per second (QPS) and 30 queries per minute (QPM) per app ID."):
        new_lines.append("> - Giới hạn tần suất cho endpoint này là 1 truy vấn mỗi giây (QPS) và 30 truy vấn mỗi phút (QPM) trên mỗi App ID.")
    elif s.startswith("|budget|number|The budget for the new campaign"):
        new_lines.append("|budget|number|Ngân sách cho chiến dịch mới hoặc giới hạn ngân sách cho tất cả các nhóm quảng cáo trong chiến dịch mới.<br><br>Để biết các quy tắc thiết lập trường này, xem [Ngân sách chiến dịch](../huong-dan/quan-ly-chien-dich-p1.md#doc-1745292231199745).|")
    elif s.startswith("|dayparting|string|<ul><li>Specify this field only when you want to set the same ad delivery arrangement"):
        new_lines.append("|dayparting|string|Phân bổ thời gian phân phối quảng cáo theo khung giờ cho tất cả các nhóm quảng cáo trong chiến dịch mới, định dạng chuỗi gồm 48 x 7 ký tự.<br><br>Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian.|")
    elif s.startswith("##|excluded_audience_ids|string[]|A list of audience IDs to be excluded"):
        new_lines.append("##|excluded_audience_ids|string[]|Danh sách ID đối tượng cần loại trừ.<br><br>Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739343403234305).|")
    elif s.startswith("##|audience_ids|string[]|A list of audience IDs.<br><br>To get audience IDs"):
        new_lines.append("##|audience_ids|string[]|Danh sách ID đối tượng.<br><br>Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739343403234305).|")
    elif s.startswith("##|creative_list|object[]|A list of creatives"):
        new_lines.append("##|creative_list|object[]|Danh sách các mẫu quảng cáo. Khoảng kích thước: 1-50.<br><br><p><span style=\"color:darkred\"><b>Lưu ý</b></span>: Khi bạn cung cấp trường này, các mẫu quảng cáo trong nhóm quảng cáo mới sẽ bị ghi đè hoàn toàn.|")
    elif s.startswith("####|video_info {+Conditional}|object|Required for Spark Ads"):
        new_lines.append("####|video_info {+Conditional}|object|Bắt buộc đối với quảng cáo Spark Ads Video đơn thông qua Spark Ads Push hoặc quảng cáo Video không phải Spark Ads.<br><br>Chi tiết về video.|")
    elif s.startswith("####|image_info {+Conditional}|object[]|<ul><li>Required for the following types of ads"):
        new_lines.append("####|image_info {+Conditional}|object[]|Bắt buộc đối với các loại quảng cáo Carousel (Spark Ads Standard Carousel hoặc Standard Carousel thông thường).<br><br>Chi tiết về hình ảnh.|")
    elif s.startswith("####|music_info {+Conditional}|object|Required for the following scenarios"):
        new_lines.append("####|music_info {+Conditional}|object|Bắt buộc khi tạo quảng cáo Standard Carousel thông thường sử dụng âm nhạc.<br><br>Chi tiết về âm nhạc.|")
    else:
        new_lines.append(l)

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines) + "\n")

print("Completed clean_remaining_62_p1.py")
