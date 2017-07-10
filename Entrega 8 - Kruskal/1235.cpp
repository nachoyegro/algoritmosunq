#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define INF 1000000000

typedef pair<int ,int> ii;
typedef vector <int> vi;

vector <pair<int ,ii> > edges;
vi set;

/*
    Complejidad:
*/

void inicializar(int N){
    //Inicializo el set
    set.assign(N,0);
    for(int i=0;i<N;i++){
        set[i]=i;
    }
}

int find(int i){
    if(set[i]==i){
        return set[i];
    }
    else{
        return set[i]=find(set[i]);
    }

}

bool conectados(int i,int j){
    //True si i y j comparten el mismo set
    return find(i)==find(j);
}

void unite(int i,int j){
    //Pongo a i como parte del set de j
    set[find(i)]=find(j);
}

int dist(int a,int b){
    //Calculo la diferencia entre a y b
    int sum=0;
    //Por cada digito
    for(int i=0;i<4;i++){
        //Calculo el minimo entre girar para arriba y girar para abajo
        sum+=min( abs(a%10 - b%10) , 10-abs(a%10 - b%10) );
        //Paso al siguiente digito
        a/=10,b/=10;
    }
    return sum;
}


int main(){
    int n,m,a,b,t;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        inicializar(n);
        edges.clear();
        int input[n];
        for(int i=0;i<n;i++){
            scanf("%d",&input[i]);
        }
        //Seteo sum como INF asi el primer sum es el primer input
        int sum=INF;
        for(int i=0;i<n;i++){
            sum=min(sum,dist(0,input[i]));
        }

        for(int i=0;i<n;i++)
          for(int j=i+1;j<n;j++){
            ii tmp=make_pair(i,j);
            edges.push_back(make_pair(dist(input[i],input[j]),tmp));
          }
        sort(edges.begin(),edges.end());

        for(int i=0;i<edges.size();i++){
            if(!conectados(edges[i].second.first,edges[i].second.second)){
                sum+=edges[i].first;
                unite(edges[i].second.first,edges[i].second.second);
            }
        }
        printf("%d\n",sum);
    }
    return 0;
}
