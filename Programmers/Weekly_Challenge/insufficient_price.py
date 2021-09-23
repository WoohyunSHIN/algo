from sys import stdin
"""
3
20
4
"""
price = int(stdin.readline().rstrip())
money = int(stdin.readline().rstrip())
count = int(stdin.readline().rstrip())

def solution(price:int, money:int, count:int)->int:
    answer = -1
    cnt_sum = sum(range(1,count+1))
    if money < price * cnt_sum:
        answer =  (price * cnt_sum) - money
    else:
        answer = 0   
    return answer

print(solution(price,money,count))