import math
print('\033[1;33m-=-\033[m'*12)
print(f'\033[1;33m------\033[m \033[4;31mSEQUÊNCIA DE FIBONACCI\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*12, '\n')
n = int(input('Quantos termos você gostaria de mostrar? '))
ultimo = 0
penu = 1
if n == 1:
    print('\n\033[1;31mO número digitado deve ser maior do que 1 !!!\033[m')
elif n == 2:
    print(f'{ultimo} -> {penu} -> {penu}', end=' -> ')
    print(end='\033[31mFIM\033[m')
else:
    print(f'{ultimo} -> {penu}', end=' -> ')
    cont = 3
    while cont <= n:
        termo = ultimo + penu
        print(termo, end=' -> ')
        ultimo = penu
        penu = termo
        cont += 1
    print(end='\033[31mFIM\033[m')



