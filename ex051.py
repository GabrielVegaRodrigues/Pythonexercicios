print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31m10 PRIMEIROS TERMOS DE UMA PA\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
termo = int(input('Digite o primeiro termo desta Progressão Aritmética:'))
razao = int(input('Digite a razão desta Progressão aritmética:'))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao, razao):
    print(c, end=(' > '))
print('\033[4;31mFIM\033[m')
