# import random
# print("=== SELAMAT DATANG DI GAME GUNTING BATU KERTAS ===")

# print("< SILAHKAN PILIH  >")

# pilihan = ['GUNTING', 'BATU', 'KERTAS']

# while True:
#     print('1 - GUNTING')
#     print('2 - BATU')
#     print('3 - KERTAS')

#     try:
#         pilihan_user = int(input("masukan pilihan anda"))
#     except ValueError:
#         print("harap masukan angka yang valid!")
#         continue

#     while pilihan_user < 1 or pilihan_user > 3:
#         pilihan_user = int(input("harap masukan pilihan yang valid"))

#     nama_pilihan_user = pilihan[pilihan_user - 1]

#     print("pilihan anda adalah ", nama_pilihan_user)
#     print("sekarang giliran komputer...")

#     pilihan_komputer = random.randint(1, 3)
#     nama_pilihan_komputer = pilihan[pilihan_komputer - 1]

#     print("Pilihan Komputer adalah:", nama_pilihan_komputer)
#     print(nama_pilihan_user, "vs", nama_pilihan_komputer)

#     if pilihan_user == pilihan_komputer:
#         print("hasil seri")

#     elif(
#         (pilihan_user == 1 and pilihan_komputer == 3) or
#         (pilihan_user == 2 and pilihan_komputer == 1) or
#         (pilihan_user == 3 and pilihan_komputer == 2)
#     ):
#         print("anda menang")

#     else:
#         print('anda kalah')



# def ubahCelcius ( C, satuan) :
#   if (satuan == "R"): 
#     hasil= 4/5 * C
#   elif (satuan == "F"):
#     hasil= 9/5 * C + 32
#   elif (satuan == "K"):
#     hasil= C + 273.15
#   return round (hasil, 2)

# def ubahReamur ( R, satuan) :
#   if (satuan == "C"): 
#     hasil= 5/4 * R
#   elif (satuan == "F"):
#     hasil= 9/4 * R + 32
#   elif (satuan == "K"):  
#     hasil= 5/4 * R + 273.15
#   return round (hasil, 2)

# def ubahFahrenheit ( F, satuan) :
#   if (satuan == "C"): 
#     hasil= (5/9) * F
#   elif (satuan == "R"):
#     hasil= (4/9) * (F - 32)
#   elif (satuan == "K"):  
#     hasil= (5/9) * (F - 32) + 273.15
#   return round (hasil, 2)
  
# def ubahKelvin ( K, satuan) :
#   if (satuan == "C"): 
#     hasil= K - 273.15
#   elif (satuan == "R"):
#     hasil= (4/5) * (K - 273.15)
#   elif (satuan == "F"): 
#     hasil= (9/5) * (K - 273.15) + 32
#   return round (hasil, 2)  

# def main() : 
#   print("="*40)
#   print(" masukkan satuan yang ingin diubah ")
#   satuan1= input(" C/ R/ F/ K: ").upper()
#   nilai= int(input(" berapa nilainya? "))
#   print("="*40)
#   print(" masukkan satuan satuan tujuan akhir ")
#   satuan2= input(" C/ R/ F/ K: ").upper()
#   print("="*40)

#   if (satuan1 == "C"):
#     hasil= ubahCelcius(nilai, satuan2)
#   elif(satuan1 == "R"):
#     hasil= ubahReamur(nilai, satuan2)
#   elif(satuan1 == "F") :
#     hasil= ubahFahrenheit(nilai, satuan2)
#   elif(satuan1 == "K"):
#     hasil= ubahKelvin(nilai, satuan2)

#     print( nilai, satuan1, " setara dengan ", hasil, satuan2, sep="")

# main()

# buat kalkulator

# def kalkulator():
#     print("+++ SILAHKAN PILIH OPRASI YANG INGIN ANDA LAKUKAN +++")
#     print("1 - Penjumlahan ")
#     print("2 - Pengurangan ")
#     print("3 - Perkalian ")
#     print("4 - Pembagian ")

#     while True:
#         oprasi = input("Masukan oprasi yang anda mau: ")
            
#         try:
#             angak1 = int(input("masukan angka pertama: "))
#             angak2 = int(input("masukan angka kedua: "))
#         except ValueError:
#             print("Input hasrus angka")
#             continue

