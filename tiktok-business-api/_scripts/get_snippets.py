import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

from test_engine import new_text

parts = new_text.split("```")
prose = "\n".join([parts[i] for i in range(0, len(parts), 2)])

def find_snippet(keyword, length=1200):
    idx = prose.find(keyword)
    if idx != -1:
        print(f"=== SNIPPET FOR: {keyword} ===")
        print(prose[idx:idx+length])
        print("\n" + "="*50 + "\n")

find_snippet("Tối ưu hóa và Đấu thầu · Mục tiêu (Goal)")
find_snippet("Tối ưu hóa và Đấu thầu · Chiến lược giá thầu, *(Không bắt buộc)* CPA mục tiêu")
find_snippet("Tài sản sáng tạo · Tự động chọn từ danh mục\nAny of the following options:")
