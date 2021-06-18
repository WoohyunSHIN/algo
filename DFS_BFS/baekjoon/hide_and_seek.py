from collections import deque

n, k = map(int,input().split())

def _dfs(n:int,k:int)->int:
    ret = 0 
    LIMIT = 100001
    visited = [0] * LIMIT

    q = deque()
    q.append([n,0])

    while q:
        x, cnt = q.popleft()

        if x == k:
            ret = cnt
            break

        for nx in [x+1,x-1,x*2]:
            if nx <= -1 or nx >= LIMIT:
                continue

            if visited[nx] == 0:
                visited[nx] = 1
                q.append([nx,cnt+1])

    return ret

def main(n:int,k:int)->int:
    ret = 0

    ret = _dfs(n,k)

    return ret

print(main(n,k))