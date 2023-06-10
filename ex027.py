nome = input('Digite seu nome completo:\n').strip()
nomesep = nome.split()
nome1 = nomesep[0]
nome2 = nomesep[-1]
print('')
print(f'Seu primeiro nome é: {nome1.capitalize()}')
print(f'Seu último nome é: {nome2.capitalize()}')
