from unidecode import unidecode
lista = ('Gabriel', 'Valentin', 'Francieli', 'Marisa', 'Cezar')
for pos in lista:
    print(f'\n{pos} tem as seguintes vogais: ', end='')
    for letra in pos:
        if (unidecode(letra.lower())) in 'aeiou':
            print(f'{letra}', end=' ')
