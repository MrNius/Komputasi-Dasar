import math
def hitung_nakhir(uts,uas):
    return (uts+uas)/2

#                        HURUF MUTU   ANGKA MUTU
#-----------------------------------------
#  0 <= nilai akhir < 25          E   0
# 25 <= nilai akhir < 40          D   1
# 40 <= nilai akhir < 60          C   2
# 60 <= nilai akhir < 80          B   3
# 80 <= nilai akhir <= 100        A   4
#-----------------------------------------
def hitung_hmutu(nakhir):
    if nakhir >=80:
        return 'A'
    elif nakhir >=60:
        return 'B'
    elif nakhir >=40:
        return 'C'
    elif nakhir >=25:
        return 'D'
    else:
        return 'E'
        
    
def tampil_data(nim, nama, kelompok, uts, uas, nakhir, hmutu):
    # tampilkan data dalam bentuk yang 'manis'
    print('{:11} {:38} {:8} {:3} {:3} {:5} {:5}'.format('NIM','NAMA','KELOMPOK','UTS','UAS','N.AKHIR','H.MUTU'))
##    for i in range(len(nim)):
    for i in range(163):
        print('{:11} {:38} {:8} {:3} {:3} {:5} {:3}'.format(nim[i],nama[i],kelompok[i],uts[i],uas[i],nakhir[i],hmutu[i]))

infile=open(r'D:\IPB UNIVERSITY\Pyhton\Tugas\Tugas 5\NilaiUTS-UAS_prediksi.csv')
nim=[]
nama=[]
kelompok=[]
uts=[]
uas=[]
nakhir=[]
hmutu=[]
IP=[]

brs=infile.readline()
while True:
    brs=infile.readline()
    if brs=='':
        break
    brs = brs.strip().split(';')
    nim.append(brs[0])
    nama.append(brs[1])
    kelompok.append(brs[2])
    uts.append(int(brs[3]))
    uas.append(int(brs[4]))
    nakhir.append(hitung_nakhir(int(brs[3]),int(brs[4])))
    hmutu.append('')
    IP.append('')

# tampilkan data donk!
##tampil_data(nim, nama, kelompok, uts, uas, nakhir, hmutu)

# lengkapi kolom huruf mutu
for i in range(163):
    hmutu[i] = hitung_hmutu(nakhir[i])

# tampilkan lagi data dalam bentuk yang 'manis'
tampil_data(nim, nama, kelompok, uts, uas, nakhir, hmutu)

# hitung dan tampilkan nilai rata-rata dari uts, uas dan nilai akhir
jumUTS=0
jumUAS=0
jumnakhir=0
ndata=0
for i in range(163):
    jumUTS=jumUTS+uts[i]
    jumUAS=jumUAS+uas[i]   
    jumnakhir=jumnakhir+nakhir[i]
    ndata=ndata+1
print("rata-rata UTS adalah",jumUTS/ndata)
print("rata-rata UAS adalah",jumUAS/ndata)
print("rata-rata nilai akhir adalah",jumnakhir/ndata)


Selisih_kuadrat_nilaiUTS=[]
Selisih_kuadrat_nilaiUAS=[]
Selisih_kuadrat_nilaiakhir=[]
for i in range(163):
    sel_kuadrat_nUTS=(uts[i]-(jumUTS/ndata))**2
    sel_kuadrat_nUAS=(uas[i]-(jumUAS/ndata))**2
    sel_kuadrat_nakhir=(nakhir[i]-(jumnakhir/ndata))**2
    Selisih_kuadrat_nilaiUTS.append(sel_kuadrat_nUTS)
    Selisih_kuadrat_nilaiUAS.append(sel_kuadrat_nUAS)
    Selisih_kuadrat_nilaiakhir.append(sel_kuadrat_nakhir)
total_Selisih_kuadrat_nilaiUTS=0
total_Selisih_kuadrat_nilaiUAS=0
total_Selisih_kuadrat_nilaiakhir=0
for i in range(163):
    total_Selisih_kuadrat_nilaiUTS=Selisih_kuadrat_nilaiUTS[i]+ total_Selisih_kuadrat_nilaiUTS
    total_Selisih_kuadrat_nilaiUAS=Selisih_kuadrat_nilaiUAS[i]+ total_Selisih_kuadrat_nilaiUAS
    total_Selisih_kuadrat_nilaiakhir=Selisih_kuadrat_nilaiakhir[i]+ total_Selisih_kuadrat_nilaiakhir
print("simpangan baku dari UTS adalah:",(total_Selisih_kuadrat_nilaiUTS/ndata)**0.5)
print("simpangan baku dari UAS adalah:",(total_Selisih_kuadrat_nilaiUAS/ndata)**0.5)
print("simpangan baku dari Nilai Akhir adalah:",(total_Selisih_kuadrat_nilaiakhir/ndata)**0.5)


# hitung dan tampilkan indeks prestasi mata kuliah
def hitung_ip(nakhir):
    if nakhir >=80:
        return 4
    elif nakhir >=60:
        return 3
    elif nakhir >=40:
        return 2
    elif nakhir >=25:
        return 1
    else:
        return 0
def tampil_data_IP(nim, nama,ip):
    # tampilkan data dalam bentuk yang 'manis'
    print('{:11} {:38} {:5}'.format('NIM','NAMA','IP'))
##    for i in range(len(nim)):
    for i in range(163):
        print('{:11} {:38} {:2}'.format(nim[i],nama[i],IP[i]))
for i in range(163):
    IP[i] = hitung_ip(nakhir[i])
