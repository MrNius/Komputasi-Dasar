def pisahkan(pasangan_list):
    # Periksa apakah masukan adalah list dan tidak kosong
    if not (isinstance(pasangan_list, list) and pasangan_list):
        print("Salah: masukkan harus berupa sebuah list dari list pasangan.")
        return []

    # Pisahkan pasangan-pasangan menjadi dua list terpisah
    elemen_pertama = [pasangan[0] for pasangan in pasangan_list]
    elemen_kedua = [pasangan[1] for pasangan in pasangan_list]

    return [elemen_pertama, elemen_kedua]

# Contoh penggunaan
c = [['p', 5], ['q', 6], ['r', 9]]
hasil = pisahkan(c)
print("List asli =", hasil)

c = 5
hasil = pisahkan(c)
print("List asli =", hasil)

c = []
hasil = pisahkan(c)
print("List asli =", hasil)
