from collections import deque
t = int(input())

def _bfs(x:int,y:int,graph:list,cnt:int,m:int,n:int):
    visited = [[0]*m for _ in range(n)]

    q = deque()
    q.append([x,y])
    visited[y][x] = 1
    graph[y][x] = cnt

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny <= -1 or nx <= -1 or ny >= n or nx >= m:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                graph[ny][nx] = cnt
                q.append([nx,ny])
                visited[ny][nx] = 1

def main(m:int, n:int, k:int, graph:list)->int:
    ret = 0
    cnt = 2
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                _bfs(x,y,graph,cnt,m,n)
                cnt += 1

    graph = sum(graph,[])
    ret = max(graph) - 1

    return ret

results = []
for _ in range(t):
    m, n, k = map(int,input().split())

    graph = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(0)
        graph.append(row) 

    for _ in range(k):
        j, i = map(int,input().split())
        graph[i][j] = 1
    results.append(main(m, n, k, graph))

for result in results:
    print(result)