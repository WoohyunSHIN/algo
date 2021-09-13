import heapq
INF = int(1e9)

def dijkstra(n:int,graph:list,distance:list):
    ret = 0
    q = []
    heapq.heappush(q,(0,0,graph[0][0]))
    distance[0][0] = graph[0][0]

    dx = [1,1,-1,-1]
    dy = [-1,1,1,-1]

    while q:
        x, y, dist = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            cost = graph[nx][ny] + dist

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(nx,ny,cost))

    print(distance)
    ret = distance[n-1][n-1]
    return ret

for t in range(int(input())):
    n = int(input())
    graph = []
    for _ in range(n):
        row = list(map(int,input().split()))
        graph.append(row)
    distance = [[INF]*n for _ in range(n)]
    print(dijkstra(n,graph,distance))
