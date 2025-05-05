import socket
import sys

HOST = 'localhost'  # The server's hostname or IP address
PORT = 6000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    server_address = (HOST, PORT)
    print('listening to %s port %s' % server_address, file=sys.stderr)
    sock.connect(server_address)
    mes = sock.recv(1024)
    print(mes.decode('utf-8'))
    sock.close()