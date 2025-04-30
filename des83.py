#Entrada do usuário

escrito = str(input('Digite uma expressão:\n'))

#Estrutura condicional que define se os parênteses foram fechados corretamente

if escrito.count('(') == escrito.count(')'):
    print('A expressão está correta')
else:
    print('A expressão está incorreta')
