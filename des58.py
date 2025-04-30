from time import sleep
from random import randint
print('Vou pensar em um número entre 0 e 10, Adivinhe qual é ele???')
num = 11
ran = randint(1,10)
cont = 0
sleep(3)
while ran != num:
    num = int(input('Qual é o número?\n'))
    print('Pensando...')
    if ran != num:
        print('Você errou')
        cont += 1
        if num > ran:
            print('O número é menor que isso')
        else:
            print('O número é maior que isso')
print('Você acertou!!!, de fato o número que eu pensei era {} mas você parece ter errado {} vezes'.format(ran,cont))
    
    
