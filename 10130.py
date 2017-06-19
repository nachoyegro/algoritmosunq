
import sys
PRODUCTOS = []
PERSONAS = []
CACHE = []
INF = 10001

def read_line():
    line = next(sys.stdin).strip()
    if not line:
        return ""
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def crear_cache():
    #CACHE[num][restante]
    return [[-1 for i in range(31)] for y in range(len(PRODUCTOS))]

def backtracking(num, restante):
    if restante < 0:
        return -INF
    if num == len(PRODUCTOS):
        return 0
    if restante == 0:
        return 0
    if CACHE[num][restante] == -1:
        restante_nuevo = restante-weight(num)
        ponerlo = backtracking(num+1, restante_nuevo) + price(num)
        no_ponerlo = backtracking(num+1, restante)
        CACHE[num][restante] = max(ponerlo, no_ponerlo)
    return CACHE[num][restante]

def weight(n):
    #Devuelvo el segundo elemento del par
    return PRODUCTOS[n][1]

def price(n):
    #Devuelvo el primer elemento del par
    return PRODUCTOS[n][0]

if __name__ == "__main__":
    tests = int(read_line())
    for i in range(0, tests):
        productos = int(read_line())
        for i in range(0, productos):
            p, w = map(int, read_line().split(" "))
            PRODUCTOS.append((p, w))
        personas = int(read_line())
        for i in range(0, personas):
            persona = int(read_line())
            PERSONAS.append(persona)
        total = 0
        CACHE = crear_cache()
        for peso in PERSONAS:
            total += backtracking(0, peso)
        print(total)
        PERSONAS = []
        PRODUCTOS = []
