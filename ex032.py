from datetime import date

print('Leitor de ano bissexto\n')
ano = int(input('Digite o ano desejado ou digite 0 para analisar o ano atual:\n'))
b1 = ano % 4
b2 = ano % 100
b3 = (ano % 100)
if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print(f'O ano {ano} é bissexto\n')
else:
    if b1 == 0 and b2 != 0:
        print(f'O ano {ano} é bisssexto\n')
    else:
        print(f'O ano {ano} não é bisssexto\n')
print('-----FIM_____')
