fin = open(r'F:\Pyhton\Praktikum\Praktikum 7\beritaIPB.txt', encoding = 'utf8')
wordCount = {}
baris_wordCount = [] #variabel jumlah kata tiap baris

while True :
    baris = fin.readline()
    if baris == '':
        break
    baris = baris.strip() #menghapus whitespace
    baris_baru = baris.split() #memotong setiap kata dalam satu paragraf menjadi komponen list
    baris_wordCount.append(len(baris_baru)) #menghitung jumlah kata tiap baris dan memasukkan ke variabel

#membersihkan kata dari karakter lain (tanda baca)
    bersih = []
    for kata in baris_baru:
        bersih.append(kata.strip(',.!?#"()[]{}').lower()) #menghilangkan karakter lain (tanda baca) dan menjadikan huruf kecil
#menghitung jumlah list kata
    for kata in bersih:
        if kata not in wordCount:
            wordCount[kata] = 1
        else:
            wordCount[kata] += 1
##    print(baris_baru)
##print(wordCount)

#menghitung max kata untuk menentukan jumlah format
maxKata = 0
for kata in wordCount.keys():
    if len(kata) > maxKata:
        maxKata = len(kata)
##print(maxKata)

for kata in wordCount.keys():
##    print('{:15}{:5}'.format(kata, wordCount[kata]))  #format manual
    print(('{:'+str(maxKata)+'}{:5}').format(kata, wordCount[kata])) #format otomatis setelah max kata dihitung
print(baris_wordCount) #menampilkan jumlah kata tiap baris
fin.close()
