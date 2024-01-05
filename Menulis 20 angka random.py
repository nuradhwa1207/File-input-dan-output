import random

file = open('angka_acak.txt', 'w')
# Membuat 20 angka acak antara 1 sampai 100
angka_acak = [random.randint(1, 100) for _ in range(20)]
for angka in angka_acak:
    file.write(f"{angka}\n")

# Membaca seluruh isi file dan menyimpannya dalam list
file_path = 'angka_acak.txt' 
with open('angka_acak.txt', 'r') as file:
    lines = file.readlines()  
    print("Angka ganjil dari file 'angka_acak.txt':")
    for line in lines:
        angka = int(line.strip())  # Mengubah teks menjadi angka
        if angka % 2 != 0:  # Memeriksa apakah angka ganjil
            print(angka)  # Menampilkan angka ganjil

file.close()