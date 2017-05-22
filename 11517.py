import sys

BILLETES = []
USADOS = 0
PRECIO = 0
CACHE = {}

def read_line():
    line = next(sys.stdin).strip()
    if not line:
        return ""
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def backtracking(n, acumulado):
    global BILLETES, USADOS, PRECIO
    if acumulado >= PRECIO:
        #Como tengo que minimizar el vuelto dado, y la cantidad de BILLETES
        #Lo retorno como un par, de lo que sobra para el vendedor y la cantidad de billetes que use
        return (USADOS, acumulado)
    #Si ya use todos los billetes y no llegué, retorno cualquier cosa
    if n == len(BILLETES):
        #Retorno 10.001 porque el precio no puede superar 10.000, entonces funciona como INF
        return (len(BILLETES) + 1, 10001)
    #Si usando el billete actual me paso, entonces descarto
    if (n+1, acumulado+BILLETES[n]) in CACHE:
        usarlo = CACHE[(n+1, acumulado + BILLETES[n])]
    else:
        USADOS += 1
        usarlo = backtracking(n+1, acumulado+BILLETES[n])
        USADOS -= 1
        CACHE[(n+1, acumulado+BILLETES[n])] = usarlo
    if (n+1, acumulado) in CACHE:
        no_usarlo = CACHE[(n+1, acumulado)]
    else:
        no_usarlo = backtracking(n+1, acumulado)
        CACHE[(n+1, acumulado)] = no_usarlo
    return min(usarlo, no_usarlo)

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
        resultado = backtracking(0, 0)
        print(CACHE)
        print(resultado[0], resultado[1])
        CACHE = {}
        BILLETES = []
