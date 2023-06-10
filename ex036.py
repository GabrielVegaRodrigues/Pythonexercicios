from time import sleep
print('\033[1;33m-=-\033[m'*15)
print('\033[1;33m------\033[m \033[4;31mAprovação de empréstimo Bancário\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*15, '\n')
casa = float(input('Informe o valor da casa desejada: R$'))
sal = float(input('Informe o seu salário: R$'))
tempo = float(input('Informe em quantos anos deseja pagar o financiamento: '))*12
ap = (sal*30/100)
vm = casa/tempo
print('Calculando...'), sleep(3)
print('')
if vm > ap:
    print('O valor da prestação mensal excedeu 30% do seu salário!')
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m\n')
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[m')
    print(f'O valor da prestação mensal ficou!\n\033[1;32mR$ {vm:.2f}\033[m')
    print(f'O prazo para pagamento é de:\n\033[1;33m{int(tempo/12)} anos\033[m\n')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')

