n,m = 3,4
a = [1,3,5]
b = [2,4,6,8]

def main(n:int,m:int,a:list,b:list)->list:
    ret = [0] * (n+m)
    k = 0
    pointer_a = 0 
    pointer_b = 0

    while pointer_a < n or pointer_b < m:
        if pointer_b >= m or (pointer_a < n and a[pointer_a] <= b[pointer_b]):
            ret[k] = a[pointer_a] 
            pointer_a += 1
        else:
            ret[k] = b[pointer_b] 
            pointer_b += 1
        k += 1 
        print(ret)

    return ret

print(main(n,m,a,b))