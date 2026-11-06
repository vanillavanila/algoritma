import datetime
print(""" 
                                                                   
▄▄▄   ▄▄▄       ▄▄▄      ▄▄▄   ▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄ 
████▄████       ████▄  ▄████ ▄██▀▀██▄ ███▀▀███▄ ▀▀▀███▀▀▀ 
 ▀█████▀        ███▀████▀███ ███  ███ ███▄▄███▀    ███    
▄███████▄ ▀▀▀▀▀ ███  ▀▀  ███ ███▀▀███ ███▀▀██▄     ███    
███▀ ▀███       ███      ███ ███  ███ ███  ▀███    ███    
                                                          
                                                          
    """)
print("=-=" * 35)

data_produk = {
    "12345": {"nama": "Minyak", "harga": 40000, "stok": 10},
    "22345": {"nama": "Aqua", "harga": 3500, "stok": 11},
    "32345": {"nama": "Mie", "harga": 4000, "stok": 13},
    "42345": {"nama": "Sabun", "harga": 10000, "stok": 12},
    "52345": {"nama": "Sarden", "harga": 20000, "stok": 10}
}

bacode = input("Masukan barcode / kode barang: ")

if bacode in data_produk:
    produk = data_produk[bacode]
    print(f"barang di temukan: {produk['nama']} (Rp{produk['harga']})")
    print(f"barang tersedia: {produk['stok']}")

    qty = int(input("Masukan jumlah beli: "))

    if qty > produk['stok']:
        print("\n❌ Produk tidak cukup")
    elif qty <= 0:
        print("\n Minimal Beli 1! ")
    else:
        total_belanja = qty * produk['harga']
        print(f"Total Belanja: Rp{total_belanja}")

    uang_diterima = int(input("Masukan jumlah pembayaran: "))

    if uang_diterima < total_belanja:
        print("\n❌ Uang tidak cukup! ")
    else:
        kembalian = uang_diterima - total_belanja

        produk['stok'] -= qty   
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "="*32)
        print("         X-MART")
        print("="*32)
        print(f"Tanggal : {waktu_sekarang}")
        print("-"*32)
        print(f"{produk['nama']}")
        print(f"  {qty} x {produk['harga']} = Rp{total_belanja}")
        print("-"*32)
        print(f"TOTAL     : Rp{total_belanja}")
        print(f"BAYAR     : Rp{uang_diterima}")
        print(f"KEMBALIAN : Rp{kembalian}")
        print("="*32)
        print("    TERIMA KASIH ATAS")
        print("      KUNJUNGAN ANDA")
        print("="*32)
            
else:
    print("❌ Barcode tidak ditemukan di database!")