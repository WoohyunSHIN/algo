from collections import deque
import time

m, n = map(int,input().split())

graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

def _dfs(m:int,n:int,graph:list,start_points:deque)->int:
    ret = 0

    visited = [[0]*m for _ in range(n)]

    q = deque()

    for start_point in start_points:
        q.append(start_point)
        visited[start_point[1]][start_point[0]] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q: 
        #print(q)
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= m or ny >= n:   
                continue

            if graph[ny][nx] == -1:
            # if graph[ny][nx] == -1 or visited[ny][nx] == 1:
                continue

            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
            # if graph[ny][nx] == 0:
                graph[ny][nx] = cnt + 1
                visited[ny][nx] = 1
                q.append([nx,ny,cnt+1])

    return ret

def main(m:int,n:int,graph:list)->int:
    ret = 0

    start_points = deque()
    
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                start_points.append([x,y,1])

    _dfs(m,n,graph,start_points)

    for row in graph:
        for value in row:
            if value == 0:
                return -1
            ret = max(ret,value-1)

    # graph = sum(graph,[])
    # if 0 in graph:
    #     ret = -1
    # else:
    #     ret = max(graph) - 1

    return ret

print(main(m,n,graph))