lista = ('Pão', 0.50,
         'Arroz', 5.00,
         'Feijão', 3.00,
         'Batata', 7.99,
         'Carne', 32.90,
         'Ovo', 11.00)
print('\033[1;33m-=-\033[m'*10)
print(f'\033[1;33m------\033[m \033[4;31mLISTAGEM DE PREÇO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*10)
print('~'*50)
for pos in range(0, len(lista), 2):
    print(f'{lista[pos]:.<40}R$: {lista[pos+1]:.2f}')
print('~'*50)