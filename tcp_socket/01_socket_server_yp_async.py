import socket

HOST, PORT = '', 8888


def handle_request(request: bytes) -> bytes:
    request_data = request.decode()
    http_response = f"""HTTP/1.1 200 OK\nContent-Type: text/html\n\n{request_data}"""
    return http_response.encode()


def serve_forever():
    # Устанавливаем TCP-соединение
    # socket.AF_INET - канал передачи данных
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
        listen_socket.bind((HOST, PORT))
        listen_socket.listen()
        print('Serving HTTP on port {port} ...'.format(port=PORT))

        # работа с приходящими данными:
        while True:
            # client_connection - объект клиентского сокета
            client_connection, client_address = listen_socket.accept()
            with client_connection:
                # получаем данные пачками по 1024
                request = client_connection.recv(1024)  # Получаем информацию от клиента
                http_response = handle_request(request)
                client_connection.sendall(http_response)


if __name__ == '__main__':
    serve_forever()