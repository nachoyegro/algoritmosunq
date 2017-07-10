
#include<bits/stdc++.h>
using namespace std;
//L: Es el valor actual del candado
//R: Es la cantidad de botones que hay en el candado
//U: es el codigo de desbloqueo del candado
int L, R, U, RVs[10000], c=1;
int dist[10000];
queue<int> q;
/*
  Complejidad: Como recorro todos los nodos solo una vez, la complejidad es O(n+m)
*/

int bfs() {
    //Inicializo
    q = queue<int>();
    //Inicializo con -1
    memset(dist, -1, sizeof dist);
    dist[L] = 0;
    q.push(L);
    //Mientras tenga para procesar
    while (!q.empty()) {
        //Traigo el proximo
        int u = q.front(); q.pop();
        for(int i=0; i<R; i++){
            //Solo tengo en cuenta los 4 digitos mas significativos
            int v = (u + RVs[i]) % 10000;
            //Si no fue procesado
            if (dist[v] == -1) {
                //Proceso
                dist[v] = dist[u] + 1;
                //Si llegue al codigo de desbloqueo, retorno
                if (v == U) return dist[v];
                q.push(v);
            }
        }
    }
    return -1;
}

int main() {
    while (scanf("%d %d %d", &L, &U, &R), (L || U || R)) {
        for(int i=0; i<R; i++)
        {
            scanf("%d", &RVs[i]);
        }

        printf("Case %d: ", c++);
        int resultado = bfs();
        if (resultado == -1) printf("Permanently Locked\n");
        else printf("%d\n", resultado);
    }
}
