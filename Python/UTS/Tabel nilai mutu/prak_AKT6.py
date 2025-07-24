def hitung_nakhir(uts,uas):
    return (uts+uas)/2

#                        HURUF MUTU   ANGKA MUTU
#-----------------------------------------
#  0 <= nilai akhir < 25          E   0
# 25 <= nilai akhir < 40          D   1
# 40 <= nilai akhir < 60          C   2
# 60 <= nilai akhir < 80          B   3
# 80 <= nilai akhir <= 100        A   4
#-----------------------------------------
def hitung_hmutu(nakhir):
    if nakhir >= 0 and nakhir < 25:
        return 'E'
    elif nakhir >= 25 and nakhir < 40:
        return 'D'
    elif nakhir >= 40 and nakhir < 60:
        return 'C'
    elif nakhir >= 60 and nakhir < 80:
        return 'B'
    elif nakhir >= 80 and nakhir < 100:
        return 'A'

def tampil_data(nim, nama, kelompok, uts, uas, nakhir, hmutu):
    print('FILE BERISI', len(nim), 'DATA NILAI MAHASISWA')
    print('{:11} {:38} {:8} {:3} {:3} {:5} {:5}'.format('NIM','NAMA','KELOMPOK','UTS','UAS','N.AKHIR','H.MUTU'))
    for i in range(len(nim)):
        print('{:13} {:40} {:5} {:3} {:4} {:5} {:6}'.format(nim[i], nama[i], kelompok[i], uts[i], uas[i], nakhir[i], hmutu[i]))
    return
    
# buka file data
infile = open('F:/Pyhton/Praktikum/NilaiUTS-UAS_Prediksi.csv')
baris=infile.readline()
# baca data dan masukkan ke dalam basis data
nim=[]
nama=[]
kelompok=[]
uts=[]
uas=[]
nakhir=[]
hmutu=[]
for i in range(1000):
    baris = infile.readline()
    if baris == '':
        break
    baris = baris.strip(';')
    baris_baru = baris.split(';')
    nim.append(baris_baru[0])
    nama.append(baris_baru[1])
    kelompok.append(baris_baru[2])
    nuts = int(baris_baru[3])
    uts.append(nuts)
    nuas = int(baris_baru[4])
    uas.append(nuas)
    nilai_akhir = hitung_nakhir(nuts,nuas)
    nakhir.append(nilai_akhir)
    hmutu.append(hitung_hmutu(nilai_akhir))
infile.close()

# tampilkan data donk!
tampil_data(nim, nama, kelompok, uts, uas, nakhir, hmutu)

# lengkapi kolom huruf mutu

# tampilkan lagi data dalam bentuk yang 'manis'

# hitung dan tampilkan nilai rata-rata dari uts, uas dan nilai akhir
jumUTS=0
jumUAS=0
jumnakhir=0
ndata=0
for i in range(163):
    jumUTS=jumUTS+uts[i]
    jumUAS=jumUAS+uas[i]   
    jumnakhir=jumnakhir+nakhir[i]
    ndata=ndata+1
rataUTS=jumUTS/ndata
rataUAS=jumUAS/ndata
rataNA=jumnakhir/ndata
hmA=0
hmB=0
hmC=0
hmD=0
hmE=0
for i in range(163):
    if hmutu[i] == 'A':
        hmA=hmA+1
    elif hmutu[i] == 'B':
        hmB=hmB+1
    elif hmutu[i] == 'C':
        hmC=hmC+1
    elif hmutu[i] == 'D':
        hmD=hmD+1
    elif hmutu[i] == 'E':
        hmE=hmE+1
print()
print('TERDAPAT', len(nim), 'DATA NILAI MAHASISWA')
print("Rata-rata nilai UTS",rataUTS)
print("rata-rata nilai UAS",rataUAS)
print("Rata-rata nilai Akhir",rataNA)
print()
print('Huruf mutu:\nA',hmA,'mahasiswa\nB',hmB,'mahasiswa\nC',hmC,'mahasiswa\nD',hmD,'mahasiswa\nE',hmE,'mahasiswa')
# hitung dan tampilkan simpangan baku dari uts, uas dan nilai akhir

# hitung dan tampilkan indeks prestasi mata kuliah

# hitung statistik per fakultas
