import sys

BILLETES = []
USADOS = 0
PRECIO = 0
CACHE = {}
NOT_INIT = -1
INF = 10001

def read_line():
    line = next(sys.stdin).strip()
    if not line:
        return ""
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def crear_matriz(billetes):
    return [[NOT_INIT for x in range(billetes+2)] for y in range(INF+1)]

def backtracking(acumulado, n):
    global BILLETES, USADOS, PRECIO
    if acumulado >= PRECIO:
        #Como tengo que minimizar el vuelto dado, y la cantidad de BILLETES
        #Lo retorno como un par, de lo que sobra para el vendedor y la cantidad de billetes que use
        return (acumulado, USADOS)
    #Si ya use todos los billetes y no llegué, retorno cualquier cosa
    if n == len(BILLETES):
        #Retorno 10.001 porque el precio no puede superar 10.000, entonces funciona como INF
        return (INF,len(BILLETES) + 1)
    if CACHE[acumulado][n] == NOT_INIT:
        acumulado_usado = acumulado+BILLETES[n]
        USADOS += 1
        usarlo = backtracking(acumulado_usado, n+1)
        USADOS -= 1
        no_usarlo = backtracking(acumulado, n+1)
        CACHE[acumulado][n] = min(usarlo, no_usarlo)
    return CACHE[acumulado][n]

if __name__ == "__main__":
    tests = int(read_line())
    if tests == 0:
        print('N')
    for i in range(0, tests):
        PRECIO = int(read_line())
        billetes = int(read_line())
        for i in range(0, billetes):
            actual = int(read_line())
            BILLETES.append(actual)
        CACHE = crear_matriz(billetes)
        resultado = backtracking(0, 0)
        print(resultado[0], resultado[1])
        CACHE = {}
        BILLETES = []
