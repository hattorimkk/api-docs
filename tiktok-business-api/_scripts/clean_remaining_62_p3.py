import re

path = "tiktok-business-api/docs/api-reference/62-upgraded-smartplus-p3.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

new_lines = []
for l in lines:
    s = l.strip()
    if s.startswith("| identity_id | string | Valid only in any of the following scenarios"):
        new_lines.append("| identity_id | string | Chỉ hợp lệ trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ ID danh tính (Identity ID). |")
    elif s.startswith("| value_rule_set_id | string | ID of the value rule set"):
        new_lines.append("| value_rule_set_id | string | ID của bộ quy tắc giá trị liên kết với nhóm quảng cáo. ⏎ Quy tắc giá trị cho phép bạn ưu tiên và đặt giá thầu cao hơn cho một số loại khách hàng hoặc đối tượng dựa trên các điều kiện bạn xác định. |")
    elif s.startswith("| ↳ excluded_audience_ids | string[] | A list of audience IDs"):
        new_lines.append("| ↳ excluded_audience_ids | string[] | Danh sách ID đối tượng cần loại trừ. ⏎ Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739343403234305). |")
    elif s.startswith("| ↳ audience_ids | string[] | A list of audience IDs"):
        new_lines.append("| ↳ audience_ids | string[] | Danh sách ID đối tượng. ⏎ Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739343403234305). |")
    elif s.startswith("| ↳ included_pangle_audience_package_ids | string[] | Valid only for Pangle"):
        new_lines.append("| ↳ included_pangle_audience_package_ids | string[] | Chỉ hợp lệ cho vị trí hiển thị Pangle. Không chỉ định trường này cho các vị trí khác. ⏎ Danh sách ID gói đối tượng Pangle bạn muốn bao gồm. |")
    elif s.startswith("| ↳ excluded_pangle_audience_package_ids | string[] | Valid only for Pangle"):
        new_lines.append("| ↳ excluded_pangle_audience_package_ids | string[] | Chỉ hợp lệ cho vị trí hiển thị Pangle. Không chỉ định trường này cho các vị trí khác. ⏎ Danh sách ID gói đối tượng Pangle bạn muốn loại trừ. |")
    elif s.startswith("| ↳ interest_category_ids | string[] | IDs of general interest"):
        new_lines.append("| ↳ interest_category_ids | string[] | Danh sách ID từ khóa sở thích chung bạn muốn dùng để nhắm mục tiêu đối tượng. |")
    elif s.startswith("| ↳ purchase_intention_keyword_ids | string[] | IDs of purchase intention"):
        new_lines.append("| ↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm bạn muốn dùng để nhắm mục tiêu đối tượng quan tâm đến việc mua hàng liên quan đến một danh mục nội dung. |")
    elif s.startswith("| ↳↳ video_user_actions | string[] | The specific user interactions"):
        new_lines.append("| ↳↳ video_user_actions | string[] | Các tương tác cụ thể của người dùng bạn muốn nhắm mục tiêu cho loại hành vi tương ứng. • Nếu `action_scene` là `VIDEO_RELATED`, các giá trị được phép là: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`. • Nếu `action_scene` là `CREATOR_RELATED`, các giá trị được phép là: `FOLLOWING`, `VIEW_HOMEPAGE`. • Nếu `action_scene` là `HASHTAG_RELATED`, giá trị được phép là: `VIEW_HASHTAG`. |")
    elif s.startswith("| ↳ device_model_ids | string[] | List of device model IDs"):
        new_lines.append("| ↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị. ⏎ Để lấy danh sách đầy đủ ID mẫu thiết bị và thương hiệu thiết bị, sử dụng endpoint [/tool/device_model/](70-tools-p1.md#doc-1737189745795074). |")
    elif s.startswith("| ↳ device_price_ranges | number[] | Targeting device price range"):
        new_lines.append("| ↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu. ⏎ Giá trị 10000 đại diện cho 1000+. Các số phải là bội số của 50. ⏎ **Quan trọng**: Giới hạn trên bạn đặt sẽ được cộng thêm 50 và số mới thu được sẽ được sử dụng làm giới hạn trên thực tế cho nhắm mục tiêu thiết bị. Giới hạn thực tế được hiển thị trong cài đặt nhóm quảng cáo trên Trình quản lý quảng cáo TikTok. Nếu bạn đặt và nhận khoảng giá [0, 250], điều đó thực tế có nghĩa là [0, 300]. |")
    elif s.startswith("| ↳ blocked_pangle_app_ids | string[] | Pangle app block ID list"):
        new_lines.append("| ↳ blocked_pangle_app_ids | string[] | Danh sách ID ứng dụng Pangle bị chặn. ⏎ Bạn có thể lấy ID qua trường `app_package_id` trả về từ [/tool/pangle_app/block/get/](slug:get-pangle-app-blocklist). |")
    elif s.startswith("| movie_premiere_date | string | Valid when the following conditions"):
        new_lines.append("| movie_premiere_date | string | Hợp lệ khi thỏa mãn tất cả các điều kiện: • Ở cấp chiến dịch: `objective_type` là `WEB_CONVERSIONS`, `sales_destination` là `WEBSITE`. • Ở cấp nhóm quảng cáo: `optimization_goal` là `CONVERT`, `CLICK` hoặc `TRAFFIC_LANDING_PAGE_VIEW`. ⏎ Ngày công chiếu tại rạp, theo định dạng `YYYY-MM-DD` (UTC+0). ⏎ Cung cấp ngày công chiếu cho phép hệ thống tích hợp mốc thời gian này để tối ưu hóa hiệu suất. |")
    elif s.startswith("| dayparting | string | Ad delivery arrangement"):
        new_lines.append("| dayparting | string | Phân bổ thời gian phân phối quảng cáo theo khung giờ, định dạng chuỗi gồm 48 x 7 ký tự. ⏎ Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Ký tự đầu tiên tương ứng 0:01-0:30 Thứ Hai; ký tự cuối cùng tương ứng 23:31-0:00 Chủ Nhật. ⏎ **Lưu ý**: Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian. |")
    elif s.startswith("| ↳ optimization_locations | object[] | Returned when `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION`"):
        new_lines.append("| ↳ optimization_locations | object[] | Được trả về khi `promotion_type` là `LEAD_GENERATION_MULTI_DESTINATION`. ⏎ Danh sách các vị trí tối ưu hóa cho nhóm quảng cáo Tìm kiếm khách hàng tiềm năng. ⏎ Để tìm hiểu loại quảng cáo có thể sử dụng trường này, xem [Tạo chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng nâng cấp với nhiều vị trí đích](slug:create-an-upgraded-smart-lead-generation-campaign-with-multiple-location-selection). |")
    elif s.startswith("| ↳ custom_conversion_id | string | The ID of the Custom Conversion"):
        new_lines.append("| ↳ custom_conversion_id | string | ID của Chuyển đổi tùy chỉnh (Custom Conversion) được sử dụng trong nhóm quảng cáo. |")
    elif s.startswith("| ↳ deep_funnel_event_source_id | string | Returned when `deep_funnel_optimization_status` is `ON`"):
        new_lines.append("| ↳ deep_funnel_event_source_id | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ ID nguồn sự kiện. • Khi `deep_funnel_event_source` là `PIXEL`, trường này đại diện cho ID TikTok Pixel. • Khi `deep_funnel_event_source` là `OFFLINE`, trường này đại diện cho ID bộ sự kiện ngoại tuyến. • Khi `deep_funnel_event_source` là `CRM`, trường này đại diện cho ID bộ sự kiện CRM. |")
    elif s.startswith("| ↳ deep_funnel_optimization_event | string | Returned when `deep_funnel_optimization_status` is `ON`"):
        new_lines.append("| ↳ deep_funnel_optimization_event | string | Được trả về khi `deep_funnel_optimization_status` là `ON`. ⏎ Sự kiện tối ưu hóa phễu sâu. ⏎ Ví dụ: `SHOPPING`. |")
    elif s.startswith("| ↳ identity_id | string | Returned only in any of the following scenarios"):
        new_lines.append("| ↳ identity_id | string | Chỉ được trả về trong các trường hợp: • Trường hợp 1: Khi `promotion_type` là `NATIVE_SERIES`. • Trường hợp 2: Khi `promotion_type` là `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` và tài khoản quảng cáo của bạn nằm trong danh sách cho phép chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo Tin nhắn trực tiếp TikTok. ⏎ ID danh tính (Identity ID). |")
    elif s.startswith("| ↳ identity_authorized_bc_id | string | Returned when `identity_type` is `BC_AUTH_TT`"):
        new_lines.append("| ↳ identity_authorized_bc_id | string | Được trả về khi `identity_type` là `BC_AUTH_TT`. ⏎ ID của Trung tâm doanh nghiệp (Business Center) liên kết với danh tính người dùng tài khoản TikTok trong Business Center. |")
    elif s.startswith("| ↳ native_series_id | string | The ID of a TikTok Series"):
        new_lines.append("| ↳ native_series_id | string | ID của TikTok Series. ⏎ Series cung cấp các gói video độc quyền và cao cấp do các nhà sáng tạo nội dung sản xuất. Quyền truy cập Series có thể được mua qua hồ sơ của nhà sáng tạo và các liên kết gắn kèm trên video TikTok. |")
    elif s.startswith("| ↳ messaging_app_account_id | string | The ID of the instant messaging app account"):
        new_lines.append("| ↳ messaging_app_account_id | string | ID tài khoản ứng dụng nhắn tin tức thì. • Khi `messaging_app_type` là `MESSENGER`, trường này đại diện cho Facebook Page ID. • Khi `messaging_app_type` là `LINE`, trường này đại diện cho LINE Business ID. • Khi `zalo_id_type` là `ZALO_OFFICIAL_ACCOUNT`, trường này đại diện cho ID Zalo Official Account. • Khi `messaging_app_type` là `WHATSAPP` hoặc khi `zalo_id_type` là `ZALO_PHONE_ACCOUNT`, trường này đại diện cho số điện thoại WhatsApp hoặc Zalo được tự động điền dựa trên `phone_info` đã chỉ định. |")
    elif s.startswith("| ↳ message_event_set_id | string | The ID of the message event set"):
        new_lines.append("| ↳ message_event_set_id | string | ID của bộ sự kiện tin nhắn dùng trong Nhóm quảng cáo Tin nhắn tức thì. ⏎ Nếu tài khoản ứng dụng tin nhắn (tài khoản Messenger hoặc Zalo Official Account chỉ định qua `messaging_app_account_id`, hoặc số điện thoại WhatsApp/Zalo từ `phone_info`) khớp với bộ sự kiện hiện có, trường này sẽ được **tự động điền** bộ sự kiện tin nhắn duy nhất tương ứng. |")
    elif s.startswith("| ↳ phone_info | object | Details of WhatsApp or Zalo"):
        new_lines.append("| ↳ phone_info | object | Chi tiết số điện thoại WhatsApp hoặc Zalo. |")
    elif s.startswith("| ↳↳ phone_region_code | string | The region code for WhatsApp"):
        new_lines.append("| ↳↳ phone_region_code | string | Mã vùng quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `US`. |")
    elif s.startswith("| ↳↳ phone_region_calling_code | string | The region calling code"):
        new_lines.append("| ↳↳ phone_region_calling_code | string | Mã quay số quốc gia của số điện thoại WhatsApp hoặc Zalo. ⏎ Ví dụ: `+1`. |")
    elif s.startswith("| ↳↳ phone_number | string | The WhatsApp or Zalo"):
        new_lines.append("| ↳↳ phone_number | string | Số điện thoại WhatsApp hoặc Zalo. |")
    elif s.startswith("| ↳ bid_type | string | Bidding strategy"):
        new_lines.append("| ↳ bid_type | string | Chiến lược giá thầu. ⏎ Để xem các giá trị enum và mô tả, xem [Enumeration - Bidding Strategy](../phu-luc/phu-luc-p1.md#doc-1737174886619138). |")
    elif s.startswith("| ↳ bid_price | float | The target cost per click"):
        new_lines.append("| ↳ bid_price | float | Chi phí mục tiêu trên mỗi lượt nhấp. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |")
    elif s.startswith("| ↳ conversion_bid_price | float | The target cost per conversion"):
        new_lines.append("| ↳ conversion_bid_price | float | Chi phí mục tiêu trên mỗi chuyển đổi hoặc chi phí trên mỗi lượt xem trang đích. Hệ thống sẽ hướng tới đạt nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn số tiền đã chỉ định. |")
    elif s.startswith("| ↳ dayparting | string | Ad delivery arrangement"):
        new_lines.append("| ↳ dayparting | string | Phân bổ thời gian phân phối quảng cáo theo khung giờ, định dạng chuỗi gồm 48 x 7 ký tự. ⏎ Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Ký tự đầu tiên tương ứng 0:01-0:30 Thứ Hai; ký tự cuối cùng tương ứng 23:31-0:00 Chủ Nhật. ⏎ **Lưu ý**: Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian. |")
    elif s.startswith("| ↳ targeting_optimization_mode | string | Audience targeting optimization mode"):
        new_lines.append("| ↳ targeting_optimization_mode | string | Chế độ tối ưu hóa nhắm mục tiêu đối tượng. • `MANUAL`: Nhắm mục tiêu tùy chỉnh. Bạn có thể sử dụng cài đặt tùy chỉnh để kiểm soát chính xác ai nhìn thấy quảng cáo. Điều này có thể hạn chế phân phối và ảnh hưởng hiệu suất. • `AUTOMATIC`: Nhắm mục tiêu tự động. Sử dụng dữ liệu thời gian thực và máy học để tiếp cận đối tượng có khả năng tương tác cao nhất. |")
    elif s.startswith("| ↳↳ languages | string[] | Codes of the languages"):
        new_lines.append("| ↳↳ languages | string[] | Mã ngôn ngữ bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách mã ngôn ngữ được hỗ trợ, xem [Enumeration - Language Code](../phu-luc/phu-luc-p1.md#doc-1737174886619138). |")
    elif s.startswith("| ↳↳↳ days | integer | The time range used to filter out the audiences that completed"):
        new_lines.append("| ↳↳↳ days | integer | Khoảng thời gian (số ngày) dùng để lọc loại trừ các đối tượng đã hoàn thành hành động được chỉ định. |")
    elif s.startswith("| ↳↳ device_price_ranges | number[] | Targeting device price range"):
        new_lines.append("| ↳↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu. 10000 nghĩa là 1000+. Các số phải là bội số của 50. ⏎ **Quan trọng**: Giới hạn trên bạn đặt sẽ được cộng thêm 50 và số mới thu được sẽ được sử dụng làm giới hạn trên thực tế cho nhắm mục tiêu thiết bị. Giới hạn trên thực tế được hiển thị trong cài đặt nhóm quảng cáo trên Trình quản lý quảng cáo TikTok. Nếu bạn đặt và nhận khoảng giá [0, 250], điều đó thực tế có nghĩa là [0, 300]. |")
    else:
        new_lines.append(l)

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines) + "\n")

print("Finished clean_remaining_62_p3.py")
