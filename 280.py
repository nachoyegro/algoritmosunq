import sys
GRAPH = []
VISITED = []

def read_line():
    return next(sys.stdin).strip()

def dfs(start):
    global GRAPH, VISITED
    stack = [start]
    #Mientras me quedan cosas
    while stack:
        #Traigo el proximo elemento
        vertex = stack.pop()
        #Recorro sus vecinos
        for ngb in GRAPH[vertex]:
            if not VISITED[ngb]:
                #Lo pongo como visitado
                VISITED[ngb] = 1
                #Lo pongo en el stack
                stack.append(ngb)

if __name__ == "__main__":
    result = ""
    nodes = read_line()
    #Si no es la ultima linea, sigo
    while nodes != '0':
        GRAPH = {}
        VISITED = {}
        nodes = int(nodes)
        #Genero la matriz
        GRAPH = [[] for _ in range(nodes+1)]
        edges = [int(x) for x in read_line().split()][:-1]
        while edges:
            #Genero las listas de adyacencias
            start_edge = edges[0]
            GRAPH[start_edge] += edges[1:]
            #Aristas sacando el ultimo 0
            edges = [int(x) for x in read_line().split()][:-1]
        test = [int(x) for x in read_line().split()]
        cant = test[0]
        #Arranco de 1 porque no quiero mirar el 0
        for i in range(1, len(test)):
            start = test[i]
            #Genero la lista de visitados en 0
            VISITED = [0] * (nodes + 1)
            #Hago DFS con el start actual
            dfs(start)
            #Traigo la lista de no visitados
            not_visited = [str(i) for i in range(1, len(VISITED)) if not VISITED[i]]
            cant = len(not_visited)
            if result:
                case = "\n"
            else:
                case = ""
            result = case.join([result, " ".join([str(cant)] + not_visited)])
        nodes = read_line()
    print(result)