tampil_data_IP(nim, nama, IP)

# Nomor 2
# hitung statistik per fakultas
import statistics
jumUTS_A=0
jumUAS_A=0
jumnakhir_A=0
ndata_A=0
jumUTS_B=0
jumUAS_B=0
jumnakhir_B=0
ndata_B=0
jumUTS_C=0
jumUAS_C=0
jumnakhir_C=0
ndata_C=0
jumUTS_D=0
jumUAS_D=0
jumnakhir_D=0
ndata_D=0
jumUTS_E=0
jumUAS_E=0
jumnakhir_E=0
ndata_E=0
jumUTS_F=0
jumUAS_F=0
jumnakhir_F=0
ndata_F=0
jumUTS_G=0
jumUAS_G=0
jumnakhir_G=0
ndata_G=0
jumUTS_H=0
jumUAS_H=0
jumnakhir_H=0
ndata_H=0
jumUTS_I=0
jumUAS_I=0
jumnakhir_I=0
ndata_I=0
for i in range (163):
    if nim[i][0]=="A":
        jumUTS_A=jumUTS_A+uts[i]
        jumUAS_A=jumUAS_A+uas[i]
        jumnakhir_A=jumnakhir_A+nakhir[i]
        ndata_A=ndata_A+1
    elif nim[i][0]=="B":
        jumUTS_B=jumUTS_B+uts[i]
        jumUAS_B=jumUAS_B+uas[i]
        jumnakhir_B=jumnakhir_B+nakhir[i]
        ndata_B=ndata_B+1
    elif nim[i][0]=="C":
        jumUTS_C=jumUTS_C+uts[i]
        jumUAS_C=jumUAS_C+uas[i]
        jumnakhir_C=jumnakhir_C+nakhir[i]
        ndata_C=ndata_C+1
    elif nim[i][0]=="D":
        jumUTS_D=jumUTS_D+uts[i]
        jumUAS_D=jumUAS_D+uas[i]
        jumnakhir_D=jumnakhir_D+nakhir[i]
        ndata_D=ndata_D+1
    elif nim[i][0]=="E":
        jumUTS_E=jumUTS_E+uts[i]
        jumUAS_E=jumUAS_E+uas[i]
        jumnakhir_E=jumnakhir_E+nakhir[i]
        ndata_E=ndata_E+1
    elif nim[i][0]=="F":
        jumUTS_F=jumUTS_F+uts[i]
        jumUAS_F=jumUAS_F+uas[i]
        jumnakhir_F=jumnakhir_F+nakhir[i]
        ndata_F=ndata_F+1
    elif nim[i][0]=="G":
        jumUTS_G=jumUTS_G+uts[i]
        jumUAS_G=jumUAS_G+uas[i]
        jumnakhir_G=jumnakhir_G+nakhir[i]
        ndata_G=ndata_G+1
    elif nim[i][0]=="H":
        jumUTS_H=jumUTS_H+uts[i]
        jumUAS_H=jumUAS_H+uas[i]
        jumnakhir_H=jumnakhir_H+nakhir[i]
        ndata_H=ndata_H+1
    elif nim[i][0]=="I":
        jumUTS_I=jumUAS_I+uas[i]
        jumUAS_I=jumUAS_H+uas[i]
        jumnakhir_I=jumnakhir_I+nakhir[i]
        ndata_I=ndata_I+1
        
# Membuat list untuk nilai UTS, UAS, dan Nilai Akhir pada masing-masing fakultas
list_UTS_A=[]
list_UAS_A=[]
list_nilaiakhir_A=[]
list_UTS_B=[]
list_UAS_B=[]
list_nilaiakhir_B=[]
list_UTS_C=[]
list_UAS_C=[]
list_nilaiakhir_C=[]
list_UTS_D=[]
list_UAS_D=[]
list_nilaiakhir_D=[]
list_UTS_E=[]
list_UAS_E=[]
list_nilaiakhir_E=[]
list_UTS_F=[]
list_UAS_F=[]
list_nilaiakhir_F=[]
list_UTS_G=[]
list_UAS_G=[]
list_nilaiakhir_G=[]
list_UTS_H=[]
list_UAS_H=[]
list_nilaiakhir_H=[]
list_UTS_I=[]
list_UAS_I=[]
list_nilaiakhir_I=[]
for i in range(163):
    if nim[i][0]=="A":
        nUTS_A=uts[i]
        nUAS_A=uas[i]
        nAkhir_A=nakhir[i]
        list_UTS_A.append(nUTS_A)
        list_UAS_A.append(nUAS_A)
        list_nilaiakhir_A.append(nAkhir_A)
    if nim[i][0]=="B":
        nUTS_B=uts[i]
        nUAS_B=uas[i]
        nAkhir_B=nakhir[i]
        list_UTS_B.append(nUTS_B)
        list_UAS_B.append(nUAS_B)
        list_nilaiakhir_B.append(nAkhir_B)
    if nim[i][0]=="C":
        nUTS_C=uts[i]
        nUAS_C=uas[i]
        nAkhir_C=nakhir[i]
        list_UTS_C.append(nUTS_C)
        list_UAS_C.append(nUAS_C)
        list_nilaiakhir_C.append(nAkhir_C)
    if nim[i][0]=="D":
        nUTS_D=uts[i]
        nUAS_D=uas[i]
        nAkhir_D=nakhir[i]
        list_UTS_D.append(nUTS_D)
        list_UAS_D.append(nUAS_D)
        list_nilaiakhir_D.append(nAkhir_D)
    if nim[i][0]=="E":
        nUTS_E=uts[i]
        nUAS_E=uas[i]
        nAkhir_E=nakhir[i]
        list_UTS_E.append(nUTS_E)
        list_UAS_E.append(nUAS_E)
        list_nilaiakhir_E.append(nAkhir_E)
    if nim[i][0]=="F":
        nUTS_F=uts[i]
        nUAS_F=uas[i]
        nAkhir_F=nakhir[i]
        list_UTS_F.append(nUTS_F)
        list_UAS_F.append(nUAS_F)
        list_nilaiakhir_F.append(nAkhir_F)
    if nim[i][0]=="G":
        nUTS_G=uts[i]
        nUAS_G=uas[i]
        nAkhir_G=nakhir[i]
        list_UTS_G.append(nUTS_G)
        list_UAS_G.append(nUAS_G)
        list_nilaiakhir_G.append(nAkhir_G)
    if nim[i][0]=="H":
        nUTS_H=uts[i]
        nUAS_H=uas[i]
        nAkhir_H=nakhir[i]
        list_UTS_H.append(nUTS_H)
        list_UAS_H.append(nUAS_H)
        list_nilaiakhir_H.append(nAkhir_H)
    if nim[i][0]=="I":
        nUTS_I=uts[i]
        nUAS_I=uas[i]
        nAkhir_I=nakhir[i]
        list_UTS_I.append(nUTS_I)
        list_UAS_I.append(nUAS_I)
        list_nilaiakhir_I.append(nAkhir_I)

