from random import choice

a1 = input('Nome do primeiro aluno:\n')
a2 = input('Nome do segundo aluno:\n')
a3 = input('Nome do terceiro aluno:\n')
a4 = input('Nome do quarto aluno:\n')

alun = [a1,a2,a3,a4]

print('O aluno sorteado para limpar o quadro foi {}'.format(choice(alun)))
