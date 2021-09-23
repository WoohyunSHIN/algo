import heapq

def heapsort(data:list)->list:
    # 최소 heap
    ret = []
    h = []

    for v in data:
        heapq.heappush(h,v)

    print(f"h : {h}")

    for _ in range(len(h)):
        ret.append(heapq.heappop(h))

    return ret

def rev_heapsort(data:list)->list:
    # 최대 heap
    ret = []
    h = []

    for v in data: 
        heapq.heappush(h,-v)

    print(f"rev_h : {h}")

    for _ in range(len(h)):
        ret.append(-heapq.heappop(h))

    return ret


data = [1,3,5,7,9,2,4,6,8,0]

res = heapsort(data)
print(f"res : {res}")

rev_res = rev_heapsort(data)
print(f"rev_res : {rev_res}")