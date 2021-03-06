def find_parent(parent:list,x:int)->int:
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent:list,a:int,b:int)->None:
    print(f"origin a = {a}, b = {b}")
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    print(f"after a = {a}, b = {b}")

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b = map(int,input().split())
    union_parent(parent,a,b)

print("각 원소가 속한 집합 ", end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end='')

print()

print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ')

"""
6 4
1 4
2 3
2 4
5 6
"""