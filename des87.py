
#Declaração das listas e variáveis

matriz = []
par = 0
soma = 0
maior = 0

#Estrutura de loop da matriz

for i in range(0,3):
    for j in range(0,3):

        #Entrada do usuário e inserção dos dados na matriz
        
        num = int(input('Digite um número para o espaço[{},{}]'.format(i,j)))
        matriz.append(num)

        #Armazenamento da soma dos pares

        if num % 2 == 0:
            par = par + num

#Soma dos valores da terceira coluna e definição do maior na linha 2
            
soma = matriz[2] + matriz[5] + matriz[8]
for n in range(3,6):
    if matriz[n] > maior:
        maior = matriz[n]

#Impressão dos resultados

print('[{}] [{}] [{}]'.format(matriz[0],matriz[1],matriz[2]))
print('[{}] [{}] [{}]'.format(matriz[3],matriz[4],matriz[5]))
print('[{}] [{}] [{}]'.format(matriz[6],matriz[7],matriz[8]))
print('Com a soma dos valores pares sendo {}'.format(par))
print('A soma dos valores da terceira coluna sendo {}'.format(soma))
print('E com o maior valor da linha 2 sendo {}'.format(maior))
