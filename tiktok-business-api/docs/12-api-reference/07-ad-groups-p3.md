# Nhóm quảng cáo (Ad Groups) — phần 3/3

Tài liệu này cung cấp hướng dẫn chi tiết và đặc tả kỹ thuật cho các API cập nhật Nhóm quảng cáo (Ad Groups) trong TikTok for Business API v1.3 — Phần 3/3.

Phần này bao gồm các endpoint cho phép cập nhật cài đặt nhóm quảng cáo, thay đổi trạng thái hoạt động (bật, tắt, xóa) hàng loạt, và điều chỉnh ngân sách (ngân sách trọn đời hoặc đặt lịch thay đổi ngân sách hàng ngày).

## Danh sách các endpoint (Phần 3)

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `POST` | `/open_api/v1.3/adgroup/update/` | Cập nhật thông tin chi tiết của nhóm quảng cáo |
| `POST` | `/open_api/v1.3/adgroup/status/update/` | Cập nhật trạng thái hoạt động (bật, tắt, xóa) của các nhóm quảng cáo |
| `POST` | `/open_api/v1.3/adgroup/budget/update/` | Cập nhật ngân sách trọn đời hoặc lên lịch điều chỉnh ngân sách hàng ngày |

---

## Cập nhật nhóm quảng cáo (`Update an ad group`)
<a id="doc-1739586761631745"></a>
<!-- doc_id: 1739586761631745 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/adgroup/update/`

**Mục đích**: Sử dụng endpoint này để cập nhật cài đặt của một nhóm quảng cáo. Lưu ý không phải tất cả thông tin đều có thể sửa đổi (ví dụ: **vị trí phân phối - placement** không thể thay đổi sau khi tạo).

> [!IMPORTANT]
> Chế độ cập nhật của endpoint này là **thay thế toàn bộ (full replacement)**, không phải cập nhật gia tăng (incremental update). Ngay cả khi bạn chỉ muốn cập nhật một trường dữ liệu, bạn vẫn cần chỉ định tất cả các trường dữ liệu bắt buộc.

> [!NOTE]
> Nếu bạn đã chỉ định danh mục quảng cáo đặc biệt (`special_industries`) ở cấp chiến dịch, hãy đảm bảo rằng các nhóm quảng cáo trong chiến dịch tuân thủ các yêu cầu nhắm mục tiêu nêu tại [Yêu cầu nhắm mục tiêu cho nhóm quảng cáo có danh mục đặc biệt](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| adgroup_id | string | Bắt buộc | ID nhóm quảng cáo cần cập nhật. |
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| adgroup_name | string | Không bắt buộc | Tên nhóm quảng cáo. Tối đa 512 ký tự, không chứa emoji. |
| catalog_authorized_bc_id | string | Có điều kiện | Đối với danh mục trong Business Center, chỉ định ID Business Center sở hữu danh mục.<br>**Lưu ý**: Khi `product_source` là `STORE`, trường này sẽ bị bỏ qua. |
| deep_funnel_optimization_status | string | Không bắt buộc | Chỉ hợp lệ khi `promotion_type` là `LEAD_GENERATION`.<br>Trạng thái tối ưu hóa phễu chuyên sâu (tối ưu hóa đồng thời sự kiện đầu phễu và sự kiện sâu hơn):<br>• `ON`: Bật tối ưu hóa phễu chuyên sâu.<br>• `OFF`: Tắt tối ưu hóa phễu chuyên sâu (mặc định).<br>Xem thêm tại [Quảng cáo Tìm kiếm khách hàng tiềm năng với Biểu mẫu tức thì](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482920012801) và [với Trang web](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482976097281). |
| deep_funnel_event_source | string | Có điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`.<br>Loại nguồn sự kiện: `PIXEL` (Pixel), `OFFLINE` (Bộ sự kiện ngoại tuyến), `CRM` (Bộ sự kiện CRM - cần allowlist).<br>**Lưu ý**: Khi đã bật tối ưu hóa phễu chuyên sâu, bạn không thể cập nhật `deep_funnel_event_source`, `deep_funnel_event_source_id`, và `deep_funnel_optimization_event`. |
| deep_funnel_event_source_id | string | Có điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`.<br>ID nguồn sự kiện (Pixel ID, Offline Event Set ID, hoặc CRM Event Set ID). Tra cứu danh sách qua [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978), [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313), [/crm/list/](43-events-1-0-p2.md#doc-1780896521680898). |
| deep_funnel_optimization_event | string | Có điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`.<br>Tên sự kiện tối ưu hóa phễu chuyên sâu (ví dụ: `SHOPPING`). Xem [Sự kiện Pixel được hỗ trợ](../09-marketing-api/do-luong-quang-cao-p2.md#doc-1739585696931842). |
| comment_disabled | boolean | Không bắt buộc | Có tắt tính năng bình luận trên quảng cáo thuộc nhóm hay không: `true`, `false`. |
| share_disabled | boolean | Không bắt buộc | Có tắt tính năng chia sẻ quảng cáo sang nền tảng bên thứ ba hay không: `true`, `false`. Hỗ trợ cập nhật gia tăng. |
| blocked_pangle_app_ids | string[] | Không bắt buộc | ID danh sách chặn ứng dụng Pangle. Lấy qua endpoint [Lấy danh sách chặn Pangle](55-pangle.md#doc-1740039957181441). Chỉ có hiệu lực khi chọn vị trí Pangle. |
| search_result_enabled | boolean | Không bắt buộc | Có đưa quảng cáo vào kết quả Tìm kiếm (Search Ads) trên TikTok hay không (chuyển từ `false` sang `true`). Xem [Vị trí tìm kiếm tự động](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1771747626094593). |
| automated_keywords_enabled | boolean | Không bắt buộc | Chỉ hợp lệ khi `is_search_campaign` ở cấp chiến dịch là `true`. Có bật từ khóa tự động hay không: `true`, `false` (mặc định: `false`). Cần allowlist. |
| search_keywords | object[] | Không bắt buộc | Danh sách từ khóa tìm kiếm cho Chiến dịch quảng cáo tìm kiếm (Search Ads Campaign). Tối đa 1.000 từ khóa. Xem [Tạo Chiến dịch quảng cáo tìm kiếm](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1815394136739841).<br>**Lưu ý**: Khi cập nhật từ khóa hoặc vị trí nhắm mục tiêu, từ khóa sẽ được xét duyệt lại. |
| ↳ keyword | string | Có điều kiện | Bắt buộc khi truyền `search_keywords`. Từ khóa tìm kiếm (tối đa 80 ký tự, không chứa emoji hoặc ký tự đặc biệt). Phải tuân thủ [Điều khoản quảng cáo TikTok](https://ads.tiktok.com/help/article/advertising-on-tiktok-first-things-to-note). |
| ↳ match_type | string | Có điều kiện | Bắt buộc khi truyền `search_keywords`. Loại khớp từ khóa: `PRECISE_WORD` (khớp chính xác), `PHRASE_WORD` (khớp cụm từ), `BROAD_WORD` (khớp mở rộng). |
| ↳ keyword_bid_type | string | Không bắt buộc | Loại giá thầu từ khóa: `FOLLOW_ADGROUP` (mặc định - theo nhóm quảng cáo), `CUSTOM` (giá thầu tùy chỉnh). |
| ↳ keyword_bid | float | Có điều kiện | Bắt buộc khi `keyword_bid_type` là `CUSTOM`. Mức giá thầu tùy chỉnh (> 0). |
| audience_type | string | Có điều kiện | Bắt buộc khi `app_promotion_type` là `APP_RETARGETING` ở cấp chiến dịch. Loại đối tượng nhắm lại ứng dụng: `NEW_CUSTOM_AUDIENCE`. |
| audience_rule | object | Không bắt buộc | Quy tắc xác định tệp đối tượng (hợp lệ cho `TRAFFIC` hoặc `APP_PROMOTION`). Xem [Quy tắc đối tượng](../09-marketing-api/audience.md#doc-1739566532187138). |
| saved_audience_id | string | Không bắt buộc | ID tệp đối tượng đã lưu (Saved Audience ID). Xem [Tạo đối tượng đã lưu](../09-marketing-api/audience.md#doc-1780156510696449). |
| auto_targeting_enabled {-To be deprecated} | boolean | Không bắt buộc | *(Sắp ngừng hỗ trợ)* Có bật nhắm mục tiêu tự động hay không. Khuyến nghị chuyển sang [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| shopping_ads_retargeting_type | string | Không bắt buộc | Áp dụng khi `shopping_ads_type` là `VIDEO` và `product_source` là `CATALOG`.<br>Loại nhắm mục tiêu lại: `LAB1`, `LAB2`, `LAB3`, `OFF`, `RTA_RETARGETING`. |
| shopping_ads_retargeting_actions_days | number | Có điều kiện | Bắt buộc khi `shopping_ads_retargeting_type` là `LAB1` hoặc `LAB2`. Khoảng thời gian thực hiện hành vi: 1, 2, 3, 7, 14, 30, 60, 90, 180 ngày. |
| included_custom_actions | object[] | Có điều kiện | Điều kiện "Bao gồm" khi `shopping_ads_retargeting_type` là `LAB3`. |
| ↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳ days | integer | Khoảng thời gian thực hiện (1–180 ngày). |
| excluded_custom_actions | object[] | Có điều kiện | Điều kiện "Loại trừ" khi `shopping_ads_retargeting_type` là `LAB3`. |
| ↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳ days | integer | Khoảng thời gian không thực hiện (1–180 ngày). |
| shopping_ads_retargeting_custom_audience_relation | string | Quan hệ logic giữa đối tượng nhắm lại VSA và tệp đối tượng tùy chỉnh (`audience_ids`): `OR`, `AND`. |
| location_ids | string[] | Không bắt buộc | Danh sách ID vị trí địa lý nhắm mục tiêu (tối đa 3.000 phần tử kết hợp cùng mã bưu chính). Xem **Location IDs**. |
| zipcode_ids | string[] | Không bắt buộc | Danh sách mã bưu chính nhắm mục tiêu (hỗ trợ US, Canada, Brazil, Indonesia, Thái Lan, Việt Nam). Hỗ trợ cập nhật gia tăng. |
| languages | string[] | Không bắt buộc | Danh sách mã ngôn ngữ nhắm mục tiêu. Xem [Enum - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| gender | string | Không bắt buộc | Giới tính nhắm mục tiêu: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| age_groups | string[] | Không bắt buộc | Nhóm tuổi nhắm mục tiêu. Xem [Enum - Nhóm tuổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138) và [Hạn chế độ tuổi mới](../15-appendix/phu-luc-p1.md#doc-1788755983247362). |
| exclude_age_under_eighteen | boolean | Không bắt buộc | Có loại trừ người dùng dưới 18 tuổi hay không: `true`, `false` (mặc định: `false`). |
| spending_power | string | Không bắt buộc | Sức chi tiêu của người dùng: `ALL`, `HIGH` (chi tiêu cao). Không áp dụng cho `PRODUCT_SALES` và `RF_REACH`. |
| household_income | string[] | Không bắt buộc | Thu nhập hộ gia đình: `TOP5`, `TOP10`, `TOP10_25`, `TOP25_50` (chỉ áp dụng tại Mỹ cho vị trí TikTok). |
| audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng tùy chỉnh. Xem [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| smart_audience_enabled | boolean | Không bắt buộc | Có bật Đối tượng thông minh (Smart audience) hay không: `true`, `false`. Xem [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| excluded_audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng loại trừ. |
| interest_category_ids | string[] | Không bắt buộc | Danh sách ID danh mục sở thích chung. Tra cứu qua [/targeting/search/](70-tools-p1.md#doc-1796638342793218). |
| interest_keyword_ids | string[] | Không bắt buộc | Danh sách ID từ khóa sở thích bổ sung. Tra cứu qua [/targeting/search/](70-tools-p1.md#doc-1796638342793218). |
| purchase_intention_keyword_ids | string[] | Không bắt buộc | Danh sách ID danh mục ý định mua sắm. Hỗ trợ cập nhật gia tăng. |
| actions | object[] | Không bắt buộc | Danh sách đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳ action_scene | string | Không bắt buộc | Loại hành vi: `VIDEO_RELATED`, `CREATOR_RELATED`, `HASHTAG_RELATED`. |
| ↳ action_period | number | Không bắt buộc | Khung thời gian hành vi (ngày): `0`, `7`, `15`. |
| ↳ video_user_actions | string[] | Không bắt buộc | Hành vi cụ thể: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`, `FOLLOWING`, `VIEW_HOMEPAGE`, `VIEW_HASHTAG`. |
| ↳ action_category_ids | string[] | Không bắt buộc | Danh sách ID danh mục tương tác video, người sáng tạo hoặc hashtag. |
| smart_interest_behavior_enabled | boolean | Không bắt buộc | Có bật Sở thích & Hành vi thông minh (Smart interests & behaviors) hay không: `true`, `false`. |
| included_pangle_audience_package_ids | string[] | Không bắt buộc | Danh sách ID gói đối tượng Pangle bao gồm. |
| excluded_pangle_audience_package_ids | string[] | Không bắt buộc | Danh sách ID gói đối tượng Pangle loại trừ. |
| operating_systems | string[] | Có điều kiện | Hệ điều hành thiết bị: `ANDROID`, `IOS`. |
| min_android_version | string | Không bắt buộc | Phiên bản Android tối thiểu. Xem [Enum - Phiên bản Android](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ios14_targeting | string | Có điều kiện | Thiết bị iOS nhắm mục tiêu: `UNSET`, `IOS14_MINUS`, `IOS14_PLUS`, `ALL`. Bắt buộc là `IOS14_PLUS` cho Chiến dịch chuyên dụng iOS 14. |
| min_ios_version | string | Có điều kiện | Bắt buộc khi chỉ định `ios14_targeting`. Phiên bản iOS tối thiểu. Xem [Enum - Phiên bản iOS](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| device_model_ids | string[] | Không bắt buộc | Danh sách ID mẫu thiết bị nhắm mục tiêu. Xem [/tool/device_model/](70-tools-p1.md#doc-1737172880570369). |
| network_types | string[] | Không bắt buộc | Loại kết nối mạng thiết bị: `WIFI`, `2G`, `3G`, `4G`, `5G`. Xem [Enum - Loại kết nối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| carrier_ids | string[] | Không bắt buộc | Danh sách nhà mạng viễn thông. Xem [/tool/carrier/](70-tools-p1.md#doc-1737168013095938). |
| isp_ids | string[] | Không bắt buộc | Danh sách ID nhà cung cấp dịch vụ Internet (ISP). |
| device_price_ranges | number[] | Không bắt buộc | Khoảng giá thiết bị (bội số của 50). Ví dụ: `[0, 250]` thực tế là [0, 300]. |
| targeting_expansion {-To be deprecated} | object | Không bắt buộc | Cài đặt mở rộng nhắm mục tiêu. |
| ↳ expansion_enabled | boolean | Không bắt buộc | Có bật mở rộng nhắm mục tiêu hay không. |
| ↳ expansion_types | string[] | Có điều kiện | Các loại đối tượng muốn mở rộng: `AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `CUSTOM_AUDIENCE`. |
| contextual_tag_ids | string[] | Không bắt buộc | Danh sách ID thẻ ngữ cảnh (chỉ áp dụng cho mục tiêu `REACH` và `VIDEO_VIEWS`, cần allowlist). Xem [Nhắm mục tiêu ngữ cảnh](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292519923713). |
| brand_safety_type | string | Không bắt buộc | Loại an toàn thương hiệu: `EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`. Cần allowlist. Xem [An toàn thương hiệu](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505). |
| category_exclusion_ids | string[] | Không bắt buộc | Danh sách ID danh mục loại trừ nội dung. Lấy qua [/tool/content_exclusion/get/](70-tools-p2.md#doc-1769738074686465). |
| vertical_sensitivity_id | string | Không bắt buộc | ID danh mục nhạy cảm ngành dọc. Lấy qua [/tool/content_exclusion/get/](70-tools-p2.md#doc-1769738074686465). |
| budget | float | Không bắt buộc | Ngân sách quảng cáo. Không thể cập nhật khi bật CBO (`budget_optimize_on` = `true`). Ngân sách mới phải tối thiểu bằng 105% số tiền đã chi tiêu hiện tại (`spend`). Xem [Ngân sách](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). |
| schedule_type | string | Không bắt buộc | Loại lịch chạy: `SCHEDULE_START_END`, `SCHEDULE_FROM_NOW`. |
| schedule_start_time | datetime | Có điều kiện | Bắt buộc khi truyền `schedule_type`. Thời gian bắt đầu phân phối (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Không thể cập nhật nếu thời gian bắt đầu đã trôi qua. |
| schedule_end_time | datetime | Có điều kiện | Bắt buộc khi `schedule_type` là `SCHEDULE_START_END`. Thời gian kết thúc phân phối (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. |
| dayparting | string | Không bắt buộc | Chuỗi 336 ký tự (48 x 7) phân bổ khung giờ chạy quảng cáo 30 phút trong tuần. |
| frequency | number | Không bắt buộc | Tần suất hiển thị tối đa (chỉ áp dụng cho mục tiêu `REACH`). 1 ≤ `frequency` ≤ 1.000. |
| frequency_schedule | number | Không bắt buộc | Khoảng thời gian tính tần suất (ngày). 1 ≤ `frequency_schedule` ≤ 30. |
| secondary_optimization_event | string | Không bắt buộc | Mục tiêu thứ cấp khi `optimization_goal` là `INSTALL` hoặc `VALUE`. Cần truyền kèm `deep_bid_type`. Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| bid_type | string | Không bắt buộc | Chiến lược giá thầu. Xem [Enum - Chiến lược giá thầu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Không thể sửa khi bật CBO. |
| bid_price | float | Không bắt buộc | Giá thầu mục tiêu cho chiến lược Cost Cap (áp dụng khi `billing_event` là `CPC`, `CPM`, hoặc `CPV`). |
| conversion_bid_price | float | Không bắt buộc | Giá thầu mục tiêu CPA cho oCPM. |
| deep_bid_type | string | Có điều kiện | Chiến lược giá thầu cho sự kiện chuyên sâu trong ứng dụng. Xem [Enum - Chiến lược giá thầu chuyên sâu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| roas_bid | float | Có điều kiện | Bắt buộc khi `deep_bid_type` là `VO_MIN_ROAS`. Mục tiêu ROAS cho Tối ưu hóa giá trị. |
| deep_cpa_bid | float | Không bắt buộc | Mức giá thầu CPA chuyên sâu sau khi chọn chiến lược sự kiện trong ứng dụng (ví dụ: `VO_MIN`). |
| next_day_retention | float | Không bắt buộc | Tỷ lệ giữ chân ngày thứ 2: `conversion_bid_price` / `deep_cpa_bid`. Khoảng giá trị (0, 1]. |
| pacing | string | Không bắt buộc | Tốc độ phân phối ngân sách: `PACING_MODE_SMOOTH` (đều đặn), `PACING_MODE_FAST` (nhanh nhất có thể). |
| is_hfss | boolean | Không bắt buộc | Sản phẩm/thương hiệu HFSS (Nhiều chất béo, muối, đường): `true`, `false`. Chỉ có thể cập nhật từ `false` sang `true`. |
| is_lhf_compliance | boolean | Không bắt buộc | Tuân thủ quy định Thực phẩm kém lành mạnh (LHF) tại Vương quốc Anh: `true`, `false`. Bắt buộc đặt là `true` khi nhắm mục tiêu UK và `is_hfss` là `true`. |


### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu, định danh duy nhất cho một yêu cầu HTTP. |
| data | object | Dữ liệu nhóm quảng cáo sau khi cập nhật. |
| ↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳ campaign_id | string | ID của chiến dịch. |
| ↳ campaign_name | string | Tên chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳ create_time | string | Thời gian tạo nhóm quảng cáo (`YYYY-MM-DD HH:MM:SS`). |
| ↳ modify_time | string | Thời gian sửa đổi nhóm quảng cáo (`YYYY-MM-DD HH:MM:SS`). |
| ↳ shopping_ads_type | string | Loại quảng cáo mua sắm: `VIDEO`, `LIVE`, `PRODUCT_SHOPPING_ADS`, `CATALOG_LISTING_ADS`, `UNSET`. |
| ↳ identity_id | string | ID danh tính. |
| ↳ identity_type | string | Loại danh tính: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. Xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ identity_authorized_bc_id | string | ID Business Center liên kết khi `identity_type` là `BC_AUTH_TT`. |
| ↳ product_source | string | Nguồn sản phẩm: `UNSET`, `CATALOG`, `STORE`, `SHOWCASE`. |
| ↳ catalog_id | string | ID danh mục sản phẩm. |
| ↳ catalog_authorized_bc_id | string | ID Business Center sở hữu danh mục. |
| ↳ store_id | string | ID của TikTok Shop. |
| ↳ store_authorized_bc_id | string | ID Business Center được ủy quyền truy cập TikTok Shop. |
| ↳ promotion_type | string | Loại hình quảng bá (vị trí tối ưu hóa). Xem [Enum - Loại hình quảng bá](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ promotion_target_type | string | Loại đích quảng bá cho Lead Generation: `INSTANT_PAGE`, `EXTERNAL_WEBSITE`, `UNSET`. |
| ↳ messaging_app_type | string | Loại ứng dụng nhắn tin tức thì: `MESSENGER`, `WHATSAPP`, `ZALO`, `LINE`, `IM_URL`. |
| ↳ messaging_app_account_id | string | ID tài khoản ứng dụng nhắn tin. |
| ↳ phone_region_code | string | Mã vùng điện thoại WhatsApp hoặc Zalo (ví dụ: `US`). |
| ↳ phone_region_calling_code | string | Mã gọi quốc tế cho số điện thoại WhatsApp hoặc Zalo (ví dụ: `+1`). |
| ↳ phone_number | string | Số điện thoại WhatsApp hoặc Zalo. |
| ↳ promotion_website_type | string | Loại trang tức thì TikTok: `UNSET`, `TIKTOK_NATIVE_PAGE`. |
| ↳ app_id | string | ID ứng dụng được quảng bá. |
| ↳ app_type | string | Hệ điều hành ứng dụng: `APP_ANDROID`, `APP_IOS`. |
| ↳ app_download_url | string | Liên kết tải xuống ứng dụng. |
| ↳ pixel_id | string | Pixel ID (cho trang đích). |
| ↳ optimization_event | string | Sự kiện chuyển đổi của nhóm quảng cáo. Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳ custom_conversion_id | string | ID chuyển đổi tùy chỉnh. |
| ↳ app_config | object[] | Chi tiết ứng dụng được quảng bá khi `sales_destination` là `WEB_AND_APP`. |
| ↳↳ app_id | string | ID ứng dụng được quảng bá. |
| ↳ deep_funnel_optimization_status | string | Trạng thái tối ưu hóa phễu chuyên sâu: `ON`, `OFF`. |
| ↳ deep_funnel_event_source | string | Nguồn sự kiện tối ưu hóa phễu chuyên sâu: `PIXEL`, `OFFLINE`, `CRM`. |
| ↳ deep_funnel_event_source_id | string | ID nguồn sự kiện phễu chuyên sâu. |
| ↳ deep_funnel_optimization_event | string | Sự kiện tối ưu hóa phễu chuyên sâu (ví dụ: `SHOPPING`). |
| ↳ placement_type | string | Chiến lược vị trí phân phối: `PLACEMENT_TYPE_AUTOMATIC`, `PLACEMENT_TYPE_NORMAL`. |
| ↳ placements | string[] | Danh sách ứng dụng phân phối quảng cáo: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`. |
| ↳ tiktok_subplacements | string[] | Vị trí phân phối phụ trong TikTok: `IN_FEED`, `SEARCH_FEED`, `TIKTOK_LITE`, `LEMON8`. |
| ↳ search_result_enabled | boolean | Có đưa quảng cáo vào kết quả Tìm kiếm TikTok hay không: `true`, `false`. |
| ↳ automated_keywords_enabled | boolean | Có bật tự động tạo từ khóa tìm kiếm hay không: `true`, `false`. |
| ↳ search_keywords | object[] | Danh sách từ khóa tìm kiếm (chỉ áp dụng cho Search Ads Campaign). |
| ↳↳ keyword | string | Từ khóa tìm kiếm. |
| ↳↳ match_type | string | Loại khớp từ khóa: `PRECISE_WORD`, `PHRASE_WORD`, `BROAD_WORD`. |
| ↳↳ keyword_bid_type | string | Loại giá thầu từ khóa: `FOLLOW_ADGROUP`, `CUSTOM`. |
| ↳↳ keyword_bid | float | Mức giá thầu tùy chỉnh cho từ khóa. |
| ↳↳ audit_status | string | Trạng thái xét duyệt từ khóa: `AUDITING`, `PASS`, `REJECTED`. |
| ↳↳ reject_info | object[] | Chi tiết lý do từ chối từ khóa khi `audit_status` là `REJECTED`. |
| ↳↳↳ forbidden_location | string | Khu vực bị từ chối xét duyệt. Xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ reject_reasons | object[] | Danh sách lý do từ chối. |
| ↳↳↳↳ reason | string | Lý do từ chối chi tiết. |
| ↳ comment_disabled | boolean | Có tắt bình luận trên quảng cáo hay không: `true`, `false`. |
| ↳ video_download_disabled | boolean | Có tắt tải video quảng cáo hay không: `true`, `false`. |
| ↳ share_disabled | boolean | Có tắt chia sẻ quảng cáo hay không: `true`, `false`. |
| ↳ blocked_pangle_app_ids | string[] | Danh sách ID danh sách chặn ứng dụng Pangle. |
| ↳ audience_type | string | Loại tệp đối tượng nhắm lại ứng dụng. Xem [Enum - Loại đối tượng nhắm lại](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ audience_rule | object | Quy tắc xác định tệp đối tượng. Xem [Quy tắc đối tượng](../09-marketing-api/audience.md#doc-1739566532187138). |
| ↳ saved_audience_id | string | ID tệp đối tượng đã lưu (Saved Audience ID). |
| ↳ auto_targeting_enabled {-To be deprecated} | boolean | *(Sắp ngừng hỗ trợ)* Có bật nhắm mục tiêu tự động hay không. |
| ↳ shopping_ads_retargeting_type | string | Loại nhắm mục tiêu lại của quảng cáo mua sắm: `LAB1`, `LAB2`, `LAB3`, `OFF`, `RTA_RETARGETING`. |
| ↳ shopping_ads_retargeting_actions_days | number | Khoảng thời gian thực hiện hành vi: 1, 2, 3, 7, 14, 30, 60, 90, 180 ngày. |
| ↳ included_custom_actions | object[] | Hành vi tùy chỉnh làm điều kiện "Bao gồm" để nhắm lại. |
| ↳↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳↳ days | integer | Khoảng thời gian đã hoàn thành hành vi (1–180 ngày). |
| ↳ excluded_custom_actions | object[] | Hành vi tùy chỉnh làm điều kiện "Loại trừ" để nhắm lại. |
| ↳↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳↳ days | integer | Khoảng thời gian không thực hiện hành vi (1–180 ngày). |
| ↳ shopping_ads_retargeting_custom_audience_relation | string | Quan hệ logic giữa đối tượng nhắm lại VSA và tệp đối tượng tùy chỉnh (`audience_ids`): `OR`, `AND`. |
| ↳ location_ids | string[] | Danh sách ID vị trí địa lý nhắm mục tiêu. Xem [Lấy vị trí](70-tools-p1.md#doc-1737189539571713). |
| ↳ zipcode_ids | string[] | Danh sách mã bưu chính nhắm mục tiêu. |
| ↳ languages | string[] | Mã ngôn ngữ nhắm mục tiêu. Xem [Enum - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ gender | string | Giới tính nhắm mục tiêu: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳ age_groups | string[] | Nhóm tuổi nhắm mục tiêu. Xem [Enum - Nhóm tuổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ spending_power | string | Sức chi tiêu của người dùng: `ALL`, `HIGH`. |
| ↳ household_income | string[] | Thu nhập hộ gia đình: `TOP5`, `TOP10`, `TOP10_25`, `TOP25_50`. |
| ↳ audience_ids | string[] | Danh sách ID tệp đối tượng tùy chỉnh nhắm mục tiêu. |
| ↳ smart_audience_enabled | boolean | Có bật Đối tượng thông minh hay không: `true`, `false`. |
| ↳ excluded_audience_ids | string[] | Danh sách ID tệp đối tượng loại trừ. |
| ↳ interest_category_ids | string[] | Danh sách ID danh mục sở thích chung. |
| ↳ interest_keyword_ids | string[] | Danh sách ID từ khóa sở thích bổ sung. |
| ↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm. |
| ↳ actions | object[] | Danh sách đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳↳ action_scene | string | Loại hành vi: `VIDEO_RELATED`, `CREATOR_RELATED`, `HASHTAG_RELATED`. |
| ↳↳ action_period | number | Khung thời gian hành vi: `0`, `7`, `15` ngày. |
| ↳↳ video_user_actions | string[] | Hành vi tương tác cụ thể: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`, `FOLLOWING`, `VIEW_HOMEPAGE`, `VIEW_HASHTAG`. |
| ↳↳ action_category_ids | string[] | Danh sách ID danh mục tương tác video, người sáng tạo hoặc hashtag. |
| ↳ smart_interest_behavior_enabled | boolean | Có bật Sở thích & Hành vi thông minh hay không: `true`, `false`. |
| ↳ included_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle bao gồm. |
| ↳ excluded_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle loại trừ. |
| ↳ operating_systems | string[] | Hệ điều hành thiết bị nhắm mục tiêu: `ANDROID`, `IOS`. |
| ↳ min_android_version | string | Phiên bản Android tối thiểu. Xem [Enum - Phiên bản Android](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ ios14_targeting | string | Thiết bị iOS nhắm mục tiêu: `UNSET`, `IOS14_MINUS`, `IOS14_PLUS`, `ALL`. |
| ↳ min_ios_version | string | Phiên bản iOS tối thiểu. Xem [Enum - Phiên bản iOS](70-tools-p1.md#doc-1738308662898689). |
| ↳ ios14_quota_type | string | Có tính vào hạn mức iOS 14 hay không: `OCCUPIED`, `UNOCCUPIED`. |
| ↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị nhắm mục tiêu. Xem [Mẫu thiết bị](70-tools-p1.md#doc-1737172880570369). |
| ↳ network_types | string[] | Loại kết nối mạng: `WIFI`, `2G`, `3G`, `4G`, `5G`. Xem [Enum - Loại kết nối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ carrier_ids | string[] | Danh sách nhà mạng viễn thông. Xem [Nhà mạng](70-tools-p1.md#doc-1737168013095938). |
| ↳ isp_ids | string[] | Danh sách ID nhà cung cấp dịch vụ Internet (ISP). |
| ↳ device_price_ranges | number[] | Khoảng giá thiết bị (bội số của 50). |
| ↳ targeting_expansion {-To be deprecated} | object | Cài đặt mở rộng nhắm mục tiêu. |
| ↳↳ expansion_enabled | boolean | Có bật mở rộng nhắm mục tiêu hay không. |
| ↳↳ expansion_types | string[] | Các loại đối tượng muốn mở rộng: `AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `CUSTOM_AUDIENCE`. |
| ↳ contextual_tag_ids | string[] | Danh sách ID thẻ ngữ cảnh. |
| ↳ brand_safety_type | string | Loại an toàn thương hiệu: `NO_BRAND_SAFETY`, `EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`, `THIRD_PARTY`. |
| ↳ brand_safety_partner | string | Đối tác an toàn thương hiệu: `IAS`, `OPEN_SLATE` (DoubleVerify). |
| ↳ inventory_filter_enabled | boolean | Bộ lọc khoảng không quảng cáo an toàn: `true`, `false`. |
| ↳ category_exclusion_ids | string[] | Danh sách ID danh mục loại trừ nội dung. |
| ↳ vertical_sensitivity_id | string | ID danh mục nhạy cảm ngành dọc. |
| ↳ budget_mode | string | Chế độ ngân sách của nhóm quảng cáo. Xem [Ngân sách](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). |
| ↳ budget | float | Ngân sách nhóm quảng cáo. |
| ↳ scheduled_budget | float | Ngân sách lên lịch cho ngày hôm sau. |
| ↳ schedule_type | string | Loại lịch chạy: `SCHEDULE_START_END`, `SCHEDULE_FROM_NOW`. |
| ↳ schedule_start_time | datetime | Thời gian bắt đầu phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳ schedule_end_time | datetime | Thời gian kết thúc phân phối (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳ delivery_mode | string | Chiến lược phân phối nhóm R&F: `STANDARD`, `SCHEDULE`, `SEQUENCE`, `OPTIMIZE`. |
| ↳ dayparting | string | Chuỗi 336 ký tự phân bổ khung giờ chạy quảng cáo trong tuần. |
| ↳ optimization_goal | string | Mục tiêu tối ưu hóa. Xem [Enum - Mục tiêu tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ secondary_optimization_event | string | Mục tiêu thứ cấp khi `optimization_goal` là `INSTALL` hoặc `VALUE`. Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳ message_event_set_id | string | ID bộ sự kiện tin nhắn trong nhóm quảng cáo Tin nhắn tức thì. |
| ↳ frequency | number | Tần suất hiển thị tối đa (mục tiêu `REACH`). |
| ↳ frequency_schedule | number | Khoảng thời gian tính tần suất (ngày). |
| ↳ bid_type | string | Chiến lược giá thầu. Xem [Enum - Chiến lược giá thầu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ bid_price | float | Giá thầu mục tiêu cho Cost Cap. |
| ↳ conversion_bid_price | float | Giá thầu mục tiêu CPA cho oCPM. |
| ↳ deep_bid_type | string | Chiến lược giá thầu cho sự kiện chuyên sâu trong ứng dụng. Xem [Enum - Chiến lược giá thầu chuyên sâu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | Mục tiêu ROAS cho Tối ưu hóa giá trị. |
| ↳ vbo_window | string | Khung thời gian cho chiến lược tối ưu hóa giá trị: `SEVEN_DAYS`, `ZERO_DAY`. |
| ↳ bid_display_mode | string | Cách tính và đo lường Cost per View. |
| ↳ deep_cpa_bid | float | Mức giá thầu CPA chuyên sâu cho sự kiện trong ứng dụng. |
| ↳ cpv_video_duration | string | Thời lượng phát video tối ưu hóa: `SIX_SECONDS`, `TWO_SECONDS`. |
| ↳ next_day_retention | float | Tỷ lệ giữ chân ngày thứ 2: `conversion_bid_price` / `deep_cpa_bid`. |
| ↳ click_attribution_window | string | Khung thời gian phân bổ lượt nhấp: `OFF`, `ONE_DAY`, `SEVEN_DAYS`, `FOURTEEN_DAYS`, `TWENTY_EIGHT_DAYS`. |
| ↳ engaged_view_attribution_window | string | Khung thời gian phân bổ lượt xem tương tác: `ONE_DAY`, `SEVEN_DAYS`. |
| ↳ view_attribution_window | string | Khung thời gian phân bổ lượt xem: `OFF`, `ONE_DAY`, `SEVEN_DAYS`. |
| ↳ attribution_event_count | string | Cách tính đếm sự kiện phân bổ: `UNSET`, `EVERY`, `ONCE`. |
| ↳ billing_event | string | Sự kiện tính phí. Xem [Enum - Sự kiện tính phí](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ pacing | string | Tốc độ phân phối ngân sách: `PACING_MODE_SMOOTH`, `PACING_MODE_FAST`. |
| ↳ operation_status | string | Trạng thái hoạt động: `ENABLE`, `DISABLE`, `FROZEN`. |
| ↳ secondary_status | string | Trạng thái phụ của nhóm quảng cáo. Xem [Enum - Trạng thái nhóm quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ statistic_type | string | Loại thống kê giá thầu chuyển đổi: `EVERYTIME`, `NONE`. |
| ↳ is_hfss | boolean | Sản phẩm/thương hiệu HFSS: `true`, `false`. |
| ↳ is_lhf_compliance | boolean | Tuân thủ quy định Thực phẩm kém lành mạnh (LHF) tại Anh: `true`, `false`. |
| ↳ creative_material_mode | string | Chiến lược phân phối nội dung sáng tạo: `CUSTOM`, `DYNAMIC`, `SMART_CREATIVE`. |
| ↳ adgroup_app_profile_page_state | string | Nhóm quảng cáo có sử dụng Trang hồ sơ ứng dụng hay không: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳ feed_type | string | Loại bảng tin: `STANDARD_FEED`, `TOP_FEED`. |
| ↳ rf_purchased_type | string | Phương thức thanh toán Reach & Frequency (luôn là null với quảng cáo thông thường). |
| ↳ purchased_impression | number | Lượt hiển thị đã mua (luôn là null với quảng cáo thông thường). |
| ↳ purchased_reach | number | Lượng người dùng tiếp cận đã mua (luôn là null với quảng cáo thông thường). |
| ↳ rf_estimated_cpr | number | CPR ước tính cho nhóm R&F (luôn là null với quảng cáo thông thường). |
| ↳ rf_estimated_frequency | number | Tần suất hiển thị ước tính (luôn là null với quảng cáo thông thường). |
| ↳ is_new_structure | boolean | Nhóm quảng cáo có sử dụng cấu trúc mới hay không. |
| ↳ skip_learning_phase | boolean | Có bỏ qua giai đoạn học máy hay không. |
| ↳ conversion_window {-Deprecated} | string | *(Đã ngừng hỗ trợ)* Cửa sổ chuyển đổi để tối ưu hóa phân phối. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số nhóm quảng cáo thỏa mãn điều kiện. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/update/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "adgroup_id": "1765432109876599",
    "adgroup_name": "Summer_Traffic_AdGroup_Updated",
    "budget": 600.0
}'
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
ADGROUP_ID = "1765432109876599"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/update/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_id": ADGROUP_ID,
    "adgroup_name": "Summer_Traffic_AdGroup_Updated",
    "budget": 600.0
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1765432109876545",
    "campaign_name": "Summer_Promotion_2023",
    "adgroup_id": "1765432109876599",
    "adgroup_name": "Summer_Traffic_AdGroup_Updated",
    "create_time": "2023-05-22 10:05:00",
    "modify_time": "2023-05-22 11:30:00",
    "budget": 600.0,
    "budget_mode": "BUDGET_MODE_TOTAL",
    "operation_status": "ENABLE",
    "secondary_status": "ADGROUP_STATUS_ENABLE",
    "optimization_goal": "CLICK",
    "is_new_structure": true
  }
}
```


---

## Cập nhật trạng thái của các nhóm quảng cáo (Update the statuses of ad groups)
<a id="doc-1739591716326402"></a>
<!-- doc_id: 1739591716326402 -->

Sử dụng endpoint này để bật, tắt hoặc xóa một hoặc nhiều nhóm quảng cáo. Bạn có thể:
- Bật (`ENABLE`) nhóm quảng cáo để phân phối tới đối tượng mục tiêu theo kế hoạch phân phối cụ thể.
- Tắt (`DISABLE`) nhóm quảng cáo để tạm dừng phân phối.
- Xóa (`DELETE`) nhóm quảng cáo.

> **Lưu ý:**
> - Nhóm quảng cáo trong Dedicated Campaign (Chiến dịch Chuyên dụng) không thể bị xóa riêng lẻ. Để xóa nhóm quảng cáo đó, bạn cần phải xóa toàn bộ chiến dịch.
> - Trạng thái hoạt động (`operation_status`) của nhóm quảng cáo đã xóa hoặc nhóm quảng cáo thuộc chiến dịch đã xóa không thể sửa đổi. Bạn có thể sử dụng [/campaign/get/](24-campaign.md#doc-1739315828649986) hoặc [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922) để tra cứu trạng thái hoạt động của chiến dịch hoặc nhóm quảng cáo qua trường `operation_status`.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/adgroup/status/update/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập xác thực người dùng. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị cố định: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `adgroup_ids` **(Bắt buộc)** | string[] | Danh sách ID các nhóm quảng cáo cần thao tác. Độ dài mảng: 1–20 ID. |
| `operation_status` **(Bắt buộc)** | string | Thao tác cần thực hiện trên các nhóm quảng cáo.<br>Enum: `DISABLE` (tạm dừng), `ENABLE` (bật), `DELETE` (xóa).<br>**Lưu ý:**<br>• Không thể sửa đổi trạng thái của nhóm quảng cáo đã bị xóa hoặc nhóm quảng cáo thuộc chiến dịch đã xóa.<br>• Thao tác `ENABLE` và `DISABLE` không được hỗ trợ đối với nhóm quảng cáo Reach & Frequency (R&F). |
| `allow_partial_success` | boolean | Cho phép thao tác thành công một phần hay không.<br>Enum: `true`, `false`. Mặc định: `false`.<br>Nếu đặt là `true` khi thao tác trên nhiều nhóm quảng cáo, thao tác có thể thành công với một số nhóm đủ điều kiện; các nhóm không đủ điều kiện sẽ được lọc ra và trả về trong `error_list`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/status/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "adgroup_ids": [
      "1765432109876599"
    ],
    "operation_status": "DISABLE",
    "allow_partial_success": false
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/status/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "adgroup_ids": [
        "1765432109876599"
    ],
    "operation_status": "DISABLE",
    "allow_partial_success": False
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu kết quả phản hồi. |
| `↳ adgroup_ids` | string[] | Danh sách ID các nhóm quảng cáo đã áp dụng thao tác thành công. |
| `↳ status` | string | Trạng thái hiện tại của các nhóm quảng cáo đã thao tác thành công.<br>Enum: `DISABLE` (đã tạm dừng), `ENABLE` (đang bật), `DELETE` (đã xóa). |
| `↳ error_list` | object[] | Danh sách lỗi và các nhóm quảng cáo thất bại tương ứng. Chỉ trả về khi `allow_partial_success` được đặt thành `true`. |
| `↳↳ adgroup_id` | string | ID của nhóm quảng cáo có thao tác bị thất bại. |
| `↳↳ error_message` | string | Thông điệp lỗi chi tiết tương ứng với nhóm quảng cáo thất bại. |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu để theo dõi và đối soát. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020031110223101018904922300361F64",
  "data": {
    "status": "DISABLE",
    "adgroup_ids": [
      "1765432109876599"
    ]
  }
}
```

---

## Cập nhật ngân sách của các nhóm quảng cáo (Update the budgets of ad groups)
<a id="doc-1739591133130817"></a>
<!-- doc_id: 1739591133130817 -->

Sử dụng endpoint này để cập nhật ngân sách trọn đời (`lifetime budgets`) của một hoặc nhiều nhóm quảng cáo, hoặc thiết lập lịch thay đổi ngân sách theo lịch trình (`scheduled_budget`) cho ngân sách hàng ngày (`daily budgets`) hoặc ngân sách hàng ngày linh hoạt (`dynamic daily budgets`) của một hoặc nhiều nhóm quảng cáo.

Các thay đổi ngân sách theo lịch trình (`scheduled_budget`) sẽ có hiệu lực bắt đầu từ khoảng 00:00 sáng ngày hôm sau theo múi giờ của tài khoản quảng cáo. Lưu ý rằng ngân sách không thể được thiết lập hoặc cập nhật trong khoảng thời gian khóa ngân sách (budget lock time: 23:55 – 00:00) theo múi giờ của tài khoản quảng cáo.

Xem [Currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433) để tra cứu giới hạn ngân sách quảng cáo tối thiểu và tối đa theo từng loại tiền tệ.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/adgroup/budget/update/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập xác thực người dùng. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị cố định: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `budget` {+Conditional} | object[] | Bắt buộc truyền `budget` hoặc `scheduled_budget`.<br>• Để cập nhật ngân sách trọn đời cho một hoặc nhiều nhóm quảng cáo, chỉ định `budget`. Thay đổi này có hiệu lực ngay lập tức.<br>• Để cập nhật ngân sách hàng ngày hoặc ngân sách hàng ngày linh hoạt, chỉ định `scheduled_budget`.<br>Thông tin về ngân sách trọn đời mới muốn thiết lập. Kích thước mảng tối đa: 20 đối tượng. |
| `↳ adgroup_id` {+Conditional} | string | Bắt buộc khi truyền mảng `budget`.<br>ID của nhóm quảng cáo cần cập nhật ngân sách trọn đời. |
| `↳ budget` {+Conditional} | float | Bắt buộc khi truyền mảng `budget`.<br>Ngân sách trọn đời mới dành cho nhóm quảng cáo (`adgroup_id`). |
| `scheduled_budget` {+Conditional} | object[] | Bắt buộc truyền `budget` hoặc `scheduled_budget`.<br>Thông tin về lịch trình thay đổi ngân sách hàng ngày hoặc ngân sách hàng ngày linh hoạt cho một hoặc nhiều nhóm quảng cáo.<br>Kích thước mảng tối đa: 20 đối tượng.<br>**Lưu ý:** Lịch thay đổi ngân sách sẽ có hiệu lực từ 00:00 sáng ngày hôm sau theo múi giờ của tài khoản quảng cáo. |
| `↳ adgroup_id` {+Conditional} | string | Bắt buộc khi truyền mảng `scheduled_budget`.<br>ID của nhóm quảng cáo cần cập nhật ngân sách theo lịch trình. |
| `↳ scheduled_budget` {+Conditional} | float | Bắt buộc khi truyền mảng `scheduled_budget`.<br>Ngân sách hàng ngày hoặc ngân sách hàng ngày linh hoạt mới dành cho nhóm quảng cáo (`adgroup_id`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/budget/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "budget": [
      {
        "adgroup_id": "1765432109876599",
        "budget": 500.0
      }
    ],
    "scheduled_budget": [
      {
        "adgroup_id": "1765432109876599",
        "scheduled_budget": 100.0
      }
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/budget/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "budget": [
        {
            "adgroup_id": "1765432109876599",
            "budget": 500.0
        }
    ],
    "scheduled_budget": [
        {
            "adgroup_id": "1765432109876599",
            "scheduled_budget": 100.0
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi cập nhật thành công). |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu để theo dõi và đối soát. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020031110223101018904922300361F64",
  "data": {}
}
```
