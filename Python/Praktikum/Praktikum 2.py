print('Hallo Selamat Pagi')

nama=input('Masukan nama anda :')

#Tanda (+) itu untuk menghilangkan spasi setelah string
print('Hallo', nama.title()+',', 'selamat datang diprogram kami')
print('Nama anda :', nama.upper())
print('Nama anda :', nama.lower())
print('Nama anda :', nama.capitalize())
print('Nama anda :', nama.title())

#Untuk memecah string
namaTerpecah=nama.split()

#Untuk mengetahui jumlah karakter dalam nama
print('Nama anda terdiri dari', len(nama), 'huruf')

#Untuk mengetahui jumlah kata dalam nama
print('Nama anda terdiri dari', len(namaTerpecah), 'kata')

#Untuk menyusun string di belakang jadi di depan
namaTerpecah=nama.split()
print('Hallo tuan', namaTerpecah[-1].title()+',', nama[0:len(nama)-len(namaTerpecah[-1])].title())
