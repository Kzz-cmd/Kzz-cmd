from random import randint
ppt = ['pedra','papel','tesoura']
sort = randint(0,2)
u = ''
while u not in ['0','1','2']:
    u = str(input('''Escolha entre:
[0] Pedra
[1] Papel
[2] Tesoura\n'''))

u = int(u)

print('Eu computador joguei {} e você jogou {}'.format(ppt[sort],ppt[u]))

if u == sort:
    print('O resultado foi um empate')
elif u == 0 and sort == 2:
    print('Você venceu pois pedra ganha de tesoura')
elif u == 1 and sort == 0:
    print('Você venceu pois papel ganha de pedra')
elif u == 2 and sort == 1:
    print('Você venceu pois tesoura ganha de papel')
else:
    print('Você perdeu pois {} ganha de {}'.format(ppt[sort],ppt[u]))
