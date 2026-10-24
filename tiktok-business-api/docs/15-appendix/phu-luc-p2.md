# Phụ lục: mã lỗi, enum, quyền, múi giờ… — phần 2/2

Tài liệu này là phần tiếp theo của Phụ lục TikTok API for Business, tập trung vào các quy tắc kỹ thuật nâng cao dành cho giải pháp quảng cáo thông minh Upgraded Smart+, bao gồm các cài đặt nhắm mục tiêu khả dụng theo từng chế độ tối ưu hóa và các kịch bản cấu hình thông tin sản phẩm (`product_info`).

---

## Cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu trong Upgraded Smart+ Ad Groups (`Available targeting settings for different targeting optimization modes in Upgraded Smart+ Ad Groups`)
<a id="doc-1847839827327106"></a>
<!-- doc_id: 1847839827327106 -->

> Đường dẫn: Appendix > Available targeting settings for different targeting optimization modes in Upgraded Smart+ Ad Groups

Bảng dưới đây phác thảo các cài đặt nhắm mục tiêu khả dụng đối với các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong [Upgraded Smart+ Ad Groups](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843310524500993).

### Chế độ nhắm mục tiêu tự động (`Automatic targeting`)
Áp dụng khi `targeting_optimization_mode` được đặt là `AUTOMATIC` hoặc không chỉ định (mặc định).