##Buat data frame
#Buat data frame UTS
print("""
 ____________________________________________________________________________________
|                                           Statistik UTS                            |""")
print('|'+'Fakultas/Sekolah'+2*' '+'Mahasiswa'+5*' '+'Rata-Rata'+11*' '+'st.deviasi'+5*' '+'Minimum'+2*' '+'Maksimum'+'|')
print('|'+'FAPERTA         '+6*' '+str(ndata_A)+5*' '+str(jumUTS_A/ndata_A)+2*' '+str(statistics.stdev(list_UTS_A))+5*' '+
      str(min(list_UTS_A))+6*' '+str(max(list_UTS_A))+3*' '+'|')
print('|'+'SKHB            '+6*' '+str(ndata_B)+5*' '+str(jumUTS_B/ndata_B)+1*' '+str(statistics.stdev(list_UTS_B))+5*' '+
      str(min(list_UTS_B))+6*' '+str(max(list_UTS_B))+4*' '+'|')
print('|'+'FPIK            '+6*' '+str(ndata_C)+5*' '+str(jumUTS_C/ndata_C)+14*' '+str(statistics.stdev(list_UTS_C))+5*' '+
      str(min(list_UTS_C))+6*' '+str(max(list_UTS_C))+4*' '+'|')
print('|'+'FAPET           '+6*' '+str(ndata_D)+5*' '+str(jumUTS_D/ndata_D)+14*' '+str(statistics.stdev(list_UTS_D))+5*' '+
      str(min(list_UTS_D))+6*' '+str(max(list_UTS_D))+4*' '+'|')
print('|'+'FAHUTAN         '+6*' '+str(ndata_E)+5*' '+str(jumUTS_E/ndata_E)+2*' '+str(statistics.stdev(list_UTS_E))+5*' '+
      str(min(list_UTS_E))+6*' '+str(max(list_UTS_E))+4*' '+'|')
print('|'+'FATETA          '+6*' '+str(ndata_F)+5*' '+str(jumUTS_F/ndata_F)+14*' '+str(statistics.stdev(list_UTS_F))+5*' '+
      str(min(list_UTS_F))+6*' '+str(max(list_UTS_F))+4*' '+'|')
print('|'+'FMIPA           '+6*' '+str(ndata_G)+5*' '+str(jumUTS_G/ndata_G)+3*' '+str(statistics.stdev(list_UTS_G))+5*' '+
      str(min(list_UTS_G))+6*' '+str(max(list_UTS_G))+4*' '+'|')
print('|'+'FEM             '+6*' '+str(ndata_H)+5*' '+str(jumUTS_H/ndata_H)+15*' '+str(statistics.stdev(list_UTS_H))+5*' '+
      str(min(list_UTS_H))+6*' '+str(max(list_UTS_H))+3*' '+'|')
print('|'+'FEMA            '+6*' '+str(ndata_I)+5*' '+str(jumUTS_I/ndata_I)+2*' '+str(statistics.stdev(list_UTS_I))+5*' '+
      str(min(list_UTS_I))+6*' '+str(max(list_UTS_I))+4*' '+'|')
print('|'+'IPB UNIVERSITY  '+6*' '+str(ndata)+4*' '+str(jumUTS/ndata)+1*' '+str((total_Selisih_kuadrat_nilaiUTS/ndata)**0.5)+5*' '+
      str(min(uts))+6*' '+str(max(uts))+3*' '+'|')
print('|'+84*'_'+'|')

#Buat data frame UAS
print("""
 ____________________________________________________________________________________
|                                           Statistik UAS                            |""")
print('|'+'Fakultas/Sekolah'+2*' '+'Mahasiswa'+5*' '+'Rata-Rata'+11*' '+'st.deviasi'+5*' '+'Minimum'+2*' '+'Maksimum'+'|')
print('|'+'FAPERTA         '+6*' '+str(ndata_A)+5*' '+str(jumUAS_A/ndata_A)+3*' '+str(statistics.stdev(list_UAS_A))+5*' '+
      str(min(list_UAS_A))+6*' '+str(max(list_UAS_A))+3*' '+'|')
