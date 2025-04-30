n = []
while True:
    r = int(input('Digite um número:\n'))
    if r in n:
        print('Esse número já existe')
    else:
        n.append(r)
    r = ''
    while r not in ['S','N']:
        r = str(input('Deseja continuar?(S/N)').replace('n','N').replace('s','S'))
    if r == 'N':
        break
print('Você digitou os valores {}'.format(sorted(n)))
