idade = sexo = r = ''
a = b = c = 0
while True:
    print('---' * 15)
    print('Cadastre UMA PESSOA')
    print('---' * 15)
    r = ''
    idade = ''
    sexo = ''
    while idade.isnumeric() == False:
        idade = input('Idade:\n')
    idade = int(idade)
    while sexo not in ['F','M']:
        sexo = input('Sexo: [M/F]\n').replace('f','F').replace('m','M')
    if idade > 18:
        a = a + 1
    elif sexo == 'M':
        b = b + 1
    elif sexo == 'F' and 20 > idade:
        c = c + 1
    while r not in ['S','N']:
        r = input('Denovo?: [S/N]\n').replace('s','S').replace('n','N')
    if r == 'S':
        pass
    else:
        break
print('De todos os valores digitados {} pessoas tem mais de 18 anos e {} são homens e {} mulheres com menos de 20 anos'.format(a,b,c))