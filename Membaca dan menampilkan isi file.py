

# Contoh 1: Membaca isi file dan menampilkan baris per baris 
file_path = "aini.txt" 
with open(file_path, "r") as file: 
    for line in file: 
        print(line)

# Contoh 2: Membaca seluruh isi file dan menyimpannya dalam 1 
file_path = "aini.txt" 
with open(file_path, "r") as file: 
    lines = file.readlines()

# Menampilkan isi file dengan pemisah baris baru 
print("\n".join(lines))