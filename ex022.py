nome = input('Digite seu nome completo:\n')
dividido = nome.split()
print('')
print(f'Nome maíúsculo: {nome.upper()}')
print('')
print(f'Nome minúsculo: {nome.lower()}')
print('')
print(f'O nome tem {len(nome.strip())} caracteres')
print('')
print(f'O primeiro nome é {dividido[0]} e tem {len(dividido[0])} caracteres')