import socket
import sys
import signal

HOST = 'localhost'  # The server's hostname or IP address
PORT = 5001        # The port used by the server

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
   
    while True:
        try:
            # Receive the data in small chunks and retransmit it
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            # Here you can process the data as needed
            # For example, you could save it to a file or perform some calculations
        except socket.timeout:
            # Timeout occurred, just continue the loop
            pass