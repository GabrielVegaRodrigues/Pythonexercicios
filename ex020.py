from random import shuffle
print('Sorteio da ordem de apresentação dos alunos')

a1 = input('Digite o nome do aluno:\n')
a2 = input('Digite o nome do próximo aluno:\n')
a3 = input('Digite o nome do próximo aluno:\n')
a4 = input('Digite o nome do último aluno:\n')
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação dos trabalhos será :\n{alunos}')
