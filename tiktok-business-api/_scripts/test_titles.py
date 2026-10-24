# Verify all 56 doc_ids
DOC_TITLES = {
    "1874421347053569": ("Tạo quảng cáo danh mục chung trên web Upgraded Smart+", "Create Upgraded Smart+ Web Generic Catalog Ads"),
    "1843324498993154": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+", "Create Upgraded Smart+ Lead Generation Campaigns"),
    "1843324592169986": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Biểu mẫu tức thì", "Create an Upgraded Smart+ Lead Generation Campaign with Location as Instant Form"),
    "1843324606213121": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Trang web", "Create an Upgraded Smart+ Lead Generation Campaign with Location as Website"),
    "1847302969710913": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Tin nhắn trực tiếp TikTok", "Create an Upgraded Smart+ Lead Generation Campaign with optimization location as TikTok direct messages"),
    "1847302988449921": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Ứng dụng nhắn tin tức thì", "Create an Upgraded Smart+ Lead Generation Campaign with optimization location as instant messaging apps"),
    "1847302998941697": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Cuộc gọi điện thoại", "Create an Upgraded Smart+ Lead Generation Campaign with optimization location as phone call"),
    "1876685025962241": ("Tạo chiến dịch tìm kiếm khách hàng tiềm năng Upgraded Smart+ với nhiều vị trí tối ưu hóa", "Create an Upgraded Smart+ Lead Generation Campaign with multiple location selection"),
    "1843324618421314": ("Tạo quảng cáo ô tô Upgraded Smart+", "Create Upgraded Smart+ Automotive Ads"),
    "1843325008693250": ("Tạo quảng cáo ô tô Upgraded Smart+ theo kho hàng", "Create Upgraded Smart+ Automotive Ads for Inventory"),
    "1843325022799873": ("Tạo quảng cáo ô tô Upgraded Smart+ theo dòng xe", "Create Upgraded Smart+ Automotive Ads for Models"),
    "1874421377372161": ("Tạo quảng cáo danh mục chung tìm kiếm khách hàng tiềm năng Upgraded Smart+", "Create Upgraded Smart+ Lead Generic Catalog Ads"),
    "1847303035303106": ("Tạo quảng cáo danh mục Upgraded Smart+ cho ứng dụng", "Create Upgraded Smart+ Catalog Ads for App"),
    "1854746404386113": ("Tạo quảng cáo Upgraded Smart+ tối ưu hóa cho cả Trang web và Ứng dụng", "Create Upgraded Smart+ Ads with Website and App Optimization"),
    "1855007137120578": ("Tạo quảng cáo danh mục Upgraded Smart+ tối ưu hóa cho cả Trang web và Ứng dụng", "Create Upgraded Smart+ Catalog Ads with Website and App Optimization"),
    "1855007163018689": ("Tạo quảng cáo không danh mục Upgraded Smart+ tối ưu hóa cho cả Trang web và Ứng dụng", "Create Upgraded Smart+ Non-Catalog Ads with Website and App Optimization"),
    "1873144295333889": ("Tạo chiến dịch quảng cáo tìm kiếm Upgraded Smart+", "Create Upgraded Smart+ Search Ads Campaigns"),
    "1873147546166737": ("Tạo chiến dịch quảng cáo tìm kiếm quảng bá ứng dụng Upgraded Smart+", "Create an Upgraded Smart+ App Promotion Search Ads Campaign"),
    "1873147575660753": ("Tạo chiến dịch quảng cáo tìm kiếm ứng dụng non-DC Upgraded Smart+", "Create an Upgraded Smart+ non-DC App Search Ads Campaign"),
    "1873147588534657": ("Tạo chiến dịch quảng cáo tìm kiếm ứng dụng DC Upgraded Smart+", "Create an Upgraded Smart+ DC App Search Ads Campaign"),
    "1873147560720593": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign"),
    "1873147602825601": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Biểu mẫu tức thì", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign with optimization location as Instant Form"),
    "1873147614281746": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Trang web", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign with optimization location as Website"),
    "1873147628169218": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Tin nhắn trực tiếp TikTok", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign with optimization location as TikTok direct messages"),
    "1873147640065409": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Ứng dụng nhắn tin tức thì", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign with optimization location as instant messaging apps"),
    "1873147653815745": ("Tạo chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí là Cuộc gọi điện thoại", "Create an Upgraded Smart+ Lead Generation Search Ads Campaign with optimization location as phone call"),
    "1873147670578193": ("Tạo quảng cáo tìm kiếm ô tô Upgraded Smart+", "Create Upgraded Smart+ Automotive Search Ads"),
    "1873147685889425": ("Tạo quảng cáo tìm kiếm ô tô Upgraded Smart+ theo kho hàng", "Create Upgraded Smart+ Automotive Search Ads for Inventory"),
    "1873147699663874": ("Tạo quảng cáo tìm kiếm ô tô Upgraded Smart+ theo dòng xe", "Create Upgraded Smart+ Automotive Search Ads for Models"),
    "1875743103825537": ("Tạo chiến dịch quảng cáo tìm kiếm bán hàng Upgraded Smart+", "Create an Upgraded Smart+ Sales Search Ads Campaign"),
    "1875743211659265": ("Tạo chiến dịch quảng cáo tìm kiếm Upgraded Smart+ cho Web", "Create an Upgraded Smart+ Search Ads Campaign for Web"),
    "1875743288255489": ("Tạo chiến dịch quảng cáo tìm kiếm không danh mục Upgraded Smart+ cho Web", "Create an Upgraded Smart+ Non-Catalog Search Ads Campaign for Web"),
    "1875743291988242": ("Tạo chiến dịch quảng cáo tìm kiếm thương mại điện tử Upgraded Smart+ cho Web", "Create an Upgraded Smart+ E-commerce Search Ads Campaign for Web"),
    "1875743295409170": ("Tạo chiến dịch quảng cáo tìm kiếm du lịch Upgraded Smart+ cho Web", "Create an Upgraded Smart+ Travel Search Ads Campaign for Web"),
    "1875743331398673": ("Tạo chiến dịch quảng cáo tìm kiếm truyền phát trực tuyến Upgraded Smart+ cho Web", "Create an Upgraded Smart+ Streaming Search Ads Campaign for Web"),
    "1875743215419394": ("Tạo chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho Ứng dụng", "Create an Upgraded Smart+ Catalog Search Ads Campaign for App"),
    "1875743384633345": ("Tạo chiến dịch quảng cáo tìm kiếm thương mại điện tử Upgraded Smart+ cho Ứng dụng", "Create an Upgraded Smart+ E-commerce Search Ads Campaign for App"),
    "1875743388430337": ("Tạo chiến dịch quảng cáo tìm kiếm du lịch Upgraded Smart+ cho Ứng dụng", "Create an Upgraded Smart+ Travel Search Ads Campaign for App"),
    "1875743392271362": ("Tạo chiến dịch quảng cáo tìm kiếm truyền phát trực tuyến Upgraded Smart+ cho Ứng dụng", "Create an Upgraded Smart+ Streaming Search Ads Campaign for App"),
    "1875743219104321": ("Tạo chiến dịch quảng cáo tìm kiếm Upgraded Smart+ cho cả Trang web và Ứng dụng", "Create an Upgraded Smart+ Search Ads Campaign for Website and App"),
    "1875743454192641": ("Tạo chiến dịch quảng cáo tìm kiếm không danh mục Upgraded Smart+ cho cả Trang web và Ứng dụng", "Create an Upgraded Smart+ Non-Catalog Search Ads Campaign for Website and App"),
    "1875743457587714": ("Tạo chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho cả Trang web và Ứng dụng", "Create an Upgraded Smart+ Catalog Search Ads Campaign for Website and App"),
    "1780164603696130": ("Tạo quảng cáo tìm kiếm", "Create Search Ads"),
    "1815394136739841": ("Tạo chiến dịch quảng cáo tìm kiếm thủ công", "Create Manual Search Ads Campaigns"),
    "1839876593708034": ("Tạo quảng cáo tối ưu hóa cho cả Trang web và Ứng dụng", "Create ads with Website and App Optimization"),
    "1839882947475458": ("Tạo quảng cáo danh mục thủ công tối ưu hóa cho cả Trang web và Ứng dụng", "Create Manual Catalog Ads with Website and App Optimization"),
    "1839882969587906": ("Tạo quảng cáo không danh mục thủ công tối ưu hóa cho cả Trang web và Ứng dụng", "Create Manual Non-Catalog Ads with Website and App Optimization"),
    "1842232769643905": ("Tạo quảng cáo danh mục Smart+ tối ưu hóa cho cả Trang web và Ứng dụng", "Create Smart+ Catalog Ads with Website and App Optimization"),
    "1777633230937090": ("Tạo quảng cáo hình ảnh đơn", "Create single image ads"),
    "1766217791987713": ("Tạo quảng cáo xoay vòng (Carousel Ads)", "Create Carousel Ads"),
    "1739470744631298": ("Tạo quảng cáo Spark Ads", "Create Spark Ads"),
    "1848048566169730": ("Chuyển đổi sang Spark Ads", "Migrate to Spark Ads"),
    "1797011827608577": ("Tạo chiến dịch chuyên dụng nâng cao", "Create Advanced Dedicated Campaigns"),
    "1738963942132738": ("(Không còn hỗ trợ) Tạo quảng cáo bộ sưu tập (Collection Ads)", "(Deprecated) Create Collection ads"),
    "1739470724723714": ("(Không còn hỗ trợ) Tạo Dynamic Showcase Ads", "(Deprecated) Create Dynamic Showcase Ads"),
    "1739470947488770": ("(Không còn hỗ trợ) Tạo Dynamic Showcase Ads chi tiết", "(Deprecated) Create Dynamic Showcase Ads"),
}

import json
units = json.load(open('tiktok-business-api/_work/units.json'))
u102 = [u for u in units if u['unit_id'] == 'u102'][0]
doc_ids = u102['doc_ids']

print(f"Total doc_ids in u102: {len(doc_ids)}")
print(f"Total in DOC_TITLES: {len(DOC_TITLES)}")
diff = set(doc_ids) ^ set(DOC_TITLES.keys())
print("Difference:", diff)