print('|'+'SKHB            '+6*' '+str(ndata_B)+5*' '+str(jumUAS_B/ndata_B)+1*' '+str(statistics.stdev(list_UAS_B))+5*' '+
      str(min(list_UAS_B))+6*' '+str(max(list_UAS_B))+4*' '+'|')
print('|'+'FPIK            '+6*' '+str(ndata_C)+5*' '+str(jumUAS_C/ndata_C)+15*' '+str(statistics.stdev(list_UAS_C))+5*' '+
      str(min(list_UAS_C))+6*' '+str(max(list_UAS_C))+4*' '+'|')
print('|'+'FAPET           '+6*' '+str(ndata_D)+5*' '+str(jumUAS_D/ndata_D)+1*' '+str(statistics.stdev(list_UAS_D))+5*' '+
      str(min(list_UAS_D))+6*' '+str(max(list_UAS_D))+3*' '+'|')
print('|'+'FAHUTAN         '+6*' '+str(ndata_E)+5*' '+str(jumUAS_E/ndata_E)+1*' '+str(statistics.stdev(list_UAS_E))+5*' '+
      str(min(list_UAS_E))+6*' '+str(max(list_UAS_E))+4*' '+'|')
print('|'+'FATETA          '+6*' '+str(ndata_F)+5*' '+str(jumUAS_F/ndata_F)+13*' '+str(statistics.stdev(list_UAS_F))+5*' '+
      str(min(list_UAS_F))+6*' '+str(max(list_UAS_F))+4*' '+'|')
print('|'+'FMIPA           '+6*' '+str(ndata_G)+5*' '+str(jumUAS_G/ndata_G)+2*' '+str(statistics.stdev(list_UAS_G))+5*' '+
      str(min(list_UAS_G))+6*' '+str(max(list_UAS_G))+4*' '+'|')
print('|'+'FEM             '+6*' '+str(ndata_H)+5*' '+str(jumUAS_H/ndata_H)+14*' '+str(statistics.stdev(list_UAS_H))+5*' '+
      str(min(list_UAS_H))+6*' '+str(max(list_UAS_H))+4*' '+'|')
print('|'+'FEMA            '+6*' '+str(ndata)+4*' '+str(jumUAS/ndata)+2*' '+str((total_Selisih_kuadrat_nilaiUAS/ndata)**0.5)+5*' '+
      str(min(uas))+6*' '+str(max(uas))+3*' '+'|')
print('|'+'IPB UNIVERSITY  '+6*' '+str(ndata)+4*' '+str(jumUAS/ndata)+2*' '+str((total_Selisih_kuadrat_nilaiUAS/ndata)**0.5)+5*' '+
      str(min(uas))+6*' '+str(max(uas))+3*' '+'|')
print('|'+84*'_'+'|')

#Buat data frame NILAI AKHIR
print("""
 ____________________________________________________________________________________
|                                           Statistik Nilai Akhir                    |""")
print('|'+'Fakultas/Sekolah'+2*' '+'Mahasiswa'+5*' '+'Rata-Rata'+11*' '+'st.deviasi'+5*' '+'Minimum'+2*' '+'Maksimum'+'|')
print('|'+'FAPERTA         '+6*' '+str(ndata_A)+5*' '+str(jumnakhir_A/ndata_A)+2*' '+str(statistics.stdev(list_nilaiakhir_A))+3*' '+
      str(min(list_nilaiakhir_A))+6*' '+str(max(list_nilaiakhir_A))+2*' '+'|')
print('|'+'SKHB            '+6*' '+str(ndata_B)+5*' '+str(jumnakhir_B/ndata_B)+1*' '+str(statistics.stdev(list_nilaiakhir_B))+2*' '+
      str(min(list_nilaiakhir_B))+6*' '+str(max(list_nilaiakhir_B))+2*' '+'|')
print('|'+'FPIK            '+6*' '+str(ndata_C)+5*' '+str(jumnakhir_C/ndata_C)+15*' '+str(statistics.stdev(list_nilaiakhir_C))+2*' '+
      str(min(list_nilaiakhir_C))+6*' '+str(max(list_nilaiakhir_C))+2*' '+'|')
print('|'+'FAPET           '+6*' '+str(ndata_D)+5*' '+str(jumnakhir_D/ndata_D)+2*' '+str(statistics.stdev(list_nilaiakhir_D))+2*' '+
      str(min(list_nilaiakhir_D))+6*' '+str(max(list_nilaiakhir_D))+2*' '+'|')
print('|'+'FAHUTAN         '+6*' '+str(ndata_E)+5*' '+str(jumnakhir_E/ndata_E)+2*' '+str(statistics.stdev(list_nilaiakhir_E))+3*' '+
      str(min(list_nilaiakhir_E))+6*' '+str(max(list_nilaiakhir_E))+2*' '+'|')
print('|'+'FATETA          '+6*' '+str(ndata_F)+5*' '+str(jumnakhir_F/ndata_F)+13*' '+str(statistics.stdev(list_nilaiakhir_F))+2*' '+
      str(min(list_nilaiakhir_F))+6*' '+str(max(list_nilaiakhir_F))+2*' '+'|')
print('|'+'FMIPA           '+6*' '+str(ndata_G)+5*' '+str(jumnakhir_G/ndata_G)+2*' '+str(statistics.stdev(list_nilaiakhir_G))+3*' '+
      str(min(list_nilaiakhir_G))+6*' '+str(max(list_nilaiakhir_G))+2*' '+'|')
