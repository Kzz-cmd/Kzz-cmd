km = float(input('Quantos kilômetros serão percorridos nessa viagem de ônibus?\n'))

if km >= 200:
    print('A viagem longa vai acabar custando um valor de {} reais'.format(km * 0.45))
else:
    print('A viagem curta vai ter um custo de {} reais'.format(km * 0.50))
