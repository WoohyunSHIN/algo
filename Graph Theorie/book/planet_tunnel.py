def dist_cal(a:tuple, b:tuple)->int:
    ax, ay, az = a
    bx, by, bz = b
    return min(abs(ax-bx),abs(ay-by),abs(az-bz))

def find_parent(parent:list,x:int)->int:
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent:list,a:int,b:int)->None:
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

planet_pos = []
planet_dist = []
edges = []
parent = [0] * n
total_cost = 0

for i in range(n):
    parent[i] = i

for _ in range(n):
    x,y,z = map(int,input().split())
    planet_pos.append((x,y,z))

for i in range(len(planet_pos)):
    for j in range(i+1,len(planet_pos)):
        #print(f"i = {planet_pos[i]}, j = {planet_pos[j]} i = {i}, j = {j}")
        edges.append((dist_cal(planet_pos[i],planet_pos[j]),i,j))

for edge in sorted(edges):
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_cost += cost

print(total_cost)

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""
