print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m------\033[m \033[4;31mCalculadoraa de IMC\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')

peso = float(input('Digite seu peso(kg):'))
altura = float(input('Digite sua altura(M):'))
imc = peso/(altura**2)
print('')
print(f'Seu imc é: {imc:.2f}')
if imc < 18.5:
    print('Você está ABAIXO do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO.')
elif 30.1 <= imc < 40:
    print('Você está OBESO.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
