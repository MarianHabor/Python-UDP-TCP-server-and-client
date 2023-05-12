import socket # python socket library

# establishing a TCP connection
# AF_INET refers to the ip address-family ipv4.
# the SOCK_STREAM is the TCP protocol
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the server on localhost ip and port 8080
clientSocket.connect(('127.0.0.1', 8080))

# printing that the conection has been establish
print("Connection with server has been established.")

# keeping connection alive and send message to server
# till client inputs exit
while True:
    message = input("Enter your message: ")
    if message == 'exit':
        break
    clientSocket.sendall(message.encode())

    # receive the message sent from the server and print it
    data = clientSocket.recv(1024)
    print(F"Received from server: {data.decode()}\n")
    