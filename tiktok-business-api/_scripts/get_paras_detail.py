import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

from test_engine import new_text

parts = new_text.split("```")
prose = "\n".join([parts[i] for i in range(0, len(parts), 2)])

def print_exact(start_kw, end_kw):
    idx1 = prose.find(start_kw)
    if idx1 == -1:
        print(f"NOT FOUND: {start_kw}")
        return
    idx2 = prose.find(end_kw, idx1)
    if idx2 == -1:
        idx2 = idx1 + 1000
    print(f"=== {start_kw} ===")
    print(prose[idx1:idx2+len(end_kw)])
    print("\n" + "="*50 + "\n")

print_exact("| TikTok Shop | Chỉ định một TikTok Shop khả dụng cho Chiến dịch GMV Max", "|---")
print_exact("Điểm đến chuyển hướng (Destination)\n• If optimization goal is specified as Follow", "call_to_action_id")
print_exact("> **Important:** \n> - **Upgraded Smart+ API**:", "endpoints](../12-api-reference/62-upgraded-smartplus-p1.md")
print_exact("Tối ưu hóa và Đấu thầu · Sự kiện · Sự kiện tối ưu hóa\n• Bắt buộc khi Goal is Conversion", "campaign.")
print_exact("Select your Instant messaging app or use a customized URL", "phone_number")
