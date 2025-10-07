import socket # Mengimpor modul socket yang digunakan untuk komunikasi jaringan

def start_server():#membuat fungsi bernama start_server, isinya nanti semua langkah untuk menjalankan server.
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Membuat socket baru dengan jenis IPv4 (AF_INET) misalya 127.0.01. dan protokol TCP (SOCK_STREAM)adi datanya dikirim berurutan dan aman.
    serverSocket.bind(("localhost", 12345)) # Mengikat (bind) socket ke alamat localhost dan port 12345
    serverSocket.listen(5)# Mengatur agar server bisa mendengarkan maksimal 5 koneksi yang menunggu
    print("server mendengarkan informasi dari port 12345")# Menampilkan pesan bahwa server sudah siap

    while True:# Loop tak hingga agar server terus berjalan dan siap menerima client baru
        clientSocket, clientAddress = serverSocket.accept()#Dapat menerima koneksi dari client, menandakan server menerima koneksi dari client.

        data = clientSocket.recv(1024).decode("utf-8")# Menerima data/pesan dari client, maksimal 1024 byte, lalu mendekode dari bentuk byte ke teks UTF-8
        print(f"menerima pesan dari klien: {data}")# Menampilkan pesan yang diterima dari client di terminal

        clientSocket.send("hallo dari server!".encode("utf-8"))# Mengirimkan balasan ke client berupa pesan konfirmasi

        clientSocket.close()# Menutup koneksi dengan client setelah komunikasi selesai

if __name__ == '__main__':# Mengecek apakah file ini dijalankan langsung (bukan diimpor)
    start_server()# Memanggil fungsi start_server untuk memulai server