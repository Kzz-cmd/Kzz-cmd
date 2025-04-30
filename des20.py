from random import shuffle

a1 = str(input('Nome do primeiro aluno:\n'))
a2 = str(input('Nome do segundo aluno:\n'))
a3 = str(input('Nome do terceiro aluno:\n'))
a4 = str(input('Nome do quarto aluno:\n'))

alun = [a1,a2,a3,a4]
shuffle(alun)

print('A lista de apresentação será:')
print (alun)
