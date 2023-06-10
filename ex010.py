print('Conversor Real x Dolar x Euro')
print('')
print('Cotação atual do Dolar: $ 3.27\nCotação atual do  Euro: € 4.25')
print('')
n = float(input('Digite quantos reais tu tens na carteira: \n"(OBS: use ponto ao invés de virgula)"\nR$:'))
res = n/3.27
res2 = n/4.25
print(f'Com os teus R$ {n} tu consegue comprar:\n$ {res:,.2f}\n€ {res2:,.2f} ')
