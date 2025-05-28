import socket

HOST = '127.0.0.1'  # 또는 서버 IP
PORT = 10011

# 소켓 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 서버에 연결
    s.connect((HOST, PORT))
    
    # HTTP GET 요청 보내기
    request = (
        "GET / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    s.sendall(request.encode('utf-8'))

    # 응답 받기
    response = b''
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk

    print(response.decode('utf-8'))