print('|'+'FEM             '+6*' '+str(ndata_H)+5*' '+str(jumnakhir_H/ndata_H)+15*' '+str(statistics.stdev(list_nilaiakhir_H))+2*' '+
      str(min(list_nilaiakhir_H))+6*' '+str(max(list_nilaiakhir_H))+2*' '+'|')
print('|'+'FEMA            '+6*' '+str(ndata_I)+5*' '+str(jumnakhir_I/ndata_I)+2*' '+str(statistics.stdev(list_nilaiakhir_I))+3*' '+
      str(min(list_nilaiakhir_I))+6*' '+str(max(list_nilaiakhir_I))+2*' '+'|')
print('|'+'IPB UNIVERSITY  '+6*' '+str(ndata)+4*' '+str(jumnakhir/ndata)+2*' '+str((total_Selisih_kuadrat_nilaiakhir/ndata)**0.5)+2*' '+
      str(min(nakhir))+6*' '+str(max(nakhir))+2*' '+'|')
print('|'+84*'_'+'|')

# Membuat list untuk mempermudah pembuatan data frame UTS
Fakultas=["FAHUTAN","SKHB","FPIK","FAPET","FAHUTAN","FATETA","FMIPA","FEM","FEMA","IPB"]
Jumlah=[ndata_A,ndata_B,ndata_C,ndata_D,ndata_E,ndata_F,ndata_G,ndata_H,ndata_I,ndata]
Rata2_UTS=[jumUTS_A/ndata_A,jumUTS_B/ndata_B,jumUTS_C/ndata_C,jumUTS_D/ndata_D,jumUTS_E/ndata_E,jumUTS_F/ndata_F,jumUTS_G/ndata_G,jumUTS_H/ndata_H,jumUTS_I/ndata_I,jumUTS/ndata]
stDev_UTS=[statistics.stdev(list_UTS_A),statistics.stdev(list_UTS_B),statistics.stdev(list_UTS_C),statistics.stdev(list_UTS_D),statistics.stdev(list_UTS_E),statistics.stdev(list_UTS_F),statistics.stdev(list_UTS_G),statistics.stdev(list_UTS_H),(total_Selisih_kuadrat_nilaiUTS/ndata)**0.5]
min_UTS=[min(list_UTS_A),min(list_UTS_B),min(list_UTS_C),min(list_UTS_D),min(list_UTS_E),min(list_UTS_F),min(list_UTS_G),min(list_UTS_H),min(list_UTS_I),min(uts)]
max_UTS=[max(list_UTS_A),max(list_UTS_B),max(list_UTS_C),max(list_UTS_D),max(list_UTS_E),max(list_UTS_F),max(list_UTS_G),max(list_UTS_H),max(list_UTS_I),max(uts)]
                                                                                                                            
# Membuat list untuk mempermudah pembuatan data frame UAS 
Fakultas=["FAHUTAN","SKHB","FPIK","FAPET","FAHUTAN","FATETA","FMIPA","FEM","FEMA","IPB"]
Jumlah=[ndata_A,ndata_B,ndata_C,ndata_D,ndata_E,ndata_F,ndata_G,ndata_H,ndata_I]
Rata2_UAS=[jumUAS_A/ndata_A,jumUAS_B/ndata_B,jumUAS_C/ndata_C,jumUAS_D/ndata_D,jumUAS_E/ndata_E,jumUAS_F/ndata_F,jumUAS_G/ndata_G,jumUAS_H/ndata_H,jumUAS_I/ndata_I,ndata]
stDev_UAS=[statistics.stdev(list_UAS_A),statistics.stdev(list_UAS_B),statistics.stdev(list_UAS_C),statistics.stdev(list_UAS_D),statistics.stdev(list_UAS_E),statistics.stdev(list_UAS_F),statistics.stdev(list_UAS_G),statistics.stdev(list_UAS_H),statistics.stdev(list_UAS_I),(total_Selisih_kuadrat_nilaiUAS/ndata)**0.5]
min_UAS=[min(list_UAS_A),min(list_UAS_B),min(list_UAS_C),min(list_UAS_D),min(list_UAS_E),min(list_UAS_F),min(list_UAS_G),min(list_UAS_H),min(list_UAS_I),min(uas)]
max_UAS=[max(list_UAS_A),max(list_UAS_B),max(list_UAS_C),max(list_UAS_D),max(list_UAS_E),max(list_UAS_F),max(list_UAS_G),max(list_UAS_H),max(list_UAS_I),max(uas)]

