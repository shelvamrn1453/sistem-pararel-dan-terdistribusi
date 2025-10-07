import socket

def start_server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("localhost", 12345))
    serverSocket.listen(5)
    print("server mendengarkan informasi dari port 12345")

    while True:
        clientSocket, clientAddress = serverSocket.accept()

        data = clientSocket.recv(1024).decode("utf-8")
        print(f"menerima pesan dari klien: {data}")

        clientSocket.send("hallo dari server!".encode("utf-8"))

        clientSocket.close()

if __name__ == '__main__':
    start_server()