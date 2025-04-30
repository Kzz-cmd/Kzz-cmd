#Declaração de listas

lista_principal = []
lista_tratamento = []

#Importando randomizador 

from random import randint

#Interface

print('--' * 10)
print('JOGA NA MEGA SENA')
print('--' * 10)

#Entrada do usuário fornecendo quantos jogos terão

jogos = int(input('Quantos jogos você quer que eu sorteie?\n'))

#Estrutura de loop e geração de números aleatória

for c in range(0,jogos):
    for r in range(0,6):
        num = randint(0,60)

        #Tratamento para evitar 2 números iguais

        if num not in lista_tratamento:
            lista_tratamento.append(num)

    #Tratamento de sequência crescente e inserção na lista principal
    
    lista_tratamento = sorted(lista_tratamento)
    lista_principal.append(lista_tratamento[:])
    lista_tratamento.clear()

#Impressão dos dados

for c in range(0,jogos):
    print('Jogo {}: {}'.format(c + 1,lista_principal[c]))
