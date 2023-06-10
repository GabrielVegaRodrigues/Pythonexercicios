from time import sleep
print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA DE VALORES\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
n = 0
soma = 0
cont = 0
n = int(input('Digite um número inteiro(ou 999 para parar): '))
while n != 999:
    if n != 999:
        soma += n
        cont += 1
        n = int(input('Digite um número inteiro(ou 999 para parar): '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
print('Finalizando...')
sleep(2)
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
