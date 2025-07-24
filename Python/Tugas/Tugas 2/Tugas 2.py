import random

jumlah_data = int(input("Masukkan jumlah data yang akan diproses: "))

data = [random.randint(0, 101) for _ in range(jumlah_data)]

intervals = [0, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101]

frekuensi = {f"{intervals[i]}-{intervals[i+1]-1}": 0 for i in range(len(intervals)-1)}

for nilai in data:
    for i in range(len(intervals)-1):
        if intervals[i] <= nilai <= intervals[i+1]-1:
            frekuensi[f"{intervals[i]}-{intervals[i+1]-1}"] += 1

print("Distribusi Frekuensi Data Nilai:")
for interval, freq in frekuensi.items():
    print(interval :, '*'*freq)
