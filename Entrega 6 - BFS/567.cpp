
#include<bits/stdc++.h>
using namespace std;

vector<int>graph[21];
/*
  Complejidad: Dado que por cada inicio inicializo la lista de visitados y recorro,
      el algoritmo tiene complejidad O(n^2)
*/
void bfs(int s, int d)
{
    //Inicializo la cola
    queue< int >q;
    int visited[50]={0}, level[50];
    visited[s]=1;
    level[s]=0;
    //Encolo el elemento inicial
    q.push(s);
    //Mientras tengo elementos para procesar
    while(!q.empty())
    {
        //Traigo el proximo
        int u=q.front();
        for(int l=0; l<graph[u].size(); l++)
        {
            //Me traigo el proximo vecino
            int v = graph[u][l];
            //Si no fue visitado..
            if(!visited[v])
            {
                //Lo proceso
                visited[v]=1;
                level[v] = level[u]+1;
                //Lo pongo en la cola para ser procesado
                q.push(v);
            }
        }
        q.pop();
    }
   printf("%2d to %2d: %d\n", s, d, level[d]);
}

int main()
{
    int x, y, caseno=0;
    //Mientras tenga input para procesar
    while(scanf("%d",&x)==1)
    {
        //Recorro el input
        for(int j=0; j<x; j++)
        {   //Genero para 1
            scanf("%d",&y);
            graph[1].push_back(y);
            graph[y].push_back(1);
        }
        for(int i=2; i<=19; i++)
        {
            scanf("%d",&x);
            for(int j=0; j<x; j++)
            {
                scanf("%d",&y);
                graph[i].push_back(y);
                graph[y].push_back(i);
            }
        }
        int inicio, destino, n;
        scanf("%d",&n);
        printf("Test Set #%d\n",++caseno);
        for(int i=0; i<n; i++)
        {
            scanf("%d %d",&inicio, &destino);
            bfs(inicio,destino);
        }
       printf("\n");
       for(int i=0; i<21; i++)
       {
           graph[i].clear();
       }
    }
    return 0;
}
