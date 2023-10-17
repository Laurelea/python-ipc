import socket
HOST, PORT = '', 8888

# принимает только 1 соединение
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            received_data = conn.recv(512)
            if not received_data:
                break
            conn.sendall(received_data)