def ratarata(n):
    total = 0
    for i in range(n):
        nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
        while nilai < 0 or nilai > 100:
            print("NIlai harus antara 0  dan 100")
            nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
        total += nilai
    rata_rata = total/n
    return rata_rata

n = int(input("Menghitung rata-rata berapa nilai UTS? "))
print("Menghitung rata-rata", n, "nilai UTS")
print("Rata-rata =", ratarata(n))
