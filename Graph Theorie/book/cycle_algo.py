def find_parent(parent:list,x:int)->int:
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

v, e = map(int,input().split())
parent = [0] * (v+1)
cycle = False

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b= map(int,input().split())

    # 핵심 코드
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생되었습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

"""
3 3
1 2
1 3
2 3
"""