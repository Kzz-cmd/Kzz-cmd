#Declaração da lista onde vai ser armazenado todos os valores

lista = []

#Estrutura de repetição

while True:
    
    #Declaração do dicionário que irá servir para melhor separação de dados e limpeza da váriável de repetição
    
    registro = {}
    r = ''

    #Entrada do usuário
    
    registro['nome'] = str(input('Nome:\n'))
    registro['sexo'] = str(input('Sexo [M/F]:\n'))
    registro['idade'] = int(input('Idade:\n'))

    #Armazenamento de dados na lista
    
    lista.append(registro)

    #Estrutura condicional de fim de loop
    while r not in ['S','N']:
        r = str(input('Deseja continuar?\n').replace('s','S').replace('n','N'))
        if r not in ['S','N']:
            print('ERRO! Responda apenas S ou N')
    if r == 'N':
        break

#Declaração da média

media = 0
for c in range(0,len(lista)):
    media = media + lista[c]['idade']
media = media/len(lista)

#Impressão dos resultados

print('A) Ao todo temos {} pessoas cadastradas'.format(len(lista)))
print('B) A média de idade é de {:.2f} anos'.format(media))
print('C) As mulheres cadastradas foram')
for p in lista:
    if p['sexo'] in 'Ff':
        print(' {} '.format(p['nome']))
print('D) Lista das pessoas que tem idade acima da média')
for p in lista:
    if p['idade'] > media:
        print('{} = {}'.format(p['nome'],p['idade']))
