n1 = int(input('Qual é o primeiro termo da sua PA de 10 termos?\n'))
raz = int(input('Qual é a razão da sua PA?\n'))
for c in range(n1,n1 + 10):
    print('{}'.format(n1))
    n1 = n1 + raz
print('\nAcabou')
