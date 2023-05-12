import socket # python socket library
  
# establishing a UDP connection
# AF_INET refers to the ip address-family ipv4.
# the SOCK_DGRAM is the UDP protocol
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# binding the server to localhost ip and port 8080
serverSocket.bind(('127.0.0.1', 8080))

# printing that the server is wating for a client to conncet
print("Server is waiting for a connection.")

# keeping connection and receving any messages from
# connected client
while True:
    data, clientAddress = serverSocket.recvfrom(1024)

    if not data:
        break

    if data:
        print(F"Received from client {clientAddress} : {data.decode()}")
    
    # send the message back to the client
    serverSocket.sendto(data, clientAddress)