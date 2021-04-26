n = int(input())


# example)
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

def main(n:int)->int:
    schedules = []
    
    for _ in range(n):
        schedule = tuple(map(int, input().split()))
        schedules.append(schedule)

    # 1. 시작시간으로 오름 정렬
    schedules = sorted(schedules) 
    print(schedules)
 
    # 2. 끝나는 시간으로 오름 정렬 한번 더
    schedules = sorted(schedules, key=lambda x: x[1]) 
    print(schedules)
 
    ret = 1
    end_time = schedules[0][1]
    for i in range(1,n):
        if schedules[i][0] >= end_time:
            ret += 1
            end_time = schedules[i][1]
            
    return ret

print(main(n))