from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] * (n+1)
results = [0] * (n+1)

# 5개
for i in range(1,n+1):
    info = list(map(int,input().split()))
    
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort(n:int,graph:list,indegree:list,time:list)->None:
    q = deque()
    result = copy.deepcopy(time)
    print(graph)

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        print(f"now = {now}")

        for node in graph[now]:
            # 핵심 코드
            # result[node] = result[now] + time[node]
            result[node] = max(result[node],result[now] + time[node])
            print(f"result[node] = {result[node]}")
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

    for i in range(1,n+1):
        print(result[i])


topology_sort(n,graph,indegree,time)
# (강의시간) (선수강 번호) (-1)
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""