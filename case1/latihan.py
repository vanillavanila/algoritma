alas   =   float(input("masukan alas: "))
tinggi =   float(input("masukan tinngi: "))
hasil  =   float(0.5 * alas * tinggi)

print(hasil)

a = 10

b = 2

print(a ** b)

nama = ['naruto', 'boboiboy', 'balmond']
hoby = ['main ff', 'main bola', 'main futsal']
umurn= [10, 20, 30]

for i, a, b in zip(nama, hoby, umurn):
    print(f"{i} hobinya {a} umurnya {b}")

    print(f"{nama} hobinya {hoby} umur {umurn}")

nama = "indra"

print(nama[-5])


ctx = 0

while (ctx < 10):
    ctx = ctx + 1
    print('indra')

for angka in range(10000):
    print(angka)

x = 10
y = 2

print(x + y)

x = int(input('masukan angka pertama: '))
y = int(input('masukan angka kedua: '))

hasil = x + y

output = print(f'hasil dari {x} + {y} = {hasil}')