import socket
import threading

clients = [] # List of (socket, username) tuples

def broadcast(message, sender_socket=None):
    for client, _ in clients:
        try:
            client.send(message.encode("utf-8"))
        except:
            client.close()
            clients.remove((client, _))

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode("utf-8")
        clients.append((client_socket, username))
        broadcast(f"{username} telah bergabung ke chat")

        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message or message.lower() == "tata":
                break
            broadcast(f"{username}:{message}", client_socket)
    except:
        pass
    finally:
        for c, u in clients:
            if c == client_socket:
                clients.remove((c, u))
                broadcast(f"*** {u} telah keluar dari chat ***")
                break
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 54321))
    server.listen(5)
    print("Server listening on port 54321")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    start_server()
