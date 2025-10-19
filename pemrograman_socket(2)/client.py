import socket
import threading
import sys

def receive_messages(sock, username):
    while True:
        try:
            data = sock.recv(1024).decode("utf-8")
            if not data:
                print("\n[INFO] Terputus dari server")
                break
            if data.startswith("***"):
                print(f"\n{data}")
            else:
                try:
                    sender, msg = data.split(":", 1)
                    if sender == username:
                        print(f"{'':>40}{msg.strip()} << Anda")
                    else:
                        print(f"{sender}: {msg.strip()}")
                except:
                    print(data)
        except:
            print("\n[ERROR] Gagal menerima pesan")
            break
    sys.exit()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 54321))
    username = input("Masukkan username Anda: ").strip()
    client.send(username.encode("utf-8"))

    threading.Thread(target=receive_messages, args=(client, username), daemon=True).start()

    while True:
        message = input()
        if message.lower() == "tata":
            client.send("tata".encode("utf-8"))
            print("[INFO] Keluar dari chat...")
            break
        client.send(message.encode("utf-8"))
    client.close()

if __name__ == "__main__":
    start_client()
