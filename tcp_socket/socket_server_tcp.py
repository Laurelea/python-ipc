import socket

server_address = ('192.168.31.176', 8886)
# server_address = ('127.0.0.1', 7071)
# server_address = ('localhost', 8080)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)
print(f'server is running on {server_address}, please, press ctrl+c to stop')

while True:
    connection, client_address = server.accept()
    print(f'connected: {client_address}')

    try:
        while True:
            datagram = connection.recv(1024)
            if datagram:
                print(f'received message: {datagram}')
                connection.sendall(bytes(f'Hello from server! This was your message: {datagram}', encoding='UTF-8'))
            else:
                print('no more data from', client_address)
                break
    finally:
        connection.close()