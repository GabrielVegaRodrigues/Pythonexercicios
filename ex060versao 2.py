from time import sleep
print('\033[1;33m-=-\033[m'*11)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA FATORIAL\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
num = int(input('Digite um número:'))
print(f'Calculando {num}! ->', end=' ')
sleep(2)
c = num
f = 1
for c in range(num, 0, -1):
    if c != 1:
        print(c, end=' x ')
        f = c * f
    else:
        print(end='1 = ')
print(f'{f}')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
