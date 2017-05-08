BOXES = [(19, 15), (7, 13), (5, 7), (6, 8), (1, 2)]
CANTIDAD = 0

def backtracking(n, acumulado):
    global CANTIDAD
    if n == 0:
        return cajas
    if acumulado > load(n):
        return -1
    else:
        return max(backtracking(n-1, acumulado+weight(n), cajas + 1), backtracking(n-1, acumulado, cajas))

def weight(n):
    #Devuelvo el primer elemento del par
    return BOXES[n][0]

def load(n):
    #Devuelvo el segundo elemento del par
    return BOXES[n][1]

if __name__ == "__main__":
    for box in BOXES:
    backtracking(len(BOXES))
