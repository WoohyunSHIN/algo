"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

def main(n:int,m:int,mine:list)->int:
    ret = 0
    mine_graph = []
    start = 0
    end = m
    for _ in range(n):
        mine_graph.append(mine[start:end])
        start = end
        end += m
    #print(mine_graph)
    # j = m, m = 4
    # i = n, n = 3
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = mine_graph[i-1][j-1]
            
            if i == n-1:
                left_down = 0 
            else:
                left_down = mine_graph[i+1][j-1]
            
            left = mine_graph[i][j-1]

            mine_graph[i][j] = mine_graph[i][j] + max(left_up,left_down,left)

    for i in range(n):
        ret = max(ret,mine_graph[i][m-1])

    return ret

T = int(input())

final_ret = []

for _ in range(T):
    n, m = map(int,input().split())
    mine = list(map(int,input().split()))
    final_ret.append(main(n,m,mine))
    """
    1 3 3 2
    2 1 4 1 
    0 6 4 7
    """
for ret in final_ret:
    print(ret)