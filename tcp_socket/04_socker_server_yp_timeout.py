import socket
HOST, PORT = '', 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((HOST, PORT))
    s.settimeout(5)
    data, addr = s.recvfrom(512)
except socket.timeout:
    pass
finally:
    s.close()
