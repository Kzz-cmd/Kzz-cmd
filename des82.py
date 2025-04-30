#Criação das listas
lista_normal = []
lista_par = []
lista_impar = []

#Estrutura de loop
while True:
    #Garantia de funcionamento controlado de loop

    repetidor = ''

    #Estrutura de entrada de dados do usuário junto de sua inserção na lista

    num = int(input('Digite um número:\n'))
    lista_normal.append(num)

    #Estrutura condicional para inserir os números pares na lista par e os números ímpares na lista ímpar
    
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

    #Estrutura condicional de fim de loop
    
    while repetidor not in ['s','n']:
        repetidor = str(input('Deseja continuar?(s/n)\n'))
    if repetidor == 'n':
        break

#Impressão dos resultados
    
print('Você digitou os números {}'.format(lista_normal))
print('Dos números que você digitou {} são pares'.format(lista_par))
print('Dos números que você digitou {} são ímpares'.format(lista_impar))


    
