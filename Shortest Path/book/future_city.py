INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(1,N+1):
    for b in range(1,N+1):
        if a == b:
            graph[a][b] = 0 

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

def main(N:int, M:int, X:int, K:int, graph:list)->int:
    # X = 도착
    # K = 들르는곳
    ret = 0

    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    
    if graph[1][K] == INF or graph[K][X] == INF:
        ret = -1
    else:
        cost = graph[1][K] + graph[K][X]
        ret = cost

    return ret

print(main(N,M,X,K,graph)) 

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

"""
4 2
1 3
2 4
3 4
"""

