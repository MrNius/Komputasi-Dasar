### DATA 1
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Membaca data dari file Excel
NF1 = pd.read_excel(r'F:\Pyhton\UAS\Tugas08_NilaiFilsafat1.xlsx', usecols='A:J', skiprows=[68], index_col=0)

# Mengubah nilai NaN menjadi blank putih
NF1 = NF1.fillna('')

# Mengubah angka dengan koma 0 menjadi bilangan bulat
NF1[['UTS', 'UAS', 'Tugas']] = NF1[['UTS', 'UAS', 'Tugas']].applymap(lambda x: int(x) if x == x else x)

# Menghitung Nilai Akhir (NA) dengan bobot 35%, 40%, 25%
NF1['NA'] = NF1['UTS'] * 0.35 + NF1['UAS'] * 0.40 + NF1['Tugas'] * 0.25

# Membuat fungsi untuk mengkonversi Nilai Akhir ke Huruf Mutu
def HurufMutu(na):
    if na >= 80:
        return 'A'
    elif na >= 70:
        return 'AB'
    elif na >= 60:
        return 'B'
    elif na >= 50:
        return 'BC'
    elif na >= 40:
        return 'C'
    elif na >= 20:
        return 'D'
    else:
        return 'E'

# Mengaplikasikan fungsi nilai_ke_huruf_mutu untuk membuat kolom Huruf Mutu
NF1['HM'] = NF1['NA'].apply(HurufMutu)

# Menyimpan data yang sudah dilengkapi ke dalam file Excel baru
NF1.to_excel("Tugas08_NilaiFilsafat1_LENGKAP.xlsx", index=False)

# Menampilkan huruf mutu dan jumlah mahasiswa yang mendapatkannya dalam tabel
count_huruf_mutu = NF1['HM'].value_counts().sort_index()
print("Tabel Sebaran Huruf Mutu MK Filsafat Pertanian :")
table_huruf_mutu = tabulate(count_huruf_mutu.reset_index(), headers=['Huruf Mutu', 'Jumlah Mahasiswa'], tablefmt='pretty', showindex=False)
print(table_huruf_mutu)

# Membuat Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(count_huruf_mutu, labels=count_huruf_mutu.index, autopct=lambda p: '{:.0f}'.format(p * sum(count_huruf_mutu) / 100), startangle=90, counterclock=False)
plt.title('Sebaran Huruf Mutu\nMK Filsafat Pertanian')
plt.show()

# Menghitung indeks prestasi untuk setiap mahasiswa
NF1['Indeks Prestasi'] = NF1['HM'].map({'A': 4, 'AB': 3.5, 'B': 3, 'BC': 2.5, 'C': 2, 'D': 1, 'E': 0})

# Menghitung rata-rata indeks prestasi keseluruhan
indeks_prestasi_keseluruhan = round(NF1['Indeks Prestasi'].mean(), 2)

# Menampilkan tabel indeks prestasi keseluruhan
print("\nTabel Indeks Prestasi Filsafat Pertanian Keseluruhan:")
print(tabulate([["Keseluruhan", indeks_prestasi_keseluruhan]], headers=['Kelas', 'Indeks Prestasi'], tablefmt='pretty', numalign='center', floatfmt=".2f"))

# Menghitung Indeks Prestasi per kelas paralel
angka_mutu = {'A': 4, 'AB': 3.5, 'B': 3, 'BC': 2.5, 'C': 2, 'D': 1, 'E': 0}

def hitung_indeks_prestasi(data):
    return sum(angka_mutu[huruf_mutu] for huruf_mutu in data) / len(data)

# Menampilkan Indeks Prestasi per kelas paralel dalam tabel
kelas_paralel = NF1['Kelas'].unique()
indeks_prestasi_kelas = [round(hitung_indeks_prestasi(NF1[NF1['Kelas'] == kelas]['HM']), 2) for kelas in kelas_paralel]
print("\nTabel Indeks Prestasi Filsafat Pertanian Setiap Kelas Paralel :")
table_indeks_prestasi = tabulate(zip(kelas_paralel, indeks_prestasi_kelas), headers=['Kelas', 'Indeks Prestasi'], tablefmt='pretty', showindex=False)
print(table_indeks_prestasi)

