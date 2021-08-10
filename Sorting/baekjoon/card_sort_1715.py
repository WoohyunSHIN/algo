from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for _ in range(N):
    heapq.heappush(heap,int(stdin.readline()))

def main(N:int,heap:list)->int:
    ret = 0
    if len(heap)<=1:
        ret = 0
        return ret

    while len(heap)>1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        tmp = a+b
        ret += tmp
        heapq.heappush(heap,tmp)

    return ret
print(main(N,heap))