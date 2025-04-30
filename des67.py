n = ''
while True:
    n = ''
    while n.isnumeric() == False:
        n = input('Digite um número e mostrarei sua tabuada:\n')
    n = int(n)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    print('-=-' * 15)
    for c in range(1,11):
        print('{} X {} = {}'.format(n,c,n * c))
    print('-=-' * 15)
