#Variáveis para armazenamento do pesado e leve

pesado = leve = 0

#Criação da lista de inserção de dados e seu armazenamento

nome_peso = list()

lista = list()

#Estrutura de entrada de dados 

while True:
    nome_peso.append(str(input('Digite o seu nome:\n')))
    nome_peso.append(float(input('Digite seu peso:\n')))

    #Checagem do maior/menor e armazenamento de quem é maior e menor

    if len(lista) == 0:
        pesado = leve = nome_peso[1]
    else:
        if nome_peso[1] >= pesado:
            pesado = nome_peso[1]
        if nome_peso[1] <= leve:
            leve = nome_peso[1]

    #Armazenamento de dados

    lista.append(nome_peso[:])

    #Limpeza da estrutura de inserção de dados

    nome_peso.clear()

    #Estrutura condicional de fim de loop

    repetidor = ''
    
    while repetidor not in ['S','N']:
        repetidor = str(input('Deseja continuar?[S/N]\n').replace('s','S').replace('n','N'))
        
    if repetidor == 'N':
        break

#Impressão dos resultados

print('Ao total foram cadastradas {} pessoas'.format(len(lista)))
for c in lista:
    if c[1] == pesado:
        print('Com {} pesando {} kilos'.format(c[0],c[1]))
    if c[1] == leve:
        print('Com {} pesando {} kilos'.format(c[0],c[1]))

    
    

