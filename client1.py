import socket

HOST = '127.0.0.1'  # 또는 서버의 IP 주소
PORT = 10011
USERNAME = '세영'  # 보낼 이름

# GET 요청을 구성
request = (
    f"GET /greet?username={USERNAME} HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# 소켓을 열고 요청 보내기
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(request.encode('utf-8'))

    # 응답 수신
    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

# 출력
print(response.decode('utf-8'))

