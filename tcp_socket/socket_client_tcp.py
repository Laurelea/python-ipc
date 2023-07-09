import socket

# address_to_server = ('192.168.31.176', 8886)
address_to_server = ('192.168.31.71', 8886)
# address_to_server = ('localhost', 8886)
# address_to_server = ('127.0.0.1', 7071)
# address_to_server = ('localhost', 8765)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)
client.send(bytes("Hello My Love!", encoding='UTF-8'))

data = client.recv(1024)
print(str(data))

client.close()