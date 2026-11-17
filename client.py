#import socket module for network communication
import socket

# Define the server's IP address (localhost) and port number
HOST="127.0.0.1"
PORT =9090

# Create a TCP socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server at the specified HOST and PORT
socket.connect((HOST,PORT))

# Encode the string message into UTF-8 bytes and send it to the server
socket.send("Hello World".encode("utf-8"))

# Receive up to 1024 bytes of response from the server, decode it, and print
print(socket.recv(1025))

# Close the client socket connection
socket.close()
