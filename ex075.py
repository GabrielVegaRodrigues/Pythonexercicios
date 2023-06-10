num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o próximo número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Os números digitados foram {num}')
print(f'O número 9 apareceu {num.count(9)} vez(es) na lista digitada.')
if 3 in num:
       print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
       print(f'O valor 3 nao aparece em nenuma das posições digitadas.')
print(f'Os números pares digitados foram:', end=' ')
for c in num:
       if c % 2 == 0:
              print(c, end=', ')
