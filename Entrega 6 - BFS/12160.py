import queue
import sys


def bfs():
    q = queue.Queue()
    while not q.empty():
        u = q.get()

int L, R, U, RVs[10000], c=1;
int dist[10000];
queue<int> q;

int bfs() {
    q = queue<int>();
    memset(dist, -1, sizeof dist);
    dist[L] = 0;
    q.push(L);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        REP(i, R) {
            int v = (u + RVs[i]) % 10000;
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                if (v == U) return dist[v];
                q.push(v);
            }
        }
    }
    return -1;
}

int main() {
    while (scanf("%d %d %d", &L, &U, &R), (L || U || R)) {
        REP(i, R) scanf("%d", &RVs[i]);

        printf("Case %d: ", c++);
        int val = bfs();
        if (val == -1) printf("Permanently Locked\n");
        else printf("%d\n", val);
    }
}
