n = ''
print('---' * 25)
while n.isnumeric() == False:
    n = str(input('Digite um número para ver sua tabuada:\n'))
n = int(n)
for c in range(1,11):
    print('{} X {} = {}'.format( n, c, n * c))
print('---' * 25)
