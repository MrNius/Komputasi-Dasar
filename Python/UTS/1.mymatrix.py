def mymatrix(n):
    matrix = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            if i < j:
                row.append(10*i + j)
            elif i > j:
                row.append(i + 100*j)
            else:
                row.append(i)
        matrix.append(row)
    return matrix

# Contoh penggunaan
print(mymatrix(4))
