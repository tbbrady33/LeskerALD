import socket
import sys

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    server_address = (HOST, PORT)
    print('connecting to %s port %s' % server_address, file=sys.stderr)
    sock.connect(server_address)
    sock.sendall(b'Hello, world') # this is where the data goes
