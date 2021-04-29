n = int(input())

def main(n:int)->int:
    schedules = []
    
    for _ in range(n):
        schedule = tuple(map(int, input().split()))
        schedules.append(schedule)

    # 1. 시작시간으로 오름 정렬
    schedules = sorted(schedules) 
 
    # 2. 끝나는 시간으로 오름 정렬 한번 더
    schedules = sorted(schedules, key=lambda x: x[1]) 
 
    ret = 1
    end_time = schedules[0][1]
    for i in range(1,n):
        if schedules[i][0] >= end_time:
            ret += 1
            end_time = schedules[i][1]
            
    return ret

print(main(n))