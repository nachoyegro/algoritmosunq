#include <cstdio>
#include <string>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <cstring>
#include <set>
#include <queue>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <sstream>
using namespace std;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const int maxn = 100 + 10;

//Input siendo n: el numero de ascensores, k: el piso al que tengo que llegar
int n, k;
//Grafo
int G[maxn][maxn];
int tiempos[maxn];
int memo[maxn];

int calcular(const string &s){
    int ans = 0;
    for(int i = 0; i < s.size(); ++i){
        ans = ans * 10 + s[i] - '0';
    }
    return ans;
}

/*
  Complejidad:
*/

int dijkstra(){
    //Inicializo la cola de prioridad
    priority_queue<ii, vector<ii>, greater<ii> > pq;
    //Arranco con tiempo 0 en el piso 0
    pq.push(ii(0, 0));
    memset(memo, INF, sizeof memo);
    memo[0] = 0;

    while(!pq.empty()){
        //Traigo el proximo par
        ii p = pq.top();
        pq.pop();
        //Traigo el piso en el que estoy
        int piso_actual = p.second;
        //Si ya llegue al piso, retorno el tiempo
        if(piso_actual == k)  return p.first;
        //Si el tiempo actual es mayor al almacenado, continuo
        if(memo[piso_actual] < p.first)  continue;
        for(int i = 0; i < 100; ++i){
          //Si todavia no fue procesado, continuo
          if(G[piso_actual][i] == INF)  continue;
          if(memo[i] > memo[piso_actual] + G[piso_actual][i] + 60){
            memo[i] = memo[piso_actual] + G[piso_actual][i] + 60;
            pq.push(ii(memo[i], i));
          }
        }
    }
    //Si la cola queda vacia y no llegue al piso, retorno -1
    return -1;
}

int main(){
    while(cin >> n >> k){
        for(int i = 0; i < n; ++i){
          //Traigo los tiempos de cada ascensor
          cin >> tiempos[i];
        }
        cin.get();
        //Inicializo el grafo
        memset(G, INF, sizeof G);
        for(int i = 0; i < n; ++i){
            string line;
            getline(cin, line);
            stringstream ss(line);
            string s;
            vector<int> vv;
            while(ss >> s){
              vv.push_back(calcular(s));
            }
            sort(vv.begin(), vv.end());
            //Genero el grafo
            for(int j = 0; j < vv.size(); ++j){
                for(int l = j+1; l < vv.size(); ++l){
                    tiempo_minimo = min(G[vv[j]][vv[l]], (vv[l]-vv[j]) * tiempos[i]);
                    G[vv[j]][vv[l]] = tiempo_minimo;
                    G[vv[l]][vv[j]] = tiempo_minimo;
                }
            }
        }
        if(k == 0){
          cout << "0" << endl;
          continue;
        }
        //Hago dijkstra
        int ans = dijkstra();
        //Si no llego al piso, retorno IMPOSSIBLE
        if(ans == -1){
          cout << "IMPOSSIBLE" << endl;
        }
        else{
          cout << ans - 60 << endl;
        }
    }
    return 0;
}
