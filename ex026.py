from unidecode import unidecode
frase = input('Digite uma frase:\n').replace('A', 'a')
frase = unidecode(frase)
print('A frase digitada contém', frase.count('a'), 'A(s)!')
print('')
print(frase)
print('O primeiro A aparece na posição', frase.index('a'))
print('O último A aparece na posição', frase.rindex('a'))
