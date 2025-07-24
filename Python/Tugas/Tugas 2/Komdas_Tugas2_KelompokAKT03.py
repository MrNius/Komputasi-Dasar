import random
jumlah_data = int(input("Masukkan jumlah data yang akan diproses: "))
data = random.sample(range(0,101),jumlah_data)
print('Data yang akan diproses adalah :')
print (str(data))

#Data dalam interval
data_interval1 = ''
for i in data:
	if i in range (0,11):
		data_interval1 = data_interval1 + '*'
		
data_interval2 = ''
for i in data:
	if i in range (11,21):
		data_interval2 = data_interval2 + '*'
		
data_interval3 = ''
for i in data:
	if i in range (21,31):
		data_interval3 = data_interval3 + '*'
		
data_interval4 = ''
for i in data:
	if i in range (31,41):
		data_interval4 = data_interval4 + '*'
		
data_interval5 = ''
for i in data:
	if i in range (41,51):
		data_interval5 = data_interval5 + '*'
		
data_interval6 = ''
for i in data:
	if i in range (51,61):
		data_interval6 = data_interval6 + '*'
		
data_interval7 = ''
for i in data:
	if i in range (61,71):
		data_interval7 = data_interval7 + '*'
		
data_interval8 = ''
for i in data:
	if i in range (71,81):
		data_interval8 = data_interval8 + '*'
		
data_interval9 = ''
for i in data:
	if i in range (81,91):
		data_interval9 = data_interval9 + '*'
		
data_interval10 = ''
for i in data:
	if i in range (91,101):
		data_interval10 = data_interval10 + '*'

#Menampilkan data distribusi frekuensi dalam diagram
print()
print("Distribusi Frekuensi")
print("  0-10 :", data_interval1)
print(" 11-20 :", data_interval2)
print(" 21-30 :", data_interval3)
print(" 31-40 :", data_interval4)
print(" 41-50 :", data_interval5)
print(" 51-60 :", data_interval6)
print(" 61-70 :", data_interval7)
print(" 71-80 :", data_interval8)
print(" 81-90 :", data_interval9)
print("91-100 :", data_interval10)
