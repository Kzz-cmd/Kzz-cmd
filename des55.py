alta = 0
baixa = 9999999999999999999999999999999999999999999999999999999999999999999999999999
pa = 0
pb = 0

for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa:\n'.format(c)))
    if peso > alta:
        alta = peso
        pa = c
    if peso < baixa:
        baixa = peso
        pb = c
if alta == baixa:
    print('Todos os valores são iguais, se todos são iguais não existe maior ou menor.')
else:
    print('''De todos os pesos lidos, o maior foi da {}ª pessoa com
{} kilos e o menor foi da {}ª pessoa com {} kilos.'''.format( pa, alta, pb, baixa))

