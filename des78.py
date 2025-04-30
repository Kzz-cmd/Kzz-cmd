valores = []
pos = 0
pos2 = 0
for c in range(5):
    valores.append(int(input('Digite um número')))
for c, v in enumerate(valores):
    if v == max(valores):
        pos = c
    elif v == min(valores):
        pos2 = c
print('De todos os números {} foi o maior e {} o menor estando respectivamente na posição {} e {}'.format(max(valores),min(valores),pos,pos2))
