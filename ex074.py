from random import sample
lista = tuple(sample(range(99), 5))
print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
