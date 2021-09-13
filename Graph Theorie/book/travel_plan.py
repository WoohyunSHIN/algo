def find_parent(parent:list, x:int)->int:
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent:list, a:int, b:int)->None:
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main(n:int,m:int,parent:list,edges:list,route:list)->None:
    for edge in edges:
        a, b = edge
        union_parent(parent,a,b)

    start_root = parent[route[0]]

    flag = True
    for i in range(1,len(route)):
        if start_root != parent[i]:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")


n, m = map(int,input().split())
parent = [0] * (n+1)
edges = []

for i in range(1,n+1):
    parent[i] = i

for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(i,len(row)):
        if row[j] == 1:
            edges.append((i,j+1))
route = list(map(int,input().split()))

main(n,m,parent,edges,route)


"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""