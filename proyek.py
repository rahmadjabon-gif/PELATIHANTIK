#====================================================================
# Program Kasir Mini Sederhana
# Dibuat oleh : Rahmad Adi Nugraha
# Sekolah : SMK Negeri Pasirian
# Tujuan : Menghitung total belanjaan, diskon, dan kembalian
#====================================================================

from datetime import datetime

# Data barang
barang_list = [
    {"kode": "A1", "nama": "Pensil", "harga": 2000},
    {"kode": "A2", "nama": "Buku Tulis", "harga": 5000},
    {"kode": "A3", "nama": "Penghapus", "harga": 1500},
    {"kode": "A4", "nama": "Penggaris", "harga": 3000},
    {"kode": "A5", "nama": "Spidol", "harga": 4000},
]

# Fungsi menampilkan daftar barang
def tampilkan_barang():
    print("\n=== DAFTAR BARANG TOKO ===")
    print("Kode\tNama Barang\tHarga")
    print("---------------------------")
    for b in barang_list:
        print(f"{b['kode']}\t{b['nama']:<15}\tRp{b['harga']}")
    print("---------------------------")

# Fungsi cetak struk
def cetak_struk(keranjang, total, diskon):
    print("\n===============================")
    print("         STRUK PEMBAYARAN       ")
    print("===============================")
    print(f"Tanggal : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("--------------------------------")
    for item in keranjang:
        print(f"{item['nama']:<15} x{item['jumlah']} = Rp{item['subtotal']}")
    print("--------------------------------")
    if diskon > 0:
        print(f"Diskon 10%        : -Rp{int(diskon)}")
    print(f"Total Bayar       : Rp{int(total)}")
    print("================================")

    # Input pembayaran
    while True:
        try:
            bayar = int(input("Uang pembeli     : Rp"))
            if bayar < total:
                print("Uang tidak cukup, silakan masukkan lagi.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka!")

    kembalian = bayar - total
    print(f"Kembalian         : Rp{int(kembalian)}")
    print("================================")
    print("   Terima Kasih Telah Berbelanja!")
    print("================================")

# Fungsi transaksi
def transaksi():
    tampilkan_barang()
    keranjang = []
    total_belanja = 0

    while True:
        kode = input("\nMasukkan kode barang (atau 'selesai' untuk selesai): ").upper()
        if kode == 'SELESAI':
            break

        barang = next((b for b in barang_list if b['kode'] == kode), None)
        if barang:
            try:
                jumlah = int(input(f"Masukkan jumlah {barang['nama']}: "))
                subtotal = barang['harga'] * jumlah
                keranjang.append({
                    "nama": barang['nama'],
                    "harga": barang['harga'],
                    "jumlah": jumlah,
                    "subtotal": subtotal
                })
                total_belanja += subtotal
                print(f"{barang['nama']} x{jumlah} ditambahkan (Subtotal: Rp{subtotal})")
            except ValueError:
                print("Jumlah harus berupa angka!")
        else:
            print("Kode barang tidak ditemukan!")

    if not keranjang:
        print("\nTidak ada barang dibeli.")
        return

    # Hitung diskon
    diskon = 0
    if total_belanja > 50000:
        diskon = total_belanja * 0.10
    total_akhir = total_belanja - diskon

    # Cetak struk
    cetak_struk(keranjang, total_akhir, diskon)

# Menu utama
def menu():
    while True:
        print("\n=== MENU KASIR MINI ===")
        print("1. Lihat daftar barang")
        print("2. Mulai transaksi")
        print("0. Keluar")
        pilihan = input("Pilih menu (1/2/0): ").strip()

        if pilihan == '1':
            tampilkan_barang()
        elif pilihan == '2':
            transaksi()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan program kasir mini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    menu()

