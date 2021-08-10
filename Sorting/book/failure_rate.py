from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
stages = list(map(int,stdin.readline().split()))

def solution(N:int, stages:list)->list:
    answer = []
    stages = sorted(stages)
    rate_info = defaultdict(int)

    for stage in range(1,N+1):
        # 분모 = 리스트에서 stage 보다 크거나 같은 숫자의 갯수
        denominator = [i for i in stages if i >= stage]
        
        if len(denominator) == 0:
            rate_info[stage] = 0
            continue
        else:
            # 분자 = 리스트에서 stage의 숫자
            numerator = [i for i in denominator if i == stage]
            rate_info[stage] = len(numerator)/len(denominator)

    rate_info = sorted(rate_info.items(),key=lambda data: data[1],reverse=True)

    for data in rate_info:
        answer.append(data[0])

    return answer

print(solution(N,stages))

"""
5
2 1 2 6 2 4 3 3 
"""

"""
4
4 4 4 4 4
"""

"""
5
4 4 4 4 4
"""