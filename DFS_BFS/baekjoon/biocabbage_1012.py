from collections import deque
t = int(input())

def _dfs(i:int,j:int,graph:list)->bool:
    if i <= -1 or j <= -1 or i >= m or j >= n:
        return False

    if graph[j][i] == 1:
        graph[j][i] = 0
        _dfs(i+1,j,graph)
        _dfs(i-1,j,graph)
        _dfs(i,j+1,graph)
        _dfs(i,j-1,graph)
        return True

    return False

def _bfs(graph:list,x:int,y:int)->int:
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    queue = deque()
    queue.append((x,y))

    while queue:
        print(graph)
        print("---")
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue

            try:
                if graph[nx][ny] == 0:
                    continue
            except:
                print(f"nx{nx} ny{ny}")

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))


def main(m:int,n:int,k:int,graph:list)->int:
    ret = 0
    for i in range(m):
        for j in range(n):
            # if _dfs(i,j,graph) == True:
            #     ret += 1
    
            if graph[i][j] == 1:
                _bfs(graph,i,j)
                graph[i][j] = 0 
                ret += 1
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
