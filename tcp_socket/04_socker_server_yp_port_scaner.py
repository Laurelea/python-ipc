import socket
HOST ='127.0.0.1'
PORTS = [22, 23, 80, 443, 3000, 8000, 8001, 9000]

for port in PORTS:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        res = s.connect_ex((HOST, port))
        print(f"{port}: {res}")
        