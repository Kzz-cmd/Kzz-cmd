#Declaração da função

def area():
    print('Controle de Terrenos')
    print('-' * 10)

    #Entrada dos dados que serão usados para calcular a area
    
    l = float(input('LARGURA(m): '))
    c = float(input('COMPRIMENTO(m): '))

    #Impressão dos resultados
    
    print('A área de um terreno {} X {} é de {} metros quadrados'.format(l,c,l*c))

#Chamada da função
    
area()
