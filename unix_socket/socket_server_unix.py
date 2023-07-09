import socket
import os
import sys
import time
from collections import deque

server_address = '/tmp/uds_socket'

flist = []


if os.path.exists(server_address):
    os.unlink(server_address)
    # os.remove(server_address)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(1)

while True:
    connection, client_address = server.accept()
    print(f'connected: {client_address}')

    try:
        while True:
            datagram = connection.recv(1024)
            if datagram:
                print(f'received message: {datagram}')
                connection.sendall(datagram)
                # tokens = datagram.strip().split()
                # if tokens[0].lower() == "post":
                #     flist.append(tokens[1])
                #     connection.send(len(tokens) + "")
                # elif tokens[0].lower() == "get":
                #     connection.send(tokens[0])
                # else:
                #     connection.send("-1")
            else:
                print('no more data from', client_address)
                break
    finally:
        connection.close()