"""
Program perulangan membaca buku
"""
jumlah_buku = 10
print('Ibu berkata : "Baca semua bukumu"')
print()

jumlah_buku_yang_sudah_dibaca = 9
print(f"jumlah Buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")
print()

for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku_yang_sudah_dibaca+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} "
          f"sudah dibaca ")

print()
print(f"JUmlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

# tanpa for
