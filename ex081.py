valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Deseja digitar outro valor? S/N ')
    cont += 1
    if opcao in'nN':
        break
valores.sort(reverse=True)
print(f'Foram digitados {cont} valores. ')
print(f'A lista de valores ordenada de forma decrescente é: {valores}')
if 5 in valores:
    print('O número 5 foi digitado na lista!!!')
else:
    print('O número 5 não foi digitado na lista!!!')
