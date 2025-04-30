n1 = int(input('Qual é o primeiro termo da sua PA?:\n'))
raz = int(input('Qual é a razão da sua PA?:\n'))
c = 0
l = 1
while c < 10:
    print(n1)
    n1 += raz
    c += 1

c = 0

while l != 0:
    l = int(input('Mais quantos termos serão mostrados?\n'))
    while c < l:
        print(n1)
        n1 += raz
        c += 1
print('Até mais')
