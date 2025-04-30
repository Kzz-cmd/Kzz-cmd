alta = int(0)
baixa = int(99999999999999999999)

n1 = int(input('Digite o primeiro número:\n'))

alta = n1
baixa = n1

n2 = int(input('Digite o segundo número:\n'))

if alta > n2:
    alta = alta
else:
    alta = n2

if baixa < n2:
    baixa = baixa
else:
    baixa = n2

n3 = int(input('Digite o terceiro número:\n'))

if alta > n3:
    alta = alta
else:
    alta = n3

if baixa < n3:
    baixa = baixa
else:
    baixa = n3
print('O número mais alto dos 3 é {} e o mais baixo é {}'.format(alta,baixa))
