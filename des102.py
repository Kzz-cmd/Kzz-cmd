#Definição da função de fatorial

def fatorial(a,show=False):

    #Declarando acumulador

    acum = 1

    #Estrutura condicional para caso o segundo parâmetro seja False

    if not show:

        #Estrutura de repetição de multiplicação do c pelo acumulador

        for c in range(1,a + 1):
            acum = acum * c
        
        #Impressão do valor do acumulador

        print(acum)
    
    #Estrutura condicional para caso o segundo parâmetro seja True

    else:
        
        #Estrutura de repetição de multiplicação do c pelo acumulador e impressão

        for c in range(1,a + 1):
            acum = acum * c
            if c < a:
                print('{} X '.format(c),end='')
            else:
                print('{}'.format(c),end='')

        #Impressão do fatorial do primeiro parâmetro

        print(' =',acum,end='')

#Chamada da Função

fatorial(5)
fatorial(6,True)