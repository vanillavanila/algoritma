import datetime
print(""" 
                                                                   
▄▄▄   ▄▄▄       ▄▄▄      ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄ 
████▄████       ████▄  ▄████ ▄██▀▀██▄ ███▀▀███▄ ▀▀▀███▀▀▀ 
 ▀█████▀        ███▀████▀███ ███  ███ ███▄▄███▀    ███    
▄███████▄ ▀▀▀▀▀ ███  ▀▀  ███ ███▀▀███ ███▀▀██▄     ███    
███▀ ▀███       ███      ███ ███  ███ ███  ▀███    ███    
                                                          
                                                          
    """)
print("=-=" * 35)

data_pegawai = {
    "0001": {"nama": "Thanos", "username": "thanos_123", "password": "123"},
    "0002": {"nama": "Saber", "username": "saber_123", "password": "123"},
    "0003": {"nama": "Balmond", "username": "balmond_123", "password": "123"}
}

data_produk = {
    "12345": {"nama": "Minyak", "harga": 40000, "stok": 10},
    "22345": {"nama": "Aqua", "harga": 3500, "stok": 11},
    "32345": {"nama": "Mie", "harga": 4000, "stok": 13},
    "42345": {"nama": "Sabun", "harga": 10000, "stok": 12},
    "52345": {"nama": "Sarden", "harga": 20000, "stok": 10}
}


def login():
    print("=" * 30)
    print("Silahkan Login Terlebih Dahulu")
    user = input("Masukan kode pegawai: ")
    password = input("Masukan password: ")

    if user in data_pegawai and data_pegawai[user]["password"] == password:
        nama_pegawai = data_pegawai[user]["nama"]
        print(f"\n Selamat datang, {nama_pegawai}")
        return True, nama_pegawai
    else:
        print("=" * 30)
        print(f"\n❌ Pegawai tidak terdaptar")
        return False, ""

def trasnsaksi():
        keranjang = []

        print("\n Mulai transaksi baru")
        while True:
            barcode = input("Masukan barcode / kode barang (Jika sudah tidak ada barang yang ditambahkan bisa ketik 'selesai' untuk proses transaksi): ").strip() 

            if barcode.lower() == 'selesai':
                break

            if barcode in data_produk:
                produk = data_produk[barcode]
                print(f"barang di temukan: {produk['nama']} (Rp{produk['harga']})")
                print(f"barang tersedia: {produk['stok']}")

                try:
                    qty = int(input(f"Masukan jumlah '{produk["nama"]}' yang ingin dibeli: "))
                except ValueError:
                    print("\n Input harus berupa angka")
                    continue
                
                if qty > produk['stok']:
                    print("\n❌ Produk tidak cukup")
                elif qty <= 0:
                    print("\n Minimal Beli 1! ")
                else:
                    subtotal = qty * produk['harga']

                    keranjang.append({
                        "barcode"  : barcode,
                        "nama"     : produk['nama'],
                        "harga"    : produk['harga'],
                        "qty"      : qty,
                        "subtotal" : subtotal
                    })
                    print(f"\n☑️ Barang  berhasil  ditambahkan ke keranjang...")
            else:
                print("❌ Barcode tidak ditemukan di database!")

        if len(keranjang) == 0:
            print("\n Transaksi gagal keranjang tidak boleh kosong")
            return True

        total_belanja = sum(item['subtotal'] for item in keranjang)

        print("=" *30)
        print(f"\n Total yang harus dibayar: (Rp{total_belanja})")

        try:
            uang_diterima = int(input("Masukan jumlah pembayaran untuk : "))
        except ValueError:
            print("❌ Pembyaran harus berupa angka...")
            return True

        if uang_diterima < total_belanja:
            print("❌ uang tidak cukup")
            print("Transaksi di batalkan!")
            return True
        else:
            kembalian = uang_diterima - total_belanja

            for item in keranjang:
                data_produk[item['barcode']]['stok'] -= item['qty']

            waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\n" + "="*32)
            print("            X-MART")
            print("="*32)
            print(f"Tanggal : {waktu_sekarang}")
            print("-"*32)

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

while True:
    sukses, kasir = login()

    if sukses:
        break

while True:
    lanjut = trasnsaksi()
    pertanyaan = input(f"\n Ingin melakukan transaksi lagi? (y/t)")

    if pertanyaan.lower() == 't':
        print(f"Sesi transaksi selesai...Seee You {kasir}")
        break