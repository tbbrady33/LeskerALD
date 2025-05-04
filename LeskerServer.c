
// THIS IS FAR FROM COMPLETE, the working code is in python

#include <winsock2.h>
#include <stdio.h>

#pragma comment(lib, "ws2_32.lib") // Link with ws2_32.lib

// Well I need to rewrite this for windows

#define PORT 5000
#define BUFFER_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[BUFFER_SIZE];

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }


    address.sin_family = AF_INET; // IPv4
    address.sin_addr.s_addr = INADDR_LOOPBACK; // Any incoming address
    address.sin_port = htons(PORT); // Port number

    // Bind the socket to the specified port and address
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Start listening for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    printf("Listening on port %d...\n", PORT);

    while (1) {
        // Accept a new connection
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
            perror("accept");
            exit(EXIT_FAILURE);
        }

        // Read data from the client
        read(new_socket, buffer, BUFFER_SIZE);
        printf("Received: %s\n", buffer);

        // Send a response back to the client
        send(new_socket, hello, strlen(hello), 0);
        printf("Hello message sent\n");

        close(new_socket); // Close the connection with the client
    }

    return 0;
}