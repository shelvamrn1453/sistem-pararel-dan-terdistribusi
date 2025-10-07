import socket

def start_client(): # Mendefinisikan fungsi utama untuk menjalankan client
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect (("localhost", 12345))# Menghubungkan socket client ke alamat server (localhost) dan port 12345

    clientSocket.send("hallo saya dari klien!".encode("utf-8")) # Mengirim pesan ke server dalam bentuk byte (harus di-encode ke UTF-8)

    data = clientSocket.recv(1024).decode("utf-8")# Menerima balasan dari server, maksimal 1024 byte, lalu ubah dari byte ke teks UTF-8
    print(f"menerima pesan dari server: {data}") # Menampilkan pesan balasan yang diterima dari server ke terminal

    clientSocket.close()

if __name__ == "__main__":# Mengecek apakah file ini dijalankan langsung (bukan diimpor)
    start_client() # Memanggil fungsi start_client untuk menjalankan program client