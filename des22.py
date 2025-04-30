nome = str(input('Qual seu nome?\n'))

nome = nome.upper()

print('Seu nome em LETRAS MAIÚSCULAS é {}'.format(nome))

nome = nome.lower()

print('Seu nome em letras minúsculas é {}'.format(nome))

print('Contendo {} palavras no total'.format(len(nome.replace(' ',''))))

nome = nome.split()

print('E sendo o primeiro nome',nome[0].capitalize(),'que contém {} letras'.format(len(nome[0])))
