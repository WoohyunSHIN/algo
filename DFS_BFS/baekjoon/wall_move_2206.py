from collections import deque
n, m = map(int,input().split())

graph = []

for _ in range(n):
    row = list(map(lambda x:int(x),list(input())))
    graph.append(row)

def _bfs(n:int,m:int,graph:list,x:int,y:int)->int:
    ret = 0
    visited = [[0]*m for _ in range(n)]
    visited[y][x] = 1

    q = deque()
    q.append([x,y,1])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        print(q)
        x, y, drill = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue

            if graph[ny][nx] == 1:
                continue

            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1 
                visited[ny][nx] = 1
                q.append([ny,nx,drill])
                print(graph)
            
    
    return ret

def main(n:int,m:int,graph:list)->int:
    ret = 0

    _bfs(n,m,graph,0,0)

    return ret

print(main(n,m,graph))


# 복붙
"""
Test 1.
6 4
0000
1110
1000
0000
0111
0000
9
"""

"""
Test 2.
6 4
0100
1110
1000
0000
0111
0000
15
"""

"""
Test 3.
6 4
0110
1110
1000
0000
0111
0000
-1
"""