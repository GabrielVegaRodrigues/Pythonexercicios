import random
from time import sleep
print('\033[1;33m-=-\033[m'*11)
print(f'\033[1;33m------\033[m \033[4;31mJOGO DA ADIVINHAÇÃO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
cont = 1
esc = random.randint(0, 10)
print('Sou seu computador... acabei de pensar em um número entre 0 e 10.\nSerá que voce consegue adivinhar qual foi?')
nusu = int(input('Digitar o número que você acha que "eu" pensei:\n'))
print('PROCESSANDO...')
sleep(1)
while esc != nusu:
    if nusu < esc:
        print('Mais..')
        cont = cont + 1
        print(f'Infelizmente você errou.Faça uma nova tentativa.')
        nusu = int(input('Digite o número que você acha que "eu" pensei:\n'))
        print('PROCESSANDO...')
        sleep(1)
        print('')
    else:
        print('Menos...')
        cont = cont + 1
        print(f'Infelizmente você errou.Faça uma nova tentativa.')
        nusu = int(input('Digite o número que você acha que "eu" pensei:\n'))
        print('PROCESSANDO...')
        sleep(1)
        print('')
print(f'Você acertou!!! Parabéns o número escolhido pelo computador foi: {esc} e você escolheu: {nusu}')
print(f'Você precisou de {cont} palpites para acertar!')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
