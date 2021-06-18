from collections import deque
import time

case = int(input())

def _dfs(l:int, start:list, end:list)->int:
    ret = 0

    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    q = deque()
    start.append(0)
    q.append(start)
    visited = [[0]*l for _ in range(l)]

    while q:
        x, y, cnt= q.popleft()

        if [x,y] == end:
            ret = visited[y][x]
            return ret
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or ny <= -1 or nx >= l or ny >= l:
                continue

            if visited[ny][nx] == 1:
                continue

            if visited[ny][nx] == 0:
                q.append([nx,ny,cnt+1])
                visited[ny][nx] = visited[y][x] + 1 

    return ret

def main(l:int, start:list, end:list)->int:
    ret = 0

    ret = _dfs(l,start,end)

    return ret

t_start = time.time()
for _ in range(case):
    l = int(input())
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    print(main(l,start,end))



