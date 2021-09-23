from bisect import bisect_left, bisect_right

def count_by_range(a:list,start:int,end:int)->int:
    ret = 0 
    start_idx = bisect_left(a,start)
    end_idx = bisect_right(a,end)

    ret = end_idx - start_idx
    return ret

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))