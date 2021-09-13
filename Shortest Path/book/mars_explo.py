import heapq
t = int(input())
# INF = int(1e9)

def dijkstra(n:int,graph:list,visited:list)->int:
    ret = 0
    q = []
    visited[0][0] = True
    
    for x in range(n):
        for y in range(n):
            if x == 0 and y == 0:
                continue

            elif x == 0:
                graph[x][y] = graph[x][y] + graph[x][y-1]

            elif y == 0:
                graph[x][y] = graph[x][y] + graph[x-1][y]
            
            else:
                graph[x][y] = graph[x][y] + min(graph[x-1][y],graph[x][y-1])
    ret = graph[n-1][n-1]
    return ret


for _ in range(t):
    n = int(input())
    graph = []
    visited = [[False]*n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    
    print("ans : ",dijkstra(n,graph,visited))


"""
1
3
5 5 4
3 9 1
3 2 7
"""


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""