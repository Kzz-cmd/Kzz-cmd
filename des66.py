n = 'a'
c = 0
q = 0
while True:
    n = 'a'
    while n.isnumeric() == False:
        n = str(input('Digite um valor (999 para parar):\n'))
        if n.isnumeric() == False:
            print('Tem que ser um número')
    n = int(n)
    if n == 999:
        break
    q = q + 1
    c = c + n
print('Ao total foram digitados {} números e a soma de todos é {}'.format(q,c))
