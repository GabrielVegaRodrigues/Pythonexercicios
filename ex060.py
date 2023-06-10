from time import sleep
print('\033[1;33m-=-\033[m'*11)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA FATORIAL\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
num = int(input('Digite um número:'))
print(f'Calculando {num}! ->', end=' ')
sleep(2)
multi = num
f = 1
while multi != 1:
    print(multi, end=' x ')
    f = f * multi
    multi -= 1
    if multi == 1:
        print(multi, end=' =')
print(f' {f}')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
