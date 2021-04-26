n = int(input())
data = list(map(int, input().split()))


def main(n:int, data:list)->int:
    ret = 0
    data = sorted(data)

    for one_data in data:
        ret += one_data*n
        n -= 1

    return ret

print(main(n, data))