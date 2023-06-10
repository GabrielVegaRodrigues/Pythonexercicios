import math
a = float(input('Digite um angulo qualquer:\n'))
seno = math.sin(a)
cosseno = math.cos(a)
tangente = math.tan(a)
print(f'Referente ao angulo digitado o resultado em grade é:')
print(f'O seno é: {seno}\nO cosseno é: {cosseno}\nA tangente é:{tangente}\n')
print(f'Referente ao angulo digitado o resultado em radiano é:')
print(f'O seno é: {math.sin(math.radians(a)):.2f}\n'
      f'O cosseno é: {math.cos(math.radians(a)):.2f}\n'
      f'A tangente é:{math.tan(math.radians(a)):.2f}')

