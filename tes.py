# nama = "indra"

# for i in range(100):
#     i = nama
#     print(nama)


# sebut_nama = 1

# while sebut_nama <= 100:
#     print('indra')
#     sebut_nama +=1


# def hitung_gaji():
#     print("\n--- PROGRAM PENGGAJIAN KARYAWAN PT MAJU SEJAHTERA ---")
#     nama = input("Masukkan Nama Karyawan: ")
#     nik = input("Masukkan NIK: ")
#     jabatan = input("Jabatan (Administrasi / Teknisi / Supervisor): ").strip().lower()
    
#     try:
#         jam = int(input("Masukkan Jumlah Jam Kerja (1 bulan): "))
#     except ValueError:
#         print("Input jam kerja harus berupa angka!")
#         return True # Lanjutkan loop jika input salah

#     # Tentukan tarif per jam berdasarkan jabatan
#     if jabatan == 'administrasi':
#         tarif_normal = 25000
#     elif jabatan == 'teknisi':
#         tarif_normal = 35000
#     elif jabatan == 'supervisor':
#         tarif_normal = 50000
#     else:
#         print("Jabatan tidak valid! Silakan ulangi dengan benar.")
#         return True # Lanjutkan loop

#     # Perhitungan Jam Normal dan Jam Lembur
#     if jam > 160:
#         jam_normal = 160
#         jam_lembur = jam - 160
#     else:
#         jam_normal = jam
#         jam_lembur = 0

#     # Perhitungan Upah
#     gaji_pokok = jam_normal * tarif_normal
#     tarif_lembur_per_jam = tarif_normal * 1.5
#     upah_lembur = jam_lembur * tarif_lembur_per_jam
    
#     subtotal = gaji_pokok + upah_lembur
#     pajak = subtotal * 0.05
#     gaji_bersih = subtotal - pajak

#     # Menampilkan Laporan Terperinci sesuai Studi Kasus
#     print("\n==============================================")
#     print("            LAPORAN GAJI KARYAWAN           ")
#     print("==============================================")
#     print(f"Nama Lengkap             : {nama}")
#     print(f"NIK                      : {nik}")
#     print(f"Jabatan                  : {jabatan.capitalize()}")
#     print(f"Jumlah Jam Kerja         : {jam} jam")
#     print(f"Jumlah Jam Lembur        : {jam_lembur} jam")
#     print(f"Tarif Upah per Jam       : Rp{tarif_normal:,}")
#     print(f"Gaji Pokok               : Rp{gaji_pokok:,.0f}")
#     print(f"Upah Lembur              : Rp{upah_lembur:,.0f}")
#     print(f"Total Penghasilan (Bruto): Rp{subtotal:,.0f}")
#     print(f"Potongan Pajak (5%)      : Rp{pajak:,.0f}")
#     print(f"Total Gaji Bersih (Netto): Rp{gaji_bersih:,.0f}")
#     print("==============================================\n")
    
#     return True

# # Perulangan Utama (While Loop) untuk memproses banyak karyawan
# aktif = True
# while aktif:
#     hitung_gaji()
    
#     # Pertanyaan apakah ingin menghitung karyawan lain
#     pilihan = input("Apakah masih ada karyawan lain yang akan dihitung? (y/t): ").strip().lower()
#     if pilihan != 'y':
#         print("\nProgram selesai. Terima kasih!")
#         aktif = False


# def parameter(nama, kelas, alamat):
#     print(f"hallo {nama}")
#     print(f"kelaas {kelas}")
#     print(f"alamat {alamat}")
    
# parameter('indra', 12, 'ntah')

def sapa(nama, alamat, dus):
    print(f"nama {nama} dan alamat {alamat}")


nama = input("masukan nama: ")
alamat = input("masukan alamat: ")
sapa(nama, alamat)


# nama = input("masukan nama")

# print(nama)

# alamat = input("Masukan alamat:")

# print(alamat)

# print(f"{nama} dan {alamat}")