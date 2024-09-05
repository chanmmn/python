import socket
# Define the server's IP address and port
server_ip = 'localhost'
server_port = 18999
# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    # Send the message to the server
    message = 'Hello'
    client_socket.sendall(message.encode())
    # Receive the response from the server
    response = client_socket.recv(1024)
    print('Response from server:', response.decode())
finally:
    # Close the socket
    client_socket.close()