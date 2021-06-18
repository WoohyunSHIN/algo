from collections import deque
import time

case = int(input())

def _dfs(l:int, start:list, end:list)->int:
    ret = 0

    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    q = deque()
    # start
    # [0,0,0]
    start.append(0)
    q.append(start)
    visited = [[0]*l for _ in range(l)]

    while q:
        #print(visited)
        x, y, cnt= q.popleft()
        # visited.append((x,y))

        if [x,y] == end:
            ret = cnt
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
                visited[ny][nx] = 1

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

print("time : ", time.time() - t_start)

"""
Case 1.
1
8
0 0
7 0

ans = 5
"""

"""
1
10
1 1
1 1

ans = 0
"""

"""
1
10
1 1
3 0

ans = 1
"""

"""
1
100
0 0
30 50

ans = 25
"""

