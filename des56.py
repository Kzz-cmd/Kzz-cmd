total = 0
velho = 0
maisvelho = ''
cont = 0
for c in range(1,5):
    print('---' * 25)
    nom = str(input('Qual é seu nome?\n'))
    idad = int(input('Qual é sua idade?\n'))
    sex = int(input('''Digite qual sexo você possui:
1 - Masculino
2 - Feminino\n'''))
    if sex == 1 and idad > velho:
        velho = idad
        maisvelho = nom
    if sex == 2 and idad < 20:
        cont = cont + 1
    total = total + idad
    print('---' * 25)

total = total / 4

print('''Dá pra se ter como média de todas as idades {},
com {} sendo mais velho que todos homens e com {} mulheres
tendo menos de 20 anos.'''.format(total, maisvelho, cont))
    
    
