print('Programa que informa o maior e o menor número.')
n1 = float(input('Digite o primeiro número inteiro e aperte enter:\n'))
n2 = float(input('Digite o segundo número inteiro e aperte enter:\n'))
n3 = float(input('Digite o terceiro número inteiro e aperte enter:\n'))
if n3 < n2 and n3 < n1:
    print(f'O menor numero é:{int(n3)}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O menor número é:{int(n2)}')
    else:
        print(f'O menor número é:{int(n1)}')
if n3 > n2 and n3 > n1:
    print(f'E o maior numero é:{int(n3)}')
else:
    if n2 > n1 and n2 > n3:
        print(f'E o maior número é:{int(n2)}')
    else:
        print(f'E o maior numero é:{int(n1)}')
print('')
print('-----FIM-----')
