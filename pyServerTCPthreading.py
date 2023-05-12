import socket
import threading

 

HOST = 'localhost'

PORT = 8080

BACKLOG = 50 # Maximum number of queued connections

 

# Function to handle a client connection

def handle_client(conn, addr):

   print(f"New client connected: {addr}")

   # Send a welcome message to the client

   conn.send("Welcome to the server!".encode())

 

   while True:

       # Receive data from the client

       data = conn.recv(1024).decode()

       if not data:

           break

       print(f"Received from client {addr}: {data}")

       # Send the received data back to the client

       conn.send(data.encode())

 

   print(f"Client {addr} disconnected")

   conn.close()

 

# Create a TCP socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket option to reuse the address/port

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the specified host and port

server_socket.bind((HOST, PORT))

# Set the socket to listen for incoming connections

server_socket.listen(BACKLOG)

 

print(f"Server is listening on {HOST}:{PORT}")

 

# Start a loop to handle incoming connections

while True:

   # Wait for a client to connect

   conn, addr = server_socket.accept()

   # Start a new thread to handle the client connection

   client_thread = threading.Thread(target=handle_client, args=(conn, addr))

   client_thread.start()