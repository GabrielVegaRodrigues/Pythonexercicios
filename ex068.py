from random import randint
print('\033[1;33m-=-\033[m'*7)
print(f'\033[1;33m------\033[m \033[4;31mPAR OU ÍMPAR\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*7, '\n')
cont = 0
while True:
    print('='*40)
    jogador = int(input('Digite um valor:'))
    resu = (input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('=' * 40)
    while resu not in 'PI':
        resu = (input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    computador = randint(0, 999)
    soma = jogador + computador
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
    if soma % 2 == 0 and resu == 'P' or soma % 2 != 0 and resu == 'I':
        cont += 1
        print('Parabéns !!!! Você venceu!')
    else:
        print('GAME OVER!!! Infelizmente você perdeu!')
        break
    print('Jogue novamente')
print(f'Você jogou {jogador} e o computador jogou {computador}, total {soma}.')
print(f'Você venceu {cont} partida(s) consecutivas.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
