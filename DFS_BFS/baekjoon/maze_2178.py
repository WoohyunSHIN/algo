from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(input())
    row = list(map(int,row))
    graph.append(row)

def _dfs(graph:list,x:int,y:int,n:int,m:int)->int:
    ret = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0] 

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    ret = graph[-1][-1]
    return ret

def main(n:int,m:int,graph:list)->int:
    ret = 0

    ret = _dfs(graph,0,0,n,m)
    return ret

print(main(n,m,graph))