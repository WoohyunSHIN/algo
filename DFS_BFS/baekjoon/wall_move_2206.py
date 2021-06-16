from collections import deque
n, m = map(int,input().split())

graph = []

for _ in range(n):
    row = list(map(lambda x:int(x),list(input())))
    graph.append(row)

def _bfs(n:int,m:int,graph:list,x:int,y:int)->int:
    ret = 0
    
    q = deque()
    q.append((x,y))

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx <= -1 or ny <= -1 or nx >= m or ny >= n:
                continue   

            if graph[ny][nx] == 1:
                continue

            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 2
                q.append((nx,ny))
                print(graph)

    return ret

def main(n:int,m:int,graph:list)->int:
    ret = 0

    ret = _bfs(n,m,graph,0,0)

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