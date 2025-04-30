n1 = int(input('Qual é o primeiro  número?\n'))
n2 = int(input('Qual é o segundo  número?\n'))
if n1 > n2:
    print('O primeiro valor({}) é maior que o segundo({})'.format(n1,n2))
elif n2 > n1:
    print('O segundo valor({}) é maior que o primeiro({})'.format(n2,n1))
else:
    print('Ambos valores são iguais, logo nenhum é maior que o outro'.format(n1,n2))
