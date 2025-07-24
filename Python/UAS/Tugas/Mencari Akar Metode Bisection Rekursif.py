## ANTONIUS ADITYA RIZKY WIJAYA
## G5402221003

import math
def f(x):
    return x**2-4

def g(x):
    return math.sin(x)

def bisection_rekursif(f, a, b):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print('Tak yakin ada akar di situ, NYERAH')
        return 
    c = (a + b) / 2
    fc = f(c)
    if abs(fc) < 1e-6:
        return c
    if fa * fc < 0:
        return bisection_rekursif(f, a, c)
    else:
        return bisection_rekursif(f, c, b)
kiri1, kanan1 = -1, 3
kiri2, kanan2 = -3, 3
kiri3, kanan3 = 2, 4
kiri4, kanan4 = 1, 2


## Persamaan kuadrat
# Ada akar
print('Akar fungsi pada selang [' + str(kiri1) + ',' + str(kanan1) + '] =\n', bisection_rekursif(f, kiri1, kanan1))
print()
# Tidak ada akar
print('Akar fungsi pada selang [' + str(kiri2) + ',' + str(kanan2) + '] =\n', bisection_rekursif(f, kiri2, kanan2))
print()

## Persamaan trigonometri
# Ada akar
print('Akar fungsi pada selang [' + str(kiri3) + ',' + str(kanan3) + '] =\n', bisection_rekursif(g, kiri3, kanan3))
print()
# Tidak ada akar
print('Akar fungsi pada selang [' + str(kiri4) + ',' + str(kanan4) + '] =\n', bisection_rekursif(g, kiri4, kanan4))
print()


##def bisection(f, a, b):
##    fa = f(a)
##    fb = f(b)
##    if fa*fb > 0:
##        print('Tak yakin ada akar di situ, NYERAH')
##        return
##    
##    while True:
##        c = (a + b)/2
##        fc = f(c)
##        if fa*fc < 0:
##            b = c
##            fb = fc
##        else:
##            a = c
##            fa = fc
##
##        if abs(fc) < 1e-6: ## bila |fc| < 10^-6
##            return c
##        
##uKiri, uKanan  = -1, 3 
##print('Mencari akar fungsi pada selang ['+str(uKiri)+','+str(uKanan)+']')
##print(bisection(f, uKiri, uKanan))
