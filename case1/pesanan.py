for i in range(1):
    print("===== Pilih Mneu Di Bawah")
    print("Nasi Ayam")
    print("Nasi Goreng")
    print("Ayam Geprek")

daftar_menu = ['Nasi Ayam', 'Nasi Goreng', 'Ayam Geprek']
daftar_minuman = ['Es Teh', 'kopi', 'air putih']

while True:

    pesanan = input('masukan nama menu: ').lower()
    jumlah = int(input('masukan jumlah yang ingin di pesan: '))

    harga = 0

    if pesanan == 'nasi ayam':
        harga = 15000
    elif pesanan == 'nasi goreng':
        harga = 10000
    elif pesanan == 'ayam geprek':
        harga = 8000
    else:
        print(f'menu belum ada!')

    if harga > 0:
        total = harga * jumlah

        print(f"anda memesan {pesanan} berjumlah {jumlah}. dan total harga Rp{total}")

    while True:
        jawaban = input("mau lanjut pesan minum apa nggak? Y or N: ").lower()

        if jawaban in ['n']:
            break

        if jawaban in ['y']:
            for m in range(1):
                print("===== Pilih Mneu Minuman")
                print("Es Teh")
                print("Kopi")
                print("Air Putih")

            minuman = input('masukan nama minuman yang ingin di pesan: ').lower()
            jumlah_m = int(input('jumlahnya berapa: '))

            harga_m = 0

            
            if minuman == 'es teh':
                harga_m = 5000
            elif minuman == 'kopi':
                harga_m = 10000
            elif minuman == 'air putih':
                harga_m = 8000
            else:
                print(f'menu belum ada!')

            if harga_m > 0:
                total_m = harga_m * jumlah_m
                print(f"anda memesan {minuman} berjumlah {jumlah_m}. dan total harga Rp{total_m}")

                total_keseluruhan = total + total_m

        print(f'total pesanan anda Rp{total_keseluruhan}')

        jawaban = input('udah cuman itu apa mau mesan lagi? Y or N ').lower()

        if jawaban in ['y', 'n']:
            break

    if jawaban == 'n':
        break
        

    

       