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
int n, m;
int G[maxn][maxn];
int v[maxn];
int d[maxn];

int calc(const string &s){
    int ans = 0;
    for(int i = 0; i < s.size(); ++i)  ans = ans * 10 + s[i] - '0';
    return ans;
}

int dijkstra(){
    priority_queue<ii, vector<ii>, greater<ii> > pq;
    pq.push(ii(0, 0));
    memset(d, INF, sizeof d);
    d[0] = 0;

    while(!pq.empty()){
        ii p = pq.top();  pq.pop();
        int v = p.second;
        if(v == m)  return p.first;
        if(d[v] < p.first)  continue;
        for(int i = 0; i < 100; ++i){
          if(G[v][i] == INF)  continue;
          if(d[i] > d[v] + G[v][i] + 60){
            d[i] = d[v] + G[v][i] + 60;
            pq.push(ii(d[i], i));
          }
        }
    }
    return -1;
}

int main(){
    while(cin >> n >> m){
        for(int i = 0; i < n; ++i)  cin >> v[i];
        cin.get();
        memset(G, INF, sizeof G);
        for(int i = 0; i < n; ++i){
            string line;
            getline(cin, line);
            stringstream ss(line);
            string s;
            vector<int> vv;
            while(ss >> s)  vv.push_back(calc(s));
            sort(vv.begin(), vv.end());
            for(int j = 0; j < vv.size(); ++j)
                for(int k = j+1; k < vv.size(); ++k)
                    G[vv[j]][vv[k]] = G[vv[k]][vv[j]] = min(G[vv[j]][vv[k]], (vv[k]-vv[j])*v[i]);
            }
        if(m == 0){ cout << "0" << endl;  continue; }
        int ans = dijkstra();
        if(ans == -1)  cout << "IMPOSSIBLE" << endl;
        else  cout << ans - 60 << endl;
    }
    return 0;
}
