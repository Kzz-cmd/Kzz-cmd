from datetime import date

anat = date.today().year

ano = int(input('Qual a sua data de nascimento?\n'))

ano = anat - ano

if ano < 18:
    print('Você não pode se alistar pois você tem {} anos e faltam {} anos para você se alistar no exército'.format(ano,- (ano - 18)))
if ano == 18:
    print('É hora de se alistar para o exército pois você tem {} anos'.format(ano))
if ano > 18:
    print('Já passou do tempo de alistamento para o exército com um prazo de {} anos'.format(ano - 18))
    
