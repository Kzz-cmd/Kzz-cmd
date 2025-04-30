#Definição da função de input

def leiaInt(escrito):
    
    #Declaração da variável de armazenamento da entrada do usuário 
    
    entrada = ''

    #Tratamento de entrada de usuário

    while not entrada.isnumeric():
        entrada = input(escrito)

        #Estrutura condicional avisando o erro

        if entrada.isnumeric() == False:
            print('Argumento Inválido')
    
    #Retorno da função

    return entrada

#Chamada da função

n = leiaInt('Digite um número:\n')
print('Você acabou de digitar o número {}'.format(n))