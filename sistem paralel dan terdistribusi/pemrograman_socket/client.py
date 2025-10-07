import socket

def start_client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect (("localhost", 12345))

    clientSocket.send("hallo saya dari klien!".encode("utf-8"))

    data = clientSocket.recv(1024).decode("utf-8")
    print(f"menerima pesan dari server: {data}")

    clientSocket.close()

if __name__ == "__main__":
    start_client()