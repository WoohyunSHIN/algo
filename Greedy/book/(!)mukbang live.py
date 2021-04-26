food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times:list, k:int)->int:
    """
    시간 초과
    """
    answer = 0
    zero_cnt = 0
    size = len(food_times)

    while True:
        #print(f"zero_cnt : {zero_cnt} k : {k}")

        zero_cnt = 0
        for food_time in food_times:
            if food_time == 0:
                zero_cnt += 1
        
        if k < size - zero_cnt: # 0 이 아닌 갯수보다 작을 경우
            #print(f"zero_cnt : {zero_cnt} k : {k} food_times : {food_times}")
            break

        food_times = list(map(lambda x: x-1 if x>0 else 0, food_times))

        k = k - (size - zero_cnt)
    
    for idx, value in enumerate(food_times):
        if k == 0 and value != 0:
            answer = idx+1
            break

        if value != 0:
            k -= 1

    return answer

def main(food_times:list, k:int)->int:
    import heapq
    """
    음식을 시간을 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을 이용하면 된다.
    우선순위 큐를 이용하여 구현할 수 있다.
    """
    answer = 0

    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    
    print(q)

    sum_value = 0
    previous = 0 
    length = len(food_times)
    #....

    

    return answer

# print(solution(food_times, k))
main(food_times, k)