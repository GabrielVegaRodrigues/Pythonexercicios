print('Calculadora de consumo de tinta')
print('')
alt = float(input('Digite a altura da sua parede:'))
larg = float(input('Digite a largura da sua parede:'))
area = (alt*larg)/2
print(f'A área da tua parede é: {alt*larg:.2f}M²')
print(f'Tu precisará de {area:,.2f}Lts de tinta para pintar toda a tua parede com uma demão de tinta.')
