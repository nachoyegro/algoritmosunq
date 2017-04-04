import sys

def read_line():
    line = next(sys.stdin).strip()
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def backtracking(grafo, visitables, nodo_actual, visitados=[],distancia_actual=0, mayor_distancia=0):
    #Seteo el nodo actual que estoy visitando
    if distancia_actual >= mayor_distancia:
        mayor_distancia = distancia_actual
    if visitables == []:
        return mayor_distancia
    mejor = mayor_distancia
    for nodo in visitables:
        #Si la proxima arista no fue visitada
        if (nodo, nodo_actual) not in visitados and (nodo_actual, nodo) not in visitados:
            #Agrego la visita actual a la lista de visitados
            visitados.append((nodo_actual, nodo))
            #Saco el nodo anterior de la lista de proximos nodos
            grafo[nodo].remove(nodo_actual)
            #Hago backtracking sobre los nodos restantes
            mejor = max(backtracking(grafo, grafo[nodo], nodo, visitados, distancia_actual+1, mayor_distancia), mejor)
            #Vuelvo a construir las listas
            grafo[nodo].append(nodo_actual)
            visitados.remove((nodo_actual, nodo))
    return mejor

if __name__ == "__main__":
    while True:
        G = {}
        #Genero los vertices
        vertices = []
        #Me traigo la primer linea, que es la cantidad de nodos y la cantidad de aristas
        nodos, aristas = map(int, read_line().split(" "))
        if nodos == 0 and aristas == 0:
            break
        #Por cada arista...
        for i in range(0, aristas):
            #Traigo sus nodos
            a, b = map(int, read_line().split(" "))
            #Los pongo en la matriz
            if a in G:
                G[a].append(b)
            else:
                G[a] = [b]
            if b in G:
                G[b].append(a)
            else:
                G[b] = [a]
            vertices.append(a)
            vertices.append(b)
        vertices = list(set(vertices))
        mejor = 0
        for nodo in vertices:
            mejor = max(backtracking(G, G[nodo], nodo), mejor)
        print(mejor)
