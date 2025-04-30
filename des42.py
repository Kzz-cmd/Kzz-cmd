#Função de entrada de dados do usuário
def pergunta(letra):
    letra = input(f'Digite o comprimento {letra} do triângulo:\n')
    return letra

#Chamada da função de pergunta
a = float(pergunta('A'))
b = float(pergunta('B'))
c = float(pergunta('C'))

#Declaração da variável de armazenamento do tipo de triângulo
tip = ''

#Estrutura condicional de checagem se o triângulo atende os requisitos de um triângulo
if b + c >= a and c + a >= b and b + a >= c:

    #Estrutura de definição do tipo de triângulo
    if a == b == c:
        tip = 'equilátero'
    elif a != b != c:
        tip = 'escaleno'
    else:
        tip = 'isósceles'
    print('Isso é um triângulo do tipo {}'.format(tip))
else:
    print('Isso não é um triângulo')

