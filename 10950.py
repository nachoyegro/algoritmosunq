import sys

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def backtracking(G, codigo_restante):
    for letra in codigo_restante:
        

if __name__ == "__main__":
    while True:
        G = {}
        cantidad = int(read_line())
        if cantidad == 0:
            break
        for i in range(0, cantidad):
            #Traigo sus nodos
            code, num = read_line().split(" ")
            #Los pongo en la matriz
            G[num] = code
        codigo = read_line()
        print(backtracking(G, codigo))
