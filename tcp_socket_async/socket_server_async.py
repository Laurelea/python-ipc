# https://practicum.yandex.ru/learn/async-python/courses/be7a81c7-2443-4476-8813-604159438fcb/sprints/140330/topics/244229b0-57e3-42c8-8296-1f44fb4ee205/lessons/a56e81f0-37de-43af-9699-df87c9de6211/



# краткий пример
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
#     listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     listen_socket.bind((HOST, PORT))
#     listen_socket.listen()
#     listen_socket.setblocking(False)

#  его используют при поллинге событий с помощью select



"""неблокирующий echo-сервер"""

import logging
import selectors
import socket
import sys

HOST, PORT = '', 8000  # Порт сервера

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))

"""это селектор - обертка на select
обработчик событий от ОС
У селектора существует два основных события для обработки:
EVENT_READ (1) — событие, когда сокет готов принимать данные.
EVENT_WRITE (2) — событие, когда данные были отправлены из сокета или когда сокет снова готов для записи данных."""
def new_connection(selector: selectors.BaseSelector, sock: socket.socket):
    # new_conn - клиентский сокет
    new_conn, address = sock.accept()
    logger.info('accepted new_conn from %s', address)
    new_conn.setblocking(False)

    selector.register(new_conn, selectors.EVENT_READ, read_callback)

def read_callback(selector: selectors.BaseSelector, sock: socket.socket):
    data = sock.recv(1024)
    if data:
        sock.send(data)
    else:
        logger.info('closing connection %s', sock)
        selector.unregister(sock)
        sock.close()

# получение событий по зарегистрированным сокетам от ОС
def run_iteration(selector: selectors.BaseSelector):
    events = selector.select()  # забирает все события от ОС
    """
    Ключ SelectorKey, который содержит информацию:
    - о зарегистрированном сокете fileobj;
    - закреплённом за сокетом файловым дескриптором fd;
    - событиях, которые ожидаются для сокета events;
    - данных, которые передали при регистрации data. 
    В текущем примере данные — это функция, которую нужно вызвать при наступлении события.
    Маска mask, которая может принимать одно из четырёх основных значений:
    0 — не произошло ни одного из событий;
    1 — произошло событие EVENT_READ;
    2 — произошло событие EVENT_WRITE;
    3 — произошли оба события: и EVENT_READ, и EVENT_WRITE..
    """
    for key, mask in events:
        callback = key.data  # функция, которую нужно вызвать при наступлении события.
        # Далее для каждого события вызывается зарегистрированная функция с двумя параметрами: текущий селектор и сокет.
        # Селектор нужен, чтобы регистрировать клиентские сокеты для обработки событий, а сам сокет — чтобы принимать
        # новые соединения или обрабатывать данные.
        callback(selector, key.fileobj)

def serve_forever():
    """
    Метод запускает сервер на постоянное прослушивание новых сообщений
    """
    with selectors.SelectSelector() as selector:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            """
            Сокет использует для своей работы файловые дескрипторы, но в некоторых случаях ему может не хватить объёма портов
            — максимум 65 535. Поэтому необходимо включить опцию переиспользования
            listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True).
            Она позволит подключать больше клиентов, чем портов, так как файловые дескрипторы не имеют ограничения по количеству.
            """
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            #  блокировка с сокета снимается так:
            #  socket.setblocking(False)
            server_socket.setblocking(False)
            logger.info('Server started on port %s', PORT)

            # Зарегистрировать каждое событие получения новых данных по серверному сокету и вызвать функцию new_connection
            # Другими словами, каждый раз, когда к серверу отправляют новую пачку данных и её получает ОС,
            # она отправляет событие в программу, а та вызывает функцию new_connection.
            selector.register(server_socket, selectors.EVENT_READ, new_connection)

            while True:
                run_iteration(selector)

if __name__ == '__main__':
    serve_forever()

"""
У echo-сервера из примера используется два важных концепта:
цикл событий (event-loop) для обработки неблокирующих сокетов;
callback для вызова последующего кода.
Эти концепты заложены в основу почти всех асинхронных библиотек, которые будут вам встречаться в Python.
"""