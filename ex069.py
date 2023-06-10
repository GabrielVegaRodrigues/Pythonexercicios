print('\033[1;33m-=-\033[m'*10)
print(f'\033[1;33m------\033[m \033[4;31mFICHA CADASTRAL\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*10, '\n')
pess = 1
maior = contsex = novinhas = 0
while True:
    idade = int(input(f'Digite a idade da {pess}ª pessoa: '))
    esc = sexo = ' '
    while sexo not in 'FM' and esc not in 'SN':
        sexo = input(f'Digite o sexo da {pess}ª pessoa[M/F]: ').strip().upper()[0]
    print('='*40)
    esc = input('Deseja continuar cadastrando?[S/N] ').strip().upper()[0]
    print('=' * 40)
    pess += 1
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        contsex += 1
    if sexo == 'F' and idade < 20:
        novinhas += 1
    if esc == 'N':
        break
print('')
print(f'Temos {maior} pesssoa(s) maiores de 18 anos cadastradas.')
print(f'Temos {contsex} homen(s) cadastrados.')
print(f'Temos {novinhas} mulher(es) menores de 20 anos cadastradas.')
print('='*40)
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
