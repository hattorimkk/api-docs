# Khám phá (Discovery)
<a id="doc-1825119005427714"></a>
<!-- doc_id: 1825119005427714 -->

Discovery API cho phép bạn khám phá các hashtag phổ biến trên TikTok nhằm sáng tạo nội dung xoay quanh các chủ đề thịnh hành, đồng thời tìm kiếm các bản nhạc thịnh hành từ Thư viện Âm nhạc Thương mại (Commercial Music Library) để sử dụng trong nội dung tự nhiên (organic) và tạo quảng cáo.

Xem thêm [Tổng quan](../10-organic-api/discovery-api.md#doc-1825127469285442) để tìm hiểu thêm về quy trình tích hợp và cấp quyền sử dụng Discovery API.

Nhóm API này bao gồm các endpoint sau:
- [Lấy danh sách hashtag phổ biến](40-discovery.md#doc-1825119032526849)
- [Lấy thông tin chi tiết của một hashtag phổ biến](40-discovery.md#doc-1825119047070721)
- [Lấy danh sách video thịnh hành liên quan đến hashtag](40-discovery.md#doc-1825119056527362)
- [Lấy danh sách bài hát thịnh hành từ Thư viện Âm nhạc Thương mại](40-discovery.md#doc-1825119063013505)
- [Lấy danh sách video thịnh hành liên quan đến bài hát](40-discovery.md#doc-1825119068941314)
- [Lấy từ khóa tìm kiếm thịnh hành](40-discovery.md#doc-1832798345014338)
- [Lấy từ khóa tìm kiếm được đề xuất](40-discovery.md#doc-1832798361818114)

---

## Lấy danh sách hashtag phổ biến (`Get popular hashtags`)
<a id="doc-1825119032526849"></a>
<!-- doc_id: 1825119032526849 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/trending_list/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách top 200 hashtag thịnh hành và phổ biến nhất trên TikTok theo từng quốc gia, danh mục ngành hàng và khoảng thời gian.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. Truyền một trong các ID được trả về qua trường `advertiser_ids` từ [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| discovery_type | string | Bắt buộc | Loại đối tượng khám phá. Hiện tại chỉ hỗ trợ giá trị: `HASHTAG`. |
| country_code | string | Không | Mã vị trí quốc gia/khu vực. Giá trị mặc định: `US`. Xem [Mã vị trí (Location code)](../15-appendix/phu-luc-p1.md#doc-1737585867307010) để biết các giá trị được hỗ trợ (ví dụ: `VN`, `US`, `DE`). |
| category_name | string | Không | Tên danh mục ngành hàng của hashtag. Giá trị mặc định: `ALL`. Có thể truyền danh mục cấp 1 hoặc cấp 2 (ví dụ: `FOOD_AND_BEVERAGE`, `BEAUTY`). Nếu truyền đồng thời cả `category_name` và `industry_id`, hệ thống sẽ ưu tiên `category_name` và bỏ qua `industry_id`. |
| date_range | string | Không | Khoảng thời gian đo lường độ phổ biến của hashtag. Giá trị mặc định: `7DAY`.<br>Các giá trị enum:<br>• `1DAY`: 1 ngày gần nhất.<br>• `7DAY`: 7 ngày gần nhất.<br>• `30DAY`: 30 ngày gần nhất.<br>• `120DAY`: 120 ngày gần nhất. |

### Danh mục ngành hàng hashtag (`Hashtag industry category names`)

Bảng dưới đây liệt kê các danh mục ngành hàng cấp 1 (Level-1) và cấp 2 (Level-2) bạn có thể truyền vào tham số `category_name`:

| Danh mục cấp 1 (Level-1) | Danh mục cấp 2 (Level-2) | Mô tả nội dung |
|---|---|---|
| `ALL` | - | Nội dung bao quát tất cả các chủ đề. |
| `APPAREL_AND_ACCESSORIES` | `OTHER_FASHION`<br>`OUTFITS` | Thời trang và phụ kiện: xu hướng mới nhất, mẹo phối đồ, phong cách thời trang. |
| `BABY_KIDS_AND_MATERNITY` | `BABY_CARE` | Mẹ và bé: lời khuyên nuôi dạy con, chăm sóc trẻ, đánh giá sản phẩm cho bé. |
| `BEAUTY_AND_PERSONAL_CARE` | `BEAUTY`<br>`BEAUTY_SERVICES`<br>`HAIR_CARE`<br>`OTHER_BEAUTY` | Làm đẹp và chăm sóc cá nhân: hướng dẫn trang điểm, quy trình skincare, chăm sóc tóc, dịch vụ spa, salon. |
| `BUSINESS_SERVICES` | `CAREER_AND_PROFESSIONAL_GROWTH` | Dịch vụ doanh nghiệp: định hướng nghề nghiệp, kỹ năng công sở, phát triển chuyên môn, tuyển dụng. |
| `EDUCATION` | `ACADEMIC_RESOURCES`<br>`COLLEGE`<br>`HISTORY_AND_LITERATURE`<br>`LEARNING_AND_DEVELOPMENT`<br>`SCIENCE` | Giáo dục: tài liệu học tập, đời sống đại học, lịch sử, văn học, khoa học, phát triển bản thân. |
| `FINANCIAL_SERVICES` | `BUSINESS_AND_FINANCE` | Dịch vụ tài chính: tài chính cá nhân, đầu tư, quản lý tài chính, xu hướng thị trường. |
| `FOOD_AND_BEVERAGE` | `COOKING`<br>`DRINKS`<br>`EATING_EXPERIENCES`<br>`FOOD`<br>`FOOD_RECOMMENDATIONS` | Thực phẩm và đồ uống: công thức nấu ăn, đồ uống, review quán ăn, trải nghiệm ẩm thực. |
| `GAMES` | `CARD_AND_BOARD_GAMES`<br>`VIDEO_GAMES` | Trò chơi: game board, video game, review game, gameplay và văn hóa gaming. |
| `HEALTH` | `HEALTH_AND_WELLNESS` | Sức khỏe: thể dục, chăm sóc sức khỏe tinh thần, phòng bệnh, lối sống lành mạnh. |
| `HOME_IMPROVEMENT` | `HOME_AND_GARDEN`<br>`HOUSEHOLD_PRODUCTS`<br>`TOYS_COLLECTIBLES_AND_MEMORABILIA` | Cải tạo nhà cửa: thiết kế nội thất, đồ gia dụng, làm vườn, đồ chơi và mô hình sưu tầm. |
| `LIFE_SERVICES` | `CRAFTING_AND_CREATIONS`<br>`DIARY_AND_VLOG`<br>`ENVIRONMENT`<br>`FAMILY`<br>`PHOTOGRAPHY`<br>`PRODUCTIVITY_AND_EFFICIENCY` | Đời sống: đồ thủ công DIY, vlog thường ngày, môi trường, gia đình, nhiếp ảnh, mẹo năng suất. |
| `NEWS_AND_ENTERTAINMENT` | `ANIMATION_AND_COMICS`<br>`ART`<br>`COMEDY`<br>`COMMUNITY_UPDATES_AND_ISSUES`<br>`CULTURE`<br>`DANCE`<br>`ENTERTAINMENT_AND_SPORTS_NEWS`<br>`MISCELLANEOUS_PERFORMANCES`<br>`MOVIES_AND_TV`<br>`MUSIC`<br>`PERFORMING_ARTS`<br>`PERSONAL_PHOTOGRAPHY`<br>`ROMANCE`<br>`SENSORY_EXPERIENCES`<br>`SHOWS_FESTIVALS_AND_EXHIBITIONS`<br>`SPECIAL_EFFECTS`<br>`SPORTS`<br>`SUPERNATURAL_AND_HORROR` | Tin tức và giải trí: hoạt hình, truyện tranh, nghệ thuật, hài kịch, văn hóa, nhảy múa, tin sao, phim ảnh, âm nhạc, kịch nghệ, chuyện tình cảm, trải nghiệm ASMR, lễ hội, hiệu ứng điện ảnh, thể thao, kinh dị. |
| `PETS` | `PET_CARE_AND_ACCESSORIES`<br>`LIVESTOCK_AND_FARMING`<br>`WILDLIFE_AND_EXOTIC_PETS` | Thú cưng: chăm sóc chó mèo, phụ kiện thú cưng, chăn nuôi, động vật hoang dã và kỳ lạ. |
| `SPORTS_AND_OUTDOOR` | `CONVENTIONAL_AND_MAINSTREAM_SPORTS`<br>`EXERCISE_AND_FITNESS`<br>`EXTREME_AND_ADVENTURE_SPORTS`<br>`LEISURE_AND_RECREATION_FACILITIES`<br>`OUTDOOR_RECREATION` | Thể thao và ngoài trời: bóng đá, bóng rổ, tennis, tập gym, thể thao mạo hiểm, khu vui chơi, cắm trại, leo núi, câu cá. |
| `TECHNOLOGY` | `GADGETS_AND_INNOVATION`<br>`SOFTWARE_AND_APPS` | Công nghệ: đánh giá thiết bị thông minh, công nghệ mới, ứng dụng di động và phần mềm. |
| `TRAVEL` | `GENERAL_TRAVEL` | Du lịch: cẩm nang du lịch, điểm đến hấp dẫn, mẹo du lịch, lưu trú và trải nghiệm. |
| `VEHICLE_AND_TRANSPORTATION` | `AUTOMOTIVE`<br>`OTHER_TRANSPORTATION` | Phương tiện giao thông: đánh giá ô tô, bảo dưỡng xe, mô tô, xe đạp, phương tiện công cộng. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ filter_info | object | Thông tin bộ lọc đã áp dụng cho yêu cầu. Nếu không truyền trong yêu cầu, hệ thống sẽ trả về các giá trị mặc định (`date_range = 7DAY`, `country_code = US`, `category_name = ALL`). |
| ↳↳ date_range | string | Khoảng thời gian đã áp dụng (`1DAY`, `7DAY`, `30DAY`, `120DAY`). |
| ↳↳ country_code | string | Mã quốc gia/khu vực đã áp dụng (ví dụ: `US`, `VN`). |
| ↳↳ category_name | string | Tên danh mục ngành hàng đã áp dụng (ví dụ: `ALL`, `FOOD_AND_BEVERAGE`). |
| ↳ list | object[] | Danh sách các hashtag phổ biến nhất (tối đa 200). |
| ↳↳ hashtag_id | string | ID định danh của hashtag (ví dụ: `4268426520694`). |
| ↳↳ hashtag_name | string | Tên hashtag (ví dụ: `yummy`, `fashion`). |
| ↳↳ rank_position | string | Thứ hạng hiện tại của hashtag trong danh mục (`category_name`) hoặc khu vực (`country_code`) đã chọn (ví dụ: `1`, `100`). |
| ↳↳ rank_change | string | Thay đổi thứ hạng so với kỳ trước:<br>• Số dương: thăng hạng (ví dụ từ 5 lên 1 là `4`).<br>• Số âm: tụt hạng (ví dụ từ 1 xuống 5 là `-4`).<br>• `0`: thứ hạng không đổi.<br>• `NEW`: hashtag mới lọt vào top 200 trong kỳ này. |
| ↳↳ views | integer | Số lượt xem của các video liên quan có gắn hashtag này trong khu vực và khoảng thời gian đã chọn. |
| ↳↳ views_global_lifetime | integer | Tổng số lượt xem toàn cầu trọn đời (lifetime) của các video gắn hashtag này. |
| ↳↳ posts | integer | Số lượng video đăng tải có gắn hashtag này trong khu vực và khoảng thời gian đã chọn. |
| ↳↳ posts_global_lifetime | integer | Tổng số lượng video đăng tải toàn cầu trọn đời có gắn hashtag này. |
| ↳↳ top_country_list | string[] | Danh sách mã vị trí của top 5 quốc gia/khu vực mà hashtag này phổ biến nhất trên thế giới (ví dụ: `["US", "VN", "TH", "ID", "PH"]`). |
| ↳↳ trending_history | object[] | Dữ liệu lịch sử xếp hạng của hashtag trong tối đa 30 ngày gần nhất. |
| ↳↳↳ date | string | Ngày ghi nhận dữ liệu theo định dạng `YYYY-MM-DD`. |
| ↳↳↳ rank_position_daily | string | Thứ hạng hàng ngày của hashtag trên toàn bộ các danh mục tại khu vực đã chọn. Giá trị sẽ là `null` nếu hashtag không đủ điều kiện thịnh hành trong ngày đó. |
| ↳↳↳ views_daily | integer | Số lượt xem video hàng ngày của hashtag tại khu vực đã chọn. Nếu số lượt xem dưới 1.000, giá trị sẽ là `null`. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/trending_list/?advertiser_id=7123456789012345678&discovery_type=HASHTAG&category_name=FOOD_AND_BEVERAGE&country_code=VN&date_range=7DAY' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/trending_list/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "discovery_type": "HASHTAG",
    "category_name": "FOOD_AND_BEVERAGE",
    "country_code": "VN",
    "date_range": "7DAY"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for item in data.get("data", {}).get("list", [])[:5]:
    print(f"Top {item.get('rank_position')}: #{item.get('hashtag_name')} | Lượt xem: {item.get('views')} | Thay đổi: {item.get('rank_change')}")
```

#### Ví dụ phản hồi thành công (Rút gọn)

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048A1B2C3",
    "data": {
        "list": [
            {
                "hashtag_id": "4268426520694",
                "hashtag_name": "yummy",
                "rank_position": "1",
                "rank_change": "0",
                "posts": 44585,
                "posts_global_lifetime": 26055679,
                "views": 836896026,
                "views_global_lifetime": 136840398711,
                "top_country_list": [
                    "US",
                    "TH",
                    "ID",
                    "VN",
                    "PH"
                ],
                "trending_history": [
                    {
                        "date": "2026-04-06",
                        "rank_position_daily": "85",
                        "views_daily": 49419265
                    },
                    {
                        "date": "2026-04-07",
                        "rank_position_daily": "128",
                        "views_daily": 45524768
                    }
                ]
            }
        ],
        "filter_info": {
            "country_code": "VN",
            "date_range": "7DAY",
            "category_name": "FOOD_AND_BEVERAGE"
        }
    }
}
```

---

## Lấy thông tin chi tiết của một hashtag phổ biến (`Get details of a popular hashtag`)
<a id="doc-1825119047070721"></a>
<!-- doc_id: 1825119047070721 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/detail/`

**Mục đích**: Sử dụng endpoint này để lấy thông tin chi tiết chuyên sâu về một hashtag phổ biến, bao gồm thông tin chi tiết về đối tượng người xem (audience insights) và trạng thái của hashtag (`hashtag_status`).

> [!TIP]
> - Nếu `hashtag_status` trả về là `ONLINE`, bạn có thể sử dụng endpoint [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) và truyền `hashtag_id` nhận được vào trường `action_category_ids` để nhắm mục tiêu (targeting) theo hành vi người dùng tương tác với hashtag đó.
> - Bạn cũng có thể khám phá thêm các hashtag tương tự bằng endpoint [/tool/hashtag/recommend/](70-tools-p1.md#doc-1736271339521025) bằng cách truyền `hashtag_name` vào trường `keywords`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. Truyền một trong các ID được trả về qua trường `advertiser_ids` từ [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| discovery_type | string | Bắt buộc | Loại đối tượng khám phá. Hiện tại chỉ hỗ trợ: `HASHTAG`. |
| hashtag_id | string | Bắt buộc | ID của hashtag, lấy từ endpoint [/discovery/trending_list/](40-discovery.md#doc-1825119032526849). Nếu ID hashtag cung cấp không nằm trong danh sách trả về từ `/discovery/trending_list/`, bạn sẽ nhận được kết quả rỗng. Ví dụ: `4268426520694`. |
| country_code | string | Bắt buộc | Mã vị trí quốc gia/khu vực. Phải truyền cùng giá trị `country_code` như đã dùng trong `/discovery/trending_list/`. Nếu mã quốc gia không gắn với hashtag, hệ thống sẽ trả về lỗi. Xem [Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). Ví dụ: `US`, `VN`. |
| date_range | string | Bắt buộc | Khoảng thời gian thịnh hành của hashtag. Phải truyền cùng giá trị `date_range` như đã dùng trong `/discovery/trending_list/`. Các giá trị enum: `1DAY`, `7DAY`, `30DAY`, `120DAY`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ hashtag_id | string | ID của hashtag. |
| ↳ hashtag_name | string | Tên hashtag. |
| ↳ views | integer | Số lượt xem video liên quan gắn hashtag này trong khu vực và khoảng thời gian đã chọn. |
| ↳ views_global_lifetime | integer | Tổng số lượt xem toàn cầu trọn đời của hashtag. |
| ↳ posts | integer | Số lượng video gắn hashtag này trong khu vực và khoảng thời gian đã chọn. |
| ↳ posts_global_lifetime | integer | Tổng số lượng video toàn cầu trọn đời gắn hashtag này. |
| ↳ top_country_list | string[] | Mã vị trí của top 5 quốc gia/khu vực mà hashtag này phổ biến nhất thế giới. |
| ↳ hashtag_status | string | Trạng thái của hashtag dùng cho quảng cáo:<br>• `ONLINE`: Khả dụng để tạo nhóm quảng cáo nhắm mục tiêu.<br>• `OFFLINE`: Không khả dụng để tạo quảng cáo. |
| ↳ trending_history | object[] | Dữ liệu lịch sử thứ hạng của hashtag trong tối đa 30 ngày qua. |
| ↳↳ date | string | Ngày ghi nhận dữ liệu (`YYYY-MM-DD`). |
| ↳↳ rank_position_daily | string | Thứ hạng hàng ngày của hashtag. Trả về `null` nếu hashtag không đủ điều kiện thịnh hành trong ngày đó. |
| ↳↳ views_daily | integer | Số lượt xem video hàng ngày. Trả về `null` nếu lượt xem dưới 1.000. |
| ↳ audience_insights | object | Thông tin chi tiết về nhân khẩu học của khán giả xem video gắn hashtag này. Lưu ý: Trường này sẽ rỗng nếu `hashtag_status` là `OFFLINE` hoặc quy mô khán giả ước tính dưới 1.000. |
| ↳↳ audience_ages | object[] | Phân bố độ tuổi của khán giả xem video. |
| ↳↳↳ age | string | Nhóm độ tuổi. Các giá trị enum: `18-24`, `25-34`, `35+`. |
| ↳↳↳ percentage | number | Tỷ lệ phần trăm xấp xỉ của khán giả thuộc nhóm độ tuổi tương ứng (ví dụ: `0.3692` tức ~36.92%). |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/detail/?advertiser_id=7123456789012345678&discovery_type=HASHTAG&hashtag_id=4268426520694&country_code=US&date_range=7DAY' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/detail/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "discovery_type": "HASHTAG",
    "hashtag_id": "4268426520694",
    "country_code": "US",
    "date_range": "7DAY"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

hashtag_data = data.get("data", {})
print(f"Hashtag: #{hashtag_data.get('hashtag_name')} | Trạng thái: {hashtag_data.get('hashtag_status')}")
print(f"Tổng lượt xem: {hashtag_data.get('views')} | Video: {hashtag_data.get('posts')}")
for age_info in hashtag_data.get("audience_insights", {}).get("audience_ages", []):
    print(f"  - Độ tuổi {age_info.get('age')}: {age_info.get('percentage') * 100:.1f}%")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048D4E5F6",
    "data": {
        "hashtag_status": "ONLINE",
        "posts": 31927,
        "hashtag_id": "4268426520694",
        "audience_insights": {
            "audience_ages": [
                {
                    "percentage": 0.36926615840545485,
                    "age": "25-34"
                },
                {
                    "percentage": 0.3550167061571056,
                    "age": "18-24"
                },
                {
                    "percentage": 0.2757171047811277,
                    "age": "35+"
                }
            ]
        },
        "hashtag_name": "tattoo",
        "views_global_lifetime": 157770993216,
        "posts_global_lifetime": 12543346,
        "views": 216408760,
        "top_country_list": [
            "US",
            "MX",
            "BR",
            "VN",
            "ID"
        ],
        "trending_history": [
            {
                "date": "2026-04-06",
                "rank_position_daily": "85",
                "views_daily": 49419265
            },
            {
                "date": "2026-04-07",
                "rank_position_daily": "128",
                "views_daily": 45524768
            }
        ]
    }
}
```

---

## Lấy danh sách video thịnh hành liên quan đến hashtag (`Get trending videos related to hashtags`)
<a id="doc-1825119056527362"></a>
<!-- doc_id: 1825119056527362 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/video_list/`

**Mục đích**: Sử dụng endpoint này để lấy top 20 video thịnh hành nhất có sử dụng một hashtag phổ biến tại quốc gia hàng đầu và khoảng thời gian đã chọn. Các video này được xếp hạng dựa trên điểm số tổng hợp từ lượt xem, bình luận, lượt thích và lượt chia sẻ.

> [!NOTE]
> Trước khi gọi endpoint này, hãy gọi [/discovery/trending_list/](40-discovery.md#doc-1825119032526849) để lấy danh sách các hashtag phổ biến trên TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. Truyền một trong các ID được trả về qua trường `advertiser_ids` từ [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| discovery_type | string | Bắt buộc | Loại đối tượng khám phá. Giá trị enum: `HASHTAG` (video liên quan đến hashtag). |
| hashtag_ids | string[] | Bắt buộc | Danh sách các ID hashtag. Số lượng tối đa: 10 ID. Truyền một hoặc nhiều ID hashtag phổ biến nhận được qua trường `hashtag_id` từ [/discovery/trending_list/](40-discovery.md#doc-1825119032526849). Lưu ý: Truyền dưới dạng mảng chuỗi JSON trong query string (ví dụ: `["4268426520694"]`). |
| country_code | string | Không | Mã vị trí quốc gia/khu vực. Giá trị mặc định: `US`. Truyền một trong các mã vị trí được trả về qua trường `top_country_list` từ `/discovery/trending_list/`. |
| date_range | string | Không | Khoảng thời gian đo lường độ phổ biến của video. Giá trị mặc định: `7DAY`. Các giá trị enum: `1DAY`, `7DAY`, `30DAY`, `120DAY`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách video thịnh hành sử dụng các hashtag phổ biến. Mảng trả về tối đa top 20 video liên quan cho mỗi hashtag tại khu vực và khoảng thời gian đã chọn. |
| ↳↳ hashtag_id | string | ID của hashtag. |
| ↳↳ hashtag_name | string | Tên hashtag. |
| ↳↳ top_video_list | object[] | Danh sách các video thịnh hành nhất của hashtag. |
| ↳↳↳ video_id | string | Mã định danh duy nhất của video TikTok. |
| ↳↳↳ embed_url | string | Đường dẫn nhúng (embeddable link) của video TikTok. URL này có thể dùng để nhúng video vào website hoặc ứng dụng ngoài. Lưu ý: Nếu quyền riêng tư của video là "Bạn bè" hoặc "Chỉ mình tôi", video sẽ không thể xem qua đường dẫn này. |
| ↳↳↳ share_url | string | Đường dẫn chia sẻ (shareable URL) của video TikTok. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/video_list/?advertiser_id=7123456789012345678&discovery_type=HASHTAG&hashtag_ids=%5B%224268426520694%22%5D&country_code=US&date_range=7DAY' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests
import json

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/video_list/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "discovery_type": "HASHTAG",
    "hashtag_ids": json.dumps(["4268426520694"]),
    "country_code": "US",
    "date_range": "7DAY"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for hashtag_item in data.get("data", {}).get("list", []):
    print(f"Hashtag: #{hashtag_item.get('hashtag_name')}")
    for video in hashtag_item.get("top_video_list", [])[:3]:
        print(f"  - Video ID: {video.get('video_id')} | Share URL: {video.get('share_url')}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048A9B8C7",
    "data": {
        "list": [
            {
                "hashtag_id": "4268426520694",
                "hashtag_name": "relatable",
                "top_video_list": [
                    {
                        "video_id": "7198765432109876543",
                        "embed_url": "https://www.tiktok.com/embed/v2/7198765432109876543",
                        "share_url": "https://www.tiktok.com/@creator/video/7198765432109876543"
                    }
                ]
            }
        ]
    }
}
```


---

## Lấy danh sách bài hát thịnh hành từ Thư viện Âm nhạc Thương mại (`Get popular tracks from the Commercial Music Library`)
<a id="doc-1825119063013505"></a>
<!-- doc_id: 1825119063013505 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/cml/trending_list/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách tối đa 100 bản nhạc thịnh hành đã được cấp phép sẵn (pre-cleared) để sử dụng trong nội dung tự nhiên (organic) và tạo quảng cáo từ Thư viện Âm nhạc Thương mại (Commercial Music Library).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token được nhà sáng tạo TikTok ủy quyền. Để lấy access token, sử dụng endpoint [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | Mã định danh duy nhất riêng cho ứng dụng của tài khoản TikTok. Truyền giá trị của trường `open_id` được trả về trong phản hồi của [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| genre | string | Không | Thể loại âm nhạc cụ thể để lọc kết quả. Giá trị mặc định: `ALL`. Xem danh sách các giá trị thể loại được hỗ trợ bên dưới. |
| country_code | string | Không | Mã vị trí quốc gia/khu vực để lọc kết quả. Giá trị mặc định: `US`. Xem [Mã vị trí (Location code)](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| date_range | string | Không | Khoảng thời gian bài hát đạt độ thịnh hành. Giá trị mặc định: `7DAY`.<br>Các giá trị enum:<br>• `1DAY`: 1 ngày gần nhất.<br>• `7DAY`: 7 ngày gần nhất.<br>• `30DAY`: 30 ngày gần nhất.<br>• `90DAY`: 90 ngày gần nhất. |

### Danh sách các giá trị cho `genre`

| Giá trị enum | Tên thể loại (Tiếng Anh) | Mô tả thể loại |
|---|---|---|
| `ALL` | All | Tất cả các thể loại |
| `ROCK` | Rock | Nhạc Rock |
| `POP` | Pop | Nhạc Pop |
| `LATIN` | Latin | Nhạc Latin |
| `METAL` | Metal | Nhạc Metal |
| `ELECTRONIC` | Electronic | Nhạc điện tử (Electronic) |
| `HIP_HOP/RAP` | Hip Hop/Rap | Nhạc Hip Hop / Rap |
| `ALTERNATIVE/INDIE` | Alternative/Indie | Nhạc Alternative / Indie |
| `FOLK` | Folk | Nhạc dân gian / Folk |
| `R&B/SOUL` | R&B/Soul | Nhạc R&B / Soul |
| `COUNTRY` | Country | Nhạc đồng quê |
| `CLASSICAL` | Classical | Nhạc cổ điển |
| `JAZZ` | Jazz | Nhạc Jazz |
| `REGGAE` | Reggae | Nhạc Reggae |
| `CHILDHOOD` | Childhood | Nhạc thiếu nhi |
| `BLUES` | Blues | Nhạc Blues |
| `EASY_LISTENING` | Easy Listening | Nhạc êm dịu, dễ nghe |
| `NEW_AGE` | New Age | Nhạc New Age |
| `WORLD_MUSIC` | World Music | Âm nhạc thế giới |
| `EXPERIMENTAL` | Experimental | Nhạc thể nghiệm |
| `DEVOTIONAL` | Devotional | Nhạc tôn giáo / tâm linh |
| `CHINESE_TRADITION` | Chinese Tradition | Nhạc truyền thống Trung Hoa |
| `8_BIT` | 8 Bit | Nhạc 8-bit / chiptune |
| `A_CAPPELLA` | A capella | Hát mộc không nhạc đệm (A cappella) |
| `AFRO-POP` | Afro-Pop | Nhạc Pop Châu Phi |
| `ALTERNATIVE_HIP_HOP` | Alternative Hip Hop | Hip Hop thể nghiệm |
| `ALTERNATIVE_ROCK` | Alternative Rock | Rock Alternative |
| `AMBIENT` | Ambient | Nhạc Ambient không gian |
| `ARABIC_POP` | Arabic Pop | Pop Ả Rập |
| `BASS_HOUSE` | Bass House | Nhạc điện tử Bass House |
| `BGM` | BGM | Nhạc nền (Background Music) |
| `BOOMBAP` | Boombap | Hip Hop phong cách Boom Bap |
| `BOSSA_NOVA` | Bossa Nova | Nhạc Bossa Nova |
| `BRAZILIAN_FUNK_STYLE` | Brazilian Funk Style | Funk phong cách Brazil |
| `BUDDHIST_MUSIC` | Buddhist Music | Nhạc Phật giáo |
| `CANTOPOP` | Cantopop | Nhạc Pop tiếng Quảng Đông |
| `CELTIC_POP` | Celtic Pop | Nhạc Pop phong cách Celtic |
| `CHAMBER_MUSIC` | Chamber Music | Nhạc thính phòng |
| `CHILL_BEATS` | Chill Beats | Tiết tấu thư giãn |
| `CHILLOUT` | Chillout | Nhạc Chillout |
| `CHINESE_FOLK` | Chinese Folk | Dân ca Trung Quốc |
| `CHINESE_OPERA` | Chinese Opera | Kinh kịch Trung Hoa |
| `CHINESE_POP` | Chinese Pop | Nhạc Pop tiếng Hoa (Mandopop) |
| `CHINESE_STYLE` | Chinese Style | Nhạc phong cách cổ phong Trung Hoa |
| `CHINOISERIE_ELECTRONIC` | Chinoiserie Electronic | Điện tử phong cách Trung Hoa |
| `CHINOISERIE_RAP` | Chinoiserie Rap | Rap phong cách Trung Hoa |
| `CHRISTIAN_MUSIC` | Christian Music | Thánh ca / Nhạc Cơ Đốc |
| `CONTEMPORARY_R&B` | Contemporary R&B | R&B đương đại |
| `COUNTRY_POP` | Country Pop | Nhạc Pop đồng quê |
| `DANCE_POP` | Dance Pop | Nhạc Pop khiêu vũ |
| `DISCO` | Disco | Nhạc Disco |
| `DJ` | DJ | Nhạc phối DJ |
| `DRUM&BASS` | Drum&Bass | Nhạc Drum and Bass |
| `DUBSTEP` | Dubstep | Nhạc Dubstep |
| `EDM` | EDM | Nhạc nhảy điện tử (Electronic Dance Music) |
| `EDM_TRAP` | EDM Trap | Trap điện tử |
| `ELECTRO_POP` | Electro Pop | Nhạc Pop điện tử |
| `EPIC` | Epic | Nhạc hùng tráng điện ảnh |
| `FOLK_POP` | Folk Pop | Nhạc Folk Pop |
| `FUNK` | Funk | Nhạc Funk |
| `FUTURE_BASS` | Future Bass | Nhạc điện tử Future Bass |
| `GOSPEL` | Gospel | Nhạc Phúc âm |
| `GUFENG_MUSIC` | Gufeng Music | Nhạc cổ phong |
| `HARD_ROCK` | Hard Rock | Nhạc Hard Rock |
| `HIP_HOUSE` | Hip House | Nhạc Hip House |
| `HOLIDAY_MUSIC` | Holiday Music | Nhạc lễ hội / ngày lễ |
| `HOUSE` | House | Nhạc House |
| `INDIAN_POP` | Indian Pop | Nhạc Pop Ấn Độ |
| `INDIE_FOLK` | Indie Folk | Nhạc Indie Folk |
| `INDIE_POP` | Indie Pop | Nhạc Indie Pop |
| `INDIE_ROCK` | Indie Rock | Nhạc Indie Rock |
| `INSTRUMENTAL_HIP_HOP` | Instrumental Hip Hop | Hip Hop không lời |
| `INSTRUMENTAL_ROCK` | Instrumental Rock | Rock không lời |
| `IRISH_FOLK` | Irish Folk | Dân ca Ireland |
| `J_ROCK` | J-Rock | Nhạc Rock Nhật Bản |
| `JAPANESE_TRADITIONAL_MUSIC` | Japanese Traditional Music | Nhạc truyền thống Nhật Bản |
| `JAZZ_FUSION` | Jazz Fusion | Nhạc Jazz Fusion |
| `JAZZ_HIP_HOP` | Jazz Hip Hop | Nhạc Jazz kết hợp Hip Hop |
| `JAZZ_POP` | Jazz Pop | Nhạc Jazz Pop |
| `J-POP` | J-Pop | Nhạc Pop Nhật Bản |
| `K-POP` | K-Pop | Nhạc Pop Hàn Quốc |
| `LATIN_POP` | Latin Pop | Nhạc Latin Pop |
| `LO-FI` | Lo-fi | Nhạc Lo-fi thư giãn |
| `MC` | MC | Nhạc dẫn chương trình / MC |
| `NOISE` | Noise | Nhạc Noise thể nghiệm |
| `OLD_SCHOOL` | Old School | Nhạc phong cách Old School |
| `OTHERS` | Others | Các thể loại khác |
| `POP_RAP` | Pop Rap | Nhạc Pop kết hợp Rap |
| `POP_ROCK` | Pop Rock | Nhạc Pop Rock |
| `POP_SOUL` | Pop Soul | Nhạc Pop kết hợp Soul |
| `PSYCHEDELIC_ROCK` | Psychedelic Rock | Nhạc Rock ảo giác |
| `PUNK` | Punk | Nhạc Punk |
| `R&B_RAP` | R&B/Rap | Nhạc R&B kết hợp Rap |
| `REGGAETON` | Reggaeton | Nhạc Reggaeton |
| `RUSSIAN_POP` | Russian Pop | Nhạc Pop tiếng Nga |
| `SERTANEJO` | Sertanejo | Nhạc đồng quê Brazil |
| `SON_CUBANO` | Son Cubano | Nhạc truyền thống Cuba |
| `SOUL` | Soul | Nhạc Soul |
| `SOUNDTRACK` | Soundtrack | Nhạc phim / nhạc nền |
| `SYMPHONY` | Symphony | Nhạc giao hưởng |
| `SYNTH_POP` | Synth Pop | Nhạc Synth Pop |
| `TANGO` | Tango | Nhạc khiêu vũ Tango |
| `TECHNO` | Techno | Nhạc điện tử Techno |
| `TEEN_POP` | Teen Pop | Nhạc Pop thanh thiếu niên |
| `TRADITIONAL_CHINESE_FOLK` | Traditional Chinese Folk | Dân ca truyền thống Trung Hoa |
| `TRANCE` | Trance | Nhạc Trance |
| `TRAP_RAP` | Trap Rap | Nhạc Trap Rap |
| `TRIP_HOP` | Trip Hop | Nhạc Trip Hop |
| `TROPICAL_HOUSE` | Tropical House | Nhạc Tropical House |
| `TURKISH_POP` | Turkish Pop | Nhạc Pop Thổ Nhĩ Kỳ |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các bản nhạc thịnh hành. |
| ↳↳ commercial_music_id | string | ID của bài hát (ví dụ: `1234567890`). |
| ↳↳ commercial_music_name | string | Tên của bài hát. |
| ↳↳ duration | integer | Thời lượng bài hát tính bằng giây. Lưu ý: Đối với đoạn nhạc trích đoạn (clips) không phải toàn bộ bài nhạc, thời lượng có thể ghi nhận là `0`. |
| ↳↳ thumbnail_url | string | URL hình thu nhỏ (thumbnail) ảnh bìa của bài hát. |
| ↳↳ artist | string | Tên nghệ sĩ thể hiện bài hát. |
| ↳↳ preview_url | string | URL nghe thử đoạn nhạc. URL này không bao giờ hết hạn. |
| ↳↳ genres | string[] | Danh sách các thể loại âm nhạc của bài hát. |
| ↳↳ rank_position | string | Thứ hạng hiện tại của bài hát tại khu vực đã chọn (`country_code`) (ví dụ: `1`, `100`). |
| ↳↳ trending_history | object[] | Dữ liệu lịch sử thứ hạng của bài hát trong tối đa 30 ngày qua. |
| ↳↳↳ date | string | Ngày ghi nhận dữ liệu theo định dạng `YYYY-MM-DD`. |
| ↳↳↳ rank_position_daily | string | Thứ hạng hàng ngày của bài hát tại khu vực đã chọn. Giá trị sẽ là `NULL` nếu bài hát không đủ điều kiện thịnh hành trong ngày đó. |
| ↳↳ full_duration_song_clip | object | Thông tin chi tiết đoạn nhạc với thời lượng đầy đủ của bài hát. |
| ↳↳↳ preview_url | string | URL nghe thử của đoạn nhạc đầy đủ. URL không bao giờ hết hạn. |
| ↳↳↳ duration | integer | Thời lượng bài hát tính bằng giây. |
| ↳↳↳ song_clip_id | string | ID định danh đoạn nhạc. Giá trị này có thể truyền vào trường `music_sound_id` trong [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234). |
| ↳↳ trending_song_clip | object | Thông tin liên quan đến đoạn trích nhạc thịnh hành nhất trong 30 ngày qua. |
| ↳↳↳ preview_url | string | URL nghe thử đoạn trích nhạc thịnh hành. URL không hết hạn. |
| ↳↳↳ duration | integer | Thời lượng đoạn trích nhạc tính bằng giây. |
| ↳↳↳ song_clip_id | string | ID đoạn nhạc thịnh hành. Giá trị này có thể truyền vào trường `music_sound_id` trong [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234). |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/cml/trending_list/?business_id=open_id_example_123&genre=FOLK&country_code=US&date_range=7DAY' \
--header 'Access-Token: act.creator_token_example123'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.creator_token_example123"
BUSINESS_ID = "open_id_example_123"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/cml/trending_list/"

params = {
    "business_id": BUSINESS_ID,
    "genre": "FOLK",
    "country_code": "US",
    "date_range": "7DAY"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for track in data.get("data", {}).get("list", [])[:5]:
    print(f"Top {track.get('rank_position')}: {track.get('commercial_music_name')} - {track.get('artist')} | ID: {track.get('commercial_music_id')}")
    print(f"  - Preview: {track.get('preview_url')}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048F1E2D3",
    "data": {
        "list": [
            {
                "commercial_music_id": "7182938475610293847",
                "commercial_music_name": "Acoustic Breeze",
                "artist": "Soundscapes Studio",
                "duration": 123,
                "genres": [
                    "Folk"
                ],
                "preview_url": "https://sf16-ies-music-va.tiktokcdn.com/obj/ies-music-maliva/preview_7182938475610293847.mp3",
                "rank_position": "1",
                "thumbnail_url": "https://p16-va.tiktokcdn.com/img/tos-maliva-avt-0068/cover.jpeg",
                "trending_history": [
                    {
                        "date": "2026-04-06",
                        "rank_position_daily": "1"
                    },
                    {
                        "date": "2026-04-07",
                        "rank_position_daily": "1"
                    }
                ],
                "full_duration_song_clip": {
                    "song_clip_id": "7182938475610293847",
                    "duration": 123,
                    "preview_url": "https://sf16-ies-music-va.tiktokcdn.com/obj/ies-music-maliva/preview_7182938475610293847.mp3"
                },
                "trending_song_clip": {
                    "song_clip_id": "7182938475610293847_30s",
                    "duration": 30,
                    "preview_url": "https://sf16-ies-music-va.tiktokcdn.com/obj/ies-music-maliva/trending_7182938475610293847.mp3"
                }
            }
        ]
    }
}
```

---

## Lấy danh sách video thịnh hành liên quan đến bài hát (`Get trending videos related to tracks`)
<a id="doc-1825119068941314"></a>
<!-- doc_id: 1825119068941314 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/cml/video_list/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách top video thịnh hành nhất có sử dụng một bản nhạc thương mại phổ biến tại một quốc gia hoặc khu vực đã chọn.

> [!NOTE]
> Trước khi gọi endpoint này, hãy gọi [/discovery/cml/trending_list/](40-discovery.md#doc-1825119063013505) để lấy danh sách các bài hát thịnh hành từ Commercial Music Library kèm theo `commercial_music_id`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token được nhà sáng tạo TikTok ủy quyền. Để lấy access token, sử dụng endpoint [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | Mã định danh duy nhất riêng cho ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` từ phản hồi của [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| commercial_music_id | string | Bắt buộc | ID định danh của bài hát, nhận được qua `/discovery/cml/trending_list/`. |
| country_code | string | Không | Mã vị trí quốc gia/khu vực để lọc video. Giá trị mặc định: `US`. Xem [Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ commercial_music_id | string | ID định danh của bài hát. |
| ↳ commercial_music_name | string | Tên của bài hát. |
| ↳ top_video_list | object[] | Danh sách top 20 video thịnh hành nhất sử dụng bài hát này. |
| ↳↳ video_id | string | Mã định danh duy nhất của video TikTok. |
| ↳↳ embed_url | string | Đường dẫn nhúng (embeddable link) của video TikTok dùng để nhúng trên web hoặc ứng dụng. Lưu ý: Không hỗ trợ xem nếu video đặt chế độ riêng tư "Bạn bè" hoặc "Chỉ mình tôi". |
| ↳↳ share_url | string | Đường dẫn chia sẻ (shareable URL) của video TikTok. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/cml/video_list/?business_id=open_id_example_123&commercial_music_id=7182938475610293847&country_code=US' \
--header 'Access-Token: act.creator_token_example123'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.creator_token_example123"
BUSINESS_ID = "open_id_example_123"
COMMERCIAL_MUSIC_ID = "7182938475610293847"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/cml/video_list/"

params = {
    "business_id": BUSINESS_ID,
    "commercial_music_id": COMMERCIAL_MUSIC_ID,
    "country_code": "US"
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

music_data = data.get("data", {})
print(f"Bài hát: {music_data.get('commercial_music_name')} (ID: {music_data.get('commercial_music_id')})")
for video in music_data.get("top_video_list", [])[:3]:
    print(f"  - Video ID: {video.get('video_id')} | Share: {video.get('share_url')}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048C3D4E5",
    "data": {
        "commercial_music_id": "7182938475610293847",
        "commercial_music_name": "Acoustic Breeze",
        "top_video_list": [
            {
                "video_id": "7198765432109876543",
                "embed_url": "https://www.tiktok.com/embed/v2/7198765432109876543",
                "share_url": "https://www.tiktok.com/@creator/video/7198765432109876543"
            }
        ]
    }
}
```

---

## Lấy từ khóa tìm kiếm thịnh hành (`Get trending search keywords`)
<a id="doc-1832798345014338"></a>
<!-- doc_id: 1832798345014338 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/`

**Mục đích**: Sử dụng endpoint này để lấy top 20 từ khóa tìm kiếm đang thịnh hành trên TikTok hoặc các từ khóa tìm kiếm được cá nhân hóa cho tài khoản TikTok của bạn.

### Điều kiện tiên quyết trước khi bắt đầu

> [!IMPORTANT]
> 1. **Quyền truy cập**: Lấy access token tài khoản TikTok có phạm vi quyền `discovery.search.words` và mã định danh duy nhất của ứng dụng cho tài khoản TikTok theo quy trình [Ủy quyền (Authorization)](../10-organic-api/accounts-api.md#doc-1738083939371009) và [Xác thực (Authentication)](../10-organic-api/accounts-api.md#doc-1738084387220481).
>    - Để kiểm tra xem token đã có quyền `discovery.search.words` hay chưa, sử dụng [/tt_user/token_info/get/](01-accounts-p1.md#doc-1765927978092545) và kiểm tra trường `scope` trả về. Nếu chưa có, yêu cầu chủ tài khoản phê duyệt quyền **"Query for recommended search terms based on trends or specific keywords"**.
> 2. **Cấp độ tài khoản**: Đảm bảo tài khoản TikTok là tài khoản có quyền truy cập nâng cao (TikTok Account with Advanced Access) hoặc Tài khoản doanh nghiệp đã xác minh (Verified Business Account). Để kiểm tra, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và xác nhận tham số `has_advanced_access` có giá trị `true`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token được tài khoản TikTok ủy quyền. Để lấy token ngắn hạn, dùng endpoint [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | Mã định danh duy nhất riêng cho ứng dụng của tài khoản TikTok. Truyền giá trị của trường `open_id` trong phản hồi của [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| is_personalized | boolean | Không | Có trả về từ khóa tìm kiếm được cá nhân hóa cho tài khoản TikTok hay không. Giá trị hỗ trợ:<br>• `true`: Trả về các từ khóa thịnh hành được cá nhân hóa riêng cho tài khoản TikTok.<br>• `false`: Trả về các từ khóa thịnh hành chung trên toàn hệ thống.<br>Giá trị mặc định: `false`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ search_keywords | string[] | Danh sách 20 từ khóa tìm kiếm đang thịnh hành. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/?business_id=open_id_example_123&is_personalized=false' \
--header 'Access-Token: act.creator_token_example123'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.creator_token_example123"
BUSINESS_ID = "open_id_example_123"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/"

params = {
    "business_id": BUSINESS_ID,
    "is_personalized": False
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

keywords = data.get("data", {}).get("search_keywords", [])
print(f"Top {len(keywords)} từ khóa tìm kiếm thịnh hành:")
for idx, kw in enumerate(keywords, 1):
    print(f"  {idx}. {kw}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048D5E6F7",
    "data": {
        "search_keywords": [
            "summer outfit ideas",
            "easy dinner recipes",
            "home workout routine",
            "skincare tips",
            "travel hacks 2026"
        ]
    }
}
```

---

## Lấy từ khóa tìm kiếm được đề xuất (`Get recommended search keywords`)
<a id="doc-1832798361818114"></a>
<!-- doc_id: 1832798361818114 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/keyword/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách 20 từ khóa tìm kiếm được đề xuất dựa trên một truy vấn tìm kiếm cụ thể (query) hoặc lấy các từ khóa đề xuất được cá nhân hóa cho tài khoản TikTok của bạn.

### Điều kiện tiên quyết trước khi bắt đầu

> [!IMPORTANT]
> 1. **Quyền hạn**: Access token tài khoản TikTok phải có scope `discovery.search.words` và mã `business_id` (open_id). Kiểm tra qua [/tt_user/token_info/get/](01-accounts-p1.md#doc-1765927978092545). Nếu thiếu, yêu cầu phê duyệt quyền **"Query for recommended search terms based on trends or specific keywords"**.
> 2. **Tài khoản**: Đảm bảo tài khoản TikTok là TikTok Account with Advanced Access hoặc Verified Business Account (tham số `has_advanced_access = true` trong [/business/get/](01-accounts-p1.md#doc-1762228399168514)).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token được tài khoản TikTok ủy quyền. Để lấy access token ngắn hạn, dùng endpoint [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

### Tham số (Query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | Mã định danh duy nhất riêng cho ứng dụng của tài khoản TikTok. Truyền giá trị của trường `open_id` trong phản hồi của [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| query | string | Bắt buộc | Truy vấn tìm kiếm gốc. Bạn có thể chỉ định tên sản phẩm, dịch vụ hoặc thương hiệu làm từ khóa truy vấn. Giới hạn độ dài: tối đa 255 ký tự. |
| is_personalized | boolean | Không | Có trả về từ khóa tìm kiếm đề xuất được cá nhân hóa hay không. Giá trị hỗ trợ:<br>• `true`: Trả về từ khóa đề xuất được cá nhân hóa.<br>• `false`: Trả về từ khóa đề xuất phổ biến chung.<br>Giá trị mặc định: `false`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ search_keywords | string[] | Danh sách 20 từ khóa tìm kiếm được đề xuất dựa trên truy vấn. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/keyword/?business_id=open_id_example_123&query=coffee&is_personalized=false' \
--header 'Access-Token: act.creator_token_example123'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.creator_token_example123"
BUSINESS_ID = "open_id_example_123"
url = "https://business-api.tiktok.com/open_api/v1.3/discovery/trending/search/keyword/"

params = {
    "business_id": BUSINESS_ID,
    "query": "coffee",
    "is_personalized": False
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

keywords = data.get("data", {}).get("search_keywords", [])
print(f"Từ khóa đề xuất cho 'coffee':")
for idx, kw in enumerate(keywords, 1):
    print(f"  {idx}. {kw}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048E6F7A8",
    "data": {
        "search_keywords": [
            "coffee brewing methods",
            "best iced coffee recipe",
            "aesthetic coffee shop vlog",
            "latte art tutorial",
            "cold brew vs iced coffee"
        ]
    }
}
```
