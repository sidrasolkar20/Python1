# Exp06(Postlab02)
# Aim:Write a python program to create simple socket for file sending between server and client.
# Name:Sidra Solkar
# UIN: 231P087
# Roll No.: 43
import socket

HOST = '127.0.0.1'
PORT = 56789

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

file_name = conn.recv(1024).decode()
print(f"Receiving file: {file_name}")

with open("received_" + file_name, "wb") as file:
    while True:
        data = conn.recv(1024)  
        if not data:
            break  
        file.write(data)  

print(f"File '{file_name}' received successfully.")

conn.close()
server_socket.close()
