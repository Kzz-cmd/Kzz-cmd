n = []
r = int(input('Digite um valor:\n'))
n.append(r)
for c in range(4):
    r = int(input('Digite um valor:\n'))
    if r > n[c]:
        n.append(r)
    if r <= n[0]:
        n.insert(n[0],r)
    r = 0
print(n)
