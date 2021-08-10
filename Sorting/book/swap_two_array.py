n, k = map(int,input().split())

a = list(map(int,input().split()))    
b = list(map(int,input().split()))    

def main(n:int,k:int,a:list,b:list)->int:
    ret = 0
    a = sorted(a)
    print(a)

    b = sorted(b, reverse=True)
    print(b)

    for i in range(k):
        if a[i] > b[i]:
            break
        a[i], b[i] = b[i], a[i]

    return sum(a)

print(main(n,k,a,b))
"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
