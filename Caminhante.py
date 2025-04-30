import numpy as np
import random as rd

# Inicializa a matriz 5x5 com zeros
matriz = np.zeros((5, 5), dtype=int)

# Define a posição inicial do caminhante
x, y = rd.randint(0, 4), rd.randint(0, 4)
print(f'Posição inicial: ({x}, {y})')
matriz[x][y] = 1

# Enquanto o caminhante não atingir a posição (4, 4)
while matriz[2][2] == 0:
    while True:
        print(matriz)
        aleatorio = rd.choice([-1, 1])
        direcao = rd.choice(['x', 'y'])
        
        if direcao == 'x':
            novo_x = x + aleatorio
            novo_y = y
        else:
            novo_x = x
            novo_y = y + aleatorio
        
        # Verifica se a nova posição está dentro dos limites da matriz e se não está ocupada
        if 0 <= novo_x < 5 and 0 <= novo_y < 5 and matriz[novo_x][novo_y] == 0:
            break
    x, y = novo_x, novo_y
    matriz[x][y] = 1
print(f'Soma dos elementos da matriz: {np.sum(matriz)}')
print(matriz)