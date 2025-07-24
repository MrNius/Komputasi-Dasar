def ratarata(n):
    total = 0
    for i in range(1, n+1):
        nilai = int(input(f"Masukkan nilai ke-{i}: "))
        total += nilai
    rata_rata = total/n
    return rata_rata
n = int(input("Menghitung rata-rata berapa nilai? "))
print("Rata-rata =", ratarata(n))
