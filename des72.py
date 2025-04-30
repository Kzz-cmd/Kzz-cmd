números = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desessete','desoito','desenove','vinte')
n = 30
while True:
    r = ''
    while True:
        n = int(input('Digite um número entre 0 e 20:\n'))
        if n >= 0 and n <= 20:
            break
        else:
            print('Tente novamente')
    print('Você digitou o número {}'.format(números[n]))
    while r not in ['s','n']:
        r = str(input('Deseja ver outro número?(S/N)\n'))
        if r == 'n':
            print()
        elif r == 's':
            print()
        else:
            print('Tente Novamente')
    if r == 'n':
            break
