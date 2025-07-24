#Rekursif
def countdown(n):
    'Count down to 0'
    if n <= 0:
        print('Finish!')
    else:
        print(n)
        countdown(n-1)
countdown(10)
print()

def countup(n):
    'Count up to 0'
    if n <= 0:
        print('Start!')
    else:
        countup(n-1)
        print(n)
countup(10)
print()

#Faktorial non-rekursif
def fakNR(n):
    total = 1
    for i in range(n, 0, -1):
        total = total * i
    return total

#Faktorial rekursif
def fakR(n):
    if n <= 1 :
        return 1
    else:
        return n*fakR(n-1)

n=5
print('fakNR('+str(n)+')=', fakNR(n))
print('fakR('+str(n)+')=', fakR(n))
print()


#f(n) = 2*f(n-1) - f(n-2), n>1
#f(1) = 2, f(0) = 1
def barisanAneh(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 3*barisanAneh(n-1) - barisanAneh(n-2)
print('Barisan Bilangan f(n) = 3*f(n-1) - f(n-2), n > 1')
for i in range(8):
    print(barisanAneh(i))
print()


#Segitiga versi rekursif
print('Segitiga versi rekrusif') 
def segi3A(n):
    if n > 0:
        print('*'*n)
        segi3A(n-1)
    else:
        return
def segi3B(n):
    if n > 0:
        segi3B(n-1)
        print('*'*n)
    else:
        return
segi3A(10)
segi3B(10)
print()

#Jumlah bulat segitiga
def barisX(n):
    if n == 1:
        return 1
    else:
        return n + barisX(n-1)
#Jumlah bulat persegi
def barisY(n):
    if n == 1:
        return 1
    else:
        return barisX(n-1) + 2*n-1
    
for i in range(1,6):
    print(barisX(i))
    
for i in range(1,6):
    print(barisY(i))
