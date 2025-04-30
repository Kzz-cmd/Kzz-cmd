sex = ''
while sex not in ['M','F']:
    sex = str(input('Qual seu sexo? \n')).strip().upper()[0]
    if sex not in ['M','F']:
        print('Errado seu otaro, digite denovo')
if sex == 'M':
    sex = 'masculino'
else:
    sex = 'feminino'
print('Você é do sexo {}'.format(sex))
