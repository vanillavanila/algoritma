print("======= Daftar Produk =======")
print("== 1 - Mie Instant ==")
print("== 2 - Pop Mie ==")
print("== 3 - Teh Pucuk ==")

daftar_belanja = ["mie instant", "pop mie", "teh pucuk"]

while True:

    daftar = int(input("pilih nomor"))

    if daftar == '0':
        break

    if daftar == 1:
        print(f'anda memesan {daftar_belanja[0]}')
    elif daftar == 2:
        print(f'anda memesan pop mie {daftar_belanja[1]}')
    elif daftar == 3:
        print(f'anda memesan teh pucuk {daftar_belanja[2]}')
    else:
        print(f'anda tidak memesan apapun')

    while True:
        pilihan = input("apakah anda mau memesan lagi? Y or N").lower()
        if pilihan in ['y', 'n']:
            break

    if pilihan == 'n':
        break
