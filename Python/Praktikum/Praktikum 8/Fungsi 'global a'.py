def f(x):
    global a
    y = 3 + x
    print('Ini fungsi')
    print('f(',x,')=', y)
    print('10a =', 10*a)
    a = 1000
    b = 10
    print('b =',b)

def g(x):
    y = 30 + 10*x
    print('Ini fungsi')
    print('g(',x,')=', y)
    a=250+x
    print('a =',a,'b =',b)

y = 10
print(y)
a=3
f(1)
b=100
g(5)
print('Nilai a di main program =', a)
