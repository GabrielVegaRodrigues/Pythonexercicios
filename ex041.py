from datetime import date

print('\033[1;33m-=-\033[m' * 12)
print('\033[1;33m------\033[m \033[4;31mCategoria dos atletas\033[m \033[1;33m-------\033[m')
print('\033[1;33m-=-\033[m' * 12, '\n')

anoatual = date.today().year
nasc = int(input('Digite o ano que o atleta nasceu:'))
idade = anoatual-nasc
if idade <= 9:
    print(f'Este atleta tem \033[1;34m{idade}\033[m anos, sua categoria é a: \033[1;34mMIRIM.\033[m')
elif idade <= 14:
    print(f'Este atleta tem \033[1;32m{idade}\033[m anos, sua categoria é a: \033[1;32mINFANTIL.\033[m')
elif idade <= 19:
    print(f'Este atleta tem \033[1;33m{idade}\033[m anos, sua categoria é a: \033[1;33mJUNIOR.\033[m')
elif idade <= 25:
    print(f'Este atleta tem \033[1;35m{idade}\033[m anos, sua categoria é a: \033[1;35mSÊNIOR.\033[m')
elif idade > 25:
    print(f'Este atleta tem \033[1;31m{idade}\033[m anos, sua categoria é a: \033[1;31mMASTER.\033[m')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
