import random
import time
print('\033[1;33m-=-\033[m'*15)
print(f'\033[1;33m------\033[m \033[4;31mJOKENPO(pedra, papel e tesoura)\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*15, '\n')
lista = ('Pedra', 'Papel', 'Tesoura')
escopc = random.randint(0, 2)
print('Faça a sua escolha:')
print('''(0) - Pedra
(1) - Papel
(2) - Tesoura''')
esco = int(input('Qual a sua opção: '))
if esco > 2:
    print('\033[4;31mOpção inválida, tente novamente!!!\033[m')
elif esco <= 2:
    time.sleep(0.5)
    print('JO', end='')
    time.sleep(0.5)
    print('KEN', end='')
    time.sleep(0.5)
    print('PO!!!\n', end='')
    time.sleep(1)
    print('')
    print(f'Você escolheu {lista[esco]} e o computador escolheu {lista[escopc]}')
if escopc == 0:
    if esco == 0:
        print(f'Tivemos um EMPATE.')
    elif esco == 1:
        print(f'Você GANHOU.')
    elif esco == 2:
        print(f'Você PERDEU.')
if escopc == 1:
    if esco == 1:
        print(f'Tivemos um EMPATE.')
    elif esco == 2:
        print(f'Você GANHOU.')
    elif esco == 0:
        print(f'Você PERDEU.')
if escopc == 2:
    if esco == 2:
        print(f'Tivemos um EMPATE.')
    elif esco == 1:
        print(f'Você PERDEU.')
    elif esco == 0:
        print(f'Você GANHOU.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
