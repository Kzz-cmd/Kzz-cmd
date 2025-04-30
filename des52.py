n = int(input('Digite um número e eu vou avaliar se ele é primo:\n'))

if n == 2 or n == 3 or n == 5 or n == 7:
    print('O número {} é primo'.format(n))    
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n < 2:
    print('O número {} não é primo'.format(n))
else:
    print('O número {} é primo'.format(n))
