# api id, hash
API_ID = xxxx
API_HASH = 'xxxx'

REF_LINK = 'https://t.me/BlumCryptoBot/app?startapp=ref_KWLqXBcHmF'

DELAYS = {
    "RELOGIN": [5, 7],  # trì hoãn sau lần thử đăng nhập
    'ACCOUNT': [5, 15],  # độ trễ giữa các kết nối với tài khoản (càng nhiều tài khoản thì độ trễ càng lâu)
    'PLAY': [5, 15],   # độ trễ giữa các lần chơi tính bằng giây
    'ERROR_PLAY': [5, 8],    # độ trễ giữa các lỗi trong trò chơi tính bằng giây
    'CLAIM': [600, 1800],   # độ trễ tính bằng giây trước điểm yêu cầu cứ sau 8 giờ
    'GAME': [35, 37],  # trì hoãn sau khi bắt đầu trò chơi
}

# nếu bạn cần chơi trong trò chơi
PLAY_GAME = True

# điểm sau mỗi lần chơi trò chơi; tối đa 280
POINTS = [240, 280]

BLACKLIST_TASK = ['Đăng ký Blum Telegram', 'Tham gia $PARK trên SOL', "Tham gia $CLOUT của OFFSET", 'Tham gia trò chơi $RACE', 'Tham gia hoặc tạo bộ lạc', 'Gặp Ví Blum', 'NFT là gì?', 'USDT hay USDC?', 'BTC dễ biến động. Tại sao?']

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "http",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "http"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# thư mục phiên (không thay đổi)
WORKDIR = "sessions/"

# thời gian chờ tính bằng giây để kiểm tra tài khoản hợp lệ
TIMEOUT = 30
