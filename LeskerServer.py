import socket
import asyncio
import signal
from pymodbus.client import AsyncModbusTcpClient
import sys
from getpressforserver import read_pressure
import getaborted


# Connection parameters
IP = '192.168.137.11'
PORT = 502
REGISTER_ADDRESS = 1
SCALE_FACTOR = 0.000152590218967


# Define the signal handler to exit gracefully
def signal_handler(sig, frame):
    print('Exiting gracefully...')
    sys.exit(0)

# Set up the signal handler for graceful exit on Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

Host = 'localhost'  # The server's hostname or IP address
Port = 5001       # The port used by the server

# Create a TCP/IP socket that closes on its own when the program ends
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:    # Bind the socket to the address and port
    server_address = (Host, Port)
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    # Set a timeout to periodically allow signal handling
    sock.settimeout(1.0)  # Set the timeout to 1 second

    print('waiting for a connection', file=sys.stderr)

    while True:
        try:
            # Wait for a connection (with timeout)
            connection, client_address = sock.accept()
            try:
                print('connection from', client_address, file=sys.stderr)

                # Receive the data in small chunks and retransmit it
                with connection:
                    print(f"Connected by {client_address}")
                    
                    data = connection.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    # Here you can process the data as needed
                    # For example, you could save it to a file or perform some calculations

                    # lets send the real time data back to the client
                    asyncio.run(read_pressure(sock))


            finally:
                # Clean up the connection
                connection.close()

        except socket.timeout:
            # Timeout occurred, just continue the loop
            pass
