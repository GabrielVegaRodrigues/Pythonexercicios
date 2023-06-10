print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA DE VALORES PARES\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
s = 0
cont = 0
for c in range(1, 7):
    inicio = int(input('Digite um número:'))
    if inicio % 2 == 0:
        s = s + inicio
        cont = cont+1
if s == 0:
    print('')
    print('Você não digitou nenhum número par, por favor tente novamente!')
else:
    print('')
    print(f'A soma entre os {cont} numeros pares digitados é: {s}')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
