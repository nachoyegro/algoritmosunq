import sys

BILLETES = []
USADOS = 0
PRECIO = 0
CACHE = {}
NOT_INIT = -1
INF = 1e7

def read_line():
    return next(sys.stdin).strip()

def crear_matriz(billetes):
    return [[NOT_INIT for _ in range(PRECIO+1)] for _ in range(billetes+1)]

def backtracking(acumulado, num):
    global BILLETES, USADOS, PRECIO, MIN
    if acumulado >= PRECIO:
        #Como tengo que minimizar el vuelto dado, y la cantidad de BILLETES
        #Lo retorno como un par, de lo que sobra para el vendedor y la cantidad de billetes que use
        return (acumulado, 0)
    #Si ya use todos los billetes y no llegué, retorno cualquier cosa
    if num == len(BILLETES):
        #Retorno 10.001 porque el precio no puede superar 10.000, entonces funciona como INF
        return (INF, INF)
    #TODO El problema aca es que en algun momento se guarda como mejor uno que no es tan bueno como el actual,
    # entonces ni lo considera
    if CACHE[num][acumulado] == NOT_INIT:
        acumulado_usado = acumulado+BILLETES[num]
        usarlo = backtracking(acumulado_usado, num+1)
        usarlo = (usarlo[0], usarlo[1] + 1)
        no_usarlo = backtracking(acumulado, num+1)
        CACHE[num][acumulado] = min(usarlo, no_usarlo)
    return CACHE[num][acumulado]

if __name__ == "__main__":
    tests = int(read_line())
    if tests == 0:
        print('N')
    for i in range(0, tests):
        PRECIO = int(read_line())
        billetes = int(read_line())
        for _ in range(0, billetes):
            actual = int(read_line())
            BILLETES.append(actual)
        #TODO: probar inicializar la cache una sola vez
        CACHE = crear_matriz(billetes)
        resultado = backtracking(0, 0)
        print(resultado[0], resultado[1])
        CACHE = {}
        BILLETES = []
