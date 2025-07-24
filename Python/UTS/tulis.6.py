barisan_ganjil = []
barisan_genap = []

while True:
    c = int(input('Berikan saya sebuah bilangan bulat positif: '))

    if c < 0:
        print('Salah. Saya mintanya bilangan bulat positif')
        break
    elif c == 0:
        break
    else:
        if c%2 != 0:
            barisan_ganjil.append(c)
        else:
            barisan_genap.append(c)

print('Barisan ganjil =', barisan_ganjil)
print('Barisan genap =', barisan_genap)
