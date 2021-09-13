from collections import deque

v, e = map(int,input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(v:int, e:int, indegree:list, graph:list)->None:
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

    for i in result:
        print(i, end=' ')

topology_sort(v,e,indegree,graph)

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""