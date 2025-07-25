import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

# Tạo socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Nhập chuỗi: ")
    if not message:
        break
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print("Server gửi lại:", data)

client_socket.close()
