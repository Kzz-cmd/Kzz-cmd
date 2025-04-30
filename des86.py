#Declaração das listas

x = []

for c in range(0,3):
    for i in range(0,3):
        x.append(int(input('Digite o valor para [{},{}]'.format(c,i))))
print('[{}] [{}] [{}]'.format(x[0],x[1],x[2]))
print('[{}] [{}] [{}]'.format(x[3],x[4],x[5]))
print('[{}] [{}] [{}]'.format(x[6],x[7],x[8]))
