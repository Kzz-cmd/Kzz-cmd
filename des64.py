c = 1
d = 0
n = 0
while d != 999:
    d = int(input('Digite o {}º número:\n'.format(c)))
    n = n + d
    c = c + 1
print('Ao total foram digitados {} números e a soma de todos eles é {}'.format(c - 2,n - 999))
    
