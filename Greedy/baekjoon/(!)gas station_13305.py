n = int(input())
dists = list(map(int,input().split()))
prices = list(map(int,input().split()))

# example )
# 5
# 3 2 1 4
# 5 8 9 4 1
# 46

# 4
# 2 3 1
# 5 2 4 1
# 18

# 4
# 3 3 4
# 1 1 1 1
# 10

def main(n:int, dists:list, prices:list)->int:
    ret = 0

    ret += dists[0]*prices[0]

    # for idx in range(len(prices)-2):
    #     print(f"Before : idx : {idx} ret : {ret}")
    #     if ret + prices[idx+1]*dists[idx+1] > prices[idx]*dists[idx] + prices[idx]*dists[idx+1]:
    #         ret += prices[idx]*dists[idx+1]
    #         prices[idx+1] = prices[idx]
    #     ret += prices[idx+1]*dists[idx+1]
    #     print(f"After : idx : {idx} ret : {ret}")
    #     print("---")

    # ret += dists[-1]*prices[-2] # cz  

    # for idx in range(len(n)-2,-1, -1):
    #     # idx : 2 -> 1 -> 0
    #     if prices[idx-1]*dists[idx-1]+ret > prices[idx-1]*dists[idx-1]+price[idx-1]*dists[idx]:
    #         ret = prices[idx-1]*dists[idx-1]+price[idx-1]*dists[idx]
    #     print(idx)
    acc = 0

    for idx in range(1,n-1):
        # idx : 0 -> 1 -> 2
        if prices[idx] > prices[idx+1] and idx != n-2:
            # ret += sum(dists[idx:idx+1])*prices[idx]
            ret += acc*prices[idx]
            print(f"idx : {idx} acc : {acc}, price : {prices[idx]}")
            acc = 0
        else:
            prices[idx+1] = prices[idx]
            acc += dists[idx]
        
        # base case
        if idx == n-2:
            ret += prices[idx-1]*acc

    return ret

print(main(n, dists, prices))
