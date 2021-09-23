n = 5
m = 5
data = [1,2,3,2,5]

def main(n:int, m:int, data:list)->int: 
    ret = 0

    e = 0
    interval_sum = 0
    for start in range(n):
        # start = 0, 0 < 5 and 0 < 5 --> is=3,e=1 --> 3 <5 and 1 < 5 --> is=6,e=2 --> is=5
        # start = 1, 
        while interval_sum < m and e < n:
            interval_sum += data[e]
            e += 1
        if interval_sum == m:
            ret += 1
        interval_sum -= data[start]
        print(interval_sum) 
    

    return ret

main(n,m,data)
