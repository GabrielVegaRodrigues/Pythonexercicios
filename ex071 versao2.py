print('\033[1;33m-=-\033[m'*10)
print(f'\033[1;33m------\033[m \033[4;31mCAIXA ELETRONICO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*10, '\n')
saque = int(input('Qual valor você deseja sacar? R$ '))
ced = 50
totaldecedulas = 0
while True:
    if saque >= ced:
        saque -= ced
        totaldecedulas += 1
    else:
        if totaldecedulas > 0:
            print(f'Total de {totaldecedulas} cedulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaldecedulas = 0
        if saque == 0:
            break
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')

