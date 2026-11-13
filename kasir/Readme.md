import datetime

print(""" 
▄▄▄   ▄▄▄       ▄▄▄       ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄ 
████▄████       ████▄  ▄████ ▄██▀▀██▄ ███▀▀███▄ ▀▀▀███▀▀▀ 
 ▀█████▀        ███▀████▀███ ███  ███ ███▄▄███▀    ███    
▄███████▄ ▀▀▀▀▀ ███  ▀▀  ███ ███▀▀███ ███▀▀██▄     ███    
███▀ ▀███       ███      ███ ███  ███ ███  ▀███    ███    
""")
print("=-=" * 35)

data_pegawai = {
    "0001": {"nama": "Thanos", "username": "thanos", "password": "123"},
    "0002": {"nama": "Saber", "username": "saber", "password": "123"},
    "0003": {"nama": "Balmond", "username": "balmond", "password": "123"}
}

data_produk = {
    "12345": {"nama": "Minyak", "harga": 40000, "stok": 10},
    "22345": {"nama": "Aqua", "harga": 3500, "stok": 11},
    "32345": {"nama": "Mie", "harga": 4000, "stok": 13},
    "42345": {"nama": "Sabun", "harga": 10000, "stok": 12},
    "52345": {"nama": "Sarden", "harga": 20000, "stok": 10}
}

def login():
    print("\n--- SILAKAN LOGIN KASIR ---")
    user = input("Masukkan kode pegawai: ")
    password = input("Masukkan password: ")

    if user in data_pegawai and data_pegawai[user]["password"] == password:
        nama_kasir = data_pegawai[user]["nama"]
        print(f"\nLogin Berhasil! Selamat datang, {nama_kasir}")
        return True, nama_kasir
    else:
        print("\n❌ Pegawai tidak ditemukan atau password salah!")
        return False, ""

def transaksi():
    keranjang = []  # List untuk menampung banyak barang belanjaan
     
    print("\n--- MULAI TRANSAKSI BARU ---")
    while True:
        barcode = input("Masukkan barcode barang (ketik 'selesai' untuk proses pembayaran): ").strip()
        
        if barcode.lower() == 'selesai':
            break  # Berhenti memasukkan barang dan lanjut ke pembayaran

        if barcode in data_produk:
            produk = data_produk[barcode]
            print(f"  -> Ditemukan: {produk['nama']} | Harga: Rp{produk['harga']} | Stok: {produk['stok']}")

            try:
                qty = int(input("  -> Masukkan jumlah beli: "))
            except ValueError:
                print("❌ Input jumlah harus berupa angka!\n")
                continue

            if qty > produk['stok']:
                print("❌ Stok produk tidak mencukupi!\n")
            elif qty <= 0:
                print("❌ Minimal beli 1!\n")
            else:
                subtotal = qty * produk['harga']
                
                # Masukkan ke dalam keranjang belanja
                keranjang.append({
                    "barcode": barcode,
                    "nama": produk['nama'],
                    "harga": produk['harga'],
                    "qty": qty,
                    "subtotal": subtotal
                })
                print(f"✔ Berhasil ditambahkan ke keranjang.\n")
        else:
            print("❌ Barcode tidak ditemukan di database!\n")

    # Jika keranjang kosong (langsung ketik selesai)
    if len(keranjang) == 0:
        print("Transaksi dibatalkan, keranjang kosong.")
        return True

    # --- PROSES HITUNG TOTAL & PEMBAYARAN ---
    total_belanja = sum(item['subtotal'] for item in keranjang)
    
    print("\n" + "="*32)
    print(f"TOTAL YANG HARUS DIBAYAR: Rp{total_belanja}")
    print("="*32)

    try:
        uang_diterima = int(input("Masukkan jumlah pembayaran: "))
    except ValueError:
        print("❌ Pembayaran harus berupa angka! Transaksi dibatalkan.")
        return True

    if uang_diterima < total_belanja:
        print("❌ Uang tidak cukup! Transaksi dibatalkan.")
        return True
    else:
        kembalian = uang_diterima - total_belanja

        # Kurangi stok produk secara permanen di database setelah pembayaran sukses
        for item in keranjang:
            data_produk[item['barcode']]['stok'] -= item['qty']

        # Cetak Struk Gabungan
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "="*32)
        print("            X-MART")
        print("="*32)
        print(f"Tanggal : {waktu_sekarang}")
        print("-"*32)
        
        # Cetak semua barang di keranjang
        for item in keranjang:
            print(f"{item['nama']}")
            print(f"  {item['qty']} x {item['harga']} = Rp{item['subtotal']}")
            
        print("-"*32)
        print(f"TOTAL     : Rp{total_belanja}")
        print(f"BAYAR     : Rp{uang_diterima}")
        print(f"KEMBALIAN : Rp{kembalian}")
        print("="*32)
        print("    TERIMA KASIH ATAS")
        print("      KUNJUNGAN ANDA")
        print("="*32)
        
    return True

