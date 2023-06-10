from datetime import date
print('\033[1;33m-=-\033[m'*14)
print(f'\033[1;33m------\033[m \033[4;31mVERIFICADOR DE MAIORIDADE\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')
cont = 0
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 5):
    cont = cont + 1
    while True:
        try:
            nascimento = int(input(f'Digite o ano de nascimento da {cont}ª pessoa: '))
            if nascimento <= anoatual:
                break
            print(f'A data digitada deve ser menor ou igual a data atual que é {anoatual}!')
        except ValueError:
            print('Não foi digitado nenhuma data, por favor tente novamente!')
    if (anoatual - nascimento) >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('')
print(f'Na lista digitada temos {maior} maiore(s) de idade e {menor} menore(s) de idade.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
