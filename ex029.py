print('Calculador de velocidade e multa.\n')
v = float(input('Qual a velocidade do veículo?\n'))
multa = (v - 80)*7
if v > 80:
    print(f'Você ultrapassou a velocidade maxima permitida que é de 80KMh!!!')
    print(f'Terá que pagar uma multa no valor de R${multa:.2f}. Tome mais cuidado da próxima vez.')
else:
    print('Tenha um bom dia!')
