import socket # python socket library
  
# establishing a TCP connection
# AF_INET refers to the ip address-family ipv4.
# the SOCK_STREAM is the TCP protocol
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the server to localhost ip and port 8080
serverSocket.bind(('127.0.0.1', 8080))

# accepting one client connection
serverSocket.listen(10)

# printing that the server is wating for a client to conncet
print("Server is waiting for a connection.")

# accepting incoming client connection
clientSocket, clientAddress = serverSocket.accept()

# prining that conncetion is been established
print(F"Connection from {clientAddress} has been established.")

# keeping connection and receving any messages from
# connected client
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    if data:
        print(F"Received from client: {data.decode()}")
    
    # send the message back to the client
    clientSocket.sendall(data)