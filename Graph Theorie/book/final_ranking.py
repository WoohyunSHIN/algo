from collections import deque

def main()->None:
    n = int(input())
    t = list(map(int,input().split()))

    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(i+1,n):
            graph[t[i]][t[j]] = True
            indegree[t[j]] += 1
    #print(f"graph = {graph}")
    print(f"bf: indegree = {indegree}")

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    print(f"af: indegree = {indegree}")

    ret = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        ret.append(now)

        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in ret:
            print(i, end=' ')

tc = int(input())

for _ in range(tc):
    main()

"""
1
5
5 4 3 2 1
2
2 4
3 4
"""

"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""