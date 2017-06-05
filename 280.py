GRAPH = {0:[1, 4], 1:[0, 2, 4], 2:[1, 3, 4], 3:[2, 4], 4: [0, 1, 2, 3]}
VISITED = {0: 0, 1:0, 2:0, 3:0, 4:0}


def dfs(start):
    global GRAPH, VISITED
    #Inicializo el stack
    stack = [start]
    #Mientras me quedan cosas
    while stack:
        #Traigo el proximo elemento
        vertex = stack.pop()
        #Recorro sus vecinos
        for ngb in GRAPH[vertex]:
            #Si no fue visitado, lo agrego al stack
            if not VISITED[ngb]:
                stack.append(ngb)
        #Lo pongo como visitado
        VISITED[vertex] = 1
    return VISITED

if __name__ == "__main__":
    print(dfs(0))
