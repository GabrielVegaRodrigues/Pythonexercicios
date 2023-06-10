print('\033[1;33m-=-\033[m'*15)
print(f'\033[1;33m------\033[m \033[4;31m1VERIFICADOR DE PALÍNDROMOS\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*15, '\n')
f = str(input('Digite uma frase que eu vou verificar se ela é ou não um PALÍNDROMO:\n'))
f = f.replace(' ', '').upper()
fi = (f[::-1]).upper()
print(f'O inverso de {f} é {fi}!')
if f == fi:
    print('A frase digitada é PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
