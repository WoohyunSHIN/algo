from collections import defaultdict, deque
K = int(input())

def _dfs(visited:list,q:deque):
    ret = True

    while q:
        # print(f"visited  = {visited} q = {q}")
        A,B = q.popleft()
        if visited[A] == 1 and visited[B] == 1:
            ret = False
            return ret

        visited[A] = 1
        visited[B] = 1     

    return ret

def main(V:int,E:int,q:deque)->bool:
    ret = False

    visited = [0] * (V+1)
    if _dfs(visited,q):
        ret = True
        return ret

    return ret

res = []
for _ in range(K):
    V, E = map(int,input().split())
    q = deque()
    for _ in range(E):
        A_node, B_node = map(int,input().split())
        q.append((A_node,B_node))
    
    if main(V,E,q):
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)

# https://jdselectron.tistory.com/51