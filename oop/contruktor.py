# tanpa contruktor
class Mahasiswa:
    nim = 0
    nama = ""

    def setup(self, nim, nama):
        self.nim = nim 
        self.nama = nama

mhs = Mahasiswa()
mhs.setup(1111, 'indra')

print(mhs.nim)
print(mhs.nama)

# menggunakan contruktor

class Siswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim 
        self.nama = nama

murid = Siswa(1212, 'balmond')

print(murid.nim)
print(murid.nama)