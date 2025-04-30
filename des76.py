produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('###' * 7)
print('Listagem de preços')
print('###' * 7)
n = 1
r = 0
for c in range(0, len(produtos)):
    print('{}............R$ {}'.format(produtos[r],produtos[n]))
    n = n + 2
    r = r + 2
    if r > 18:
        break
    elif n > 18:
        break
print('###' * 7)
