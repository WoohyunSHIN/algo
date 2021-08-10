from sys import stdin

N = int(stdin.readline().rstrip())
offers = list(map(int,stdin.readline().split()))
offers = sorted(offers)
M = int(stdin.readline().rstrip())
demands = list(map(int,stdin.readline().split()))

def binary_search(offers:list,demand:int,start:int,end:int)->str:
    ret = ''
    if start > end:
        ret = 'no'
        return ret
    
    mid = (start+end) // 2
    
    if offers[mid] == demand:
        ret = 'yes'
        return ret
    elif offers[mid] > demand:
        return binary_search(offers,demand,start,mid-1)
    elif offers[mid] < demand:
        return binary_search(offers,demand,mid+1,end)

result = ''

for demand in demands:
    result += binary_search(offers,demand,0,N-1) + ' '

print(result.rstrip())


"""
5
8 3 7 9 2
3
5 7 9
"""