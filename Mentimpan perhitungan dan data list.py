# Contoh 1: Menyimpan hasil perhitungan ke file 
def hitung_luas_persegi(sisi):
    return sisi * sisi

#Buka file untuk menulis hasil perhitungan 
file = open('luas_persegi.txt', 'w')

#Hitung dan simpan hasil perhitungan ke file 
for i in range(1, 6): 
    luas = hitung_luas_persegi(i) 
    file.write(f"Sisi: {i}, Luas: {luas}\n")

# Tutup file setelah selesai menulis 
file.close()

#Contoh 2: Menyimpan data list ke file 
data_list = [10, 20, 30, 40, 50]

#Buka file untuk menulis data list 
file = open('data_list.txt', 'w')

#Simpan data list ke file 
for data in data_list: 
    file.write(str(data) + '\n')

#Tutup file setelah selesai menulis 
file.close()
