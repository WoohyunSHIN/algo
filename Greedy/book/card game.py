n, m = map(int, input().split())

# n = 행
# m = 열

# 1. 행에서 가장 낮은 수를 뽑고
# 2. 낮은 수 중에서 가장 높은 수를 뽑는 것.

def my_main(n:int, m:int)->int:
    from collections import defaultdict

    my_dict = defaultdict(int)
    for i in range(1,n+1):
        data = list(map(int, input().split()))    
        my_dict[i] = min(data)

    ret = max(my_dict.values())
    return ret

def main(n:int, m:int)->int:
    ret = 0
    for i in range(n):
        data = list(map(int,input().split()))
        min_value = min(data)

        ret = max(ret,min_value)
    return ret

print(my_main(n,m))
print(main(n,m))