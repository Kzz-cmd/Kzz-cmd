palavras = ("cachorro", "gato", "elefante", "girafa", "tigre", "urso", "coelho","cavalo", "vaca", "ovelha", "macaco", "panda", "golfinho","águia", "coruja", "papagaio", "pinguim", "falcão")
for p in palavras:
    print('\nA palavra {} tem as vogais:'.format(p.upper()))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
