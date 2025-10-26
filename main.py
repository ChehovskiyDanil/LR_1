import math

print('Ввдедите данные для вычисления по формулам: ')
a = float(input('Введите a = '))
b = float(input('Введите b = '))
c = float(input('Введите c = '))
pi = 3.14159

z1 = ((a-b-c)/2)*a
print (('z1 = ')+str(z1))
z2 = (c-b)/a+2*b
print (('z2 = ')+str(z2))
z3 = (a*c*b)/pi
print (('z3 = ')+str(z3))
z4 = ((((1/a-1/(b+c))/(1/a+1/(b+c)))*(1+(pow(b,2)+pow(c,2)+pow(a,2))/(2*b*c))/(a-b-c/(a*b*c))))
print (('z4 = ')+str(z4))
z5 = (z1+z2+z3+z4)/4
print (('z5 = ')+str(z5))