## Praktikum 11

class MyClass:
    def __init__ (self):
        self.x = 5
        print('oh, aku lahir dengan nilai awal',self.x)
    def tampil(self):
        print('hi, saya bernilai',self.x)
    def set(self, x):
        self.x = x
    
p1 = MyClass()
p1.tampil()
p1.set(10)
p1.tampil()

class Mahasiswa:
    def __init__ (self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.thLahir = 2000
    def setTahunLahir(self, tahun):
        self.thLahir = tahun
    def tampil(self):
        print('Hi, nama saya {:8} dengan NIM {:10}, saya berusia {:3} tahun'.format(self.nama, self.nim, 2023-self.thLahir))
m1 = Mahasiswa('G54012221003', 'Antonius')
m2 = Mahasiswa('G104012221003', 'Babeh')

m1.setTahunLahir(2004)
m2.setTahunLahir(2003)

m1.tampil()
m2.tampil()


class BujurSangkar:
    def __init__(self, sisi):
        self.sisi = sisi
    def tampil(self):
        print('Bujursangkar dengan sisi', self.sisi)
    def setSisi(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi**2

x = BujurSangkar(4)
y = BujurSangkar(3)

x.tampil()
y.tampil()

# Membuat objek-objek dan dimasukan ke dalam sebuah list
daftarObjek = []
daftarObjek.append(BujurSangkar(4))
daftarObjek.append(BujurSangkar(3))
daftarObjek.append(BujurSangkar(10))
daftarObjek.append(Mahasiswa('G11402221003','Cindy Tabuty'))

for i in daftarObjek:
    i.tampil()
