from time import sleep
print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31m10 PRIMEIROS TERMOS DE UMA PA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
primeirtermo = int(input('Digite o primeiro termo desta Progressão Aritmética:'))
razao = int(input('Digite a razão desta Progressão aritmética:'))
termo = primeirtermo
cont = 1
total = 0
esc = 10
print('\n\033[1;31mPARA SAIR DO PROGRAMA A QUALQUER MOMENTO DIGITE 0!!!\033[m\n')
while esc != 0:
    total = total + esc
    while cont <= total:
        print(termo, end=' > ')
        termo += razao
        cont += 1
    print(end='\033[1mPAUSA\033[m')
    print('\n\033[1mVocê gostaria de ver mais termos desta PA?\033[m')
    esc = int(input('''Digite a quantidade de termos que gostaria de ver a mais: '''))
print('\nVocê escolheu sair do programa.')
print(f'Você solicitou {total} termos desta PA.')
print('Desligando...')
sleep(2)
print('\n\033[31mFIM\033[m')
