import datetime

print('\033[1;33m-=-\033[m'*17)
print('\033[1;33m------\033[m \033[4;31mVerificador de idade para alistamento\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*17, '\n')


print('Você é do gênero Masculino ou Feminino?')
sexo = input('(M) - para Masculino\n(F) - para Feminino\n')
if sexo == 'm':
    ano = int(input('Digite o ano que você nasceu:'))
    anoatual = datetime.date.today().year
    idade = anoatual - ano
    print(f'Você nasceu em {ano} e tem {idade} anos de idade.')
    if idade > 18:
        print('Você ja deveria ter se alistado!')
        print(f'Seu ano de alistamento foi {anoatual - (idade - 18)}.')
    elif idade < 18:
        print(f'Ainda faltam {18 - idade} anos para você poder se alistar')
        print(f'Você só poderá se alistar em {(18-idade)+anoatual}')
    elif idade == 18:
        print(f'Você tem {idade} anos e precisa se alistar ainda este ano.')
else:
    print('')
    print('\033[31mPor ser do gênero Feminino você não precisa se alistar!\033[m')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
