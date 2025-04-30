par = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º número:\n'.format(c)))
    if n % 2 == 0:
        par += n
        cont += 1 
print('A soma de todos os {} números pares é {}'.format(cont,par))
