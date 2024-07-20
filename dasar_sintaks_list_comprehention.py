# LIST COMPREHENSION
print('\nPerintah Del (menghapus)')
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
del daftar_buku[2]   # menghapus sesuai dengan elemen indexnya
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list komprehension')
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
del daftar_buku[:]   # menghapus semua isi list --> sama dengan "del daftar_buku[0:]"
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# [start:end] [dimulai index berapa : jumlahnya berapa]
# 1 : 3 --> irisan antara dimulai dari index ke 1 (dari 0) dengan jumlah sebanyak 3 (dari 1)
print('\nPerintah Del dengan list komprehension start')
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
# del daftar_buku[1:3]   # yang dihapus 9 habits dan 11 habits
del daftar_buku[1:-2]    # yang dihapus 9 habits aja. dimulai dari 9 habits sampai dengan -2 dari belakang itu 11 habits, 11 habits dipertahankan
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list komprehension step')
daftar_buku = ['7 Habits','9 Habits', '11 Habits', 'Box of Live']
# del daftar_buku[0::1]  # start:end:step, dimulai dari index 0, setiap 1 langkah dihapus --> hasil semua data kehapus
del daftar_buku[0::2]  # start:end:step, dimulai dari index 0, setiap 2 langkah dihapus
# --> hasil 9 habits dan box of live
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

# LIST BARU
print('\nMembuat List Baru')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku    # nama beda tetapi mengacu list yang sama
print('\nDaftar Buku')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Daftar Buku Lama di delete, tetapi buku baru tidak muncul
print('\nMembuat List Baru')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku    # nama beda tetapi mengacu list yang sama
print('\nDaftar Buku')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
del daftar_buku[:]     # daftar buku baru kehapus karena mengacu hal yang sama dengan buku lama
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

# Daftar Buku Lama di delete, buku baru  muncul
print('\nMembuat List Baru')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku [:]   # copy semua list yang ada di daftar_buku ke daftar_buku_baru
print('\nDaftar Buku Lama')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
del daftar_buku[:]      # daftar buku lama terhapus tidak terpengaruh dengan daftar buku baru
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru - Ganjil')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku [0::2]   # copy data ganjil pada list daftar_buku ke daftar_buku_baru
print('\nDaftar Buku Lama')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru - Ganjil - Sederhana')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
print(daftar_buku[0::2])

print('\nMembuat List Baru - Genap')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku [1::2]   # copy data genap pada list daftar_buku ke daftar_buku_baru
print('\nDaftar Buku Lama')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat List Baru - Data ujung tidak dipakai')
daftar_buku = ['1. Seven Habits','2. Nine Habits', '3. Eleven Habits', '4. Box of Live']
daftar_buku_baru = daftar_buku [0:-1]
print('\nDaftar Buku Lama')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nDaftar Buku Baru')
del daftar_buku[:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])