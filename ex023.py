num = int(input('Digite um número de 0 a 9999:\n '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O número {num} tem:')
print('')
print(f'Unidade(s): {u}')
print(f'Dezena(s) : {d}')
print(f'Centen(s) : {c}')
print(f'Milhar(s) : {m}')
