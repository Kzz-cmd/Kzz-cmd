total = 0
cont = 0
for c in range(1 , 501 , 2):
    if c % 3 == 0:
        print(c)
        cont = cont + 1
        total = total + c
print('\n')
print('Com toda essa lista em mãos, a soma de todos os {} múltiplos de 3 é {}'.format(cont,total))
        
        
