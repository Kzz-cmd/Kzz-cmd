#Importação da biblioteca de aleatoriedade

from random import randint

#Criação da lista de armazenamento de 5 números que serão armazenados

lista = []

#Criação da função de sorteio de 5 números aleatórios

def sorteio(lista):

    #Sorteio e inserção dos números na lista

    for c in range(5):
        lista.append(randint(1,10))
    
    #Impressão da lista sorteada

    print('Sorteando 5 valores da lista: {}'.format(lista))

#Criação da função de soma dos números pares aleatórios da função passada 

def somaPar(lista):

    #Chamada do acumulador para realizar a soma de todos os pares

    c = 0
    
    #Estrutura de repetição, para cada item na lista

    for i in lista:
    
        #Estrutura condicional que acumula a soma do números pares
        if i % 2 == 0:
            c = c + i
    
    #Impressão dos resultados
    
    print('Somando os valores pares de {}, temos {}'.format(lista,c))

sorteio(lista)
somaPar(lista)
