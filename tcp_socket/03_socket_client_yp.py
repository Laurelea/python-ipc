import socket
HOST, PORT = '', 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ping-pong')
    received_data = s.recv(512)
