import sys

ENCONTRADO = False
CAMINO = []
RESULTADO = []

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
    #Si el total de nodos es igual a la longitud del camino SIN EL ULTIMO NODO
    #y el ultimo nodo es el mismo que el primero, entonces es un ciclo hamiltoniano
    return TOTAL_NODOS == len(CAMINO) and ultimo_nodo == NODO_INICIAL

def backtracking(grafo, nodo_actual):
    global CAMINO
    #En base al nodo actual, me traigo todos los visitables
    visitables = grafo[nodo_actual] 
    #Seteo el nodo actual que estoy visitando
    for nodo in visitables:   
        if esHamiltoniano(nodo): 
            return ' '.join([str(v) for v in CAMINO] + [str(NODO_INICIAL)])
        if nodo not in CAMINO:
            #Si el nodo no esta en el camino
            #Agrego la visita actual a la lista de visitados
            CAMINO.append(nodo)
            #Hago backtracking sobre los nodos restantes
            res = backtracking(grafo, nodo)
            #Saco el nodo del camino
            CAMINO.remove(nodo)
            #Si el resultado de hacer backtracking no es N, entonces es un ciclo y lo retorno
            if res != 'N':
                return res
    return 'N'

if __name__ == "__main__":
    while True:
        G = {}
        CAMINO = []
        RESULTADO = []
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
                    a, b = map(int, arista.split(" "))
                    if a in G:
                        G[a].append(b)
                    else:
                        G[a] = [b]
                    if b in G:
                        G[b].append(a)
                    else:
                        G[b] = [a]
                    #Los agrego a la lista de nodos
                    vertices.append(a)
                    vertices.append(b)
                arista = read_line()
            #Si hay al menos un nodo
            if vertices:
                #Entonces puedo hacer backtracking
                #Selecciono el primero de la lista como nodo inicial
                NODO_INICIAL = vertices[0]
                #Genero el camino arrancando por ese nodo
                CAMINO = [NODO_INICIAL]
                #Hago backtracking con el grafo y el nodo inicial
                res = backtracking(G, NODO_INICIAL)
                #Hago print de la solucion
                print(res)
            else:
                #En el caso de no haber nodos, hago print de N
                print('N')
        else:
            break
