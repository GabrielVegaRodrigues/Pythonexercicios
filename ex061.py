print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31m10 PRIMEIROS TERMOS DE UMA PA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
primeirtermo = int(input('Digite o primeiro termo desta Progressão Aritmética:'))
razao = int(input('Digite a razão desta Progressão aritmética:'))
termo = primeirtermo
cont = 1
while not cont == 11:
        cont += 1
        print(termo, end=' > ')
        termo += razao
print(end='\033[1mFIM\033[m')
