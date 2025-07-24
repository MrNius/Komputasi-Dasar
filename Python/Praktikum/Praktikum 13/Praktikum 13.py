import numpy as np

a = np.arange(9)
print(a)
print('Dimensi :', a.ndim, '\n')

a2 = a[np.newaxis, :]
print(a2)
print('Dimensi :', a2.ndim, '\n')

a3 = np.arange(15).reshape(3, 5)
print(a3)
print('Dimensi :', a3.ndim, '\n')

a4 = np.arange(60).reshape(3, 5, 4)
print(a4)
print('Dimensi :', a4.ndim, '\n')

a5 = np.arange(120).reshape(3, 5, 2, 4)
print(a5)
print('Dimensi :', a5.ndim, '\n')


## TUGAS
A = np.matrix('4 2 -1; 5 0 3; 1 3 2')
print('Matrix A =\n', A)

b = np.matrix('5; 14; 13')
print('Matrix b =\n', b)

I = np.matrix('1 0 0; 0 1 0; 0 0 1')
print('Matrix I =\n', I)

B = A - 3*I
print('B = A - 3*I\n', B)

p = A*b
print('p = A*b\n', p)

c = b.getT()*p
print('c = b^T*p\n', c)

C = b*p.getT()
print('C = b*p^T\n', C)
