# 신장 트리 > 최소 신장 트리 알고리즘 > 크루스칼 알고리즘(Greedy)
# 신장 트리중에서 최소 비용으로 만들 수 있는 신장트리를 찾는 알고리즘을 최소 신장 트리 알고리즘이라고 하며 대표적인 최소 신장 트리 알고리즘이 크루스칼 알고리즘이다.
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

v, e = map(int,input().split())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

for edge in sorted(edges):
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)

"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""