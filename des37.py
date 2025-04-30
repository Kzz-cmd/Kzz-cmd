val = int(input('Digite um valor inteiro:\n'))
print('Para qual base numérica será convertida?\n')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
op = int(input(''))
if op == 1:
    print('O número {} em binário é {}'.format(val, bin(val)[2:]))
elif op == 2:
    print('O número {} em octal é {}'.format(val, oct(val)[2:]))
elif op == 3:
    print('O número {} em binário é {}'.format(val, hex(val)[2:]))
else:
    print('Opção inválida')
