print('\033[1;33m-=-\033[m'*7)
print(f'\033[1;33m------\033[m \033[4;31mTABUADA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*7, '\n')
n = int(input('Digite um numero para ver sua tabuada:'))
print(f'A tabuada do {n} é :\n')
for c in range(0, 11):
    print(f'{n} x {c:2} = {c*n}')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
