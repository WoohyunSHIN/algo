# from collections import deque
# n, k = map(int,input().split())

# def main(n:int,k:int)->int:
#     ret = 0
#     visited = set([])

#     queue = deque()
#     queue.append([n])

#     while queue:
#         x = queue.popleft()

#         sum_nx = 
#         minus_nx = 
#         multi_nx = 


#     return ret

# print(main(n,k))




from collections import deque
n, k = map(int,input().split())

def main(n:int,k:int)->int:
    ret = 0
    visited = set([])

    queue = deque()
    queue.append([n])

    cnt = 0

    while queue:
        tmp = []
        x = queue.popleft()
        visited = set(list(visited) + x)
        print(visited)

        if k in x:
            ret = cnt
            break

        tmp += list(map(lambda i:i+1,x))
        tmp += list(map(lambda i:i-1,x))
        tmp += list(map(lambda i:i*2,x))

        tmp = [x for x in tmp if (0 <= x and x <= 100000)] 
        tmp = list(set(tmp)-visited)

        queue.append(tmp)
        cnt += 1

    return ret

print(main(n,k))
