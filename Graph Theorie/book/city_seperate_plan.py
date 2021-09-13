def find_parent(parent:list, x:int)->int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list, a:int, b:int)->None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

result = 0
edges = []
last = 0
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

for edge in sorted(edges):
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result-last)


"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""