import os, re

def complete_u115():
    path = "docs/09-marketing-api/quan-ly-chien-dich-p2.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Cleanly format currency table in doc 1750444779586561
    # Read the clean source from _clean/1750444779586561.md
    clean_curr_path = "_clean/1750444779586561.md"
    if os.path.exists(clean_curr_path):
        c_lines = [l.strip() for l in open(clean_curr_path).readlines() if l.strip()]
        # skip initial lines until first currency (British Pound)
        start_curr = -1
        for idx, l in enumerate(c_lines):
            if l == "British Pound":
                start_curr = idx
                break
        if start_curr != -1:
            curr_rows = []
            j = start_curr
            while j + 8 < len(c_lines):
                name = c_lines[j]
                code = c_lines[j+1]
                prec = c_lines[j+2]
                cpc = c_lines[j+3]
                cpm = c_lines[j+4]
                cpv = c_lines[j+5]
                ocpc = c_lines[j+6]
                gd = c_lines[j+7]
                ocpm = c_lines[j+8]
                curr_rows.append(f"| {name} | `{code}` | {prec} | {cpc} | {cpm} | {cpv} | {ocpc} | {gd} | {ocpm} |")
                j += 9
            
            table_str = ("| Tiền tệ (Currency) | Mã (Code) | Độ chính xác (Precision) | Giá thầu tối đa CPC | Giá thầu tối đa CPM | Giá thầu tối đa CPV | Giá thầu tối đa OCPC | Giá thầu tối đa GD | Giá thầu tối đa OCPM |\n"
                         "|---|---|---|---|---|---|---|---|---|\n" + "\n".join(curr_rows) + "\n\n")

            # Replace the currency block in text
            doc_marker = "<!-- doc_id: 1750444779586561 -->"
            end_marker = "<a id=\"doc-1746463274713089\"></a>"
            p1 = text.find(doc_marker)
            p2 = text.find(end_marker, p1)
            if p1 != -1 and p2 != -1:
                section_hdr = (doc_marker + "\n"
                               "# Giới hạn giá thầu (Bidding limits)\n"
                               "> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding > Bidding limits\n"
                               "Vui lòng tham khảo bảng dưới đây để tra cứu độ chính xác thập phân cho phép của từng loại tiền tệ và mức giá thầu tối đa tương ứng với từng sự kiện tính phí.\n\n")
                text = text[:p1] + section_hdr + table_str + "---\n\n" + text[p2:]

    # 2. Translate Budget EDR and Bid EDR tables
    budget_edr_old_frag = """# Get recommended budgets
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended budgets
Budget EDR (Estimated Delivery Results) enables you to adopt the suitable budget from estimated results to scale up your ad group and drive more conversions."""

    budget_edr_new_frag = """# Nhận ngân sách đề xuất (Get recommended budgets)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended budgets
Tính năng EDR ngân sách (Budget EDR) cho phép bạn áp dụng mức ngân sách tối ưu từ kết quả ước tính để mở rộng quy mô nhóm quảng cáo và thúc đẩy thêm nhiều chuyển đổi hơn. Kết quả ước tính (dành cho hiệu suất nhóm quảng cáo trong cùng ngày) bao gồm 15 bộ dữ liệu tương ứng với các tỷ lệ tăng ngân sách từ -20% đến 50% (bước nhảy 5%), cùng dữ liệu tăng trưởng chuyển đổi ước tính tương ứng.

## Điều kiện tiên quyết (Prerequisites)
Vui lòng bảo đảm các điều kiện sau được thỏa mãn trước khi gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378) để nhận đề xuất ước tính ngân sách:

### Ở cấp chiến dịch (At the campaign level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo (Advertising objective) | Một trong các mục tiêu: <ul><li>Quảng bá ứng dụng (App promotion)</li><li>Chuyển đổi web (Web conversions)</li><li>Tìm kiếm khách hàng tiềm năng (Lead generation)</li></ul> | `objective_type` | Giá trị hợp lệ: <ul><li>`APP_PROMOTION`</li><li>`WEB_CONVERSIONS`</li><li>`LEAD_GENERATION`</li></ul> |
| Tối ưu hóa ngân sách chiến dịch (Campaign Budget Optimization - CBO) | Tắt (Disabled) | `budget_optimize_on` | `false` |

### Ở cấp nhóm quảng cáo (At the ad group level)
> **Lưu ý:**
> Kết quả ước tính phân phối ngân sách được đưa ra theo cấu hình nhóm quảng cáo cụ thể. Nếu bạn đánh giá nhiều nhóm quảng cáo có cùng cấu hình qua `/tool/diagnosis/get/`, hệ thống chỉ trả về kết quả cho nhóm quảng cáo được tạo sớm nhất.

| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Vị trí hiển thị (Placement) | <ul><li><strong>Vị trí tự động (Automatic Placement)</strong> hoặc </li><li><strong>Chọn vị trí hiển thị (Select Placement)</strong> có bao gồm vị trí TikTok</li></ul> | `placement_type` & `placements` | <ul><li> Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc </li><li> Đặt `placement_type` là `PLACEMENT_TYPE_NORMAL` và bao gồm `PLACEMENT_TIKTOK` trong `placements`</li></ul> |
| Quảng cáo phát trực tiếp (Live ads) | Tắt (Disabled) | `promotion_type` | <strong>Khác</strong> `LIVE_SHOPPING` |
| Loại ngân sách (Budget type) | Ngân sách hàng ngày (Daily budget) | `budget_mode` | `BUDGET_MODE_DAY` |
| Mục tiêu tối ưu hóa (Optimization goal) | Một trong các mục tiêu: <ul><li> Lượt nhấp (Click) </li><li> Cài đặt (Install) </li><li>Khách hàng tiềm năng (Leads)</li><li>Chuyển đổi (Conversions)</li><li>Cuộc trò chuyện (Conversations)</li></ul> | `optimization_goal` | Giá trị hợp lệ: <ul><li>`CLICK`</li><li>`INSTALL`</li><li>`LEAD_GENERATION`</li><li>`CONVERT`</li><li>`CONVERSATION`</li></ul> |
| Chiến lược giá thầu (Bidding strategy) | Phân phối tối đa (Maximum Delivery) | `bid_type` | `BID_TYPE_NO_BID` |
| Sự kiện tính phí (Billing Event) | Loại `OCPX` | `billing_event` | `OCPC` hoặc `OCPM` |
| Tối ưu hóa sự kiện ứng dụng & VBO (App Event Optimization & Value-based Optimization) | Cả hai đều tắt (Both disabled) | `deep_bid_type` | `DEFAULT` |
| Ngân sách theo lịch (Scheduled budget) | Tắt (Disabled) | `scheduled_budget` | Không thiết lập qua [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817) |
| Yêu cầu khác (Other) | <ul><li> Không điều chỉnh ngân sách nhóm quảng cáo trong ngày muốn lấy đề xuất từ [/delivery/budget/recommend/](../12-api-reference/70-tools-p2.md#doc-1746463695763458).</li><li> Có ít nhất <strong>5</strong> lượt chuyển đổi trong ngày gần nhất.</li><li> Không phải nhóm quảng cáo đặt trước (reservation).</li></ul> | / | / |

## Các bước thực hiện (Steps)
Thực hiện các bước sau để sử dụng tính năng EDR Ngân sách:
1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Tạo quảng cáo** bằng cách gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
4. **Lọc ra các nhóm quảng cáo đạt điều kiện chuyển đổi** bằng cách xuất báo cáo. Nhóm quảng cáo cần có ít nhất **5** lượt chuyển đổi trong ngày gần nhất. Khuyến nghị chạy [Báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737), [Báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201), [Báo cáo mẫu tương tác](bao-cao-p3.md#doc-1738864940608513) hoặc [Báo cáo DSA](bao-cao-p3.md#doc-1738864960144385).
5. **Lấy đề xuất ngân sách** thông qua endpoint [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378). Truyền danh sách ID nhóm quảng cáo đạt chuẩn vào trường `adgroup_ids`. Kết quả ước tính phân phối ngân sách nằm trong đối tượng `budget_edr_info`.
6. **Cập nhật ngân sách trong cùng ngày** (theo múi giờ tài khoản nhà quảng cáo) bằng endpoint [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817)."""

    # Replace old Budget EDR section
    p_b_start = text.find("# Get recommended budgets\n> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended budgets")
    p_b_end = text.find("<a id=\"doc-1746463347473410\"></a>", p_b_start)
    if p_b_start != -1 and p_b_end != -1:
        text = text[:p_b_start] + budget_edr_new_frag + "\n\n---\n\n" + text[p_b_end:]

    # Replace old Bid EDR section
    bid_edr_new_frag = """# Nhận giá thầu đề xuất (Get recommended bids)
> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended bids
Tính năng EDR giá thầu (Bid EDR) cho phép bạn áp dụng mức giá thầu phù hợp từ kết quả ước tính để mở rộng quy mô nhóm quảng cáo và gia tăng tốc độ cắn tiền ngân sách. Kết quả ước tính (áp dụng trong cùng ngày) bao gồm 9 bộ dữ liệu tương ứng với các tỷ lệ tăng giá thầu từ -10% đến 30% (bước nhảy 5%) cùng dữ liệu chi phí gia tăng ước tính tương ứng.

## Điều kiện tiên quyết (Prerequisites)
Vui lòng bảo đảm các điều kiện sau được thỏa mãn trước khi gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378) để nhận đề xuất giá thầu:

### Ở cấp chiến dịch (At the campaign level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Mục tiêu quảng cáo (Advertising objective) | Một trong các mục tiêu: <ul><li>Quảng bá ứng dụng (App promotion)</li><li>Chuyển đổi web (Web conversions)</li><li>Tìm kiếm khách hàng tiềm năng (Lead generation)</li></ul> | `objective_type` | Giá trị hợp lệ: <ul><li>`APP_PROMOTION`</li><li>`WEB_CONVERSIONS`</li><li>`LEAD_GENERATION`</li></ul> |
| Tối ưu hóa ngân sách chiến dịch (Campaign Budget Optimization - CBO) | Tắt (Disabled) | `budget_optimize_on` | `false` |

### Ở cấp nhóm quảng cáo (At the ad group level)
| Cài đặt (Setting) | Yêu cầu (Requirement) | Tham số (Parameter) | Cách cấu hình tham số |
|---|---|---|---|
| Vị trí hiển thị (Placement) | <ul><li><strong>Vị trí tự động (Automatic Placement)</strong> hoặc </li><li><strong>Chọn vị trí hiển thị (Select Placement)</strong> có bao gồm TikTok</li></ul> | `placement_type` & `placements` | <ul><li> Đặt `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc </li><li> Đặt `placement_type` là `PLACEMENT_TYPE_NORMAL` và thêm `PLACEMENT_TIKTOK` vào `placements`</li></ul> |
| Quảng cáo phát trực tiếp (Live ads) | Tắt (Disabled) | `promotion_type` | <strong>Khác</strong> `LIVE_SHOPPING` |
| Loại ngân sách (Budget type) | Ngân sách hàng ngày (Daily budget) | `budget_mode` | `BUDGET_MODE_DAY` |
| Mục tiêu tối ưu hóa (Optimization goal) | Một trong các mục tiêu: <ul><li>Lượt nhấp (Click)</li><li>Cài đặt (Install)</li><li>Khách hàng tiềm năng (Leads)</li><li>Chuyển đổi (Conversions)</li><li>Cuộc trò chuyện (Conversations)</li></ul> | `optimization_goal` | Giá trị hợp lệ: <ul><li>`CLICK`</li><li>`INSTALL`</li><li>`LEAD_GENERATION`</li><li>`CONVERT`</li><li>`CONVERSATION`</li></ul> |
| Chiến lược giá thầu (Bidding strategy) | Giới hạn chi phí (Cost Cap) | `bid_type` | `BID_TYPE_CUSTOM` |
| Sự kiện tính phí (Billing Event) | Loại `OCPX` | `billing_event` | `OCPC` hoặc `OCPM` |
| Tối ưu sự kiện app & VBO (App Event Optimization & Value-based Optimization) | Cả hai đều tắt (Both disabled) | `deep_bid_type` | `DEFAULT` |
| Ngân sách theo lịch (Scheduled budget) | Tắt (Disabled) | `scheduled_budget` | Không thiết lập qua [/adgroup/budget/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739591133130817) |
| Yêu cầu khác (Other) | <ul><li>Không điều chỉnh giá thầu nhóm quảng cáo trong ngày muốn lấy đề xuất từ [/delivery/bid/recommend/](../12-api-reference/70-tools-p2.md#doc-1746463732779009).</li><li>Có ít nhất <strong>5</strong> lượt chuyển đổi trong ngày gần nhất.</li><li>Không phải nhóm quảng cáo đặt trước (reservation).</li></ul> | / | / |

## Các bước thực hiện (Steps)
Thực hiện theo các bước sau để áp dụng tính năng EDR Giá thầu:
1. **Tạo chiến dịch** bằng cách gọi [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo** bằng cách gọi [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
3. **Tạo mẫu quảng cáo** bằng cách gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
4. **Lọc các nhóm quảng cáo thỏa mãn điều kiện chuyển đổi** bằng cách xuất báo cáo (cần có tối thiểu **5** chuyển đổi trong ngày gần nhất). Bạn có thể chạy [Báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737), [Báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201), [Báo cáo mẫu tương tác](bao-cao-p3.md#doc-1738864940608513) hoặc [Báo cáo DSA](bao-cao-p3.md#doc-1738864960144385).
5. **Lấy đề xuất giá thầu** bằng cách gọi [/tool/diagnosis/get/](../12-api-reference/06-ad-diagnosis.md#doc-1738674986981378). Truyền ID nhóm quảng cáo đạt chuẩn vào trường `adgroup_ids`. Kết quả ước tính nằm trong đối tượng phản hồi `bid_edr_info`.
6. **Cập nhật giá thầu trong cùng ngày** (theo múi giờ tài khoản quảng cáo) bằng endpoint [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745) và gán giá thầu đã chọn vào trường `conversion_bid_price` hoặc `bid_price`."""

    p_bid_start = text.find("# Get recommended bids\n> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Estimated Delivery Results > Get recommended bids")
    p_bid_end = text.find("<a id=\"doc-1745292235571201\"></a>", p_bid_start)
    if p_bid_start != -1 and p_bid_end != -1:
        text = text[:p_bid_start] + bid_edr_new_frag + "\n\n---\n\n" + text[p_bid_end:]

    # 3. Clean up doc 1855450880142402 (Automatic Enhancements)
    # Translate table headings and text in doc 1855450880142402
    text = text.replace("#### For App Promotion ads", "#### Dành cho quảng cáo Quảng bá ứng dụng (App Promotion ads)")
    text = text.replace("#### For Lead Generation ads", "#### Dành cho quảng cáo Thu thập khách hàng tiềm năng (Lead Generation ads)")
    text = text.replace("#### For Sales ads", "#### Dành cho quảng cáo Doanh số bán hàng (Sales ads)")
    text = text.replace("### For Manual Ads", "### Dành cho quảng cáo thủ công (Manual Ads)")
    text = text.replace("#### For other ads", "#### Dành cho các loại quảng cáo khác (Other ads)")

    text = text.replace("**Advertising objective** (objective_type)", "**Mục tiêu quảng cáo (Advertising objective)** (`objective_type`)")
    text = text.replace("**App promotion type** (app_promotion_type)", "**Loại quảng bá ứng dụng (App promotion type)** (`app_promotion_type`)")
    text = text.replace("**Use catalog** (catalog_enabled)", "**Sử dụng danh mục (Use catalog)** (`catalog_enabled`)")
    text = text.replace("**Placement ** (placement_type and placements)", "**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)")
    text = text.replace("**Placement** (placement_type and placements)", "**Vị trí hiển thị (Placement)** (`placement_type` và `placements`)")
    text = text.replace("**Are Automatic Enhancements (creative_auto_enhancement_strategy_list)  available?**", "**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**")
    text = text.replace("**Are Automatic Enhancements (creative_auto_enhancement_strategy_list) available?**", "**Tính năng Tự động nâng cao (`creative_auto_enhancement_strategy_list`) khả dụng?**")
    text = text.replace("**Optimization Location** (promotion_type and promotion_target_type)", "**Vị trí tối ưu hóa (Optimization Location)** (`promotion_type` và `promotion_target_type`)")
    text = text.replace("**Sales destination** (sales_destination)", "**Đích đến bán hàng (Sales destination)** (`sales_destination`)")
    text = text.replace("**Catalog type** (catalog_type)", "**Loại danh mục (Catalog type)** (`catalog_type`)")
    text = text.replace("**Campaign type** (rf_campaign_type)", "**Loại chiến dịch (Campaign type)** (`rf_campaign_type`)")

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Done complete_u115")

if __name__ == "__main__":
    complete_u115()
