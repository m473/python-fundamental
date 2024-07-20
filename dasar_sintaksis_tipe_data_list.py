daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
print('Tampilkan variabel daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')   # Looping for in
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print("\nTampilkan dengan for in range")
for i in range (0,len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Mate', -313, 345]  # tipe data dengan isi berbeda
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("Kembalikan nilai awal daftar_buku")
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
print("\nTambahkan 1 buku baru")
daftar_buku.append("Dua Dunia")     # nambahin data list di paling belakang
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print()
print("Hapus isi list")
daftar_buku.clear()   # menghapus isi list
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("Membalikkan isi list")
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
daftar_buku[0] = '8 Habits'     # mengganti elemen 1
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# mengambil data ke-.. pada elemen list
print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# menyimpan hasil pop
print('\nBuku yang diambil tadi')
print(buku)

print('\nPOP')
daftar_buku.pop()     # mengambil data yang paling belakang
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPOP-1')
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
daftar_buku.pop(-1)   # mengambil data ke-1 dari belakang. dimulai dengan angka 1 bukan 0
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


