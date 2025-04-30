#Declaração do dicionário e lista de gols

jogador = {}
gols = []

#Entrada do usuário

jogador['nome'] = str(input('Nome do Jogador:\n'))

#Definição de quantas vezes o loop vai se repetir

quantia = int(input('Quantas partidas {} jogou?\n'.format(jogador['nome'])))

#Estrutura de repetição perguntando e armazenando os os gols

for c in range(0,quantia):
    gols.append(int(input('Quantos gols na partida {}?\n'.format(c))))
    jogador['gols'] = gols

#Somando todos os itens dentro da lista dos gols e os armazenando

jogador['total'] = sum(jogador['gols'])

#Estilo de impressão n#1

print('¨%¨' * 10)
print(jogador)

#Estilo de impressão n#2

print('¨%¨' * 10)
for k,v in jogador.items():
    print('O campo {} tem o valor {}'.format(k,v))
print('¨%¨' * 10)
print('O jogador {} jogou {} partidas'.format(jogador['nome'],quantia))

#Estilo de impressão n#3

for c,v in enumerate(gols):
    print('=> Na partida {}, fez {} gols'.format(c,v))
print('Foi um total de {} gols'.format(jogador['total']))
    
