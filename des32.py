from datetime import date
print('Digite 0 para saber se o ano atual é bissexto')
ano = int(input('Digite um ano e eu vou verificar se esse ano é bissexto:\n'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))
    
    
