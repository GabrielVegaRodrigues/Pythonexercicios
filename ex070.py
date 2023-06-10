print('\033[1;33m-=-\033[m'*10)
print(f'\033[1;33m------\033[m \033[4;31mCONTROLE DE COMPRAS\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*10, '\n')
esc = nomebar = ' '
caros = tot = menor = cont = 0
while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o preço do produto:R$ '))
    tot += valor
    cont += 1
    esc = ' '
    while esc not in 'SN':
        esc = input('Deseja continuar cadastrando?[S/N] ').strip().upper()[0]
    print('~' * 40)
    if valor > 1000:
        caros += 1
    if cont == 1 or valor < menor:
        nomebar = nome
        menor = valor
    if esc == 'N':
        break
print('~' * 40)
print(f'Sua lista custou um total de:R$ {tot:.2f}')
print(f'Sua lista tem {caros} produto(s) custando mais de R$ 1000,00')
print(f'Na sua lista o produto mais barato foi: {nomebar} custando R$ {menor:.2f}')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
