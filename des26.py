frase = str(input('Digite uma frase:\n'))

frase = frase.strip().upper().replace('Á' , 'A')

print('A frase escrita tem {} letras A´s'.format(frase.count('A')))

print('Com a primeira letra A estando na posição {}'.format(frase.find('A')))

print('Com a última letra A estando na posição {}'.format(frase.rfind('A')))
