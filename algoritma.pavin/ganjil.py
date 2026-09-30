# a) Membuat list kosong bernama belanja
belanja = []

# b) Meminta pengguna memasukkan 5 nama barang (loop)
for i in range(5):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    belanja.append(barang)

print("\n--- Daftar Belanja ---")

# c) Menampilkan daftar belanja bernomor
for nomor, item in enumerate(belanja, start=1):
    print(f"{nomor}. {item}")

print("\n--- Informasi Daftar ---")

# d) Menampilkan total item dan item ke-3 dalam daftar
print(f"Total item dalam daftar belanja: {len(belanja)}")
print(f"Item ke-3 dalam daftar: {belanja[2]}")