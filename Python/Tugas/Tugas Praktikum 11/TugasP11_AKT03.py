import random
import math

list_objek = ["BujurSangkar", "PersegiPanjang", "SegitigaSamaSisi", "SegitigaSikuSiku", "Lingkaran"]

class BangunDatar:
    def __init__(self, jenis):
        self.jenis = jenis
        self.ukuran = self.generate_ukuran()

    def generate_ukuran(self):
        return random.randint(1, 10)

    def hitung_luas(self):
        if self.jenis == "BujurSangkar":
            return self.ukuran ** 2
        elif self.jenis == "PersegiPanjang":
            return self.ukuran * random.randint(1, 10)
        elif self.jenis == "SegitigaSikuSiku":
            return 0.5 * self.ukuran * random.randint(1, 10)
        elif self.jenis == "SegitigaSamaSisi":
            return (math.sqrt(3) / 4) * self.ukuran ** 2
        elif self.jenis == "Lingkaran":
            return math.pi * (self.ukuran ** 2)

U_BujurSangkar = []
U_PersegiPanjang = []
U_SegitigaSikuSiku = []
U_SegitigaSamaSisi = []
U_Lingkaran = []

L_BujurSangkar = []
L_PersegiPanjang = []
L_SegitigaSikuSiku = []
L_SegitigaSamaSisi = []
L_Lingkaran = []

total_luas_bujur_sangkar = 0
total_luas_persegi_panjang = 0
total_luas_segitiga_siku_siku = 0
total_luas_segitiga_sama_sisi = 0
total_luas_lingkaran = 0

# Run pertama
print('='*20, 'Jumlah objek berkisar antara 6 - 12 objek', '='*20)
x = int(input('Masukkan banyaknya jumlah objek yang ingin dibangkitkan (6-12 objek) : '))
while x > 12 or x < 6:
    print('>>> Jumlah input harus antara 6-12')
    x = int(input('Masukkan banyaknya jumlah objek yang ingin dibangkitkan (6-12 objek) : '))
print()
for i in range(x):
    x = random.sample(list_objek, 1)[0]  # Mengambil elemen pertama dari list hasil sampling
    y = BangunDatar(x)
    print("Jenis:", y.jenis)
    print("Ukuran:", y.ukuran)
    luas = y.hitung_luas()
    print("Luas:", luas, "\n")

    if x == "BujurSangkar":
        U_BujurSangkar.append(y.ukuran)
        L_BujurSangkar.append(luas)
        total_luas_bujur_sangkar += luas
    elif x == "PersegiPanjang":
        U_PersegiPanjang.append(y.ukuran)
        L_PersegiPanjang.append(luas)
        total_luas_persegi_panjang += luas
    elif x == "SegitigaSikuSiku":
        U_SegitigaSikuSiku.append(y.ukuran)
        L_SegitigaSikuSiku.append(luas)
        total_luas_segitiga_siku_siku += luas
    elif x == "SegitigaSamaSisi":
        U_SegitigaSamaSisi.append(y.ukuran)
        L_SegitigaSamaSisi.append(luas)
        total_luas_segitiga_sama_sisi += luas
    elif x == "Lingkaran":
        U_Lingkaran.append(y.ukuran)
        L_Lingkaran.append(luas)
        total_luas_lingkaran += luas
print("=== Ukuran, Luas, dan Total Luas Masing-Masing Bangun Datar ===\n")
print("1) Bujur Sangkar", "\n   Ukuran:", U_BujurSangkar, "\n   Luas:", L_BujurSangkar, "\n   Total Luas:", total_luas_bujur_sangkar, "\n")
print("2) Persegi Panjang", "\n   Ukuran:", U_PersegiPanjang, "\n   Luas:", L_PersegiPanjang, "\n   Total Luas:", total_luas_persegi_panjang,"\n")
print("3) Segitiga Sama Sisi", "\n   Ukuran:", U_SegitigaSamaSisi, "\n   Luas:", L_SegitigaSamaSisi, "\n   Total Luas:", total_luas_segitiga_sama_sisi, "\n")
print("4) Segitiga Siku Siku", "\n   Ukuran:", U_SegitigaSikuSiku, "\n   Luas:", L_SegitigaSikuSiku, "\n   Total Luas:", total_luas_segitiga_siku_siku, "\n")
print("5) Lingkaran:", "\n   Ukuran:", U_Lingkaran, "\n   Luas:", L_Lingkaran, "\n   Total Luas:", total_luas_lingkaran, "\n")

#Run kedua
print()
print('='*20, 'Jumlah objek berkisar antara 40 - 60 objek', '='*20)
x = int(input('Masukkan banyaknya jumlah objek yang ingin dibangkitkan (40-60 objek): '))
while x > 60 or x < 40:
    print('>>> Jumlah input harus antara 40-60')
    x = int(input('Masukkan banyaknya jumlah objek yang ingin dibangkitkan (40-60 objek) : '))
print()
for i in range(x):
    x = random.sample(list_objek, 1)[0]  # Mengambil elemen pertama dari list hasil sampling
    y = BangunDatar(x)
    print("Jenis:", y.jenis)
    print("Ukuran:", y.ukuran)
    luas = y.hitung_luas()
    print("Luas:", luas, "\n")

    if x == "BujurSangkar":
        U_BujurSangkar.append(y.ukuran)
        L_BujurSangkar.append(luas)
        total_luas_bujur_sangkar += luas
    elif x == "PersegiPanjang":
        U_PersegiPanjang.append(y.ukuran)
        L_PersegiPanjang.append(luas)
        total_luas_persegi_panjang += luas
    elif x == "SegitigaSikuSiku":
        U_SegitigaSikuSiku.append(y.ukuran)
        L_SegitigaSikuSiku.append(luas)
        total_luas_segitiga_siku_siku += luas
    elif x == "SegitigaSamaSisi":
        U_SegitigaSamaSisi.append(y.ukuran)
        L_SegitigaSamaSisi.append(luas)
        total_luas_segitiga_sama_sisi += luas
    elif x == "Lingkaran":
        U_Lingkaran.append(y.ukuran)
        L_Lingkaran.append(luas)
        total_luas_lingkaran += luas
print("=== Ukuran, Luas, dan Total Luas Masing-Masing Bangun Datar ===\n")
print("1) Bujur Sangkar", "\n   Ukuran:", U_BujurSangkar, "\n   Luas:", L_BujurSangkar, "\n   Total Luas:", total_luas_bujur_sangkar, "\n")
print("2) Persegi Panjang", "\n   Ukuran:", U_PersegiPanjang, "\n   Luas:", L_PersegiPanjang, "\n   Total Luas:", total_luas_persegi_panjang,"\n")
print("3) Segitiga Sama Sisi", "\n   Ukuran:", U_SegitigaSamaSisi, "\n   Luas:", L_SegitigaSamaSisi, "\n   Total Luas:", total_luas_segitiga_sama_sisi, "\n")
print("4) Segitiga Siku Siku", "\n   Ukuran:", U_SegitigaSikuSiku, "\n   Luas:", L_SegitigaSikuSiku, "\n   Total Luas:", total_luas_segitiga_siku_siku, "\n")
print("5) Lingkaran:", "\n   Ukuran:", U_Lingkaran, "\n   Luas:", L_Lingkaran, "\n   Total Luas:", total_luas_lingkaran, "\n")
