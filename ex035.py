print('Programa que avalia se é possível formar um triângulo com tres retas digitadas.')
r1 = float(input('Digite o tamanho da primeira reta:\n'))
r2 = float(input('Digite o tamanho da segunda reta:\n'))
r3 = float(input('Digite o tamanho da terceira reta:\n'))
lista = [r1, r2, r3]
ordenado = sorted(lista)
menor = (ordenado[0])
medio = (ordenado[1])
maior = (ordenado[2])
if (menor + medio) > maior:
    print('Um triângulo pode ser formado com as três retas digitadas!\n')
else:
    print('Um triângulo NÃO pode ser formado com as três retas digitadas!\n')
print('-----FIM-----')

