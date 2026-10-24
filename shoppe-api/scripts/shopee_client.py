"""
Bộ Thư Viện SDK Kết Nối Shopee Open Platform API v2
===================================================
Module chính thức hỗ trợ kết nối, xác thực chữ ký HMAC-SHA256,
quản lý token và gọi các API Shopee Open Platform v2.
"""

import hmac
import hashlib
import time
import json
import logging
from typing import Dict, Any, Optional, List
import urllib.request
import urllib.parse
import urllib.error

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ShopeeClient")


class ShopeeClient:
    """
    Client tương tác với Shopee Open Platform API v2.
    
    Hỗ trợ:
    - Tự động sinh timestamp và chữ ký HMAC-SHA256 (sign)
    - Phân biệt Public API, Shop API và Merchant API
    - Tự động kiểm tra thời hạn và làm mới Access Token (Token Rotation)
    - Tự động retry khi gặp lỗi tạm thời hoặc hết hạn token
    """

    LIVE_BASE_URL = "https://partner.shopeemobile.com"
    TEST_BASE_URL = "https://partner.test-stable.shopeemobile.com"

    def __init__(
        self,
        partner_id: int,
        partner_key: str,
        shop_id: Optional[int] = None,
        merchant_id: Optional[int] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        token_expires_at: Optional[float] = None,
        sandbox: bool = False,
    ):
        """
        Khởi tạo Shopee Client.
        
        :param partner_id: ID ứng dụng (Partner ID) được cấp từ Shopee Console
        :param partner_key: Secret key (Partner Key) dùng để băm HMAC-SHA256
        :param shop_id: ID của gian hàng (Shop ID) cần thao tác
        :param merchant_id: ID tài khoản tổng CNSC (nếu là Merchant Cross-Border)
        :param access_token: Token truy cập (có hạn 4 giờ)
        :param refresh_token: Token làm mới (có hạn 30 ngày)
        :param token_expires_at: Thời điểm hết hạn của access_token (Unix timestamp)
        :param sandbox: True nếu chạy ở môi trường Test-Stable (Sandbox), False nếu chạy Live
        """
        self.partner_id = int(partner_id)
        self.partner_key = str(partner_key)
        self.shop_id = int(shop_id) if shop_id is not None else None
        self.merchant_id = int(merchant_id) if merchant_id is not None else None
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expires_at = token_expires_at or 0.0
        self.base_url = self.TEST_BASE_URL if sandbox else self.LIVE_BASE_URL
        if HAS_REQUESTS:
            self.session = requests.Session()
        else:
            self.session = None

    def _send_http(self, method: str, url: str, params: Optional[Dict[str, Any]] = None, json_data: Optional[Dict[str, Any]] = None, timeout: int = 30) -> Dict[str, Any]:
        """Gửi request bằng requests hoặc fallback sang urllib."""
        if params:
            query_str = urllib.parse.urlencode(params)
            url = f"{url}?{query_str}"

        if HAS_REQUESTS and self.session:
            req_kwargs: Dict[str, Any] = {"headers": {"Content-Type": "application/json"}, "timeout": timeout}
            if json_data is not None:
                req_kwargs["json"] = json_data
            resp = self.session.request(method, url, **req_kwargs)
            try:
                return resp.json()
            except Exception:
                raise Exception(f"Shopee API trả về nội dung không phải JSON (HTTP {resp.status_code}): {resp.text}")
        else:
            data_bytes = json.dumps(json_data).encode("utf-8") if json_data is not None else None
            req = urllib.request.Request(url, data=data_bytes, headers={"Content-Type": "application/json"}, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    body = response.read().decode("utf-8")
                    return json.loads(body)
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8")
                try:
                    return json.loads(body)
                except Exception:
                    raise Exception(f"Shopee API HTTP Error {e.code}: {body}")
            except Exception as e:
                raise Exception(f"Lỗi kết nối Shopee API: {e}")

    def generate_sign(
        self,
        api_path: str,
        timestamp: int,
        access_token: Optional[str] = None,
        shop_id: Optional[int] = None,
        merchant_id: Optional[int] = None,
    ) -> str:
        """
        Tạo chữ ký số `sign` bằng thuật toán HMAC-SHA256 theo đúng chuẩn Shopee v2.
        
        Quy tắc ghép chuỗi base string:
        - Public API: partner_id + api_path + timestamp
        - Shop API: partner_id + api_path + timestamp + access_token + shop_id
        - Merchant API: partner_id + api_path + timestamp + access_token + merchant_id
        """
        base_string = f"{self.partner_id}{api_path}{timestamp}"

        if access_token:
            base_string += f"{access_token}"
            if shop_id is not None:
                base_string += f"{shop_id}"
            elif merchant_id is not None:
                base_string += f"{merchant_id}"

        signature = hmac.new(
            self.partner_key.encode("utf-8"),
            base_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return signature

    def get_auth_link(self, redirect_url: str) -> str:
        """
        Tạo đường link ủy quyền Shop để người bán truy cập trên trình duyệt.
        Sau khi người bán đồng ý, Shopee sẽ chuyển hướng về `redirect_url` kèm theo `code` và `shop_id`.
        """
        api_path = "/api/v2/shop/auth_partner"
        timestamp = int(time.time())
        sign = self.generate_sign(api_path=api_path, timestamp=timestamp)
        
        from urllib.parse import urlencode
        query_params = {
            "partner_id": self.partner_id,
            "timestamp": timestamp,
            "sign": sign,
            "redirect": redirect_url,
        }
        return f"{self.base_url}{api_path}?{urlencode(query_params)}"

    def get_access_token_by_code(self, code: str, shop_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Đổi Authorization Code lấy Access Token và Refresh Token lần đầu.
        
        Endpoint: POST /api/v2/auth/token/get
        """
        target_shop_id = shop_id or self.shop_id
        if not target_shop_id:
            raise ValueError("Cần cung cấp shop_id để lấy access token.")

        api_path = "/api/v2/auth/token/get"
        timestamp = int(time.time())
        sign = self.generate_sign(api_path=api_path, timestamp=timestamp)

        params = {
            "partner_id": self.partner_id,
            "timestamp": timestamp,
            "sign": sign,
        }

        payload = {
            "code": code,
            "partner_id": self.partner_id,
            "shop_id": int(target_shop_id),
        }

        url = f"{self.base_url}{api_path}"
        data = self._send_http("POST", url, params=params, json_data=payload, timeout=15)

        if data.get("error"):
            logger.error(f"Lỗi khi lấy access token: {data}")
            raise Exception(f"Shopee API Error: {data.get('message')} (Code: {data.get('error')})")

        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")
        expires_in = data.get("expire_in", 14400)
        self.token_expires_at = time.time() + expires_in
        self.shop_id = target_shop_id

        logger.info(f"Lấy Access Token thành công cho shop {self.shop_id}. Hết hạn sau {expires_in}s.")
        return data

    def refresh_access_token(self) -> Dict[str, Any]:
        """
        Làm mới Access Token bằng Refresh Token (Token Rotation).
        Shopee trả về Access Token mới VÀ Refresh Token mới.
        
        Endpoint: POST /api/v2/auth/access_token/get
        """
        if not self.refresh_token or not self.shop_id:
            raise ValueError("Không có refresh_token hoặc shop_id để thực hiện làm mới token.")

        api_path = "/api/v2/auth/access_token/get"
        timestamp = int(time.time())
        sign = self.generate_sign(api_path=api_path, timestamp=timestamp)

        params = {
            "partner_id": self.partner_id,
            "timestamp": timestamp,
            "sign": sign,
        }

        payload = {
            "refresh_token": self.refresh_token,
            "partner_id": self.partner_id,
            "shop_id": int(self.shop_id),
        }

        url = f"{self.base_url}{api_path}"
        data = self._send_http("POST", url, params=params, json_data=payload, timeout=15)

        if data.get("error"):
            logger.error(f"Lỗi khi làm mới token: {data}")
            raise Exception(f"Shopee Refresh Token Error: {data.get('message')} (Code: {data.get('error')})")

        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")
        expires_in = data.get("expire_in", 14400)
        self.token_expires_at = time.time() + expires_in

        logger.info(f"Làm mới token thành công cho shop {self.shop_id}. Hạn mới: {expires_in}s.")
        return data

    def _ensure_valid_token(self):
        """Tự động kiểm tra thời hạn token. Nếu còn dưới 5 phút, tự động refresh."""
        if self.access_token and self.refresh_token:
            remaining = self.token_expires_at - time.time()
            if remaining < 300:  # Còn dưới 5 phút
                logger.info(f"Access token sắp hết hạn (còn {int(remaining)}s). Đang làm mới...")
                self.refresh_access_token()

    def request(
        self,
        method: str,
        api_path: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        is_public: bool = False,
        retry_on_token_error: bool = True,
    ) -> Dict[str, Any]:
        """
        Thực hiện một yêu cầu HTTP đến Shopee API v2.
        
        Tự động tính toán các tham số bắt buộc trong URL query:
        - partner_id
        - timestamp
        - access_token (nếu không phải public API)
        - shop_id hoặc merchant_id (nếu không phải public API)
        - sign
        """
        method = method.upper()
        if not is_public:
            self._ensure_valid_token()

        timestamp = int(time.time())
        query_params = params.copy() if params else {}

        # Gán các query chuẩn
        query_params["partner_id"] = self.partner_id
        query_params["timestamp"] = timestamp

        if not is_public:
            if not self.access_token:
                raise ValueError("Cần có access_token để gọi API Shop/Merchant.")
            query_params["access_token"] = self.access_token

            if self.shop_id is not None:
                query_params["shop_id"] = self.shop_id
            elif self.merchant_id is not None:
                query_params["merchant_id"] = self.merchant_id

        # Tạo chữ ký sign
        token_for_sign = None if is_public else self.access_token
        shop_id_for_sign = None if is_public else self.shop_id
        merchant_id_for_sign = None if is_public else self.merchant_id

        sign = self.generate_sign(
            api_path=api_path,
            timestamp=timestamp,
            access_token=token_for_sign,
            shop_id=shop_id_for_sign,
            merchant_id=merchant_id_for_sign,
        )
        query_params["sign"] = sign

        url = f"{self.base_url}{api_path}"
        res_json = self._send_http(method, url, params=query_params, json_data=json_data, timeout=30)

        # Kiểm tra lỗi hết hạn token từ Shopee (ví dụ: error_auth / Invalid access_token)
        if res_json.get("error") in ("error_auth", "error_param") and "token" in str(res_json.get("message", "")).lower():
            if retry_on_token_error and self.refresh_token:
                logger.warning("Phát hiện token hết hạn khi gọi API, thử làm mới token và gọi lại...")
                self.refresh_access_token()
                return self.request(method, api_path, params, json_data, is_public, retry_on_token_error=False)

        return res_json


    # =========================================================================
    # CÁC HÀM TIỆN ÍCH TRÍCH XUẤT DỮ LIỆU ĐƯỢC ĐÓNG GÓI SẴN
    # =========================================================================

    def get_shop_info(self) -> Dict[str, Any]:
        """Lấy thông tin cơ bản của shop."""
        return self.request("GET", "/api/v2/shop/get_shop_info")

    def get_order_list(
        self,
        time_range_field: str = "create_time",
        time_from: Optional[int] = None,
        time_to: Optional[int] = None,
        page_size: int = 50,
        cursor: str = "",
        order_status: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Lấy danh sách mã đơn hàng (order_sn).
        Thời gian giữa time_from và time_to tối đa 15 ngày.
        """
        now = int(time.time())
        t_to = time_to or now
        t_from = time_from or (t_to - 14 * 86400)

        params: Dict[str, Any] = {
            "time_range_field": time_range_field,
            "time_from": t_from,
            "time_to": t_to,
            "page_size": min(page_size, 100),
            "cursor": cursor,
        }
        if order_status:
            params["order_status"] = order_status

        return self.request("GET", "/api/v2/order/get_order_list", params=params)

    def get_order_detail(
        self,
        order_sn_list: List[str],
        response_optional_fields: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Lấy thông tin chi tiết của tối đa 50 đơn hàng cùng lúc.
        """
        if not order_sn_list:
            return {"response": {"order_list": []}}

        default_fields = [
            "buyer_user_id",
            "buyer_username",
            "estimated_shipping_fee",
            "recipient_address",
            "actual_shipping_fee",
            "package_list",
            "item_list",
            "invoice_data",
            "payment_method",
            "note",
            "cancel_reason",
        ]
        fields = response_optional_fields or default_fields

        params = {
            "order_sn_list": ",".join(order_sn_list[:50]),
            "response_optional_fields": ",".join(fields),
        }
        return self.request("GET", "/api/v2/order/get_order_detail", params=params)

    def get_item_list(
        self,
        offset: int = 0,
        page_size: int = 50,
        item_status: str = "NORMAL",
        update_time_from: Optional[int] = None,
        update_time_to: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Lấy danh sách ID sản phẩm (item_id).
        item_status: NORMAL, BANNED, UNLIST
        """
        params: Dict[str, Any] = {
            "offset": offset,
            "page_size": min(page_size, 100),
            "item_status": item_status,
        }
        if update_time_from:
            params["update_time_from"] = update_time_from
        if update_time_to:
            params["update_time_to"] = update_time_to

        return self.request("GET", "/api/v2/product/get_item_list", params=params)

    def get_item_base_info(self, item_id_list: List[int]) -> Dict[str, Any]:
        """
        Lấy thông tin chi tiết cơ bản của tối đa 50 sản phẩm.
        """
        if not item_id_list:
            return {"response": {"item_list": []}}

        params = {
            "item_id_list": ",".join(str(x) for x in item_id_list[:50])
        }
        return self.request("GET", "/api/v2/product/get_item_base_info", params=params)

    def get_model_list(self, item_id: int) -> Dict[str, Any]:
        """
        Lấy danh sách các biến thể (phân loại hàng, size, màu) của 1 sản phẩm.
        """
        params = {"item_id": int(item_id)}
        return self.request("GET", "/api/v2/product/get_model_list", params=params)

    def get_escrow_list(
        self,
        release_time_from: int,
        release_time_to: int,
        page_size: int = 50,
        page_no: int = 1,
    ) -> Dict[str, Any]:
        """
        Lấy danh sách quyết toán tiền về ví (Escrow).
        """
        params = {
            "release_time_from": release_time_from,
            "release_time_to": release_time_to,
            "page_size": min(page_size, 100),
            "page_no": page_no,
        }
        return self.request("GET", "/api/v2/payment/get_escrow_list", params=params)

    def get_escrow_detail(self, order_sn: str) -> Dict[str, Any]:
        """
        Lấy chi tiết doanh thu, dòng tiền, phí sàn và thuế của 1 đơn hàng.
        """
        params = {"order_sn": order_sn}
        return self.request("GET", "/api/v2/payment/get_escrow_detail", params=params)

    def get_tracking_info(self, order_sn: str, package_number: str = "") -> Dict[str, Any]:
        """
        Lấy lộ trình di chuyển của kiện hàng.
        """
        params = {"order_sn": order_sn}
        if package_number:
            params["package_number"] = package_number
        return self.request("GET", "/api/v2/logistics/get_tracking_info", params=params)

    def get_return_list(
        self,
        page_no: int = 1,
        page_size: int = 50,
        create_time_from: Optional[int] = None,
        create_time_to: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Lấy danh sách các đơn khiếu nại trả hàng/hoàn tiền.
        """
        params: Dict[str, Any] = {
            "page_no": page_no,
            "page_size": min(page_size, 100),
        }
        if create_time_from:
            params["create_time_from"] = create_time_from
        if create_time_to:
            params["create_time_to"] = create_time_to

        return self.request("GET", "/api/v2/returns/get_return_list", params=params)

    def get_return_detail(self, return_sn: str) -> Dict[str, Any]:
        """
        Lấy chi tiết khiếu nại trả hàng theo mã return_sn.
        """
        params = {"return_sn": return_sn}
        return self.request("GET", "/api/v2/returns/get_return_detail", params=params)

    # =========================================================================
    # PHÂN HỆ CHĂM SÓC KHÁCH HÀNG & CHAT (SELLER CHAT)
    # =========================================================================

    def get_conversation_list(
        self,
        conversation_type: str = "all",
        page_size: int = 50,
        direction: str = "latest",
        next_timestamp_nano: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Lấy danh sách các cuộc hội thoại chat của Shop."""
        params: Dict[str, Any] = {
            "type": conversation_type,
            "direction": direction,
            "page_size": min(page_size, 50),
        }
        if next_timestamp_nano:
            params["next_timestamp_nano"] = next_timestamp_nano
        return self.request("GET", "/api/v2/sellerchat/get_conversation_list", params=params)

    def get_message(
        self,
        conversation_id: str,
        page_size: int = 50,
        direction: str = "older",
        next_timestamp_nano: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Lấy lịch sử tin nhắn trong một cuộc hội thoại cụ thể."""
        params: Dict[str, Any] = {
            "conversation_id": conversation_id,
            "direction": direction,
            "page_size": min(page_size, 50),
        }
        if next_timestamp_nano:
            params["next_timestamp_nano"] = next_timestamp_nano
        return self.request("GET", "/api/v2/sellerchat/get_message", params=params)

    def send_message(self, to_id: int, text: str) -> Dict[str, Any]:
        """Gửi tin nhắn phản hồi cho người mua."""
        payload = {
            "to_id": int(to_id),
            "message_type": "text",
            "content": {"text": text},
        }
        return self.request("POST", "/api/v2/sellerchat/send_message", json_data=payload)

    def read_conversation(self, conversation_id: str, last_read_message_id: str) -> Dict[str, Any]:
        """Đánh dấu đã đọc cuộc hội thoại để duy trì Tỷ lệ phản hồi chat (CRR)."""
        payload = {
            "conversation_id": conversation_id,
            "last_read_message_id": last_read_message_id,
        }
        return self.request("POST", "/api/v2/sellerchat/read_conversation", json_data=payload)

    # =========================================================================
    # PHÂN HỆ MARKETING & KHUYẾN MÃI (DISCOUNT, VOUCHER, FOLLOW PRIZE)
    # =========================================================================

    def get_discount_list(self, discount_status: str = "ALL", page_no: int = 1, page_size: int = 50) -> Dict[str, Any]:
        """Lấy danh sách chương trình giảm giá của shop."""
        params = {
            "discount_status": discount_status,
            "page_no": page_no,
            "page_size": min(page_size, 50),
        }
        return self.request("GET", "/api/v2/discount/get_discount_list", params=params)

    def get_discount(self, discount_id: int) -> Dict[str, Any]:
        """Lấy thông tin chi tiết các sản phẩm trong chương trình giảm giá."""
        params = {"discount_id": int(discount_id)}
        return self.request("GET", "/api/v2/discount/get_discount", params=params)

    def get_voucher_list(self, status: str = "ALL", page_no: int = 1, page_size: int = 50) -> Dict[str, Any]:
        """Lấy danh sách mã giảm giá Voucher của shop."""
        params = {
            "status": status,
            "page_no": page_no,
            "page_size": min(page_size, 50),
        }
        return self.request("GET", "/api/v2/voucher/get_voucher_list", params=params)

    def get_bundle_deal_list(self, page_size: int = 50, time_status: str = "ALL") -> Dict[str, Any]:
        """Lấy danh sách combo mua kèm / combo khuyến mãi (Bundle Deal)."""
        params = {
            "page_size": min(page_size, 50),
            "time_status": time_status,
        }
        return self.request("GET", "/api/v2/bundle_deal/get_bundle_deal_list", params=params)

    def get_follow_prize_list(self, status: str = "all", page_no: int = 1, page_size: int = 50) -> Dict[str, Any]:
        """Lấy danh sách chiến dịch Ưu đãi người theo dõi (Follow Prize)."""
        params = {
            "status": status,
            "page_no": page_no,
            "page_size": min(page_size, 50),
        }
        return self.request("GET", "/api/v2/follow_prize/get_follow_prize_list", params=params)

    def get_follow_prize_detail(self, campaign_id: int) -> Dict[str, Any]:
        """Lấy chi tiết và số lượng followers tăng trưởng từ chiến dịch Follow Prize."""
        params = {"campaign_id": int(campaign_id)}
        return self.request("GET", "/api/v2/follow_prize/get_follow_prize_detail", params=params)

    # =========================================================================
    # PHÂN HỆ CẤU HÌNH WEBHOOK (PUSH API)
    # =========================================================================

    def get_app_push_config(self) -> Dict[str, Any]:
        """Xem cấu hình Webhook Push Notification hiện tại của ứng dụng."""
        return self.request("GET", "/api/v2/push/get_app_push_config", is_public=True)

    def set_app_push_config(self, callback_url: str, push_service: List[Dict[str, int]]) -> Dict[str, Any]:
        """Cập nhật đường dẫn callback và danh sách sự kiện push muốn nhận."""
        payload = {
            "callback_url": callback_url,
            "push_service": push_service,
        }
        return self.request("POST", "/api/v2/push/set_app_push_config", json_data=payload, is_public=True)

    # =========================================================================
    # PHÂN HỆ SẢN PHẨM TOÀN CẦU (GLOBAL PRODUCTS - CNSC)
    # =========================================================================

    def get_global_item_list(self, offset: int = 0, page_size: int = 50, global_item_status: str = "NORMAL") -> Dict[str, Any]:
        """Lấy danh sách sản phẩm toàn cầu ở cấp độ tài khoản tổng Merchant CNSC."""
        params = {
            "offset": offset,
            "page_size": min(page_size, 100),
            "global_item_status": global_item_status,
        }
        return self.request("GET", "/api/v2/global_product/get_global_item_list", params=params)
