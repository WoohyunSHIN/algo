n, k = map(int, input().split())

def main(n:int, k:int)->int:
    ret = 0
    coin_types = []
    
    for _ in range(n):
        coin_types.append(int(input()))

    coin_types = sorted(coin_types, reverse=True)

    for coin in coin_types:
        if k >= coin:
            ret += (k//coin)
            k %= coin 

    return ret

print(main(n,k))
