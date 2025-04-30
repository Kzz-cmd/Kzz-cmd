'''n = ''
while n.isnumeric() == False:
    n = str(input('Digite um número e eu mostrarei seu fatorial:\n'))
n = int(n)
for c in range(1,n):
    n = n * c
print('O fatorial do número digitado acima é {}'.format(n))'''

c = 0
n = ''
while n.isnumeric() == False:
    n = str(input('Digite um número e eu mostrarei seu fatorial:\n'))
n = int(n)
d = n
while c < d - 1:
    c += 1
    n = n * c
print(n)
    
