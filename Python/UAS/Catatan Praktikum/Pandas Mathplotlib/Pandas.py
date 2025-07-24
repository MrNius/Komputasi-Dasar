import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6.8])
print(s, '\n')
ss = np.array([1.,3.,5.,np.nan,6.,8.,])
print(ss, '\n')

#Menentukan tanggal
dates = pd.date_range("20130101", periods = 6)
print(dates, '\n')
dates2 = pd.date_range("20130101", periods = 3)
print(dates2, '\n')

#Membuat suatu data frame
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df,'\n')
df2 = pd.DataFrame(100*np.random.randn(5, 3), columns=['UTS','UAS','NAKHIR'])
print(df2,'\n')
df3 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df3, '\n')
print(df3.dtypes, '\n')

#3 data awal dan akhir
print(df.head(3), '\n')
print(df.tail(3), '\n')

#Konversi data frame ke matrix
print(df.to_numpy(), '\n')

#Menghitung summary statistik
print(df.describe(), '\n')

#Import data excel
dataKu = pd.read_excel(r'D:\IPB UNIVERSITY\Pyhton\Praktikum\Praktikum 14\ContohData.xlsx', index_col=0)
print(dataKu, '\n')
#Melihat tipe data
print(dataKu.dtypes, '\n')
#Menampilkan sebagian data dengan jumlah 3
print(dataKu.loc[3:5,['NIM','Nama']], '\n')
#Mengubah data
dataKu.at[3,'Nama'] = 'Rudi'
print(dataKu)
