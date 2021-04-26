n, m = map(int, input().split())
data = list(map(int, input().split()))

# example) 
# 5 3
# 1 3 2 3 2

def my_main(n:int, m:int, data:list)->int:
    ret = 0
    data = sorted(data)
    
    for idx in range(len(data)-1):
        criteria = data[idx]
        for compare in data[idx:]:
            if criteria < compare:
                ret += 1

    return ret

def main(n:int, m:int, data:list)->int:
    ret = 0

    array = [0] * 11

    for x in data:
        array[x] += 1

    # print(array)

    for i in range(1, m+1):
        # print(f'i : {i}, n : {n}, ret : {ret}')
        n = n - array[i]
        ret = ret + array[i] * n
    return ret

# print(my_main(n,m,data))
# print(main(n,m,data))