import random
random.seed(23)
data = random.sample(range(0,101),10)

min = data[0]
max = data[0]
for i in range(1,len(data)):
    if data[i] < min:
        min = data[i]
    if data[i] > max:
        max = data[i]

total = 0
for i in data:
    total = total + i

rata_rata = total/len(data)

print('Data yang diberikan adalah: '+str(data))
print('Nilai minimum dari data adalah '+str(min))
print('Nilai maksimum dari data adalah '+str(max))
print('Nilai rata-rata data tersebut adalah ', rata_rata)

kurang_rata = 0
lebih_rata = 0
for i in data:
    if i < rata_rata:
        kurang_rata = kurang_rata + 1
               
    if i > rata_rata:
        lebih_rata =lebih_rata + 1

print('Banyaknya data yang kurang dari rata-rata ada', kurang_rata, 'buah')
print('Banyaknya data yang lebih dari rata-rata ada '+str(lebih_rata)+' buah')
