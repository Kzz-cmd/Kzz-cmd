#Declaração da função de definição do maior

def maior(*valores):

    #Definição do maior
    
    maximo = max(valores)
    print('-=-' * 10)

    #Impressão dos resultados
    
    print('Analisando os valores passados...')
    print('{} Foram informados {} valores ao todo.'.format(valores,len(valores)))
    print('O maior valor informado foi {}'.format(maximo))

#Consecutivas chamadas da função
  
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
