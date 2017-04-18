import sys

ENCONTRADO = False
CAMINO = []

def read_line():
    try:
        line = next(sys.stdin).strip()
    except:
        return ''
    while(len(line) == 0):
        line = next(sys.stdin).strip()
    return line

def esHamiltoniano(ultimo_nodo):
    global CAMINO
    return TOTAL_NODOS == len(CAMINO) and ultimo_nodo == NODO_INICIAL

def backtracking(grafo, visitables, nodo_actual):
    global ENCONTRADO, CAMINO
    if visitables == []:
        return
    if ENCONTRADO:
        return
    #Seteo el nodo actual que estoy visitando
    for nodo in visitables:
        if nodo not in CAMINO:
            #Si el nodo no esta en el camino
            #Agrego la visita actual a la lista de visitados
            CAMINO.append(nodo)
            #Hago backtracking sobre los nodos restantes
            backtracking(grafo, grafo[nodo], nodo)
            #O(1)
            if esHamiltoniano(nodo):
                ENCONTRADO = True
                print(' '.join([str(NODO_INICIAL)] + [str(v) for v in CAMINO]))
                return
            #Vuelvo a construir las listas
            CAMINO.remove(nodo)

if __name__ == "__main__":
    while True:
        G = {}
        CAMINO = []
        ENCONTRADO = False
        #Genero los vertices
        vertices = []
        #Me traigo la primer linea, que es la cantidad de nodos
        nodos = read_line()
        arista = ''
        if nodos:
            TOTAL_NODOS = int(nodos)
            while arista != '%':
                #Traigo sus nodos
                if arista:
                    #Los pongo en la matriz
                    a, b = arista.split(" ")
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
                arista = read_line()
            if vertices:
                NODO_INICIAL = vertices[0]
                for nodo in vertices:
                    if ENCONTRADO:
                        break
                    backtracking(G, G[nodo], nodo)
            if not ENCONTRADO:
                print('N')
        else:
            break
