gols = []
lista_jog = []
while True:
    jogador = {}
    r = ''
    jogador['nome'] = str(input('Nome do Jogador:\n'))
    quantia = int(input('Quantas partidas {} jogou?\n'.format(jogador['nome'])))
    for c in range(0,quantia):
        gols.append(int(input('Quantos gols na partida {}?\n'.format(c))))
        jogador['gols'] = gols
    jogador['total'] = sum(jogador['gols'])
    lista_jog.append(jogador)
    while r not in ['S','N']:
        r = str(input('Quer continuar?[S/N]\n').upper())
    if r == 'N':
        break
print('#-#' * 15)
print('cod nome gols total')
for num,item in enumerate(lista_jog):
    print('/ {} / {} / {} / {} /'.format(num,item['nome'],item['gols'],item['total']))
while True:
    r = int(input('Mostrar dados de qual jogador? (999 para parar)\n'))
    if r == 999:
        break
    elif r > -1 and r < len(lista_jog):
        print('-- LEVANTAMENTO DO JOGADOR {}:'.format(lista_jog[r]['nome']))
        for num,item in enumerate(lista_jog[r]['gols']): 
            print('No jogo {} fez {} gols.'.format(num,item))
    else:
        print('Não existe jogador com o código digitado')
print('Fim do programa')
    
