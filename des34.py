sal = float(input('Qual o valor do seu salário?\n'))

if sal > 1250:
    print('Seu salário, com um aumento de 10% irá receber um aumento de {} reais,se tornando {} reais'.format(sal * 10/100,sal + sal * 10/100))

else:
    print('Seu salário, com um aumento de 15% irá receber um aumento de {} reais,se tornando {} reais'.format(sal * 15/100,sal + sal * 15/100))
