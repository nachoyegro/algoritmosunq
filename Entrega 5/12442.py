import sys
GRAPH = []
VISITED = []
RESULTS = []
MAX = (0, 0)

def read_line():
    return next(sys.stdin).strip()

def dfs(start):
    global GRAPH, VISITED, MAX
    stack = [start]
    r = 0
    #Mientras me quedan cosas
    while stack:
        #Traigo el proximo elemento
        vertex = stack.pop()
        #Recorro sus vecinos
        for ngb in GRAPH[vertex]:
            if not VISITED[ngb]:
                #Lo pongo como visitado
                VISITED[ngb] = 1
                r += 1
                #Lo pongo en el stack
                stack.append(ngb)
    #Si la cantidad de nodos es mayor a la almacenada, o si es igual pero de numero menor
    if r > MAX[1] or (r == MAX[1] and start < MAX[0]):
        MAX = (start, r)

if __name__ == "__main__":
    result = ""
    tests = int(read_line())
    #Si no es la ultima linea, sigo
    for i in range(tests):
        edges = int(read_line())
        nodes = []
        #Genero la matriz
        cant = edges
        GRAPH = GRAPH = [[] for _ in range(cant+1)]
        for _ in range(edges):
            x, y = map(int, read_line().split())
            nodes.append(x)
            GRAPH[x].append(y)
        for node in nodes:
            VISITED = [0] * (cant + 1)
            dfs(node)
        print("Case %d: %d" % (i+1, MAX[0]))
        MAX = (0, 0)
