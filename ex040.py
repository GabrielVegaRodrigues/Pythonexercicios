print('\033[1;33m-=-\033[m'*14)
print('\033[1;33m------\033[m \033[4;31mVerificador de média do aluno\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*14, '\n')

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2
if media < 5:
    print(f'Sua média foi \033[31m{media}\033[m, infelizmente você está \033[1;31mREPROVADO.\033[m')
    print('Você precisa estudar mais!!!')
elif 5 <= media < 7:
    print(f'Sua média foi \033[33m{media}\033[m, infelizmente você ficou em \033[1;33mRECUPERAÇÃO.\033[m')
    print('Se você estudar mais, vai conseguir!!!')
elif media >= 7:
    print(f'Sua média foi \033[32m{media}\033[m, você foi \033[1;32mAPROVADO.\033[m')
    print('Meus parabéns, nos vemos no próximo ano!!!')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
