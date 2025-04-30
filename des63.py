n1 = 1
n2 = 0
n = 0
f = 0
while 0 >= n: 
    n = int(input('Quantos termos sua sequência de Fibonacci vai ter?\n'))
c = 0
while c < n:
    f = n1 + n2
    print(f)
    n1 = n2
    n2 = f
    c += 1

    
