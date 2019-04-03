a=int(input('Введите число A: '))
b=int(input('Введите число B: '))
c=int(input('Введите число C: '))
d=int(input('Введите число D: '))
k=int(input('Введите число K: '))
if b !=0 and a !=0:
    print(abs(1 - a*b*c - a*(b**2-c**12) + (b-c+a)*(12+b)/(c-a)))
else:
    print('Переменные A и B не могут принимать нули, так как на ноль делить нельзя.')
