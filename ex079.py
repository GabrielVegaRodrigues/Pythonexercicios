valores = []
opcao = 's'
while opcao in 'sS':
    valor = (input('Digite um valor: '))
    if valor not in valores:
        print('Valor incluído com sucesso...')
        opcao = input('Você deseja incluir outro valor? S/N ')
        valores.append(valor)
    else:
        print('Valor duplicado, tente novamente...')
        opcao = input('Você deseja incluir outro valor? S/N ')
if opcao in 'nN':
    print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
    print(f'Você digitou os valores: ', sorted(valores))



