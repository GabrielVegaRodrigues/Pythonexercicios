print('Preço da passagem')
d = float(input('Digite a distância da sua viagem em km.\nkm:'))
pp = d * 0.50
pr = d * 0.45
if d <= 200:
    print(f'O valor da sua passagem é :\nR${pp:.2f}')
else:
    print(f'O valor da sua passagem é :\nR${pr:.2f}')
print('')
print('-----FIM-----')
