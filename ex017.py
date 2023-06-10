from math import sqrt, hypot
co = float(input('Digite a medida do cateto oposto:\n'))
ca = float(input('Digite a medida do cateto adjacente:\n'))
h = sqrt(co**2 + ca**2)
print(f'O comprimento da hipotenusa é: {h:.2f}')

'''cato = float(input('Digite a medida do cateto oposto:\n'))
cata = float(input('Digite a medida do cateto adjacente:\n'))
hipo = hypot(cato,cata)
print(f'O comprimento da hipotenusa é: {hipo:,.2f}')
'''