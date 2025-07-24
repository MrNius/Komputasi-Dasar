def pasangan(list1, list2):
    # Mengecek apakah kedua masukan adalah list dan memiliki jumlah elemen yang sama
    if not (isinstance(list1, list) and isinstance(list2, list)) or len(list1) != len(list2):
        print("Salah: masukkan harus berupa 2 buah list dengan jumlah elemen yang sama.")
        return []
    # Membuat pasangan elemen dari kedua list
    pasangan_list = [[list1[i], list2[i]] for i in range(len(list1))]
    return pasangan_list

# Contoh penggunaan
a = ['p', 'q', 'r']
b = [5, 6, 9]
print("Pasangan =", pasangan(a, b))

a = 7
b = 5
print("Pasangan =", pasangan(a, b))

a = ['p', 'q', 'r']
b = [5, 6]
print("Pasangan =", pasangan(a, b))
