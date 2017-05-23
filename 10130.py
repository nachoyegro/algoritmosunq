import sys
PRODUCTOS = []
PERSONAS = []
CACHE = []

def read_line():
    line = next(sys.stdin).strip()
    if not line:
        return ""
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def crear_cache(billetes):
    return [[0 for i in range(31)] for y in range(len(PRODUCTOS))]

def backtracking(num, restante):
    if num == len(PRODUCTOS):
        #Si ya termine de recorrer los productos, termino.
        return 0
    if restante < 0:
        #Si ya me pase con el peso, recorto.
        return 0
    if CACHE[num][restante] == 0:
        restante_nuevo = restante-weight(num)
        if restante_nuevo >= 0:
            ponerlo = backtracking(num+1, restante_nuevo) + price(num)
        else:
            ponerlo = 0
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
        CACHE = crear_cache(PERSONAS)
        for peso in PERSONAS:
            total += backtracking(0, peso)
        print(total)
        print(CACHE)
        PERSONAS = []
        PRODUCTOS = []
