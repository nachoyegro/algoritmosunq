import sys

ENCONTRADO = False
CAMINO = []
MAX = 1
ULTIMO = 1
ULTIMA_FILA = 0
ULTIMA_COLUMNA = 0
G = { 0:{0:2, 1:3, 2:1, 3:4},
      1:{0:3, 1:2, 2:1, 3:3},
      2:{0:2, 1:1, 2:2, 3:4},
      3:{0:3, 1:1, 2:2, 3:4},
      4:{0:1, 1:2, 2:3, 3:4},}

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def posibles_movimientos(ultimo, x, y, visitados):
    global ULTIMA_FILA, ULTIMA_COLUMNA
    posibles = []
    if x+1 <= ULTIMA_FILA and G[x+1][y] == ultimo and not (x+1, y) in visitados:
        posibles.append((x+1, y))
    if x-1 >= 0 and G[x-1][y] == ultimo and not (x-1, y) in visitados:
        posibles.append((x-1, y))
    if y+1 <= ULTIMA_COLUMNA and G[x][y+1] == ultimo and not (x, y+1) in visitados:
        posibles.append((x, y+1))
    if y-1 >= 0 and G[x][y-1] == ultimo and not (x, y-1) in visitados:
        posibles.append((x, y-1))
    return posibles


def backtracking(ultimo, x, y, max, visitados=[]):
    if y == ULTIMA_FILA:
        print((x, y))
    """
        * Aca determino si tengo que arrancar el contador de nuevo
           o si sigo aumentandolo
    """
    #Si el ultimo numero por el que pase es igual al maximo
    if ultimo == max:
        #Incremento el maximo
        max += 1
        #Vuelvo el contador a 1
        ultimo = 1
    else:
        #Sino, significa que todavia no llegue al maximo, entonces sigo incrementando
        ultimo += 1
    for i, j in posibles_movimientos(ultimo, x, y, visitados):
        visitados.append((i, j))
        backtracking(ultimo, i, j, max)
        visitados.remove((i, j))
    return

if __name__ == "__main__":
    ULTIMA_FILA = 4
    ULTIMA_COLUMNA = 3
    for i in G[0]:
        if G[0][i] == 1:
            backtracking(1, 0, i, 1)
