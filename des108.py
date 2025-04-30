from afins import moeda
quantia = float(input('Digite sua quantia de dinheiro:\n'))
print(f'O dobro de {moeda.moeda(quantia)} é {moeda.moeda(moeda.dobrar(quantia))}')
print(f'A metade de {moeda.moeda(quantia)} é {moeda.moeda(moeda.partir(quantia))}')
print(f'Aumentando em 10% se tem {moeda.moeda(moeda.aumentar(quantia,10))}')
print(f'Reduzindo em 13% se tem {moeda.moeda(moeda.diminuir(quantia,13))}')