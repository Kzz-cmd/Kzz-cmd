from random import randint
poi = ''
s = 0
v = 0
print('<->' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('<->' * 15)
while True:
    poi = ''
    s = 0
    c = randint(1,11)
    n = int(input('Diga um valor:\n'))
    while poi not in ['P','I']:
        poi = input('Par ou Ímpar? [P/I]\n').replace('Í','I').replace('i','I').replace('p','P')
    s = n + c
    print('¨¨&¨¨' * 15)
    print('Eu joguei {} e você jogou {}, somando os dois valores o resultado é {}'.format(c,n,s))
    print('¨¨&¨¨' * 15)
    if s % 2 == 0 and poi == 'P':
        print('Você Venceu!!')
        print('Vamos jogar novamente...')
        v = v + 1
    elif s % 2 == 1 and poi == 'I':
        print('Você Venceu!!')
        print('Vamos jogar novamente...')
        v = v + 1
    else:
        break
print('Você perdeu mas você conseguiu ganhar {} vezes '.format(v))
        
