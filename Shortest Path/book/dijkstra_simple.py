INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b,dist))

def _get_smallest_node(graph:list,visited:list)->int:
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def main(n:int,m:int,start:int,graph:list,visited:list,distance:list)->list:
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = _get_smallest_node(graph,visited)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

    return distance

updated_distance = main(n,m,start,graph,visited,distance)

for i in range(1, n+1):
    if updated_distance[i] == INF:
        print("INFINITY")
    else:
        print(updated_distance[i])

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""


