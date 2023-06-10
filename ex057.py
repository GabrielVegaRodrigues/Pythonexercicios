print('\033[1;33m-=-\033[m' * 10)
print(f'\033[1;33m------\033[m \033[4;31mVALIDAÇÃO DE SEXO\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m' * 10, '\n')
sexo = input('Digite seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MmfF':
    print('Por favor tente novamente e escolha [M/F]! ')
    sexo = input('Digite seu sexo [M/F]: ').upper().strip()[0]
print('Sexo escolhido corretamente, obrigado!')
