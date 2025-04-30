from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
alto = -1
baixo = 11
print('Gerando sequência aleatória:')
print(num)
print('De todos números sorteados {} é o mais alto e {} o mais baixo'.format(max(num),min(num)))
