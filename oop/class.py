# class attribute
class Kampus:
    nama = ""
    alamat = ""

# Encapsulation
class Mahasiswa:
    nama = ""
    nim = ""

    def perkenalan(self):
        print(f'Hallo saya {self.nama}')

    def sapa(self, nama):
        print(f"Hallo {nama}, nama saya {self.nama}")

    


kampus1 = Kampus()
kampus2 = Kampus()

# instance attribute 
mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 1111
mahasiswa1.nama = 'indra'
mahasiswa1.perkenalan()
mahasiswa1.sapa("balmond")

print(mahasiswa1.nim)
print(mahasiswa1.nama)


mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 1212
mahasiswa2.nama = 'budi'
mahasiswa2.perkenalan()
print(mahasiswa2.nim)
print(mahasiswa2.nama)

print(type(kampus1))
print(type(kampus2))

print(type(mahasiswa1))
print(type(mahasiswa2))
