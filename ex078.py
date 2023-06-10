valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] < menor:
            menor = valores[cont]
        if valores[cont] > maior:
            maior = valores[cont]
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos} -> ', end='')
print('')
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos} -> ', end='')
print('')

