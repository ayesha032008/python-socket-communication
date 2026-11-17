#import python's built in socket module for network communication
import socket 

#define the server ip address to accept incoming connections
HOST="127.0.0.1"

#define the port number for the server to listen 
PORT=9090  

#create a socket object using ipv4 and TCP protocol
server= socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

#bind the socket to the specified ip address and port
server.bind((HOST,PORT))

#put the server into listenng mode to accept incoming connections
server.listen(5)

#start the infinite loop to keep the srver running continuously
while True:
    #accept an incoming client connection and retrieve it's socket and address 
    communication_socket, address= server.accept()

    #Log the successfull connection with client address
    print(f"Connection from {address}has been estabilished")
    
    #receive data from the client (upto 1024 bytes) and decode it to UTF-8 string
    message=communication_socket.recv(1024).decode("utf-8")
    
    #print the received message to the console
    print(f"Message from client:{message}")

    #send an acknowledgment message back to the client
    communication_socket.send(f"Message received".encode("utf-8"))

    #close the communication socket for this client
    communication_socket.close()

    # Log that the connection has ended
    print(f"Connection with {address} ended")
