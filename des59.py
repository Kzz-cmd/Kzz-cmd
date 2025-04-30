n1 = 'a'
n2 = 'b'
op = ''
while n1.isnumeric() == False:
    n1 = input('Digite o primeiro número:\n')
while n2.isnumeric() == False:
    n2 = input('Digite o segundo número:\n')
n1 = int(n1)
n2 = int(n2)
while op not in ['5']:
    print('-=-' * 25)
    op = str(input('''
Oque você deseja fazer com esses números?
[1]Somar
[2]Multiplicar
[3]Qual é o maior?
[4]Novos números
[5]Sair

'''))
    print('-=-' * 25)
    if op == '1':
        print('A soma dos dois números digitados é {}\n'.format(n1 + n2))
    if op == '2':
        print('A multiplicação dos dois números digitados é {}\n'.format(n1 * n2))
    if op == '3':
        if n1 > n2:
            print('O primeiro número ( {} ) é maior que o segundo\n'.format(n1))
        elif n2 > n1:
            print('O segundo número ( {} ) é maior que o primeiro\n'.format(n2))
        else:
            print('Os números são iguais\n')
    if op == '4':
        n1 = 'a'
        n2 = 'b'
        while n1.isnumeric() == False:
            n1 = input('Digite o primeiro número:\n')
        while n2.isnumeric() == False:
            n2 = input('Digite o segundo número:\n')
        n1 = int(n1)
        n2 = int(n2)

print('Fim do programa')
