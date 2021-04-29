n = int(input())
dists = list(map(int,input().split()))
costs = list(map(int,input().split()))

def main(n:int, dists:list, costs:list)->int:
    ret = 0
    
    ret += dists[0]*costs[0]
    base_cost = costs[0]
    base_dist = 0

    for idx in range(1,n-1):
        if base_cost > costs[idx]:
            ret += base_dist*base_cost
            base_cost = costs[idx]
            base_dist = 0
        base_dist += dists[idx]
        if idx == n-2:
            ret += base_dist*base_cost

    return ret

print(main(n, dists, costs))
