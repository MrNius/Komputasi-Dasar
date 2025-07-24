n = 5
kode = []
for i in range (1,n):
    for j in range (1,n):
        if i<j:
            kode.append(10*i+j)
        elif i>j:
            kode.append(100*j+i)
        else:
            kode.append(i)
print(kode)

n = 5
kode = []
for i in range (1,n):
    for j in range (1,n):
        if i<j:
            kode.append(int(str(i)+str(j)))
        elif i>j:
            kode.append(int(str(j)+str('0')+str(i)))
        else:
            kode.append(i)
print(kode)

