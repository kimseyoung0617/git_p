import socket

HOST = '127.0.0.1'
PORT = 10011

# 전송할 데이터
body = "username=세영"
content_length = len(body)

# HTTP POST 요청 구성
request = (
    "POST /greet HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    f"Content-Length: {content_length}\r\n"
    "Connection: close\r\n"
    "\r\n"
    f"{body}"
)

# 소켓 열고 전송
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(request.encode('utf-8'))

    # 응답 수신
    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

# 결과 출력
print(response.decode('utf-8'))

