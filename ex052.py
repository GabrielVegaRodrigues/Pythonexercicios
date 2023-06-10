print('\033[1;33m-=-\033[m'*15)
print(f'\033[1;33m------\033[m \033[4;31m10 VERIFICADOR DE NÚMEROS PRIMOS\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*15, '\n')
n = int(input("Digite um numero inteiro:"))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot = tot+1
        print('\033[33m', end='')

    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
if tot <= 2:
    print(f'\nO número {n} só é divisivel por 1 e por ele mesmo, por isso ele é um número PRIMO!')
else:
    print(f'\nO número {n} é divisivel por 1 por, por ele mesmo e por mais {tot-2} número(s)\nPor isso ele não é um número PRIMO!')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
