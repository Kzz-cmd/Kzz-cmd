v = float(input('Quantos Km/h?\n'))
if v > 80:
    print('''Você passou do valor limite de velocidade
e por isso você recebeu uma multa de {} reais'''.format( v * 7 ))
else:
    print('Você está dentro da lei, agora vaza!!!')
