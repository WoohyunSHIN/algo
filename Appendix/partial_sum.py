n = 5
data = [10,20,30,40,50]

def main(n:int,data:list,s:int,e:int)->int:
    ret = 0 
    prefix_sum = [0] * (n+1)
    data = sorted(data)

    for i in range(1,len(data)+1):
        prefix_sum[i] = prefix_sum[i-1] + data[i-1]
    
    ret = prefix_sum[e] - prefix_sum[s-1]
    


    return ret

print(main(n,data,2,5))
