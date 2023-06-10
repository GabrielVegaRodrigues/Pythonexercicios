from time import sleep
from emoji import emojize
print('\033[1;33m-=-\033[m'*18)
print(f'\033[1;33m------\033[m \033[4;31mFOGOS DE ARTIFÍCIO(regressiva 10 segundos)\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*18, '\n')
print('CONTAGEM REGRESSIVA...\n')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('')
print(emojize(":collision:")*9)
sleep(1.2)
print(emojize("FELIZ ANO NOVO!!!:collision:"))
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
