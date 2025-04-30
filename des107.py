from afins import moeda
quantia = float(input('Digite sua quantia de dinheiro:\n'))
print(f'O dobro de {quantia} é {moeda.dobrar(quantia)}')
print(f'A metade de {quantia} é {moeda.partir(quantia)}')
print(f'Aumentando em 10% se tem {moeda.aumentar(quantia,10)}')
print(f'Reduzindo em 13% se tem {moeda.diminuir(quantia,13)}')