#         if oprasi == '1':
#             penjumlahan = angak1 + angak2
#             print(f'hasil dari penjumlahan {angak1} + {angak2} adalah = {penjumlahan}')
#         elif oprasi == '2':
#             penjumlahan = angak1 - angak2
#             print(f'hasil dari pengurangan {angak1} - {angak2} adalah = {penjumlahan}')
#         elif oprasi == '3':
#             penjumlahan = angak1 * angak2
#             print(f'hasil dari perkalian {angak1} x {angak2} adalah = {penjumlahan}')
#         elif oprasi == '4':
#             penjumlahan = angak1 / angak2
#             print(f'hasil dari pembagian {angak1} / {angak2} adalah = {penjumlahan}')
#         else:
#             print("pilihan tidak valid!!!!")

# kalkulator()

# username = ('indra')
# password = ('123')

# input_user = input("Masukan username: ")
# input_pass = input("Masukan password: ")

# if username == input_user and password == input_pass:
#     print("berhasil  login")
# elif username != input_user:
#     print("username tidak terdaptar")
# elif password != input_pass:
#     print("password salah")
# else:
#     print("username tidak terdaftar")



# print("=" * 40)
# print("=== THANKS MART ===")
# print("=" * 40)

# data_produk = {
#         "0011" : {"nama": "nasi", "harga": 50000, "stok": 100},
#         "0012" : {"nama": "nasi", "harga": 50000, "stok": 100},
#         "0013" : {"nama": "nasi", "harga": 50000, "stok": 100},
#         "0014" : {"nama": "nasi", "harga": 50000, "stok": 100},
#         "0015" : {"nama": "nasi", "harga": 50000, "stok": 100}
#     }   


# barcode = input("masukan bbarcode: ")

# if barcode in data_produk:
#     produk = data_produk[barcode]

#     print(f"\n Nama barang = {produk['nama']} (harga = Rp{produk['harga']}) ")
#     print(f"\n Stok barang = {produk['stok']}")

#     jumlah_beli = int(input("Masukan jumlah barang yang di beli: "))

#     if jumlah_beli > produk['stok']:
#         print("\n Stok tidak mencukupi...")
#     elif jumlah_beli <=0:
#         print("\n Minimal beli satu barang...")
#     else:
#         # ambil total belanja
#         total_belanja = jumlah_beli * produk["harga"]
#         print(f"\n Total harga Rp{total_belanja}")

#     uang = int(input("masukan uang bayar: "))

#     if uang < total_belanja:
#         print("uang tidak cukup")
#     else:
#         kembalian = uang - total_belanja

#         print("===THANKS MART===")
#         print("=-=" * 35)
#         print(f"\n Nama Produk: {produk['nama']}")
#         print(f"\n Jumlah: {jumlah_beli}")
#         print(f"\n total harga: Rp{total_belanja}")
#         print(f"\n bayar: Rp{uang}")
#         print(f"\n kembalian: Rp{kembalian}")
#         print("=-=" * 30)
#         print("Terimakasih sudah berbelkanja :)")
# else:
#     print("===Produk tidak ada===")


list_produk = { 
    "0001": {"nama": "laptop", "harga": 1000000, "stok": 5},
    "0002": {"nama": "hp", "harga": 2000000, "stok": 2},
    "0003": {"nama": "ipad", "harga": 5000000, "stok": 3}
 }

barcode = input("Masukan barcode: ")

if barcode in list_produk:
    produk = list_produk[barcode]

    print(f"nama barang {produk['nama']} harga (Rp{produk['harga']})")
    print(f"Stok {produk['stok']}")

    jumlah = int(input("Masukan jumlah barang: "))

    if jumlah > produk['stok']:
        print(f"Stok tidak cukup")
    elif jumlah <= 0:
        print("Minimal beli 1 barang..")
    else:
        total_belanja = jumlah * produk['harga']
        print(f"Total belanja (Rp{total_belanja})")

    bayar = int(input("Masukan uang: "))

    if bayar < total_belanja:
        print(f"Uang anda tidak cukup")
    else:
        kembalian = bayar - total_belanja

        print(f"kembalian (Rp{kembalian}) ")

        print("thank you")

else:
    print("Barang tidak ada")