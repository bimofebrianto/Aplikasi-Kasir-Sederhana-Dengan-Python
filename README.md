# Aplikasi Kasir Sederhana dengan Python

Aplikasi kasir berbasis terminal yang dibuat menggunakan **Python**. Aplikasi ini dirancang untuk mempermudah proses transaksi penjualan di toko dengan menampilkan daftar barang, menghitung total belanja, menerima input pembayaran, dan memberikan rincian struk pembelian.

## Fitur Utama
1. **Daftar Barang:**
   - Menampilkan tabel barang lengkap dengan nama barang, harga satuan (Rp), dan jumlah yang diinputkan.
2. **Input Barang yang Dibeli:**
   - Pengguna dapat memasukkan nama barang yang ingin dibeli dan jumlahnya.
   - Ketik `selesai` untuk mengakhiri proses input barang.
3. **Rincian Pesanan:**
   - Menampilkan ringkasan pesanan yang mencakup nama barang, jumlah, harga satuan, dan subtotal.
4. **Hitung Total dan Pembayaran:**
   - Menghitung total harga semua barang yang dibeli.
   - Pengguna dapat memasukkan jumlah uang yang dibayarkan.
   - Menghitung kembalian dan memberikan rincian pembayaran.
5. **Struk Pembelian:**
   - Menampilkan struk yang mencakup semua rincian pembelian, total harga, pembayaran, dan kembalian.

## Cara Kerja
1. Jalankan program Python menggunakan terminal.
2. Aplikasi akan menampilkan daftar barang yang tersedia beserta harganya.
3. Masukkan nama barang yang ingin dibeli satu per satu dan jumlahnya.
4. Ketik `selesai` jika sudah selesai memilih barang.
5. Program akan menampilkan rincian pesanan dan meminta input jumlah pembayaran.
6. Struk pembelian akan ditampilkan setelah transaksi selesai.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama yang digunakan untuk membangun logika aplikasi.

## Instalasi
1. Pastikan Python sudah terinstal di komputer Anda.
2. Unduh atau clone repositori ini.
3. Jalankan file `kasir.py` menggunakan terminal.

```bash
# Clone repositori
git clone https://github.com/yourusername/aplikasi-kasir-python.git

# Buka direktori proyek
cd aplikasi-kasir-python

# Jalankan aplikasi
python kasir.py
```

## Struktur File
```
.
├── kasir.py         # File Python utama
├── README.md        # Dokumentasi
```

## Contoh Output
```
=== Barang Toko Bimo ===
Nama Barang       Harga (Rp)
---------------------------
Sabun            5000
Shampoo         15000
Pasta Gigi      10000
Detergen         2000
Minyak Goreng   25000
Gula Pasir      12000
Tissue           8000
Cuka             7000

Masukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk selesai): selesai

=== Rincian Pesanan ===
Nama Barang    Jumlah    Harga Satuan (Rp)    Subtotal (Rp)
----------------------------------------------------------
Sabun              1              5000              5000
Shampoo            1             15000             15000
...
Total yang harus dibayar: Rp 77000
Masukkan jumlah yang dibayar: Rp 100000

=== STRUK PEMBELIAN ===
Nama Barang    Jumlah    Harga Satuan (Rp)    Subtotal (Rp)
----------------------------------------------------------
Sabun              1              5000              5000
...
Total               Rp 77000
Dibayar             Rp 100000
Kembalian           Rp 23000

Terima kasih telah berbelanja di Toko Kami!
```

## Pengembangan di Masa Depan
- Menambahkan fitur untuk diskon dan pajak.
- Menyimpan riwayat transaksi ke dalam file.
- Mendukung antarmuka grafis (GUI).

## Contoh Tampilan Aplikasi

Berikut adalah contoh tampilan aplikasi kasir sederhana:
![Capture1](https://github.com/user-attachments/assets/7c079962-20a8-468c-babe-e2a37edaf615)
![Capture](https://github.com/user-attachments/assets/240289ec-e5e5-46a4-8740-4bc490803b44)

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file LICENSE untuk detail lebih lanjut.

## Penulis
- **Bimo Febrianto** - https://github.com/bimofebrianto
