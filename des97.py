#Declaração da função

def escreva(palavra):

    #Conforme o tamanho do que foi digitado irão existir bordas
    
    print('-' * len(palavra))
    print(palavra)
    print('-' * len(palavra))
    
#Entrada do usuário que irá servir de parâmetro para a função

pavalra = str(input('Digite algo:\n'))

#Chamada da função com o parâmetro

escreva(pavalra)
