pag = 0
preco = ''
while preco.isnumeric() == False:
    preco = str(input('Preço da compra:\n'))
while pag not in ['1','2','3','4']:
    pag = str(input('''1 - Á vista dinheiro/cheque
2 - Á vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão\n'''))

pag = int(pag)
preco = float(preco)
if pag == 1:
    print('Pagando á vista com dinheiro você tem um desconto de 10%, tornando o preço digitado em {} reais'.format((preco * 90)/100))
elif pag == 2:
    print('Pagando á vista no cartão você tem um desconto de 5%, tornando o preço digitado em {} reais'.format((preco * 95)/100))
elif pag == 3:
    print('Pagando á 2x no cartão você não paga juros, no final, saindo por {} reais'.format(preco))
elif pag == 4:
    print('Pagando á 3x ou mais no cartão você recebe uma taxa de 20%, tornando o valor digitado em {}'.format((preco * 20)/100 + preco))
