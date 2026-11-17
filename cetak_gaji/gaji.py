

# data_karyawaan = {
#     "1000001": {"nama": "Bambang Pamungkas", "jabatan": "Teknisi", "jam": 160},
#     "2000002": {"nama": "Gio Nanda", "jabatan": "Supervisor", "jam": 170},
#     "3000003": {"nama": "Luna", "jabatan": "Administrasi", "jam": 175}
# }




def hitung_gaji(nik, nama, jabatan_karyawan, jam_kerja):
    if jabatan_karyawan == 'teknisi':
        tarif = 35000
    elif jabatan_karyawan == 'administrasi':
        tarif = 25000
    elif jabatan_karyawan == 'supervisor':
        tarif = 50000
    else:
        print("jabatan tidak ada! ")
        return 0

    if jam_kerja > 160:
        jam_normal = 160
        lembur = jam_kerja - jam_normal
    else:
        jam_normal = jam_kerja
        lembur = 0

    gaji_pokok = jam_normal * tarif
    bonus = lembur * tarif * 1.5
    subtotal = gaji_pokok + bonus
    pajak = subtotal * 0.05
    gaji_bersih = subtotal -pajak
    

    print(f"="* 20, "Laporan Gaji", "=" * 20)
    print(f"NIK: {nik} | Nama: {nama} | Jabatan: {jabatan} | Jam kerja: {jam} jam ")
    print(f"Tarif karyawaan (Rp{tarif})")
    print(f"Gaji awal sebelum bonus (Rp{gaji_pokok})")
    print(f"Bonus (Rp{bonus})")
    print(f"Gaji sebelum pajak (Rp{subtotal})")
    print(f"pajak (Rp{pajak})")
    print(f"Gaji bersih (Rp{gaji_bersih})")
    print(f"Jam kerja karyawan: {jam_normal} jam || Jam lembur: {lembur} jam")  



aktif = True
while aktif:

    try:
        nik = int(input("masukan nik: "))
        nama = input("nama: ")
        jabatan= input("jabatan: ").lower()
        jam = int(input("jam: "))
    except ValueError:
        print("masukan inputan yang benar!")
        continue

    hitung_gaji(nik, nama, jabatan, jam)

    pilihan = input("mau gaji karyawan lagi? (y/t) ")

    if pilihan != 'y':
        print("makasih")
        aktif = False
        
    
