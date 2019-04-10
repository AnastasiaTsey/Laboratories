n=int(input('Введите длину списка: '))
l = []
for i in range (0, n):
    l.append(int(input('Введите элемент списка: ')))
print (l)
    #del range[4,5,6,7,8]
l.remove(4)
l.remove(5)
l.remove(6)
l.remove(7)
l.remove(8)
print(l)

for i in range (0, 2):
    l.append(int(input('Введите новый элемент: ')))

print(l)