# Membuat list untuk mempermudah pembuatan data frame NILAI AKHIR
Fakultas=["FAHUTAN","SKHB","FPIK","FAPET","FAHUTAN","FATETA","FMIPA","FEM","FEMA","IPB"]
Jumlah=[ndata_A,ndata_B,ndata_C,ndata_D,ndata_E,ndata_F,ndata_G,ndata_H,ndata_I,ndata]
Rata2_NAkhir=[jumnakhir_A/ndata_A,jumnakhir_B/ndata_B,jumnakhir_C/ndata_C,jumnakhir_D/ndata_D,jumnakhir_E/ndata_E,jumnakhir_F/ndata_F,jumnakhir_G/ndata_G,jumnakhir_H/ndata_H,jumnakhir_I/ndata_I,ndata]
stDev_NAkhir=[statistics.stdev(list_nilaiakhir_A),statistics.stdev(list_nilaiakhir_B),statistics.stdev(list_nilaiakhir_C),statistics.stdev(list_nilaiakhir_D),statistics.stdev(list_nilaiakhir_E),statistics.stdev(list_nilaiakhir_F),statistics.stdev(list_nilaiakhir_G),statistics.stdev(list_nilaiakhir_H),statistics.stdev(list_nilaiakhir_I),(total_Selisih_kuadrat_nilaiakhir/ndata)**0.5]
min_NAkhir=[min(list_nilaiakhir_A),min(list_nilaiakhir_B),min(list_nilaiakhir_C),min(list_nilaiakhir_D),min(list_nilaiakhir_E),min(list_nilaiakhir_F),min(list_nilaiakhir_G),min(list_nilaiakhir_H),min(list_nilaiakhir_I),min(nakhir)]
max_NAkhir=[max(list_nilaiakhir_A),max(list_nilaiakhir_B),max(list_nilaiakhir_C),max(list_nilaiakhir_D),max(list_nilaiakhir_E),max(list_nilaiakhir_F),max(list_nilaiakhir_G),max(list_nilaiakhir_H),max(list_nilaiakhir_I),max(nakhir)]
jumlah_A_Faperta=0
jumlah_B_Faperta=0

# Nomor 3 dan 4
# Menghitung jumlah mahasiswa yang mendapat huruf mutu A,B,C,D, dan E dari setiap fakultas
jumlah_A_Faperta=0
jumlah_B_Faperta=0
jumlah_C_Faperta=0
jumlah_D_Faperta=0
jumlah_E_Faperta=0
for i in range(163):
    if nim[i][0]=="A":
        if IP[i]==4:
            jumlah_A_Faperta+=1
        if IP[i]==3:
            jumlah_B_Faperta+=1
        if IP[i]==2:
            jumlah_C_Faperta+=1
        if IP[i]==1:
            jumlah_D_Faperta+=1
        if IP[i]==0:
            jumlah_E_Faperta+=1

jumlah_A_SKHB=0
jumlah_B_SKHB=0
jumlah_C_SKHB=0
jumlah_D_SKHB=0
jumlah_E_SKHB=0
for i in range(163):
    if nim[i][0]=="B":
        if IP[i]==4:
            jumlah_A_SKHB+=1
        if IP[i]==3:
            jumlah_B_SKHB+=1
        if IP[i]==2:
            jumlah_C_SKHB+=1
        if IP[i]==1:
            jumlah_D_SKHB+=1
        if IP[i]==0:
            jumlah_E_SKHB+=1

jumlah_A_FPIK=0
jumlah_B_FPIK=0
jumlah_C_FPIK=0
jumlah_D_FPIK=0
jumlah_E_FPIK=0
for i in range(163):
    if nim[i][0]=="C":
        if IP[i]==4:
            jumlah_A_FPIK+=1
        if IP[i]==3:
            jumlah_B_FPIK+=1
        if IP[i]==2:
            jumlah_C_FPIK+=1
        if IP[i]==1:
            jumlah_D_FPIK+=1
        if IP[i]==0:
            jumlah_E_FPIK+=1

jumlah_A_Fapet=0
jumlah_B_Fapet=0
jumlah_C_Fapet=0
jumlah_D_Fapet=0
jumlah_E_Fapet=0
for i in range(163):
    if nim[i][0]=="D":
        if IP[i]==4:
            jumlah_A_Fapet+=1
        if IP[i]==3:
            jumlah_B_Fapet+=1
        if IP[i]==2:
            jumlah_C_Fapet+=1
        if IP[i]==1:
            jumlah_D_Fapet+=1
        if IP[i]==0:
            jumlah_E_Fapet+=1

jumlah_A_Fahutan=0
jumlah_B_Fahutan=0
jumlah_C_Fahutan=0
jumlah_D_Fahutan=0
jumlah_E_Fahutan=0
for i in range(163):
    if nim[i][0]=="E":
        if IP[i]==4:
            jumlah_A_Fahutan+=1
        if IP[i]==3:
            jumlah_B_Fahutan+=1
        if IP[i]==2:
            jumlah_C_Fahutan+=1
        if IP[i]==1:
            jumlah_D_Fahutan+=1
        if IP[i]==0:
            jumlah_E_Fahutan+=1
            
jumlah_A_Fateta=0
jumlah_B_Fateta=0
jumlah_C_Fateta=0
jumlah_D_Fateta=0
jumlah_E_Fateta=0
for i in range(163):
    if nim[i][0]=="F":
        if IP[i]==4:
            jumlah_A_Fateta+=1
        if IP[i]==3:
            jumlah_B_Fateta+=1
        if IP[i]==2:
            jumlah_C_Fateta+=1
        if IP[i]==1:
            jumlah_D_Fateta+=1
        if IP[i]==0:
            jumlah_E_Fateta+=1
            
jumlah_A_FMIPA=0
jumlah_B_FMIPA=0
jumlah_C_FMIPA=0
jumlah_D_FMIPA=0
jumlah_E_FMIPA=0
for i in range(163):
    if nim[i][0]=="G":
        if IP[i]==4:
            jumlah_A_FMIPA+=1
        if IP[i]==3:
            jumlah_B_FMIPA+=1
        if IP[i]==2:
            jumlah_C_FMIPA+=1
        if IP[i]==1:
            jumlah_D_FMIPA+=1
        if IP[i]==0:
            jumlah_E_FMIPA+=1
            
