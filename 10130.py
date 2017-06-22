
import sys
PRODUCTOS = []
PERSONAS = []
CACHE = []
INF = -10001

def read_line():
    return next(sys.stdin).strip()

def crear_cache():
    #CACHE[num][restante]
    return [[-1 for i in range(31)] for _ in range(len(PRODUCTOS)+1)]

def backtracking(num, restante):
    if restante < 0:
        #Si me paso, retorno INF
        return INF
    if num == len(PRODUCTOS):
        #Si llego al final, corto
        return 0
    #Si el par num, restante todavia no lo procese
    if CACHE[num][restante] == -1:
        #Resto el peso actual
        restante_nuevo = restante-weight(num)
        #Hago backtracking con el peso restado, y sumo el precio actual al resultado
        ponerlo = backtracking(num+1, restante_nuevo) + price(num)
        #Hago backtracking sin tener en cuenta el actual
        no_ponerlo = backtracking(num+1, restante)
        #Guardo el maximo de ambos en la cache
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
