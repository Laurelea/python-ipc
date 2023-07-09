import socket
import sys

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = '/tmp/uds_socket'
print('connecting to ', server_address)
try:
    sock.connect(server_address)
except socket.error as msg:
    print(f'error connecting to socket: {sys.stderr, msg}')
    sys.exit(1)

try:
    # Send data
    message = ('This is the message from Python Unix Socket CLient.  It will be repeated.').encode()
    print(f'sending message: {message}')
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message) + 16

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f'received: {data.decode()}')
finally:
    print('closing socket')
    sock.close()
