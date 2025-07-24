#Nomor 2
def anu(x):
    if x==1:
        return 1
    else:
        return x + anu(x-1)
print(anu(1))
#output = 1
print(anu(2))
#output = 3
print(anu(3))
#output = 6
print(2*anu(2*3))
#output = 42
