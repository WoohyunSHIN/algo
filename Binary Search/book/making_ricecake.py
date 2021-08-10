from sys import stdin

N, M = map(int,stdin.readline().split())

array = list(map(int,stdin.readline().split()))

def main(M:int,array:list,start:int,end:int)->int:
    ret = 0

    while end >= start:
        print(f"start : {start}, end : {end}")
        mid = (start+end) // 2
        tmp_array = [i for i in array if i > mid]
        tmp_res = sum(tmp_array) - len(tmp_array) * mid
        
        if tmp_res == M:
            ret = mid
            break
        elif tmp_res > M:
            start = mid+1
            ret = max(ret,mid)
        elif tmp_res < M:
            end = mid-1

    return ret

print(main(M,array,0,max(array)))

"""
4 6
19 15 10 17
"""