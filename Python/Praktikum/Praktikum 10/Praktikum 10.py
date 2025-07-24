def f(x):
    return x**2-4

def bisection(f, a, b):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print('Tak yakin ada akar di situ, NYERAH')
        return
    
    while True:
        c = (a + b)/2
        fc = f(c)
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        if abs(fc) < 1e-6: ## bila |fc| < 10^-6
            return c
        
uKiri, uKanan  = -1, 3 
print('Mencari akar fungsi pada selang ['+str(uKiri)+','+str(uKanan)+']')
print(bisection(f, uKiri, uKanan))
