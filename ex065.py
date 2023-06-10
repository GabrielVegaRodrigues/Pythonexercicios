print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mCALCULADORA DE VALORES VERSÃO 2\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
n = soma = cont = maior = menor = 0
continuar = 's'.upper()
while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    cont += 1
    soma += n
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'''A média entre todos os {cont} valores digitados foi: {media:.2f}
O maior valor digitado foi: {maior}
O menor valor digitado foi: {menor}''')

