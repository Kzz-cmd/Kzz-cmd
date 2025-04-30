#Declaração de função de texto que mostra o inicio fim e pulos

def texto(inicio,fim,pulo):
    print('\nContagem de {} até {} de {} em {}\n'.format(inicio,fim,pulo,pulo))

#Declaração da função de contagem

def contagem(inicio,fim,pulos):
    texto(inicio,fim,pulos)

    #Estrutura condicional para casos em que o o inicio seja maior que o fim
    
    if inicio > fim:
        pulos = 0 - pulos
        fim = fim - 1
    else:
        fim = fim + 1
    
    #Impressão da contagem de números
    
    for c in range(inicio,fim,pulos):
        print(c)
#Chamada da função para testes

contagem(1,10,1)
contagem(10,0,2)

#Contagem personalizada

print('')
print('Agora é sua vez de personalizar a contagem!\n')

#Entrada do usuário de definição de parâmetros

inicio = int(input('Início:'))
fim = int(input('Fim:'))

#Tratamento dos pulos para evitar erros lógicos

pulos = str(input('Pulos:').replace('-','').replace('0','1'))
pulos = int(pulos)

#Chamada da função com os parâmetros definidos pelo usuário

contagem(inicio,fim,pulos)
