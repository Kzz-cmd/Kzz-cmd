n = 0
d = ''
t = 0
c = 1
a = -9999999999999999
b = 9999999999999999
while d not in ['não','n']:
    n = int(input('Digite o {}º número:\n'.format(c)))
    t += n
    c += 1
    if n > a:
        a = n
    if n < b:
        b = n
    d = str(input('Quer continuar?\n')).replace('a','ã').lower()

c = c - 1

print('A média de todos os {} valores digitados é {}'.format(c,t/c))
print('Com o maior valor digitado sendo {} e o menor {}'.format(a,b))
