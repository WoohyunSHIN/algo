INF = int(1e9)
n,m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = -1
    graph[b][a] = 1

def main(n:int,m:int,graph:list)->int:
    ret = 0

    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if graph[a][k] != INF and graph[k][b] != INF and graph[a][k] == graph[k][b]:
                    graph[a][b] = graph[a][k]

    for ls in graph:
        # 500은 최대 학생의 수
        if sum(ls) < (2*INF)-500:
            ret += 1
    return ret

print(main(n,m,graph))

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""