from time import sleep
print('\033[1;33m-=-\033[m'*17)
print('\033[1;33m------\033[m \033[4;31mConversor:Binário, Octal, Hexadecimal\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*17, '\n')
num = int(input('Digite um numero inteiro:'))
print('')
print('Escolha qual a base de conversão: ')
print('(1) - para Binário\n(2) - para Octal\n(3) - para Hexadecimal')
op = int(input('Digite a sua opção:'))
print('\033[1;33mCALCULANDO...\033[m')
sleep(3)
if op == 1:
    print(f'O número {num} em binário é:', '\033[1;33m', bin(num)[2:], '\033[m')
elif op == 2:
    print(f'O número {num} em octal é:', '\033[1;33m', oct(num)[2:], '\033[m')
elif op == 3:
    print(f'O número {num} em hexadecimal é:', '\033[1;33m', hex(num)[2:], '\033[m')
else:
    print('Opção inválida')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
