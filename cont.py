c = 0
for r in range(14):
    n = ''
    while n.isnumeric() == False:
        n = str(input('Contador\n'))
    n = int(n)
    c = c + n
    print(c)
    if n == 0:
        break
    print('++',r,'++')
print('---',c,'---')
