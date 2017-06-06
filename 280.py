import sys
GRAPH = {}
VISITED = {}

def read_line():
    return next(sys.stdin).strip()

def dfs(start):
    global GRAPH, VISITED
    #Recorro sus vecinos
    for ngb in GRAPH[start]:
        #Si no fue visitado, lo agrego al stack
        if not VISITED[ngb]:
            #Lo pongo como visitado
            VISITED[ngb] = 1
            dfs(ngb)

if __name__ == "__main__":
    nodes = read_line()
    #Si no es la ultima linea, sigo
    while nodes != '0':
        GRAPH = {}
        VISITED = {}
        nodes = int(nodes)
        #Genero el grafo
        GRAPH = {i: [] for i in range(1, nodes+1)}
        edges = [int(x) for x in read_line().split()][:-1]
        while edges:
            #Genero las listas de adyacencias
            start_edge = edges[0]
            GRAPH[start_edge] = edges[1:]
            edges = [int(x) for x in read_line().split()][:-1]
        test = [int(x) for x in read_line().split()]
        cant = test[0]
        for start in test[1:]:
            VISITED = {i: 0 for i in range(1, nodes+1)}
            dfs(start)
            not_visited = [str(i) for i in VISITED.keys() if not VISITED[i]]
            cant = len(not_visited)
            print(" ".join([str(cant)] + not_visited))
        nodes = read_line()
