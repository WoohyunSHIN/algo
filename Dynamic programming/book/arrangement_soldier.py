"""
7
15 11 4 8 5 2 4
"""

def main(N:int, rev_arr:list)->int:
    ret = 0
    dp = [1] * N

    for i in range(1,N):
        for j in range(i):
            if rev_arr[i] > rev_arr[j]:
                dp[i] = max(dp[i],dp[j]+1)

    ret = N - max(dp)

    return ret

N = int(input())
arr = list(map(int, input().split()))

rev_arr = list(reversed(arr))

print(main(N,rev_arr))