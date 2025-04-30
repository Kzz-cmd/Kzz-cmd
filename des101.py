#Importação da do ano atual

from datetime import date

#Declaração da data de nascimento do usuário

data = -1

#Declaração da função de escolhas

def voto(n):

    #Estrutura condicional de definição de escolhas

    if date.today().year - n < 18:
        return 'não vota'
    elif date.today().year - n >= 18 and date.today().year - n < 65:
        return 'é obrigado a votar'
    elif date.today().year - n >= 65:
        return 'tem seu voto sendo opcional'

#Estrutura de tratamento de data de nascimento

while data < 0:
    data = int(input('Em que ano você nasceu?\n'))

#Impressão dos resultados

print('Com {} anos você {}'.format(date.today().year - data,voto(data)))