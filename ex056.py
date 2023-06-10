print('\033[1;33m-=-\033[m'*11)
print(f'\033[1;33m------\033[m \033[4;31mANALISADOR DE DADOS\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
nomevelho = 0
novinhas = 0
idadevelho = 0
somaidade = 0
media = 0
for pess in range(1, 5):
    print(f'===== {pess}ª PESSOA =====')
    nome = input(f'Digite o nome: ').strip()
    idade = int(input(f'Digite a idade: '))
    sexo = input(f'Digite o sexo [M/F]: ').upper().strip()
    if sexo == 'M' and idadevelho < idade:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        novinhas = novinhas + 1
    if idade != 0:
        somaidade = somaidade + idade
        media = somaidade/4
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O nome do homem mais velho é o {nomevelho} e ele tem {idadevelho} anos.')
print(f'O grupo tem {novinhas} mulher(es) com menos de 20 anos de idade.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
