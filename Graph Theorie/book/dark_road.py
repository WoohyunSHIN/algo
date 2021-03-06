def find_parent(parent:list, x:int)->int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list,a:int,b:int)->None:
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)
edges = []
total = 0
min_cost = 0
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,cost = map(int, input().split())
    total += cost
    edges.append((cost,a,b))

for edge in sorted(edges):
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        min_cost += cost

print(total-min_cost)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""

