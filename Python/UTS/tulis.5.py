c = int(input('Beri saya sebuah bilangan bulat positif: '))
b_pertama = []
b_kedua = []
def barisan(n):
    a = n//2
    for i in range (a, n+1):
        b_pertama.append(i)
    for i in range (n, a-1, -2):
        b_kedua.append(i)
        
    if b_kedua[-1] != a:
            b_kedua.append(a)
    print("Barisan pertama:\n", b_pertama)
    print ("Barisan kedua:\n", b_kedua)

barisan(c)
