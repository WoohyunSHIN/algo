from collections import defaultdict, deque

n = int(input())
m = int(input())
start = 1
graph = defaultdict(set)

for _ in range(m):
    n1, n2 = map(int,input().split())
    graph[n1].add(n2)
    graph[n2].add(n1)

def bfs(start:int, graph:dict)->int:
    ret = 0

    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        
        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n] - set(visited), reverse = True) 
    ret = len(visited) - 1 
    return ret

def dfs(start:int,graph:dict)->int:
    ret = 0

    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    
    ret = len(visited)-1

    return ret

print(dfs(start,graph))
print(bfs(start, graph))