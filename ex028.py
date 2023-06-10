import random
from time import sleep
print('Jogo da adivinhação:')
n = [0, 1, 2, 3, 4, 5]
esc = random.choice(n)
print('Este computador irá pensar em um número de 0 a 5, você consegue adivinhar qual será?\n')
nusu = int(input('Digite o número que você acha que o computador pensou:\n'))
print('PROCESSANDO...')
sleep(3)
print('')
if nusu == esc:
    print(f'Você acertou!!! Parabéns o número escolhido pelo computador foi: {esc} e você escolheu: {nusu}')
else:
    print(f'Infelizmente você errou. O computador pensou em: {esc} e você escolheu: {nusu}')
print('')
print('--------FIM--------')