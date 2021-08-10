# 못풀겠음... 
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

def main(N:int, T:list, P:list)->int:
    ret = 0
    dp = [0] * (N+1)
    for i in range(N-1, -1, -1):
        # i = 6,5,4,3,2,1,0
        time = T[i] + i
        print(time)
        if time <= N:
            dp[i] = max(P[i] + dp[time])
            
        #print(P[i])

    return ret

N = int(input())
T = []
P = []

for _ in range(N):
    t, p = map(int,input().split())
    T.append(t)
    P.append(p)
    
print(main(N,T,P))


