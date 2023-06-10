from time import sleep
print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA DE VALORES VERSÃO 2\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
soma = cont = 0
while True:
    n = int(input('Digite um valor ou 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('CALCULANDO ...')
sleep(2)
print(f'\nA soma dos {cont} valores foi {soma}.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')

