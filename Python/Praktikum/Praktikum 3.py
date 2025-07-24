# Data yang di proses
data =[4, 8, 5, 1, 7, 6, 2, 10]

#Mencari nilai minimum dan maksimum
min = data[0]
max = data[0]
for i in range(1,len(data)):
    if data[i] < min:
        min = data[i]
    if data[i] > max:
        max = data[i]

#Mencari jumlah kumulatif dari data
total = data[0]
for i in range(1,len(data)):
    total = total + data[i]
if len(data)==0:
    total=0
##total = 0
##for i in data:
##    total = total + i
#(Ini lebih efisien)

#Menghitung nilai rata-rata
rata_rata = total/len(data)

#Menampilkan hasil pemrosesan
##Kalau pake koma gak perlu pake 'str', kalau pake '+' harus pake 'str'
print('Data yang diberikan adalah: '+str(data))
print('Nilai minimum dari data adalah '+str(min))
print('Nilai maksimum dari data adalah '+str(max))
print('Nilai rata-rata data tersebut adalah ', rata_rata)

#Menampilkan angka random
import random

##Angka random 0<x<1
random.random()

##Angka random bilangan bulat
random.randint(1,10)

##Random sampel dari list
random.sample(['a', 'b', 'c', 'kopi', 'teh'],3)

##Random sampel dengan interval
random.sample(range(0,101),10)

##Random sampel dengan awal diketahui
random.seed(23)

##Memisahkan data yang lebih rendah dan lebih tinggi dari rata-rata
kurang_rata = 0
lebih_rata = 0
for i in data:
    if i < rata_rata:
        kurang_rata = kurang_rata + 1
               
    if i > rata_rata:
        lebih_rata =lebih_rata + 1
