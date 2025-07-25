import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

# Tạo socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server đang lắng nghe...")

conn, addr = server_socket.accept()
print(f"Đã kết nối với {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Nhận:", data)
    # Chuyển thành chữ hoa
    result = data.upper()
    conn.send(result.encode())

conn.close()
