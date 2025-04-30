tupla = (int(input('Digite um valor:\n')),
int(input('Digite outro valor:\n')),
int(input('Digite outro valor:\n')),
int(input('Digite outro valor:\n')))
print('Você digitou os valores {} '.format(tupla))
print('Com o número 9 se repetindo {} vezes'.format(tupla.count(9)))
if 3 not in tupla:
    print('O valor 3 nunca apareceu')
else:
    print('O valor 3 pareceu na {}ª posição'.format(tupla.index(3) + 1))
val3 = 0
for c in range(0,len(tupla)):
    if tupla[c] % 2 == 0:
        val3 = val3 + 1
if val3 != 0:
    print('Com {} números pares sendo eles:'.format(val3))
    for c in range(0,len(tupla)):
        if tupla[c] % 2 == 0:
            print(tupla[c])
else:
    print('Sem números pares')
