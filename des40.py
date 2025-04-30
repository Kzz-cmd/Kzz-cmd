n1 = float(input('Qual foi sua primeira nota?\n'))
n2 = float(input('Qual foi sua segunda nota?\n'))

m = (n1 + n2)/2

if m < 5.0:
    print('Você foi reprovado!!')
elif 5.0 <= m and m < 7.0:
    print('Você está de recuperação!!!')
elif m >= 7.0:
    print('Meus parabéns!!!Você foi aprovado!!')
