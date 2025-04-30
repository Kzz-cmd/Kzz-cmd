#Importação da data atual

from datetime import date

#Declaração do registro do cidadão

registro = {}

#Entrada do usuário

registro['nome'] = str(input('Nome:\n'))
registro['idade'] = int(input('Ano de Nascimento:\n'))

#Diminuindo o ano de nascimento com o ano atual gerando a idade

registro['idade'] = date.today().year - registro['idade']

#Entrada de definição de estrutura condicional

registro['CLT'] = int(input('Carteira de trabalho (0 não tem):\n'))

if registro['CLT'] != 0:

    #Entrada do usuário
    
    registro['contratação'] = int(input('Ano de contratação:\n'))
    registro['salário'] = float(input('Salário:\n'))
    registro['aposentadoria'] = registro['idade'] + 32
else:
    print('')

#Impressão dos resultados
    
print('-=-' * 10)
for requerimento,valor in registro.items():
    print('- {} tem o valor {}'.format(requerimento,valor))
