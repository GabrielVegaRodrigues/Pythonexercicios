print('Programa para calcular aumento dos funcionários.')
s = float(input('Digite o salário do funcionário:\nR$:'))
r1 = (10/100)*s
r2 = (15/100)*s
if s <= 1250:
    print(f'O sálario foi reajustado com 15% e ficou:\nR$:{s + r2:.2f}')
else:
    print(f'O salário foi reajustado em 10% e ficou:\nR$:{s + r1:.2f}')
print('')
print('-----FIM-----')
