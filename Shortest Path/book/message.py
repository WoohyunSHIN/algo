import heapq

INF = int(1e9)
n,m,c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,dist = map(int, input().split())
    graph[a].append((b,dist))

def main(n:int,m:int,c:int,graph:list,distance:list)->list:
    q = []
    heapq.heappush(q,(0,c))
    distance[c] = 0 

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: 
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,now))

    return distance

updated_distance = main(n,m,c,graph,distance)

cnt = 0
max_value = 0

for i in updated_distance[1:]:
    if i != INF:
        cnt += 1
        max_value = max(max_value,i)

print(cnt-1, max_value)
"""
3 2 1
1 2 4
1 3 2
"""