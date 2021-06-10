n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def _dfs(i:int, j:int)->bool:
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False
    
    if graph[i][j] == 0:
        graph[i][j] = 1
        _dfs(i-1,j)
        _dfs(i,j-1)
        _dfs(i+1,j)
        _dfs(i,j+1)
        return True
    return False

def my_main(n:int, m:int, graph:list)->int:
    ret = 0

    for i in range(n):
        for j in range(m):
            if _dfs(i,j) == True:
                print(f"coordination : ({i+1},{j+1})")
                print("------------------")
                ret += 1

    return ret

print(my_main(n,m,graph))