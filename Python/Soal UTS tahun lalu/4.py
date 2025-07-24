# NOMOR 4
total = 0
for i in range(10):
    while True:
        nilai_uts = int(input(f'Masukan nilai UTS ke-{i+1}: '))
        if 0 <= nilai_uts <= 100:
            break
        else:
            print('Nilai harus antara 0-100,\nMohon masukkan nilai kembali')
    total += nilai_uts
avarage = total/10
print('Rata-rata nilai UTS =', avarage)


total = 0
for i in range(10):
    while True:
        nilai_uts = int(input(f'Masukan nilai UTS ke-{i+1}: '))
        if nilai_uts <0 or nilai_uts > 100:
            print('Nilai harus antara 0-100,\nMohon masukkan nilai kembali')
        else:
            break
    total += nilai_uts
avarage = total/10
print('Rata-rata nilai UTS =', avarage)


