import random
jumlah_data = int(input("Masukkan jumlah data yang akan diproses: "))
data = random.sample(range(0,101),jumlah_data)
print('Data yang akan diproses adalah',str(data))

#Interval 0-10
list1 = [0,1,2,3,4,5,6,7,8,9,10]
list1_baru = []
for i in range(0,len(data)):
    if data[i] in list1:
        list1_baru.append(data[i])
bintang1 = len(list1_baru)*'*'

#Interval 11-20
list2 = [11,12,13,14,15,16,17,18,19,20]
list2_baru = []
for i in range(0,len(data)):
    if data[i] in list2:
        list2_baru.append(data[i])
bintang2 = len(list2_baru)*'*'

#Interval 21-30
list3 = [21,22,23,24,25,26,27,28,29,30]
list3_baru = []
for i in range(0,len(data)):
    if data[i] in list3:
        list3_baru.append(data[i])
bintang3 = len(list3_baru)*'*'

#Interval 31-40
list4 = [31,32,33,34,35,36,37,38,39,40]
list4_baru = []
for i in range(0,len(data)):
    if data[i] in list4:
        list4_baru.append(data[i])
bintang4 = len(list4_baru)*'*'

#Interval 41-50
list5 = [41,42,43,44,45,46,47,48,49.50]
list5_baru = []
for i in range(0,len(data)):
    if data[i] in list5:
        list5_baru.append(data[i])
bintang5 = len(list5_baru)*'*'

#Interval 51-60
list6 = [51,52,53,54,55,56,57,58,59,60]
list6_baru = []
for i in range(0,len(data)):
    if data[i] in list6:
        list6_baru.append(data[i])
bintang6 = len(list6_baru)*'*'

#Interval 61-70
list7 = [61,62,63,64,65,66,67,68,69,70]
list7_baru = []
for i in range(0,len(data)):
    if data[i] in list7:
        list7_baru.append(data[i])
bintang7 = len(list7_baru)*'*'

#Interval 71-80
list8 = [71,72,73,74,75,76,77,78,79,80]
list8_baru = []
for i in range(0,len(data)):
    if data[i] in list8:
        list8_baru.append(data[i])
bintang8 = len(list8_baru)*'*'

#Interval 81-90
list9 = [81,82,83,84,85,86,87,88,89,90]
list9_baru = []
for i in range(0,len(data)):
    if data[i] in list9:
        list9_baru.append(data[i])
bintang9 = len(list9_baru)*'*'

#Interval 91-100
list10 = [91,92,93,94,95,96,97,98,99,100]
list10_baru = []
for i in range(0,len(data)):
    if data[i] in list10:
        list10_baru.append(data[i])
bintang10 = len(list10_baru)*'*'

#Menampilkan distribusi frekuensi
print()
print("===Distribusi Frekuensi===")
print("0-10:"+str(bintang1))
print("11-20:"+str(bintang2))
print("21-30:"+str(bintang3))
print("31-40:"+str(bintang4))
print("41-50:"+str(bintang5))
print("51-60:"+str(bintang6))
print("61-70:"+str(bintang7))
print("71-80:"+str(bintang8))
print("81-90:"+str(bintang9))
print("91-100:"+str(bintang10))
