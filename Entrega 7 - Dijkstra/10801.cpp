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
#include <map>
#include <cctype>
#include <cmath>
#include <stack>
#include <sstream>
#define debug() puts("++++");
#define gcd(a, b) __gcd(a, b)
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define freopenr freopen("in.txt", "r", stdin)
#define freopenw freopen("out.txt", "w", stdout)
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> P;
const int INF = 0x3f3f3f3f;
const double inf = 0x3f3f3f3f3f3f;
const double PI = acos(-1.0);
const double eps = 1e-8;
const int maxn = 100 + 10;
const int mod = 1e9 + 7;
const int dr[] = {-1, 0, 1, 0};
const int dc[] = {0, 1, 0, -1};
const char *de[] = {"0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"};
int n, m;
const int mon[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const int monn[] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
inline bool is_in(int r, int c){
  return r >= 0 && r < n && c >= 0 && c < m;
}

int G[maxn][maxn];
int v[maxn];

int calc(const string &s){
  int ans = 0;
  for(int i = 0; i < s.size(); ++i)  ans = ans * 10 + s[i] - '0';
  return ans;
}
int d[maxn];

int dijkstra(){
  priority_queue<P, vector<P>, greater<P> > pq;
  pq.push(P(0, 0));
  memset(d, INF, sizeof d);
  d[0] = 0;

  while(!pq.empty()){
    P p = pq.top();  pq.pop();
    int v = p.second;
    if(v == m)  return p.first;
    if(d[v] < p.first)  continue;
    for(int i = 0; i < 100; ++i){
      if(G[v][i] == INF)  continue;
      if(d[i] > d[v] + G[v][i] + 60){
        d[i] = d[v] + G[v][i] + 60;
        pq.push(P(d[i], i));
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
