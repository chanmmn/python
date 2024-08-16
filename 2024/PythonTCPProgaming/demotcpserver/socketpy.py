import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 18999))

# Listen for incoming connections
server_socket.listen()

print("Server is listening on port 18999...")

try:
    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")

        # Send a response back to the client
        response = "Hello from the server!"
        client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()

except KeyboardInterrupt:
    print("Server stopped by user")

# Close the server socket
server_socket.close()