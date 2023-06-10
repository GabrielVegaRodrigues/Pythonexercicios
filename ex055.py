print('\033[1;33m-=-\033[m'*12)
print(f'\033[1;33m------\033[m \033[4;31mVERIFICADOR DE PESO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*12, '\n')
cont = 0
contmaio = 0
contmeno = 0
pesomaior = 0
pesomenor = 0
for pess in range(1, 6):
    cont = cont + 1
    peso = float(input(f'Digite o peso da {cont}ª pessoa:'))
    if peso < pesomenor or pesomenor == 0:
        contmeno = cont
        pesomenor = peso
    if peso > pesomaior:
        contmaio = cont
        pesomaior = peso
print(f'O maior peso digitado foi da {contmaio}ª pessoa e foi {pesomaior:.1f}KG')
print(f'e o menor peso digitado foi da {contmeno}ª pessoa e foi {pesomenor:.1f}KG')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')