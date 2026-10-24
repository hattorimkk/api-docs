"""
Server Tiếp Nhận Webhook Shopee Push Mechanism (Webhook Receiver)
==================================================================
Hỗ trợ:
- Tiếp nhận HTTP POST callback từ Shopee Open Platform
- Đọc raw body chính xác (không bị format lại JSON)
- Xác thực chữ ký số Authorization header bằng HMAC-SHA256
- Định tuyến và xử lý các loại sự kiện (Code 1, 2, 3, 4, 6, 8, 10,...)
"""

import hmac
import hashlib
import json
import logging
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ShopeeWebhookServer")

PARTNER_KEY = os.getenv("SHOPEE_PARTNER_KEY", "your_partner_key_here")
CALLBACK_URL = os.getenv("SHOPEE_CALLBACK_URL", "https://your-domain.com/webhook/shopee")


def verify_shopee_push(url: str, request_body: bytes, partner_key: str, auth_header: str) -> bool:
    """
    Xác thực chữ ký Shopee Push Mechanism.
    Công thức: HMAC_SHA256(URL + "|" + raw_body, partner_key)
    """
    base_string = url.encode("utf-8") + b"|" + request_body
    calculated_sign = hmac.new(partner_key.encode("utf-8"), base_string, hashlib.sha256).hexdigest()
    return hmac.compare_digest(calculated_sign.lower(), auth_header.lower())


class ShopeeWebhookHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # 1. Đọc header Authorization
        auth_header = self.headers.get("Authorization", "")
        content_length = int(self.headers.get("Content-Length", 0))

        # 2. Đọc raw body (dạng bytes nguyên bản)
        raw_body = self.rfile.read(content_length)

        # 3. Xác thực tính hợp lệ của request
        # Lưu ý: URL dùng để verify phải khớp với URL cấu hình trong Shopee Open Platform Console
        target_url = CALLBACK_URL
        if PARTNER_KEY != "your_partner_key_here" and auth_header:
            is_valid = verify_shopee_push(
                url=target_url,
                request_body=raw_body,
                partner_key=PARTNER_KEY,
                auth_header=auth_header,
            )
            if not is_valid:
                logger.warning("Cảnh báo: Chữ ký Authorization không hợp lệ!")
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'{"error": "invalid_signature"}')
                return

        # 4. Phân tích nội dung sự kiện
        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception as e:
            logger.error(f"Không thể phân tích JSON body: {e}")
            self.send_response(400)
            self.end_headers()
            return

        code = payload.get("code")
        shop_id = payload.get("shop_id")
        timestamp = payload.get("timestamp")
        data = payload.get("data", {})

        logger.info(f"==> Nhận Push Event [Code {code}] từ Shop {shop_id} lúc {timestamp}")

        # 5. Xử lý từng mã sự kiện
        if code == 1:
            logger.info(f"[Shop Authorized] Shop {shop_id} đã ủy quyền thành công cho ứng dụng.")
        elif code == 2:
            logger.warning(f"[Shop Deauthorized] Shop {shop_id} đã hủy ủy quyền ứng dụng!")
        elif code == 3:
            # Sự kiện trạng thái đơn hàng thay đổi
            ordersn = data.get("ordersn")
            status = data.get("status")
            update_time = data.get("update_time")
            logger.info(f"[Order Status Changed] Đơn hàng: {ordersn} | Trạng thái mới: {status} | Lúc: {update_time}")
            # GỌI HÀM CẬP NHẬT DATABASE CỦA BẠN TẠI ĐÂY
        elif code == 4:
            # Sự kiện mã vận đơn thay đổi
            ordersn = data.get("ordersn")
            tracking_no = data.get("tracking_no")
            logger.info(f"[Tracking Update] Đơn hàng {ordersn} đã có mã vận đơn: {tracking_no}")
        elif code == 6:
            # Sản phẩm bị khóa / vi phạm
            item_id = data.get("item_id")
            logger.warning(f"[Banned Item] Sản phẩm {item_id} đã bị Shopee tạm khóa hoặc vi phạm chính sách!")
        elif code == 8:
            # Thay đổi lượng tồn kho dự trữ flash sale
            item_id = data.get("item_id")
            logger.info(f"[Reserved Stock] Tồn kho dự trữ thay đổi cho sản phẩm {item_id}")
        else:
            logger.info(f"[Other Event] Sự kiện Code {code}: {data}")

        # 6. Luôn phản hồi HTTP 200 OK kèm JSON rỗng để xác nhận đã nhận
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b"{}")

    def do_GET(self):
        """Điểm kiểm tra trạng thái máy chủ (Health check)."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Máy chủ Shopee Webhook đang hoạt động bình thường.".encode("utf-8"))


def run_server(port: int = 8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, ShopeeWebhookHandler)
    logger.info(f"Shopee Webhook Server đang lắng nghe tại cổng {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Đang dừng server...")
        httpd.server_close()


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    run_server(port)

