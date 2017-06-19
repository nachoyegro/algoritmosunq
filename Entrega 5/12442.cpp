#include<cstdio>
#include<vector>

using namespace std;

int T, N, a, b;
vector<int> graph, sum;
vector<bool> vis;

int dfs(int u) {
    //Seteo como visitado el actual
    vis[u] = true;
    //Inicializo el total
    int tot = 0;
    //Si el vecino no fue inicializado ni visitado
    if(graph[u] != -1 && !vis[graph[u]]){
        //Sumo el dfs de mi vecino mas el actual
        tot += 1 + dfs(graph[u]);
    }
    //Saco la visita
    vis[u] = false;
    //Seteo el total al vector de sumas
    return sum[u] = tot;
}

int main() {
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        scanf("%d", &N);
        //Inicializo mis vectores
        graph.assign(N, -1);
        sum.assign(N, -1);
        vis.assign(N, false);
        //Inicializo el grafo
        for(int i = 0; i < N; i++) {
            scanf("%d %d", &a, &b);
            graph[a - 1] = b - 1;
        }
        //Inicializo las respuestas
        int ans = 0, best_len = 0;
        //Recorro los nodos
        for(int i = 0; i < N; i++) {
            //Si el nodo actual no tiene un valor asignado, hago dfs
            if(sum[i] == -1) dfs(i);
            //Si el valor del nodo actual es mayor al mejor
            if(sum[i] > best_len) {
                //Seteo el valor del nodo actual como mejor
                best_len = sum[i];
                ans = i;
            }
        }
        printf("Case %d: %d\n", t, ans + 1);
    }
}
