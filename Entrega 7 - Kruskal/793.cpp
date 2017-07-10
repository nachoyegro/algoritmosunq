#include <iostream>
#include <cstdio>
using namespace std;
#define MAXN 10000

int id[MAXN];    // id[i] = padre de i
int sz[MAXN];    // sz[i] = numero de elementos en el subarbol con raiz en i
int componentes;   // numero de componentes

/*
  Complejidad: 
*/

// Creo una estructura de UnionFind con N sets independientes
void init(int N) {
  componentes = N;
  for (int i = 0; i < N; i++) {
      id[i] = i;
      sz[i] = 1;
  }
}
int find(int p) {
  //TODO: Probar cambiar el while por un if
  while (p != id[p])
      p = id[p];
  return p;
}

// Devuelve si p y q estan en el mismo conjunto
bool conectados(int p, int q) {
  return find(p) == find(q);
}


// Hace la union del conjunto al que pertenece p con el de q
void makeUnion(int p, int q) {
  int i = find(p);
  int j = find(q);
  if (i == j) return;

  // apunto la raiz mas chica a la mas grande
  if   (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
  else                 { id[j] = i; sz[i] += sz[j]; }
  componentes--;
}


int main(){
  int n,a,b,test,success,fail;
  char ch,buffer[100];
  scanf("%d",&test);
  while(test--){
    scanf("%d",&n);
    getchar();
    init(n);
    success=0;
    fail=0;
    buffer[0]='1';
    while (getline(buffer)) {
      if(buffer[0]==NULL)break;
      sscanf(buffer,"%c %d %d",&ch,&a,&b);
      a--;
      b--;
      if(ch=='c')  makeUnion(a, b);
      else if (connected(a, b)) success++;
      else fail++;
    }
    printf("%d,%d\n",success,fail);
    if(test!=0){
      printf("\n");
    }
  }
  return 0;
}
