n = int(input())
lost = list(map(int,input().split()))
reserve = list(map(int,input().split()))

def solution(n:int, lost:list, reserve:list)->int:
    ret = 0
    check = [True]*(n+1)
    
    for lost_idx in lost:
        check[lost_idx] = False

    for res_idx in reserve:
        if res_idx == n:
            break
        if check[res_idx-1] == False:
            check[res_idx-1] = True
            continue
        elif check[res_idx+1] == False:
            check[res_idx+1] = True
            continue
    print(check)

    return ret - 1

print(solution(n,lost,reserve))