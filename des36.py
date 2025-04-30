casa = float(input('Qual é o  valor da casa?\n'))
sal  = float(input('Quanto você recebe de salário?\n'))
ano = int(input('Tudo isso em quantos anos?\n'))
prestação = casa / (ano * 12)
mini = sal * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f} reais\n'.format(casa,ano,prestação))
if prestação <= mini:
    print('O empréstimo concedido')
else:
    print('Empréstimo não concedido')