jumlah_A_FEM=0
jumlah_B_FEM=0
jumlah_C_FEM=0
jumlah_D_FEM=0
jumlah_E_FEM=0
for i in range(163):
    if nim[i][0]=="H":
        if IP[i]==4:
            jumlah_A_FEM+=1
        if IP[i]==3:
            jumlah_B_FEM+=1
        if IP[i]==2:
            jumlah_C_FEM+=1
        if IP[i]==1:
            jumlah_D_FEM+=1
        if IP[i]==0:
            jumlah_E_FEM+=1
        
jumlah_A_Fema=0
jumlah_B_Fema=0
jumlah_C_Fema=0
jumlah_D_Fema=0
jumlah_E_Fema=0
for i in range(163):
    if nim[i][0]=="I":
        if IP[i]==4:
            jumlah_A_Fema+=1
        if IP[i]==3:
            jumlah_B_Fema+=1
        if IP[i]==2:
            jumlah_C_Fema+=1
        if IP[i]==1:
            jumlah_D_Fema+=1
        if IP[i]==0:
            jumlah_E_Fema+=1

# Menghitung jumlah mahasiswa IPB yang mendapat huruf mutu A,B,C,D, dan E
jumlah_A_IPB = (jumlah_A_Faperta + jumlah_A_SKHB + jumlah_A_FPIK + jumlah_A_Fapet + jumlah_A_Fahutan + jumlah_A_Fateta + jumlah_A_FMIPA + jumlah_A_FEM + jumlah_A_Fema)
jumlah_B_IPB = (jumlah_B_Faperta + jumlah_B_SKHB + jumlah_B_FPIK + jumlah_B_Fapet + jumlah_B_Fahutan + jumlah_B_Fateta + jumlah_B_FMIPA + jumlah_B_FEM + jumlah_B_Fema)
jumlah_C_IPB = (jumlah_C_Faperta + jumlah_C_SKHB + jumlah_C_FPIK + jumlah_C_Fapet + jumlah_C_Fahutan + jumlah_C_Fateta + jumlah_C_FMIPA + jumlah_C_FEM + jumlah_C_Fema)
jumlah_D_IPB = (jumlah_D_Faperta + jumlah_D_SKHB + jumlah_D_FPIK + jumlah_D_Fapet + jumlah_D_Fahutan + jumlah_D_Fateta + jumlah_D_FMIPA + jumlah_D_FEM + jumlah_D_Fema)
jumlah_E_IPB = (jumlah_E_Faperta + jumlah_E_SKHB + jumlah_E_FPIK + jumlah_E_Fapet + jumlah_E_Fahutan + jumlah_E_Fateta + jumlah_E_FMIPA + jumlah_E_FEM + jumlah_E_Fema)

#Mencari IP tiap fakultas
IP_Faperta = ((4*int(jumlah_A_Faperta)+3*int(jumlah_B_Faperta)+2*int(jumlah_C_Faperta)+1*int(jumlah_D_Faperta)+0*int(jumlah_E_Faperta))/ndata_A)
IP_SKHB = ((4*int(jumlah_A_SKHB)+3*int(jumlah_B_SKHB)+2*int(jumlah_C_SKHB)+1*int(jumlah_D_SKHB)+0*int(jumlah_E_SKHB))/ndata_B)
IP_FPIK = ((4*int(jumlah_A_FPIK)+3*int(jumlah_B_FPIK)+2*int(jumlah_C_FPIK)+1*int(jumlah_D_FPIK)+0*int(jumlah_E_FPIK))/ndata_C)
IP_Fapet = ((4*int(jumlah_A_Fapet)+3*int(jumlah_B_Fapet)+2*int(jumlah_C_Fapet)+1*int(jumlah_D_Fapet)+0*int(jumlah_E_Fapet))/ndata_D)
IP_Fahutan = ((4*int(jumlah_A_Fahutan)+3*int(jumlah_B_Fahutan)+2*int(jumlah_C_Fahutan)+1*int(jumlah_D_Fahutan)+0*int(jumlah_E_Fahutan))/ndata_E)
IP_Fateta = ((4*int(jumlah_A_Fateta)+3*int(jumlah_B_Fateta)+2*int(jumlah_C_Fateta)+1*int(jumlah_D_Fateta)+0*int(jumlah_E_Fateta))/ndata_F)
IP_FMIPA = ((4*int(jumlah_A_FMIPA)+3*int(jumlah_B_FMIPA)+2*int(jumlah_C_FMIPA)+1*int(jumlah_D_FMIPA)+0*int(jumlah_E_FMIPA))/ndata_G)
IP_FEM = ((4*int(jumlah_A_FEM)+3*int(jumlah_B_FEM)+2*int(jumlah_C_FEM)+1*int(jumlah_D_FEM)+0*int(jumlah_E_FEM))/ndata_H)
IP_Fema = ((4*int(jumlah_A_Fema)+3*int(jumlah_B_Fema)+2*int(jumlah_C_Fema)+1*int(jumlah_D_Fema)+0*int(jumlah_E_Fema))/ndata_I)
IP_IPB = ((4*jumlah_A_IPB+3*jumlah_B_IPB+2*jumlah_C_IPB+1*jumlah_D_IPB+0*jumlah_E_IPB)/163)

