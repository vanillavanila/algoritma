import random

# Menampilkan aturan permainan
print("Selamat datang di permainan Batu-Kertas-Gunting!\n")
print("Aturan Kemenangan:")
print("Batu vs Kertas -> Kertas menang")
print("Batu vs Gunting -> Batu menang")
print("Kertas vs Gunting -> Gunting menang\n")

pilihan = ["Batu", "Kertas", "Gunting"]

while True:

    print("Pilih salah satu opsi:")
    print("1 - Batu")
    print("2 - Kertas")
    print("3 - Gunting")

    # Validasi input pengguna
    try:
        pilihan_user = int(input("Masukkan pilihan Anda: "))
    except ValueError:
        print("Harap masukkan angka yang valid.\n")
        continue

    while pilihan_user < 1 or pilihan_user > 3:
        pilihan_user = int(input("Harap masukkan pilihan yang valid (1-3): "))

    # Pilihan pengguna
    nama_pilihan_user = pilihan[pilihan_user - 1]

    print("\nPilihan Anda adalah:", nama_pilihan_user)
    print("Sekarang giliran Komputer...")

    # Pilihan komputer
    pilihan_komputer = random.randint(1, 3)
    nama_pilihan_komputer = pilihan[pilihan_komputer - 1]

    print("Pilihan Komputer adalah:", nama_pilihan_komputer)
    print(nama_pilihan_user, "vs", nama_pilihan_komputer)

    # Menentukan pemenang
    if pilihan_user == pilihan_komputer:
        print("<== Seri / Imbang! ==>")

    elif (
        (pilihan_user == 1 and pilihan_komputer == 3) or
        (pilihan_user == 2 and pilihan_komputer == 1) or
        (pilihan_user == 3 and pilihan_komputer == 2)
    ):
        print("<== Anda Menang! ==>")

    else:
        print("<== Komputer Menang! ==>")

    # Bermain lagi
    while True:
        jawaban = input("\nApakah Anda ingin bermain lagi? (Y/N): ").lower()

        if jawaban in ['y', 'n']:
            break

        print("Harap masukkan Y atau N.")

    if jawaban == 'n':
        break

    print()

print("\nTerima kasih telah bermain!")