from datetime import date
ano = int(input('Digite o seu ano de nascimento:\n'))

idade = date.today().year - ano

cat = str()

if idade <= 9:
    cat = 'MIRIM'
elif idade > 9 and idade <= 14:
    cat = 'INFANTIL'
elif idade > 14 and idade <= 19:
    cat = 'JUNIOR'
elif idade == 20:       
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'


print('Você tem a categoria {}'.format(cat))
    
