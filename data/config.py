#id api, hàm băm
API_ID = 1488
API_HASH = 'abcde1488'

REF_LINK = 'https://t.me/BlumCryptoBot/app?startapp=ref_KWLqXBcHmF'

DELAYS = {
    "RELOGIN": [5, 7],  #trì hoãn sau lần thử đăng nhậpp
    'ACCOUNT': [5, 15],  #độ trễ giữa các kết nối với tài khoản (càng nhiều tài khoản, độ trễ càng lâu)
    'PLAY': [5, 15],   #độ trễ giữa các lần chơi tính bằng giây
    'ERROR_PLAY': [5, 8],    #độ trễ giữa các lỗi trong trò chơi tính bằng giây
    'CLAIM': [600, 1800],   #độ trễ tính bằng giây trước điểm yêu cầu cứ sau 8 giờ
    'GAME': [35, 37],  #trì hoãn sau khi bắt đầu trò chơi
    'TASK_COMPLETE': [2, 3],  #trì hoãn sau khi hoàn thành nhiệm vụ
    'TASK_ACTION': [5, 10]  #trì hoãn sau khi bắt đầu nhiệm vụ
}

#nếu bạn cần chơi trong trò chơi
PLAY_GAME = True

#điểm sau mỗi lần chơi trò chơi; tối đa 280
POINTS = [240, 280]

BLACKLIST_TASK = ['Join or create tribe']

PROXY = {
    "USE_PROXY_FROM_FILE": False,  #True -nếu sử dụng proxy từ tập tin, False -nếu sử dụng proxy từ account.json
    "PROXY_PATH": "data/proxy.txt",  #đường dẫn đến tập tin proxy
    "TYPE": {
        "TG": "http",  #loại proxy cho máy khách tg. "socks4", "socks5" và "http" được hỗ trợ
        "REQUESTS": "http"  #loại proxy cho các yêu cầu. "http" cho proxy https và http, "sock5" cho proxy vớ5.
        }
}

#thư mục phiên (không thay đổi)
WORKDIR = "sessions/"

#thời gian chờ tính bằng giây để kiểm tra tài khoản hợp lệ
TIMEOUT = 30
