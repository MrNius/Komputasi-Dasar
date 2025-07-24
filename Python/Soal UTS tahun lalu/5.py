# NOMOR 5
def konversi(n):
    if 0 <= n <= 1000:
        verbal = ['nol','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas']
        if n <= 11:
            return verbal [n]
        elif n<20:
            return verbal [n%10] + ' belas '
        elif n<100:
            return verbal [n//10] + ' puluh ' + konversi (n%10)
        elif n<200:
            return ' seratus ' + konversi (n-100)
        elif n<1000:
            return verbal [n//100] + ' ratus ' + konversi (n%100)
        else:
            return 'seribu'
    else:
        return 'bilangan di luar rentang 1-1000'

n = int(input('masukkan bil. bulat 1-1000: '))
hasil = konversi (n)
print (f'konversi verbal dari {n} adalah: {hasil}')
