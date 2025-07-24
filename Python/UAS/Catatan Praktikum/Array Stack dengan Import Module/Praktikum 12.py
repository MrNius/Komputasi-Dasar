import MyKOMDAS

s = MyKOMDAS.ArrayStack()
s.push('Saya')
s.push(15)
s.push(['IPB','Bogor',60])
print(s.len())
print(s.top())
print(s.len())
print(s.pop())
print(s.top())
print(s.len())

stack = MyKOMDAS.ArrayStack()
lefty='({['
righty=')}]'
ekspresi = input('Masukkan sebuah ekspresi: ')
for c in ekspresi:
    if c in lefty:
        stack.push(c)
    elif c in righty:
        d = stack.top()
        if lefty.index(d) != righty.index(c):
            break
        else:
            stack.pop()
if stack.len()>0:
    print('Ekspresi \''+ekspresi+'\' TIDAK VALID')
else:
    print('Ekspresi \''+ekspresi+'\' VALID')
