#perubahan suhu dari kelvin ke yang lain
print("pilih rumus konversi")
print("1- dari kelvin ke celcius")
print("2- dari kelvin ke reaumure")
print("3- dari kelvin ke fahrenheit")

angka = input("masukan pilihan (1, 2, 3): ")

if angka == '1':
    K = float(input("masukan nilai kelvin: "))
    Kelvin = K - 273.15
    print(f"hasil dari konversi kelvin ke celcius {Kelvin}")
elif angka == '2': 
    K = input("masukan nilai kelvin")
    Kelvin= 4/5 * (K - 273)
    print(f"hasil dari konversi kelvin ke celcius {Kelvin}")
elif angka == '3': 
    K = input("masukan nilai kelvin")
    Kelvin= 4/5 * (K - 273)
    print(f"hasil dari konversi kelvin ke celcius {Kelvin}")
else:
    print('0')
    
