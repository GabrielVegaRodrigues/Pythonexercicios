print('\033[1;33m-=-\033[m'*8)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*8, '\n')
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
lista = [1, 2, 3, 4, 5]
print('''
(1) - SOMAR
(2) - MULTIPLICAR
(3) - MAIOR
(4) - NOVOS NUMEROS
(5) - SAIR DO PROGRAMA''')
opcao = int(input('Qual a sua opção? '))
while opcao == 4:
    num1 = int(input('\nDigite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    lista = [1, 2, 3, 4, 5]
    print('''
    (1) - SOMAR
    (2) - MULTIPLICAR
    (3) - MAIOR
    (4) - NOVOS NUMEROS
    (5) - SAIR DO PROGRAMA''')
    opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    soma = num1 + num2
    print(f'\nO resuldado da soma de {int(num1)} mais {int(num2)} é: {int(soma)}')
elif opcao == 2:
    mult = num1 * num2
    print(f'\nO resuldado da multiplicação de {int(num1)} vezes {int(num2)} é: {int(mult)}')
elif opcao == 3:
    if num1 > num2:
        print(f'\nEntre {int(num1)} e {int(num2)} o maior valor é {int(num1)}')
    elif num1 == num2:
        print(f'\nNão existe um valor maior entre {int(num1)} e {int(num2)} pois você digitou dois valores iguais.')
    elif num2 > num1:
        print(f'Entre {int(num1)} e {int(num2)} o maior valor é {int(num2)}')
elif opcao == 5:
    print('\nVocê escolheu sair do programa.Obrigado e até a próxima.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
