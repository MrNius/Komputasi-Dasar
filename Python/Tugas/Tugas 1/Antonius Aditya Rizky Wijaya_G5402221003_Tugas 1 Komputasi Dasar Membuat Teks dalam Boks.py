print('===[HALO, SELAMAT DATANG DI PROGRAM SAYA]===')
print()

print ('Mohon Isi Beberapa Data Berikut : ')
nama=input('Nama : ')
while len(nama) > 20:
    print("Lebih dari 20 karakter, mohon isi kembali")
    nama=input('Nama : ')
	
nim=input('NIM : ')
while len(nim) > 20:
    print("Lebih dari 20 karakter, mohon isi kembali")
    nim=input('NIM : ')

asalSMA=input('Nama SMA asal : ')
while len(asalSMA) > 20:
    print("Lebih dari 20 karakter, mohon isi kembali")
    asalSMA=input('Nama SMA asal : ')
    
warna=input('Warna yang disukai : ')
while len(warna) > 20:
    print("Lebih dari 20 karakter, mohon isi kembali")
    warna=input('Warna yang disukai : ')
    
print()
print('-'*30)
print('|'+' '*28+'|')
print('|'+' '*3+nama.title()+' '*(30-len(nama)-5)+'|')
print('|'+' '*3+nim.title()+' '*(30-len(nim)-5)+'|')
print('|'+' '*3+asalSMA.upper()+' '*(30-len(asalSMA)-5)+'|')
print('|'+' '*3+warna.title()+' '*(30-len(warna)-5)+'|')
print('|'+' '*28+'|')
print('-'*30)
print()
print('===[PROGRAM SELESAI, TERIMA KASIH]===')
