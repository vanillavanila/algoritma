import datetime

data_produk = {
    "0101": {"nama": "apel", "harga": 5000, "stok": 20},
    "0202": {"nama": "nanas", "harga": 10000, "stok": 20},
    "0303": {"nama": "duren", "harga": 50000, "stok": 20},
}

data_pegawai = {
    "111": {"nama": "abdul", "password": "kasir_1"},
    "222": {"nama": "abdul", "password": "kasir_2"},
    "333": {"nama": "abdul", "password": "kasir_3"}
}

print("=||=" * 30)
print("Hallow silahkan login dulu baru lanjut")


def login():

    kode = input("Masukan kode: ")
    password = input("masukan password: ")

    if kode in data_pegawai and data_pegawai[kode]["password"] == password:
        nama = data_pegawai[kode]['nama']
        print(f"selamat datang {nama}")
        return True, nama
    else:
        print("gagal login")
        return False, ""

def transaksi():
        print("||" *30)
        print("Selamat bekerja... ")

        keranjang = []
        while True:
            barcode = input("silahkan masukan kode barang (jika mau langsung ke pembayaran tinggal ketik 'bayar'): ")

            if barcode.lower() == 'bayar':
                break

            if barcode in data_produk:
                produk = data_produk[barcode]

                print(f"Nama barang: {produk['nama']}")
                print(f"harga (Rp{produk['harga']})")
                print(f"stok: {produk['stok']}")

                qty = int(input("Masulan jumlah produk yang ingin di beli: "))

                if qty > produk['stok']:
                    print('produk tidak cukup! ')
                elif qty <= 0:
                    print("minimal beli 1")
                else:
                    subtotal = qty * produk['harga']
                    print(f"subtotal: {subtotal}")

                    keranjang.append({
                            "barcode"  : barcode,
                            "nama"     : produk['nama'],
                            "harga"    : produk['harga'],
                            "qty"      : qty,
                            "subtotal" : subtotal
                    })
                    print("produk sudah berhasil dimasukan ke keranjang")
            else:
                print("Produk tidak ditemukan")

        if len(keranjang) == 0:
            print("Keranjang tidak boleh kososng")
            return True
        
        total_belanja = sum(item['subtotal'] for item in keranjang)

        print(f"total (Rp{total_belanja})")
        bayar = int(input("masukan pembayaran: "))

        if bayar < total_belanja:
            print('uang tidak cukup ')
        else:
            kembalian = bayar - total_belanja

            for item in keranjang:
                data_produk[item['barcode']]['stok'] -= item['qty']

            for item in keranjang:
                print(f"Nama produk: {item['nama']}")
                print(f"Harga: {item['qty']} x {item['subtotal']}")

            print("=" * 30)
            waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(waktu)
            print(f"Total: {total_belanja}")
            print(f"Kembalian: {kembalian}")


        return True

while True:
    sukses, kasir = login()

    if sukses:
        break

while True:
    lanjut = transaksi()

    pertanyaan = input("Mau melakukan teransaksi lagi (y/t)")

    if pertanyaan.lower() == 't':
        print("terimakasih :)")
        break