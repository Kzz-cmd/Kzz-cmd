#Criação da lista

lista = []

#Criação de loop

while True:
    
    #Garantia do funcionamento da estrutura de entrada e tratamento

    repetidor = ''

    #Entrada do usuário junto da inserção dos dados na lista

    lista.append(int(input('Digite um número:\n')))

    #Estrutura de entrada e tratamento

    while repetidor not in ['n','s']:

        repetidor = str(input('Deseja continuar(s/n)?\n'))

    #Estrutura condicional para fim de loop
        
    if repetidor == 'n':
        break

#Impressão dos resultados especificados no objetivo

print('Ao total foram digitados {} números'.format(len(lista)))

#Decrescendo números e imprimindo logo em seguida

lista.sort(reverse=True)

print('Com a sequência representada de maneira decrescente sendo {}'.format(lista))

#Checagem e impressão de se 5 está na lista

if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
            
