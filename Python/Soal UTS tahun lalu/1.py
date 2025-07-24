#Nomor 1
#a
def misteri1(x):
    res = x**2+2*x-5
    return res
print(misteri1(1))
#Letak error: tidak ada
#Program yang benar: sudah benar
#Output program benar: -2
#---------------------

#b
##def misteri2(x):
##    res = x**2+2*x-5
##    return = res
##print(misteri2(2))
#Letak error: fungsi return tidak memperbolehkan penggunaan tanda '=', kecuali tanda '=='
#Program yang benar:
def misteri2(x):
    res = x**2+2*x-5
    return res
print(misteri2(2))
#Output program benar: 3
#---------------------

#c
##def misteri3(x):
##    res = x**2+2*x-5
##     return res == 3
##print(misteri3(3))
#Letak error: terdapat satu spasi sebelum fungsi return, fungsi return harus sejajar dengan yang apa yang ingin dipanggil
#Program yang benar:
def misteri3(x):
    res = x**2+2*x-5
    return res == 3
print(misteri3(3))
#Output program benar: FALSE
#---------------------

#d
def misteri4(x):
    res = x**2+2*x-5
print(misteri4(4))
#Letak error: tidak ada, namun outputnya akan menhasilkan 'None' karena definisi fungsi tersebut tidak menggunakan return untuk memanggil hasilnya
#Program yang benar: sudah benar
#Output program benar: None
#---------------------

#e
##def misteri5(x):
##    res = x**2+2*x-5
##     return res
##print(misteri5(5))
#Letak error: terdapat satu spasi sebelum fungsi return, fungsi return harus sejajar dengan yang apa yang ingin dipanggil
#Program yang benar: 
def misteri5(x):
    res = x**2+2*x-5
    return res
print(misteri5(5))
#Output program benar: 30
#---------------------
