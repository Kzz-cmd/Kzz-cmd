#Entrada do nome do usuário

nome = input('Nome do Jogador:\n')

#Entrada dos gols do usuário

gols = input('Número de Gols:\n')

#Declaração da função de ficha

def ficha(nome,gols):

    #Checagem de espaços vazio

    if nome == '':
        nome = 'spacewar'
    
    #Checagem de espaço vazio

    if gols == '':
        gols = '0'

    #Impressão dos resultados
    
    print('O jogador {} fez {} gols'.format(nome,gols))

#Chamada da função

ficha(nome,gols)