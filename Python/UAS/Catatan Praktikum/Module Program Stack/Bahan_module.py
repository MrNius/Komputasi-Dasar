def fa(x):
    'Menghitung nilai fungsi sesepenggal\n          = x**2 + 3*x - 5;  x<2\n f(x) = 0; x=2\n          = 6 - x; x>2'
    print('call fungsi fa('+str(x)+')')
    if x<2:
        y = x**2 + 3*x - 5
    else:
        if x==2:
            y=0
        else:
            y = 6-x
    return y

def fb(x):
    'Menghitung jumlah kuadrat setiap elemen dari list x'
    print('call fungsi fb('+str(x)+')')
    jumlah=0
    for i in x:
        jumlah = jumlah + i**2
    return jumlah
print(fb([1, 3, 5]))
print(fb([3, 2, 6]))
print()

def fc(x,y):
    print('call fungsi fc ('+str(x)+','+str(y)+')')
    return x,y

def fd(x,y):
    print('call fungsi fd ('+str(x)+','+str(y)+')')
    x[0], y[0] = y[0], x[0]
    y = [2,5,10,15,23]
    return x,y
