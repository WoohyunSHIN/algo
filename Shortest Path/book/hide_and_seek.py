import heapq

INF = int(1e9)
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def main(n:int,m:int,graph:list)->list:
    ret = []
    q = []
    start = 1

    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    nums = []
    max_dist = 0

    for i in range(1,n+1):
        max_dist = max(max_dist,distance[i])

    for i in range(len(distance)):
        if distance[i] == max_dist:
            nums.append(i)
    print(nums)
    
    ret.append(sorted(nums)[0])
    ret.append(max_dist)
    ret.append(len(nums))


    return ret

for x in main(n,m,graph):
    print(x,end=" ")

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""