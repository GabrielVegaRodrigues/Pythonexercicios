print('\033[1;33m-=-\033[m'*23)
print(f'\033[1;33m------\033[m \033[4;31mSOMA DOS NUMEROS IMPARES MULTIPLOS DE 3 DO 1 ATÉ O 500)\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*23, '\n')
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont+1
        s = s + c
print(f'A soma dos {cont} números ímpares múltiplos de 3 do numero 1 até o 500 é {s}.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
