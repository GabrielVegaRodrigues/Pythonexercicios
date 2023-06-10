print('\033[1;33m-=-\033[m'*13)
print('\033[1;33m------\033[m \033[4;31mCalculadora de pagamento\033[m \033[1;33m-----\033[m')
print('\033[1;33m-=-\033[m'*13, '\n')

preco = float(input('Digite o preço do produto:R$'))
print('Selecione a forma de pagamento abaixo:')
print('''(1) - Pagamento à vista em dinheiro/cheque: \033[33mVocê recebe \033[32m10%\033[m \033[33mde desconto!\033[m')
(2) - Pagamento à vista no cartão: \033[33mVocê recebe \033[32m5%\033[m \033[33mde desconto!\033[m')
(3) - Pagamento em até 2X no cartão: Você pagará o preço normal do produto.')
(4) - Pagamento em 3X ou mais no cartão: \033[33mVocê pagará\033[m \033[31m5% \033[33mde juros.\033[m')''')
forma = int(input('Selecione sua opção:'))
print('')
print(f'Preço do produto:R$ {preco:.2f}')
if forma == 1:
    print(f'Selecionado pagamento à vista em dinheiro/cheque: Você receberá 10% de desconto.')
    print(f'O valor final do produto ficou:\n\033[32mR$ {preco-(preco*10/100):.2f}\033[m')
elif forma == 2:
    print(f'Selecionado pagamento à vista no cartão:Você receberá 5% de desconto.')
    print(f'O valor final do produto ficou:\n\033[32mR$ {preco - (preco * 5 / 100):.2f}\033[m com desconto de 5%.')
elif forma == 3:
    print(f'Selecionado pagamento em até 2X no cartão:')
    total = preco
    parcela = total/2
    print(f'O valor final do produto ficou:\nR$ {preco:.2f}, cada parcela será de R$ {parcela:.2f} sem JUROS.')
elif forma == 4:
    print(f'Selecionado pagamento em 3X ou mais no cartão: Você terá um acrescimo de 20% de JUROS.')
    vezes = float(input('Em quantas vezes você deseja parcelar sua compra?'))
    total = preco+(preco*20/100)
    parcela = total / vezes
    print(f'O valor final do produto ficou:\n\033[31mR$ {total:.2f}\033[m, cada parcela será de R$ {parcela:.2f}.')
else:
    print('\033[4;31mOpção inválida, tente novamente!!!\033[m')
print('')
print('\033[1;33m-=-\033[m'*11)
print('\033[1;33m--------------\033[m \033[4;31mFIM\033[m \033[1;33m--------------\033[m')
print('\033[1;33m-=-\033[m'*11, '\n')
