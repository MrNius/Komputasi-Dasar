# Bagian 1 ###

#Perintah w untuk membuat file baru
infile = open('D:\\IPB UNIVERSITY\\Pyhton\\Tugas\\Tugas 4\\News.txt')
outfile = open('D:\\IPB UNIVERSITY\\Pyhton\\Tugas\\Tugas 4\\News_copy.txt','w')
#Untuk baca 6 baris di file baru yang diambil dari file lama
table = str.maketrans('au', 'io')
for i in range(10):
    txt = infile.readline()
    if txt == '':
        break
    print(txt)
    outfile.write(txt.translate(table))
infile.close()
outfile.close()

infile = open('D:\\IPB UNIVERSITY\\Pyhton\\Tugas\\Tugas 4\\News.txt')
#Baca sebagai list, 1 elemen 1 baris
txt = infile.readlines()
print(txt)

#Baca perbaris
##Baca baris ke 1
txt = infile.readline()
print(txt,end='')
##Baca baris ke 2
txt = infile.readline()
print(txt,end='')
##Baca baris ke 3
txt = infile.readline()
print(txt,end='')

#Baca beberapa karakter pertama
txt = infile.read(22)
print(txt,end='')

#Baca sampai akhir
txt = infile.read()
print(txt,end='')

infile.close()


### Bagian 2 ###

infile = open('D:\\IPB UNIVERSITY\\Pyhton\\Tugas\\Tugas 4\\NilaiUTS_prediksi.csv')
total_UTS = 0
baris = infile.readline()
print('Data Prediksi NIlai UTS Mahasiswa')
print()
for i in range(1000):
    baris = infile.readline()
    if baris == '':
        break
    baris_baru = baris.strip().split(',')
    print(baris_baru[0], baris_baru[1],baris_baru[2],baris_baru[3])
    total_UTS = total_UTS + int(baris_baru[3])
infile.close()

rataUTS = total_UTS/(i+1)
print()
print('Total nilai UTS adalah', total_UTS)
print('Rata-rata nilai UTS adalah', rataUTS)
