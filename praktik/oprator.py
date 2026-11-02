print("""   █████████           ████                                       █████           █████            █████                                  ███ ███
 ███░░░░░███         ░░███                                      ░░███           ░░███            ░░███                                  ░███░███
░███    ░░░   ██████  ░███   ██████   █████████████    ██████   ███████       ███████   ██████   ███████    ██████   ████████    ███████░███░███
░░█████████  ███░░███ ░███  ░░░░░███ ░░███░░███░░███  ░░░░░███ ░░░███░       ███░░███  ░░░░░███ ░░░███░    ░░░░░███ ░░███░░███  ███░░███░███░███
 ░░░░░░░░███░███████  ░███   ███████  ░███ ░███ ░███   ███████   ░███       ░███ ░███   ███████   ░███      ███████  ░███ ░███ ░███ ░███░███░███
 ███    ░███░███░░░   ░███  ███░░███  ░███ ░███ ░███  ███░░███   ░███ ███   ░███ ░███  ███░░███   ░███ ███ ███░░███  ░███ ░███ ░███ ░███░░░ ░░░ 
░░█████████ ░░██████  █████░░████████ █████░███ █████░░████████  ░░█████    ░░████████░░████████  ░░█████ ░░████████ ████ █████░░███████ ███ ███
 ░░░░░░░░░   ░░░░░░  ░░░░░  ░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░░░    ░░░░░   ░░░░░░░░ ░░░░ ░░░░░  ░░░░░███░░░ ░░░ 
                                                                                                                                ███ ░███        
                                                                                                                               ░░██████         
                                                                                                                                ░░░░░░           """)

def plus():
    x = int(input("masukan angka pertama: "))
    y = int(input("masukan angka kedua: "))
    hasil = (x + y)
    print(f'hasil dari penjumlahan {x} + {y} = {hasil}')

def minus():
    x = int(input("masukan angka pertama: "))
    y = int(input("masukan angka kedua: "))
    hasil = (x - y)
    print(f'hasil dari pengurangan {x} - {y} = {hasil}')

def perkalian():
    x = int(input("masukan angka pertama: "))
    y = int(input("masukan angka kedua: "))
    hasil = (x * y)
    print(f'hasil dari perkalian {x} x {y} = {hasil}')

def pembagian():
    x = float(input("masukan angka pertama: "))
    y = float(input("masukan angka kedua: "))
    hasil =  (x / y)
    print(f'hasil dari pembagian {x} / {y} = {hasil}')

def modulo():
    x = float(input("masukan angka pertama: "))
    y = float(input("masukan angka kedua: "))
    hasil = (x % y)
    print(f'hasil dari sisa bagi {x} % {y} = {hasil}')

def pangkat():
    x = int(input("masukan angka pertama: "))
    y = int(input("masukan angka kedua: "))
    hasil = (x ** y)
    print(f'hasil dari pangkat {x} ** {y} = {hasil}')
    
def bagi_tanpa_koma():
    x = int(input("masukan angka pertama: "))
    y = int(input("masukan angka kedua: "))
    hasil = (x // y)
    print(f'hasil dari pembagian tanpa koma {x} // {y} = {hasil}')

def perhitungan():
    print("==== Mau melakukan oprasi perhitungan apa hari ini? ===")
    print("tambah, kurang, kali, bagi, sisa bagi, pangkat, pembagian tanpa koma")

    pilihan = str(input("masukan pilihan: "))

    if pilihan == 'tambah':
        plus()
    elif pilihan == 'kurang':
        minus()
    elif pilihan == 'kali':
        perkalian()
    elif pilihan == 'bagi':
        pembagian()
    elif pilihan == 'sisa bagi':
        modulo()
    elif pilihan == 'pangkat':
        pangkat()
    elif pilihan == 'pembagian tanpa koma':
        bagi_tanpa_koma()
    else:
        print("Sory pilihan tidak ada")

while True:
    perhitungan()

    while True:
        jawaban = input("Silahkan pilih Y untuk lanjut berhitung atau N untuk stop: ").lower()

        if jawaban in['y', 'n']:
            break
        print("Silahkan pilih y/n")

    if jawaban == 'n':
        print("""                                                                                
                                                                                
    __  __   ___                 .                             .--.   .           
    |  |/  `.'   `.             .'|                             |__| .'|           
    |   .-.  .-.   '          .'  |                             .--.<  |           
    |  |  |  |  |  |    __   <    |            __               |  | | |           
    |  |  |  |  |  | .:--.'.  |   | ____    .:--.'.         _   |  | | | .'''-.    
    |  |  |  |  |  |/ |   \ | |   | \ .'   / |   \ |      .' |  |  | | |/.'''. \   
    |  |  |  |  |  |`" __ | | |   |/  .    `" __ | |     .   | /|  | |  /    | |   
    |__|  |__|  |__| .'.''| | |    /\  \    .'.''| |   .'.'| |//|__| | |     | |   
                    / /   | |_|   |  \  \  / /   | |_.'.'.-'  /      | |     | |   
                    \ \._,\ '/'    \  \  \ \ \._,\ '/.'   \_.'       | '.    | '.  
                    `--'  `"'------'  '---'`--'  `"                 '---'   '---'  """)

        break