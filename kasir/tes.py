import datetime

print("=" * 20)
print("Silahkan login terlebih dahulu")

data_pegawai = {
    "0001": {"nama": "jin", "password": "123"},
    "0002": {"nama": "jin", "password": "123"},
    "0003": {"nama": "jin", "password": "123"},
}

data_produk = {
    "0101": {"nama": "sawit utuh", "harga": 100000, "stok": 100},
    "0202": {"nama": "Minyak mentah", "harga": 50000, "stok": 10},
    "0202": {"nama": "Minyak mentah", "harga": 50000, "stok": 10},
}

def login():
    print("=" *40 )
    print("Silahkan Login Terlebih Dahulu!")

    kode = input("Masukan kode pegawai: ")
    password = input("Masukan password: ")

    if kode in data_pegawai and data_pegawai[kode]["password"] == password:
        time = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        nama_pegawai = data_pegawai[kode]["nama"]
        print(f"Nama pegawai: {nama_pegawai} (login pada: {time})")  
        return True, nama_pegawai
    else:
        print("gagal login kode/password salah")
        return False, ""

def transaksi():
    # bagian penginputan barang

            keranjang = []
            print("=" * 30)
            print("Memulai Transaksi...")

            while True:
                barcode = input("masukan kode barang, (bisa memasukan lebih dari satu jenis produk). ketik 'selesai' jika tidak ada yang ingin di tambah: ")

                if barcode.lower() == 'selesai':
                    break

                if barcode in data_produk:
                    produk = data_produk[barcode]
                    print(f"Produk ditemukan {produk["nama"]}, Harga (Rp{produk["harga"]})")
                    print(f"Stok yang tersedia -> {produk["stok"]}")

                    try:
                        qty = int(input(f"masukan jumlah '{produk["nama"]}' yang ingin di beli: "))
                    except ValueError:
                        print("❌ Input harus  berupa angka")

                    if qty > produk["stok"]:
                        print(f"❌ Stok tidak cukup...")
                    elif qty <= 0:
                        print(f"❌ Minimal jumlah produk yang di input (1) produk!")
                    else:
                        subtotal = qty * produk["harga"]

                        keranjang.append({
                            "kode"     : barcode,
                            "nama"     : produk["nama"],
                            "harga"    : produk["harga"],
                            "qty"      : qty,
                            "subtotal" : subtotal
                        })
                        print(f"☑️ Produk berhasil di tambahkan kedalam keranjang... ")
                else:
                    print("❌Produk tidak ditemukan!")

            if len(keranjang) == 0:
                print("Gagal melakukan teransaksi keranjang tidak boleh kosong!")
                return True

            total_belanja  = sum(item['subtotal'] for item  in keranjang)

            print("=" *30)
            print(f"\n Total bayar: (Rp {total_belanja})")

            try:
                uang_diterima = int(input("Masukan jumlah pembayaran: "))
            except ValueError:
                print("❌ Input harus berupa angka!")

            if uang_diterima < total_belanja:
                print("❌ Uang tidak cukup")
            else:
                kembalian = uang_diterima - total_belanja

                for item in keranjang:
                    data_produk[item['kode']]['stok'] -= item['qty']

                print("=" * 30)

                print("X-Mart")

                for item in keranjang:
                    print(f" {item["nama"]} ")
                    print(f" {item['qty']} x {item['harga']} = (Rp{item['subtotal']})")

                print("-" *30)
                print(f"Total belanja: {total_belanja}")
                print(f"Bayar: {uang_diterima}")
                print(f"Kembalian: {kembalian}")

            return True


while True:
    sukess, kasir = login()


    if sukess:
        break

while True:
    lanjut =  transaksi()

    quetion = input("\n ingin melakukan teransaksi lagi (y/t)?")

    if quetion.lower() == 't':
        print("Maksih :) ")
        break
