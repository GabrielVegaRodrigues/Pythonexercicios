print('\033[1;33m-=-\033[m'*15)
print('\033[1;33m------\033[m \033[4;31mComparador de números Inteiros\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*15, '\n')
num1 = int(input('Digite o primeiro número inteiro:'))
num2 = int(input('Digite o segundo número inteiro:'))
if num1 > num2:
    print(f'O \033[1;33mprimeiro\033[m número é maior! O número {num1} é maior que o número {num2}.')
elif num2 > num1:
    print(f'O \033[1;33mSegundo\033[m número é maior! O número {num2} é maior que o número {num1}.')
else:
    print('Não existe número maior nem menor, os números digitados são \033[1;33miguais!!!\033[m')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
