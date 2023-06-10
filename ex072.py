from time import sleep
print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mNÚMERO DIGITADO POR EXTENSO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
esc = 'S'
while esc == 'S':
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente !!! ', end='')
    print(f'Você digitou o número {n[num]}.')
    esc = input('Você quer continuar?[S/N]').strip().upper()[0]
    print('')
print('Finalizando o programa...')
sleep(2)
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
