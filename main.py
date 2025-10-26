import math

print('Ввдедите данные для вычисления по формулам: ')
a = float(input('Введите a = '))
b = float(input('Введите b = '))
c = float(input('Введите c = '))

z1 = ((a-b-c)/2)*a
print (('z1 = ')+str(z1))
z2 = (c-b)/a+2*b
print (('z2 = ')+str(z2))