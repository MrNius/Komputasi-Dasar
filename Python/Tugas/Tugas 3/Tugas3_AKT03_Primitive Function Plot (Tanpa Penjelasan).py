#############################################
#
# Tugas 3 Komputasi Dasar
#--------------------------
# Kelompok : AKT03
# Tim programmer:
# 1. Antonius Aditya Rizky Wijaya_G5402221003
# 2. Sandi Agung Laksana_G5402221017
# 3. Gemala Azzahra Ocan_G5402221032
# 4. Naila Sakhsiya Akmalia_G5402221049
# 5. Annisa Aulia Putri_G5402221067
#
# Tanggal upload : 17 September 2023
#

import math

#########
# f0(x)
def f0(x):
    'f(x) = 0'
    return 0

#########
# f1(x)
def f1(x):
    'f(x) = x'
    return x

#########
# f2(x)
def f2(x):
    'f(x) = (x-2)^2'
    return (x-2)**2

#########
# f3(x)
def f3(x):
    'f(x) = 10*sin(x)'
    return 10*math.sin(x)

#########
# f4(x)
def f4(x):
    'f(x) = exp(x)'
    return math.exp(x)

################
# Plot function
#---------------

def myPlot(f,xmin,xmax):
    'Plot function f(x) for x in [xmin, xmax]'
    if f == f0:
        for a in range(41):
            print("*")
        return
    xrasio = (xmax - xmin)/40
    nilai = [f(xmin + a*xrasio) for a in range(41)]
    ymin = min(nilai)
    ymax = max(nilai)
    yrasio = (ymax - ymin)/40
    print("[xmin, xmax] = [" + str(xmin) + ", " + str(xmax) + "]")
    print("[ymin, ymax] = [" + str(ymin) + ", " + str(ymax) + "]")
    for b in range(41):
        print(" "*int((nilai[b] - ymin)/yrasio) + "*")
    return [ymin, ymax] # return minimum and maximum values of the function

##################################
# Plot area between two functions
#---------------------------------

def myPlotArea(f1,f2,xmin,xmax):
    'Plot area between two functions f1(x) and f2(x) for x in [xmin, xmax]'
    xrasio = (xmax - xmin)/40
    nilai = [[min([f1(xmin + a*xrasio), f2(xmin + a*xrasio)]), max([f1(xmin + a*xrasio), f2(xmin + a*xrasio)])] for a in range(41)]
    ymin = min([min(a) for a in nilai])
    ymax = max([max(a) for a in nilai])
    yrasio = (ymax-ymin)/40
    print("[xmin, xmax] = [" + str(xmin) + ", " + str(xmax) + "]")
    print("[ymin, ymax] = [" + str(ymin) + ", " + str(ymax) + "]")
    for b in range((41)):
        print(" "*int(round((nilai[b][0] - ymin)/yrasio)) + "*"*int(round((nilai[b][1] - ymin)/yrasio) - round((nilai[b][0] - ymin)/yrasio)))
    return [ymin, ymax] # return minimum and maximum values of the functions 


################
# Program utama
#---------------

# Fungsi-fungsi yang diplot dan daerah asal fungsi
flist=[f1, f2, f3, f4]
xmin =[ 0,  0, -math.pi, -1]
xmax =[ 1,  5, 2*math.pi, 3]

# Plot fungsi-fungsi
print('============ PLOT FUNCTIONS ============')
help(f0)
myPlot(f0, 0, 1)
for f in range(len(flist)):
    help(flist[f])
    myPlot(flist[f],xmin[f],xmax[f])

# Plot area between two functions
print()
print()
print('============ PLOT AREA BETWEEN TWO FUNCTIONS ============')
for f in range(len(flist)):
    if f == 0:
        help(f0)
        help(flist[f])
        myPlotArea(f0,flist[f],xmin[f],xmax[f])
    else:
        help(f1)
        help(flist[f])
        myPlotArea(f1,flist[f],xmin[f],xmax[f])