| Hạng mục cài đặt nhắm mục tiêu | Yêu cầu / Điều kiện | Tham số API | Cách cấu hình tham số |
|---|---|---|---|
| **Kiểm soát đối tượng · Vị trí**<br>(`Audience controls · Location`) | Chỉ định các vị trí hợp lệ. Nếu có chỉ định danh mục sản phẩm (catalog), vị trí phải khớp hoặc là tập con của vị trí nhắm mục tiêu của catalog. | `location_ids` hoặc `zipcode_ids` hoặc cả hai | Chỉ định các giá trị hợp lệ. Nếu chỉ định catalog, hãy cung cấp ID vị trí khớp hoặc là tập con của vị trí nhắm mục tiêu của `catalog_id`. Để lấy vị trí nhắm mục tiêu của catalog, hãy gọi endpoint [/catalog/get/](https://business-api.tiktok.com/portal/docs/get-catalogs/v1.3) và kiểm tra trường `country` trả về. |
| **Kiểm soát đối tượng · Độ tuổi tối thiểu**<br>(`Audience controls · Minimum age`) | Một trong các tùy chọn sau:<br>• 18 tuổi trở lên<br>• 25 tuổi trở lên | `spc_audience_age` | Một trong các giá trị sau:<br>• `OVER_EIGHTEEN` hoặc không chỉ định<br>• `OVER_TWENTY_FIVE` |
| **Kiểm soát đối tượng · Ngôn ngữ** (Tùy chọn)<br>(`Audience controls · Languages`) | Bật hoặc tắt | `languages` | Chỉ định các giá trị mã ngôn ngữ hợp lệ hoặc không chỉ định |
| **Kiểm soát đối tượng · Loại trừ đối tượng** (Tùy chọn)<br>(`Audience controls · Exclude audience`) | Bật hoặc tắt | `excluded_audience_ids` | Chỉ định danh sách ID đối tượng cần loại trừ hoặc không chỉ định |
| **Gợi ý đối tượng · Độ tuổi** (Tùy chọn)<br>(`Audience suggestions · Age`)<br>> [!NOTE]<br>> Gợi ý đối tượng chỉ mang tính định hướng cho việc nhắm mục tiêu tự động bằng cách bổ sung thêm thiết lập. Đây chỉ là các gợi ý và việc phân phối tới các đối tượng đó không được đảm bảo tuyệt đối. | Bật hoặc tắt | `age_groups` | Chỉ định các giá trị nhóm tuổi hợp lệ hoặc không chỉ định |
| **Gợi ý đối tượng · Giới tính** (Tùy chọn)<br>(`Audience suggestions · Gender`) | Bật hoặc tắt | `gender` | Chỉ định giá trị giới tính hợp lệ hoặc không chỉ định |
| **Gợi ý đối tượng · Đối tượng tùy chỉnh** (Tùy chọn)<br>(`Audience suggestions · Custom audience`) | Bật hoặc tắt | `audience_ids` | Chỉ định danh sách ID đối tượng tùy chỉnh hoặc không chỉ định |
| **Gợi ý đối tượng · Sở thích & hành vi · Sở thích** (Tùy chọn)<br>(`Audience suggestions · Interests & behaviors · Interests`) | Bật hoặc tắt | `interest_category_ids`<br>`interest_keyword_ids` | Chỉ định ID danh mục hoặc từ khóa sở thích hợp lệ hoặc không chỉ định |
| **Gợi ý đối tượng · Sở thích & hành vi · Ý định mua hàng** (Tùy chọn)<br>(`Audience suggestions · Interests & behaviors · Purchase intention`) | Bật hoặc tắt | `purchase_intention_keyword_ids` | Chỉ định ID từ khóa ý định mua hàng hợp lệ hoặc không chỉ định |
| **Gợi ý đối tượng · Sở thích & hành vi · Tương tác video · Tương tác nhà sáng tạo · Tương tác hashtag** (Tùy chọn) | Bật hoặc tắt | `actions` | Chỉ định hành động hợp lệ hoặc không chỉ định |

---

### Chế độ nhắm mục tiêu tùy chỉnh (`Custom targeting`)
Áp dụng khi `targeting_optimization_mode` được đặt là `MANUAL`.

| Hạng mục cài đặt nhắm mục tiêu | Yêu cầu / Điều kiện | Tham số API | Cách cấu hình tham số |
|---|---|---|---|
| **Nhân khẩu học · Vị trí**<br>(`Demographics · Location`) | Chỉ định giá trị hợp lệ. Nếu có catalog, vị trí phải khớp hoặc là tập con của vị trí catalog. | `location_ids` hoặc `zipcode_ids` hoặc cả hai | Chỉ định giá trị hợp lệ. Để lấy vị trí catalog, dùng [/catalog/get/](../12-api-reference/25-catalog-management.md#doc-1740315452868610) và xem trường `country`. |
| **Nhân khẩu học · Sản phẩm/Thương hiệu HFSS**<br>(`Demographics · HFSS Product/Brand`) | Bật hoặc tắt.<br>• Có thể bật khi vị trí nhắm mục tiêu bao gồm Vương quốc Anh, Úc, New Zealand và Liên minh Châu Âu (EU). | `is_hfss` | `true` hoặc `false`.<br>• Đặt thành `true` khi vị trí bao gồm UK, Australia, New Zealand hoặc EU. |
| **Nhân khẩu học · Tuân thủ LHF (Thực phẩm kém lành mạnh)**<br>(`Demographics · LHF compliance`) | Bật hoặc tắt.<br>• Cài đặt này bắt buộc phải bật khi vị trí nhắm mục tiêu bao gồm Vương quốc Anh và sản phẩm/thương hiệu HFSS được bật. | `is_lhf_compliance` | `true` hoặc `false`.<br>• Cần đặt là `true` khi vị trí bao gồm UK và `is_hfss = true`. |
| **Nhân khẩu học · Độ tuổi** (Tùy chọn)<br>(`Demographics · Age`) | Bật hoặc tắt | `age_groups` | Chỉ định các giá trị nhóm tuổi hợp lệ hoặc không chỉ định |
| **Nhân khẩu học · Giới tính** (Tùy chọn)<br>(`Demographics · Gender`) | Bật hoặc tắt | `gender` | Chỉ định giá trị giới tính hợp lệ hoặc không chỉ định |
| **Nhân khẩu học · Ngôn ngữ** (Tùy chọn)<br>(`Demographics · Languages`) | Bật hoặc tắt | `languages` | Chỉ định mã ngôn ngữ hợp lệ hoặc không chỉ định |
| **Đối tượng tùy chỉnh · Bao gồm đối tượng** (Tùy chọn)<br>(`Custom audience · Include audience`) | Bật hoặc tắt | `audience_ids` | Chỉ định danh sách ID đối tượng hoặc không chỉ định |
| **Đối tượng tùy chỉnh · Đối tượng thông minh** (Tùy chọn)<br>(`Custom audience · Smart audience`) | Bật hoặc tắt | `smart_audience_enabled` | `true` hoặc `false` |
| **Đối tượng tùy chỉnh · Loại trừ đối tượng** (Tùy chọn)<br>(`Custom audience · Exclude audience`) | Bật hoặc tắt | `excluded_audience_ids` | Chỉ định danh sách ID đối tượng cần loại trừ hoặc không chỉ định |
| **Nhắm mục tiêu chi tiết · Sở thích & hành vi · Sở thích** (Tùy chọn) | Bật hoặc tắt | `interest_category_ids`<br>`interest_keyword_ids` | Chỉ định danh mục hoặc từ khóa sở thích hợp lệ hoặc không chỉ định |
| **Nhắm mục tiêu chi tiết · Sở thích & hành vi · Ý định mua hàng** (Tùy chọn) | Bật hoặc tắt | `purchase_intention_keyword_ids` | Chỉ định ID từ khóa ý định mua hàng hoặc không chỉ định |
| **Nhắm mục tiêu chi tiết · Tương tác video, nhà sáng tạo, hashtag** (Tùy chọn) | Bật hoặc tắt | `actions` | `true` hoặc `false` |
| **Nhắm mục tiêu chi tiết · Sở thích & hành vi thông minh** (Tùy chọn)<br>(`Smart interests & behaviors`) | Bật hoặc tắt | `smart_interest_behavior_enabled` | Chỉ định giá trị hợp lệ hoặc không chỉ định |
| **Nhắm mục tiêu chi tiết · Khả năng chi tiêu** (Tùy chọn)<br>(`Detailed targeting · Spending power`) | Bật hoặc tắt | `spending_power` | Chỉ định giá trị hợp lệ hoặc không chỉ định |
| **Nhắm mục tiêu chi tiết · Thu nhập hộ gia đình** (Tùy chọn)<br>(`Detailed targeting · Household income`) | Bật hoặc tắt | `household_income` | Chỉ định giá trị hợp lệ hoặc không chỉ định |
| **Thiết bị · Hệ điều hành** (Tùy chọn)<br>(`Device · Operating system`) | Bật hoặc tắt | `operating_systems` | Chỉ định giá trị hệ điều hành hoặc không chỉ định |
| **Thiết bị · Phiên bản hệ điều hành** (Tùy chọn)<br>(`Device · OS versions`) | Bật hoặc tắt | `min_android_version`<br>`min_ios_version` | Chỉ định phiên bản tối thiểu hoặc không chỉ định |
| **Thiết bị · Dòng máy thiết bị** (Tùy chọn)<br>(`Device · Device model`) | Bật hoặc tắt | `device_model_ids` | Chỉ định danh sách ID thiết bị hoặc không chỉ định |
| **Thiết bị · Loại kết nối mạng** (Tùy chọn)<br>(`Device · Connection type`) | Bật hoặc tắt | `network_types` | Chỉ định loại mạng hoặc không chỉ định |
| **Thiết bị · Nhà mạng viễn thông** (Tùy chọn)<br>(`Device · Carriers`) | Bật hoặc tắt | `carrier_ids` | Chỉ định danh sách ID nhà mạng hoặc không chỉ định |
| **Thiết bị · Nhà cung cấp dịch vụ Internet (ISP)** (Tùy chọn) | Bật hoặc tắt | `isp_ids` | Chỉ định danh sách ID nhà mạng ISP hoặc không chỉ định |
| **Thiết bị · Giá thiết bị** (Tùy chọn)<br>(`Device · Device price`) | Bật hoặc tắt | `device_price_ranges` | Chỉ định khoảng giá thiết bị hoặc không chỉ định |
| **Sử dụng đối tượng đã lưu** (Tùy chọn)<br>(`Use saved audience`) | Bật hoặc tắt | `saved_audience_id` | Chỉ định ID đối tượng đã lưu hợp lệ hoặc không chỉ định |

---

## Cài đặt thông tin sản phẩm khả dụng trong Chiến dịch Upgraded Smart+ (`Available product information settings in Upgraded Smart+ Campaigns`)
<a id="doc-1860735968798721"></a>
<!-- doc_id: 1860735968798721 -->

> Đường dẫn: Appendix > Available product information settings in Upgraded Smart+ Campaigns

Tính khả dụng của tính năng "thông tin sản phẩm" trong Chiến dịch Upgraded Smart+ (được cấu hình thông qua tham số `product_info`) phụ thuộc vào các cài đặt chiến dịch và cài đặt nhóm quảng cáo khác nhau.

Các bảng dưới đây phác thảo chi tiết các kịch bản nơi `product_info` có thể được sử dụng để bật tính năng "thông tin sản phẩm" thông qua endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921).

### Dành cho quảng cáo Quảng bá ứng dụng (`For App Promotion ads`)

| Cấp chiến dịch: Mục tiêu quảng cáo (`objective_type`) | Cấp chiến dịch: Loại quảng bá ứng dụng (`app_promotion_type`) | Cấp chiến dịch: Sử dụng danh mục (`catalog_enabled`) | Cấp quảng cáo: `product_info` có khả dụng không? | Các cài đặt thông tin sản phẩm cụ thể khả dụng bên trong `product_info` | Cài đặt bắt buộc cho `product_info_enabled` |
|---|---|---|---|---|---|
| `APP_PROMOTION` | `APP_INSTALL` | `false` | ✅ Có | • Điểm bán hàng (`selling_points`) | `NON_CATALOG` |
| `APP_PROMOTION` | `APP_RETARGETING` | `false` | ✅ Có | • Điểm bán hàng (`selling_points`) | `NON_CATALOG` |
| `APP_PROMOTION` | `MINIS` | `false` | ✅ Có | • Điểm bán hàng (`selling_points`) | `NON_CATALOG` |
| `APP_PROMOTION` | Bất kỳ loại nào ở trên | `true` | ❌ Không | ❌ Không có | Không chỉ định (`Not specified`) |

---

### Dành cho quảng cáo Doanh số (`For Sales ads`)

| Cấp chiến dịch: Mục tiêu quảng cáo (`objective_type`) | Cấp chiến dịch: Đích bán hàng (`sales_destination`) | Cấp chiến dịch: Sử dụng catalog (`catalog_enabled`) | Cấp chiến dịch: Loại catalog (`catalog_type`) | Cấp quảng cáo: `product_info` có khả dụng? | Các cài đặt thông tin sản phẩm cụ thể khả dụng bên trong `product_info` | Cài đặt bắt buộc cho `product_info_enabled` |
|---|---|---|---|---|---|---|
| `WEB_CONVERSIONS` | `WEBSITE` | `false` | Không chỉ định | ✅ Có | • Tên sản phẩm (`product_titles`)<br>• Hình ảnh sản phẩm (`product_image_list`)<br>• Điểm bán hàng (`selling_points`)<br>• Mã ưu đãi/khuyến mãi (`promo_info_list`) | `NON_CATALOG` |
| `WEB_CONVERSIONS` | `WEBSITE` | `true` | `ECOMMERCE` | ✅ Có | • Cài đặt thẻ sản phẩm (`product_card_type`)<br>• Thông tin sản phẩm thẻ (`catalog_tag_list`) | `CATALOG` |
| `WEB_CONVERSIONS` | `WEBSITE` | `true` | `TRAVEL_ENTERTAINTAINMENT` | ❌ Không | ❌ Không có | Không chỉ định |
| `WEB_CONVERSIONS` | `WEBSITE` | `true` | `MINI_SERIES` | ❌ Không | ❌ Không có | Không chỉ định |
| `WEB_CONVERSIONS` | `APP` | `true` | `ECOMMERCE` | ✅ Có | • Thông tin sản phẩm thẻ (`catalog_tag_list`) | `CATALOG` |
| `WEB_CONVERSIONS` | `WEB_AND_APP` | `false` | Không chỉ định | ❌ Không | ❌ Không có | Không chỉ định |
| `WEB_CONVERSIONS` | `WEB_AND_APP` | `true` | `ECOMMERCE` | ✅ Có | • Thông tin sản phẩm thẻ (`catalog_tag_list`) | `CATALOG` |
| `WEB_CONVERSIONS` | `WEB_AND_APP` | `true` | `TRAVEL_ENTERTAINTAINMENT` | ❌ Không | ❌ Không có | Không chỉ định |

---

### Dành cho quảng cáo Khách hàng tiềm năng (`For Lead Generation ads`)

| Cấp chiến dịch: `objective_type` | Cấp chiến dịch: `catalog_enabled` | Cấp nhóm quảng cáo: Vị trí tối ưu hóa (`promotion_type` & `promotion_target_type`) | Cấp nhóm quảng cáo: Loại catalog (`catalog_id`) | Cấp quảng cáo: `product_info` khả dụng? | Các cài đặt cụ thể khả dụng trong `product_info` | Cài đặt bắt buộc cho `product_info_enabled` |
|---|---|---|---|---|---|---|
| `LEAD_GENERATION` | `false` | Biểu mẫu tức thì (`promotion_type = LEAD_GENERATION`, `promotion_target_type = INSTANT_PAGE`) | Không chỉ định | ✅ Có | • `product_titles`<br>• `product_image_list`<br>• `selling_points` | `NON_CATALOG` |
| `LEAD_GENERATION` | `false` | Trang web (`promotion_type = LEAD_GENERATION`, `promotion_target_type = EXTERNAL_WEBSITE`) | Không chỉ định | ✅ Có | • `product_titles`<br>• `product_image_list`<br>• `selling_points` | `NON_CATALOG` |
| `LEAD_GENERATION` | `true` | Trang web (`promotion_type = LEAD_GENERATION`, `promotion_target_type = EXTERNAL_WEBSITE`) | Auto-Inventory | ✅ Có | • `catalog_tag_list` | `CATALOG` |
| `LEAD_GENERATION` | `true` | Trang web (`promotion_type = LEAD_GENERATION`, `promotion_target_type = EXTERNAL_WEBSITE`) | Auto-Model | ❌ Không | ❌ Không có | Không chỉ định |
| `LEAD_GENERATION` | `false` | Tin nhắn trực tiếp TikTok (`promotion_type = LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`) | Không chỉ định | ✅ Có | • `product_titles`<br>• `product_image_list`<br>• `selling_points` | `NON_CATALOG` |
| `LEAD_GENERATION` | `true` | Tin nhắn trực tiếp TikTok (`promotion_type = LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`) | Auto-Inventory | ✅ Có | • `catalog_tag_list` | `CATALOG` |
| `LEAD_GENERATION` | `true` | Tin nhắn trực tiếp TikTok (`promotion_type = LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`) | Auto-Model | ❌ Không | ❌ Không có | Không chỉ định |
| `LEAD_GENERATION` | `false` | Ứng dụng nhắn tin mạng xã hội (`promotion_type = LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`) | Không chỉ định | ✅ Có | • `product_titles`<br>• `product_image_list`<br>• `selling_points` | `NON_CATALOG` |
| `LEAD_GENERATION` | `false` | Cuộc gọi điện thoại (`promotion_type = LEAD_GEN_CLICK_TO_CALL`) | Không chỉ định | ✅ Có | • `product_titles`<br>• `product_image_list`<br>• `selling_points` | `NON_CATALOG` |
