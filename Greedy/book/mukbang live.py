food_times = list(map(int, input().split()))
k = int(input())

"""
정확성 : 100%
효율성 : 0%
"""

def _checker(data:list)->list:
    cnt = 0
    my_list = []
    for idx in range(len(data)):
        if data[idx] != 0:
            cnt += 1
            my_list.append(idx)
        
    ret = [cnt, my_list]

    return ret

def solution(food_times:list, k:int)->int:
    answer = 0
    infos = _checker(food_times)

    while True:
        if sum(food_times) <= 0:
            answer = -1
            break

        if infos[0] <= k:
            food_times = list(map(lambda x: x-1 if x>1 else 0,food_times))
            k -= infos[0]
            infos = _checker(food_times)
        else:
            answer = infos[1][k] + 1
            break

    return answer

print(solution(food_times, k))
