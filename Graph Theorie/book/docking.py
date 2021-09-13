def find_parent(parent:list,x:int)->int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list,a:int,b:int)->None:
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1,g+1):
    parent[i] = i

cnt = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    cnt += 1
print(f"cnt : {cnt}")

"""
4
3
4
1
1
"""

"""
4
6
2
2
3
3
4
4
"""