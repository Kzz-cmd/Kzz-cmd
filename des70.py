print('--' * 15)
print('LOJA SUPER BARATÃO')
print('--' * 15)
caro = 0
barato = 1000000000000000000000000000000000000
produto = ''
while True:
    d = ''
    a = 0
    p = '2'
    n = ''
    while p.isnumeric() == True:
        p = input('Nome do produto:\n')
    while n.isnumeric() == False:
        n = input('Quanto esse produto custa?:\n')
    n = int(n)
    a = a + n
    if n > 1000:
        caro = caro + 1
    elif n < barato:
        produto = p 
    while d not in ['S','N']:
        d = input('Deseja continuar? [S/N]\n').replace('s','S').replace('n','N')
    if d == 'S':
        print(' ')
    else:
        break
print('A soma de todos os produtos é {} com {} sendo o mais barato deles e {} deles com custo acima de 1000 reais'.format(a,produto,caro))
    
        
