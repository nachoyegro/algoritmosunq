import sys

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def backtracking(grafo, nodos, nodo_actual=0, distancia_actual=0, mayor_distancia=0):

    if distancia_actual > mayor_distancia:
        mayor_distancia = distancia_actual
    if distancia_actual + (25-nodo_actual) <= mayor_distancia:
        return mayor_distancia
    if distancia_actual == 25:
        return mayor_distancia
    #Seteo el nodo actual que estoy visitando
    #No tengo en cuenta el elemento actual
    mejor = 0
    for nodo in nodos:
        if G[nodo_actual][nodo]:
            mejor = backtracking(grafo, nodos, i+1, distancia_actual+1)
        else:
            mejor = backtracking(grafo, nodos, i+1, distancia_actual)
    return max(mejor, mayor_distancia)

def generar_matriz():
    #Sabemos que hay a lo sumo 25 elementos
    return [[0]*25 for i in range(0, 25)]

if __name__ == "__main__":
    while True:
        G = generar_matriz()
        #Genero los vertices
        vertices = []
        #Me traigo la primer linea, que es la cantidad de nodos y la cantidad de aristas
        nodos, aristas = map(int, read_line().split(" "))
        #Por cada arista...
        for i in range(0, aristas):
            #Traigo sus nodos
            a, b = map(int, read_line().split(" "))
            #Los pongo en la matriz
            G[a][b] = 1
            G[b][a] = 1
            vertices.append(a)
            vertices.append(b)
        best = backtracking(G, list(set(vertices)))
        print(best)