# Membuat Bar Chart Indeks Prestasi per kelas paralel
kelas_paralel = NF1['Kelas'].unique()
indeks_prestasi_kelas = [hitung_indeks_prestasi(NF1[NF1['Kelas'] == kelas]['HM']) for kelas in kelas_paralel]

plt.figure(figsize=(8, 6))
bar_chart = plt.bar(kelas_paralel, indeks_prestasi_kelas, color='blue')
plt.xlabel('Kelas')
plt.ylabel('Indeks Prestasi')
plt.title('Indeks Prestasi Setiap Kelas Filsafat Pertanian')

# Menambahkan nilai rata-rata di atas setiap bar
for bar, rata_rata in zip(bar_chart, indeks_prestasi_kelas):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.05, f'{rata_rata:.2f}', ha='center', color='black')
plt.show()


### DATA 2
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Membaca data dari file Excel
NF2 = pd.read_excel(r'F:\Pyhton\UAS\Tugas08_NilaiFilsafat2.xlsx', usecols='A:J', skiprows=[2892], index_col=0)

# Mengubah nilai NaN menjadi blank putih
NF2 = NF2.fillna('')

# Mengubah angka dengan koma 0 menjadi bilangan bulat
NF2[['UTS', 'UAS', 'Tugas']] = NF2[['UTS', 'UAS', 'Tugas']].applymap(lambda x: int(x) if x == x else x)

# Menghitung Nilai Akhir (NA) dengan bobot 35%, 40%, 25%
NF2['NA'] = NF2['UTS'] * 0.35 + NF2['UAS'] * 0.40 + NF2['Tugas'] * 0.25

# Membuat fungsi untuk mengkonversi Nilai Akhir ke Huruf Mutu
def HurufMutu(na):
    if na >= 80:
        return 'A'
    elif na >= 70:
        return 'AB'
    elif na >= 60:
        return 'B'
    elif na >= 50:
        return 'BC'
    elif na >= 40:
        return 'C'
    elif na >= 20:
        return 'D'
    else:
        return 'E'

# Mengaplikasikan fungsi NilaiMutu untuk membuat kolom Huruf Mutu
NF2['HM'] = NF2['NA'].apply(HurufMutu)

# Menyimpan data yang sudah dilengkapi ke dalam file Excel baru
NF2.to_excel("Tugas08_NilaiFilsafat2_LENGKAP.xlsx", index=False)

# Menampilkan huruf mutu dan jumlah mahasiswa yang mendapatkannya dalam tabel
count_huruf_mutu = NF2['HM'].value_counts().sort_index()
print("\nTabel Sebaran Huruf Mutu MK Filsafat Pertanian :")
table_huruf_mutu = tabulate(count_huruf_mutu.reset_index(), headers=['Huruf Mutu', 'Jumlah Mahasiswa'], tablefmt='pretty', showindex=False)
print(table_huruf_mutu)

# Membuat Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(count_huruf_mutu, labels=count_huruf_mutu.index, autopct=lambda p: '{:.0f}'.format(p * sum(count_huruf_mutu) / 100), startangle=90, counterclock=False)
plt.title('Sebaran Huruf Mutu\nMK Filsafat Pertanian')
plt.show()

