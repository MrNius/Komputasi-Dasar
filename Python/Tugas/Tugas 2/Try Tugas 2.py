import random
jumlah_data = int(input("Masukkan jumlah data yang akan diproses: "))
data = random.sample(range(0,101),jumlah_data)
print('Data yang akan diproses adalah '+str(data))

frekuensi = {i: 0 for i in range(0, 101, 10)}
for nilai in data:
    for batas_bawah in range(0, 101, 10):
        if batas_bawah <= nilai <= batas_bawah + 10:
            frekuensi[batas_bawah] += 1

print()
print("===Distribusi Frekuensi===")
for batas_bawah in range(0, 100, 10):
    batas_atas = batas_bawah + 10
    bintang = '*' * frekuensi[batas_bawah]
    print(f"{batas_bawah+1}-{batas_atas}: {bintang}")
