import socket
import sys
import signal

HOST = 'localhost'  # The server's hostname or IP address
PORT = 6000        # The port used by the server

# Define the signal handler to exit gracefully
def signal_handler(sig, frame):
    print('Exiting gracefully...')
    sys.exit(0)

# Set up the signal handler for graceful exit on Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    server_address = (HOST, PORT)
    print('listening to %s port %s' % server_address, file=sys.stderr)
    sock.connect(server_address)
    mes = b"Hello, world"
    print(f"Sending data: {mes}")
    sock.sendall(mes)
   