# Membuat list untuk mempermudah pembuatan data frame
Fakultas=["FAHUTAN","SKHB","FPIK","FAPET","FAHUTAN","FATETA","FMIPA","FEM","FEMA","IPB"]
nilai_A=[jumlah_A_Faperta, jumlah_A_SKHB, jumlah_A_FPIK, jumlah_A_Fapet, jumlah_A_Fahutan, jumlah_A_Fateta, jumlah_A_FMIPA, jumlah_A_FEM, jumlah_A_Fema, jumlah_A_IPB]
nilai_B=[jumlah_B_Faperta, jumlah_B_SKHB, jumlah_B_FPIK, jumlah_B_Fapet, jumlah_B_Fahutan, jumlah_B_Fateta, jumlah_B_FMIPA, jumlah_B_FEM, jumlah_B_Fema, jumlah_B_IPB]
nilai_C=[jumlah_C_Faperta, jumlah_C_SKHB, jumlah_C_FPIK, jumlah_C_Fapet, jumlah_C_Fahutan, jumlah_C_Fateta, jumlah_C_FMIPA, jumlah_C_FEM, jumlah_C_Fema, jumlah_C_IPB]
nilai_D=[jumlah_D_Faperta, jumlah_D_SKHB, jumlah_D_FPIK, jumlah_D_Fapet, jumlah_D_Fahutan, jumlah_D_Fateta, jumlah_D_FMIPA, jumlah_D_FEM, jumlah_D_Fema, jumlah_D_IPB]
nilai_E=[jumlah_E_Faperta, jumlah_E_SKHB, jumlah_E_FPIK, jumlah_E_Fapet, jumlah_E_Fahutan, jumlah_E_Fateta, jumlah_E_FMIPA, jumlah_E_FEM, jumlah_E_Fema, jumlah_E_IPB]
IP = [IP_Faperta, IP_SKHB, IP_FPIK, IP_Fapet, IP_Fahutan, IP_FMIPA, IP_FEM, IP_Fema, IP_IPB]

#Membuat data frame
print("""
 ____________________________________________________________
|                 Distribusi Huruf Mutu                      |""")
print('|'+'Fakultas/Sekolah'+3*' '+'A'+3*' '+'B'+3*' '+'C'+3*' '+'D'+3*' '+'E'+12*' '+'IP'+10*' '+'|')
print('|'+'FAPERTA         '+3*' '+str(jumlah_A_Faperta)+3*' '+str(jumlah_B_Faperta)+3*' '+str(jumlah_C_Faperta)+3*' '+
      str(jumlah_D_Faperta)+3*' '+str(jumlah_E_Faperta)+3*' '+str(IP_Faperta)+3*' '+'|')
print('|'+'SKHB            '+3*' '+str(jumlah_A_SKHB)+3*' '+str(jumlah_B_SKHB)+2*' '+str(jumlah_C_SKHB)+3*' '+
      str(jumlah_D_SKHB)+3*' '+str(jumlah_E_SKHB)+3*' '+str(IP_SKHB)+4*' '+'|')
print('|'+'FPIK            '+3*' '+str(jumlah_A_FPIK)+3*' '+str(jumlah_B_FPIK)+3*' '+str(jumlah_C_FPIK)+3*' '+
      str(jumlah_D_FPIK)+3*' '+str(jumlah_E_FPIK)+3*' '+str(IP_FPIK)+18*' '+'|')
print('|'+'FAPET           '+3*' '+str(jumlah_A_Fapet)+3*' '+str(jumlah_B_Fapet)+3*' '+str(jumlah_C_Fapet)+3*' '+
      str(jumlah_D_Fapet)+3*' '+str(jumlah_E_Fapet)+3*' '+str(IP_Fapet)+4*' '+'|')
print('|'+'FAHUTAN         '+3*' '+str(jumlah_A_Fahutan)+3*' '+str(jumlah_B_Fahutan)+3*' '+str(jumlah_C_Fahutan)+3*' '+
      str(jumlah_D_Fahutan)+3*' '+str(jumlah_E_Fahutan)+3*' '+str(IP_Fahutan)+3*' '+'|')
print('|'+'FATETA          '+3*' '+str(jumlah_A_Fateta)+3*' '+str(jumlah_B_Fateta)+3*' '+str(jumlah_C_Fateta)+2*' '+
      str(jumlah_D_Fateta)+3*' '+str(jumlah_E_Fateta)+3*' '+str(IP_Fateta)+18*' '+'|')
print('|'+'FMIPA           '+3*' '+str(jumlah_A_FMIPA)+3*' '+str(jumlah_B_FMIPA)+3*' '+str(jumlah_C_FMIPA)+3*' '+
      str(jumlah_D_FMIPA)+3*' '+str(jumlah_E_FMIPA)+3*' '+str(IP_FMIPA)+4*' '+'|')
print('|'+'FEM             '+3*' '+str(jumlah_A_FEM)+3*' '+str(jumlah_B_FEM)+3*' '+str(jumlah_C_FEM)+3*' '+
      str(jumlah_D_FEM)+3*' '+str(jumlah_E_FEM)+3*' '+str(IP_FEM)+4*' '+'|')
print('|'+'FEMA            '+3*' '+str(jumlah_A_Fema)+3*' '+str(jumlah_B_Fema)+3*' '+str(jumlah_C_Fema)+3*' '+
      str(jumlah_D_Fema)+3*' '+str(jumlah_E_Fema)+3*' '+str(IP_Fema)+3*' '+'|')
print('|'+'IPB UNIVERSITY  '+3*' '+str(jumlah_A_IPB)+2*' '+str(jumlah_B_IPB)+2*' '+str(jumlah_C_IPB)+2*' '+
      str(jumlah_D_IPB)+2*' '+str(jumlah_E_IPB)+3*' '+str(IP_IPB)+3*' '+'|')
print('|'+60*'_'+'|')
            
