from bisect import bisect_left, bisect_right
from sys import stdin

N, x = map(int,stdin.readline().split())
array = list(map(int,stdin.readline().split()))

def main(N:int,x:int,array:list)->int:
    ret = 0
    array = sorted(array)
    if bisect_right(array,x) == bisect_left(array,x):
        ret = -1
        return ret
    ret = bisect_right(array,x) - bisect_left(array,x)
    return ret

print(main(N,x,array))

"""
7 2
1 1 2 2 2 3
"""

"""
7 4
1 1 2 2 2 3
"""