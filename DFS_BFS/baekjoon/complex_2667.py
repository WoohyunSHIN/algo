from collections import Counter
n = int(input())
graph = []

for _ in range(n):
    row = list(map(int,input()))
    graph.append(row)

def _dfs(i:int,j:int,number:int)->bool:
    if i <= -1 or j <= -1 or i >= n or j >= n:
        return False

    if graph[i][j] == 1:
        graph[i][j] = number
        _dfs(i-1,j,number)
        _dfs(i+1,j,number)
        _dfs(i,j-1,number)
        _dfs(i,j+1,number)
        return True
    return False


def main(n:int,graph:list)->str:
    ret = '\n'
    result = []
    number = 2

    for i in range(n):
        for j in range(n):

            if _dfs(i,j,number) == True:
                number += 1
    # result = ['3','7','8','9']
    print(graph)

    graph = sum(graph, [])
    cnt_graph = dict(Counter(graph))
    del cnt_graph[0]
    result.append(len(cnt_graph))
    result += sorted(list(cnt_graph.values()))

    result = list(map(str,result))
    ret = ret.join(result)
    return ret

print(main(n,graph))