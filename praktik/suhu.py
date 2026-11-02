# C = float(input('celcius '))

# hasil =4/5 * C

# C = float(input('celcius'))

# hasil = 9/5 * C + 32
# print(f'HASIL DARI KONVERSI CELCIUS KE FRANHIDE {hasil}')

print("=== Pilih mau konversi ke mana ===")
print("1 - celcius ke reamur")
print("2 - celcius ke farenheit")
print("3 - celcius ke kelvin")
print("4 - reamur ke celcius")
print("5 - reamur ke farenheit")
print("6 - reamur ke kelvin")
print("7 - farenheit ke celcius")
print("8 - farenheit ke reamur")
print("9 - farenheit ke kelvin")
print("10 - kelvin ke celcius")
print("11 - kelvin ke reamur")
print("12 - kelvin ke farenheit")




angka = input("masukan pilihan (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12): ")


if angka == '1':
    C = float(input("masukan suhu dalam celcius: "))
    hasil = 4/5 * C
    print(f'hasil konversi: {hasil}')
elif angka == '2':
    C = float(input("masukan suhu dalam celcius: "))
    hasil = (9/5 * C) + 32
    print(f'hasil konversi: {hasil}')
elif angka == '3':
    C = float(input("masukan suhu dalam celcius: "))
    hasil = C + 273.15
    print(f'hasil konversi: {hasil}')
elif angka == '4':
    R = float(input("masukan suhu dalam reamur: "))
    hasil = 5/4 * R
    print(f'hasil konversi: {hasil}')
elif angka == '5':
    R = float(input("masukan suhu dalam reamur: "))
    hasil = 9/4 * R + 32
    print(f'hasil konversi: {hasil}')
elif angka == '6':
     R = float(input("masukan suhu dalam reamur: "))
     hasil = 5/4 * R + 273.15
     print(f'hasil konversi: {hasil}')
elif angka == '7':
    F = float(input("masukan suhu dalam farenheit: "))
    hasil = 5/9 * (F - 32)
    print(f'hasil konversi: {hasil}')
elif angka == '8':
    F = float(input("masukan suhu dalam farenheit: "))
    hasil = 4/9 * (F - 32)
    print(f'hasil konversi: {hasil}')
elif angka == '9':
    F = float(input("masukan suhu dalam farenheit: "))
    hasil = 5/9 * (F - 32) + 273
    print(f'hasil konversi: {hasil}')
elif angka == '10':
    K = float(input("masukan suhu dalam kelvin: "))
    hasil = K - 273
    print(f'hasil konversi: {hasil}')
elif angka == '11':
    K = float(input("masukan suhu dalam kelvin: "))
    hasil = 4/5 * (K - 273)
    print(f'hasil konversi: {hasil}')
elif angka == '12':
    K = float(input("masukan suhu dalam kelvin: "))
    hasil = 9/5 * (K - 273) + 32
    print(f'hasil konversi: {hasil}')
else:
    print("pilihan tidak valid!")
    
