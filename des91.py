#Importando biblioteca de aleatoriedade

from random import randint

#Declarando dicionário

dicionario = {}

#Sequência de geração de jogadores e scores respectivos

for c in range(1,5):
    dicionario['Jogador {}'.format(c)] = randint(1,11)

#Impressão dos resultados iniciais

for k,v in dicionario.items():
    print(k,v)

#Organização dos resultados de maior para menor

dicio_organ = dict(sorted(dicionario.items(), key = lambda item: item[1],reverse=True))

#Reutilização do c para definir a posição dos jogadores

c = 1

#Impressão dos resultados organizados de menor para maior

for jogador,score in dicio_organ.items():
    print('Em {}º Lugar está o {} com {} pontos'.format(c,jogador,score))
    c = c + 1
