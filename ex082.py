valores = []
pares = []
impares = []
opcao = 's'
while True:
    if opcao in'sS':
        valor = int(input('Digite um número: '))
        valores.append(valor)
        opcao = input('Quer continuar? S/N ')
        if (valor%2) == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    else:
        break
print(f'A lista completa digitada foi: {valores}')
print(f'A lista de números pares digitados foi: {pares}')
print(f'A lista de números pares digitados foi: {impares}')
