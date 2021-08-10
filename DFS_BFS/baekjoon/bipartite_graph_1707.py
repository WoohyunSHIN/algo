from collections import defaultdict, deque
import sys
K = int(input())

def _dfs(visited_blue:list,visited_red:list,q:deque):
    ret = True

    while q:
        A, B = q.popleft()
        #print(f"A = {A}, B = {B}, visited_red = {visited_red} visited_blue = {visited_blue} visited_red[A] = {visited_red[A]} visited_blue[B] = {visited_blue[B]}")

        if visited_red[A] == 0 and visited_blue[A] == 0:
            visited_red[A] = 1

        if (visited_blue[A] == 1 and visited_blue[B] == 1) or (visited_red[A] == 1 and visited_red[B] == 1):
            ret = False
            return ret

        if visited_blue[A] == 1:
            visited_red[B] = 1

        if visited_red[A] == 1:
            visited_blue[B] = 1     

    return ret

def main(V:int,E:int,q:deque)->bool:
    ret = False

    visited_blue = [0] * (V+1)
    visited_red = [0] * (V+1)
    if _dfs(visited_blue,visited_red,q):
        ret = True
        return ret

    return ret

res = []
for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())
    q = deque()
    for _ in range(E):
        A_node, B_node = map(int,sys.stdin.readline().split())
        if A_node < B_node:
            q.append((A_node,B_node))
        else:
            q.append((B_node,A_node))

    q = deque(sorted(q))

    if main(V,E,q):
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)

"""
1
4 4
2 3
1 4
3 4
1 2
"""

"""
1
5 4
1 2
1 3
2 3
4 5
"""