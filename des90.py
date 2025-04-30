#Declaração do dicionário de armazenamento de dados

dicionario = {}

#Entrada de dados do usuário

dicionario['nome'] = str(input('Nome:\n'))
dicionario['média'] = float(input('Média:\n'))

#Estrutura condicional de definição da situação

if dicionario['média'] < 7:
    dicionario['situação'] = 'reprovado'
else:
    dicionario['situação'] = 'aprovado'

#Impressão dos resultados

for k,v in dicionario.items():
    print('{} é de {}'.format(k,v))


