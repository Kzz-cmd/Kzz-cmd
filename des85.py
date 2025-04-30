#Declarando as listas 

numeros = [[],[]]
par_impar = []

#Estrutura de loop 1

for c in range(0,7):
    
    #Entrada de dados do usuário
    
    par_impar.append(int(input('Digite o {}º número:\n'.format(c + 1))))

    #Inserção dos números pares em numeros[0] e ímpares em numeros[1]
    
    if par_impar[0] % 2 == 0:
        numeros[0].append(par_impar[0])
    else:
        numeros[1].append(par_impar[0])

    #Limpeza do par_impar

    par_impar.clear()

#Fim do looping

#Impressão dos resultados

print('Dos números digitados {} são pares'.format(sorted(numeros[0])))
print('Dos números digitados {} são ímpares'.format(sorted(numeros[1])))
