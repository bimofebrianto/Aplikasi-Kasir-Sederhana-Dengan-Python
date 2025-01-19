# Daftar barang beserta harga per unit
barang = {
    "Sabun": 5000,
    "Shampoo": 15000,
    "Pasta Gigi": 10000,
    "Detergen": 20000,
    "Minyak Goreng": 25000,
    "Gula Pasir": 12000,
    "Tissue": 8000,
    "Cuka": 7000
}

def tampilkan_menu():
    print("\n=== Barang Toko Bimo ===")
    print(f"{'Nama Barang':<20} {'Harga (Rp)':>10}")
    print("-" * 30)
    for item, harga in barang.items():
        print(f"{item:<20} {harga:>10}")
    print("=" * 30)

def hitung_total(pesanan):
    total = 0
    for item, jumlah in pesanan.items():
        total += barang[item] * jumlah
    return total

def cetak_struk(pesanan, total, bayar, kembalian):
    print("\n=== STRUK PEMBELIAN ===")
    print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Harga Satuan (Rp)':<20} {'Subtotal (Rp)':<20}")
    print("-" * 70)
    for item, jumlah in pesanan.items():
        harga_satuan = barang[item]
        subtotal = harga_satuan * jumlah
        print(f"{item:<20} {jumlah:<10} {harga_satuan:<20} {subtotal:<20}")
    print("-" * 70)
    print(f"{'Total':<50} Rp {total}")
    print(f"{'Dibayar':<50} Rp {bayar}")
    print(f"{'Kembalian':<50} Rp {kembalian}")
    print("=" * 70)
    print("Terima kasih telah berbelanja di Toko Kami!")
    print("=" * 70)

def kasir():
    pesanan = {}
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): ").strip().title()
        
        if pilihan.lower() == "selesai":
            break
        elif pilihan in barang:
            try:
                jumlah = int(input(f"Masukkan jumlah {pilihan} yang ingin dibeli: "))
                if jumlah > 0:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    print(f"{jumlah} {pilihan} telah ditambahkan ke pesanan.")
                else:
                    print("Jumlah harus lebih dari 0.")
            except ValueError:
                print("Masukkan angka yang valid untuk jumlah.")
        else:
            print("Barang tidak ditemukan, coba lagi.")
    
    if pesanan:
        total = hitung_total(pesanan)
        print("\n=== Rincian Pesanan ===")
        print(f"{'Nama Barang':<20} {'Jumlah':<10} {'Harga Satuan (Rp)':<20} {'Subtotal (Rp)':<20}")
        print("-" * 70)
        for item, jumlah in pesanan.items():
            harga_satuan = barang[item]
            subtotal = harga_satuan * jumlah
            print(f"{item:<20} {jumlah:<10} {harga_satuan:<20} {subtotal:<20}")
        print("=" * 70)
        print(f"Total yang harus dibayar: Rp {total}")
        
        while True:
            try:
                bayar = int(input("Masukkan jumlah uang yang dibayar: Rp "))
                if bayar >= total:
                    kembalian = bayar - total
                    cetak_struk(pesanan, total, bayar, kembalian)
                    break
                else:
                    print(f"Uang yang dibayar kurang sebesar Rp {total - bayar}, silakan coba lagi.")
            except ValueError:
                print("Masukkan angka yang valid untuk pembayaran.")
    else:
        print("Tidak ada pesanan. Program selesai.")

# Jalankan program kasir
if __name__ == "__main__":
    kasir()