# --- PROGRAM UTAMA ---
while True:
    sukses, kasir = login()
    if sukses:
        break

while True:
    lanjut = transaksi()
    tanya_lagi = input("\nIngin melayani transaksi baru lagi? (y/t): ")
    if tanya_lagi.lower() == 't':
        print(f"\nSesi kasir selesai. Sampai jumpa, {kasir}!")
        break













<!-- kalau mau nambahin titik di angka nya -->
# Fungsi bantu untuk format angka dengan titik ribuan (contoh: 40.000)
def format_rp(angka):
    return f"{angka:_}".replace("_", ".")

def login():
    print("\n--- SILAKAN LOGIN KASIR ---")
    user = input("Masukkan kode pegawai: ")
    password = input("Masukkan password: ")

    if user in data_pegawai and data_pegawai[user]["password"] == password:
        nama_kasir = data_pegawai[user]["nama"]
        print(f"\nLogin Berhasil! Selamat datang, {nama_kasir}")
        return True, nama_kasir
    else:
        print("\n❌ Pegawai tidak ditemukan atau password salah!")
        return False, ""

def transaksi():
    keranjang = []  # List untuk menampung banyak jenis produk
    
    print("\n--- MULAI TRANSAKSI BARU ---")
    while True:
        barcode = input("Masukkan barcode barang (ketik 'selesai' untuk pembayaran): ").strip()
        
        if barcode.lower() == 'selesai':
            break

        if barcode in data_produk:
            produk = data_produk[barcode]
            print(f"  -> Ditemukan: {produk['nama']} | Harga: Rp{format_rp(produk['harga'])} | Stok: {produk['stok']}")

            try:
                qty = int(input("  -> Masukkan jumlah beli: "))
            except ValueError:
                print("❌ Input jumlah harus berupa angka!\n")
                continue

            if qty > produk['stok']:
                print("❌ Stok produk tidak mencukupi!\n")
            elif qty <= 0:
                print("❌ Minimal beli 1!\n")
            else:
                subtotal = qty * produk['harga']
                
                # Masukkan produk ke keranjang
                keranjang.append({
                    "barcode": barcode,
                    "nama": produk['nama'],
                    "harga": produk['harga'],
                    "qty": qty,
                    "subtotal": subtotal
                })
                print(f"✔ Berhasil ditambahkan ke keranjang.\n")
        else:
            print("❌ Barcode tidak ditemukan di database!\n")

    # Jika keranjang kosong
    if len(keranjang) == 0:
        print("Transaksi dibatalkan, keranjang kosong.")
        return True

    # Hitung total keseluruhan belanjaan
    total_belanja = sum(item['subtotal'] for item in keranjang)
    
    print("\n" + "="*32)
    print(f"TOTAL YANG HARUS DIBAYAR: Rp{format_rp(total_belanja)}")
    print("="*32)

    try:
        uang_diterima = int(input("Masukkan jumlah pembayaran: "))
    except ValueError:
        print("❌ Pembayaran harus berupa angka! Transaksi dibatalkan.")
        return True

    if uang_diterima < total_belanja:
        print("❌ Uang tidak cukup! Transaksi dibatalkan.")
        return True
    else:
        kembalian = uang_diterima - total_belanja

        # Kurangi stok produk secara permanen
        for item in keranjang:
            data_produk[item['barcode']]['stok'] -= item['qty']

        # Cetak Struk Belanja
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "="*32)
        print("            X-MART")
        print("="*32)
        print(f"Tanggal : {waktu_sekarang}")
        print("-"*32)
        
        # Cetak semua item dari keranjang
        for item in keranjang:
            print(f"{item['nama']}")
            print(f"  {item['qty']} x Rp{format_rp(item['harga'])} = Rp{format_rp(item['subtotal'])}")
            
        print("-"*32)
        print(f"TOTAL     : Rp{format_rp(total_belanja)}")
        print(f"BAYAR     : Rp{format_rp(uang_diterima)}")
        print(f"KEMBALIAN : Rp{format_rp(kembalian)}")
        print("="*32)
        print("    TERIMA KASIH ATAS")
        print("      KUNJUNGAN ANDA")
        print("="*32)
        
    return True

# --- PROGRAM UTAMA ---
# 1. Sesi Login
while True:
    sukses, kasir = login()
    if sukses:
        break

# 2. Sesi Transaksi Berulang
while True:
    lanjut = transaksi()
    tanya_lagi = input("\nIngin melayani transaksi baru lagi? (y/t): ")
    if tanya_lagi.lower() == 't':
        print(f"\nSesi kasir selesai. Sampai jumpa, {kasir}!")
        break