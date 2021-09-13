N, M = map(int,input().split())
money = []
#INF = 10001
INF = M + 1
d = [0] * INF

for _ in range(N):
    coin = int(input())
    money.append(coin)
    d[coin] = 1

"""
2 15 <- 2 = 갯수, 15 = 타겟
2 <- 2원
3 <- 3원
"""


def main(M:int)->int:
    print(f"M = {M}, d = {d}")
    if M < 0:
        return INF
    
    if d[M] != 0:
        return d[M]

    min_value = INF
    for coin in money:
        if main(M-coin) < min_value:
            min_value = main(M-coin)
        
    d[M] = min_value + 1
    #d[M] = min(main(M-2), main(M-3)) + 1
    #d[6] = min(main(0)+2, main(3)) + 1
    #d[4] = min(main(0)+1, INF) + 1
    #d[2] = min(main(0), INF) + 1
    #d[1] = INF
    return d[M]

if main(M) < INF:
    print(main(M))
else:
    print(-1)