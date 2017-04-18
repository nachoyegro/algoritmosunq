import sys

CAMINO = []
MAX = 1
ULTIMO = 1
ULTIMA_FILA = 0
ULTIMA_COLUMNA = 0
RESULTADOS = []
MAZES = []

def read_line():
    line = next(sys.stdin).strip()
    if not line:
        return ""
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def posibles_movimientos(ultimo, x, y, visitados):
    global ULTIMA_FILA, ULTIMA_COLUMNA
    posibles = []
    #Hago esto porque sino, estando en el final, me da como posible movimiento el de al lado
    if x == ULTIMA_FILA:
        return posibles
    if x+1 <= ULTIMA_FILA and G[x+1][y] == ultimo and not (x+1, y) in visitados:
        posibles.append((x+1, y))
    if x-1 >= 1 and G[x-1][y] == ultimo and not (x-1, y) in visitados:
        posibles.append((x-1, y))
    if y+1 <= ULTIMA_COLUMNA and G[x][y+1] == ultimo and not (x, y+1) in visitados:
        posibles.append((x, y+1))
    if y-1 >= 1 and G[x][y-1] == ultimo and not (x, y-1) in visitados:
        posibles.append((x, y-1))
    return posibles


def backtracking(ultimo, x, y, max, visitados=[]):
    global RESULTADOS
    if x == ULTIMA_FILA and (INICIO[0], INICIO[1], x, y) not in RESULTADOS:
        RESULTADOS.append((INICIO[0], INICIO[1], x, y))
        return
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
        backtracking(ultimo, i, j, max, visitados)
        visitados.remove((i, j))

if __name__ == "__main__":
    cases = int(read_line())
    for i in range(0, cases):
        G = {}
        blank = read_line()#blank
        filas, columnas = map(int, read_line().split(" "))
        RESULTADOS = []
        ULTIMA_FILA = filas
        ULTIMA_COLUMNA = columnas
        for i in range(1, filas+1):
            fila = read_line().split(" ")
            G[i] = {}
            for j in range(1, columnas+1):
                G[i][j] = int(fila[j-1])
        for i in G[1]:
            if G[1][i] == 1:
                INICIO = (1, i)
                backtracking(1, 1, i, 1) #ultimo, x, y, maximo
        minimo = ()
        for ix, iy, fx, fy in RESULTADOS:
            if not minimo:
                minimo = (ix, iy, fx, fy)
            else:
                #Si lexicograficamente el inicio actual esta mas a la izquierda que el minimo
                # o lexicograficamente el inicio es igual, pero el final esta mas a la izquierda
                if iy < minimo[1] or (iy == minimo[1] and fy < minimo[3]) and G[fx][fy] >= G[minimo[2]][minimo[3]]:
                    #Queda como minimo actual
                    minimo = (ix, iy, fx, fy)
        MAZES.append(minimo)
    #Si no hago esto, me da presentation error
    for maze in MAZES[:-1]:
        print(maze[0], maze[1])
        print(maze[2], maze[3])
        print("")
    print(MAZES[-1][0], MAZES[-1][1])
    print(MAZES[-1][2], MAZES[-1][3])
