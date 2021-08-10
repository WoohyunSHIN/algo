from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
a = list(map(int,stdin.readline().split()))

def main(N:int,a:int)->int:
    ret = -1
    for data in a:
        if data == bisect_left(a,data):
            ret = data
            return ret
    
    return ret

print(main(N,a))

"""
5
-15 -6 1 3 7
"""

"""
7
-15 -4 2 8 9 13 15
"""

"""
7 
-15 -4 3 8 9 13 15
"""

