#include <iostream>
#include <cstdio>
using namespace std;
#define MAXN 10000
int set[MAXN];    // set[i] = padre de i
int sz[MAXN];    // sz[i] = numero de elementos en el subarbol con raiz en i
int componentes;   // numero de componentes

/*
  Complejidad: inicializar me lleva O(n), las operaciones de union-find me llevan O(log n).
               Como no tiene otra complejidad mas que unir conjuntos y chequear en determinado momento
               si dos nodos pertenecen al mismo conjunto (mas algunas operaciones O(1) como incrementar y decrementar variables),
               tiene complejidad O(n) + O(log n) = O(log n)
*/

// Creo una estructura de UnionFind con N sets independientes
void inicializar(int N) {
    componentes = N;
    for (int i = 0; i < N; i++) {
      set[i] = i;
      sz[i] = 1;
    }
}
int find(int i) {
    if(set[i]==i){
        return set[i];
    }
    else{
        return set[i]=find(set[i]);
    }
}

// Devuelve si p y q estan en el mismo conjunto
bool conectados(int p, int q) {
    return find(p) == find(q);
}


// Hace la union del conjunto al que pertenece p con el de q
void unite(int i, int j) {
    //Pongo a i como parte del set de j
    set[find(i)]=find(j);
    componentes--;
}


int main(){
    /*
      n: cantidad de computadoras en la red
      a: compuradora-i
      b: computadora-j
    */
    int n,a,b,test,exito,falla;
    char tipo,buffer[100];
    scanf("%d",&test);
    while(test--){
      scanf("%d",&n);
      getchar();
      //Inicializo
      inicializar(n);
      exito=0;
      falla=0;
      buffer[0]='1';
      while (gets(buffer)) {
        if(buffer[0]==NULL){
            break;
        }
        //Leo el input
        sscanf(buffer,"%c %d %d",&tipo,&a,&b);
        a--;
        b--;
        // Si estan interconectadas
        if(tipo=='c'){
            //Hago la union de a con b
            unite(a, b);
        }
        else{
            // Si es una pregunta, chequeo si pertenecen al mismo conjunto
            if(conectados(a, b)){
                //Incremento el contador de exito
                exito++;
            }
            else{
                //Incremento el contador de falla
                falla++;
            }
          }
      }
      //Printeo la cantidad de exitos y de fallas que hubo
      printf("%d,%d\n",exito,falla);
      if(test!=0){
        printf("\n");
      }
  }
  return 0;
}
