#Membuka file untuk menulis data 
file = open('data.txt', 'w')

#Menulis data ke file 
file.write('Wowwww, Keren!\n') 
file.write('Ini adalah contoh data yang ditulis ke file.\n')

#  Membaca isi file dan menampilkan baris per baris 
file_path = "data.txt" 
with open(file_path, "r") as file: 
    for line in file: 
        print(line)

# Membaca seluruh isi file dan menyimpannya dalam list
file_path = "data.txt" 
with open(file_path, "r") as file: 
    lines = file.readlines()

# Menampilkan isi file dengan pemisah baris baru 
print("\n".join(lines))

#Menutup file  
file.close()