###### MENGHITUNG MAHASISWA YANG MENDAPATKAN NILAI MUTU TERTENTU PADA MASING MASING KELAS
### Membuat fungsi untuk mengkonversi Nilai Akhir ke Huruf Mutu
##def HurufMutu(na):
##    if na >= 80:
##        return 'A'
##    elif na >= 70:
##        return 'AB'
##    elif na >= 60:
##        return 'B'
##    elif na >= 50:
##        return 'BC'
##    elif na >= 40:
##        return 'C'
##    elif na >= 20:
##        return 'D'
##    else:
##        return 'E'
##
### Mengaplikasikan fungsi NilaiMutu untuk membuat kolom Huruf Mutu
##NF2['HM'] = NF2['NA'].apply(HurufMutu)
##
### Mengelompokkan data berdasarkan kelas dan nilai mutu
##grouped_data = NF2['HM'].groupby(['Kelas', 'Nilai Mutu']).size().reset_index(name='Jumlah Mahasiswa')
##
### Menampilkan tabel nilai mutu per kelas
##print("Tabel Nilai Mutu per Kelas:")
##print(tabulate(grouped_data, headers=['Kelas', 'Nilai Mutu', 'Jumlah Mahasiswa'], tablefmt='pretty', numalign='center'))
##
### Membuat grafik pie untuk setiap kelas
##kelas_paralel = NF2['Kelas'].unique()
##plt.figure(figsize=(12, 8))
##for kelas in kelas_paralel:
##    data_kelas = grouped_data[grouped_data['Kelas'] == kelas]
##    plt.subplot(2, 2, int(kelas[-1]))
##    plt.pie(data_kelas['Jumlah Mahasiswa'], labels=data_kelas['Nilai Mutu'], autopct=lambda p: '{:.0f}'.format(p * sum(count_huruf_mutu) / 100), startangle=90, counterclock=False)
##    plt.title(f'Grafik Pie Kelas {kelas}')
##plt.tight_layout()
##plt.show()
################

# Menghitung indeks prestasi untuk setiap mahasiswa
NF2['Indeks Prestasi'] = NF2['HM'].map({'A': 4, 'AB': 3.5, 'B': 3, 'BC': 2.5, 'C': 2, 'D': 1, 'E': 0})

# Menghitung rata-rata indeks prestasi keseluruhan
indeks_prestasi_keseluruhan = round(NF2['Indeks Prestasi'].mean(), 2)

# Menampilkan tabel indeks prestasi keseluruhan
print("\nTabel Indeks Prestasi Filsafat Pertanian Keseluruhan:")
print(tabulate([["Keseluruhan", indeks_prestasi_keseluruhan]], headers=['Kelas', 'Indeks Prestasi'], tablefmt='pretty', numalign='center', floatfmt=".2f"))

# Menghitung Indeks Prestasi per kelas paralel
angka_mutu = {'A': 4, 'AB': 3.5, 'B': 3, 'BC': 2.5, 'C': 2, 'D': 1, 'E': 0}

def hitung_indeks_prestasi(data):
    return sum(angka_mutu[huruf_mutu] for huruf_mutu in data) / len(data)

# Menampilkan Indeks Prestasi per kelas paralel dalam tabel
kelas_paralel = NF2['Kelas'].unique()
indeks_prestasi_kelas = [round(hitung_indeks_prestasi(NF2[NF2['Kelas'] == kelas]['HM']), 2) for kelas in kelas_paralel]
print("\nTabel Indeks Prestasi Filsafat Pertanian Setiap Kelas Paralel :")
table_indeks_prestasi = tabulate(zip(kelas_paralel, indeks_prestasi_kelas), headers=['Kelas', 'Indeks Prestasi'], tablefmt='pretty', showindex=False)
print(table_indeks_prestasi)

# Membuat Bar Chart Indeks Prestasi per kelas paralel
kelas_paralel = NF2['Kelas'].unique()
indeks_prestasi_kelas = [hitung_indeks_prestasi(NF2[NF2['Kelas'] == kelas]['HM']) for kelas in kelas_paralel]

plt.figure(figsize=(8, 6))
bar_chart = plt.bar(kelas_paralel, indeks_prestasi_kelas, color='blue')
plt.xlabel('Kelas')
plt.ylabel('Indeks Prestasi')
plt.title('Indeks Prestasi Setiap Kelas Filsafat Pertanian')

# Menambahkan nilai rata-rata di atas setiap bar
for bar, rata_rata in zip(bar_chart, indeks_prestasi_kelas):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.05, f'{rata_rata:.2f}', ha='center', color='black')
plt.xticks(rotation=90)
plt.show()
