#include <iostream>
#include <vector>
#include <sstream>
#include <queue>
#include <map>

using namespace std;

typedef pair<string, bool> letra_usada;
typedef pair<int, letra_usada> leng_letra;
typedef vector<leng_letra> ll;
typedef vector<ll> grafo;

//Par con largo total y ultima letra
typedef pair<int, char> largo_letra;
//Par con el par anterior y el lenguaje
typedef pair<largo_letra, int> ici;

/*
  Complejidad:
*/

int dijkstra(grafo &g, int inicio, int fin) {

    priority_queue<ici> pq;
    //Pusheo el inicio
    pq.push(make_pair(make_pair(0, 'A'), inicio));

    while (!pq.empty()) {
        //Traigo el proximo de la cola de prioridad
        ici p = pq.top();
        pq.pop();

        //Si ya llegue al ultimo lenguaje, retorno el largo total
        if (p.second == fin){
          return -p.first.first;
        }

        for (int i = 0; i < g[p.second].size(); ++i) {

            //si no fue usada la arista actual y
            //la primer letra es diferente de la ultima
            if (   !g[p.second][i].second.second and
                    g[p.second][i].second.first[0] != p.first.second) {

                //agrego la arista a la cola
                //agrego el inverso del largo asi la cola ordena por el mas corto
                pq.push(
                    make_pair(
                        make_pair(  -(-(p.first.first) +
                        g[p.second][i].second.first.size()),
                        g[p.second][i].second.first[0]),
                        g[p.second][i].first));

                //marco la arista como usada
                g[p.second][i].second.second = true;
            }
        }
    }

    return -1;
}


int main() {

    string line;
    getline(cin, line);
    istringstream ss(line);

    int n;
    ss >> n;
    while (n) {

        //hago un map que me da el indice para cada lenguaje
        map<string, int> m;
        grafo graph;
        int graph_index = 0;

        getline(cin, line);
        ss.clear();
        ss.str(line);
        string inicio, fin;
        ss >> inicio >> fin;

        for (int i = 0; i < n; ++i) {

            getline(cin, line);
            ss.clear();
            ss.str(line);
            string a, b, w;
            ss >> a >> b >> w;

            if (m.find(a) == m.end()){
                m[a] = graph_index;
                graph_index++;
                graph.push_back(ll ());
            }
            if (m.find(b) == m.end()){
                m[b] = graph_index;
                graph_index++;
                graph.push_back(ll ());
            }
            graph[m[a]].push_back(make_pair(m[b], make_pair(w,false)));
            graph[m[b]].push_back(make_pair(m[a], make_pair(w,false)));
        }
        //TODO
        if (m.find(inicio) == m.end() or m.find(fin) == m.end()) {
            cout << "impossivel" << endl;
        } else {
            int cost = dijkstra(graph, m[inicio], m[fin]);
            if(cost < 0) cout << "impossivel" << endl;
            else cout << cost << endl;
        }

        getline(cin, line);
        ss.clear();
        ss.str(line);
        ss >> n;
    }
}
