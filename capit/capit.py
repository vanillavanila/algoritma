import random


menang = 5
percobaan = 0

while percobaan < menang:
    percobaan +=1
    input(f"silahkan masukan angak berapapun sampe anda menang...")

    print(f"\n coba lagi..")

hasil = random.choice([True, False])
print("usaha yang bagus")



if hasil:
    print("yeee anda menang")
else:
    print("gagal")