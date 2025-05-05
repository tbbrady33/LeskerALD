import socket
import sys

Host = 'localhost'  # The server's hostname or IP address
Port = 5000        # The port used by the server

# Create a TCP/IP socket that closes on its own when the program ends
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Bind the socket to the address and port
    server_address = (Host,Port)
    print('starting up on %s port %s' % server_address, file=sys.stderr)
    sock.bind(server_address)

    #listen for incoming connections by setting the socket to listen mode
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection', file=sys.stderr)
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address, file=sys.stderr)

            # Receive the data in small chunks and retransmit it
            with connection:
                print(f"Connected by {client_address}")
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                
        finally:
            # Clean up the connection
            connection.close()
