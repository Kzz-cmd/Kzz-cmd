#Declaração da lista principal e lista de tratamento e acumulador

lista_principal = []
lista_tratamento = []
acumulador = -1

#Estrutura de looping

while True:

    #Entrada do usuário

    lista_tratamento.append(str(input('Nome:\n')))
    lista_tratamento.append(float(input('Nota 1:\n')))
    lista_tratamento.append(float(input('Nota 2:\n')))

    #Inserção dos dados na lista principal e limpeza


    lista_principal.append(lista_tratamento[:])
    lista_tratamento.clear()

    #Acumulador

    acumulador = acumulador + 1
    
    #Estrutura condicional de fim de looping

    repetidor = ''
    while repetidor not in ['S','N']:
        repetidor = str(input('Deseja continuar?[S/N]\n').replace('s','S').replace('n','N'))
    if repetidor == 'N':
        break

#Impressão dos resultados

print('--' * 15)
print('No.NOME          MÉDIA')
for i,l in enumerate(lista_principal):
    print('{:<2} : {:<5}       {:>1.1f}'.format(i,l[0],(l[1] + l[2])/2))
print('--' * 15)

#Estrutura de looping

while True:
    n = int(input('Mostrar notas de qual aluno? (999 para interromper)\n'))
    if n <= acumulador:
        print('O aluno {} teve as notas {} e {}'.format(lista_principal[n][0],lista_principal[n][1],lista_principal[n][2]))
    elif n == 999:
        break
    else:
        print('O aluno não existe')

    
