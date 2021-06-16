# 시간초과
from collections import deque

m, n = map(int,input().split())

graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

def _bfs(graph:list,m:int,n:int,y:int,x:int,visited:list)->list:
    ret = []
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0] 

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if (ny,nx) in visited:
            continue

        if ny >= n or nx >= m or nx <= -1 or ny <= -1:
            continue
            
        if graph[ny][nx] == -1:
            continue

        if graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            ret.append((ny,nx))

    return ret

def main(graph:list,m:int,n:int)->int:
    ret = 0
    cnt = 0

    visit = deque()
    visited = []

    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                visit.append((y,x))

    while visit:
        y, x = visit.popleft()
        
        if (y,x) not in visited:
            # print(f"({cnt}) : visit = {visit} visited = {visited}")
            visit += list(set(_bfs(graph,m,n,y,x,visited)) - set(visited))
            visited.append((y,x))
            cnt += 1
    # print(graph)
    graph = sum(graph,[])

    if 0 in graph:
        ret = -1
    else:
        ret = max(graph) - 1

    return ret

print(main(graph,m,n))