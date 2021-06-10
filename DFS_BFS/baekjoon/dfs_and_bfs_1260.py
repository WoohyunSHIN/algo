from collections import deque, defaultdict

n, m, v = map(int,input().split())
graph = defaultdict(set)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(v:int,graph:dict)->str:
    ret = ' '
    visited = []
    stack = [v]

    while stack:
        #print(f"stack: {stack} visited : {visited}")
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += sorted(graph[n] - set(visited),reverse=True)

    ret = ret.join(str(i) for i in visited)
    return ret

def bfs(v:int,graph:dict)->str:
    ret = ' '

    visited = []
    queue = deque([v])

    while queue:
        print(f"queue: {queue} visited : {visited}")
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += sorted(graph[n] - set(visited))

    ret = ret.join(str(i) for i in visited)
    return ret

print(dfs(v,graph))
print(bfs(v,graph))