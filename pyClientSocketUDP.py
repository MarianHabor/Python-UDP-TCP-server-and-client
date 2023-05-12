import socket # python socket library

# establishing a UDP connection
# AF_INET refers to the ip address-family ipv4.
# the SOCK_DGRAM is the UDP protocol
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# keeping connection alive and send message to server
# till client inputs exit
while True:
    message = input("Enter your message: ")
    if message == 'exit':
        break

    clientSocket.sendto(message.encode(), ('127.0.0.1', 8080))

    # receive the message sent from the server and print it
    data, serverAddress = clientSocket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")
    